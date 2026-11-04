#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""koubo_lint.py 的回归测试（只用标准库 unittest）。

运行：python3 scripts/test_koubo_lint.py
调阈值或改词表之后先跑一遍，确认反例还能抓出来、正例没有被误报。
"""

import contextlib
import io
import os
import pathlib
import re
import sys
import tempfile
import unittest

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import koubo_lint  # noqa: E402
from koubo_lint import INFO, MUST, SHOULD, lint  # noqa: E402


def read(relative):
    return (SKILL_DIR / relative).read_text(encoding="utf-8")


def text_blocks(markdown, label=None):
    """抓 ```text 代码块；给了 label 就只抓紧跟在 **label** 后面的块。"""
    if label:
        pattern = r"\*\*" + re.escape(label) + r"\*\*\s*\n\s*```text\n(.*?)```"
    else:
        pattern = r"```text\n(.*?)```"
    return re.findall(pattern, markdown, re.S)


def run_main(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = koubo_lint.main(argv)
    return code, out.getvalue(), err.getvalue()


def found(result, level=None, category=None, match=None):
    for issue in result["issues"]:
        if level and issue["level"] != level:
            continue
        if category and issue["category"] != category:
            continue
        if match and match not in issue["match"]:
            continue
        return True
    return False


class NegativeSamples(unittest.TestCase):
    def test_ai_flavored_sample_is_caught(self):
        result = lint(read("examples/ai-flavored-sample.txt"))
        self.assertGreater(result["summary"][MUST], 0)
        for category in ("开场套话", "过渡套话", "拔高套话"):
            self.assertTrue(found(result, MUST, category), category)
        self.assertTrue(found(result, MUST, "书面符号", "括号"))
        self.assertTrue(found(result, SHOULD, "结构套路", "首先…其次"))
        self.assertTrue(found(result, SHOULD, "结构套路", "不是…而是"))
        self.assertTrue(found(result, MUST, "结构套路", "在…的今天"))

    def test_ai_flavored_sample_exit_code(self):
        code, _, _ = run_main([str(SKILL_DIR / "examples/ai-flavored-sample.txt")])
        self.assertEqual(code, 1)

    def test_before_versions_in_reference_are_caught(self):
        blocks = text_blocks(read("references/before-after.md"), "AI 味版")
        self.assertEqual(len(blocks), 3)
        for block in blocks:
            self.assertGreater(lint(block)["summary"][MUST], 0, block[:30])


class PositiveSamples(unittest.TestCase):
    def test_after_versions_in_reference_pass(self):
        blocks = text_blocks(read("references/before-after.md"), "活人版")
        self.assertEqual(len(blocks), 3)
        for block in blocks:
            result = lint(block)
            self.assertEqual(result["summary"][MUST], 0, [i for i in result["issues"] if i["level"] == MUST])

    def test_demo_script_passes_with_target(self):
        blocks = text_blocks(read("examples/demo-output.md"))
        self.assertEqual(len(blocks), 1)
        result = lint(blocks[0], target_seconds=120)
        self.assertEqual(result["summary"][MUST], 0)
        self.assertFalse(found(result, category="时长"))


class Rules(unittest.TestCase):
    def test_placeholder_is_ignored_but_counted(self):
        result = lint("你记不记得那次？[[待补：你自己的经历（越具体越好）——别编]]我是真服了。")
        self.assertFalse(found(result, category="书面符号"))
        self.assertEqual(result["stats"]["待补占位"], 1)

    def test_allow_list_releases_persona_words(self):
        text = "家人们，你听我说吧，这事儿挺简单的。"
        self.assertTrue(found(lint(text), MUST, "网络烂梗", "家人们"))
        self.assertFalse(found(lint(text, allow=["家人们"]), category="网络烂梗"))

    def test_tts_upgrades_number_hints(self):
        text = "准确率是 62%，你记住这个数吧。"
        self.assertTrue(found(lint(text), INFO, "数字", "62%"))
        self.assertTrue(found(lint(text, delivery="tts"), SHOULD, "数字", "62%"))

    def test_hard_breath_limit(self):
        long_clause = "这个系统会在每天凌晨自动把所有部门提交上来的报销单据统一整理归档再发给财务审核"
        result = lint(long_clause + "。你看行吧。")
        self.assertTrue(found(result, MUST, "气口"))

    def test_soft_breath_limit(self):
        result = lint("它会把上个月所有部门交上来的报销单都整理好再发出去。你看行吧。")  # 25 字
        self.assertTrue(found(result, SHOULD, "气口"))
        self.assertFalse(found(result, MUST, "气口"))

    def test_duration_drift(self):
        result = lint("你好吧。" * 10, target_seconds=120)
        self.assertTrue(found(result, SHOULD, "时长"))


    def test_empty_threat_is_flagged(self):
        result = lint("你再不学这个，三年后就被淘汰了。你自己想想吧。")
        self.assertTrue(found(result, SHOULD, "空洞恐吓", "被淘汰"))
        self.assertTrue(found(result, SHOULD, "结构套路", "再不…就…"))


# 测试用的样例风格卡，数值只为测试，不代表任何真实博主
FIXTURE_CARD = """# 测试风格卡

说明文字。

```json
{
  "koubo_style": "fixture",
  "name": "测试风格",
  "rate": 5.0,
  "allow": ["家人们"],
  "targets": {
    "平均句长": [5, 12],
    "语气词每百字": [3, 8],
    "你占称呼比": [50, 100]
  }
}
```
"""


class StyleCard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.card = os.path.join(self.tmp.name, "card.md")
        with open(self.card, "w", encoding="utf-8") as f:
            f.write(FIXTURE_CARD)

    def tearDown(self):
        self.tmp.cleanup()

    def test_load_and_allow(self):
        style = koubo_lint.load_style_card(self.card)
        self.assertEqual(style["name"], "测试风格")
        result = lint("家人们，你听我说吧，这事儿挺简单的。", style=style)
        self.assertFalse(found(result, category="网络烂梗"))

    def test_rate_comes_from_card_unless_given(self):
        style = koubo_lint.load_style_card(self.card)
        text = "你听我说吧，这事儿挺简单的。"
        self.assertEqual(lint(text, style=style)["stats"]["语速"], 5.0)
        self.assertEqual(lint(text, rate=3.5, style=style)["stats"]["语速"], 3.5)

    def test_deviation_is_reported(self):
        style = koubo_lint.load_style_card(self.card)
        text = "这个系统每天自动整理报销单据并发给财务审核，我们觉得效率提升很明显。我们会继续优化这个流程。"
        result = lint(text, style=style)
        self.assertTrue(found(result, SHOULD, "风格偏离", "语气词每百字"))
        self.assertTrue(found(result, SHOULD, "风格偏离", "你占称呼比"))
        rows = {r["指标"]: r for r in result["style"]["rows"]}
        self.assertFalse(rows["语气词每百字"]["在区间内"])

    def test_in_range_has_no_deviation(self):
        style = koubo_lint.load_style_card(self.card)
        result = lint("你听我说。这事儿其实很简单，你一试就懂了。你信我一次吧。", style=style)
        self.assertFalse(found(result, category="风格偏离"))
        self.assertTrue(all(r["在区间内"] for r in result["style"]["rows"]))

    def test_cli_report_and_bad_card(self):
        script = os.path.join(self.tmp.name, "s.txt")
        with open(script, "w", encoding="utf-8") as f:
            f.write("你听我说。这事儿其实很简单，你一试就懂了。你信我一次吧。")
        code, out, _ = run_main([script, "--style-card", self.card])
        self.assertEqual(code, 0)
        self.assertIn("像不像：测试风格", out)

        bad = os.path.join(self.tmp.name, "bad.md")
        with open(bad, "w", encoding="utf-8") as f:
            f.write('```json\n{"koubo_style": "x", "targets": {"不存在的指标": [1, 2]}}\n```\n')
        code, _, err = run_main([script, "--style-card", bad])
        self.assertEqual(code, 2)
        self.assertIn("不支持的指标", err)


import build_style_card  # noqa: E402

SRT_FIXTURE = """1
00:00:00,000 --> 00:00:02,000
你听我说

2
00:00:02,000 --> 00:00:04,000
这事儿其实很简单
"""

# YouTube 自动字幕式的滚动重复：下一条会把上一条的行再带一遍
VTT_FIXTURE = """WEBVTT

00:00:00.000 --> 00:00:02.000
你听我说

00:00:01.500 --> 00:00:04.000
你听我说
这事儿很简单
"""


class BuildStyleCard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, content):
        path = os.path.join(self.tmp.name, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_srt_parsing_and_rate(self):
        sample = build_style_card.load_sample(self.write("a.srt", SRT_FIXTURE))
        self.assertEqual(sample["body"], "你听我说\n这事儿其实很简单")
        self.assertAlmostEqual(sample["rate"], 12 / 4.0, places=2)  # 4 + 8 字，4 秒

    def test_vtt_rolling_duplicates_and_overlap(self):
        sample = build_style_card.load_sample(self.write("a.vtt", VTT_FIXTURE))
        self.assertEqual(sample["body"], "你听我说\n这事儿很简单")
        self.assertAlmostEqual(sample["rate"], 10 / 4.0, places=2)  # 重叠区间只算一次

    def test_card_round_trip_is_self_consistent(self):
        blocks = text_blocks(read("references/before-after.md"), "活人版")
        paths = [self.write("s%d.txt" % i, b) for i, b in enumerate(blocks)]
        card_path = os.path.join(self.tmp.name, "card.md")
        code = build_style_card.main(paths + ["--name", "自洽测试", "--slug", "selfcheck", "-o", card_path])
        self.assertEqual(code, 0)
        style = koubo_lint.load_style_card(card_path)
        self.assertEqual(style["koubo_style"], "selfcheck")
        self.assertTrue(all(low >= 0 for low, _ in style["targets"].values()))
        for block in blocks:
            rows = lint(block, style=style)["style"]["rows"]
            self.assertTrue(all(r["在区间内"] for r in rows), [r for r in rows if not r["在区间内"]])

    def test_card_has_no_full_sentences_from_samples(self):
        blocks = text_blocks(read("references/before-after.md"), "活人版")
        samples = [{"name": "s%d" % i, "body": b, "rate": None} for i, b in enumerate(blocks)]
        card = build_style_card.build_card(samples)
        for block in blocks:
            for sentence in re.split(r"[。！？\n]", block):
                if len(sentence) >= 8:
                    self.assertNotIn(sentence, card)

    def test_warnings_for_few_samples_and_missing_punctuation(self):
        samples = [{"name": "raw", "body": "你听我说这事儿其实很简单你一试就懂了你信我一次吧", "rate": None}]
        card = build_style_card.build_card(samples)
        self.assertIn("样本只有 1 份", card)
        self.assertIn("标点很少", card)
        self.assertIn("算不出真实语速", card)

    def test_no_usable_sample_returns_2(self):
        path = self.write("empty.txt", "\n")
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(build_style_card.main([path]), 2)


class Cli(unittest.TestCase):
    def test_empty_file_returns_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "empty.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n")
            code, _, err = run_main([path])
        self.assertEqual(code, 2)
        self.assertIn("空", err)

    def test_missing_file_returns_2(self):
        code, _, _ = run_main([os.path.join(tempfile.gettempdir(), "koubo-missing-file.txt")])
        self.assertEqual(code, 2)

    def test_clean_script_returns_0_and_json_works(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "ok.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text_blocks(read("examples/demo-output.md"))[0])
            code, out, _ = run_main([path, "--json"])
        self.assertEqual(code, 0)
        self.assertIn('"summary"', out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
