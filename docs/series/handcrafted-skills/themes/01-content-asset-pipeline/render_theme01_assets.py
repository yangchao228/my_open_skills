#!/usr/bin/env python3
"""Render Theme 01 Open Weave card assets from render-spec-v3.json."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SPEC_PATH = ROOT / "render-spec-v3.json"

PAPER = "#F4EFE5"
INK = "#19201D"
BLUE = "#2D58FF"
ORANGE = "#EF662F"
GREEN = "#2D7E68"
MUTED = "#747A74"
GRID = "#DED8CC"
WHITE = "#FBFAF6"
SOFT_BLUE = "#E4E9FF"
SOFT_ORANGE = "#F8DED1"
SOFT_GREEN = "#DDECE6"
DARK_BG = "#19201D"

CJK_FONT_CANDIDATES = (
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "C:/Windows/Fonts/msyh.ttc",
)
MONO_FONT_CANDIDATES = (
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "C:/Windows/Fonts/consola.ttf",
)
CJK_FONT: Path | None = None
MONO_FONT: Path | None = None
FONT_CACHE: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def resolve_font(override: str | None, candidates: tuple[str, ...], label: str) -> Path:
    paths = (override,) if override else candidates
    for value in paths:
        if value and Path(value).is_file():
            return Path(value)
    hint = f"; received override: {override}" if override else ""
    raise SystemExit(f"no usable {label} font found{hint}; pass --{label}-font")


def get_font(size: int, mono: bool = False) -> ImageFont.FreeTypeFont:
    key = ("mono" if mono else "cjk", size)
    if key not in FONT_CACHE:
        path = MONO_FONT if mono else CJK_FONT
        if path is None:
            raise RuntimeError("fonts are not configured")
        FONT_CACHE[key] = ImageFont.truetype(path, size=size)
    return FONT_CACHE[key]


def accent_color(name: str) -> str:
    return ORANGE if name == "orange" else BLUE


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
    max_lines: int | None = None,
) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for char in paragraph:
            candidate = current + char
            if current and text_width(draw, candidate, font) > max_width:
                lines.append(current)
                current = char
            else:
                current = candidate
        if current:
            lines.append(current)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and text_width(draw, last + "…", font) > max_width:
            last = last[:-1]
        lines[-1] = last + "…"
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 10,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrap_text(draw, text, font, max_width, max_lines=max_lines)
    line_height = font.size + line_gap
    for line in lines:
        draw.text((x, y), line, fill=fill, font=font)
        y += line_height
    return y


def rounded_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str = WHITE,
    outline: str = INK,
    width: int = 2,
    radius: int = 22,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    width: int = 4,
) -> None:
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 14
    spread = 0.55
    p1 = (
        end[0] - length * math.cos(angle - spread),
        end[1] - length * math.sin(angle - spread),
    )
    p2 = (
        end[0] - length * math.cos(angle + spread),
        end[1] - length * math.sin(angle + spread),
    )
    draw.polygon([end, p1, p2], fill=color)


def tag(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fill: str = INK,
    text_fill: str = WHITE,
) -> tuple[int, int, int, int]:
    font = get_font(16, mono=all(ord(char) < 128 for char in text))
    w = text_width(draw, text, font) + 24
    h = 32
    x, y = xy
    draw.rounded_rectangle((x, y, x + w, y + h), radius=8, fill=fill)
    draw.text((x + 12, y + 7), text, fill=text_fill, font=font)
    return (x, y, x + w, y + h)


def base_canvas(card: dict, width: int, height: int, profile: str, page: int, total: int):
    img = Image.new("RGB", (width, height), PAPER)
    draw = ImageDraw.Draw(img)
    accent = accent_color(card.get("accent", "blue"))
    strip = max(10, width // 90)
    draw.rectangle((0, 0, strip, height), fill=accent)

    step = 72 if height > width else 80
    for x in range(step, width, step):
        draw.line((x, 58, x, height - 58), fill=GRID, width=1)
    for y in range(58, height, step):
        draw.line((58, y, width - 58, y), fill=GRID, width=1)

    margin = 72 if width >= 1400 else 62
    header_y = 46
    draw.text((margin, header_y), "OPEN WEAVE / THEME 01", fill=MUTED, font=get_font(16, mono=True))
    profile_text = f"{profile}   {page:02d}/{total:02d}"
    pw = text_width(draw, profile_text, get_font(16, mono=True))
    draw.text((width - margin - pw, header_y), profile_text, fill=INK, font=get_font(16, mono=True))
    draw.line((margin, 82, width - margin, 82), fill=INK, width=2)

    title_size = 58 if width >= 1400 else 58
    title_y = 116 if width >= 1400 else 122
    title_end = draw_wrapped(
        draw,
        (margin, title_y),
        card["title"],
        get_font(title_size),
        INK,
        width - margin * 2,
        line_gap=8,
        max_lines=2,
    )
    subtitle_y = title_end + 8
    subtitle_end = draw_wrapped(
        draw,
        (margin, subtitle_y),
        card.get("subtitle", ""),
        get_font(24),
        MUTED,
        width - margin * 2,
        line_gap=6,
        max_lines=2,
    )
    content_top = max(278 if width >= 1400 else 330, subtitle_end + 30)

    footer_y = height - 66
    draw.text((margin, footer_y), "YANGCHAO228 / MY_OPEN_SKILLS", fill=MUTED, font=get_font(14, mono=True))
    footer = card.get("footer", "PUBLIC WORKFLOW ASSET")
    fw = text_width(draw, footer, get_font(14, mono=True))
    draw.text((width - margin - fw, footer_y), footer, fill=MUTED, font=get_font(14, mono=True))
    return img, draw, accent, margin, content_top, height - 105


def center_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    max_lines: int = 3,
) -> None:
    x1, y1, x2, y2 = box
    lines = wrap_text(draw, text, font, x2 - x1 - 30, max_lines=max_lines)
    line_h = font.size + 8
    total_h = line_h * len(lines) - 8
    y = y1 + (y2 - y1 - total_h) // 2
    for line in lines:
        w = text_width(draw, line, font)
        draw.text((x1 + (x2 - x1 - w) // 2, y), line, fill=fill, font=font)
        y += line_h


def render_matrix(draw, card, accent, margin, top, bottom, width, height):
    if width >= 1400:
        source = (margin, top + 70, margin + 350, bottom - 70)
        rounded_box(draw, source, fill=INK, outline=INK, width=3, radius=26)
        tag(draw, (source[0] + 28, source[1] + 26), "SOURCE / REVIEWED", ORANGE)
        center_text(draw, (source[0] + 20, source[1] + 45, source[2] - 20, source[3]), card["source"], get_font(42), WHITE)
        bus_x = source[2] + 86
        x0 = bus_x + 54
        cell_w = width - margin - x0
        gap = 18
        cell_h = 94
        block_h = len(card["outputs"]) * cell_h + (len(card["outputs"]) - 1) * gap
        first_y = top + (bottom - top - block_h) // 2
        centers = []
        for i, output in enumerate(card["outputs"]):
            x1 = x0
            y1 = first_y + i * (cell_h + gap)
            box = (x1, y1, x1 + cell_w, y1 + cell_h)
            rounded_box(draw, box, fill=WHITE, outline=BLUE if i < 2 else ORANGE, width=3, radius=22)
            draw.text((x1 + 24, y1 + 20), f"0{i + 1}", fill=BLUE if i < 2 else ORANGE, font=get_font(18, mono=True))
            center_text(draw, (x1 + 80, y1, box[2] - 20, box[3]), output, get_font(32), INK)
            centers.append((x1, (y1 + y1 + cell_h) // 2))
        source_mid = (source[1] + source[3]) // 2
        arrow(draw, (source[2], source_mid), (bus_x, source_mid), accent)
        draw.line((bus_x, centers[0][1], bus_x, centers[-1][1]), fill=GRID, width=3)
        for target in centers:
            arrow(draw, (bus_x, target[1]), target, accent)
    else:
        source_w = width - margin * 2 - 150
        source = (margin + 75, top + 30, margin + 75 + source_w, top + 180)
        rounded_box(draw, source, fill=INK, outline=INK, width=3, radius=26)
        tag(draw, (source[0] + 24, source[1] + 20), "SOURCE / REVIEWED", ORANGE)
        center_text(draw, (source[0] + 20, source[1] + 28, source[2] - 20, source[3]), card["source"], get_font(36), WHITE)
        bus_x = margin + 34
        x1 = margin + 112
        cell_w = width - margin - x1
        cell_h = 132
        gap = 26
        first_y = source[3] + 76
        source_link_y = source[3] + 38
        draw.line((width // 2, source[3], width // 2, source_link_y), fill=accent, width=4)
        draw.line((bus_x, source_link_y, width // 2, source_link_y), fill=GRID, width=3)
        last_center = first_y + (len(card["outputs"]) - 1) * (cell_h + gap) + cell_h // 2
        draw.line((bus_x, source_link_y, bus_x, last_center), fill=GRID, width=3)
        for i, output in enumerate(card["outputs"]):
            y1 = first_y + i * (cell_h + gap)
            box = (x1, y1, x1 + cell_w, y1 + cell_h)
            color = BLUE if i < 2 else ORANGE
            rounded_box(draw, box, fill=WHITE, outline=color, width=3, radius=22)
            draw.text((x1 + 22, y1 + 18), f"0{i + 1}", fill=color, font=get_font(18, mono=True))
            center_text(draw, (x1 + 72, y1, box[2] - 20, box[3]), output, get_font(30), INK)
            target = (x1, y1 + cell_h // 2)
            arrow(draw, (bus_x, target[1]), target, color, width=4)


def render_pipeline(draw, card, accent, margin, top, bottom, width, height):
    steps = card["steps"]
    labels = card.get("labels", [""] * len(steps))
    if width >= 1400:
        gap = 22
        box_w = (width - margin * 2 - gap * (len(steps) - 1)) // len(steps)
        y1 = top + 120
        y2 = bottom - 110
        boxes = []
        for i, step in enumerate(steps):
            x1 = margin + i * (box_w + gap)
            box = (x1, y1, x1 + box_w, y2)
            fill = INK if i == len(steps) - 1 else WHITE
            outline = ORANGE if i >= len(steps) - 2 else BLUE
            rounded_box(draw, box, fill=fill, outline=outline, width=3, radius=24)
            draw.text((x1 + 22, y1 + 24), f"0{i + 1}", fill=outline, font=get_font(18, mono=True))
            center_text(draw, (x1 + 15, y1 + 35, x1 + box_w - 15, y2 - 20), step, get_font(30), WHITE if fill == INK else INK)
            label = labels[i]
            lw = text_width(draw, label, get_font(14, mono=True))
            draw.text((x1 + (box_w - lw) // 2, y2 - 42), label, fill=MUTED if fill != INK else WHITE, font=get_font(14, mono=True))
            boxes.append(box)
        for i in range(len(boxes) - 1):
            arrow(draw, (boxes[i][2], (y1 + y2) // 2), (boxes[i + 1][0], (y1 + y2) // 2), accent, width=4)
    else:
        x1 = margin + 42
        x2 = width - margin - 42
        box_h = 128
        gap = 40
        y = top + 24
        boxes = []
        for i, step in enumerate(steps):
            box = (x1, y, x2, y + box_h)
            fill = INK if i == len(steps) - 1 else WHITE
            outline = ORANGE if i >= len(steps) - 2 else BLUE
            rounded_box(draw, box, fill=fill, outline=outline, width=3, radius=22)
            draw.text((x1 + 24, y + 18), f"0{i + 1} / {labels[i]}", fill=outline, font=get_font(17, mono=True))
            center_text(draw, (x1 + 120, y + 8, x2 - 25, y + box_h), step, get_font(34), WHITE if fill == INK else INK)
            boxes.append(box)
            y += box_h + gap
        for i in range(len(boxes) - 1):
            arrow(draw, (width // 2, boxes[i][3]), (width // 2, boxes[i + 1][1]), accent, width=4)


def render_split(draw, card, accent, margin, top, bottom, width, height):
    source_w = width - margin * 2 - (200 if width < 1400 else 760)
    source_x = (width - source_w) // 2
    source_h = 126 if width < 1400 else 140
    source = (source_x, top + 20, source_x + source_w, top + 20 + source_h)
    rounded_box(draw, source, fill=INK, outline=INK, width=3, radius=24)
    tag(draw, (source[0] + 24, source[1] + 18), "SOURCE / REVIEWED", ORANGE)
    center_text(draw, (source[0] + 20, source[1] + 25, source[2] - 20, source[3]), card["source"], get_font(34), WHITE)
    gap = 36 if width < 1400 else 60
    box_w = (width - margin * 2 - gap) // 2
    y1 = source[3] + 105
    y2 = bottom - 55
    for i, branch in enumerate(card["branches"]):
        x1 = margin + i * (box_w + gap)
        color = BLUE if i == 0 else ORANGE
        box = (x1, y1, x1 + box_w, y2)
        rounded_box(draw, box, fill=WHITE, outline=color, width=3, radius=24)
        tag(draw, (x1 + 22, y1 + 22), branch["tag"], color)
        draw.text((x1 + 24, y1 + 82), branch["title"], fill=INK, font=get_font(34 if width < 1400 else 38))
        item_y = y1 + 155
        for j, item in enumerate(branch["items"]):
            draw.ellipse((x1 + 28, item_y + 10, x1 + 44, item_y + 26), fill=color)
            draw.text((x1 + 64, item_y), item, fill=INK, font=get_font(26 if width < 1400 else 28))
            if j < len(branch["items"]) - 1:
                draw.line((x1 + 36, item_y + 34, x1 + 36, item_y + 76), fill=GRID, width=3)
            item_y += 82
        target = ((box[0] + box[2]) // 2, box[1])
        junction_y = source[3] + 52
        draw.line((width // 2, source[3], width // 2, junction_y), fill=accent, width=4)
        draw.line((width // 2, junction_y, target[0], junction_y), fill=GRID, width=3)
        arrow(draw, (target[0], junction_y), target, color, width=4)


def render_branch(draw, card, accent, margin, top, bottom, width, height):
    source_w = width - margin * 2 - (120 if width < 1400 else 620)
    sx = (width - source_w) // 2
    source_h = 130
    source = (sx, top + 28, sx + source_w, top + 28 + source_h)
    rounded_box(draw, source, fill=INK, outline=INK, width=3, radius=24)
    tag(draw, (source[0] + 22, source[1] + 18), "CHECKED FILES", ORANGE)
    center_text(draw, (source[0] + 20, source[1] + 25, source[2] - 20, source[3]), card["source"], get_font(34), WHITE)
    gap = 34 if width < 1400 else 70
    box_w = (width - margin * 2 - gap) // 2
    y1 = source[3] + 104
    y2 = bottom - 60
    for i, branch in enumerate(card["branches"]):
        x1 = margin + i * (box_w + gap)
        color = BLUE if i == 0 else ORANGE
        fill = SOFT_BLUE if i == 0 else SOFT_ORANGE
        box = (x1, y1, x1 + box_w, y2)
        rounded_box(draw, box, fill=fill, outline=color, width=3, radius=24)
        tag(draw, (x1 + 24, y1 + 24), branch["tag"], color)
        draw.text((x1 + 26, y1 + 78), branch["title"], fill=INK, font=get_font(34 if width < 1400 else 36))
        if width >= 1400:
            item_gap = 14
            item_y = y1 + 140
            inner_w = box_w - 48
            item_w = (inner_w - item_gap * (len(branch["items"]) - 1)) // len(branch["items"])
            for j, item in enumerate(branch["items"]):
                ix = x1 + 24 + j * (item_w + item_gap)
                rounded_box(draw, (ix, item_y, ix + item_w, item_y + 62), fill=WHITE, outline=color, width=2, radius=14)
                center_text(draw, (ix + 8, item_y, ix + item_w - 8, item_y + 62), item, get_font(21), INK, max_lines=2)
                if j < len(branch["items"]) - 1:
                    arrow(draw, (ix + item_w, item_y + 31), (ix + item_w + item_gap, item_y + 31), color, width=2)
        else:
            item_y = y1 + 168
            for j, item in enumerate(branch["items"]):
                rounded_box(draw, (x1 + 24, item_y, x1 + box_w - 24, item_y + 78), fill=WHITE, outline=color, width=2, radius=16)
                draw.text((x1 + 48, item_y + 22), item, fill=INK, font=get_font(24))
                if j < len(branch["items"]) - 1:
                    arrow(draw, (x1 + box_w // 2, item_y + 78), (x1 + box_w // 2, item_y + 104), color, width=3)
                item_y += 106
        target = ((box[0] + box[2]) // 2, box[1])
        junction_y = source[3] + 50
        draw.line((width // 2, source[3], width // 2, junction_y), fill=accent, width=4)
        draw.line((width // 2, junction_y, target[0], junction_y), fill=GRID, width=3)
        arrow(draw, (target[0], junction_y), target, color, width=4)


def render_evidence(draw, card, accent, margin, top, bottom, width, height):
    metrics = card["metrics"]
    gap = 28
    cell_w = (width - margin * 2 - gap) // 2
    cell_h = 190
    for i, metric in enumerate(metrics):
        row, col = divmod(i, 2)
        x1 = margin + col * (cell_w + gap)
        y1 = top + row * (cell_h + gap)
        color = BLUE if i % 2 == 0 else ORANGE
        rounded_box(draw, (x1, y1, x1 + cell_w, y1 + cell_h), fill=WHITE, outline=color, width=3, radius=22)
        draw.text((x1 + 26, y1 + 24), metric["value"], fill=color, font=get_font(64, mono=True))
        draw.text((x1 + 28, y1 + 112), metric["label"], fill=INK, font=get_font(26))
    list_y = top + 2 * (cell_h + gap) + 28
    rounded_box(draw, (margin, list_y, width - margin, bottom - 35), fill=INK, outline=INK, width=3, radius=24)
    tag(draw, (margin + 26, list_y + 24), "REAL ARTIFACTS", ORANGE)
    y = list_y + 88
    for i, artifact in enumerate(card["artifacts"]):
        draw.text((margin + 32, y), f"0{i + 1}", fill=BLUE if i < 2 else ORANGE, font=get_font(18, mono=True))
        draw.text((margin + 100, y - 4), artifact, fill=WHITE, font=get_font(24, mono=True))
        y += 72


def render_layers(draw, card, accent, margin, top, bottom, width, height):
    layers = card["layers"]
    box_h = 185
    gap = 24
    y = top + 12
    for i, layer in enumerate(layers):
        color = BLUE if i < 2 else ORANGE
        box = (margin, y, width - margin, y + box_h)
        rounded_box(draw, box, fill=WHITE, outline=color, width=3, radius=22)
        draw.text((margin + 24, y + 26), f"0{i + 1}", fill=color, font=get_font(20, mono=True))
        draw.text((margin + 100, y + 20), layer["title"], fill=INK, font=get_font(34))
        draw.text((margin + 100, y + 80), layer["note"], fill=MUTED, font=get_font(24))
        sw = text_width(draw, layer["skills"], get_font(17, mono=True))
        draw.text((width - margin - 28 - sw, y + 29), layer["skills"], fill=color, font=get_font(17, mono=True))
        y += box_h + gap


def render_gate(draw, card, accent, margin, top, bottom, width, height):
    gap = 34
    box_w = (width - margin * 2 - gap) // 2
    y1 = top + 22
    y2 = bottom - 170
    groups = [
        ("READY / 已准备", card["completed"], BLUE, SOFT_BLUE),
        ("HUMAN / 待判断", card["pending"], ORANGE, SOFT_ORANGE),
    ]
    for i, (title, items, color, fill) in enumerate(groups):
        x1 = margin + i * (box_w + gap)
        rounded_box(draw, (x1, y1, x1 + box_w, y2), fill=fill, outline=color, width=3, radius=24)
        tag(draw, (x1 + 22, y1 + 22), title, color)
        y = y1 + 92
        for j, item in enumerate(items):
            draw.ellipse((x1 + 28, y + 8, x1 + 46, y + 26), fill=color)
            draw.text((x1 + 68, y), item, fill=INK, font=get_font(25))
            y += 86
    repo_box = (margin + 40, y2 + 45, width - margin - 40, bottom - 35)
    rounded_box(draw, repo_box, fill=INK, outline=INK, width=3, radius=22)
    center_text(draw, repo_box, card.get("repo", "HUMAN CONFIRMATION"), get_font(25, mono=True), WHITE)


def render_reproduce(draw, card, accent, margin, top, bottom, width, height):
    tag(draw, (margin, top + 8), "ONE PROMPT", BLUE)
    prompt_box = (margin, top + 62, width - margin, bottom - 250)
    rounded_box(draw, prompt_box, fill=INK, outline=INK, width=3, radius=26)
    draw_wrapped(
        draw,
        (prompt_box[0] + 38, prompt_box[1] + 42),
        card["prompt"],
        get_font(29),
        WHITE,
        prompt_box[2] - prompt_box[0] - 76,
        line_gap=16,
        max_lines=10,
    )
    repo_y = bottom - 205
    draw.text((margin, repo_y), "REPOSITORY", fill=ORANGE, font=get_font(18, mono=True))
    draw.text((margin, repo_y + 44), card["repo"], fill=INK, font=get_font(33, mono=True))
    y = bottom - 85
    steps = ["输入公开长文", "生成平台资产", "停在人工确认"]
    box_w = (width - margin * 2 - 24 * 2) // 3
    for i, step in enumerate(steps):
        x1 = margin + i * (box_w + 24)
        rounded_box(draw, (x1, y, x1 + box_w, y + 68), fill=WHITE, outline=BLUE if i < 2 else ORANGE, width=2, radius=14)
        center_text(draw, (x1, y, x1 + box_w, y + 68), step, get_font(18), INK, max_lines=2)


RENDERERS = {
    "matrix": render_matrix,
    "pipeline": render_pipeline,
    "split": render_split,
    "branch": render_branch,
    "evidence": render_evidence,
    "layers": render_layers,
    "gate": render_gate,
    "reproduce": render_reproduce,
}


def render_card(card: dict, width: int, height: int, profile: str, page: int, total: int) -> Image.Image:
    img, draw, accent, margin, top, bottom = base_canvas(card, width, height, profile, page, total)
    RENDERERS[card["layout"]](draw, card, accent, margin, top, bottom, width, height)
    return img


def make_contact_sheet(set_spec: dict, paths: list[Path]) -> None:
    vertical = set_spec["height"] > set_spec["width"]
    if vertical:
        cols = 4 if len(paths) >= 8 else 3
        thumb_w = 390
    else:
        cols = 1
        thumb_w = 1120
    rows = math.ceil(len(paths) / cols)
    ratio = set_spec["height"] / set_spec["width"]
    thumb_h = int(thumb_w * ratio)
    gap = 36
    margin = 72
    title_h = 120
    sheet_w = margin * 2 + cols * thumb_w + (cols - 1) * gap
    sheet_h = margin + title_h + rows * thumb_h + (rows - 1) * gap + margin
    sheet = Image.new("RGB", (sheet_w, sheet_h), DARK_BG)
    draw = ImageDraw.Draw(sheet)
    title = f"OPEN WEAVE / THEME 01 / {set_spec['id'].upper()} CONTACT SHEET"
    draw.text((margin, 52), title, fill=WHITE, font=get_font(30, mono=True))
    for i, path in enumerate(paths):
        row, col = divmod(i, cols)
        x = margin + col * (thumb_w + gap)
        y = margin + title_h + row * (thumb_h + gap)
        img = Image.open(path).convert("RGB")
        img = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(img, (x, y))
    contact_path = ROOT / set_spec["contact_sheet"]
    contact_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(contact_path, quality=95)


def render_set(set_spec: dict) -> list[Path]:
    output_dir = ROOT / set_spec["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    total = len(set_spec["cards"])
    for i, card in enumerate(set_spec["cards"], start=1):
        img = render_card(card, set_spec["width"], set_spec["height"], set_spec["profile"], i, total)
        path = output_dir / card["filename"]
        img.save(path, quality=95)
        paths.append(path)
    make_contact_sheet(set_spec, paths)
    return paths


def main() -> None:
    global CJK_FONT, MONO_FONT
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", dest="set_id", default="all", help="wechat-inline, zhihu-idea, xiaohongshu, or all")
    parser.add_argument("--cjk-font", help="Path to a CJK TrueType or OpenType font")
    parser.add_argument("--mono-font", help="Path to a monospace TrueType or OpenType font")
    args = parser.parse_args()
    CJK_FONT = resolve_font(args.cjk_font, CJK_FONT_CANDIDATES, "cjk")
    MONO_FONT = resolve_font(args.mono_font, MONO_FONT_CANDIDATES, "mono")
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    selected = [item for item in spec["sets"] if args.set_id in ("all", item["id"])]
    if not selected:
        raise SystemExit(f"unknown set: {args.set_id}")
    for item in selected:
        paths = render_set(item)
        print(f"{item['id']}: rendered {len(paths)} cards + contact sheet")


if __name__ == "__main__":
    main()
