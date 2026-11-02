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
