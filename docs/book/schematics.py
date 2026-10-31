#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The second figure kit of the two manuals: wiring schematics, control-loop block diagrams, flowcharts, timing diagrams,
state machines, the receipts charted from the tables that hold them, and the grids (the founder's order of 16 October,
night: the Owner's Manual at a thousand pages needs fifty images that interpret the code, the wiring and the receipts,
drawn with another tool so that they do not all look the same; everything drawn before is kept).

Two kits, one pipeline. The schematics, block diagrams, flowcharts and state machines are drawn with schemdraw, in the
grammar of an electrical drawing: the governor as the control unit with its sense terminals (S1, S2, …) and its motor
terminals (M1, M2, …), the plug as the terminal block that carries the system's own command, the native controller and
the muscle (a potentiometer: the setting) as the load, the meters feeding back along one bus, the kill switch drawn as a
switch in the motor bus. The timing diagrams, the charts and the grids are drawn with matplotlib, every number read from
the repository's own files (a table in results/, the catalog, the engine's own code run for a pulse) so that a chart
cannot drift from the receipt it pictures. Every figure is saved as SVG, read into the book through svglib, and written
to docs/book/figures/ for the pages on GitHub.

Type: every label at 9 pt (the founder's order of 16 October, night: the shells stay, the type goes to 9 pt and no word
ever leaves its cell), DejaVu Sans, which carries every Greek letter the equations use. Every line of text in a box is
measured in the type it is set in (matplotlib's own metrics) and wrapped to the box's width less its padding, and every
box takes the height its lines need; a line that still would not fit is reported at build time (OVERFLOWS), never
printed. A drawing is never wider than the text frame (13.5 units of half an inch), so no label is ever shrunk. A
modelled trace (the law or the engine run for the picture) says so in its caption: class S, never a measurement.

    python3 docs/book/schematics.py              # writes every figure of this kit to docs/book/figures/*.svg
    python3 docs/book/schematics.py KEY ...      # only those
"""
from __future__ import annotations

import csv
import io
import math
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                  # noqa: E402
from matplotlib import patches                   # noqa: E402
from matplotlib.ticker import MaxNLocator        # noqa: E402
import schemdraw                                 # noqa: E402
import schemdraw.elements as elm                 # noqa: E402
from schemdraw import dsp, flow                  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "book" / "figures"
sys.path.insert(0, str(ROOT))

W_IN = 6.75                                      # the book's text frame, in inches (486 pt)
FW = 486.0
PT = 9
UNIT = 2.5                                       # schemdraw's element length, in drawing units of half an inch
PPU = 36.0                                       # points in one drawing unit (half an inch)
LH = 0.33                                        # one line of 9 pt type with its lead, in drawing units (11.9 pt)
NAVY, GOLD, RULE, INK, GREY = "#0b1f3a", "#a8801f", "#c9b27a", "#1a1a1a", "#666666"
PALE, BLUE, MIST, ROSE, RED, GREEN, AMBER = "#faf6ec", "#e8eef7", "#f3f3f1", "#f7e6e6", "#8a1f1f", "#2e6b3a", "#b8860b"
# the key's colours on paper (the founder's order of 24 October, everywhere a reading is drawn): GAIN green, STEADY yellow, LOSS red,
# power given blue (Omni-Compass's own colour), native orange
YELLOW, GIVEN_BLUE, NATIVE_ORANGE = "#c9a000", "#2f6db0", "#e0740c"
DJV = "/usr/share/fonts/truetype/dejavu/"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": PT, "svg.fonttype": "none", "axes.titlesize": PT,
                     "axes.labelsize": PT, "xtick.labelsize": PT, "ytick.labelsize": PT, "legend.fontsize": PT,
                     "axes.edgecolor": GREY, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 100, "savefig.dpi": 100,
                     "svg.hashsalt": "omni-compass"})   # the same drawing writes the same file: no random ids
schemdraw.config(fontsize=PT, font="DejaVu Sans", lw=1.2, color=INK)

# ---------------------------------------------------------------- the titles the List of Figures prints
FIGURES = {
    # wiring schematics
    "s_k8s_cluster": "Wiring schematic: Kubernetes in the cluster, levels 2 to 4",
    "s_cloud_machines": "Wiring schematic: a managed cloud cluster, the machines alone",
    "s_pgbouncer": "Wiring schematic: a database behind its connection pooler",
    "s_kafka": "Wiring schematic: a message broker's consumer group",
    "s_redis": "Wiring schematic: a cache's memory ceiling",
    "s_mongo": "Wiring schematic: a database's storage-engine cache",
    "s_mysql": "Wiring schematic: a buffer pool resized online in the server's own chunks",
    "s_gpu": "Wiring schematic: a graphics card, two wires",
    "s_cpu": "Wiring schematic: the machine's frequency governor under the processor's meter",
    "s_site": "Wiring schematic: the data center under the servers",
    "s_sims": "Wiring schematic: three independent simulators, each on its own native controller",
    "s_drones": "Wiring schematic: a drone swarm's cruise override",
    "s_feed": "Wiring schematic: the response-time feed and the line",
    "s_deploy": "Deployment diagram: the governor on a managed cluster",
    "s_sdk": "The muscle SDK's runtime: what happens to one command",
    # control-loop block diagrams
    "c_compass_loop": "Block diagram: the compass law as a closed loop on one muscle",
    "c_engine_loop": "Block diagram: from the observations through the engine to the authority",
    "c_verdict": "Block diagram: the verdict's paired trial around a slow knob, read GAIN, STEADY or LOSS",
    "c_gpu_pair": "Block diagram: the two wires of a card as an antagonist pair",
    "c_authority": "Logic diagram: the nervous system's authority to add and to give back",
    # flowcharts
    "f_wire_check": "Flowchart: the wire check, steps 1 to 4",
    "f_wire_check_b": "Flowchart: the wire check, steps 5 to 7 and the verdict",
    "f_paired_run": "Flowchart: one paired run, native against Omni-Compass on top, the pairs",
    "f_paired_run_b": "Flowchart: one paired run, from the pairs to the three-run table",
    "f_phases": "Flowchart: the implementer's eight phases and their gates",
    "f_release_gate": "Flowchart: the release gate, reasons 1 to 5",
    "f_release_gate_b": "Flowchart: the release gate, reasons 6 to 9 and the release",
    "f_stops": "Flowchart: the three ways a governor stops",
    "f_model_gate": "Flowchart: the model gate before any engine change runs for real",
    "f_reading": "Flowchart: the three-run reading rule, a change of 0.5% or more a change",
    "f_park": "Flowchart: parking and waking a machine in the cloud",
    "f_conductor": "Flowchart: one tick of the grid conductor",
    "f_trial": "Flowchart: the verdict's trial on one step, from the reference to the reading",
    "f_trial_b": "Flowchart: the verdict's trial on one step, from the reading to the step allowed or refused",
    "f_cache_rule": "Flowchart: the direction rule of a cache knob",
    # timing diagrams and modelled traces
    "t_clocks": "Timing diagram: the governor's clocks against the native controllers' own",
    "t_band_step": "Modelled trace: the compass law answering a load step on one muscle",
    "t_lease": "Timing diagram: the hand-back after a reset, a kill and a death",
    "t_bursts": "The load schedules of the cloud sets: two bursts and the real day",
    "t_climb_line": "The three loads: an organism's own load, the climb and the line",
    "t_pedal": "Modelled trace: one pedal over a burst, machines against demand",
    "t_trial": "Timing diagram: a give-back trial from reference to verdict",
    "t_engine": "Modelled trace: the engine's six states answering a pressure pulse",
    "t_force_surface": "Grid: the force over the band position and its rate of change",
    "t_damping": "Curve: the damping gain the law sets from a muscle's response time",
    # receipts charted from the tables
    "r_goldilocks": "Receipt chart: Omni-Compass on top of Goldilocks and the VPA's recommender, the judged rows",
    "r_goldilocks_shown": "Receipt chart: on top of Goldilocks, the rows shown and not judged",
    "r_keda_http": "Receipt chart: Omni-Compass on top of KEDA's HTTP add-on, the judged rows",
    "r_keda_http_shown": "Receipt chart: on top of KEDA's HTTP add-on, the rows shown and not judged",
    "r_keda_cpu": "Receipt chart: Omni-Compass on top of KEDA on the CPU target and requests in flight, the judged rows",
    "r_keda_cpu_shown": "Receipt chart: on top of KEDA on the CPU target and requests in flight, the rows shown and not judged",
    "r_cruisekube": "Receipt chart: Omni-Compass on top of CruiseKube, the judged rows",
    "r_cruisekube_shown": "Receipt chart: on top of CruiseKube, the rows shown and not judged",
    "r_capacity": "Receipt chart: the capacity test at four caps",
    "r_mechanism": "How a receipt came to be: the governor's inputs beside the service's outputs",
    "r_realms": "Receipt chart: the seven organisms under the three loads",
    "r_grid": "Grid chart: the seven organisms at every size and run count, modelled",
    "r_grid_kube": "Grid chart: the seven organisms at every size and run count, with the real cluster inside",
    "r_benefit": "Chart: the benefit sheet, one number per benchmark, the newer half",
    "r_benefit_b": "Chart: the benefit sheet, one number per benchmark, the older half",
    # structure
    "g_catalog": "Grid: the families of the spine and of the Physics / Robotics / Autonomous realm",
    "g_catalog2": "Grid: the families of the Compute / AI / Cloud realm",
    "g_catalog3": "Grid: the families of the Energy / Facility / Industrial realm",
    "g_catalog4": "Grid: the families of the Distribution / Specialized realm",
    "g_pipeline": "Flowchart: from the audit to the receipt, the table and the one number",
    "g_modes": "State machine: the governor's modes",
    "g_gpu_states": "State machine: the two-wire card governor",
    "g_muscle_life": "State machine: the life of one muscle under the plug",
}

ORGANISMS = ("The spine", "Compute / AI / Cloud", "Physics / Robotics / Autonomous", "Energy / Facility / Industrial",
             "Distribution / Specialized", "The four stacked", "The whole tower")
REALM_NAMES = {"compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
               "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized"}


# ---------------------------------------------------------------- the pipeline
def _fonts():
    try:
        from svglib.fonts import register_font
        register_font("DejaVu Sans", DJV + "DejaVuSans.ttf")
        register_font("DejaVu Sans", DJV + "DejaVuSans-Bold.ttf", weight="bold")
        register_font("DejaVu Sans Mono", DJV + "DejaVuSansMono.ttf")
    except Exception:                            # noqa: BLE001  (an older svglib: the standard fonts stand in)
        pass


MAX_H_IN = 6.9                                   # 497 pt: a chart and its caption fit a page under a few lines of text


def mpl_fig(h, **kw):
    """A chart's figure, never taller than a page holds with its caption: the rows are laid out closer, the type stays 9 pt."""
    return plt.figure(figsize=(W_IN, min(h, MAX_H_IN)), constrained_layout=True, **kw)


def fig_svg(fig) -> str:
    buf = io.StringIO()
    fig.savefig(buf, format="svg", metadata={"Date": None})    # no date stamped in: a figure changes only when it does
    plt.close(fig)
    return buf.getvalue()


def sd_svg(d: schemdraw.Drawing) -> str:
    out = d.get_imagedata("svg").decode("utf-8")
    plt.close("all")                             # schemdraw's backend leaves its pyplot figure open; a book draws dozens
    return out


MAX_H = 500.0                                    # the tallest drawing: with its caption it still follows a few lines of text (the frame is 659 pt)


def svg_to_drawing(svg: str, width: float = FW, height: float = MAX_H):
    """The SVG as a reportlab drawing. Every figure is drawn to fit the frame at its natural size, so that its type stays
    at 11 pt; the scaling here is the last guard against a figure that would not fit a page."""
    from svglib.svglib import svg2rlg
    _fonts()
    dr = svg2rlg(io.BytesIO(svg.encode("utf-8")))   # svglib reads bytes: a text SVG with its XML declaration is refused
    s = min(1.0, width / dr.width, height / dr.height)
    if s < 0.999:
        dr.scale(s, s)
        dr.width, dr.height = dr.width * s, dr.height * s
    dr.hAlign = "CENTER"
    return dr


# ---------------------------------------------------------------- shared pieces (schemdraw)
def new_drawing():
    return schemdraw.Drawing(show=False, unit=UNIT, inches_per_unit=0.5)


def wrap(text, n):
    """Lines of at most n characters, broken at spaces (for the charts, whose text matplotlib lays out itself)."""
    out, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return "\n".join(out)


# ---------------------------------------------------------------- text measured in its own type
from matplotlib.font_manager import FontProperties   # noqa: E402
from matplotlib.textpath import TextToPath           # noqa: E402
_T2P = TextToPath()
_PROP = FontProperties(family="DejaVu Sans", size=PT)
OVERFLOWS: list = []                             # (line, width allowed): a word that no wrapping could fit; must be empty


def tw(s: str) -> float:
    """The width of one line of PT-point DejaVu Sans, in drawing units."""
    return _T2P.get_text_width_height_descent(s, _PROP, ismath=False)[0] / PPU


def wrapw(text: str, width: float) -> str:
    """The text in lines no wider than width drawing units, measured in the type they are set in; line breaks already
    in the text are kept. A single word wider than the width is kept whole and reported in OVERFLOWS."""
    out = []
    text = re.sub(r"(\d) (s|ms|MB|GB|W|m|MHz|°C|pp|pairs|cores|decisions|repetitions)\b", "\\1\u00a0\\2", text)   # a number keeps its unit
    for para in text.split("\n"):
        cur = ""
        for word in para.split():
            cand = (cur + " " + word).strip()
            if cur and tw(cand) > width:
                out.append(cur); cur = word
            else:
                cur = cand
        out.append(cur)
    for ln in out:
        if tw(ln) > width + 1e-6:
            OVERFLOWS.append((ln, round(width, 2)))
    return "\n".join(out)


def fit(text, w, pad=0.5):
    """The text re-wrapped to a box w units wide, less the padding (a quarter unit each side by default)."""
    return wrapw(text, w - pad)


def lines_of(text):
    return text.count("\n") + 1


def hfor(text, w, pad=0.5, extra=0.34):
    """The height a box needs for its fitted text."""
    return lines_of(fit(text, w, pad)) * LH + extra


def box(d, x, y, w, h, text, fill=MIST, color=NAVY, lw=1.2, ls="-", size=PT, tcolor=INK, pad=0.5):
    """A rectangle with its lower-left corner at (x, y), its text fitted to its width; drawn as a flow box so that it
    carries anchors (N, S, E, W, the corners)."""
    b = flow.Box(w=w, h=h).at((x + w / 2, y + h / 2)).anchor("center").fill(fill).color(color).linewidth(lw).linestyle(ls)
    if text:
        b.label(fit(text, w, pad), fontsize=size, color=tcolor)
    d += b
    return b


def text_at(d, x, y, text, color=GREY, halign="left", valign="top", size=PT):
    d += elm.Label().at((x, y)).label(text, fontsize=size, halign=halign, valign=valign, color=color)


def arrow(d, a, b, color=NAVY, shape="-", label=None, loc="top", ls="-", head="->"):
    w = elm.Wire(shape, arrow=head).at(a).to(b).color(color).linestyle(ls)
    if label:
        w.label(label, loc=loc, fontsize=PT, color=color)
    d += w
    return w


def line(d, a, b, color=NAVY, ls="-"):
    d += elm.Line().at(a).to(b).color(color).linestyle(ls)


def notes(d, x, y, text, width=11.8, color=GREY):
    text_at(d, x, y, wrapw(" ".join(text) if isinstance(text, (list, tuple)) else text, width), color=color)


def wiring_schematic(senses, motors, adapter_lines, native, muscle, meters, notes_text, switch="the kill switch",
                     title="THE GOVERNOR", cover=None, inside=None):
    """One grammar for every stack, read top to bottom as an electrical drawing: the governor (the control unit) with its
    sense terminals S1… on the left and its motor terminals M1… on its lower edge; the motor bus through the kill switch
    into the plug (the system's own command); the plug into the native controller; the native controller setting the
    muscle (a potentiometer); the system under native carrying the meters; the meters back along one bus (the wire in)
    to the sense terminals. The audit beside the governor; the snapshot and the restore inside the plug."""
    d = new_drawing()
    L, R = 0.4, 12.3
    gx0, gx1 = 5.9, 8.9                                   # the governor
    ax0, ax1 = 9.5, R                                     # the audit
    sw_w = gx0 - 0.7 - L                                  # the sense boxes
    # the sense rows
    rows = []
    y = 0.0
    for k, s in enumerate(senses):
        t = f"S{k + 1}   {s}"
        h = hfor(t, sw_w, extra=0.28)
        rows.append((t, y - h, h))
        y -= h + 0.25
    zone = -y - 0.25
    # the release gate is the machine organ's (omnicompass/nervous_system.py node_release_gate): only the machine schematics
    # name it; every other muscle gives back under its own give-back rule and the verdict
    gov_text = title + "\n" + (inside or "the compass law · the verdict · the give-back rule · one decision a period")
    gov_h = max(zone, hfor(gov_text, gx1 - gx0))
    gov_bot = -gov_h
    box(d, gx0, gov_bot, gx1 - gx0, gov_h, gov_text, fill=BLUE, color=NAVY)
    ys = []
    for t, y1, h in rows:
        box(d, L, y1, sw_w, h, t, fill=MIST, color=GREEN, pad=0.4)
        yc = y1 + h / 2
        arrow(d, (L + sw_w, yc), (gx0, yc), color=GREEN)
        ys.append(yc)
    audit_text = "AUDIT\naudit.jsonl: one record a decision, every write with its reason and its read-back"
    box(d, ax0, -max(gov_h, hfor(audit_text, ax1 - ax0)), ax1 - ax0, max(gov_h, hfor(audit_text, ax1 - ax0)), audit_text,
        fill=MIST, color=GREY)
    arrow(d, (gx1, -0.6), (ax0, -0.6), color=GREY)
    text_at(d, L, -zone - 0.12, wrapw("the wire in: every meter read live from the system, never a number written in code", gx0 - 0.8 - L), GREEN)
    # the motor terminals and their bus through the kill switch
    m = len(motors)
    xs = [gx0 + 0.5 + k * (gx1 - gx0 - 1.0) / (m - 1) for k in range(m)] if m > 1 else [(gx0 + gx1) / 2]
    bus_y = gov_bot - 0.5
    for k, x in enumerate(xs):
        d += elm.Dot(radius=0.09).at((x, gov_bot)).color(NAVY)
        text_at(d, x + 0.1, gov_bot - 0.02, f"M{k + 1}", NAVY, valign="top")
        line(d, (x, gov_bot), (x, bus_y))
    if m > 1:
        line(d, (xs[0], bus_y), (xs[-1], bus_y))
    cx = (gx0 + gx1) / 2
    plug_top = bus_y - 1.3
    d += elm.Switch().at((cx, bus_y)).to((cx, plug_top)).color(RED)
    text_at(d, cx + 0.4, (bus_y + plug_top) / 2 + 0.05, wrapw(f"{switch}: open, every setting handed back at once; for security only", R - cx - 0.6), RED, valign="center")
    # the plug
    motor_line = "   ".join(f"M{k + 1} {mo}" for k, mo in enumerate(motors))
    plug_text = ("THE PLUG, the wire out: the system's own command, written and read back\n" + motor_line + "\n"
                 + "\n".join(adapter_lines) + "\nsnapshot once at attach; every setting restored to it on stop, read back")
    plug_h = hfor(plug_text, R - L, pad=0.4)
    plug = box(d, L, plug_top - plug_h, R - L, plug_h, plug_text, fill=PALE, color=GOLD, pad=0.4)
    plug_bot = plug_top - plug_h
    # the native controller and the muscle
    nw = 5.6
    nat_text = "NATIVE CONTROLLER\n" + native
    nat_h = max(1.3, hfor(nat_text, nw))
    nat_top = plug_bot - 0.7
    nat = box(d, L, nat_top - nat_h, nw, nat_h, nat_text, fill=MIST, color=NAVY)
    arrow(d, (L + nw / 2, plug_bot), (L + nw / 2, nat_top), color=NAVY)
    text_at(d, L + nw / 2 + 0.15, (plug_bot + nat_top) / 2, "write · read back", NAVY, valign="center")
    nat_mid = nat_top - nat_h / 2
    ym = nat_mid - 1.25
    pot = elm.Potentiometer().at((7.6, ym)).right().color(NAVY).label(muscle, loc="bottom", fontsize=PT)
    d += pot
    d += elm.Wire("-|", arrow="->").at((L + nw, nat_mid)).to(pot.tap).color(NAVY)
    text_at(d, L + nw + 0.15, nat_mid + 0.08, "the setting", NAVY, valign="bottom")
    ct = wrapw("THE MUSCLE  ·  " + (cover or "its own cover"), R - 0.4 - 5.0)
    cover_lines = lines_of(ct)
    text_at(d, 5.0, ym - 0.9, ct, GREY, valign="top")
    # the system under native, with its meters; the wire back
    sys_top = min(ym - 0.9 - LH * cover_lines - 0.3, nat_top - nat_h - 0.5)
    sys_text = "THE SYSTEM UNDER NATIVE  ·  the meters it carries, the wire in:\n" + "\n".join("•  " + mt for mt in meters)
    sys_h = hfor(sys_text, R - L, pad=0.4)
    box(d, L, sys_top - sys_h, R - L, sys_h, sys_text, fill="#f7f9fc", color=GREY, ls="--", pad=0.4)
    d += elm.Wire("-|", arrow="->").at(pot.end).to((R - 0.2, sys_top)).color(NAVY)
    sys_mid = sys_top - sys_h / 2
    d += elm.Wire("-|").at((L, sys_mid)).to((0.0, ys[0])).color(GREEN)
    for yc in ys:
        arrow(d, (0.0, yc), (L, yc), color=GREEN)
    # notes_text is not drawn: the figure's caption carries it (CAPTION_NOTES), so that the tallest stacks fit a page
    return sd_svg(d)


CAPTION_NOTES = {
    "s_k8s_cluster": "Level 2: the target and the floor; level 3: the machines through the release gate and the verdict; level 4 "
                     "(--strict-replicas): the replica decision itself. The HPA keeps its own 15-second check underneath. Nothing is ever "
                     "deleted or evicted; a parked machine is emptied by the autoscaler's own scale-down.",
    "s_cloud_machines": "A machine is parked only after its own trial (the response time holds within 2%) and woken on a breach: at the next "
                        "decision (60 s) for a response time over the line, at the next fast check (5 s) for a waiting pod. No cloud credential: "
                        "the governor holds a Kubernetes service account that can read, taint and annotate, nothing more.",
    "s_pgbouncer": "Up: a server for every percent of clients waiting; down: one idle server, only while clients waited under 1%; at 95% of "
                   "the line the pool goes back to the pooler's own setting at once. One writer; the restore read back at the end.",
    "s_kafka": "Slow with messages waiting: consumers added in proportion to the force; calm with nothing waiting: one idle consumer given "
               "back a second after a five-second dwell; at 95% of the line every consumer the topic can use. The rebalance every move "
               "costs is paid by Omni-Compass and counted in the gauges.",
    "s_redis": "Misses grow the ceiling only while the cache is full (used ≥ 90% of the ceiling); calm with nothing evicted gives one notch "
               "back a second after a five-second dwell; at 95% of the line with the cache full, a quarter of the cover.",
    "s_mongo": "Grow only while the cache is full (≥ 90%) and missing (pages read in ≥ 1% of pages requested); give one notch back after a "
               "five-second dwell only while the miss share is under 1%; at 95% of the line with the cache full, a quarter of the cover.",
    "s_mysql": "The server resizes on its own time: the plug waits for the resize before reading back, and the dwell after a move is ten "
               "seconds; the hand-back waits for the server too, writes again if ignored, and records what it waited for.",
    "s_gpu": "Learns the card on its own first (15 busy readings); races while work waits (≥ 95% utilization); at the max never below the "
             "top while the card serves; at the tune-down paces the slack in 15 MHz steps, each step through the paired trial.",
    "s_cpu": "Every notch down is tried on the machine first: eight cost samples at the deepest notch allowed and eight one further, "
             "allowed only if package power × latency / work inside the line does not rise within 2%. A snapshot of every policy, restored "
             "exactly.",
    "s_site": "Warmer while every reading is cool, colder as heat rises; a step allowed only where the paired trial at the site meter shows "
              "the site's energy no higher for the same work, every inlet inside its band and no LOSS on any service gauge. A reserve held "
              "for an outage (the UPS) is never a lever. Modelled today (class S); no live facility has run yet.",
    "s_drones": "With slack the compass spends it as speed; as the error grows it eases; at 95% of the safe error the planner's cruise at "
                "once. The separation wall: a drone within 0.5 m of another flies the planner's cruise whatever the error reads. A "
                "collision voids the cell.",
}


# ---------------------------------------------------------------- the wiring schematics
def s_k8s_cluster():
    return wiring_schematic(
        senses=["p95, the feed", "pending pods", "HPA replicas", "nodes, host busy"],
        motors=["HPA target", "replica floor", "pod CPU limit", "node pool size"],
        adapter_lines=["kubectl patch hpa … (the target, inside its cover)", "kubectl patch deploy … (the floor)",
                       "kubectl patch pods/resize … (the limit, under the quota)", "bash scripts/kind_nodepool.sh {n}"],
        native="the HPA (15 s), the scheduler, the cluster autoscaler",
        muscle="the pods and the machines", cover="covers: target [0.6·x[op], x[op]]; floor ≥ the operator's; limit ≤ the quota; machines [2, M]",
        meters=["metrics-server: CPU used, allocatable", "the feed: latency.csv, 60 s window", "the API: pods pending, HPA state"],
        inside="the compass law · the verdict · the release gate (the machines) · one decision a period",
        notes_text=["Level 2: the target and the floor; level 3: the machines through the release gate and the verdict;",
                    "level 4 (--strict-replicas): the replica decision itself. The HPA keeps its own 15-second check underneath.",
                    "Nothing is ever deleted or evicted; a parked machine is emptied by the autoscaler's own scale-down."])


def s_cloud_machines():
    return wiring_schematic(
        senses=["p95, the probe's feed", "pending pods", "nodes in service"],
        motors=["park: taint PreferNoSchedule", "wake: remove the taint", "pod-deletion-cost"],
        adapter_lines=["--mode nodepool --law compass --dial save --sensed none/none (no HPA moved) --give-back-only",
                       "--node-scale-cmd \"bash /app/scripts/kind_nodepool.sh {n}\"",
                       "--min-nodes 2 --max-node-step 1 --interval 60 --floor-interval 5"],
        native="the cloud's cluster autoscaler and every HPA, untouched",
        muscle="the work pool's machines (omni-role=work)", cover="cover: [2, the pools' autoscaler maxima]; one machine a decision; never asks the cloud for one",
        meters=["the probe: real requests every 5 s → latency.csv", "the API: pods pending (every 5 s)", "the bill: every machine that exists, every 15 s"],
        notes_text=["A machine is parked only after its own trial (the response time holds within 2%) and woken on a breach:",
                    "at the next decision (60 s) for a response time over the line, at the next fast check (5 s) for a waiting pod.",
                    "No cloud credential: the governor holds a Kubernetes service account that can read, taint and annotate, nothing more."],
        title="THE GOVERNOR, cloud mode", inside="the compass law · the verdict · the release gate · one decision a period")


def s_pgbouncer():
    return wiring_schematic(
        senses=["server time + wait, per transaction", "clients waiting for a server"],
        motors=["default_pool_size"],
        adapter_lines=["one admin connection held open; SHOW STATS, SHOW POOLS every second", "SET default_pool_size = n"],
        native="PgBouncer, as the operator runs it",
        muscle="the pool of server connections", cover="cover: [2, 90], never within ten of PostgreSQL's connection limit; reading held at 40% of a 50 ms line",
        meters=["SHOW STATS: the time per transaction", "SHOW POOLS: cl_waiting, sv_idle"],
        notes_text=["Up: a server for every percent of clients waiting; down: one idle server, only while clients waited under 1%;",
                    "at 95% of the line the pool goes back to the pooler's own setting at once. One writer; restore read back at the end."])


def s_kafka():
    return wiring_schematic(
        senses=["end-to-end latency, 1 s mean", "messages waiting"],
        motors=["consumers in the group"],
        adapter_lines=["each message carries its production time; the group's own records: lag, members", "start or stop one consumer"],
        native="the broker and the group's own rebalance",
        muscle="the consumer count", cover="cover: [1, partitions] (eight); the reading held at 40% of a 500 ms line, response time 3 s",
        meters=["consumed in the last second (handled − produced)", "the topic's lag"],
        notes_text=["Slow with messages waiting: consumers added in proportion to the force; calm with nothing waiting: one idle",
                    "consumer given back a second after a five-second dwell; at 95% of the line every consumer the topic can use.",
                    "The rebalance every move costs is paid by Omni-Compass and counted in the gauges."])


def s_redis():
    return wiring_schematic(
        senses=["request latency, 1 s mean", "memory used, evictions"],
        motors=["maxmemory"],
        adapter_lines=["CONFIG GET maxmemory; INFO memory", "CONFIG SET maxmemory <bytes>"],
        native="Redis with allkeys-lru, as Ubuntu ships it",
        muscle="the memory ceiling", cover="cover: [16, 512] MB in notches of 8 MB; the reading held at 40% of a 2 ms line",
        meters=["the application's own request latency", "INFO: used_memory, evicted_keys"],
        notes_text=["Misses grow the ceiling only while the cache is full (used ≥ 90% of the ceiling); calm with nothing evicted",
                    "gives one notch back a second after a five-second dwell; at 95% of the line with the cache full, a quarter of the cover."])


def s_mongo():
    return wiring_schematic(
        senses=["read latency, 1 s mean", "cache: bytes, pages read in / requested"],
        motors=["wiredTiger cache_size"],
        adapter_lines=["serverStatus: opLatencies, wiredTiger.cache", "setParameter wiredTigerEngineRuntimeConfig cache_size=<MB>"],
        native="MongoDB, as its publisher ships it",
        muscle="the storage-engine cache", cover="cover: [256, 2,048] MB in notches of 64 MB; the line on the stack's own figures (1 ms), held at 40%",
        meters=["serverStatus.opLatencies (differenced)", "bytes currently in the cache; pages read into it"],
        notes_text=["Grow only while the cache is full (≥ 90%) and missing (pages read in ≥ 1% of pages requested); give one notch back",
                    "after a five-second dwell only while the miss share is under 1%; at 95% of the line with the cache full, a quarter of the cover."])


def s_mysql():
    return wiring_schematic(
        senses=["statement latency, 1 s mean", "pool: read requests, reads from disk"],
        motors=["innodb_buffer_pool_size"],
        adapter_lines=["performance_schema: the statement summary", "SET GLOBAL innodb_buffer_pool_size = <chunks × 128 MB>",
                       "wait on Innodb_buffer_pool_resize_status before the read-back"],
        native="MySQL (InnoDB), as its distribution ships it",
        muscle="the buffer pool, in 128 MB chunks", cover="cover: [128, 2,048] MB, whole chunks; the line on the stack's own figures (0.6 ms), held at 40%",
        meters=["events_statements_summary (differenced)", "Innodb_buffer_pool_reads / read_requests"],
        notes_text=["The server resizes on its own time: the plug waits for the resize before reading back, and the dwell after a move is",
                    "ten seconds; the hand-back waits for the server too, writes again if ignored, and records what it waited for."])


def s_gpu():
    return wiring_schematic(
        senses=["utilization, draw, temperature", "clocks, the top clock", "p95 and service_ms, the feed"],
        motors=["clock ceiling (-lgc)", "power limit (-pl)"],
        adapter_lines=["nvidia-smi --query-gpu=… every 2 s", "nvidia-smi -i 0 -lgc <floor>,<ceiling>", "nvidia-smi -i 0 -pl <W>; -rgc on restore"],
        native="the card's firmware: its boost and its power limiter",
        muscle="the two wires of one card", cover="covers: the clock range and the power range read from the card; never under its own busy clock or busy draw",
        meters=["nvidia-smi: utilization, power.draw, temperature", "clocks.sm, clocks.max.sm; the enforced limit", "the workload's latency.csv with service_ms"],
        notes_text=["Learns the card on its own first (15 busy readings); races while work waits (≥ 95% utilization); at the max never below",
                    "the top while the card serves; at the tune-down paces the slack in 15 MHz steps, each step through the paired trial."],
        title="THE CARD GOVERNOR")


def s_cpu():
    return wiring_schematic(
        senses=["service latency, 1 s mean", "package watts (RAPL)"],
        motors=["scaling_max_freq, every CPU"],
        adapter_lines=["/sys/devices/system/cpu/cpufreq/policy*/scaling_max_freq (the ceiling, written)", "--rapl-cmd \"<prints package watts>\""],
        native="the kernel's frequency governor (schedutil) under the ceiling",
        muscle="the clock ceiling of every CPU", cover="cover: the governor's own range; notches of 5% of the top clock; the line 20 ms, held at 40%",
        meters=["the service's own latency", "RAPL energy counter, microjoules"],
        notes_text=["Every notch down is tried on the machine first: eight cost samples at the deepest notch allowed and eight one further,",
                    "allowed only if package power × latency / work inside the line does not rise within 2%. Snapshot of every policy, restored exactly."])


def s_site():
    return wiring_schematic(
        senses=["site watts", "rack inlets, supply and return air", "the services' lines"],
        motors=["supply-air setpoint"],
        adapter_lines=["--power-cmd \"<prints site watts>\" --site-limit-w <W>", "--cooling-cmd \"<sets {c}>\"",
                       "--cooling-min-c 18 --cooling-max-c 27 --cooling-restore-c 22"],
        native="the building management system and the cooling units' own loops",
        muscle="the supply-air setpoint", cover="cover: the operator's band inside the equipment's ratings (ASHRAE 18 to 27 °C); site power is read, never set",
        meters=["the site meter (watts)", "the BMS points: inlets, supply, return, chilled water"],
        notes_text=["Warmer while every reading is cool, colder as heat rises; a step allowed only where the paired trial at the site meter",
                    "shows the site's energy no higher for the same work, every inlet inside its band and no LOSS on any service gauge.",
                    "A reserve held for an outage (the UPS) is never a lever. Modelled today (class S); no live facility has run yet."])


def s_sims():
    d = new_drawing()
    L, R = 0.4, 12.3
    box(d, 4.2, -2.0, 6.0, 2.0, "THE GOVERNOR, one plug each\nthe compass law · the verdict · one decision a period", fill=BLUE, color=NAVY)
    rows = [("CityLearn: the simulator's rule-based control of each building", "each building's battery, inside its own limits (charge, discharge)", "one knob a building"),
            ("pandapower on SimBench: the tap changer holding 1.00 p.u.", "the tap position: one whole tap per move; a week of evidence before a step down", "one knob a substation"),
            ("MuJoCo Menagerie: the shipped joint controllers", "the speed of an axis with slack; an axis at its takt stays native", "one knob an axis")]
    bus_x = 6.65
    y = -2.8
    ys = []
    for nat, knob, cover in rows:
        nt = "NATIVE: " + nat
        kt = "THE KNOB: " + knob + "\n" + cover
        h = max(hfor(nt, 5.8), hfor(kt, R - 6.9))
        box(d, L, y - h, 5.8, h, nt, fill=MIST, color=NAVY)
        box(d, 6.9, y - h, R - 6.9, h, kt, fill=PALE, color=GOLD)
        yc = y - h / 2
        arrow(d, (bus_x, yc), (6.9, yc), color=NAVY)
        ys.append(yc)
        y -= h + 0.5
    line(d, (bus_x, -2.0), (bus_x, ys[-1]))
    text_at(d, bus_x + 0.1, -2.1, wrapw("the plug: the one setting the simulator accepts", R - bus_x - 0.3), NAVY, valign="top")
    d += elm.Wire("-|").at((L, ys[-1])).to((0.05, -1.0)).color(GREEN)
    arrow(d, (0.05, -1.0), (4.2, -1.0), color=GREEN)
    text_at(d, 0.1, -1.15, wrapw("the senses: battery SOC and demand; bus voltage and loading; tracking error and takt", 3.9), GREEN, valign="top")
    notes(d, L, y + 0.1, "The simulator's own controller is native in every cell; the plug writes the one setting it accepts, reads it back and "
                          "restores it at the end. Receipts are class S: statements about the simulator's model, never about hardware.")
    return sd_svg(d)


def s_drones():
    return wiring_schematic(
        senses=["tracking error, per drone", "distance to the nearest drone"],
        motors=["cruise override, per drone"],
        adapter_lines=["gym-pybullet-drones: the shipped position controller on the planner's path",
                       "the carrot's speed as a fraction of the planner's cruise, moved by at most 0.01 a control tick"],
        native="the autopilot's own position controller on the planner's path",
        muscle="the cruise override of one drone", cover="cover: [1.0, 2.0] × the planner's cruise (never over a quarter of the autopilot's speed limit); the band 0 to 0.25 m",
        meters=["the error between the drone and its commanded point", "the separation to every other drone"],
        notes_text=["With slack the compass spends it as speed; as the error grows it eases; at 95% of the safe error the planner's cruise at once.",
                    "The separation wall: a drone within 0.5 m of another flies the planner's cruise whatever the error reads. A collision voids the cell."])


def s_feed():
    d = new_drawing()
    h1 = 1.9
    svc = box(d, 0.4, -h1, 3.2, h1, "THE SERVICE at its cluster URL, behind its load balancer", fill=MIST, color=NAVY)
    probe = box(d, 4.65, -h1, 3.3, h1, "THE PROBE latency_probe.py: N=5 requests every 5 s, 10 s timeout", fill=PALE, color=GOLD)
    csvb = box(d, 9.0, -h1, 3.3, h1, "latency.csv: elapsed_seconds, latency_ms, ok; one row a response", fill=MIST, color=GREY)
    arrow(d, svc.E, probe.W, label="HTTP", color=NAVY)
    arrow(d, probe.E, csvb.W, label="rows", color=NAVY)
    y2, h2 = -3.4, 2.6
    gov = box(d, 9.0, y2 - h2, 3.3, h2, "THE GOVERNOR reads the last 60 s for its decision, the last 15 to 30 s for its fast checks, by the feed's own clock", fill=BLUE, color=NAVY)
    arrow(d, csvb.S, gov.N, color=NAVY)
    text_at(d, csvb.S.x + 0.15, (csvb.S.y + gov.N.y) / 2, "--latency-file", NAVY, valign="center")
    lin = box(d, 4.65, y2 - h2, 3.3, h2, "THE LINE, --slo-ms: the service owner's; read against the 95th percentile, the mean held in the band below it", fill=PALE, color=GOLD)
    arrow(d, lin.E, gov.W, color=NAVY)
    # omni_controller/muscles.py latency_window(): blind = the newest row older than twice the window, or no served
    # response in it; the controller then reads the position as past the wall (fail up) and gives nothing back
    blind = box(d, 0.4, y2 - h2, 3.2, h2, "BLIND: no row for twice the window, or no served response: read as past the wall; "
                                           "nothing given back, capacity added (the cloud mode: every parked machine woken)", fill=ROSE, color=RED)
    yb = y2 - h2 - 0.5
    line(d, gov.S, (gov.S.x, yb), RED); line(d, (gov.S.x, yb), (blind.S.x, yb), RED); arrow(d, (blind.S.x, yb), blind.S, color=RED)
    text_at(d, 4.65, yb - 0.1, wrapw("the safe direction: a broken feed costs savings, never service", 7.5), RED, valign="top")
    notes(d, 0.4, yb - 1.0, "Feed two: the service's own timings (an ingress, a mesh, the application's histogram) written in the same three "
                            "columns, measured at the same place as the line, never pre-smoothed. One feed for one governor.")
    return sd_svg(d)


def s_deploy():
    d = new_drawing()
    # the namespace with the one Deployment, and the pod inside it
    box(d, 0.4, -9.5, 9.0, 9.5, "", fill="#f7f9fc", color=NAVY, ls="--")
    text_at(d, 0.55, -0.2, wrapw("namespace omni-compass · service account omni-compass · one Deployment, one replica (the one writer), strategy Recreate", 8.6),
            NAVY, valign="top")
    box(d, 0.7, -9.2, 8.4, 8.1, "", fill="white", color=GREY)
    text_at(d, 0.85, -9.15, wrapw("the pod: UID 10001, read-only root filesystem, no capabilities, on the system pool (omni-role=system)", 8.0),
            GREY, valign="bottom")
    ctr = box(d, 0.9, -3.5, 4.0, 1.8, "controller\n--mode nodepool --law compass --dial save --give-back-only --dry-run (first)", fill=BLUE, color=NAVY)
    prb = box(d, 0.9, -5.6, 4.0, 1.8, "probe\nlatency_probe.py: real requests every 5 s to the service's URL", fill=PALE, color=GOLD)
    wdg = box(d, 0.9, -7.9, 4.0, 1.8, "watchdog\nomni_switch.py watchdog: the lease, the restore if the governor dies", fill=MIST, color=GREY)
    va = box(d, 5.3, -3.2, 3.4, 1.2, "volume audit\n/var/log/omni/\naudit.jsonl", fill=MIST, color=GREY)
    vf = box(d, 5.3, -5.3, 3.4, 1.2, "volume feed\n/feed/latency.csv", fill=MIST, color=GREY)
    vt = box(d, 5.3, -7.6, 3.4, 1.2, "volume tmp\n/tmp/omni.kill", fill=MIST, color=GREY)
    line(d, ctr.E, va.W, GREY); line(d, prb.E, vf.W, GREY); line(d, wdg.E, vt.W, GREY)
    line(d, (4.9, prb.E.y + 0.4), (5.1, prb.E.y + 0.4), GREY); line(d, (5.1, prb.E.y + 0.4), (5.1, va.S.y), GREY)
    line(d, (4.9, wdg.E.y + 0.4), (5.1, wdg.E.y + 0.4), GREY); line(d, (5.1, wdg.E.y + 0.4), (5.1, vt.N.y), GREY)
    # outside: the API server, the service, the work pools
    api = box(d, 9.8, -2.4, 3.0, 2.0, "THE API SERVER\nget, list; patch nodes, patch pods: nothing else", fill=MIST, color=NAVY)
    svc = box(d, 9.8, -6.7, 3.0, 2.0, "THE SERVICE and its HPA, untouched in the cloud mode", fill=MIST, color=NAVY)
    pools = box(d, 9.8, -9.5, 3.0, 2.3, "THE WORK POOLS, omni-role=work, under the cloud's own autoscaler: tainted, untainted, pods marked first to go", fill=PALE, color=GOLD)
    d += elm.Wire("|-", arrow="->").at(ctr.N).to(api.W).color(NAVY)
    text_at(d, 5.2, api.W.y - 0.08, "one kubectl proxy", NAVY, valign="top")
    d += elm.Wire("|-", arrow="->").at(prb.S).to(svc.W).color(GOLD)
    text_at(d, 5.4, svc.W.y - 0.1, "HTTP, every 5 s", GOLD, valign="top")
    line(d, api.E, (13.2, api.E.y)); line(d, (13.2, api.E.y), (13.2, pools.E.y)); arrow(d, (13.2, pools.E.y), pools.E, color=NAVY)
    notes(d, 0.4, -9.9, "No cloud credential in the pod; the cloud makes and deletes machines with its own identity. The governor talks to one "
                        "endpoint, the API server, and sends nothing off the cluster.")
    return sd_svg(d)


def s_sdk():
    d = new_drawing()
    steps = ["observe() fresh? stale → blind, no write", "the automation mode: disabled, recommend or manual write nothing; external approval waits for it", "clamp to the capability: cover, step, rate, resolution",
             "the safety contract: hard bounds, forbidden keys", "hold and cooldown since the last write", "snapshot_native() once, before the first write",
             "execute(value): the system's own command", "readback() from the system; the residual recorded"]
    bw, bh, gap = 3.0, 1.75, 0.2
    boxes = []
    for k, s in enumerate(steps):
        row, col = divmod(k, 4)
        x = 0.4 + col * (bw + gap)
        y = -(row * (bh + 1.0)) - bh
        fill = BLUE if k in (6, 7) else (PALE if k == 5 else MIST)
        boxes.append(box(d, x, y, bw, bh, f"{k + 1}  {s}", fill=fill, color=NAVY))
    for k in range(3):
        arrow(d, boxes[k].E, boxes[k + 1].W, color=NAVY)
        arrow(d, boxes[4 + k].E, boxes[5 + k].W, color=NAVY)
    ymid = boxes[3].S.y - 0.5
    line(d, boxes[3].S, (boxes[3].S.x, ymid)); line(d, (boxes[3].S.x, ymid), (boxes[4].N.x, ymid))
    arrow(d, (boxes[4].N.x, ymid), boxes[4].N, color=NAVY)
    rtop = boxes[4].S.y - 0.9
    rec = box(d, 0.4, rtop - 1.5, 12.6, 1.5, "every attempt, permitted or not, writes one MuscleReceipt: muscle_id, mode, requested, bounded, realized, units, "
              "permitted, reason, observation_age_s, actuation_latency_s, actuator_residual, evidence, status", fill=MIST, color=GREY)
    for b in boxes[4:]:
        line(d, b.S, (b.S.x, rtop), GREY, ls="--")
    notes(d, 0.4, rec.S.y - 0.35, "The five functions an engineer codes: observe, snapshot_native, execute, readback, restore_native. The three contracts "
                                   "declared: capability, timing, safety. The runtime does the rest, in this order, for every command.")
    return sd_svg(d)


# ---------------------------------------------------------------- control-loop block diagrams
def c_compass_loop():
    d = new_drawing()
    y1, y2, h = 0.0, -3.0, 1.1
    s1 = dsp.Sum().at((1.0, y1)).anchor("center"); d += s1
    kp = box(d, 1.8, y1 - h / 2, 1.4, h, "K[P]", fill=MIST)
    s2 = dsp.Sum().at((4.0, y1)).anchor("center"); d += s2
    sat = box(d, 4.8, y1 - h / 2, 1.9, h, "A·tanh(r/A)", fill=MIST)
    g = box(d, 7.1, y1 - h / 2, 1.9, h, "g[up] | g[down]\n× span", fill=MIST)
    knob = box(d, 9.5, y1 - h / 2, 2.7, h, "the knob, clipped\nto the cover", fill=PALE, color=GOLD)
    plant = box(d, 9.5, y2 - 0.7, 2.7, 1.4, "NATIVE CONTROLLER\n+ the muscle (τ)", fill=MIST)
    band = box(d, 6.0, y2 - h / 2, 2.4, h, "the band\np ∈ [0, 1]", fill=MIST)
    kd = box(d, 2.6, y2 - h / 2, 2.8, h, "K[D]·v\nv = ṗ, smoothed", fill=MIST)
    arrow(d, (0.0, y1), s1.W, label="c", color=NAVY)
    arrow(d, s1.E, kp.W, label="e", color=NAVY)
    arrow(d, kp.E, s2.W, color=NAVY)
    arrow(d, s2.E, sat.W, label="r", color=NAVY)
    arrow(d, sat.E, g.W, label="F", color=NAVY)
    arrow(d, g.E, knob.W, label="Δx", color=NAVY)
    arrow(d, knob.S, plant.N, color=NAVY)
    text_at(d, knob.S.x - 0.15, (knob.S.y + plant.N.y) / 2, "x: write, read back", NAVY, halign="right", valign="center")
    arrow(d, plant.W, band.E, label="y", color=NAVY)
    arrow(d, band.W, kd.E, label="p", color=NAVY)
    arrow(d, kd.N, s2.S, color=NAVY)
    text_at(d, s2.S.x + 0.15, (kd.N.y + s2.S.y) / 2, "K[D]·v", NAVY, valign="center")
    d += elm.Wire("|-").at(band.S).to((s1.S.x, y2 - 1.4)).color(NAVY)
    arrow(d, (s1.S.x, y2 - 1.4), s1.S, color=NAVY)
    text_at(d, s1.S.x + 0.15, (y2 - 1.4 + s1.S.y) / 2, "p", NAVY, valign="center")
    text_at(d, s1.S.x + 0.12, s1.S.y - 0.05, "+", NAVY, valign="top")                      # e = p − c: p enters plus,
    text_at(d, s1.W.x - 0.05, s1.W.y + 0.08, "−", NAVY, halign="right", valign="bottom")   # the centre c minus
    notes(d, 0.0, y2 - 1.9, "c the centre of the band; y the reading; p the reading's position in the band; e = p − c; v = ṗ smoothed; r the raw "
                            "force; F the force after the saturation; Δx the step; x the knob. Fail up: p ≥ 0.95 → F = A at once; the down side "
                            "held until p is back inside the band. No take-back while the reading climbs above the centre (F < 0 with v > 0 and "
                            "p > c → F = 0). K[D] is set from the muscle's own response time τ (critical damping), never tuned by hand.")
    return sd_svg(d)


def c_engine_loop():
    d = new_drawing()
    y1, y2, h = 0.0, -3.2, 1.9
    obs = box(d, 0.4, y1 - h / 2, 4.0, h, "nine observations: q, load, power, thermal, network, drift, stale, security, conflict", fill=MIST)
    blend = box(d, 4.8, y1 - h / 2, 3.6, h, "blend\nx ← (1 − a)x + a·x[obs]\na = 0.339", fill=MIST)
    eng = box(d, 8.8, y1 - h / 2, 4.2, h, "THE ENGINE\none macro step, RK4\nx = (E, U, I[U], S, B, Ḃ)", fill=BLUE)
    law = box(d, 8.8, y2 - h / 2, 4.2, h, "the control law, read\nu = clip(−f[U] + K[P](σ − U))\npush = u/25", fill=MIST)
    auth = box(d, 4.8, y2 - h / 2, 3.6, h, "THE NERVOUS SYSTEM\nauthority to give back only if push ≤ release, U ≥ gate", fill=PALE, color=GOLD)
    out = box(d, 0.4, y2 - h / 2, 4.0, h, "to the compass law on every muscle: the gate open or held", fill=MIST)
    arrow(d, obs.E, blend.W, color=NAVY); arrow(d, blend.E, eng.W, color=NAVY)
    arrow(d, eng.S, law.N, color=NAVY); arrow(d, law.W, auth.E, color=NAVY); arrow(d, auth.W, out.E, color=NAVY)
    d += elm.ArcLoop(arrow="->", radius=0.7).at(eng.N).to(eng.NNE).color(NAVY)
    text_at(d, eng.N.x - 0.1, eng.N.y + 0.95, "the state persists decision to decision", NAVY, halign="right", valign="bottom")
    notes(d, 0.4, y2 - h / 2 - 0.4, "The engine is the body's physiology; it grants the authority and feeds the release gate. The compass law is the hand on "
                                    "each lever; u is evaluated and never applied to a knob. Every line of this chain is in the audit record of every decision.")
    return sd_svg(d)


def c_verdict():
    """The verdict as the engine that stands reads it (omnicompass/verdict.py, judge="interval"): the trial step's cost
    against the reference's as a 95% interval on the logarithm of each piece of work's cost, read GAIN, STEADY or LOSS
    exactly as a report reads a row; the medians kept as the second guard. Every number is the controllers' own
    (omni_controller/controller.py: n = 200, a = 0.02, R = 7,200 s, 120 decisions at 60 s; omni_controller/gpu_compass.py:
    n = 30, a = 0.02, R = 900 decisions of 2 s)."""
    d = new_drawing()
    y1, h = 0.0, 2.6
    ref = box(d, 0.4, y1 - h / 2, 4.0, h, "REFERENCE r\nthe knob at the deepest step already allowed (a card: at native); the cost of each "
                                           "of n requests, measured fresh (Kubernetes n = 200; a card n = 30)", fill=MIST)
    trial = box(d, 4.8, y1 - h / 2, 4.0, h, "TRIAL t\nthe knob one step past it, the same traffic; the cost of n more requests "
                                             "(a card: its own service time, the wait in the queue left out)", fill=PALE, color=GOLD)
    read = box(d, 9.2, y1 - h / 2, 3.8, h, "THE READING\nd = mean ln c[t] − mean ln c[r], its 95% interval (Welch); stepwise a second "
                                            "interval against the costs first measured at native", fill=BLUE)
    arrow(d, ref.E, trial.W, color=NAVY); arrow(d, trial.E, read.W, color=NAVY)
    y2, h2 = -3.6, 2.2
    rule = box(d, 0.4, y2 - h2 / 2, 12.6, h2, "an interval wholly above zero is a LOSS: refused. An interval wider than the allowance "
                                               "(half-width over τ = ln(1 + a)) with fewer than 3n trial requests: measure on. Otherwise allowed "
                                               "only if median t ≤ min(r, c[native])·(1 + a) and d ≤ τ, with a = 0.02; else refused, past the allowance",
               fill=MIST, color=NAVY)
    arrow(d, read.S, (read.S.x, rule.N.y), color=NAVY)
    y3, h3 = -7.0, 1.9
    yes = box(d, 0.4, y3 - h3 / 2, 4.0, h3, "ALLOWED: the deepest allowed step is now the trial step; the law may use it; the next "
                                             "trial no sooner than P decisions after this one began (Kubernetes 10 = 600 s; a card 8)", fill="#e4efe4", color=GREEN)
    more = box(d, 4.8, y3 - h3 / 2, 4.0, h3, "MEASURE ON: the knob stays at the trial step one more decision, up to 3n requests", fill=PALE, color=GOLD)
    no = box(d, 9.2, y3 - h3 / 2, 3.8, h3, "REFUSED: the muscle is slower there. The knob goes back; the step is not tried again for R decisions "
                                            "(Kubernetes 7,200 s; a card 900 decisions = 30 min)", fill=ROSE, color=RED)
    for b, col in ((yes, GREEN), (more, GOLD), (no, RED)):
        arrow(d, (b.N.x, rule.S.y), b.N, color=col)
    yb, yt = y3 - h3 / 2 - 0.3, y1 + h / 2 + 0.4                   # the measure-on return, round the outside, into the trial
    line(d, more.S, (more.S.x, yb), color=GOLD); line(d, (more.S.x, yb), (13.4, yb), color=GOLD)
    line(d, (13.4, yb), (13.4, yt), color=GOLD); line(d, (13.4, yt), (trial.N.x, yt), color=GOLD)
    arrow(d, (trial.N.x, yt), trial.N, color=GOLD)
    text_at(d, trial.N.x + 0.15, yt + 0.05, "the trial continues", GOLD, valign="bottom")
    notes(d, 0.4, y3 - h3 / 2 - 0.65, "The verdict stands over every slow knob (the machines, the clock ceiling, a cache's notch). A trial begins only while "
                                     "the service is calm and nothing waits; a phase that sees the service leave calm, or that takes longer than its "
                                     "limit (Kubernetes 1,200 s; a card 30 decisions), is abandoned and the knob goes back, the step neither "
                                     "allowed nor refused. The knob never passes the deepest allowed step, so steps cannot add up past the allowance. "
                                     "On the max, the Kubernetes machine count never gives back a machine the cluster had on its own.")
    return sd_svg(d)


def c_gpu_pair():
    d = new_drawing()
    band = box(d, 0.4, -0.8, 3.6, 1.6, "the band: the mean response of the last 5 s, from SLO/10 to the SLO", fill=MIST)
    mode = box(d, 4.4, -0.8, 3.6, 1.6, "race? (≥ 95% utilization) steady under the limit? otherwise: pace", fill=PALE, color=GOLD)
    up = box(d, 8.8, 1.0, 4.2, 2.3, "UP WIRE: the clock ceiling. +15 MHz steps toward the top; a step down only through the verdict; never under the busy clock", fill=BLUE)
    dn = box(d, 8.8, -3.3, 4.2, 2.3, "DOWN WIRE: the power limit, the lid. ⌈1.10 × the busy draw⌉, never over the start limit, never under the envelope floor", fill=BLUE)
    arrow(d, band.E, mode.W, label="F", color=NAVY)
    line(d, mode.E, (8.4, 0.0)); line(d, (8.4, dn.W.y), (8.4, up.W.y))
    arrow(d, (8.4, up.W.y), up.W, color=NAVY); arrow(d, (8.4, dn.W.y), dn.W, color=NAVY)
    card = box(d, 8.8, -6.2, 4.2, 1.9, "THE CARD: its boost climbs to the ceiling; its limiter knocks back at the lid", fill=MIST)
    line(d, up.E, (13.3, up.E.y)); line(d, (13.3, up.E.y), (13.3, card.E.y)); line(d, dn.E, (13.3, dn.E.y))
    arrow(d, (13.3, card.E.y), card.E, color=NAVY)
    d += elm.Wire("-|", arrow="->").at(card.W).to(band.S).color(GREEN)
    text_at(d, 2.5, card.W.y - 0.1, wrapw("the meters: utilization, draw, temperature, clocks, p95 (every 2 s)", 6.0), GREEN, valign="top")
    notes(d, 0.4, -6.7, "Race: both wires to full at once while work waits. Steady under the limit: the card's own busy clock as the ceiling, no "
                        "knock-backs. Fail up on a breach, a failed request, a blind feed or a heat slowdown. A limit set by another hand: observe "
                        "only from then on.")
    return sd_svg(d)


def c_authority():
    """The nervous system's authority as logic: expansion is never gated beyond the security hold; contraction needs
    every one of its conditions."""
    d = new_drawing()
    # omnicompass/nervous_system.py authority(): contract = calm ≥ θ (pods 0.5, machines 0.7) and slo_clean and seeing;
    # calm = κ·h·(1 − clamp(σ − 1))·(1 − clamp(ν)); the controller adds its own gate (node_release_gate) and the verdict
    cond = ["the engine settled: calm = κ·h·(1 − excess stress)·(1 − unmet need) at or over the organ's threshold θ (pods 0.5; machines 0.7)",
            "the line clean: no breach now, and for the pods none in the last 180 s (the clear time)",
            "every sense live (none blind or stale): a blind sense never gives capacity back",
            "and, for the machines, the release gate: more than one machine; no pod waiting; pods not scaling up; the remaining machines at or under ρ",
            "the last command landed (proprioception: no new order to a muscle still carrying out the previous one)",
            "the verdict allows the step (the deepest step already allowed covers the count)"]
    cw, ch, step = 7.2, 0.62, 0.84
    y = 0.0
    tops = []
    for c in cond:
        hh = hfor(c, cw, 0.3)
        box(d, 0.4, y - hh, cw, hh, c, fill=MIST, color=GREY, pad=0.3)
        line(d, (0.4 + cw, y - hh / 2), (8.2, y - hh / 2))
        tops.append(y - hh / 2)
        y -= hh + step - ch
    top, bot = tops[0], tops[-1]
    mid = (top + bot) / 2
    line(d, (8.2, top), (8.2, bot))
    and1 = box(d, 8.2, mid - 0.7, 1.3, 1.4, "AND", fill=BLUE)
    give = box(d, 10.1, mid - 1.1, 2.9, 2.2, "GIVE BACK: one unit a decision (a machine: at most one a minute), or the calm share of the surplus", fill=PALE, color=GOLD)
    arrow(d, and1.E, give.W, color=NAVY)
    y2 = y - 0.5
    tops2 = []
    for c in ["a reason: the service past the wall, a sense blind, or a pod waiting for a place", "NOT a security hold (the hold flag, the forbidden key)"]:
        hh = hfor(c, cw, 0.3)
        box(d, 0.4, y2 - hh, cw, hh, c, fill=MIST, color=GREY, pad=0.3)
        line(d, (0.4 + cw, y2 - hh / 2), (8.2, y2 - hh / 2))
        tops2.append(y2 - hh / 2)
        y2 -= hh + step - ch
    top2, bot2 = tops2[0], tops2[-1]
    mid2 = (top2 + bot2) / 2
    line(d, (8.2, top2), (8.2, bot2))
    and2 = box(d, 8.2, mid2 - 0.6, 1.3, 1.2, "AND", fill=BLUE)
    add = box(d, 10.1, mid2 - 0.95, 2.9, 1.9, "ADD: at once, never held back (a parked machine woken within 5 s)", fill=ROSE, color=RED)
    arrow(d, and2.E, add.W, color=RED)
    notes(d, 0.4, y2 - 0.3, "Asymmetric on purpose: adding is cheap to undo and expensive to delay; taking back is cheap to delay and expensive to get "
                            "wrong. Every held decision writes the first reason that failed. In observe mode every authority is computed and "
                            "logged and nothing is written; under the kill switch there is no authority at all.")
    return sd_svg(d)


# ---------------------------------------------------------------- flowcharts
def chart(steps, w=5.6, decisions=None, side_w=4.0, yes="yes", no="no", gap=0.45):
    """A vertical flowchart: steps is a list of (kind, text) with kind 'start', 'box', 'decision', 'end' or 'cont' (the
    chart continues in, or from, another figure); a decision's side branch goes to a box at the right (decisions[k] =
    (branch word, text)), the other branch continues down. Every text is fitted to its shape, and every shape takes
    the height its text needs. A chart taller than a page is split into two figures by its caller."""
    d = new_drawing()
    decisions = decisions or {}
    y, prev = 0.0, None
    for k, (kind, text) in enumerate(steps):
        if kind in ("start", "end", "cont"):
            t = fit(text, w, 1.0); h = lines_of(t) * LH + 0.4
            e = flow.Start(w=w, h=h).at((0, y)).anchor("N").label(t, fontsize=PT).fill(MIST if kind == "cont" else BLUE).color(GREY if kind == "cont" else NAVY)
        elif kind == "decision":
            t = fit(text, w * 0.66, 0.0); h = lines_of(t) * LH * 2.0 + 0.4
            branch = (decisions.get(k) or (no, ""))[0] or no
            e = flow.Decision(w=w, h=h, E=branch, S=(yes if branch == no else no), fontsize=PT).at((0, y)).anchor("N").label(t, fontsize=PT).fill(PALE).color(NAVY)
        else:
            t = fit(text, w, 0.6); h = lines_of(t) * LH + 0.4
            e = flow.Box(w=w, h=h).at((0, y)).anchor("N").label(t, fontsize=PT).fill(MIST).color(NAVY)
        d += e
        if prev is not None:
            d += flow.Arrow().at(prev.S).to(e.N).color(NAVY)
        if kind == "decision" and k in decisions and decisions[k][1]:
            sw = min(side_w, tw(decisions[k][1]) + 0.8)
            st = fit(decisions[k][1], sw, 0.6); sh = lines_of(st) * LH + 0.4
            side = flow.Box(w=sw, h=sh).at((w / 2 + 0.9, e.E.y)).anchor("W").label(st, fontsize=PT).fill(ROSE).color(RED)
            d += side
            d += flow.Arrow().at(e.E).to(side.W).color(RED)
        prev = e
        y -= h + gap
    return sd_svg(d)


def _split(steps, decisions, at):
    """The steps as two charts' worth, the second renumbered, each with a 'continued' marker."""
    a = steps[:at] + [("cont", "continued in the next figure")]
    b = [("cont", "continued from the previous figure")] + steps[at:]
    da = {k: v for k, v in decisions.items() if k < at}
    db = {k - at + 1: v for k, v in decisions.items() if k >= at}
    return (a, da), (b, db)


WIRE_CHECK = ([("start", "the wire check (before any write)"),
               ("box", "1 read: every meter answers (watts, temperature, utilization, limit, clock, top clock)"),
               ("box", "2 snapshot: the setting as found, recorded once"),
               ("decision", "3 up wire: a value written is taken and read back equal?"),
               ("decision", "4 down wire: the other wire reads back exactly?"),
               ("decision", "5 restore: the snapshot written and read back equal?"),
               ("decision", "6 stop: on its signal the governor hands both wires back?"),
               ("decision", "7 another writer: a value set by someone else is left alone, exit 5?"),
               ("end", "WIRED RIGHT: the run may proceed")],
              {3: ("no", "FAIL: the wire, the step and what the device said; nothing else runs"),
               4: ("no", "FAIL"), 5: ("no", "FAIL"), 6: ("no", "FAIL"), 7: ("no", "FAIL")})


def f_wire_check():
    (a, da), _ = _split(*WIRE_CHECK, at=5)
    return chart(a, decisions=da)


def f_wire_check_b():
    _, (b, db) = _split(*WIRE_CHECK, at=5)
    return chart(b, decisions=db)


PAIRED_RUN = ([("start", "one paired run (tools/kind_paired.sh, aks-metered, gpu_paired.sh)"),
               ("box", "fresh cluster or card; the same work, the same window, the same seeds in both arms"),
               ("box", "pair 1: the native arm (the stack's own controller alone)"),
               ("box", "pair 1: the omni arm (the same controller with Omni-Compass on top); order rotated pair to pair"),
               ("decision", "the reset check: every setting back at the operator's, read back, no record left?"),
               ("decision", "ten pairs done?"),
               ("box", "the receipt: every gauge, native, omni, the paired change with its 95% interval, its reading"),
               ("box", "runs A, B and C → tools/confirm_abc.py → the three-run table with the reading key on top"),
               ("end", "every row shown, losses included")],
              {4: ("no", "the arm is invalid and left out of the table, never counted"),
               5: ("no", "the next pair, arms rotated")})


def f_paired_run():
    (a, da), _ = _split(*PAIRED_RUN, at=5)
    return chart(a, decisions=da, w=6.6, side_w=3.4)


def f_paired_run_b():
    _, (b, db) = _split(*PAIRED_RUN, at=5)
    return chart(b, decisions=db, w=6.6, side_w=3.4)


def f_phases():
    return chart([("start", "0 Verify: the copy against its manifest → VERIFICATION: PASS, the version named"),
                  ("box", "1 Account and cluster: a system pool, work pools under the cloud's autoscaler.\nGate: the autoscaler scales a work pool up and down on its own"),
                  ("box", "2 Identity: namespace, service account, the read-only role.\nGate: kubectl auth can-i answers exactly the table"),
                  ("box", "3 Watch: the governor in watch mode.\nGate: an audit with decisions and no write, one full day of the service's own load"),
                  ("box", "4 Feed and line: the response-time feed and the written line.\nGate: the feed's age under 15 s; the line signed off by the owner"),
                  ("box", "5 Paired run: native against native with Omni-Compass on top.\nGate: the receipt read row by row, every LOSS explained or fixed and rerun"),
                  ("box", "6 Govern: the role granted, the OFF switch and the watchdog wired.\nGate: the OFF switch drilled, every setting back within 60 s"),
                  ("end", "7 Day two: upgrades, rollbacks, audits, alarms, the fleet; the drill every quarter")],
                 w=9.0)


# the machine organ's release, in the order the controller tests it (omni_controller/controller.py, one decision; the
# checks of omnicompass/nervous_system.py node_release_gate() in their code order, then the one-a-minute rule)
RELEASE_GATE = ([("start", "the compass law asks for one machine back: F < −0.2, p under the centre, and the verdict's deepest allowed "
                           "step covers n − 1 (never on the max; never during a trial)"),
                 ("decision", "1 more than one machine in service?"),
                 ("decision", "2 no pod waiting for a place?"),
                 ("decision", "3 the pods not scaling up?"),
                 ("decision", "4 the line not breached now (p95 under the line, the feed live)?"),
                 ("decision", "5 the remaining machines at or under the utilisation target: used / ((n − 1) · one machine) ≤ ρ, "
                              "ρ the engine's demand clipped to [0.5, 0.95]?"),
                 ("decision", "6 the machine organ's authority to contract: its engine calm ≥ 0.7, its line clean, no security hold?"),
                 ("decision", "7 every sense live?"),
                 ("decision", "8 the last machine command landed?"),
                 ("decision", "9 a minute since the last release?"),
                 ("end", "release permitted: one machine back (n − 1), read back; cruise overrides it (work waiting for a place keeps "
                         "every machine in service)")],
                {k: ("no", "HOLD; the first reason that failed is written") for k in range(1, 10)})


def f_release_gate():
    (a, da), _ = _split(*RELEASE_GATE, at=6)
    return chart(a, decisions=da, side_w=3.4)


def f_release_gate_b():
    _, (b, db) = _split(*RELEASE_GATE, at=6)
    return chart(b, decisions=db, side_w=3.4)


def f_stops():
    return chart([("start", "the governor stops"),
                  ("decision", "the reset file (the planned end of a run)?"),
                  ("decision", "the kill switch (omni_switch.py off, SIGTERM, the kill file)?"),
                  ("decision", "a death without a hand-back: the process gone, or its lease older than 5 periods "
                               "(Kubernetes at least 2 min; a card at least 60 s)?"),
                  ("end", "in every case: every setting at native, read back, no record left")],
                 decisions={1: ("yes", "hands every setting back in reverse order, reads each back, exits 0"),
                            2: ("yes", "the same hand-back at once; no governor starts while the switch is off"),
                            3: ("yes", "the watchdog runs the recorded restore (--restore-only) from the objects themselves")},
                 w=6.2, side_w=4.6)


def f_model_gate():
    return chart([("start", "a change to a rule, a gain, a guard, a preset or a muscle"),
                  ("box", "tools/model_gate.py: the change against the engine that stands, our own models, the same seeds, paired (class S)"),
                  ("decision", "any LOSS by the gauge's aim?"),
                  ("decision", "promise shown (GAIN somewhere, STEADY elsewhere)?"),
                  ("box", "its GitHub trials: A, B and C on the real stacks"),
                  ("decision", "no LOSS, nothing behind the engine that stands?"),
                  ("end", "the next engine version: fingerprinted, every benchmark run again on it")],
                 decisions={2: ("yes", "root-caused and fixed in the model; never carried into a real run"),
                            3: ("no", "not dispatched"),
                            5: ("no", "fixed inside the newest engine and run again")})


def f_reading():
    return chart([("start", "one judged row: three runs, each a change in percent of native with its 95% interval"),
                  ("decision", "did two runs each move 0.5% or more, in opposite directions?"),
                  ("decision", "is the mean of the three changes 0.5% or more, either way?"),
                  ("decision", "is that way the gauge's aim? (time, misses, failures: a fall; work: a rise; a resource spent: a fall is a cut)"),
                  ("decision", "does every run's interval exclude zero, all three the same way?"),
                  ("end", "GAIN in all three of our runs")],
                 decisions={1: ("yes", "the runs disagree: the test is unstable there; look into it"),
                            2: ("no", "STEADY, under the floor"),
                            3: ("no", "LOSS; for a resource spent that rose, power given (in all three, or by the mean, by the next question)"),
                            4: ("no", "GAIN by the mean of our three runs, with the count of runs beyond the noise")},
                 w=6.4, side_w=4.4)


def f_park():
    return chart([("start", "a full decision in the cloud mode (every 60 s)"),
                  ("decision", "the 95th percentile over the line, or the feed blind?"),
                  ("decision", "a pod waiting for a place (checked every 5 s)?"),
                  ("decision", "the release gate open and the trial allowing one more machine parked?"),
                  ("box", "park one machine: taint PreferNoSchedule; mark its pods first to go (pod-deletion-cost)"),
                  ("end", "the cloud's own autoscaler deletes the empty machine on its own schedule")],
                 decisions={1: ("yes", "wake every parked machine at once (remove the taint)"),
                            2: ("yes", "wake one machine within 5 s; the pod lands on a parked one at once"),
                            3: ("no", "hold: nothing parked; the reason in the audit")})


def f_conductor():
    return chart([("start", "one tick of the conductor (grid.yml, every 15 minutes; its newest code)"),
                  ("decision", "an Azure run, a grid report or a verify waiting for a runner?"),
                  ("box", "read every started run back from its name; never start one twice"),
                  ("box", "the reruns: A of every benchmark on the engine that stands, then B, then C; a few a tick (scripts/reruns.txt)"),
                  ("box", "the cloud queues: the next set of each family's queue whose switch is on (Azure, Google and Amazon on)"),
                  ("box", "the grid: every square not yet started, up to what GitHub runs plus a margin"),
                  ("end", "nothing cancelled; a problem found in a run is fixed and the run made again")],
                 decisions={1: ("yes", "start nothing this tick (Azure first)")}, w=6.8)


TRIAL = ([("start", "a slow knob; the service calm and nothing waiting; P decisions since the last trial began (Kubernetes 10 = 600 s; a card 8)"),
          ("box", "reference: the knob at the deepest step already allowed (a card: at native); the cost of n requests measured fresh "
                  "(Kubernetes n = 200 response times; a card n = 30 of its own service time, the queue's wait left out)"),
          ("box", "the trial step: one step deeper, under the same traffic; the cost of n more requests"),
          ("decision", "the service calm throughout, and each phase within its limit (Kubernetes 1,200 s; a card 30 decisions)?"),
          ("box", "the reading: d = mean ln c[trial] − mean ln c[ref] with its 95% interval (Welch); stepwise, a second interval against the "
                  "costs first measured at native"),
          ("decision", "an interval wholly above zero (a LOSS)?"),
          ("decision", "an interval wider than the allowance (half-width over τ = ln(1 + a)), with fewer than 3n trial requests?"),
          ("decision", "median t ≤ min(r, c[native]) · (1 + a) and d ≤ τ, with a = 0.02?"),
          ("end", "step allowed: the deepest allowed step is now the trial step")],
         {3: ("no", "trial abandoned: the knob goes back to the deepest allowed step; the step neither allowed nor refused"),
          5: ("yes", "step refused: the muscle is slower there; the knob goes back; not tried again for R (Kubernetes 7,200 s; a card 900 decisions)"),
          6: ("yes", "measure on: the knob stays at the trial step one more decision"),
          7: ("no", "step refused, past the allowance; the knob goes back; not tried again for R decisions")})


def f_trial():
    (a, da), _ = _split(*TRIAL, at=5)
    return chart(a, decisions=da, w=6.0, side_w=4.2)


def f_trial_b():
    _, (b, db) = _split(*TRIAL, at=5)
    return chart(b, decisions=db, w=6.0, side_w=4.2)


def f_cache_rule():
    """The cache knob's decide() in its code order (tools/run_redis.py, run_ycsb.py, run_sysbench.py): fail up first, then
    grow, then give back, else hold. Full = 90% of the ceiling used; a notch is 8 MB, 64 MB or one 128 MB chunk."""
    return chart([("start", "a cache knob's decision, once a second (Redis's memory ceiling, MongoDB's storage-engine cache, "
                            "MySQL's buffer pool); p the reading in the band, F the compass law's force"),
                  ("decision", "p ≥ 0.95 (the line at hand) and the cache full (≥ 90% of the ceiling used)?"),
                  ("decision", "F > 0.05 (slow), the cache full, and (MongoDB, MySQL) misses ≥ 1% of the requests?"),
                  ("decision", "F < −0.05 (calm), the dwell passed since the last growth (5 s; InnoDB 10 s), and the cache "
                               "holding its work (Redis: nothing evicted in the last second; MongoDB, MySQL: requests seen "
                               "and misses under 1%)?"),
                  ("end", "hold: slow with room to spare is a cold miss no ceiling can mend; the reason in the audit")],
                 decisions={1: ("yes", "fail up: a quarter of the cover at once (128 MB; 448 MB; four 128 MB chunks), "
                                       "again the next second while still past"),
                            2: ("yes", "grow by ⌈F / 0.1⌉ notches, at least one (8 MB; 64 MB; one 128 MB chunk)"),
                            3: ("yes", "give one notch back")},
                 w=6.2, side_w=4.4)


# ---------------------------------------------------------------- timing diagrams and modelled traces
def t_clocks():
    fig = mpl_fig(3.4)
    ax = fig.add_subplot(111)
    T = 300
    for t in range(0, T + 1, 5):
        ax.vlines(t, 0, 0.35, color=GOLD, lw=0.8)
    for t in range(0, T + 1, 15):
        ax.vlines(t, 1.0, 1.35, color=GREY, lw=1.0)
    for t in range(0, T + 1, 60):
        ax.vlines(t, 2.0, 2.6, color=NAVY, lw=2.0)
    for t in range(0, T + 1, 2):
        ax.vlines(t, 3.0, 3.25, color=GREEN, lw=0.5)
    ax.text(T + 6, 0.15, "the governor's fast checks, every 5 s\n(a waiting pod wakes a machine; the floor)", va="center", color=GOLD)
    ax.text(T + 6, 1.15, "the HPA's own check, every 15 s\n(native, untouched)", va="center", color=GREY)
    ax.text(T + 6, 2.3, "the full decision, every 60 s: the state,\nthe law, the gate, the verdict, one write,\none audit line", va="center", color=NAVY)
    ax.text(T + 6, 3.1, "the card governor, every 2 s", va="center", color=GREEN)
    ax.annotate("", xy=(180, -0.55), xytext=(0, -0.55), arrowprops=dict(arrowstyle="<->", color=INK))
    ax.text(90, -1.0, "a clean line for 180 s (3 decisions) before the pods,\nthe clock or the power give back (a machine: no breach now)",
            ha="center", va="top", color=INK)
    ax.set_xlim(0, T * 2.35); ax.set_ylim(-1.9, 3.6)
    ax.set_xticks(range(0, T + 1, 60)); ax.set_xlabel("seconds")
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    return fig_svg(fig)


def t_band_step():
    """The law's own code answering a load step: CompassLaw on a first-order muscle (class S)."""
    from omnicompass.compass_law import Band, CompassLaw
    dt, tau = 60.0, 120.0
    law = CompassLaw(band=Band(lo=50.0, hi=500.0, center=0.4), dt=dt, tau=tau, kp=1.0)
    g_up, g_down, cover = 0.10, 0.02, (2.0, 12.0)
    x, demand, reading = 2.0, 1.0, 100.0
    T = 40
    ts, ps, Fs, xs, rs, ds = [], [], [], [], [], []
    for k in range(T):
        t = k * dt
        demand = 1.0 if k < 6 else (2.6 if k < 22 else 1.2)
        target = 100.0 * (demand / x) ** 2 * 2.0 if x > 0 else 500.0
        reading += (target - reading) * (1 - math.exp(-dt / tau))
        F = law.force(reading)
        step = (g_up if F > 0 else g_down) * F * (cover[1] - cover[0])
        x = min(cover[1], max(cover[0], x + step))
        ts.append(t / 60); ps.append(law.p); Fs.append(F); xs.append(x); rs.append(reading); ds.append(demand)
    fig = mpl_fig(5.6)
    axs = fig.subplots(3, 1, sharex=True)
    axs[0].step(ts, ds, where="post", color=GREY, label="demand (relative)")
    axs[0].plot(ts, [r / 100 for r in rs], color=NAVY, label="the reading (ms / 100)")
    axs[0].axhline(5.0, color=RED, ls="--", lw=1); axs[0].text(39, 5.15, "the line, 500 ms", ha="right", color=RED)
    axs[0].legend(loc="upper left"); axs[0].set_ylabel("reading"); axs[0].set_ylim(0, 6.2)
    axs[1].plot(ts, ps, color=NAVY, label="position p")
    axs[1].axhspan(0.0, 0.05, color=RULE, alpha=0.6); axs[1].axhspan(0.95, 1.0, color=RULE, alpha=0.6)
    axs[1].axhline(0.4, color=GOLD, ls="--", lw=1); axs[1].text(39, 0.44, "the centre c = 0.4 (the tune-down)", ha="right", color=GOLD)
    axs[1].plot(ts, Fs, color=GREEN, label="force F"); axs[1].axhline(0, color=GREY, lw=0.6)
    axs[1].set_ylim(-1.05, 1.05); axs[1].legend(loc="lower right"); axs[1].set_ylabel("p, F")
    axs[2].step(ts, xs, where="post", color=NAVY, label="the knob (machines)")
    axs[2].axhline(2, color=GREY, ls=":", lw=1); axs[2].text(0.3, 2.3, "the floor, 2", color=GREY)
    axs[2].set_ylabel("knob"); axs[2].set_xlabel("decisions (minutes, one decision every 60 s)"); axs[2].legend(loc="upper right")
    return fig_svg(fig)


def t_lease():
    fig = mpl_fig(3.4)
    ax = fig.add_subplot(111)
    t = list(range(0, 61))
    native = [10] * 61
    reset = [7 if k < 10 else 10 for k in t]
    death = [7 if k < 19 else 10 for k in t]
    walk = [7 if k < 10 else min(10, 7 + 3 * (k - 10) / 24) for k in t]
    ax.plot(t, native, color=NATIVE_ORANGE, ls="--", label="native's setting")
    ax.step(t, reset, where="post", color=NAVY, label="the reset, the kill switch: back at once, read back")
    ax.step(t, death, where="post", color=RED, label="a death: the watchdog's restore (kill test: 7 to 11 s, mean 9 s)")
    ax.plot(t, walk, color=GOLD, label="the modelled bodies' lease: walked back over 24 decisions")
    ax.axvline(10, color=INK, lw=0.8); ax.text(10.4, 10.5, "t = 10: the governor stops", color=INK)
    ax.set_ylim(6, 10.9); ax.set_xlim(0, 60)
    ax.set_xlabel("seconds (the live governor) · decisions (the modelled bodies)"); ax.set_ylabel("a setting")
    ax.legend(loc="lower right")
    return fig_svg(fig)


def t_bursts():
    fig = mpl_fig(5.4)
    axs = fig.subplots(3, 1)
    sets = [("burst 1 4 1 6 1 9 (1,800 s, 300 s a step)", [1, 4, 1, 6, 1, 9], 300),
            ("burst 1 6 1 8 1 6 (1,800 s, 300 s a step)", [1, 6, 1, 8, 1, 6], 300),
            ("the real day: Google 2011 on 1 to 9 load generators (2,592 s, 108 s a step)",
             [2, 3, 3, 4, 3, 4, 4, 3, 2, 2, 2, 2, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7, 6, 5], 108)]
    for ax, (title, steps, w) in zip(axs, sets):
        xs = [k * w for k in range(len(steps) + 1)]
        ys = steps + [steps[-1]]
        ax.step(xs, ys, where="post", color=NAVY)
        ax.fill_between(xs, ys, step="post", color=BLUE)
        ax.set_title(title, loc="left"); ax.set_ylim(0, 10); ax.set_xlim(0, xs[-1])
        ax.set_ylabel("load generators")
    axs[-1].set_xlabel("seconds; every set at the tune-down (dial save) with native's cap,\nfive repetitions a run, A, B and C")
    return fig_svg(fig)


def t_climb_line():
    fig = mpl_fig(5.0)
    axs = fig.subplots(3, 1)
    T = 24
    own = [1.0 + 0.35 * math.sin(k / 3.0) + 0.15 * math.sin(k / 1.1) for k in range(T)]
    axs[0].step(range(T), own, where="post", color=NAVY); axs[0].set_title("the organism's own load (each plant's own demand; one shape of many)", loc="left")
    seq = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]
    axs[1].step(range(T), [s / 4.0 for s in seq], where="post", color=GOLD)
    axs[1].axhline(1.0, color=GREY, ls=":"); axs[1].text(0.3, 1.12, "level 4 = the own load; 8 = twice it", color=GREY)
    axs[1].set_title("the climb: 1 2 3 2 3 4 …, the load stepping by one", loc="left")
    axs[2].step(range(T), own, where="post", color=NAVY, label="demand")
    axs[2].bar([0], [0.25], bottom=[own[0]], width=1.0, align="edge", color=RED, alpha=0.6, label="work waiting at the start: 25% of the run's own work")
    axs[2].set_title("the line: the same load with work already waiting (LINE, realms/harness.py)", loc="left"); axs[2].legend(loc="upper right")
    for ax in axs:
        ax.set_ylim(0, 2.8); ax.set_xlim(0, T)
    axs[-1].set_xlabel("decisions")
    return fig_svg(fig)


def t_pedal():
    """The rules of the pedal drawn over a burst: push at once at the wall, lift off one machine a decision through the
    gate, idle at the floor; native's autoscaler adds when pods cannot be placed and scales down after its own delay."""
    steps, w = [1, 4, 1, 6, 1, 9], 5                                 # 5 decisions a step
    T = len(steps) * w + 6
    demand = [steps[min(k // w, len(steps) - 1)] if k < len(steps) * w else 1 for k in range(T)]
    nat, om = [], []
    n, m, down_wait = 2, 2, 0
    for k in range(T):
        need = max(2, math.ceil(demand[k] / 1.5))
        if need > n:
            n = need
            down_wait = 0
        elif need < n:
            down_wait += 1
            if down_wait >= 10:
                n -= 1; down_wait = 0
        nat.append(n)
        if need > m:
            m = need                                   # push: capacity added at once at the wall
        elif need < m:
            if k % 2 == 0:
                m = max(2, m - 1)                      # lift off: one machine a decision through the gate and the trial
        om.append(m)
    fig = mpl_fig(3.6)
    ax = fig.add_subplot(111)
    ax.step(range(T), demand, where="post", color=GREY, ls="--", label="demand (load generators)")
    ax.step(range(T), nat, where="post", color=GREY, label="native: machines (its autoscaler's own delay)")
    ax.step(range(T), om, where="post", color=NAVY, lw=2, label="Omni-Compass on top: push at once, lift off a step at a time")
    ax.axhline(2, color=GOLD, ls=":"); ax.text(0.3, 2.2, "idle: the floor of 2", color=GOLD)
    ax.set_xlabel("decisions"); ax.set_ylabel("machines, demand"); ax.set_ylim(0, 11.5); ax.legend(loc="upper left")
    return fig_svg(fig)


def t_trial():
    fig = mpl_fig(4.2)
    ax = fig.add_subplot(111)
    # the phases in decisions, as the controllers set them: a phase ends when its n requests are in (Kubernetes n = 200;
    # a card n = 30) and is abandoned past its limit (Kubernetes 1,200 s; a card 30 decisions); a refusal rests R
    # (Kubernetes 7,200 s; a card 900 decisions = 30 min); the next trial no sooner than P after the last began (600 s; 8)
    spans = [(0, 8, "reference: n requests at the deepest allowed step (a card: at native)", MIST, 15),
             (8, 16, "trial: n more one step deeper, the same traffic; up to 3n", PALE, 15),
             (16, 17, "", BLUE, 1), (17, 36, "refused: not tried again for R (Kubernetes 7,200 s; a card 900 decisions = 30 min)", ROSE, 36)]
    for a, b, lab, col, n in spans:
        ax.add_patch(patches.Rectangle((a, 0.7), b - a, 1.3, color=col, ec=GREY))
        if lab:
            ax.text((a + b) / 2, 1.35, wrap(lab, n), ha="center", va="center", fontsize=PT)
    ax.annotate("the verdict (one decision): the 95% interval of the change in log cost,\nGAIN, STEADY or LOSS; allowed, the deepest step moves one deeper; the\n"
                "next trial no sooner than P after this one began (Kubernetes 600 s; a card 8 decisions)", xy=(16.5, 2.0), xytext=(0.5, 2.55),
                arrowprops=dict(arrowstyle="->", color=GREEN), color=GREEN, ha="left")
    ax.text(18, 0.3, wrap("a phase past its limit (Kubernetes 1,200 s; a card 30 decisions), or out of calm, is abandoned: the knob goes back, "
                          "the step neither allowed nor refused", 100), ha="center", va="center", color=GREY, fontsize=PT)
    ax.set_xlim(0, 36); ax.set_ylim(0, 3.7); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_xlabel("decisions (one every 60 s on Kubernetes, the main engine's beat, its rules counted in seconds; one every 2 s on a card)")
    return fig_svg(fig)


def t_engine():
    """The frozen engine (omnicompass/core.py) answering a pressure pulse, with the control law on: class S."""
    from dataclasses import asdict
    from omnicompass.core import MACRO_DT, Params, State, control_command, macro_step, s_roots
    from omnicompass.adapter import STACK_PARAMS
    p = Params(**asdict(STACK_PARAMS))
    roots = s_roots(p)
    root = max(roots) if isinstance(roots, tuple) else float(roots)          # the stable well on the positive side
    x = State(E=0.05, U=0.98, I_U=0.1, S=root, B=0.0, B_dot=0.0)
    T, pulse = 80, (15, 35)
    rows = []
    for m in range(T):
        p.beta_int = 1.2 if pulse[0] <= m < pulse[1] else 0.0
        u, _ = control_command(x, p, m * MACRO_DT, +1)
        x, _ = macro_step(x, p, m * MACRO_DT, +1)
        rows.append((m * MACRO_DT, x.E, x.U, x.I_U, x.S, x.B, u / 25.0, p.beta_int))
    t = [r[0] for r in rows]
    fig = mpl_fig(5.8)
    axs = fig.subplots(3, 1, sharex=True)
    axs[0].step(t, [r[7] for r in rows], where="post", color=RED, label="β[int], the pressure pulse")
    axs[0].plot(t, [r[1] for r in rows], color=NAVY, label="E, the deviation")
    axs[0].plot(t, [r[3] for r in rows], color=GOLD, label="I[U], the memory")
    axs[0].legend(loc="upper right"); axs[0].set_ylabel("E, I[U]")
    axs[1].plot(t, [r[2] for r in rows], color=NAVY, label="U, the alignment (pole +1)")
    axs[1].plot(t, [r[6] for r in rows], color=GREEN, label="the push u/25, read by the nervous system")
    axs[1].axhline(1.0, color=GREY, ls=":"); axs[1].legend(loc="center right"); axs[1].set_ylabel("U, push")
    axs[2].plot(t, [r[4] for r in rows], color=NAVY, label=f"S, the stress (started at its root, {root:.2f})")
    axs[2].plot(t, [r[5] for r in rows], color=GOLD, label="B, the bath")
    axs[2].legend(loc="upper right"); axs[2].set_ylabel("S, B"); axs[2].set_xlabel("engine time (macro steps of 0.1; the live governor takes one a decision)")
    return fig_svg(fig)


def t_force_surface():
    import numpy as np
    dt, tau, kp = 60.0, 120.0, 1.0
    kd = max(0.0, 2.0 * math.sqrt(kp * tau / dt) - 1.0) * dt
    P = np.linspace(0, 1, 201); V = np.linspace(-0.01, 0.01, 201)
    PP, VV = np.meshgrid(P, V)
    F = np.tanh(kp * (PP - 0.5) + kd * VV)
    F = np.where((F < 0) & (VV > 0) & (PP > 0.5), 0.0, F)
    F = np.where(PP >= 0.95, 1.0, F)
    fig = mpl_fig(4.4)
    ax = fig.add_subplot(111)
    im = ax.pcolormesh(P, V * 60, F, cmap="RdYlGn", vmin=-1, vmax=1, shading="auto")
    cs = ax.contour(P, V * 60, F, levels=[-0.5, -0.25, 0, 0.25, 0.5], colors=INK, linewidths=0.6)
    ax.clabel(cs, fmt="%.2f", fontsize=PT)
    ax.axvline(0.05, color=NAVY, ls="--"); ax.axvline(0.95, color=NAVY, ls="--"); ax.axvline(0.5, color=GOLD)
    ax.text(0.93, 0.0, "fail up: F = A", color=NAVY, rotation=90, va="center", ha="center")
    ax.text(0.515, 0.0, "the centre", color=GOLD, rotation=90, va="center")
    ax.set_xlabel("position p in the band"); ax.set_ylabel("rate of change v (band per minute)")
    ax.set_title("K[P] = 1, K[D] at critical damping for τ = 120 s, dt = 60 s", loc="left")
    fig.colorbar(im, ax=ax, label="force F (A = 1)")
    return fig_svg(fig)


def t_damping():
    fig = mpl_fig(3.2)
    ax = fig.add_subplot(111)
    xs = [k / 20.0 for k in range(5, 400)]
    for kp, col in ((0.5, GREY), (1.0, NAVY), (2.0, GOLD)):
        ax.plot(xs, [max(0.0, 2.0 * math.sqrt(kp * r) - 1.0) for r in xs], color=col, label=f"K[P] = {kp}")
    ax.set_xlabel("τ / dt: the muscle's response time in decision periods"); ax.set_ylabel("K[D] / dt")
    ax.set_title("K[D] = max(0, 2·√(K[P]·τ/dt) − 1)·dt: critical damping, no overshoot, no ringing", loc="left")
    ax.legend(); ax.grid(alpha=0.3)
    return fig_svg(fig)


# ---------------------------------------------------------------- the receipts, charted from the tables
NUM = re.compile(r"([-+]?\d[\d,]*\.?\d*)\s*(%|req/s|pp)?\s*\(([-+]?\d[\d,]*\.?\d*)\s+to\s+([-+]?\d[\d,]*\.?\d*)\)")


def _num(s):
    return float(s.replace(",", ""))


def read_table(rel, head_starts):
    """Rows of the markdown table whose header starts with head_starts, as lists of cells."""
    rows, on = [], False
    for ln in (ROOT / rel).read_text(encoding="utf-8").splitlines():
        if ln.startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if cells and cells[0].startswith(head_starts):
                on = True; continue
            if on and all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                continue
            if on:
                rows.append(cells)
        elif on and ln.strip() == "":
            on = False
    return rows


def reading_color(word):
    w = word.lower()
    if "power given" in w:
        return GIVEN_BLUE
    if w.startswith("**even") or w.startswith("even"):
        return YELLOW
    if w.startswith("**gain") or w.startswith("gain"):
        return GREEN
    if w.startswith("**loss") or w.startswith("loss"):
        return RED
    if "shown" in w:
        return "#9a9a9a"
    return GREY


def _receipt_rows(rel):
    rows = read_table(rel, "Measure")
    judged, shown = [], []
    for r in rows:
        if len(r) < 5:
            continue
        name, a, b, c, word = r[0], r[1], r[2], r[3], r[4]
        vals = [NUM.search(x) for x in (a, b, c)]
        if not all(vals):
            continue
        unit = vals[0].group(2) or ""
        pts = [(_num(m.group(1)), _num(m.group(3)), _num(m.group(4))) for m in vals]
        (shown if "shown" in word.lower() else judged).append((name, unit, pts, word))
    return [j for j in judged if j[1] == "%"], shown


def receipt_chart(rel, title):
    """The judged rows of a three-run table: the paired change of runs A, B and C with their 95% intervals, coloured by
    the reading."""
    judged, _ = _receipt_rows(rel)
    fig = mpl_fig(0.46 * len(judged) + 1.7)
    ax = fig.add_subplot(111)
    for k, (name, unit, pts, word) in enumerate(reversed(judged)):
        col = reading_color(word)
        for j, (m, lo, hi) in enumerate(pts):
            y = k + 0.25 - 0.25 * j
            lo_c, hi_c = max(lo, -110), min(hi, 110)
            ax.plot([lo_c, hi_c], [y, y], color=col, lw=1.6, solid_capstyle="butt")
            ax.plot([max(m, -110)], [y], "o", color=col, ms=3.5)
            if lo < -110:
                ax.text(-111, y, "◄", color=col, ha="right", va="center", fontsize=PT)
    ax.axvline(0, color=NAVY, lw=1)
    ax.set_yticks(range(len(judged))); ax.set_yticklabels([wrap(j[0], 36) for j in reversed(judged)])
    ax.set_xlim(-115, 115); ax.set_xlabel("paired change against native, %\n(runs A, B, C from top; the interval is 95%)")
    ax.set_title("the judged rows: green GAIN, blue power given,\nred LOSS, yellow STEADY", loc="left")
    fig.suptitle(wrap(title, 78), x=0.01, ha="left", fontsize=PT)
    return fig_svg(fig)


def shown_chart(rel, title):
    """The rows shown and not judged: the governor's own inputs and the mechanism's traces, the change in A, B and C."""
    _, shown = _receipt_rows(rel)
    fig = mpl_fig(0.5 * len(shown) + 1.3)
    ax2 = fig.add_subplot(111)
    for k, (name, unit, pts, word) in enumerate(reversed(shown)):
        txt = "   ".join(f"{m:+.3g}{unit}" for m, _, _ in pts)
        ax2.text(0.02, k, txt, va="center", ha="left", fontsize=PT, color=GREY, family="DejaVu Sans Mono")
    ax2.set_yticks(range(len(shown))); ax2.set_yticklabels([wrap(s[0], 36) for s in reversed(shown)])
    ax2.set_xlim(0, 1); ax2.set_ylim(-0.6, max(0.6, len(shown) - 0.4)); ax2.set_xticks([])
    for s in ("top", "right", "left", "bottom"):
        ax2.spines[s].set_visible(False)
    ax2.tick_params(length=0)
    ax2.set_title("shown, not judged, runs A, B, C:\nthe governor's own inputs and\nthe mechanism's traces", loc="left")
    fig.suptitle(wrap(title, 78), x=0.01, ha="left", fontsize=PT)
    return fig_svg(fig)


RECEIPTS = {"goldilocks": ("results/live/V11_GOLDILOCKS.md", "On top of Goldilocks and the VPA's recommender (omni-v11)"),
            "keda_http": ("results/live/V11_KEDA_REQUESTS.md", "On top of KEDA's HTTP add-on (omni-v11)"),
            "keda_cpu": ("results/live/V11_KEDA_CPU_REQUESTS.md", "On top of KEDA on the CPU target and requests in flight (omni-v11)"),
            "cruisekube": ("results/live/V10_CRUISEKUBE.md", "On top of CruiseKube applying its own recommendations (omni-v10)")}


def r_goldilocks():
    return receipt_chart(*RECEIPTS["goldilocks"])


def r_goldilocks_shown():
    return shown_chart(*RECEIPTS["goldilocks"])


def r_keda_http():
    return receipt_chart(*RECEIPTS["keda_http"])


def r_keda_http_shown():
    return shown_chart(*RECEIPTS["keda_http"])


def r_keda_cpu():
    return receipt_chart(*RECEIPTS["keda_cpu"])


def r_keda_cpu_shown():
    return shown_chart(*RECEIPTS["keda_cpu"])


def r_cruisekube():
    return receipt_chart(*RECEIPTS["cruisekube"])


def r_cruisekube_shown():
    return shown_chart(*RECEIPTS["cruisekube"])


def r_capacity():
    rows = read_table("results/live/V11_CAPACITY.md", "Cap (cores)")
    data = [(r[0], r[1], [NUM.search(x) for x in r[2:5]], r[5]) for r in rows if len(r) >= 6]
    data = [(cap, name, [(_num(m.group(1)), _num(m.group(3)), _num(m.group(4))) for m in ms], word) for cap, name, ms, word in data if all(ms)]
    fig = mpl_fig(0.5 * len(data) + 1.6)
    ax = fig.add_subplot(111)
    for k, (cap, name, pts, word) in enumerate(reversed(data)):
        col = reading_color(word)
        for j, (m, lo, hi) in enumerate(pts):
            y = k + 0.25 - 0.25 * j
            ax.plot([lo, hi], [y, y], color=col, lw=1.6); ax.plot([m], [y], "o", color=col, ms=3.5)
    ax.axvline(0, color=NAVY, lw=1)
    ax.set_yticks(range(len(data))); ax.set_yticklabels([f"cap {cap} cores:\n" + ("completed work, %" if "completed" in name else "work inside the line, req/s") for cap, name, _, _ in reversed(data)])
    ax.set_xlabel("paired change (percent, or requests a second),\nruns A, B, C from top; every row STEADY")
    fig.suptitle("The capacity test: four caps, five pairs a cap, three runs (omni-v11)", x=0.01, ha="left", fontsize=PT)
    return fig_svg(fig)


def r_mechanism():
    """The inputs the governor wrote beside the outputs the service showed, from the Goldilocks table (A, B, C)."""
    rows = read_table("results/live/V11_GOLDILOCKS.md", "Measure")
    want_in = [("settings commands the governor wrote", "settings commands written"), ("host CPU busy", "host CPU busy (%)"),
               ("utilisation", "utilisation (used / allocatable)"), ("CPU used (cores)", "CPU used (cores)"), ("Omni's own CPU", "the governor's own CPU (cores)")]
    want_out = [("response time (ms), mean", "response time, mean"), ("response time (ms), 95th", "response time, 95th"),
                ("response time (ms), 99th", "response time, 99th"), ("time over the response line", "time over the line"),
                ("alert minutes", "alert minutes"), ("energy, parked workers still on", "energy (idle-power model)")]
    def pick(keys):
        out = []
        for key, short in keys:
            for r in rows:
                if r[0].startswith(key) and len(r) >= 5:
                    ms = [NUM.search(x) for x in r[1:4]]
                    if all(ms):
                        out.append((short, (ms[0].group(2) or ""), [_num(m.group(1)) for m in ms], r[4])); break
        return out
    ins, outs = pick(want_in), pick(want_out)
    fig = mpl_fig(4.6)
    axs = fig.subplots(1, 2)
    for ax, data, title in ((axs[0], ins, "what the governor\nput in (runs A, B, C)"), (axs[1], outs, "what the service\nshowed (runs A, B, C)")):
        for k, (name, unit, vals, word) in enumerate(reversed(data)):
            col = reading_color(word)
            for j, v in enumerate(vals):
                ax.barh(k + 0.26 - 0.26 * j, v, height=0.24, color=col, alpha=0.5 + 0.25 * (j == 0))
        ax.set_yticks(range(len(data))); ax.set_yticklabels([wrap(n, 18) for n, _, _, _ in reversed(data)])
        ax.axvline(0, color=NAVY, lw=1); ax.set_title(title, loc="left"); ax.set_ylim(-0.6, len(data) - 0.4)
    axs[0].set_xlabel("change against native\n(percent, or a count)"); axs[1].set_xlabel("paired change against\nnative, %")
    return fig_svg(fig)


def r_realms():
    text = (ROOT / "results/realms_v5/REALMS_V5.md").read_text(encoding="utf-8")
    loads = [("the own load", "The seven organisms: the organism's own load"), ("the climb", "The seven organisms: the climb"), ("the line", "The seven organisms: work waiting in line")]
    series = []
    for lab, head in loads:
        a = text.find(head)
        chunk = text[a:a + 6000] if a >= 0 else ""
        rows = []
        for ln in chunk.splitlines():
            if ln.startswith("| ") and not ln.startswith("| Organism") and not ln.startswith("|---"):
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if len(cells) >= 7:
                    m = NUM.search(cells[5]); pg = NUM.search(cells[6])
                    if m:
                        rows.append((cells[0], _num(m.group(1)), _num(m.group(3)), _num(m.group(4)), _num(pg.group(1)) if pg else 0.0, cells[2]))
        series.append((lab, rows[:7]))
    orgs = [r[0] for r in series[0][1]]
    fig = mpl_fig(5.2)
    axs = fig.subplots(1, 2, sharey=True, width_ratios=[1.3, 1.0])
    cols = (NAVY, GOLD, GREEN)
    for j, (lab, rows) in enumerate(series):
        for k, r in enumerate(rows):
            y = k + 0.27 - 0.27 * j
            axs[0].barh(y, r[1], height=0.25, color=cols[j], xerr=[[r[1] - r[2]], [r[3] - r[1]]], ecolor=GREY, label=lab if k == 0 else None)
            axs[1].barh(y, r[4], height=0.25, color=cols[j])
    short = [wrap(o.replace("The four stacked, every shared muscle in each", "the four stacked").replace("The whole tower, every muscle once", "the whole tower")
                  .replace("The spine, the muscles every stack runs on", "the spine"), 22) for o in orgs]
    axs[0].set_yticks(range(len(orgs))); axs[0].set_yticklabels(short); axs[0].invert_yaxis()
    axs[0].axvline(0, color=INK, lw=0.8); axs[1].axvline(0, color=INK, lw=0.8)
    axs[0].set_xlabel("misses, percentage points\n(a fall is GAIN)"); axs[1].set_xlabel("power given,\n% of native's energy")
    fig.legend(loc="outside lower center", ncol=3, title="the load")
    fig.suptitle("every organism GAIN (fewer misses) under all three loads", x=0.01, ha="left", fontsize=PT)
    return fig_svg(fig)


def _grid_cells(section_start):
    """The grid of one half of GRID.md: {(organism, copies, runs): cell text}."""
    text = (ROOT / "results/grid_v5/GRID.md").read_text(encoding="utf-8")
    grid, head = {}, ""
    for h in re.split(r"^## ", text, flags=re.M):
        if not h.startswith(section_start):
            continue
        head = h.splitlines()[0]
        for sec in re.split(r"^### ", h, flags=re.M)[1:]:
            copies = sec.splitlines()[0].strip()
            if not re.fullmatch(r"\d+ cop(y|ies)", copies):
                continue
            for ln in sec.splitlines():
                if ln.startswith("| ") and not ln.startswith("| Organism") and not ln.startswith("|---"):
                    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                    if len(cells) >= 4 and cells[0] in ORGANISMS:
                        for j, runs in enumerate(("1 run", "10 runs", "100 runs")):
                            grid[(cells[0], copies, runs)] = cells[1 + j]
        break
    return head, grid


def _grid_label(cell):
    low = cell.lower()
    if not cell or "not in" in low:
        return "not in", "white"
    m = re.search(r"misses ([-+]?[\d.]+) pp", cell)
    pp = (m.group(1).replace("-", "−") + " pp") if m else ""
    g = re.search(r"GAIN on (\d+)", cell); lo = re.search(r"LOSS on (\d+)", cell)
    if low.startswith("gain"):
        return ("GAIN " + pp).strip(), "#cfe8cf"
    if low.startswith("loss"):
        return ("LOSS " + pp).strip(), "#f3c9c9"
    if low.startswith("one run") or low.startswith("one repetition"):
        return ("1 run " + pp).strip(), "#ededed"
    if g:
        if lo and int(lo.group(1)) > 0:
            return f"GAIN {g.group(1)}, LOSS {lo.group(1)}", "#f3c9c9"
        return f"GAIN on {g.group(1)}", "#cfe8cf"
    if low.startswith("even"):
        return ("STEADY " + pp).strip(), "#f6e7a6"
    if "pending" in low:
        return "pending", "white"
    return "·", "white"


SHORT_ORG = {"The spine": "the spine", "Compute / AI / Cloud": "Compute", "Physics / Robotics / Autonomous": "Physics",
             "Energy / Facility / Industrial": "Energy", "Distribution / Specialized": "Distribution", "The four stacked": "the four stacked",
             "The whole tower": "the whole tower"}


def grid_chart(section_start, title, key):
    head, grid = _grid_cells(section_start)
    copies_all = [c for c in ("1 copy", "10 copies", "100 copies", "1,000 copies", "1000 copies") if any(k[1] == c for k in grid)]
    runs_all = ("1 run", "10 runs", "100 runs")
    rows = [(o, c) for o in ORGANISMS for c in copies_all]
    fig = mpl_fig(0.3 * len(rows) + 1.6)
    ax = fig.add_subplot(111)
    for i, (o, c) in enumerate(rows):
        for j, r in enumerate(runs_all):
            label, col = _grid_label(grid.get((o, c, r), ""))
            ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor=col, edgecolor=GREY, lw=0.6))
            ax.text(j + 0.5, i + 0.5, label, ha="center", va="center", fontsize=PT, color=INK if col != "white" else GREY)
        if (i + 1) % len(copies_all) == 0:
            ax.plot([0, 3], [i + 1, i + 1], color=NAVY, lw=1.2)
    ax.set_xlim(0, 3); ax.set_ylim(len(rows), 0)
    ax.set_xticks([0.5, 1.5, 2.5]); ax.set_xticklabels(runs_all); ax.xaxis.tick_top()
    ax.set_yticks([k + 0.5 for k in range(len(rows))])
    ax.set_yticklabels([f"{SHORT_ORG[o]}, {c}" for o, c in rows])
    fig.suptitle(wrap(title + ". " + key, 78), x=0.01, ha="left", fontsize=PT)
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    return fig_svg(fig)


def r_grid():
    return grid_chart("Modelled", "Modelled (class S, our own models): the seven organisms at every size and run count, the change in misses against native",
                      "Green GAIN, yellow STEADY, red LOSS, light grey one run (no label yet), white not in the receipt")


def r_grid_kube():
    return grid_chart("With the real", "With the real Kubernetes cluster inside (the cluster class L, the organism class S): the seven organisms at every size and run count",
                      "Green: GAIN on n gauges, LOSS on none; red: a LOSS among them; light grey one repetition; white not in the report")


def _benefit_rows():
    rows = read_table("docs/BENEFIT_SHEET.md", "Date")
    data = []
    for r in rows:
        if len(r) < 6:
            continue
        m = re.search(r"([-+]?[\d.]+)%", r[4])
        if not m:
            continue
        word = re.sub(r"\*", "", r[3])
        name = re.sub(r",? Omni-Compass on top(, ten pairs)?(, three runs)?", "", r[1]).replace("Real Kubernetes", "Kubernetes")
        data.append((name, r[2], word, float(m.group(1))))
    return data


def benefit_chart(data, title):
    """The benefit as a percentage of improvement on a square-root axis with its ticks at 10, 25, 50 and 100%, so that a
    benefit of a few percent is a visible bar; a benefit over 100% is drawn to 100% and marked ► (the founder's order of
    16 October, night)."""
    import numpy as np
    fig = mpl_fig(0.5 * len(data) + 1.6)
    ax = fig.add_subplot(111)
    cap = 100.0
    for k, (bench, eng, word, v) in enumerate(reversed(data)):
        col = reading_color(word)
        ax.barh(k, min(max(v, 0.0), cap), color=col, height=0.7)
        if v > cap:
            ax.text(cap, k, " ►", va="center", ha="left", fontsize=PT, color=col)
        ax.text(cap * 1.06, k, f"{v:+.1f}% {word}\n({eng})", va="center", fontsize=PT, color=INK)
    ax.set_xscale("function", functions=(lambda x: np.sqrt(np.maximum(x, 0.0)), lambda y: np.square(y)))
    ax.set_xticks([0, 10, 25, 50, 100]); ax.set_xticklabels(["0", "10%", "25%", "50%", "100%"])
    ax.set_yticks(range(len(data))); ax.set_yticklabels([wrap(b, 34) for b, _, _, _ in reversed(data)], fontsize=PT)
    ax.axvline(0, color=NAVY, lw=1); ax.set_xlim(0, cap * 2.9)
    ax.grid(axis="x", color=RULE, lw=0.6, alpha=0.7)
    ax.set_xlabel("percentage of improvement against native (the Omni index's rule);\n"
                  "a square-root axis, so that a small benefit is a visible bar;\na bar past 100% is drawn to 100% and marked ►")
    fig.suptitle(wrap(title, 78), x=0.01, ha="left", fontsize=PT)
    return fig_svg(fig)


def r_benefit():
    data = _benefit_rows()
    return benefit_chart(data[:(len(data) + 1) // 2], "The benefit sheet, newest first: the newer half of its rows")


def r_benefit_b():
    data = _benefit_rows()
    return benefit_chart(data[(len(data) + 1) // 2:], "The benefit sheet, newest first: the older half of its rows")


# ---------------------------------------------------------------- structure
def _families():
    rows = list(csv.DictReader(open(ROOT / "realms/catalog_v5.csv", encoding="utf-8")))
    spine = [r for r in rows if r["realms"].count(";") == 3]
    groups = {"spine": {}}
    for r in spine:
        groups["spine"][r["family"]] = groups["spine"].get(r["family"], 0) + 1
    for realm in REALM_NAMES:
        g = {}
        for r in rows:
            if realm in r["realms"].split(";") and r["realms"].count(";") < 3:
                g[r["family"]] = g.get(r["family"], 0) + 1
        groups[realm] = g
    totals = {realm: sum(1 for r in rows if realm in r["realms"].split(";")) for realm in REALM_NAMES}
    return groups, totals, len(spine), len(rows)


def catalog_bars(keys):
    groups, totals, n_spine, n_all = _families()
    panels = []
    for key in keys:
        g = groups[key]
        if key == "spine":
            title = f"the spine: {n_spine} muscles in {len(g)} families, every one of them in all four realms"
        else:
            title = f"{REALM_NAMES[key]}: {totals[key]} muscles ({n_spine} of them the spine's); its own {sum(g.values())} muscles in {len(g)} families"
        panels.append((title, sorted(g.items(), key=lambda kv: (-kv[1], kv[0])), BLUE if key == "spine" else PALE))
    # one column, a row of 0.2 in a family: the longest family name still leaves the bar its room, and a realm's chart
    # takes about half a page, so the text that follows fills the rest (no dead space under a chart)
    n_rows = sum(len(p[1]) for p in panels)
    fig = mpl_fig(0.2 * n_rows + 0.8 * len(panels) + 0.5)
    axs = fig.subplots(len(panels), 1, height_ratios=[len(p[1]) + 2.5 for p in panels]) if len(panels) > 1 else [fig.add_subplot(111)]
    for ax, (title, fams, col) in zip(axs, panels):
        names = [f for f, _ in fams]; vals = [n for _, n in fams]
        ax.barh(range(len(fams)), vals, color=col, edgecolor=NAVY, height=0.72)
        for k, v in enumerate(vals):
            ax.text(v + 0.6, k, str(v), va="center", fontsize=PT)
        ax.set_yticks(range(len(fams))); ax.set_yticklabels(names); ax.set_ylim(len(fams) - 0.5, -0.5)
        ax.set_xlim(0, max(vals) * 1.15); ax.set_title(wrap(title, 52), loc="left")
        ax.tick_params(axis="y", length=0)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))   # a count of muscles: whole numbers on the axis
    axs[-1].set_xlabel(wrap(f"muscles in the family (the whole catalog: {n_all:,} distinct muscles in 70 families)", 52), loc="left")
    return fig_svg(fig)


def g_catalog():
    return catalog_bars(["spine", "physics_robotics_autonomous"])


def g_catalog2():
    return catalog_bars(["compute_ai_cloud"])


def g_catalog3():
    return catalog_bars(["energy_facility_industrial"])


def g_catalog4():
    return catalog_bars(["distribution_specialized"])


def g_pipeline():
    d = new_drawing()
    stages = [("audit.jsonl: one record a decision: senses, state, force, gate, write, read-back", BLUE),
              ("tools/live_reps.py: the paired receipt of one run: every gauge, native, omni, the change, its 95% interval", MIST),
              ("tools/confirm_abc.py: runs A, B, C → the three-run table; the engine of every run checked against the fingerprint", MIST),
              ("tools/readings.py: GAIN, STEADY, LOSS by the gauge's aim; the reading key on top of every table", PALE),
              ("docs/BENEFIT_SHEET.md, results/OMNI_INDEX.md: one number per benchmark, its word; the index over all", BLUE)]
    bw, bh = 4.0, 2.2
    boxes = []
    for k, (t, col) in enumerate(stages):
        row, c = divmod(k, 3)
        x = 0.4 + c * (bw + 0.3)
        y = -(row * (bh + 1.0)) - bh
        boxes.append(box(d, x, y, bw, bh, t, fill=col, color=NAVY))
    arrow(d, boxes[0].E, boxes[1].W); arrow(d, boxes[1].E, boxes[2].W); arrow(d, boxes[3].E, boxes[4].W)
    ymid = boxes[2].S.y - 0.5
    line(d, boxes[2].S, (boxes[2].S.x, ymid)); line(d, (boxes[2].S.x, ymid), (boxes[3].N.x, ymid)); arrow(d, (boxes[3].N.x, ymid), boxes[3].N)
    notes(d, 0.4, boxes[3].S.y - 0.4, "Every table is made by a tool, never by hand; raw records keep their recorded values, every page that shows them "
                                      "uses the words. A reader can follow one run from its audit line to its row in the benefit sheet.")
    return sd_svg(d)


def state_machine(states, edges, bottom):
    """States as rounded boxes at given positions; edges (a, b, label, kind) with kind 'line' or 'arc', drawn between
    the facing sides of the two boxes and numbered; the numbers are read in the key under the diagram, so that no label
    sits on a box."""
    d = new_drawing()
    pos = {}
    bw, bh = 2.9, 1.3
    for name, (x, y), kind in states:
        e = flow.RoundBox(w=bw, h=bh).at((x, y)).anchor("center").label(fit(name, bw, 0.3), fontsize=PT)
        e.fill(BLUE if kind == "end" else (MIST if kind == "box" else PALE)).color(NAVY)
        if kind == "end":
            e.linewidth(2.0)
        d += e
        pos[name] = e
    key = []
    for n, (a, b, label, kind) in enumerate(edges, 1):
        ea, eb = pos[a], pos[b]
        if a == b:
            d += elm.ArcLoop(arrow="->", radius=0.9).at(ea.NNW).to(ea.NNE).color(GREY)
            text_at(d, ea.N.x, ea.N.y + 1.0, str(n), GREY, halign="center", valign="bottom")
        else:
            dx, dy = eb.center.x - ea.center.x, eb.center.y - ea.center.y
            if abs(dx) >= abs(dy):
                pa, pb = (ea.E, eb.W) if dx > 0 else (ea.W, eb.E)
            else:
                pa, pb = (ea.N, eb.S) if dy > 0 else (ea.S, eb.N)
            k = {"arc": 0.25, "arc-": -0.25}.get(kind, 0.0)
            d += flow.Arc2(arrow="->", k=k).at(pa).to(pb).color(GREY).label(str(n), fontsize=PT, color=NAVY)
        key.append(f"{n}  {label}" if label else f"{n}  (no condition)")
    notes(d, min(e.W.x for e in pos.values()), bottom, "   ·   ".join(key))
    return sd_svg(d)


def g_modes():
    S = {"off": "OFF: native alone", "watch": "WATCHING: reads, logs, writes nothing", "auto": "AUTOPILOT: push, lift off, idle",
         "cruise": "CRUISE: every machine in service", "reset": "RESET: handed back, read back", "kill": "KILLED: handed back at once"}
    states = [(S["off"], (1.5, 0), "end"), (S["watch"], (4.9, 0), "state"), (S["auto"], (8.3, 0), "state"), (S["cruise"], (11.7, 0), "state"),
              (S["reset"], (8.3, -3.6), "state"), (S["kill"], (4.9, -3.6), "end")]
    edges = [(S["off"], S["watch"], "level 1", "arc"),
             (S["watch"], S["auto"], "the wire check passed; level 2 and up", "arc"),
             (S["auto"], S["cruise"], "pods waited 2 decisions", "arc"),
             (S["cruise"], S["auto"], "the line empty 2 decisions", "arc"),
             (S["auto"], S["reset"], "the reset file: the end of a run", "line"),
             (S["reset"], S["off"], "exit 0", "arc-"),
             (S["auto"], S["kill"], "the kill switch, from any mode", "line"),
             (S["watch"], S["kill"], "the kill switch", "line"),
             (S["auto"], S["auto"], "idle at once when demand is at zero", "line")]
    return state_machine(states, edges, bottom=-4.7)


def g_gpu_states():
    S = {"learn": "LEARNING: 15 busy readings of the card alone", "race": "RACE: both wires full, work waits",
         "steady": "STEADY: the busy clock as ceiling, no knock-backs", "pace": "PACE: 15 MHz steps, through the verdict",
         "fail": "FAIL UP: ceiling top, lid at the start limit", "obs": "OBSERVE ONLY: another writer owns the limit"}
    states = [(S["learn"], (1.5, 0), "state"), (S["race"], (6.5, 2.4), "state"), (S["steady"], (6.5, -2.4), "state"),
              (S["pace"], (11.5, 0), "state"), (S["fail"], (11.5, 4.4), "state"), (S["obs"], (11.5, -4.4), "end")]
    # omni_controller/gpu_compass.py: learning until --learn-samples busy readings; race while utilization ≥ --race-util;
    # steady only under an operator's cap (the start limit under the factory limit) while saturated at it; fail up and
    # observe-only are entered from any state
    edges = [(S["learn"], S["race"], "learned; utilization ≥ 95%", "arc"),
             (S["learn"], S["steady"], "learned; saturated at an operator's cap (draw ≥ 97% of it)", "arc"),
             (S["learn"], S["pace"], "learned; slack", "line"),
             (S["race"], S["pace"], "slack (the tune-down)", "arc"),
             (S["steady"], S["pace"], "off the cap: slack", "arc"),
             (S["pace"], S["race"], "work waits again", "arc"),
             (S["pace"], S["fail"], "from any state: p95 at the line, a failed request, a blind feed, a heat slowdown", "line"),
             (S["fail"], S["pace"], "clear for --slo-clear", "arc"),
             (S["pace"], S["obs"], "from any state: a limit not written by the governor", "line")]
    return state_machine(states, edges, bottom=-5.5)


def g_muscle_life():
    S = {"attach": "ATTACH: the snapshot", "check": "WIRE CHECK: 7 steps", "watch": "WATCH: recommend only", "govern": "GOVERN: write, read back",
         "foreign": "FOREIGN WRITER: observe only", "restored": "RESTORED: back as found"}
    states = [(S["attach"], (1.5, 0), "state"), (S["check"], (4.9, 0), "state"), (S["watch"], (8.3, 0), "state"),
              (S["govern"], (11.7, 0), "state"), (S["foreign"], (11.7, -3.6), "end"), (S["restored"], (6.6, -3.6), "end")]
    edges = [(S["attach"], S["check"], "the snapshot taken", "arc"), (S["check"], S["watch"], "WIRED RIGHT", "arc"),
             (S["check"], S["restored"], "FAIL: nothing written, the knob as found", "line"),
             (S["watch"], S["govern"], "the paired trial passed", "arc"),
             (S["govern"], S["govern"], "every decision: clamp, gate, write, read back, receipt", "line"),
             (S["govern"], S["foreign"], "the knob found where the governor did not put it", "line"),
             (S["govern"], S["restored"], "stop: reset, OFF, the lease", "arc"),
             (S["watch"], S["restored"], "stop before the trial passed", "arc")]
    return state_machine(states, edges, bottom=-4.7)


BUILDERS = {k: globals()[k] for k in FIGURES}


# ---------------------------------------------------------------- the interface build_book.py uses
_cache: dict = {}


def svg(key: str) -> str:
    if key not in _cache:
        _cache[key] = BUILDERS[key]()
    return _cache[key]


def drawing(key: str, width: float = FW):
    return svg_to_drawing(svg(key), width)


NOTICE = ("© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, "
          "commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass "
          "requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and "
          "printout carries this notice with LICENSE, NOTICE and DISCLOSURES.md. All patents, copyrights and trademarks filed "
          "in the USA. www.omni-compass.com")


def write_svgs(out: Path = OUT, keys=None) -> list:
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for key in (keys or FIGURES):
        s = svg(key)
        s = re.sub(r"<!DOCTYPE svg[^>]*>\s*", "", s, flags=re.S)
        s = re.sub(r"\n\s*<dc:date>[^<]*</dc:date>", "", s)       # no render date: a file changes only when its drawing does
        s = s.replace("<svg ", f"<!-- {NOTICE} -->\n<svg ", 1).rstrip() + f"\n<!-- {NOTICE} -->\n"
        p = out / f"{key}.svg"
        p.write_text(s, encoding="utf-8")
        paths.append(p)
    return paths


if __name__ == "__main__":
    keys = sys.argv[1:] or None
    for p in write_svgs(keys=keys):
        print(p.relative_to(ROOT))
