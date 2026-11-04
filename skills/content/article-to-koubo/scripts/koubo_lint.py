#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""口播稿体检脚本（只用 Python 标准库）。

找出口播稿里"像 AI 写的""像在念课文""听众听不懂"的地方，
给出能逐条修改的命中项。它只负责可量化的部分；幽默是否好笑、
情绪是否自然，仍由人或模型按 SKILL.md 的五维自评判断。

用法：
  python3 koubo_lint.py 稿件.txt
  python3 koubo_lint.py 稿件.txt --target-seconds 120 --rate 4
  python3 koubo_lint.py 稿件.txt --terms "智能体,误差累积" --allow "老铁"
  cat 稿件.txt | python3 koubo_lint.py - --json

只传口播正文，不要把改稿说明一起传进来。
[[待补：...]] 形式的占位符不参与检查，只统计数量。

退出码：0 没有必须改的项；1 有必须改的项；2 读取或参数错误。
"""

import argparse
import json
import re
import sys

MUST = "必须改"
SHOULD = "建议改"
INFO = "提示"
LEVEL_ORDER = {MUST: 0, SHOULD: 1, INFO: 2}

PLACEHOLDER_RE = re.compile(r"\[\[.*?\]\]")
CJK_RE = re.compile(r"[一-鿿]")
LATIN_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9.+#'-]*")
DIGIT_RE = re.compile(r"\d")
PAUSE_SPLIT_RE = re.compile(r"[，,。！？!?；;：:、…—~～\s]+")
CLAUSE_SPLIT_RE = re.compile(r"[，,、；;]")
SENTENCE_END_RE = re.compile(r"(?<=[。！？!?…])")

# ---------------------------------------------------------------------------
# 词表
# 每组：(类别, 级别, 修改建议, 词语列表, 是否按词聚合报告)
# 必须改 = 日常说话里几乎不会出现、一出现就像 AI 或像念稿的说法。
# 建议改 = 偶尔可以，多了就有味道，需要逐条判断。
# ---------------------------------------------------------------------------
PHRASE_GROUPS = [
    (
        "开场套话", MUST,
        "删掉，直接从一个具体画面、一个反常识的事实或一个真问题开始",
        ["在当今", "当今社会", "众所周知", "让我们一起", "让我们来", "接下来让我们",
         "下面让我们", "你是否曾经", "你是否也曾", "在这个快节奏的", "在这个信息爆炸的"],
        False,
    ),
    (
        "过渡套话", MUST,
        "删掉这句引子，直接说事；需要转场就用口头路标，比如'还有个事儿''再说回来'",
        ["值得注意的是", "值得一提的是", "值得关注的是", "值得我们注意的是", "值得我们思考的是",
         "需要注意的是", "需要指出的是", "不可否认", "毋庸置疑", "显而易见", "由此可见",
         "不难发现", "不难看出", "我们可以看到", "综上所述", "与此同时", "此外", "基于此",
         "鉴于此", "换言之", "总而言之", "总的来说", "简而言之", "这告诉我们"],
        False,
    ),
    (
        "拔高套话", MUST,
        "别替听众总结意义，说清楚具体会发生什么、跟他有什么关系",
        ["具有重要意义", "意义深远", "深远影响", "里程碑", "划时代", "新篇章", "新纪元",
         "革命性", "颠覆性", "不可或缺", "至关重要", "举足轻重", "彰显", "助力",
         "注入新的活力", "注入了新的活力", "无限可能", "未来可期", "拭目以待",
         "奠定了坚实的基础", "深度融合", "全方位", "多维度", "深入探讨", "深度解析",
         "全面解析", "致力于", "旨在", "无缝", "这不仅仅是", "这不仅是"],
        False,
    ),
    (
        "客服腔", MUST,
        "删掉；口播不是客服回复",
        ["好问题", "希望对你有所帮助", "希望对你有帮助", "希望对大家有所帮助",
         "希望对大家有帮助", "希望这期内容对你有", "内容对你有帮助", "如果你有任何问题",
         "感谢您的"],
        False,
    ),
    (
        "假情绪", MUST,
        "别用形容词喊，换成有来由的具体反应，比如'我看到这个数愣了一下'",
        ["震撼", "炸裂", "令人惊叹", "叹为观止", "颠覆认知", "史诗级", "王炸", "封神",
         "杀疯了", "重磅", "惊呆了", "太绝了"],
        False,
    ),
    (
        "网络烂梗", MUST,
        "换成自己的话；人设卡里本来就有的口头禅可以用 --allow 放行",
        ["家人们", "宝子们", "宝子", "绝绝子", "yyds", "集美", "芭比Q", "栓Q", "泰裤辣",
         "尊嘟假嘟", "格局打开", "主打一个", "听君一席话"],
        False,
    ),
    (
        "视觉指代", MUST,
        "听众看不到图、表和上下文，改成口头描述",
        ["如下图", "如图所示", "下图", "上图", "见下表", "如下表", "如下所示", "上述",
         "下述", "前文", "后文", "本文", "笔者", "如前所述", "详见"],
        False,
    ),
    (
        "限定词堆叠", MUST,
        "留一个就够，或者干脆说清楚到底确定不确定",
        ["在一定程度上", "也许可能", "可能也许", "或许可能", "大概可能"],
        False,
    ),
    (
        "模板开场收尾", SHOULD,
        "太常见了，听众耳朵会自动跳过；换成这条视频独有的开头或结尾",
        ["今天我们来聊聊", "今天我们来聊一聊", "今天给大家分享", "今天和大家分享",
         "今天跟大家分享", "话不多说", "废话不多说", "那么问题来了", "点赞关注不迷路",
         "欢迎在评论区留言", "欢迎点赞关注", "你怎么看？欢迎", "某种程度上"],
        False,
    ),
    (
        "假情绪", SHOULD,
        "偶尔可以，多了像营销号；确认前面有事实撑着",
        ["震惊", "不得不说", "细思极恐", "天花板", "遥遥领先", "破防", "拿捏", "狠狠", "谁懂啊"],
        True,
    ),
    (
        "书面词", SHOULD,
        "换成说话时会用的词",
        ["然而", "因此", "并且", "以及", "是否", "如何", "为何", "何时", "从而", "进而",
         "极其", "十分", "诸多", "众多", "倘若", "若是", "予以", "加以", "即可", "均为",
         "尚未", "无法", "能够", "具备", "拥有", "显著", "迅速", "逐渐", "仍然", "依然",
         "存在着"],
        True,
    ),
    (
        "书面成语", SHOULD,
        "像作文里的词，换成大白话，比如'层出不穷'说'一个接一个冒出来'",
        ["层出不穷", "日新月异", "方兴未艾", "如火如荼", "应运而生", "不胜枚举", "屡见不鲜",
         "与日俱增", "首当其冲", "不言而喻", "不容忽视", "息息相关", "密不可分", "相辅相成"],
        True,
    ),
    (
        "黑话术语", SHOULD,
        "确认听众懂；不懂就换成大白话，或者先讲它干什么再给名字（见 jargon-translation.md）",
        ["赋能", "抓手", "闭环", "底层逻辑", "顶层设计", "颗粒度", "心智", "全链路", "链路",
         "范式", "飞轮", "拉通", "对齐", "沉淀", "打法", "组合拳", "赛道", "生态位", "矩阵",
         "私域", "公域", "势能", "方法论", "降本增效", "提质增效", "降维打击", "护城河",
         "第一性原理", "中台", "触点", "场景化", "数字化转型", "认知升级", "价值主张",
         "解决方案", "一站式", "维度", "层面", "体系化", "结构化", "系统性", "落地"],
        True,
    ),
    (
        "AI 高频词", SHOULD,
        "这些词本身没错，但 AI 特别爱用；换成更具体的动词或干脆删掉",
        ["打造", "构建", "聚焦", "精准", "契机", "愿景", "格局", "范畴", "视角", "涵盖",
         "诸如", "不仅仅是", "真正意义上", "本质上", "从某种意义上", "高质量", "深入",
         "核心", "一系列"],
        True,
    ),
    (
        "空洞恐吓", SHOULD,
        "紧迫感要有事实撑着：说清楚具体会失去什么、依据是原文哪一句；没有依据的恐吓删掉",
        ["被淘汰", "淘汰你", "再不学", "就晚了", "来不及了", "最后的机会", "最后一次机会",
         "最后一波红利", "唯一出路", "唯一的出路", "被时代抛弃", "被AI取代", "被 AI 取代",
         "取代你", "错过这一波", "错过这个时代"],
        True,
    ),
]

BOOKISH_SUGGESTIONS = {
    "然而": "不过／但是", "因此": "所以", "并且": "而且／还", "以及": "还有／和",
    "是否": "是不是／有没有", "如何": "怎么", "为何": "为什么", "何时": "什么时候",
    "从而": "这样就", "进而": "然后", "极其": "特别", "十分": "特别／挺",
    "诸多": "好多", "众多": "一大堆", "倘若": "要是", "若是": "要是", "予以": "给",
    "加以": "直接用动词", "即可": "就行", "均为": "都是", "尚未": "还没",
    "无法": "没法", "能够": "能", "具备": "有", "拥有": "有", "显著": "明显",
    "迅速": "很快", "逐渐": "慢慢", "仍然": "还是", "依然": "还是", "存在着": "有",
}

# 假口语：真人会说，但密集出现就是另一种 AI 味
FILLER_WORDS = ["说白了", "其实", "说实话", "讲真", "坦白讲", "老实说", "你发现没",
                "对吧", "对不对", "简单来说", "简单说", "换句话说", "说到底", "你懂的", "真的"]

# 结构模式：(类别, 级别, 正则, 修改建议)
STRUCTURE_PATTERNS = [
    ("不是…而是", SHOULD, re.compile(r"不是[^。！？!?\n]{1,24}?而是"),
     "直接说结论；真要对比，口语里说'不是A，是B'就够了，全稿最多一次"),
    ("不仅…更", SHOULD, re.compile(r"不仅(仅)?[^。！？!?\n]{1,24}?(更|还|也|而且)"),
     "书面递进句，拆成两句平着说"),
    ("一方面…另一方面", SHOULD, re.compile(r"一方面[\s\S]{1,120}?另一方面"),
     "口播里听众记不住两个'方面'，挑一个重要的说透"),
    ("随着…发展", MUST,
     re.compile(r"随着[^，。！？!?\n]{1,20}?(不断|快速|飞速|迅速|日益|持续)?(发展|普及|进步|到来|兴起|演进)"),
     "空背景开场，删掉，直接说事"),
    ("在…的今天", MUST, re.compile(r"在[^，。！？!?\n]{1,16}?的今天"),
     "空背景开场，删掉，直接说事"),
    ("在…背景下", MUST,
     re.compile(r"在[^，。！？!?\n]{0,12}?(背景下|浪潮中|大潮中|大背景下|新形势下)"),
     "空背景，删掉"),
    ("在…时代", SHOULD, re.compile(r"在[^，。！？!?\n]{1,12}?时代"),
     "如果只是铺背景就删掉；真在讲某个年代可以保留"),
    ("答案是：", SHOULD, re.compile(r"(答案|原因|结论|秘诀|关键)(就是|是|很简单)?[：:]"),
     "揭晓式冒号像 PPT，直接说出来"),
    ("再不…就…", SHOULD, re.compile(r"再不[^。！？!?\n]{1,16}?就(晚了|来不及|被|没机会|完了)"),
     "空洞恐吓句式；紧迫感要有原文事实撑着，说清楚具体会失去什么"),
]

# ---------------------------------------------------------------------------
# 风格卡：references/style-cards/*.md 里的第一个 ```json 代码块，必须含 "koubo_style" 键。
# targets 里只能用下面这些可计算的指标，值是 [下限, 上限]。
# ---------------------------------------------------------------------------
STYLE_METRICS = {
    "平均句长": "字",
    "短句占比": "%",
    "语气词每百字": "个",
    "问句每百字": "个",
    "感叹号每百字": "个",
    "你占称呼比": "%",
}
STYLE_JSON_RE = re.compile(r"```json\s*\n(.*?)```", re.S)


def load_style_card(path):
    """读取风格卡，返回 dict。格式不对时抛 ValueError，信息是中文。"""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for block in STYLE_JSON_RE.findall(text):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        if isinstance(data, dict) and "koubo_style" in data:
            break
    else:
        raise ValueError("风格卡里没有找到含 koubo_style 键的 json 代码块：%s" % path)

    targets = data.get("targets", {})
    if not isinstance(targets, dict):
        raise ValueError("风格卡 targets 必须是对象")
    for metric, bounds in targets.items():
        if metric not in STYLE_METRICS:
            raise ValueError("风格卡里有不支持的指标：%s（支持：%s）" % (metric, "、".join(STYLE_METRICS)))
        if (not isinstance(bounds, list) or len(bounds) != 2
                or not all(isinstance(b, (int, float)) for b in bounds) or bounds[0] > bounds[1]):
            raise ValueError("风格卡指标 %s 的区间必须是 [下限, 上限]" % metric)
    allow = data.get("allow", [])
    if not isinstance(allow, list) or not all(isinstance(w, str) for w in allow):
        raise ValueError("风格卡 allow 必须是字符串列表")
    for key in ("rate", "soft_breath", "hard_breath"):
        if key in data and not isinstance(data[key], (int, float)):
            raise ValueError("风格卡 %s 必须是数字" % key)
    data.setdefault("name", data["koubo_style"])
    return data


def compare_style(stats, style, issues):
    """把稿子的统计值和风格卡区间逐项对比，返回对比结果列表。"""
    rows = []
    for metric, (low, high) in style.get("targets", {}).items():
        value = stats.get(metric)
        if value is None:
            continue
        ok = low <= value <= high
        rows.append({"指标": metric, "数值": value, "区间": [low, high], "在区间内": ok})
        if not ok:
            unit = STYLE_METRICS[metric]
            direction = "偏低" if value < low else "偏高"
            issues.append(make_issue(SHOULD, "风格偏离", None,
                                     "%s %s%s，%s" % (metric, value, unit, direction), "",
                                     "%s的区间是 %s–%s%s；对照风格卡调整" % (style["name"], low, high, unit)))
    return rows

PARTICLE_RE = re.compile(r"[吧呢嘛啊呀哈呗啦嘞哦噢]")
COMMON_LATIN = {"ai", "app", "ok", "iphone", "ppt", "wifi", "wi-fi", "bug"}
NUMBER_HARD_RE = re.compile(r"\d+(\.\d+)?\s?[%％]|\d+\.\d+|\d{5,}|\d{4}年|\d+[:：]\d+")
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕]")


def speech_units(text):
    """估算朗读长度：汉字算 1，英文单词算 2，数字每位算 1。"""
    return (len(CJK_RE.findall(text))
            + 2 * len(LATIN_WORD_RE.findall(text))
            + len(DIGIT_RE.findall(text)))


def context_of(line, start, end, width=10):
    left = max(0, start - width)
    right = min(len(line), end + width)
    prefix = "…" if left > 0 else ""
    suffix = "…" if right < len(line) else ""
    return prefix + line[left:right].strip() + suffix


def make_issue(level, category, line_no, match, context, suggestion, **extra):
    issue = {
        "level": level,
        "category": category,
        "line": line_no,
        "match": match,
        "context": context,
        "suggestion": suggestion,
    }
    issue.update(extra)
    return issue


def check_written_marks(lines, issues):
    patterns = [
        (re.compile(r"^\s*#{1,6}\s"), "Markdown 标题", "口播稿不要标题，删掉或改成一句口头路标"),
        (re.compile(r"^\s*([-*+•]|\d+[.、)）])\s*"), "列表符号", "听众看不到列表，改成'先说第一个……还有一个……'这种说法"),
        (re.compile(r"\*\*|__|`"), "Markdown 强调", "删掉；要强调就靠语气和重复"),
        (re.compile(r"[()（）]"), "括号", "括号里的话没法念：要么删，要么单独说一句"),
        (re.compile(r"——|—|--"), "破折号", "破折号念不出来，改成逗号或拆成两句"),
        (re.compile(r"[【】「」『』]"), "方括号或直角引号", "删掉；要引用就说'他原话是'"),
        (EMOJI_RE, "表情符号", "删掉"),
    ]
    for line_no, line in lines:
        for regex, name, suggestion in patterns:
            for m in regex.finditer(line):
                issues.append(make_issue(MUST, "书面符号", line_no, name,
                                         context_of(line, m.start(), m.end()), suggestion))
                break  # 同一行同一种符号只报一次
        if re.search(r"[一-鿿]/|/[一-鿿]", line):
            issues.append(make_issue(SHOULD, "书面符号", line_no, "斜杠", line.strip()[:30],
                                     "斜杠念不出来，改成'或者'或者挑一个"))
        if "；" in line or ";" in line:
            issues.append(make_issue(SHOULD, "书面符号", line_no, "分号", line.strip()[:30],
                                     "分号是书面标点，口播里改成句号"))


def check_phrases(lines, issues, allow):
    entries = []
    for category, level, suggestion, words, aggregate in PHRASE_GROUPS:
        for word in words:
            if word.lower() in allow:
                continue
            entries.append((word, category, level, suggestion, aggregate))
    entries.sort(key=lambda e: len(e[0]), reverse=True)

    aggregated = {}
    for line_no, line in lines:
        lowered = line.lower()
        taken = []
        for word, category, level, suggestion, aggregate in entries:
            start = 0
            needle = word.lower()
            while True:
                idx = lowered.find(needle, start)
                if idx < 0:
                    break
                end = idx + len(needle)
                start = end
                if any(idx < t_end and end > t_start for t_start, t_end in taken):
                    continue
                taken.append((idx, end))
                if aggregate:
                    key = (category, level, word)
                    slot = aggregated.setdefault(key, {"lines": [], "context": context_of(line, idx, end),
                                                       "suggestion": suggestion})
                    slot["lines"].append(line_no)
                else:
                    issues.append(make_issue(level, category, line_no, word,
                                             context_of(line, idx, end), suggestion))

    for (category, level, word), slot in aggregated.items():
        suggestion = slot["suggestion"]
        if category == "书面词" and word in BOOKISH_SUGGESTIONS:
            suggestion = "换成：" + BOOKISH_SUGGESTIONS[word]
        issues.append(make_issue(level, category, slot["lines"][0], word, slot["context"], suggestion,
                                 count=len(slot["lines"]), lines=sorted(set(slot["lines"]))))


def check_structures(full_text, line_starts, issues):
    def line_of(pos):
        number = 1
        for i, start in enumerate(line_starts):
            if start <= pos:
                number = i + 1
            else:
                break
        return number

    for category, level, regex, suggestion in STRUCTURE_PATTERNS:
        for m in regex.finditer(full_text):
            snippet = m.group(0).replace("\n", " ")
            if len(snippet) > 40:
                snippet = snippet[:40] + "…"
            issues.append(make_issue(level, "结构套路", line_of(m.start()), category, snippet, suggestion))

    if "首先" in full_text and ("其次" in full_text or "再次" in full_text):
        issues.append(make_issue(SHOULD, "结构套路", line_of(full_text.index("首先")), "首先…其次",
                                 "首先／其次／最后", "教科书式排序，改成'先说一个……还有个事儿……'"
                                 "，或者干脆只讲两点"))


def check_fillers(full_text, total_units, issues, allow):
    per_word_cap = max(1, total_units // 300)
    total_cap = max(2, total_units // 150)
    total = 0
    over = []
    for word in FILLER_WORDS:
        if word in allow:
            continue
        count = full_text.count(word)
        total += count
        if count > per_word_cap:
            over.append("%s×%d" % (word, count))
    if over:
        issues.append(make_issue(SHOULD, "假口语", None, "、".join(over), "",
                                 "这些词真人会说，但每个大约 300 字最多 1 次；多了是硬凹口语"))
    if total > total_cap:
        issues.append(make_issue(SHOULD, "假口语", None, "口语填充词共 %d 个" % total, "",
                                 "全稿上限约 %d 个，删掉一半，靠句子本身的节奏说话" % total_cap))


def split_sentences(lines):
    sentences = []
    for line_no, line in lines:
        for piece in SENTENCE_END_RE.split(line):
            if speech_units(piece) > 0:
                sentences.append((line_no, piece.strip()))
    return sentences


def check_breath(lines, issues, soft, hard):
    for line_no, line in lines:
        for seg in PAUSE_SPLIT_RE.split(line):
            units = speech_units(seg)
            if units > hard:
                issues.append(make_issue(MUST, "气口", line_no, "%d 字不停顿" % units, seg[:40],
                                         "一口气说不完，拆成两三截"))
            elif units > soft:
                issues.append(make_issue(SHOULD, "气口", line_no, "%d 字不停顿" % units, seg[:40],
                                         "偏长，念出来试试，喘不过气就拆"))


def check_rhythm(sentences, issues):
    lengths = [speech_units(s) for _, s in sentences]
    i = 0
    while i + 2 < len(lengths):
        window = lengths[i:i + 3]
        if min(window) >= 12 and max(window) - min(window) <= 3:
            issues.append(make_issue(SHOULD, "节奏", sentences[i][0], "连续 3 句一样长（%s 字）" % "/".join(map(str, window)),
                                     sentences[i][1][:30], "插一个短句，或者把其中一句拆开、合并"))
            i += 3
        else:
            i += 1

    for i in range(len(sentences) - 2):
        heads = [s[:2] for _, s in sentences[i:i + 3]]
        if CJK_RE.match(heads[0] or "") and heads[0] == heads[1] == heads[2]:
            issues.append(make_issue(SHOULD, "节奏", sentences[i][0], "连续 3 句都以「%s」开头" % heads[0],
                                     sentences[i][1][:30], "排比味太重，换一种说法开头"))

    if lengths:
        short_ratio = sum(1 for n in lengths if n < 10) / len(lengths)
        avg = sum(lengths) / len(lengths)
        if avg > 35:
            issues.append(make_issue(SHOULD, "节奏", None, "平均句长 %.0f 字" % avg, "",
                                     "句子整体太长，像在念文章"))
        if len(lengths) >= 6 and short_ratio < 0.15:
            issues.append(make_issue(INFO, "节奏", None, "短句只占 %.0f%%" % (short_ratio * 100), "",
                                     "太工整了，加几个十个字以内的短句，比如'对，就这么简单。'"))
        return short_ratio, avg
    return 0.0, 0.0


def check_grammar(lines, issues):
    de_exempt = ("的确", "目的", "的话", "真的", "的士", "似的")
    for line_no, line in lines:
        for clause in PAUSE_SPLIT_RE.split(line):
            count = clause.count("的") - sum(clause.count(w) for w in de_exempt)
            if count >= 3:
                issues.append(make_issue(SHOULD, "书面句式", line_no, "一口气 %d 个'的'" % count, clause[:40],
                                         "长定语，拆成两句：先说是什么，再补它的特点"))
        for m in re.finditer(r"进行(了)?(?![中时])[一-鿿]", line):
            issues.append(make_issue(SHOULD, "书面句式", line_no, "进行＋动词", context_of(line, m.start(), m.end() + 2),
                                     "删掉'进行'，直接用动词：进行讨论→聊，进行测试→试一下"))
        for sentence in SENTENCE_END_RE.split(line):
            if sentence.count("被") >= 2:
                issues.append(make_issue(SHOULD, "书面句式", line_no, "被字句堆叠", sentence.strip()[:40],
                                         "改成主动句，说清楚是谁干的"))
        for sentence in SENTENCE_END_RE.split(line):
            for part in re.split(r"[，,；;：:]", sentence):
                if part.count("、") >= 2:
                    issues.append(make_issue(SHOULD, "书面句式", line_no, "三项以上并列", part.strip()[:40],
                                             "耳朵记不住一串并列，留两个最重要的，或者拆开一个一个说"))
        clauses = [c.strip() for c in CLAUSE_SPLIT_RE.split(line)]
        run = 0
        for c in clauses:
            if len(c) == 4 and len(CJK_RE.findall(c)) == 4:
                run += 1
                if run == 3:
                    issues.append(make_issue(SHOULD, "书面句式", line_no, "四字词连排", line.strip()[:40],
                                             "像在念标语，留一个，其余换成大白话"))
            else:
                run = 0


def check_audience(full_text, total_units, issues, stats):
    you = full_text.count("你")
    we = full_text.count("我们")
    me = full_text.count("我") - we
    crowd = sum(full_text.count(w) for w in ("大家", "各位", "朋友们", "观众"))
    questions = len(re.findall(r"[？?]", full_text))
    particles = len(PARTICLE_RE.findall(full_text))
    exclaims = len(re.findall(r"[！!]", full_text))
    per100 = particles * 100.0 / total_units if total_units else 0.0

    address_total = you + me + we
    stats.update({"你": you, "我": me, "我们": we, "大家类称呼": crowd, "问句": questions,
                  "语气词": particles, "语气词每百字": round(per100, 1), "感叹号": exclaims,
                  "问句每百字": round(questions * 100.0 / total_units, 1) if total_units else 0.0,
                  "感叹号每百字": round(exclaims * 100.0 / total_units, 1) if total_units else 0.0,
                  "你占称呼比": round(you * 100.0 / address_total) if address_total else 0})

    if total_units > 80 and you == 0:
        issues.append(make_issue(SHOULD, "对象感", None, "全稿没有一个'你'", "",
                                 "没在跟听众说话，至少让听众出现在几句话里"))
    if we >= 3 and we > you:
        issues.append(make_issue(SHOULD, "对象感", None, "'我们' %d 次 > '你' %d 次" % (we, you), "",
                                 "少说'我们'，多说'你'和'我'"))
    if crowd >= 3 and crowd > you:
        issues.append(make_issue(SHOULD, "对象感", None, "'大家／各位' %d 次" % crowd, "",
                                 "像站在台上讲话，换成对着一个人说"))
    if total_units > 100 and particles == 0:
        issues.append(make_issue(SHOULD, "活人信号", None, "一个语气词都没有", "",
                                 "吧、呢、嘛、啊、哈这类词一个没有，听着像念稿；挑两三处自然地加上"))
    elif per100 > 6:
        issues.append(make_issue(SHOULD, "活人信号", None, "语气词每百字 %.1f 个" % per100, "",
                                 "太密了，像硬凹，砍掉一半"))
    elif total_units > 100 and per100 < 1:
        issues.append(make_issue(INFO, "活人信号", None, "语气词每百字 %.1f 个" % per100, "",
                                 "偏少，通常每百字 1–4 个；在自然停顿处补一两个，别硬塞"))
    if re.search(r"[！!]{2,}", full_text):
        issues.append(make_issue(MUST, "假情绪", None, "连续感叹号", "", "只留一个，或者换成句号"))
    exclaim_cap = max(1, total_units // 150)
    if exclaims > exclaim_cap:
        issues.append(make_issue(SHOULD, "假情绪", None, "感叹号 %d 个" % exclaims, "",
                                 "约每 150 字最多 1 个；情绪靠内容，不靠标点"))
    if total_units > 150 and questions == 0:
        issues.append(make_issue(INFO, "活人信号", None, "全稿没有问句", "",
                                 "可以试着用一个真问题把听众拉进来"))


def check_terms_and_numbers(lines, full_text, issues, terms, delivery):
    latin_words = {}
    for line_no, line in lines:
        for m in LATIN_WORD_RE.finditer(line):
            latin_words.setdefault(m.group(0), line_no)
    uncommon = [w for w in latin_words if w.lower() not in COMMON_LATIN]
    if uncommon:
        level = SHOULD if len(uncommon) >= 4 else INFO
        issues.append(make_issue(level, "术语", latin_words[uncommon[0]], "英文词：" + "、".join(uncommon[:8]), "",
                                 "确认读法、确认听众懂；能用中文说就用中文，英文太多听众会走神"))

    for term in terms:
        count = full_text.count(term)
        if count:
            first_line = next((n for n, l in lines if term in l), None)
            issues.append(make_issue(SHOULD, "术语", first_line, "%s ×%d" % (term, count), "",
                                     "确认第一次出现时先讲它干什么再给名字，之后别反复用；听众用不上就删"))

    level = SHOULD if delivery == "tts" else INFO
    for line_no, line in lines:
        for m in NUMBER_HARD_RE.finditer(line):
            suggestion = ("配音模式：改成汉字读法，比如 62% 写成'百分之六十二'或'六成出头'"
                          if delivery == "tts" else "确认读法；口播里数字越少越圆越好，比如 62% 说'六成出头'")
            issues.append(make_issue(level, "数字", line_no, m.group(0), context_of(line, m.start(), m.end()), suggestion))
        if delivery == "tts" and re.search(r"[嗯呃]", line):
            issues.append(make_issue(SHOULD, "配音", line_no, "嗯／呃", line.strip()[:30],
                                     "配音引擎念这类词很怪，删掉"))


def lint(text, rate=None, target_seconds=None, terms=(), allow=(), delivery="human",
         soft_breath=None, hard_breath=None, style=None):
    """style 是 load_style_card() 的返回值。显式传入的 rate／气口参数优先于风格卡。"""
    style = style or {}
    rate = rate if rate is not None else style.get("rate", 4.0)
    soft_breath = soft_breath if soft_breath is not None else style.get("soft_breath", 22)
    hard_breath = hard_breath if hard_breath is not None else style.get("hard_breath", 32)
    allow = {w.strip().lower() for w in list(allow) + list(style.get("allow", [])) if w.strip()}
    raw_lines = text.splitlines()
    placeholders = sum(len(PLACEHOLDER_RE.findall(l)) for l in raw_lines)
    cleaned = [PLACEHOLDER_RE.sub("", l) for l in raw_lines]
    lines = [(i + 1, l) for i, l in enumerate(cleaned) if l.strip()]

    full_text = "\n".join(cleaned)
    line_starts = []
    pos = 0
    for l in cleaned:
        line_starts.append(pos)
        pos += len(l) + 1

    total_units = sum(speech_units(l) for _, l in lines)
    seconds = total_units / rate if rate > 0 else 0.0
    issues = []
    stats = {
        "字数估算": total_units,
        "语速": rate,
        "时长秒": round(seconds),
        "待补占位": placeholders,
    }

    check_written_marks(lines, issues)
    check_phrases(lines, issues, allow)
    check_structures(full_text, line_starts, issues)
    check_fillers(full_text, total_units, issues, allow)
    check_breath(lines, issues, soft_breath, hard_breath)
    sentences = split_sentences(lines)
    short_ratio, avg = check_rhythm(sentences, issues)
    stats["句子数"] = len(sentences)
    stats["短句占比"] = round(short_ratio * 100)
    stats["平均句长"] = round(avg, 1)
    check_grammar(lines, issues)
    check_audience(full_text, total_units, issues, stats)
    check_terms_and_numbers(lines, full_text, issues, [t for t in terms if t], delivery)

    if target_seconds:
        stats["目标秒"] = target_seconds
        deviation = (seconds - target_seconds) / float(target_seconds)
        if abs(deviation) > 0.15:
            direction = "超出" if deviation > 0 else "不足"
            target_units = int(target_seconds * rate)
            issues.append(make_issue(SHOULD, "时长", None,
                                     "%s目标 %.0f%%" % (direction, abs(deviation) * 100), "",
                                     "目标约 %d 字（%d 秒 × %.1f 字/秒），现在约 %d 字" %
                                     (target_units, target_seconds, rate, total_units)))
    if placeholders:
        issues.append(make_issue(INFO, "待补", None, "%d 处 [[待补]]" % placeholders, "",
                                 "录之前换成你自己的经历或确认过的信息"))

    result = {"stats": stats}
    if style:
        result["style"] = {"name": style["name"], "rows": compare_style(stats, style, issues)}

    issues.sort(key=lambda x: (LEVEL_ORDER[x["level"]], x["line"] if x["line"] is not None else 10 ** 6))
    result["summary"] = {level: sum(1 for x in issues if x["level"] == level) for level in (MUST, SHOULD, INFO)}
    result["issues"] = issues
    return result


def format_report(result):
    stats = result["stats"]
    summary = result["summary"]
    seconds = stats["时长秒"]
    out = []
    out.append("口播体检报告")
    out.append("=" * 24)
    duration = "约 %d 字，按 %.1f 字/秒约 %d 秒（%d 分 %02d 秒）" % (
        stats["字数估算"], stats["语速"], seconds, seconds // 60, seconds % 60)
    if "目标秒" in stats:
        duration += "，目标 %d 秒" % stats["目标秒"]
    out.append(duration)
    out.append("必须改 %d ｜ 建议改 %d ｜ 提示 %d" % (summary[MUST], summary[SHOULD], summary[INFO]))
    out.append("活人信号：问句 %d ｜ 语气词 %.1f/百字 ｜ 短句占比 %d%% ｜ 平均句长 %.1f ｜ 你 %d ／ 我 %d ／ 我们 %d" % (
        stats.get("问句", 0), stats.get("语气词每百字", 0), stats.get("短句占比", 0), stats.get("平均句长", 0),
        stats.get("你", 0), stats.get("我", 0), stats.get("我们", 0)))

    if result.get("style"):
        rows = result["style"]["rows"]
        hit = sum(1 for r in rows if r["在区间内"])
        out.append("")
        out.append("【像不像：%s】%d/%d 项在区间内" % (result["style"]["name"], hit, len(rows)))
        for r in rows:
            unit = STYLE_METRICS[r["指标"]]
            mark = "在区间内" if r["在区间内"] else "偏离"
            out.append("  %s %s%s（区间 %s–%s%s）%s" % (r["指标"], r["数值"], unit, r["区间"][0], r["区间"][1], unit, mark))

    for level in (MUST, SHOULD, INFO):
        items = [x for x in result["issues"] if x["level"] == level]
        if not items:
            continue
        out.append("")
        out.append("【%s】" % level)
        for x in items:
            where = "L%-3d" % x["line"] if x["line"] is not None else "全稿"
            match = x["match"]
            if x.get("count", 1) > 1:
                match += " ×%d（%s）" % (x["count"], ",".join("L%d" % n for n in x["lines"]))
            line = "%s %s｜%s" % (where, x["category"], match)
            if x["context"]:
                line += "｜%s" % x["context"]
            out.append(line)
            out.append("      → %s" % x["suggestion"])

    if summary[MUST] == 0:
        out.append("")
        out.append("没有必须改的项。建议改的项逐条判断，别为了清零硬改。")
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description="口播稿体检：找出像 AI、像念稿、听不懂的地方")
    parser.add_argument("path", help="口播正文文件路径；用 - 表示从标准输入读取")
    parser.add_argument("--rate", type=float, default=None, help="语速，字/秒，默认 4.0（约 240 字/分钟）；风格卡可以覆盖")
    parser.add_argument("--target-seconds", type=int, default=None, help="目标时长（秒）")
    parser.add_argument("--terms", default="", help="额外要盯的术语，逗号分隔")
    parser.add_argument("--allow", default="", help="放行的词（比如人设卡里的口头禅），逗号分隔")
    parser.add_argument("--delivery", choices=["human", "tts"], default="human", help="human 真人出镜／tts 配音或数字人")
    parser.add_argument("--soft-breath", type=int, default=None, help="不停顿超过多少字算偏长，默认 22")
    parser.add_argument("--hard-breath", type=int, default=None, help="不停顿超过多少字必须拆，默认 32")
    parser.add_argument("--style-card", default=None, help="风格卡路径（references/style-cards/*.md），对比像不像")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args(argv)

    style = None
    if args.style_card:
        try:
            style = load_style_card(args.style_card)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            print("风格卡读取失败：%s" % exc, file=sys.stderr)
            return 2

    try:
        if args.path == "-":
            text = sys.stdin.read()
        else:
            with open(args.path, encoding="utf-8") as f:
                text = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        print("读取失败：%s" % exc, file=sys.stderr)
        return 2

    if not text.strip():
        print("稿件是空的", file=sys.stderr)
        return 2

    split = lambda s: [w.strip() for w in re.split(r"[,，、]", s) if w.strip()]
    result = lint(text, rate=args.rate, target_seconds=args.target_seconds, terms=split(args.terms),
                  allow=split(args.allow), delivery=args.delivery,
                  soft_breath=args.soft_breath, hard_breath=args.hard_breath, style=style)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_report(result))
    return 1 if result["summary"][MUST] else 0


if __name__ == "__main__":
    sys.exit(main())
