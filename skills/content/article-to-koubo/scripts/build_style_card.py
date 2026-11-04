#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从口播逐字稿生成风格卡骨架（只用 Python 标准库）。

把某位博主（或你自己）的几份口播逐字稿喂进来，自动算出：
- 真实语速（只有带时间戳的 .srt／.vtt 字幕才能算）
- 各项可量化指标的区间，写成 koubo_lint.py --style-card 能读的 json 代码块
- 体检在真人稿上的误报（命中"必须改"的项），用来校准规则
- 高频口头语，留给人工判断哪些是说话习惯、哪些是不能照搬的标志性用语

开头套路、结构、金句、情绪推进这些定性部分，工具只留空位，需要看过原视频后人工补全。

用法：
  python3 build_style_card.py 稿1.srt 稿2.vtt 稿3.txt --name "某某风格" --slug someone -o 风格卡.md

逐字稿原文只用来统计，输出里不包含任何整句原文。
退出码：0 成功；2 读取失败或没有可用样本。
"""

import argparse
import json
import os
import re
import statistics
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from koubo_lint import FILLER_WORDS, MUST, STYLE_METRICS, lint, speech_units  # noqa: E402

TIME_RE = re.compile(
    r"(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})\s*-->\s*(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})")
TAG_RE = re.compile(r"<[^>]*>|\{[^}]*\}")
PUNCT_RE = re.compile(r"[，,。！？!?、…；;：:]")
CJK_RUN_RE = re.compile(r"[一-鿿]+")

# 这些类别在任何风格里都不放行
NEVER_ALLOW = {"空洞恐吓", "拔高套话", "客服腔", "视觉指代", "书面符号"}
PERCENT_METRICS = {k for k, unit in STYLE_METRICS.items() if unit == "%"}
# 跨词切出来的残片（"的时""有一"）多半以这些字开头或结尾，过滤掉
FRAGMENT_BAD_START = set("的了着地得们")
FRAGMENT_BAD_END = set("一的")


def _seconds(h, m, s, ms):
    return int(h or 0) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000.0


def parse_subtitle(text):
    """解析 SRT／VTT，返回 [(开始秒, 结束秒, [文字行])]，已去掉滚动字幕的重复行。"""
    cues = []
    previous_lines = set()
    last_emitted = None
    for block in re.split(r"\n\s*\n", text.replace("\r\n", "\n").replace("\r", "\n")):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        time_index = next((i for i, l in enumerate(lines) if TIME_RE.search(l)), None)
        if time_index is None:
            continue
        m = TIME_RE.search(lines[time_index])
        start = _seconds(m.group(1), m.group(2), m.group(3), m.group(4))
        end = _seconds(m.group(5), m.group(6), m.group(7), m.group(8))
        texts = []
        for raw in lines[time_index + 1:]:
            line = TAG_RE.sub("", raw).strip()
            if not line or line in previous_lines or line == last_emitted:
                continue
            texts.append(line)
            last_emitted = line
        previous_lines = {TAG_RE.sub("", l).strip() for l in lines[time_index + 1:]}
        if end > start:
            cues.append((start, end, texts))
    return cues


def voiced_seconds(cues):
    """合并重叠区间后的有声时长。"""
    total = 0.0
    current_start = current_end = None
    for start, end, _ in sorted(cues):
        if current_end is None or start > current_end:
            if current_end is not None:
                total += current_end - current_start
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)
    if current_end is not None:
        total += current_end - current_start
    return total


def load_sample(path):
    with open(path, encoding="utf-8-sig") as f:
        raw = f.read()
    name = os.path.basename(path)
    is_subtitle = path.lower().endswith((".srt", ".vtt")) or bool(TIME_RE.search(raw))
    if is_subtitle:
        cues = parse_subtitle(raw)
        body = "\n".join(line for _, _, texts in cues for line in texts)
        seconds = voiced_seconds(cues)
        rate = round(speech_units(body) / seconds, 2) if seconds > 0 and body else None
    else:
        body = raw.strip()
        rate = None
    return {"name": name, "body": body, "rate": rate}


def frequent_fragments(bodies, limit=30):
    """跨样本反复出现的 2–4 字片段：先按出现在几篇排序，再按总次数；去掉被更长片段完全覆盖的短片段。"""
    total = Counter()
    doc_freq = Counter()
    for body in bodies:
        seen = set()
        for run in CJK_RUN_RE.findall(body):
            for n in (2, 3, 4):
                for i in range(len(run) - n + 1):
                    piece = run[i:i + n]
                    total[piece] += 1
                    seen.add(piece)
        doc_freq.update(seen)
    min_docs = 2 if len(bodies) >= 2 else 1
    kept = [p for p in total if doc_freq[p] >= min_docs and total[p] >= 3
            and p[0] not in FRAGMENT_BAD_START and p[-1] not in FRAGMENT_BAD_END]
    kept.sort(key=lambda p: (-doc_freq[p], -total[p], -len(p)))
    result = []
    for piece in kept:
        if any(piece in longer and total[longer] == total[piece] for longer, _, _ in result):
            continue
        result.append((piece, total[piece], doc_freq[piece]))
        if len(result) >= limit:
            break
    return result


def widen(low, high, metric, margin):
    lo = round(low * (1 - margin), 1)
    hi = round(high * (1 + margin), 1)
    if lo == hi:
        lo, hi = round(lo - 0.5, 1), round(hi + 0.5, 1)
    lo = max(0, lo)  # 所有指标都不会是负数
    if metric in PERCENT_METRICS:
        hi = min(100, hi)
    return [lo, hi]


def build_card(samples, name="未命名风格", slug="custom", margin=0.1):
    """samples 是 load_sample() 的结果列表，返回风格卡 Markdown 文本。"""
    samples = [s for s in samples if speech_units(s["body"]) > 0]
    if not samples:
        raise ValueError("没有可用的逐字稿样本")

    rows = []
    must_hits = Counter()
    must_docs = Counter()
    candidate_hits = Counter()
    candidate_docs = Counter()
    filler_over = Counter()
    punct_per100 = []
    for s in samples:
        result = lint(s["body"], rate=s["rate"] or 4.0)
        stats = result["stats"]
        units = stats["字数估算"]
        punct_per100.append(len(PUNCT_RE.findall(s["body"])) * 100.0 / units if units else 0.0)
        seen_must, seen_candidate = set(), set()
        for issue in result["issues"]:
            key = (issue["category"], issue["match"].split(" ")[0])
            if issue["level"] == MUST:
                must_hits[key] += issue.get("count", 1)
                seen_must.add(key)
            if issue["category"] not in NEVER_ALLOW and issue["category"] in (
                    "网络烂梗", "模板开场收尾", "假情绪", "书面词", "AI 高频词", "黑话术语", "过渡套话", "开场套话"):
                candidate_hits[key] += issue.get("count", 1)
                seen_candidate.add(key)
        must_docs.update(seen_must)
        candidate_docs.update(seen_candidate)
        cap = max(1, units // 300)
        for word in FILLER_WORDS:
            if s["body"].count(word) > cap:
                filler_over[word] += 1
        rows.append((s, stats, result["summary"][MUST]))

    targets = {}
    for metric in STYLE_METRICS:
        values = [stats[metric] for _, stats, _ in rows if metric in stats]
        if values:
            targets[metric] = widen(min(values), max(values), metric, margin)

    allow = sorted(w for w, n in filler_over.items() if n * 2 >= len(samples))
    card = {"koubo_style": slug, "name": name, "targets": targets, "allow": allow}
    rates = [s["rate"] for s in samples if s["rate"]]
    if rates:
        card["rate"] = round(statistics.median(rates), 2)

    warnings = []
    if len(samples) < 3:
        warnings.append("样本只有 %d 份，区间很可能偏窄或偏移，建议至少 3–5 份。" % len(samples))
    low_punct = [s["name"] for s, p in zip(samples, punct_per100) if p < 3]
    if low_punct:
        warnings.append("这些样本标点很少（每百字不到 3 个），像是自动字幕：%s。平均句长、短句占比、问句密度会失真，"
                        "建议先补标点再生成。" % "、".join(low_punct))
    if not rates:
        warnings.append("没有带时间戳的字幕，算不出真实语速，json 里没有写 rate。")

    out = []
    out.append("# 风格卡：%s" % name)
    out.append("")
    out.append("> 由 `build_style_card.py` 根据 %d 份逐字稿自动生成的骨架。数值部分来自统计；"
               "\"待人工填写\"的部分要看过原视频后补全。" % len(samples))
    out.append("> 用途是学说话方式，不是冒充本人：不用对方的名字、身份、经历、标志性开场和结束语，"
               "不照搬原句，不编事实和经历，紧迫感要有原文事实撑着。")
    if warnings:
        out.append("")
        out.append("**警告**")
        out.append("")
        for w in warnings:
            out.append("- %s" % w)

    out.append("")
    out.append("## 数值目标")
    out.append("")
    out.append("体检时加 `--style-card <本文件>`，脚本会读取下面的 json，对比\"像不像\"。")
    out.append("")
    out.append("```json")
    out.append(re.sub(r"\[\s*([^\[\]]*?)\s*\]",
                      lambda m: "[" + re.sub(r",\s+", ", ", m.group(1)) + "]",
                      json.dumps(card, ensure_ascii=False, indent=2)))
    out.append("```")

    out.append("")
    out.append("## 逐篇统计")
    out.append("")
    header = ["样本", "字数", "语速"] + list(STYLE_METRICS) + ["必须改"]
    out.append("| " + " | ".join(header) + " |")
    out.append("| " + " | ".join(["---"] * len(header)) + " |")
    for s, stats, must in rows:
        cells = [s["name"], str(stats["字数估算"]), str(s["rate"]) if s["rate"] else "—"]
        cells += [str(stats.get(m, "—")) for m in STYLE_METRICS]
        cells.append(str(must))
        out.append("| " + " | ".join(cells) + " |")

    out.append("")
    out.append("## 体检误报（真人稿命中\"必须改\"）")
    out.append("")
    if must_hits:
        out.append("先判断是规则太严，还是这种风格本来就和默认规则不同：前者调整 `koubo_lint.py` 的默认规则，"
                   "后者写进下面\"覆盖默认规则的地方\"。")
        out.append("")
        out.append("| 类别 | 命中 | 次数 | 出现在几篇 |")
        out.append("| --- | --- | --- | --- |")
        for (category, match), count in must_hits.most_common():
            out.append("| %s | %s | %d | %d |" % (category, match, count, must_docs[(category, match)]))
    else:
        out.append("没有误报。")

    out.append("")
    out.append("## 可能需要放行的词（人工判断）")
    out.append("")
    out.append("体检在这些词上报了问题，但它们在样本里反复出现，可能是这种风格的说话习惯。"
               "确认是习惯、又不是对方的标志性用语后，再手动加进 json 的 allow。")
    out.append("")
    repeated = [(k, n) for k, n in candidate_hits.most_common() if candidate_docs[k] >= min(2, len(samples))]
    if repeated:
        out.append("| 类别 | 词 | 次数 | 出现在几篇 |")
        out.append("| --- | --- | --- | --- |")
        for (category, match), count in repeated:
            out.append("| %s | %s | %d | %d |" % (category, match, count, candidate_docs[(category, match)]))
    else:
        out.append("没有。")

    out.append("")
    out.append("## 高频口头语（需要人工筛选）")
    out.append("")
    out.append("跨样本反复出现的 2–4 字片段，里面混着普通词，需要人工挑。分成两类："
               "普通的说话习惯可以学；对方的标志性用语（一听就知道是他）不能照搬。")
    out.append("")
    out.append("| 片段 | 次数 | 出现在几篇 |")
    out.append("| --- | --- | --- |")
    for piece, count, docs in frequent_fragments([s["body"] for s in samples]):
        out.append("| %s | %d | %d |" % (piece, count, docs))

    out.append("")
    out.append("## 待人工填写")
    out.append("")
    out.append("每一条都写成：他怎么做 → 为什么有效 → 你怎么用，再配一个自己写的示例。不要贴原句。")
    for section in ("开头套路", "结构模板", "讲故事的方法", "金句：写法、数量、位置", "情绪推进",
                    "幽默手法", "术语和数字的处理", "结尾方式", "覆盖默认规则的地方"):
        out.append("")
        out.append("### %s" % section)
        out.append("")
        out.append("（待填写）")
    out.append("")
    out.append("### 底线")
    out.append("")
    out.append("- 不冒充本人：不用对方的名字、身份、经历，不用对方标志性的自我介绍和结束语。")
    out.append("- 不照搬对方的原句和原稿。")
    out.append("- 不编事实、不编经历：故事位置换成用户自己的经历，用户没提供时写成 `[[待补]]`。")
    out.append("- 紧迫感可以学，但必须有原文事实撑着，不能变成空洞的恐吓。")
    out.append("")
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description="从口播逐字稿生成风格卡骨架")
    parser.add_argument("files", nargs="+", help="逐字稿文件：.txt／.srt／.vtt")
    parser.add_argument("--name", default="未命名风格", help="风格名，显示在体检报告里")
    parser.add_argument("--slug", default="custom", help="风格标识，写进 json 的 koubo_style")
    parser.add_argument("--margin", type=float, default=0.1, help="区间放宽比例，默认 0.1（10%%）")
    parser.add_argument("-o", "--output", default=None, help="输出文件路径；不写就打印到标准输出")
    args = parser.parse_args(argv)

    samples = []
    for path in args.files:
        try:
            samples.append(load_sample(path))
        except (OSError, UnicodeDecodeError) as exc:
            print("读取失败：%s" % exc, file=sys.stderr)
            return 2
    try:
        card = build_card(samples, name=args.name, slug=args.slug, margin=args.margin)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(card)
        print("已写入 %s" % args.output, file=sys.stderr)
    else:
        print(card)
    return 0


if __name__ == "__main__":
    sys.exit(main())
