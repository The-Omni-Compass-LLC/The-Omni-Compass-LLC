#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The figures of the two manuals, drawn from the book's own code (the founder's order of 16 October, night: flow charts
and illustrations that interpret the language of the mathematics, built into the manuals with the tools at hand).

Every figure is a reportlab drawing, built here from the numbers the engine and the law actually carry
(omnicompass/compass_law.py, omnicompass/core.py, omnicompass/adapter.py), so a figure cannot drift from the code it
pictures. docs/book/build_book.py places a figure where a manual carries the line

    ![caption](book/figures/KEY.svg)

numbers it ("Figure N."), lists it in the List of Figures after the Contents and prints the caption under it. The same
drawings are written as SVG files to docs/book/figures/ so the pages on GitHub show them. None of the founder's plates
(his illustration images) are figures: they stay in docs/book/plates/ as his property, and no chart of a result is drawn.

Type: every label at 11 pt (the founder's prompt rules), words in Liberation Sans, mathematics in DejaVu Sans, which
carries every Greek letter, subscript and dot the equations use.

    python3 docs/book/figures.py            # writes every figure to docs/book/figures/*.svg
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

from reportlab.graphics import renderSVG
from reportlab.graphics.shapes import Circle, Drawing, Group, Line, PolyLine, Polygon, Rect, String
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "book" / "figures"

W = 486.0                               # the text frame of the book, in points (US Letter, 1 in and 0.75 in margins)
PT = 9                                  # every label at 9 pt (the founder's order of 16 October, night: the shells stay,
                                        # the type goes to 9 pt so that no word ever leaves its cell)
NAVY = colors.HexColor("#0b1f3a")
GOLD = colors.HexColor("#a8801f")
RULE = colors.HexColor("#c9b27a")
INK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#666666")
PALE = colors.HexColor("#faf6ec")       # the note tint of the book
BLUE = colors.HexColor("#e8eef7")
MIST = colors.HexColor("#f3f3f1")
RED = colors.HexColor("#8a1f1f")
ROSE = colors.HexColor("#f7e6e6")
GREEN = colors.HexColor("#2e6b3a")
WORDS, BOLD, MATH = "Sans", "Sans-Bold", "Sym"

# The titles the List of Figures prints; a manual's own caption (the line's alt text) is printed under the figure.
FIGURES = {
    "plug": "The two-way plug: one wire out, one wire in",
    "band": "The compass band, its cushions, and the smoothing of the force",
    "loop": "One decision of the governor, from the senses to the audit",
    "levels": "The eight levels of an installation",
    "pedal": "One pedal, no brake: the modes and the two switches",
    "organisms": "The seven organisms on the spine",
    "readings": "The three-run rule: a change of 0.5% or more is a change, STEADY under it, and the runs that disagree",
    "engine": "The engine's six states, their couplings and the control law",
    "potential": "The double well of the alignment and the cubic potential of the stress",
}


def ensure_fonts():
    """The book's fonts, registered once (build_book.py registers them first; run alone, this file does)."""
    if "Sym" in pdfmetrics.getRegisteredFontNames():
        return
    lib, djv = "/usr/share/fonts/truetype/liberation/", "/usr/share/fonts/truetype/dejavu/"
    for name, path in (("Sans", lib + "LiberationSans-Regular.ttf"), ("Sans-Bold", lib + "LiberationSans-Bold.ttf"),
                       ("Serif", lib + "LiberationSerif-Regular.ttf"), ("Mono", djv + "DejaVuSansMono.ttf"),
                       ("Sym", djv + "DejaVuSans.ttf")):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, path))


# ---------------------------------------------------------------- the drawing vocabulary
def text(d, x, y, s, font=WORDS, size=PT, color=INK, anchor="start"):
    d.add(String(x, y, s, fontName=font, fontSize=size, fillColor=color, textAnchor=anchor))


def lines(d, cx, top, rows, font=WORDS, size=PT, color=INK, lead=None, anchor="middle"):
    """Rows of centered text, the first row's baseline `lead` under `top`."""
    lead = lead or size + 3
    for k, row in enumerate(rows):
        f = font
        if isinstance(row, tuple):
            row, f = row
        text(d, cx, top - lead * (k + 1) + 3, row, font=f, size=size, color=color, anchor=anchor)


def box(d, x, y, w, h, rows=(), fill=MIST, stroke=NAVY, width=1.0, dash=None, font=WORDS, color=INK, radius=5):
    d.add(Rect(x, y, w, h, rx=radius, ry=radius, fillColor=fill, strokeColor=stroke, strokeWidth=width,
               strokeDashArray=dash))
    if rows:
        lead = PT + 3
        top = y + h / 2 + lead * len(rows) / 2
        lines(d, x + w / 2, top, rows, font=font, color=color, lead=lead)
    return x, y, w, h


def diamond(d, cx, cy, w, h, rows=(), fill=PALE, stroke=GOLD):
    d.add(Polygon([cx - w / 2, cy, cx, cy + h / 2, cx + w / 2, cy, cx, cy - h / 2], fillColor=fill, strokeColor=stroke,
                  strokeWidth=1.0))
    lead = PT + 3
    lines(d, cx, cy + lead * len(rows) / 2, rows, lead=lead)


def arrow(d, pts, color=NAVY, width=1.0, head=True, dash=None):
    """A polyline through pts with an arrowhead at its end."""
    flat = [c for p in pts for c in p]
    d.add(PolyLine(flat, strokeColor=color, strokeWidth=width, strokeDashArray=dash))
    if head:
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        dx, dy = x2 - x1, y2 - y1
        n = math.hypot(dx, dy) or 1.0
        ux, uy = dx / n, dy / n
        L, Hh = 8.0, 3.6
        bx, by = x2 - L * ux, y2 - L * uy
        d.add(Polygon([x2, y2, bx + Hh * uy, by - Hh * ux, bx - Hh * uy, by + Hh * ux], fillColor=color, strokeColor=color))


def plot_line(d, pts, color=NAVY, width=1.4, dash=None):
    d.add(PolyLine([c for p in pts for c in p], strokeColor=color, strokeWidth=width, strokeDashArray=dash))


def dot(d, x, y, r=3.0, color=GOLD):
    d.add(Circle(x, y, r, fillColor=color, strokeColor=color))


# ---------------------------------------------------------------- the figures
def fig_plug():
    """The plug of omnicompass/compass_law.py: attach (the snapshot), read, write (clipped, read back), one writer, restore."""
    d = Drawing(W, 240)
    box(d, 8, 70, 136, 120, [("THE BRAIN", BOLD), "the compass law,", "one law for every", "muscle; the mathematics", "lives here"],
        fill=BLUE)
    box(d, 342, 70, 136, 120, [("THE MUSCLE", BOLD), "its native controller,", "its knob (the lever),", "its meters", "(the reading)"],
        fill=PALE, stroke=GOLD)
    box(d, 200, 60, 86, 140, [], fill=None, stroke=GREY, dash=[3, 3])
    text(d, 243, 206, "THE PLUG", font=BOLD, color=GREY, anchor="middle")
    # the wire out, the brain's write, and the wire in, the muscle's reading
    arrow(d, [(144, 168), (342, 168)])
    text(d, 243, 177, "wire out: write one value", anchor="middle")
    text(d, 243, 152, "clipped to the cover; read back", color=GREY, anchor="middle")
    arrow(d, [(342, 100), (144, 100)], color=GOLD)
    text(d, 243, 123, "wire in: the reading, and", anchor="middle")
    text(d, 243, 109, "the knob as it stands", anchor="middle")
    text(d, 243, 84, "in its band: 0 calm, 1 the line", color=GREY, anchor="middle")
    # the contract's three rules that make a write safe
    box(d, 10, 8, 150, 42, ["attach: the snapshot, the knob", "read once before any write"], fill=MIST, stroke=GREY)
    box(d, 168, 8, 150, 42, ["restore: back to the snapshot,", "read back, at the end"], fill=MIST, stroke=GREY)
    box(d, 326, 8, 150, 42, ["one writer: a knob moved by", "another hand is left alone"], fill=MIST, stroke=GREY)
    return d


def fig_band():
    """The band of Band (walls at 0.05 and 0.95) and the force of CompassLaw.force: A tanh(raw / A)."""
    d = Drawing(W, 372)
    # (a) the band
    text(d, W / 2, 358, "(a) the service reading placed in its band: the position p, from 0 (calm) to 1 (the line)",
         anchor="middle")
    x0, x1, yb, hb = 50, 450, 298, 26
    d.add(Rect(x0, yb, x1 - x0, hb, fillColor=BLUE, strokeColor=NAVY, strokeWidth=1.0))
    d.add(Rect(x0, yb, 20, hb, fillColor=RULE, strokeColor=None))                     # cushion 0 to 0.05
    d.add(Rect(x1 - 20, yb, 20, hb, fillColor=RULE, strokeColor=None))                # cushion 0.95 to 1
    d.add(Line(250, yb - 4, 250, yb + hb + 4, strokeColor=GOLD, strokeWidth=1.6))      # the centre
    text(d, 60, 332, "cushion 5%", color=GREY, anchor="middle")
    text(d, 440, 332, "cushion 5%", color=GREY, anchor="middle")
    text(d, 250, 332, "the centre c (0.5 by default)", anchor="middle")
    text(d, 70, 282, "wall 0.05", color=GREY, anchor="middle")
    text(d, 430, 282, "wall 0.95", color=GREY, anchor="middle")
    text(d, x0, 268, "0  calm", anchor="start")
    text(d, x1, 268, "1  the line", anchor="end")
    # (b) the force
    text(d, W / 2, 248, "(b) the force F = A·tanh(r/A): a spring near the centre,", font=MATH, anchor="middle")
    text(d, W / 2, 234, "flattening into the authority A far out and never past it", font=MATH, anchor="middle")
    px0, px1, py0, py1 = 60, 450, 48, 220
    cx, cy = (px0 + px1) / 2, (py0 + py1) / 2
    sx, sy = (px1 - px0) / 6.0, (py1 - py0) / 3.0                                     # r in [-3, 3], F in [-1.5, 1.5]
    d.add(Line(px0, cy, px1, cy, strokeColor=GREY, strokeWidth=0.8))
    d.add(Line(cx, py0, cx, py1, strokeColor=GREY, strokeWidth=0.8))
    for F in (1.0, -1.0):
        y = cy + F * sy
        d.add(Line(px0, y, px1, y, strokeColor=RULE, strokeWidth=0.8, strokeDashArray=[4, 3]))
    text(d, px0 + 2, cy + sy - 13, "+A, the authority", font=MATH, color=GREY, anchor="start")
    text(d, px1 - 2, cy - sy + 4, "−A", font=MATH, color=GREY, anchor="end")
    spring = [(cx + r * sx, cy + r * sy) for r in (-1.45, 1.45)]
    plot_line(d, spring, color=GREY, width=0.9, dash=[2, 3])
    text(d, cx + 1.1 * sx + 6, cy + 1.3 * sy, "a plain spring, F = r", font=MATH, color=GREY, anchor="start")
    curve = [(cx + r * sx, cy + math.tanh(r) * sy) for r in [k / 20.0 for k in range(-60, 61)]]
    plot_line(d, curve, color=NAVY, width=1.8)
    text(d, cx + 2.0 * sx, cy + 0.72 * sy, "F = A·tanh(r/A)", font=MATH, color=NAVY, anchor="middle")
    text(d, cx - 1.5 * sx, cy + 1.28 * sy, "the up side, F > 0: add capacity", anchor="middle")
    text(d, cx + 1.5 * sx, cy - 1.38 * sy, "the down side, F < 0: give back", anchor="middle")
    text(d, cx, 28, "the raw force r = K[P]·(p − c) + K[D]·v:", font=MATH, anchor="middle")
    text(d, cx, 12, "the pull to the centre, plus the push against the motion v", font=MATH, anchor="middle")
    return d


def fig_loop():
    """One decision of the live controller: senses, blind-means-hold, the engine, the law, the gate, the verdict, the write,
    the audit; the order of omni_controller/controller.py and the rules of omnicompass/nervous_system.py."""
    d = Drawing(W, 500)                       # 500 pt: with its caption the figure fits a page under a few lines of text
    L, Rr = 60, 340                                                                  # the main column
    cx = (L + Rr) / 2
    wmain = Rr - L

    def step(y, h, rows, fill=MIST):
        box(d, L, y, wmain, h, rows, fill=fill)
        return y

    def down(y_from, y_to):
        arrow(d, [(cx, y_from), (cx, y_to)])

    step(454, 30, ["Wake on the period: a full decision every 60 s,", "the fast checks every 5 s"], fill=BLUE)
    down(454, 444)
    step(414, 30, ["Read every sense: the service gauge, the resource,", "and the knob read back from the device"])
    down(414, 404)
    diamond(d, cx, 382, wmain, 44, ["a sense blind or stale?"])
    down(360, 350)
    step(308, 42, ["The engine: the state blended toward the", "observations and moved one macro step; from it", "the authority, the push and the convergence"])
    down(308, 298)
    step(268, 30, ["The compass law: the reading's position p in its", ("band, and the force F = A·tanh(r/A)", MATH)])
    down(268, 258)
    diamond(d, cx, 236, wmain, 44, [("F > 0: the up side?", MATH)])
    down(214, 204)
    diamond(d, cx, 175, wmain, 58, ["the release gate: calm, the line clean for", "three decisions, nothing pending,", "every sense live?"])
    down(146, 136)
    step(94, 42, ["The verdict on a slow knob: the paired trial at", "the 2% line against the step before; a step", "that costs the work more is refused"])
    down(94, 84)
    step(54, 30, ["Write one value through the plug, clipped to", "the cover; read back what the device took"])
    down(54, 44)
    step(14, 30, ["The audit: every sense, the state, the force, the", "gate's reason, the value sent and the value taken"], fill=BLUE)
    # the right lane: a hold goes straight to the audit, with its reason
    lane = 430
    arrow(d, [(Rr, 382), (lane, 382), (lane, 29), (Rr, 29)], color=GOLD)
    text(d, Rr + 6, 388, "yes: hold", color=GOLD, anchor="start")
    arrow(d, [(Rr, 175), (lane, 175)], color=GOLD, head=False)
    text(d, Rr + 6, 181, "no: hold, reason written", color=GOLD, anchor="start")
    text(d, cx + 6, 352, "no", color=GREY, anchor="start")
    text(d, cx + 6, 206, "no: the down side", color=GREY, anchor="start")
    text(d, cx + 6, 138, "yes", color=GREY, anchor="start")
    # the left lane: the up side is never gated beyond the security hold; it goes straight to the write
    arrow(d, [(L, 236), (30, 236), (30, 69), (L, 69)], color=GREEN)
    text(d, 34, 222, "yes: add at once", color=GREEN, anchor="start")
    # the loop: the audit closes one decision and the next begins
    arrow(d, [(L, 29), (12, 29), (12, 469), (L, 469)], color=GREY, dash=[3, 3])
    text(d, 12, 488, "the next decision", color=GREY, anchor="start")
    return d


def fig_levels():
    """The eight levels of the Operator's Manual, chapter 6, as the manual's own table names them."""
    rows = [
        ("Level 0. Verify the software, touching nothing: python3 verify.py", "pass: VERIFICATION: PASS", False),
        ("Level 1. Watch, read-only: every decision logged, none written", "pass: zero writes, and readings your operators agree with", False),
        ("Level 2. The pods, through your own autoscalers", "pass: p95, p99 and failures never behind native, in paired runs", True),
        ("Level 3. The machines, through the release gate and the verdict", "pass: fewer machines in service, no LOSS on any service gauge", True),
        ("Level 4. The replica decision itself (an option, not a step)", "pass: as level 3", True),
        ("Level 5. A GPU card, two wires: the clock ceiling and the lid", "pass: work per energy up or equal; no request over 2% slower", True),
        ("Level 6. The processor's clock and power on bare metal", "pass: energy per unit of work down, no LOSS on any service gauge", True),
        ("Level 7. The site: site power and the supply-air setpoint", "pass: the site meter down, every rack inlet inside its band", True),
    ]
    rh, gap, bw = 34, 4, 396
    d = Drawing(W, 8 * (rh + gap) + 58)
    for k, (title, passes, writes) in enumerate(rows):
        x = 20 + 10 * k
        y = 36 + k * (rh + gap)
        box(d, x, y, bw, rh, [], fill=BLUE if writes else MIST)
        text(d, x + 8, y + rh - 14, title, font=BOLD, color=NAVY)
        text(d, x + 8, y + 6, passes, color=GREY)
        if writes:
            text(d, x + bw - 6, y + rh - 14, "WRITES", font=BOLD, color=GOLD, anchor="end")
    arrow(d, [(8, 36), (8, 8 * (rh + gap) + 32)], color=GOLD)
    text(d, W / 2, 20, "take them in order: the OFF switch works at every level,", color=GREY, anchor="middle")
    text(d, W / 2, 6, "and the wire check passes before any level that writes", color=GREY, anchor="middle")
    return d


def fig_pedal():
    """One pedal (push, lift off, idle, reset), cruise, watching, off; the kill switch apart, for security only."""
    d = Drawing(W, 262)
    # the pedal's travel
    x0, x1, y, h = 40, 446, 166, 22
    d.add(Rect(x0, y, x1 - x0, h, fillColor=BLUE, strokeColor=NAVY))
    for k in range(1, 8):
        xx = x0 + (x1 - x0) * k / 8
        d.add(Line(xx, y, xx, y + h, strokeColor=colors.white, strokeWidth=1.2))
    arrow(d, [(x0 + 50, y + h / 2), (x1 - 52, y + h / 2)], color=NAVY, width=1.2)
    text(d, x0 + 6, y + 7, "lifted", color=NAVY)
    text(d, x1 - 6, y + 7, "pushed", color=NAVY, anchor="end")
    lines(d, 100, 254, ["IDLE: pedal lifted all", "the way; calm traffic,", "the floor of 2 machines"], lead=14)
    lines(d, 243, 254, ["LIFT OFF: capacity eased", "back toward native, a", "step at a time"], lead=14)
    lines(d, 388, 254, ["PUSH: capacity added at", "once, never held back,", "up to the pool's top"], lead=14)
    for xx in (100, 243, 388):
        arrow(d, [(xx, 206), (xx, y + h + 2)], color=GREY, width=0.8)
    # cruise, a known queue waiting
    box(d, 40, 116, 406, 38, ["CRUISE: work waiting in line for two decisions puts every machine into service,",
                              "held there until the line has been empty for two decisions"], fill=PALE, stroke=GOLD)
    # the modes beside the pedal
    box(d, 40, 54, 128, 52, ["WATCHING: reads every", "gauge, logs its decision,", "writes nothing"], fill=MIST, stroke=GREY)
    box(d, 179, 54, 128, 52, ["RESET: every setting", "handed back to native,", "read back; a run's end"], fill=MIST, stroke=GREY)
    box(d, 318, 54, 128, 52, ["OFF (manual): native", "alone; the native arm", "of every paired run"], fill=MIST, stroke=GREY)
    # the kill switch, apart
    box(d, 40, 6, 406, 38, ["THE KILL SWITCH: security only, one human hand, instant; every governor hands",
                            "back and exits, and none starts while it is off. The end of trust, not of a run."],
        fill=ROSE, stroke=RED, width=1.4)
    return d


def fig_organisms():
    """The seven organisms (the founder's order of 16 October): the spine, the four realms on it, the four stacked, the tower."""
    d = Drawing(W, 276)
    d.add(Rect(18, 42, 450, 200, rx=8, ry=8, fillColor=None, strokeColor=GREY, strokeWidth=1.0, strokeDashArray=[4, 3]))
    text(d, W / 2, 250, "6. The whole tower: 1,107 distinct muscles in 70 families, every muscle once", anchor="middle")
    box(d, 30, 54, 426, 44, [("THE SPINE: 267 muscles, every muscle that sits in all four realms", BOLD),
                             "7. an organism in its own right, listed first: the base every stack runs on"], fill=BLUE)
    realms = [["1. Compute /", "AI / Cloud", "540 muscles"], ["2. Physics /", "Robotics /", "Autonomous", "404 muscles"],
              ["3. Energy /", "Facility /", "Industrial", "480 muscles"], ["4. Distribution", "/ Specialized", "484 muscles"]]
    for k, rows in enumerate(realms):
        x = 30 + k * 109.3
        box(d, x, 106, 98, 96, rows, fill=PALE, stroke=GOLD)
    # the bracket of the four stacked
    d.add(Line(30, 212, 456, 212, strokeColor=NAVY, strokeWidth=1.0))
    d.add(Line(30, 207, 30, 217, strokeColor=NAVY, strokeWidth=1.0))
    d.add(Line(456, 207, 456, 217, strokeColor=NAVY, strokeWidth=1.0))
    text(d, W / 2, 221, "5. The four stacked: 1,908 muscles, the spine once in each realm's body", anchor="middle")
    text(d, W / 2, 22, "every organism runs native and with Omni-Compass on top of native,", color=GREY, anchor="middle")
    text(d, W / 2, 8, "on its own load, on the climb and on the line", color=GREY, anchor="middle")
    return d


def fig_readings():
    """The readings of tools/readings.py (the founder's order of 24 October 2026: a change of 0.5% or more, the mean of the
    three runs, is a change), as three runs' intervals beside the zero line and the floor band of 0.5% either way."""
    d = Drawing(W, 384)
    z, fl = 300.0, 12.0                      # the zero line, and the floor's half width on this scale
    d.add(Rect(z - fl, 34, 2 * fl, 318, fillColor=colors.Color(0.85, 0.87, 0.9), strokeColor=None))
    d.add(Line(z, 34, z, 352, strokeColor=NAVY, strokeWidth=1.0))
    text(d, z, 356, "0: no change; the band: under 0.5% either way", color=NAVY, anchor="middle")
    text(d, z - 8, 370, "the side the gauge's aim calls GAIN", color=GREEN, anchor="end")
    text(d, z + 8, 370, "the side it calls LOSS", color=RED, anchor="start")
    rows = [
        ("GAIN in all three of our runs", [(-80, -30), (-95, -40), (-70, -20)], 314),
        ("GAIN by the mean: beyond the noise in 2 of 3", [(-80, -30), (-60, 20), (-75, -25)], 254),
        ("STEADY, under the floor: the mean under 0.5%", [(-9, 7), (-6, 10), (-10, 5)], 194),
        ("LOSS in all three of our runs", [(30, 80), (45, 95), (20, 70)], 134),
        ("the runs disagree: look into the test", [(-90, -40), (30, 80), (-60, -15)], 74),
    ]
    for label, bars, top in rows:
        text(d, 14, top, label, font=BOLD, color=NAVY)
        for k, (a, b) in enumerate(bars):
            y = top - 13 - 13 * k
            crosses = a < 0 < b
            col = GREY if crosses else (GREEN if b < 0 else RED)
            d.add(Line(z + a, y, z + b, y, strokeColor=col, strokeWidth=1.6))
            d.add(Line(z + a, y - 3, z + a, y + 3, strokeColor=col, strokeWidth=1.2))
            d.add(Line(z + b, y - 3, z + b, y + 3, strokeColor=col, strokeWidth=1.2))
            dot(d, z + (a + b) / 2, y, 2.4, col)
            text(d, 404, y - 4, "ABC"[k] + ("  crosses 0" if crosses else ""), color=GREY, anchor="start")
    text(d, W / 2, 14, "each bar: one run's paired change, Omni-Compass against native, with its 95% interval",
         color=GREY, anchor="middle")
    return d


def fig_engine():
    """The six states of omnicompass/core.py, their main couplings, the control law and what the governor reads from it."""
    d = Drawing(W, 440)
    box(d, 20, 392, 446, 40, ["Nine observations, each clipped to its range: queue, load, power,",
                              "thermal, network, drift, staleness, security, conflict"], fill=BLUE)
    arrow(d, [(243, 392), (243, 330)])
    text(d, 252, 358, "blended into the state, weight a = 0.339", font=MATH, color=GREY)
    bw, bh, gap = 109, 46, 59.5
    xs = (20, 20 + bw + gap, 20 + 2 * (bw + gap))
    y1, y2 = 284, 196
    box(d, xs[0], y1, bw, bh, [("E   the deviation", BOLD), ("drains at α[E]", MATH)])
    box(d, xs[1], y1, bw, bh, [("U   the alignment", BOLD), ("poles ±1, ridge 0", MATH)])
    box(d, xs[2], y1, bw, bh, [("I[U]   the memory", BOLD), ("leaks at λ[I]", MATH)])
    box(d, xs[0], y2, bw, bh, [("S   the stress", BOLD), ("rolls down Φ(S)", MATH)])
    box(d, xs[1], y2, bw, bh, [("B, Ḃ   the bath", BOLD), ("damped, ω[B]/Q[B]", MATH)])
    box(d, xs[2], y2, bw, bh, [("R[B]   the audit", BOLD), ("never fed back", MATH)], fill=None, stroke=GREY, dash=[3, 3])
    # the couplings: the drive of E on U, the need U leaves in the memory, the stress driving the bath, the audit on it
    ym1, ym2 = y1 + bh / 2, y2 + bh / 2
    arrow(d, [(xs[0] + bw, ym1), (xs[1], ym1)])
    text(d, (xs[0] + bw + xs[1]) / 2, ym1 + 5, "dE/dt", font=MATH, color=GREY, anchor="middle")
    arrow(d, [(xs[1] + bw, ym1), (xs[2], ym1)])
    text(d, (xs[1] + bw + xs[2]) / 2, ym1 + 5, "1 − U", font=MATH, color=GREY, anchor="middle")
    arrow(d, [(xs[0] + bw, ym2), (xs[1], ym2)])
    text(d, (xs[0] + bw + xs[1]) / 2, ym2 + 5, "γ[c]·δ·S", font=MATH, color=GREY, anchor="middle")
    arrow(d, [(xs[1] + bw, ym2), (xs[2], ym2)], color=GREY, dash=[3, 3])
    arrow(d, [(xs[0] + 30, y2 + bh), (xs[0] + 30, y1)])
    text(d, xs[0] + 36, (y2 + bh + y1) / 2 - 4, "−δS", font=MATH, color=GREY)
    text(d, xs[0], y1 + bh + 8, "filled by β[int] + β[ext] + v[eff]", font=MATH, color=GREY)
    # the control law and what is read from it
    box(d, 20, 94, 270, 60, [("the control law, every micro step:", WORDS), ("u = clip(−f[U](x, t) + K[P]·(σ − U), ±25)", MATH),
                             ("cancels the drift of U, pulls it to its pole σ", MATH)], fill=PALE, stroke=GOLD)
    arrow(d, [(xs[1] + 24, y1), (xs[1] + 24, 154)], color=GOLD)
    text(d, xs[1] + 30, 166, "u", font=MATH, color=GOLD)
    arrow(d, [(xs[1] + 54, 154), (xs[1] + 54, y1)], color=GOLD)
    text(d, xs[1] + 60, 166, "K[P] = 12", font=MATH, color=GOLD)
    arrow(d, [(290, 124), (304, 124)])
    box(d, 304, 94, 162, 60, ["read, never applied:", ("the push u/25, the", MATH), "authority, release and", "change permitted"], fill=MIST, stroke=GREY)
    arrow(d, [(155, 94), (155, 54)])
    box(d, 20, 12, 446, 42, ["to the nervous system and the compass law on every muscle:", "the force F, the release gate, the verdict, one write through the plug"], fill=BLUE)
    return d


def fig_potential():
    """The alignment's double well, V(U) = μ(U⁴/4 − U²/2), and the stress's cubic potential Φ(S) with the engine's defaults
    (omnicompass/core.py: αₛ = 0.12, βₛ = 0.10, δ = 0.5): the stable root and the ridge are computed, not drawn by eye."""
    d = Drawing(W, 286)
    # (a) the alignment
    text(d, 124, 272, "(a) the alignment U, a double well:", font=MATH, anchor="middle")
    text(d, 124, 256, "V(U) = μ(U⁴/4 − U²/2)", font=MATH, anchor="middle")
    ax, ay, sx, sy = 124, 150, 68, 300
    d.add(Line(ax - 1.5 * sx, ay, ax + 1.5 * sx, ay, strokeColor=GREY, strokeWidth=0.8))
    d.add(Line(ax, ay - 0.27 * sy, ax, ay + 0.08 * sy, strokeColor=GREY, strokeWidth=0.8))
    pts = [(ax + u * sx, ay + (u ** 4 / 4 - u ** 2 / 2) * sy) for u in [k / 50.0 for k in range(-73, 74)]]
    plot_line(d, pts, color=NAVY, width=1.8)
    dot(d, ax - sx, ay - 0.25 * sy); dot(d, ax + sx, ay - 0.25 * sy); dot(d, ax, ay, 2.6, GREY)
    text(d, ax - sx, ay - 0.25 * sy - 16, "−1, the failed pole", font=MATH, anchor="middle")
    text(d, ax + sx, ay - 0.25 * sy - 16, "+1, the healthy pole", font=MATH, anchor="middle")
    text(d, ax, ay + 0.08 * sy + 6, "the ridge at U = 0", font=MATH, color=GREY, anchor="middle")
    text(d, 124, 36, "dU/dt = μU(1 − U²) + …", font=MATH, color=GREY, anchor="middle")
    text(d, 124, 20, "the ball rolls to the nearer pole", font=MATH, color=GREY, anchor="middle")
    # (b) the stress, with the engine's default parameters
    a_s, b_s, dl = 0.12, 0.10, 0.5
    phi = lambda s: 0.5 * a_s * s * s + 0.25 * b_s * s ** 3 - dl * s          # noqa: E731  (the potential of core.py)
    disc = math.sqrt(a_s * a_s + 3.0 * b_s * dl)
    s_root, s_ridge = (-a_s + disc) / (1.5 * b_s), (-a_s - disc) / (1.5 * b_s)
    text(d, 362, 272, "(b) the stress S, a cubic potential:", font=MATH, anchor="middle")
    text(d, 362, 256, "Φ(S) = αₛS²/2 + βₛS³/4 − δS", font=MATH, anchor="middle")
    text(d, 362, 240, "(αₛ 0.12, βₛ 0.10, δ 0.5: the engine's defaults)", font=MATH, color=GREY, anchor="middle")
    bx, by, tx, ty = 372, 110, 20, 45
    d.add(Line(bx - 5.3 * tx, by, bx + 3.7 * tx, by, strokeColor=GREY, strokeWidth=0.8))
    d.add(Line(bx, by - 0.7 * ty, bx, by + 1.55 * ty, strokeColor=GREY, strokeWidth=0.8))
    pts = [(bx + s * tx, by + phi(s) * ty) for s in [k / 25.0 for k in range(-130, 91)]]
    plot_line(d, pts, color=NAVY, width=1.8)
    dot(d, bx + s_root * tx, by + phi(s_root) * ty); dot(d, bx + s_ridge * tx, by + phi(s_ridge) * ty, 3.0, GREY)
    text(d, bx + s_root * tx, by + phi(s_root) * ty - 16, f"the stable root, S = {s_root:.2f}", font=MATH, anchor="middle")
    text(d, bx + s_ridge * tx + 4, by + phi(s_ridge) * ty + 8, f"the ridge, S = −{-s_ridge:.2f}", font=MATH, color=GREY, anchor="start")
    text(d, 362, 36, "dS/dt = −dΦ/dS: S rolls to the stable root;", font=MATH, color=GREY, anchor="middle")
    text(d, 362, 20, "the landscape is open below the ridge", font=MATH, color=GREY, anchor="middle")
    return d


BUILDERS = {"plug": fig_plug, "band": fig_band, "loop": fig_loop, "levels": fig_levels, "pedal": fig_pedal,
            "organisms": fig_organisms, "readings": fig_readings, "engine": fig_engine, "potential": fig_potential}
assert set(BUILDERS) == set(FIGURES)


def drawing(key: str, width: float = W) -> Drawing:
    """The figure `key`, scaled to `width` points (the book's text frame)."""
    ensure_fonts()
    d = BUILDERS[key]()
    if abs(width - W) > 0.5:
        s = width / W
        g = Group(*d.contents)
        g.scale(s, s)
        d.contents = [g]
        d.width, d.height = d.width * s, d.height * s
    d.hAlign = "CENTER"
    return d


# ---------------------------------------------------------------- the SVG files for the pages on GitHub
FAMILIES = {"Sans": "'Liberation Sans', Arial, Helvetica, sans-serif", "Sans-Bold": "'Liberation Sans', Arial, Helvetica, sans-serif",
            "Serif": "'Liberation Serif', 'Times New Roman', serif", "Sym": "'DejaVu Sans', Verdana, sans-serif",
            "Mono": "'DejaVu Sans Mono', Menlo, monospace"}
NOTICE = ("© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, "
          "commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass "
          "requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and "
          "printout carries this notice with LICENSE, NOTICE and DISCLOSURES.md. All patents, copyrights and trademarks filed "
          "in the USA. www.omni-compass.com")


def svg(key: str) -> str:
    s = renderSVG.drawToString(drawing(key))
    s = re.sub(r"<!DOCTYPE svg[^>]*>\s*", "", s, flags=re.S)
    s = re.sub(r"<title>.*?</title>", f"<title>{FIGURES[key]}</title>", s, count=1, flags=re.S)
    s = re.sub(r"<desc>.*?</desc>", "<desc>Drawn by docs/book/figures.py from the code of Omni-Compass.</desc>", s, count=1, flags=re.S)

    def fam(m):
        name = m.group(1)
        weight = " font-weight: bold;" if name.endswith("-Bold") else ""
        return f"font-family: {FAMILIES.get(name, 'sans-serif')};{weight}"
    s = re.sub(r"font-family: ([A-Za-z-]+);", fam, s)
    s = s.replace("<svg ", f"<!-- {NOTICE} -->\n<svg ", 1)
    return s.rstrip() + f"\n<!-- {NOTICE} -->\n"


def write_svgs(out: Path = OUT) -> list[Path]:
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for key in FIGURES:
        p = out / f"{key}.svg"
        p.write_text(svg(key), encoding="utf-8")
        paths.append(p)
    return paths


if __name__ == "__main__":
    for p in write_svgs():
        print(p.relative_to(ROOT))
