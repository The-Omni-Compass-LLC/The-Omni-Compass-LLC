#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live benchmark engine's glossary and index: every muscle of the catalog, every organism, every arm and every term a reader of
the live benchmark engine meets, each in the repository's own words, and where on the page each one appears.

The founder's words of 24 October: "That live benchmark engine better have at the back of it a glossary and index and what that means.
And that simply will have all 1,000 muscles and every other thing that should be in this so people know what it is. You can
bulk in the glossary the organisms by their realms ... I have the catalog."

Nothing here is typed twice. The muscles are realms/catalog_v5.csv, row for row; what each plant, class of machine and kind of
knob is, and what the max does with each muscle, are tools/muscle_catalog.py's words (the manuals' muscle appendix,
docs/MUSCLE_CATALOG.md); what the native controller under each plant is, is realms/plants.py's own docstring; who runs each
family natively and how it is wired is docs/wiring_recipes.csv. The organisms are made by the runners' own rules, imported, not
copied: the spine, the four realms, the four stacked and the tower by tools/run_realms_v5.py, the orchestra by
tools/run_orchestra.py (the governors' mapping of tools/governors_page.py), the live benchmark engine's sixty muscles by
docs/engine/export_harness_trace.py, the whole organism by docs/engine/export_whole.py and results/WHOLE_SYSTEM.json. Two arms,
native and Omni-Compass on native: Omni-Compass is never by itself (the founder's order of 25 October). Every term carries its definition, drawn from the file it names,
and a short quote from that file that this tool finds there before it writes anything: a term whose source no longer says what
it is cited for stops the build. The index reads docs/engine/OMNI_COMPASS_LIVE_ENGINE.html section by section (each
<section id="s-...">, its heading, its visible words and its monitors' own names) and keeps, for every term, organism and arm,
the anchors of the sections that print it. Once the page carries this record and its own glossary, both are left out of every
read (strip_glossary: the <script> holding this JSON, and any section whose id begins s-gloss or s-index), so the glossary is
never read back as the page's own words. The JSON holds no "</" and no "<!--", so it can sit inside a <script> element as it is.

  python3 tools/live_glossary.py            write docs/engine/glossary.json (compact, embeddable) and docs/engine/GLOSSARY.md
  python3 tools/live_glossary.py --check    exit 1 if either file differs from what the repository gives now
"""
from __future__ import annotations

import argparse
import csv
import html
import importlib.util
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.legal import PLAIN, stamp  # noqa: E402
from tools.muscle_catalog import TEMPLATE, KNOB, PRESET, does, card_text, nice  # noqa: E402
from realms.compass_arm_v5 import load_cards  # noqa: E402
from realms.harness import TOWER, STACK  # noqa: E402
import realms.plants as plants  # noqa: E402
import tools.run_realms_v5 as RR  # noqa: E402
from tools.run_orchestra import bodies, ORCHESTRA  # noqa: E402
from tools.governors_page import GOVERNORS  # noqa: E402

CATALOG = ROOT / "realms" / "catalog_v5.csv"
RECIPES = ROOT / "docs" / "wiring_recipes.csv"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
MONITORS = ROOT / "docs" / "engine" / "monitors.json"
OUT_JSON = ROOT / "docs" / "engine" / "glossary.json"
OUT_MD = ROOT / "docs" / "engine" / "GLOSSARY.md"
SIXTY, WHOLE = "sixty", "whole"


def _load(path: Path, name: str):
    """A module of docs/engine/ (not a package), loaded from its file."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


HARNESS_TRACE = _load(ROOT / "docs" / "engine" / "export_harness_trace.py", "_gloss_export_harness_trace")
EXPORT_WHOLE = _load(ROOT / "docs" / "engine" / "export_whole.py", "_gloss_export_whole")

REALM_KEYS = RR.REALMS                               # the four realms, in the order every table lists them
REALM_NAMES = {k: RR.NAMES[k] for k in REALM_KEYS}
PART_ORGAN = {"spine": ("nodes", 0.7), "compute": ("pods", 0.5), "physics": ("cpufreq", 0.3), "energy": ("power", 0.3),
              "distribution": ("routing", 0.5)}       # the page's own words, section 7c: each body part answers to one organ


# ------------------------------------------------------------------------------------------------ the repository's words
def _plants_entries(start: str, stop: str) -> dict:
    """{template: its paragraph} from one block of realms/plants.py's docstring (the five plant models; by plant and knob)."""
    doc = plants.__doc__
    block = doc[doc.index(start):doc.index(stop)]
    out, cur = {}, None
    for ln in block.split("\n"):
        m = re.match(r"^  (\w+)\s+(.*)$", ln)
        if m and m.group(1) in plants.TEMPLATES:
            cur = m.group(1)
            out[cur] = m.group(2).strip()
        elif cur and ln.startswith("   ") and ln.strip():
            out[cur] += " " + ln.strip()
        elif not ln.strip():
            cur = None
    return out


def templates() -> dict:
    """Each of the five plants: what it is and what Omni-Compass reads and moves (tools/muscle_catalog.py), its native
    controller and what each knob on it does (realms/plants.py)."""
    models = _plants_entries("Five plant models", "A muscle is one knob")
    by_knob = _plants_entries("By plant and knob", "Every disturbance trace")
    out = OrderedDict()
    for t, (what, reads, moves) in TEMPLATE.items():
        model = models[t]
        native = model.split("; native: ", 1)[1] if "; native: " in model else ""
        out[t] = {"what": what, "model": model.split("; native: ", 1)[0], "native": native, "reads": reads, "moves": moves,
                  "by_knob": by_knob.get(t, "")}
    return out


def knobs() -> dict:
    """The four kinds of knob, in tools/muscle_catalog.py's words: {knob: (short, full)}."""
    out = OrderedDict()
    for k, v in KNOB.items():
        full = re.sub(r"\*\*", "", v).split(": ", 1)[1]
        short = full.split(". ", 1)[0].rstrip(".")
        out[k] = {"short": short, "full": full}
    return out


def catalog_rows() -> list[dict]:
    return list(csv.DictReader(CATALOG.open(encoding="utf-8")))


def sort_key(r):
    """The muscle catalog's own order inside a family (tools/muscle_catalog.py): numbered rows first, then by their digits."""
    mid = r["muscle_id"]
    return (not mid.isdigit(), int("".join(c for c in mid if c.isdigit()) or 0), mid)


def is_spine(r) -> bool:
    return set(REALM_KEYS) <= set(r["realms"].split(";"))


def groups(rows) -> list[dict]:
    """The catalog bulked by its realms (the founder's words): the spine's families first, then each realm's own families,
    every muscle once, in the order docs/MUSCLE_CATALOG.md lists them."""
    out = []

    def fams(rs):
        f = OrderedDict()
        for r in rs:
            f.setdefault(r["family_id"], []).append(r)
        return [{"id": fid, "name": v[0]["family"], "muscles": [r["muscle_id"] for r in sorted(v, key=sort_key)]}
                for fid, v in f.items()]

    spine = [r for r in rows if is_spine(r)]
    out.append({"key": RR.SPINE, "title": "Spine", "note": f"{len(spine)} muscles in all four realms; an organism of its own",
                "families": fams(spine)})
    for k in REALM_KEYS:
        own = [r for r in rows if r["realm"] == k and not is_spine(r)]
        n = sum(1 for r in rows if k in r["realms"].split(";"))
        out.append({"key": k, "title": REALM_NAMES[k], "note": f"{len(own)} muscles of its own; {n} in its organism with the spine",
                    "families": fams(own)})
    return out


# --------------------------------------------------------------------------------------------------------- the organisms
def sixty_rows() -> list[dict]:
    """The live benchmark engine's sixty muscles, exactly as its recorder takes them from the catalog (docs/engine/export_harness_trace.py
    rows(): by name, the catalog's last row of a name winning), each with its body part."""
    return HARNESS_TRACE.rows()


def memberships(rows):
    """{muscle_id: {"organisms": [...], "governors": [...], "part": ...}} by the runners' own rules."""
    orch = bodies(rows)
    gov_of = {}
    for slug, *_ in GOVERNORS:
        for r in orch[slug]:
            gov_of.setdefault(r["muscle_id"], []).append(slug)
    orch_ids = {r["muscle_id"] for r in orch[ORCHESTRA]}
    part_of = {r["muscle_id"]: r["part"] for r in sixty_rows()}
    out = {}
    for r in rows:
        rl = r["realms"].split(";")
        orgs = ([RR.SPINE] if is_spine(r) else []) + [k for k in REALM_KEYS if k in rl] + [STACK, TOWER]
        if r["muscle_id"] in orch_ids:
            orgs.append(ORCHESTRA)
        if r["muscle_id"] in part_of:
            orgs.append(SIXTY)
        out[r["muscle_id"]] = {"organisms": orgs, "governors": gov_of.get(r["muscle_id"], []), "part": part_of.get(r["muscle_id"])}
    return out


def family_list(rs, weight=None) -> list[dict]:
    c, names = Counter(), {}
    for r in rs:
        c[r["family_id"]] += weight(r) if weight else 1
        names[r["family_id"]] = r["family"]
    return [{"id": fid, "name": names[fid], "n": n} for fid, n in sorted(c.items(), key=lambda kv: (-kv[1], int(kv[0])))]


def organisms(rows) -> list[dict]:
    """The ten organisms the page shows, in its order, each with its count, its families and its meaning in the repository's
    own words (each source quoted and checked like a term's)."""
    by = {k: [r for r in rows if k in r["realms"].split(";")] for k in REALM_KEYS}
    spine = [r for r in rows if is_spine(r)]
    orch = bodies(rows)
    six = sixty_rows()
    out = [{
        "key": RR.SPINE, "name": "Spine", "class": "S", "muscles": len(spine), "families": family_list(spine),
        "meaning": (f"The {len(spine)} muscles every real stack runs on, every one in all four realms: the computers' scheduling, "
                    f"placement, processors and memory, network, storage, observability, security, power and cooling, "
                    f"{len(family_list(spine))} families. An organism in its own right, the seventh, run "
                    "native and with Omni-Compass on top of native like the other six: the base every stack runs on, as an "
                    "operating system is the base of every program. Each spine muscle is also part of every realm's organism, "
                    "counted once in the tower and four times in the stack."),
        "sources": [{"file": "docs/THE_SPINE.md", "quote": "is the set of muscles every real stack runs on: the 267 muscles of the 1,107-muscle catalog"},
                    {"file": "docs/MUSCLE_CATALOG.md", "quote": "counted once in the tower and four times in the stack"}],
        "aka": ["the spine", "spine"]}]
    realm_aka = {"compute_ai_cloud": ["Compute / AI / Cloud", "Compute · AI · cloud", "compute, AI and the cloud"],
                 "physics_robotics_autonomous": ["Physics / Robotics / Autonomous", "Physics · robotics", "physics, robotics and autonomy"],
                 "energy_facility_industrial": ["Energy / Facility / Industrial", "Energy · facility", "energy, facilities and industry"],
                 "distribution_specialized": ["Distribution / Specialized", "distribution and specialized systems"]}
    for k in REALM_KEYS:
        own = [r for r in by[k] if not is_spine(r)]
        fam_own = family_list(own)
        out.append({
            "key": k, "name": REALM_NAMES[k], "class": "S", "muscles": len(by[k]), "own": len(own), "families": family_list(by[k]),
            "meaning": (f"Every muscle whose realm list includes {REALM_NAMES[k]}, the spine among them: its own {len(own)} "
                        f"muscles in {len(fam_own)} families of its trade (the largest: "
                        + ", ".join(f["name"] for f in fam_own[:4]) +
                        f") on the spine's {len(spine)}, {len(by[k])} in all, one organism on one clock, run native and with "
                        "Omni-Compass on top of native."),
            "sources": [{"file": "docs/MUSCLE_CATALOG.md", "quote": "each of the four realms (every muscle whose realm list includes it, the spine among them)"},
                        {"file": "docs/REALMS.md", "quote": "each realm's organism (its own families on the spine"}],
            "aka": realm_aka[k]})
    stack_n = sum(len(by[k]) for k in REALM_KEYS)
    out.append({
        "key": STACK, "name": "Four Stacked", "class": "S", "muscles": stack_n, "distinct": len(rows),
        "families": family_list(rows, weight=lambda r: len(r["realms"].split(";"))),
        "meaning": (f"The four realms stacked on one clock with every duplicate of the spine kept ({stack_n:,} muscles: the "
                    f"spine once in each realm's body). Each realm keeps its own body, so every muscle in the stack runs exactly "
                    "the native it runs in its own realm, plant by plant."),
        "sources": [{"file": "tools/run_realms_v5.py", "quote": "The four stacked keep each realm's own body on one clock"},
                    {"file": "CLAUDE.md", "quote": "the four stacked (1,908, the spine once in each realm's body)"}],
        "aka": ["the four stacked", "four stacked"]})
    out.append({
        "key": TOWER, "name": "Whole Tower", "class": "S", "muscles": len(rows), "families": family_list(rows),
        "meaning": (f"The whole catalog as one body, every muscle once: {len(rows):,} distinct muscles in "
                    f"{len(family_list(rows))} families, nine open-source pieces among them (Kepler, Climatik, "
                    "EAR, CruiseKube, Goldilocks, the Kubernetes Power Manager, PEAKS, Adaptive GPU Power Capping, NVIDIA's "
                    "platform power manager)."),
        "sources": [{"file": "CLAUDE.md", "quote": "the whole tower (1,107 distinct muscles in 70 families"},
                    {"file": "tools/run_realms_v5.py", "quote": "The whole tower, every muscle once"}],
        "aka": ["the whole tower", "the tower"]})
    govs = [{"slug": slug, "name": name, "muscles": len(orch[slug])} for slug, name, *_ in GOVERNORS]
    out.append({
        "key": ORCHESTRA, "name": "Orchestra Organism", "class": "S", "muscles": len(orch[ORCHESTRA]),
        "families": family_list(orch[ORCHESTRA]), "governors": govs,
        "meaning": (f"The eighth organism: every catalog muscle that stands for a knob "
                    f"of one of {len(govs)} governors and orchestrators (" + ", ".join(g["name"] for g in govs) +
                    f"), each governor's muscles a body of its own and all of them together one body, {len(orch[ORCHESTRA])} "
                    "muscles, native and with Omni-Compass on top, modelled. The governors themselves run live on real "
                    "Kubernetes, each as its project ships it with Omni-Compass on top."),
        "sources": [{"file": "tools/run_orchestra.py", "quote": "every catalog muscle that stands for a knob of a governor or orchestrator"},
                    {"file": "CLAUDE.md", "quote": "governors and orchestrators in their own"}],
        "aka": ["the orchestra", "orchestra"]})
    parts = OrderedDict()
    for r in six:
        parts.setdefault(r["part"], []).append(r["muscle_id"])
    dup = sorted(n for n, c in Counter(r["muscle"] for r in rows).items() if c > 1)
    out.append({
        "key": SIXTY, "name": "Live Organism", "class": "S",
        "muscles": len(six), "families": family_list(six),
        "parts": [{"part": p, "muscles": ids, "organ": PART_ORGAN[p][0], "theta": PART_ORGAN[p][1]} for p, ids in parts.items()],
        "meaning": ("The sixty muscles the page draws, twelve from the spine and twelve from each realm, put in one organism of "
                    "the realms harness (the plants of realms/plants.py coupled through their heat and their power) under the "
                    "climb, on seeds 3000, 3001 and 3002 (runs A, B and C). Native is the plants and their native controllers "
                    "alone; Omni-Compass on native is the max with the body's bone, its twins and the muscles' cards, and at 80% "
                    "of the run the brain goes silent and the lease walks every setting back to native over 24 decisions. On "
                    "the page each body part answers to one organ: the spine to nodes (θ 0.7), compute to pods (0.5), physics "
                    "to cpufreq (0.3), energy to power (0.3), distribution to routing (0.5)."
                    + (f" The recorder takes each muscle by its name; the name {dup[0]} is carried by two catalog rows, and the "
                       "catalog's last row of that name is the one in the record." if dup else "")),
        "sources": [{"file": "docs/engine/export_harness_trace.py", "quote": "The sixty muscles the page draws (twelve from the spine, twelve from each realm"},
                    {"file": "docs/engine/OMNI_COMPASS_LIVE_ENGINE.html", "quote": "the spine to nodes (θ 0.7), compute to pods (0.5), physics to cpufreq (0.3), energy to power (0.3), distribution to routing (0.5)"}],
        "aka": ["sixty muscles", "the sixty"]})
    out.append(whole_organism())
    return out


def whole_organism() -> dict:
    """The whole organism in three sectors: the software, the cloud as the wire between them, the bare metal (the groups of
    docs/engine/export_whole.py over the layers of results/WHOLE_SYSTEM.json), and the ways a stack is bought."""
    try:
        layers = list(json.loads(EXPORT_WHOLE.WS.read_text(encoding="utf-8"))["layers"])
    except (OSError, ValueError, KeyError):
        layers = []
    no = {EXPORT_WHOLE.layer_no(n): n for n in layers}
    grp = {k: (name, nos) for k, name, nos in EXPORT_WHOLE.GROUPS}
    sectors = []
    for k in ("software", "cloud", "hardware"):            # the software at one end, the cloud the wire, the bare metal at the other
        name, nos = grp[k]
        sectors.append({"key": k, "name": name,
                        "layers": [no.get(n) or EXPORT_WHOLE.NOT_RUN.get(n, f"layer {n}: not yet run") for n in nos]})
    ways = [{"key": k, "name": name, "pieces": list(p)} for k, name, p, _ in EXPORT_WHOLE.SCENARIOS]
    return {
        "key": WHOLE, "name": "Whole Organism", "class": "S of P and L", "muscles": None,
        "layers": len([s for g in sectors for s in g["layers"]]), "families": [], "sectors": sectors, "ways": ways,
        "meaning": ("Omni-Compass at every layer of a stack, each layer measured against its own native with the layer under it "
                    "as native runs it, composed by the product law into one benefit for the whole stack. Three sectors: the "
                    "software at one end (the cluster, its add-ons, its governors and the services on it), the bare metal at "
                    "the other (the card and the machine), and the cloud as the wire between them (the machines it bills, "
                    "metered). No run has stacked the layers yet: the composition is class S of class P and L measurements. "
                    "It is the tenth of the ten organisms, read like each of the others native and with Omni-Compass on top of "
                    "native. It has layers, not catalog muscles."),
        "sources": [{"file": "DISCLOSURES.md", "quote": "composes each layer's own measured ratio, native against Omni-Compass on top of native, into one benefit for a whole stack"},
                    {"file": "tools/whole_system.py", "quote": "the cloud is the wire between the chip at one end and the software at the other"},
                    {"file": "DISCLOSURES.md", "quote": "and the whole organism in its three places (the software end, the cloud's wire, the bare metal) composed above: ten organisms"}],
        "aka": ["the whole organism", "whole system"]}


# ------------------------------------------------------------------------------------------------------------- the arms
def arms() -> list[dict]:
    return [
        {"key": "native", "name": "native", "colour": "orange", "hex": "#ff8a1f", "aka": ["native"],
         "def": ("The whole system by itself with everything it ships with: every muscle under its own native controller "
                 "(the Kubernetes pod autoscaler, the GPU's firmware, the cooling, the batteries, a grid's tap changer, a "
                 "robot's servo). In the models, the plant and its native controller alone."),
         "sources": [{"file": "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md", "quote": "The whole system by itself with everything it ships with"},
                     {"file": "realms/harness.py", "quote": "native  the plant and its native controller alone"}]},
        {"key": "omni", "name": "Omni-Compass on native", "colour": "blue", "hex": "#4e97d1",
         "aka": ["Omni-Compass on native", "Omni-Compass and native", "Omni on native", "on top of native"],
         "def": ("The same system with Omni-Compass on top of all of it: every native controller still running underneath, "
                 "Omni-Compass setting only the knobs those controllers already expose. On Kubernetes, Omni-Compass on top of "
                 "Kubernetes on top of the muscles. The arm every table carried as \"omni\", its machine key unchanged."),
         "sources": [{"file": "CLAUDE.md", "quote": "Omni on native is Omni on top of Kubernetes on top of the muscles"},
                     {"file": "CLAUDE.md", "quote": "Omni-Compass and native (the arm every table carried as \"omni\", its machine key unchanged)"}]},
    ]


def scenarios(orgs, arm_list) -> list[dict]:
    """Every organism under both arms: 10 × 2, named."""
    out = []
    for o in orgs:
        for a in arm_list:
            s = {"key": f"{o['key']}/{a['key']}", "organism": o["key"], "arm": a["key"], "name": f"{o['name']} · {a['name']}"}
            if o["muscles"] is not None:
                n = o["muscles"]
                if a["key"] == "native":
                    s["what"] = f"{n:,} muscles, each under its own native controller alone."
                elif a["key"] == "omni":
                    s["what"] = f"the same {n:,} muscles, every native controller running, Omni-Compass on top of all of them."
            else:
                s["what"] = {"native": "every layer as native runs it.",
                             "omni": "Omni-Compass on top of every piece, composed layer by layer."}[a["key"]]
            out.append(s)
    return out


# ------------------------------------------------------------------------------------------------------------ the terms
def run_live(s: str) -> str:
    """A family's live cell (docs/wiring_recipes.csv) as the page prints it after "Run live:": its leading "live" said once, and
    nobody's name in it."""
    s = s.replace(" by the founder's order", "")
    for a, b in (("live: ", "yes, "), ("live in part: ", "in part, "), ("live on ", "on ")):
        if s.startswith(a):
            return b + s[len(a):]
    return s


def T(term, group, d, sources, aka=(), note=None):
    t = {"term": term, "group": group, "aka": list(aka), "def": d, "sources": [{"file": f, "quote": q} for f, q in sources]}
    if note:
        t["note"] = note
    return t


R, A, L, B, D, P, C, G, W = ("Result Readings", "Arms and Placement", "Compass Law and Plug", "Brain and Nervous System",
                             "Controls and Tuning", "Proof and Evidence", "Catalog and Organisms", "Runs and Grid",
                             "Page and Monitors")
IGT = "tools/injection_grid.py"   # the injection grid (25 October)
FP = "docs/FACTORY_PROFILE.md"    # the common language of the factory profile, the tuning bench and the bill (24 October)
PAGE_F, CL, DIS, RD, MAN = ("docs/engine/OMNI_COMPASS_LIVE_ENGINE.html", "CLAUDE.md", "DISCLOSURES.md", "tools/readings.py",
                            "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md")
LAW, NERV, CORE, ARM5, THEO = ("omnicompass/compass_law.py", "omnicompass/nervous_system.py", "omnicompass/core.py",
                               "realms/compass_arm_v5.py", "docs/book/THEORY.md")
TERMS = [
    # ------------------------------------------------------------------------------------------------- reading a result
    T("GAIN", R, "The gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or "
      "failures, or a resource cut. Decided by what the gauge is for, never by the plus or minus sign of its number; its size is "
      "printed without a sign (GAIN 73.0%), the raw change apart with its true sign. G.A.I.N.: Growth, Advantage, Improvement, Net-positive. Green.",
      [(RD, "the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures")]),
    T("STEADY", R, "A change under 0.5% (the mean of the three runs' changes under the floor), no change at all, or a knob native "
      "already runs at the top of its range (at its limit on native). A change of 0.5% or more is never STEADY. Of three kinds: "
      "exactly the same (to nine decimal places), under the floor (a measured change under 0.5%), and, in a table read by an older "
      "key, no difference beyond the noise. Its size is printed without a sign (STEADY 0.3%), the raw change apart. S.T.E.A.D.Y.: Stable, True to baseline, Equilibrium, At par, Drift-free, Yield held. Yellow, and the yellow of the traffic signal on every "
      "monitor carries the same word.",
      [(RD, "STEADY is kept for a change under 0.5%"), (RD, "the top of its range is STEADY, at its limit on native")]),
    T("LOSS", R, "The gauge moved away from its declared aim against native: less work done, a longer wait, more misses or "
      "failures. A LOSS row is never cut: its cause is found and fixed (our own wiring first, then native's setup, then the "
      "scoring) and the test is run again. Its size is printed without a sign (LOSS 16.8%), the raw change apart with its true sign. L.O.S.S.: Leakage, Off-track, Setback, "
      "Subpar. Red.",
      [(RD, "the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures"),
       (RD, "is found and fixed (our own wiring first, then native's setup, then the scoring)")]),
    T("power given", R, "A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor "
      "time, a bill, wear) that rose: what Omni-Compass put in to buy the work and the speed shown beside it, always shown and "
      "never called a loss. The same resource falling is a cut, a GAIN. Work per energy that falls is power given too. Blue on a "
      "reading.",
      [(RD, "A rise is **power given**: what Omni put in to buy the work"),
       (MAN, "on a reading, power given")], aka=["power given"]),
    T("the runs disagree", R, "Runs that moved 0.5% or more in opposite directions: the test is unstable there and is looked "
      "into.", [(RD, "**The runs disagree**: runs moved 0.5% or more in opposite")],
      aka=["the runs disagree", "runs disagree"]),
    T("shown, not judged", R, "A gauge declared in advance as shown only, such as the knob's own setting; counted in no total. "
      "Grey.", [(RD, "SHOWN = \"shown, not judged\"                 # declared in advance as shown only")], aka=["shown, not judged"]),
    T("the 0.5% floor", R, "A change of half of one percent (0.5%) or more either way is a change: GAIN, LOSS or power given by "
      "what the gauge is for. The change is the mean of the three runs' changes, each in percent of native; a mean under 0.5% "
      "reads STEADY, under the floor, with its size; every change of 0.5% or more shows its word.",
      [(RD, "percent (0.5%) or more either way is a change, and reads **GAIN** or **LOSS** (or **power given**) by what the gauge "),
       (RD, "A mean under 0.5% reads **STEADY, under the floor**, with its size.")],
      aka=["the floor", "under the floor", "0.5%"]),
    T("the raw change and the word", R, "Two numbers, never mixed: every row shows native's "
      "value, Omni-Compass's value and the raw change, (Omni-Compass − native) / native, with its true sign; the word beside it is "
      "judged by what the gauge is for, and the size printed beside a word carries no sign. A wait that fell 3% prints raw −3.0% and "
      "GAIN 3.0%; failed requests that rose 2% print raw +2.0% and LOSS 2.0%.",
      [(RD, "Two numbers, never mixed")], aka=["sign beside a word", "number beside a word", "raw change"]),
    T("the key", R, "GAIN, STEADY and LOSS, with power given and the letters behind each word: The Omni-Compass LLC's own convention "
      "for reading its own results, in the words of underwriting and actuarial work, where every outcome is graded as surplus, "
      "break-even or deficit. Not an actuarial, financial or insurance opinion; no outside body defined, reviewed or approved it.",
      [(RD, "they are the words of underwriting and actuarial work"),
       (RD, "are The Omni-Compass LLC's own convention")], aka=["the one key", "the key", "reading key"]),
    T("do no harm", R, "Omni-Compass's one goal: to strengthen the organism it governs and keep it healthy, working at the best "
      "state its own muscles can carry. Harm is judged at the organism: less output than native (less work; more time waited, "
      "missed or failed) or less health (a muscle past its own limit, a service over its own line, anything made to fail). Every "
      "muscle only as far as it can go, never past. The engine that stands keeps the strictest form: every muscle judged on "
      "itself, never below native, nothing traded between muscles; where it cannot bring a knob a GAIN, that knob stays native.",
      [(DIS, "Omni-Compass has one goal: to strengthen the organism it governs and keep it healthy"),
       (DIS, "Harm is judged at the organism.")], aka=["do no harm"]),
    T("at its limit on native", R, "A knob native already runs at the top of its range: the max has nothing above native to "
      "give it, so Omni-Compass reads it and leaves it native. It reads STEADY.",
      [(CL, "A knob native already runs at the top of its range is \"at its limit on native\"."),
       (ARM5, "Whether native already runs this kind of knob at the top of its range, so the max has nothing above native to")],
      aka=["at its limit on native"]),
    T("alert minute", R, "A whole minute whose 95th percentile, failed requests counted over, was over the line: a minute over "
      "the line wakes a person. In the cloud the aim is no alert minute at all; one on Omni-Compass's side is found and fixed, "
      "never accepted.", [(MAN, "whole minutes whose 95th percentile, failed requests counted over, was over the line"),
                          (CL, "a minute over the line wakes a person")], aka=["alert minute", "alert minutes"]),
    # ------------------------------------------------------------------------------------------------------- the arms
    T("Omni-Compass", A, "A supervisory governor. It always sits on top of a native controller and never in its place: the "
      "Kubernetes pod autoscaler, GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo. It treats each setting "
      "a native controller already exposes as a muscle and the whole stack as one body. Headline: more work, faster, on fewer "
      "machines, with less energy.",
      [(CL, "Omni-Compass is a **supervisory governor**."),
       (CL, "Headline: more work, faster, on fewer machines, with less energy.")]),
    T("native", A, "The whole system by itself with everything it ships with: every muscle under its own native controller. Every "
      "benchmark's baseline, and the controller Omni-Compass always sits on top of. Amber on the page.",
      [(MAN, "The whole system by itself with everything it ships with"),
       (CL, "It always sits **on top of a native controller**")], aka=["native"]),
    T("Omni-Compass on native", A, "The same system with Omni-Compass on top of all of it, every native controller still "
      "running underneath. On Kubernetes, Omni-Compass on top of Kubernetes on top of the muscles. The arm every table carried as "
      "\"omni\", its machine key unchanged. Blue on the page.",
      [(CL, "Omni on native is Omni on top of Kubernetes on top of the muscles")],
      aka=["Omni-Compass on native", "Omni-Compass and native", "Omni on native", "on top of native"]),
    T("the yardstick", A, "Kubernetes' published autoscaling rule, written by us from its documentation (a description of a rule, "
      "not Kubernetes' code): the native that Omni-Compass on native is read against in the real three-run test of section 2a, "
      "the Scorecard.",
      [("docs/OMNI_ORCHESTRATOR.md", "as the yardstick Omni is read against")], aka=["yardstick"]),
    T("the three places Omni-Compass lives", A, "Omni-Compass sits at both ends of the cloud's wire and at every layer between: "
      "the software end (the cluster, Kubernetes, its add-ons, its governors and the services on it), the cloud between them (the "
      "machines it bills, metered) and the bare metal (the card, the chip, and the machine: the kernel, bare metal, Kepler).",
      [("tools/whole_system.py", "Omni-Compass sits at both ends and at every layer between"),
       ("tools/whole_system.py", "the machine (the kernel, bare metal, Kepler)")],
      aka=["bare metal", "the software end"]),
    T("the cloud as the wire", A, "The cloud is the wire between the chip at one end and the software at the other. A cloud run "
      "can show only the bill of the machines it parks: through the cloud the bare metal belongs to the provider (no tenant can "
      "read its meters or write its chips' limits), so the cloud's benefit is what the provider itself meters and bills, the "
      "machines counted every fifteen seconds and the bill at list price. Every cloud set runs Omni-Compass at the tune-down on "
      "the machines alone: the same work as native for a smaller bill, never a bigger one. The work and the speed live on the "
      "software end and the bare-metal end.",
      [("tools/whole_system.py", "the cloud is the wire between the chip at one end and the software at the other"),
       (DIS, "The cloud's back end is not ours to meter."),
       (CL, "the same work as native for a smaller bill, never a bigger one")], aka=["the cloud", "the bill"]),
    # -------------------------------------------------------------------------------------------- the law and the plug
    T("the compass", L, "The word for the band every reading is held in and for the whole mechanism drawn as one picture (the "
      "Omni-Compass rose). The law is omnicompass/compass_law.py (CompassLaw): a band with 5% cushions, two antagonist forces, "
      "smooth (tanh), not hammering.",
      [(CL, "a band with 5% cushions, two antagonist forces, smooth (tanh), not hammering"),
       (THEO, "The Omni-Compass rose is the whole mechanism drawn as one picture.")], aka=["compass"]),
    T("the compass law", L, "One smooth law for every muscle: the service reading is placed as a position in its band, "
      "p = (r − lo)/(hi − lo) (0 calm, 1 the service line), and the force is F = A·tanh((k[p]·(p − centre) + k[d]·v)/A). It "
      "fails up past the 0.95 wall; a positive force adds capacity, power, cooling or speed, a negative force takes it back.",
      [(LAW, "The compass: one smooth law for every muscle, and the plug every muscle is wired through.")],
      aka=["compass law", "CompassLaw"]),
    T("the band", L, "A reading's safe range, from calm (p = 0) through its centre (p = 0.5) to its line (p = 1); the walls run to "
      "0.05 and 0.95, and the last 5% on each side is cushion (10% in all) before the line. Where a reading sits in it is its "
      "compass position.", [(LAW, "the walls run to 0.05 and 0.95, and the last 5% on each side is cushion (10% in all) before the line")],
      aka=["band", "compass position"]),
    T("the cushion", L, "The last 5% of the band on each side before the line; from 1 − cushion the force is the whole authority A, "
      "so a muscle is never let past the line. In the max the cushion moves with each muscle's own risk (the edge).",
      [(LAW, "the last 5% on each side is cushion"),
       (PAGE_F, "from 1 − cushion the force is the whole authority A: a muscle is never let past the line")],
      aka=["cushion", "cushions"]),
    T("the centre", L, "The bottom of the compass, 0.5 by default, where the two forces balance: below it the force pulls capacity "
      "back, above it pushes capacity in.",
      [(LAW, "the brain pulls it to the bottom of the compass, the center (0.5 by default)"),
       (PAGE_F, "where the two forces balance; below it the force pulls capacity back, above it pushes capacity in")], aka=["the centre", "the center"]),
    T("the two antagonist forces", L, "Up: a positive force adds capacity, power, cooling or speed (scale out, raise a clock, start "
      "a chiller). Down: a negative force takes it back (scale in, lower a limit, warm a setpoint). Each side has its own gain, "
      "because adding and taking back do not cost the same.",
      [(LAW, "Two forces (antagonist pairs)"), (LAW, "because adding and taking back do not cost the same")],
      aka=["two antagonist forces", "antagonist", "two forces"]),
    T("k[p]", L, "The spring: the pull k[p] × (position − centre), gentle near the bottom, harder up the walls.",
      [(LAW, "K_P x (position - center): gentle near the bottom, harder up the walls")], aka=["k[p]", "k_p", "the spring"]),
    T("k[d]", L, "The damping: k[d] × velocity meets whatever is shoving the position (a load rising, heat building) with an equal "
      "and opposite push. Chosen for critical damping, k[d] = max(0, 2√(k[p]·τ/dt) − 1)·dt, the reading glides to the centre and "
      "stops, no overshoot, no ringing. Some wires set it at three times that, so a rising load is met before it reaches the wall "
      "(the Kubernetes governor, the GPU governors, the realms' arms and the grid's runner); the data stores' runners, the "
      "orchestrator's brain and the other simulators keep the class's critical damping. The page's section 5h lists every wire, "
      "read from the repository at each build.",
      [(LAW, "K_D x velocity: whatever is shoving the position"),
       ("omni_controller/controller.py", "self.compass_law.kd *= 3.0"),
       (PAGE_F, "Which wires multiply k_d by three")], aka=["k[d]", "k_d", "the damping"]),
    T("A", L, "The authority: the force's ceiling. The force is A × tanh(raw / A), a spring near the centre that bends over and "
      "flattens into its maximum A, never a corner, never a hammer.",
      [(LAW, "the force is A x tanh(raw / A)")], aka=["the authority", "A·tanh"]),
    T("tanh", L, "The hyperbolic tangent the force is passed through so that it is smooth and never hammers: the same shape the "
      "engine already uses for v_eff (omnicompass/core.py).",
      [(LAW, "the same shape the engine already uses for v_eff")], aka=["tanh"]),
    T("fail up", L, "Past the 0.95 wall the up side goes to its full force at once, and the down side may not act until the "
      "position is back inside the compass.", [(LAW, "past the 0.95 wall the up side goes to its full force at once")],
      aka=["fails up", "fail up"]),
    T("the two-way plug", L, "A muscle is a plug with one wire in and one wire out: it reads its meters and writes its lever, "
      "clips each write to the cover, reads back what the device took, restores the snapshot at the end, and stops writing if it "
      "finds the lever at a value the brain did not write (one writer). All the thinking is in the brain, written once for every "
      "muscle.", [(LAW, "A muscle is a plug with one wire in and one wire out."),
                  (CL, "Wiring is a two-way plug, one wire in and one wire out.")], aka=["plug", "two-way plug", "one wire in"]),
    T("the snapshot", L, "The lever's value read once, before the first write; restore puts the lever back to it, and it never "
      "moves after that. Reset hands everything back to it.",
      [(LAW, "the lever back to the snapshot, the value read once before the first write"),
       (PAGE_F, "the snapshot taken once at the start is what reset restores")], aka=["snapshot", "snapshotted"]),
    T("the cover", L, "The outer band: the lever's hard range (the device's or the buyer's lowest and highest setting). Every "
      "write is clipped to it, so nothing the math does can set the lever outside.",
      [(LAW, "the outer band, the lever's hard range")], aka=["the cover"]),
    # ---------------------------------------------------------------------------------------- the brain and its nerves
    T("the four pieces", B, "The engine is built in four pieces, each feeding the next. In the software they are the engine's state "
      "equations (piece 1: deviation, alignment, memory and basin), the basin potential and its flow (piece 2), the bath that "
      "absorbs and redistributes (piece 3), and the one governor that couples every muscle to one law with no outside authority "
      "(piece 4). The mechanism panel turns each piece's constants live.",
      [(THEO, "the four pieces appear as the engine's state equations (piece 1: deviation, alignment, memory and basin)")],
      aka=["four pieces", "the brain's four pieces"]),
    T("piece 1, the state and the basin", B, "Energy E (dE/dt = −α_E E + β_int + β_ext + v_eff: how fast stress energy "
      "drains), unity U on a double well with two basins at U = ±1 (dU/dt = μU(1 − U²) − (dE/dt)/E_max − λ_U U + u), and its "
      "integral I[U], the remembered shortfall (dI_U/dt = (1 − U) − σ₁E − δS − λ_I I_U). The command u = −U̇ + K[P]·(1 − U), "
      "bounded by U[auth], brings unity back to its basin at U = 1.",
      [(PAGE_F, "Piece 1, State and Basin"),
       (CORE, "(2) dU/dt = mu U (1 - U^2) - (dE/dt)/E_max - lambda_U U + u")],
      aka=["E, U, I[U]", "I_U", "I[U]", "unity U", "the basin"]),
    T("piece 2, the basin's potential and flow", B, "dS/dt = δ − α_s S − ¾β_s S² = −Φ′(S), with "
      "Φ(S) = α_s S²/2 + β_s S³/4 − δS: the basin state S rolls down its potential Φ(S) to a stable bottom, S*, the root of "
      "dS/dt = 0.",
      [(CORE, "(5) Phi(S) = alpha_s S^2 / 2 + beta_s S^3 / 4 - delta S"),
       (THEO, "the basin state S rolls down its potential Phi(S) to a stable bottom")], aka=["Φ(S)", "Phi(S)"]),
    T("piece 3, the bath", B, "A damped oscillator driven by the flow: dB/dt = Ḃ, dḂ/dt = γ_c δS − (ω_B/Q_B)Ḃ − ω_B² B; its "
      "beat enters energy through v_eff = cos(ω_B t/2)·c·tanh(λ₀ + λ₁(U − ½) + λ₂S). In the theory, the bath that absorbs and "
      "redistributes.",
      [(CORE, "(7) dB/dt = B_dot ; dB_dot/dt = gamma_c delta S - (omega_B/Q_B) B_dot - omega_B^2 B"),
       (PAGE_F, "Piece 3, Bath")], aka=["the bath", "B_dot"]),
    T("piece 4, the governor's law", B, "The governor's law (omnicompass/adapter.py, nervous_system.py): "
      "push and the utilisation target ρ* from the state, and the nerves' grants to every organ: one law for every muscle, with "
      "no outside authority.",
      [(PAGE_F, "Piece 4, Governor Law"),
       (THEO, "the one governor that couples every muscle to one law with no outside authority (piece 4)")],
      aka=["one law coupling every muscle", "the governor's law"]),
    T("RK4", B, "The fourth-order Runge–Kutta step that integrates the engine's six states (E, U, I_U, S, B, Ḃ): ten micro steps "
      "over 0.1·k of the engine's time a decision, k = the decision's period over 60 s (omni-v16's period rule; 0.01 each at one "
      "decision a minute); 20 macro steps of 10 micro steps in the core's Monte Carlo, the bounded command held across the four "
      "stages.",
      [(CORE, "six-state ODE, RK4 integrator"), (PAGE_F, "RK4, ten micro steps over macro_dt = 0.1·k"),
       ("tools/core_runs.py", "the fourth-order Runge–Kutta step, 20 macro steps of 10")], aka=["RK4", "Runge–Kutta", "Runge-Kutta"]),
    T("push", B, "The command the brain asks for to bring unity back to its basin, as a share of its authority: "
      "push = clip(−f_U + 12(1 − U), ±25)/25. A push above κ's knee holds every give-back.",
      [(PAGE_F, "push = clip(−f_U + 12(1 − U), ±25)/25")], aka=["push =", "the push", "push_release"]),
    T("ρ*", B, "The engine's utilisation target: how full a muscle may run after a give-back, "
      "ρ* = clamp(ρ₀ − k_I I_U − k_E E, ρ_min, ρ₀); the live controller reads it clamped to 0.5 to 0.95.",
      [(PAGE_F, "ρ* = clamp(ρ₀ − k_I I_U − k_E E, ρ_min, ρ₀)"),
       ("realms/plants.py", "The engine's utilisation target as the live controller reads it.")], aka=["ρ*", "utilisation target"]),
    T("κ", B, "Convergence, the first of the nerves' four scalars: κ = 1 while push ≤ push_release, else push_release / push. The "
      "further the engine is from its basin, the less it may give back.",
      [(NERV, "kappa convergence = 1 if push <= push_release, else push_release / push")], aka=["κ", "convergence"]),
    T("h", B, "Basin health: h = clamp((U − U_gate)/(1 − U_gate), 0, 1).",
      [(NERV, "h basin health = clamp((U - U_gate) / (1 - U_gate), 0, 1)")], aka=["basin health"]),
    T("σ", B, "The stress ratio σ = S/S*, where S* solves δ − α_s S − ¾β_s S² = 0; above 1 it holds every give-back. (On the "
      "console σ also names the noise knob's spread, 1 + σ·z.)",
      [(NERV, "sigma stress ratio = S / S*")], aka=["σ", "stress ratio"]),
    T("ν", B, "Unmet need: ν = max(0, I_U).", [(NERV, "nu unmet need = max(0, I_U)")], aka=["ν", "unmet need"]),
    T("calm", B, "The nerves' one number, calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)), in [0, 1]; 1 means fully settled. An organ may "
      "hand capacity back only while calm ≥ its threshold θ, the line is clean and every sense is live; continuous organs shed "
      "at most the calm share of their surplus a decision.",
      [(NERV, "in [0, 1]; 1 means fully settled"),
       (MAN, "the nerves' one number, against which each organ's threshold θ grants a hand-back")], aka=["calm"]),
    T("the organs and their grants", B, "The organ families the nerves grant authority to: pods, nodes, cpufreq, gpu, power, "
      "batch, routing and rollback. Expanding is always allowed except during a security hold; contracting (giving capacity "
      "back) only when calm ≥ the organ's reversibility threshold θ (pods 0.5; nodes 0.7, since a node costs a boot to reverse; "
      "cpufreq, gpu and power 0.3; routing 0.5) and the service is clean.",
      [(NERV, "Only when calm >= the organ's reversibility threshold"),
       (NERV, 'THETA = {"pods": 0.5, "nodes": 0.7, "cpufreq": 0.3, "gpu": 0.3, "power": 0.3, "routing": 0.5}')],
      aka=["θ", "organ", "organs", "grant", "grants"]),
    T("the nervous system", B, "One evolving engine state granting authority to every organ family. Omni-Compass does not replace "
      "the specialist controllers (the HPA and VPA size pods, the Cluster Autoscaler and Karpenter size node pools, Linux "
      "schedutil picks CPU frequency, NVIDIA DCGM manages GPUs); the nervous system decides, from one shared state, the envelope "
      "inside which each of them may act.",
      [(NERV, "The supervisory nervous system: one evolving engine state grants authority to every organ family.")],
      aka=["nervous system", "nerves"]),
    T("the immune system", B, "Omni-Compass's own: native twins of every room and pool, the heat debt, the cure on the spot, the "
      "pools' give-back and the bone's grant (V6 to V13). Reactive and proactive: it answers a breach at once, and it acts before "
      "a line is crossed.",
      [(MAN, "Omni-Compass's: native twins, the heat debt, the cure on the spot, the pools' give-back, the bone's grant."),
       (DIS, "Like an immune system, the brain answers a breach at once, and it acts before a line is")],
      aka=["immune system"]),
    T("the heat debt", B, "The body's power that would carry, over one decision, the heat by which the rooms that cannot cure "
      "themselves stand warmer than their twins. The pools hand it back (the other muscles kick in): the max's added machines go "
      "back until no such room is warmer than native's.",
      [(ARM5, "the max's added machines go back until no such room is warmer than native's")], aka=["heat debt"]),
    T("the twin", B, "The brain's model of native: what the operator's own autoscaler would have had with no cap, on the same "
      "arrivals and the same rules (the HPA's tolerance, its scale-down window, the machines' start time); every room wired by "
      "its setpoint has one too, under its operator's setpoint and native's heat. The max never leaves a pool with fewer machines "
      "than its twin, nor a room warmer.",
      [(ARM5, "What the operator's own autoscaler would have had with no cap")],
      aka=["the twin", "its twin", "the twins", "native twins", "pool's twin"]),
    T("the bone", B, "The body's skeleton for the max: the lines every muscle stands on (a site's grid line, a room's cooling), "
      "loaded by the whole body. What the max adds is granted only out of the room the most loaded line has left, read one "
      "decision ahead; with no room, the machines this brain added go back at once, never below the pool's twin.",
      [(ARM5, "The body's skeleton for the max: the lines every muscle stands on.")], aka=["bone"]),
    T("the edge", B, "The compass's balance point is not a fixed middle: it moves with each muscle's own risk, at 1 − cushion, "
      "cushion = climb × reaction + z × wobble (z = 3.09: 99.9% of steps inside the cushion), widened at once when the need rises "
      "and narrowed slowly when it falls, as a driver doubles the following distance the moment rain starts.",
      [("omnicompass/edge.py", "The v5 edge: the compass's balance point is not a fixed middle, it moves with each muscle's own risk.")],
      aka=["the edge"]),
    T("the reflex rule", B, "A new setting is earned by a trial on the muscle itself, read from the muscle's own reaction: the urge "
      "proposes, the reaction disposes. A trial runs to its full measurement and is never ended by the calm it causes; one trial "
      "at a time inside a body; nothing permanent; the wall belongs to the body.",
      [(THEO, "The urge proposes; the reaction disposes."),
       (THEO, "a trial runs to its full measurement and is never ended by the calm it causes")], aka=["reflex"]),
    T("the release gate", B, "Giving a unit back only when nothing is waiting and, after the release, the rest runs at or under the "
      "engine's utilisation target.",
      [("realms/plants.py", "through a release gate (nothing waiting, and after the release the rest runs at or under the engine's utilisation target)")],
      aka=["release gate"]),
    # ------------------------------------------------------------------------------------------------------- driving it
    T("the max", D, "The default brain: every muscle runs at its own limit, never past it and never below native; it "
      "rides the edge, not the middle. The energy it takes is power given, shown beside the work, the speed and the wear it "
      "bought, never called a loss.",
      [(CL, "every muscle runs at its own limit, never past it and never below native; it rides the edge, not the middle")],
      aka=["the max", "at the max", "under the max"]),
    T("the tune-down", D, "The dial's other setting (V5SAVE): never more than native, capacity handed back only with the organ's "
      "grant and the release gate: the same work with less. Every cloud set runs at the tune-down.",
      [(MAN, "the tune-down (never more than native)"),
       (PAGE_F, "Tune-down: never more than native; capacity handed back only with the organ's grant and the release gate."),
       (CL, "Every cloud set runs Omni-Compass on top at the tune-down")], aka=["tune-down", "V5SAVE"]),
    T("the dial", D, "The choice between the max (every muscle to its own limit, never below native; the default) and the "
      "tune-down (never more than native). Anyone can tune Omni-Compass down from the max.",
      [(MAN, "The max (every muscle to its own limit, never below native; the default) or the tune-down (never more than native)."),
       (CL, "Anyone can tune it down from the max")], aka=["dial"]),
    T("one pedal", D, "Like an electric car, one pedal: push for more, lift off for less; lifting hands the setting back toward "
      "native; idle is the pedal lifted all the way; reset hands everything back to native.",
      [(CL, "push for more, lift off for less; lifting hands the setting back toward native"),
       (CL, "idle is the pedal lifted all the way; reset hands everything back to native")], aka=["pedal", "one pedal"]),
    T("lift-off", D, "Lifting the pedal: a force below zero moves the setting toward native's by min(1, base + slope·|F|) a "
      "decision. Under the max, lifting off toward native never needs the nerves' grant; going below native does.",
      [(CL, "lift off for less"),
       (PAGE_F, "Under the max, lifting off toward native never needs this grant; going below native does.")],
      aka=["lift-off", "lift off", "lifting off"]),
    T("cruise", D, "One of the pedal's states beside idle and reset, with autopilot, watching and off: cruise is for a known queue "
      "waiting. The Kubernetes governor's cruise wait is never fewer than two readings (omni-v17).",
      [(CL, "cruise (a known queue waiting), autopilot / watching / off"),
       (CL, "the cruise wait is now never fewer than two readings")], aka=["cruise"]),
    T("the lease", D, "The governor's proof of life, renewed every decision. If a governor dies without handing back (killed "
      "outright, the machine crashed, it hung), the watchdog finds any governor whose process is gone or whose lease is older "
      "than its limit and walks every setting back to native, gradually (in the models over 24 decisions).",
      [(MAN, "The governor's proof of life; when it ages past its limit the watchdog walks every setting back to native."),
       ("omnicompass/master.py", "renews a lease every decision"),
       ("realms/harness.py", "decisions over which the lease walks every setting back to native after the brain goes silent")],
      aka=["lease"]),
    T("the kill switch", D, "The master switch, for security only and instant: one switch in a human hand turns Omni-Compass's "
      "governing off everywhere at once. At its next decision every governor puts every setting it ever wrote back to the value "
      "it read before its first write, reads each one back, writes its last audit line and exits. Separate from the lease's "
      "gradual walk back after a crash.",
      [("omnicompass/master.py", "one switch in a human hand turns Omni-Compass's governing off everywhere at once")],
      aka=["kill switch", "master switch"]),
    T("the heartbeat", D, "The governor's full decision, one turn of its loop: read, decide, write, renew the lease. The main "
      "engine takes it every 60 s (omni-v17 on); the controller takes any beat from 5 to 120 s (--interval), and the page offers "
      "five, 15, 30, 60, 90 and 120 s, each shown beside native with what it buys and what it costs.",
      [(CL, "the main engine takes its full decision every 60 s"),
       (MAN, "One turn of the governor's loop: read, decide, write, renew the lease.")], aka=["heartbeat", "beat", "the heart"]),
    T("the fast checks", D, "The governor's checks between its beats, every 5 s at every beat: the scheduling floor, the pod "
      "reflex, and the conveyance every 15 s. Native's pod autoscaler checks every 15 s.",
      [(PAGE_F, "the fast checks (the scheduling floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat"),
       (CL, "Its fast checks already run every 5 s (native's pod autoscaler: 15 s)")], aka=["fast checks", "fast check"]),
    T("the conveyance", D, "Moving a conserved budget between organs (site watts, cluster cores): moved, never created, down the "
      "gradient of need. On Kubernetes the governor raises a running pod's processor limit in place to the room its machine can "
      "still give under 75% busy, bounded by the namespace's quota, and hands every limit back to the operator's on a shared "
      "host at its top: the unit answers at its machine's speed, not its paper quota's, with no unit and no machine added.",
      [("docs/CONVEYANCE_LAW.md", "The conveyance law: moving a conserved budget between organs"),
       ("docs/OMNI_ORCHESTRATOR.md", "a unit answers at its machine's speed, not its paper quota's, with no unit and no machine added"),
       (CL, "conveyance bounded by each namespace's CPU quota"), (CL, "every limit given goes back to the operator's")],
      aka=["conveyance", "conveyed"]),
    T("the factory tune", D, "The engine as The Omni-Compass LLC tuned and ships it, every muscle on the setting found for it "
      "(its own card where one was kept, the engine's own setting otherwise). Every published benchmark result is one engine at "
      "its one factory tune; a changed tune's results are the tuner's own. One button returns every knob to it.",
      [(DIS, "Every published benchmark result is one engine at its one factory tune"),
       (PAGE_F, "Every knob back to the factory tune")], aka=["factory tune"]),
    T("the live tuning engine", D, "The live benchmark engine page and its control panel: every knob, button and monitor turns in real time "
      "to show the mechanism of action with native alone, with Omni-Compass on top, or both; what it shows at any other setting "
      "is the engine's range, never a benchmark result.",
      [(DIS, "The live benchmark engine page and the control panel are a live tuning engine")], aka=["live tuning engine"]),
    # ------------------------------------------------------------------------------------------------ proof and evidence
    T("the verdict", P, "Omni-Compass moves a knob only where it measures that the muscle loses nothing by it. The trial step is "
      "read as a report reads a row: the 95% interval of its change in cost, on the logarithm of each piece of work's cost. "
      "Wholly above zero is a LOSS: refused and undone. A GAIN or a STEADY step is kept only within the 2% allowance. The 2% "
      "verdict is the engine's trigger, not a stamp on a report.",
      [("omnicompass/verdict.py", "The verdict: Omni-Compass moves a knob only where it measures that the muscle loses nothing by it."),
       (CL, "is the engine's trigger, not a stamp on a report")], aka=["verdict", "2% allowance"]),
    T("the give-back trial", P, "Every give-back is tried in its own paired trial, while the service is calm: the muscle with and "
      "without it, under the same load (the knob at native first, the reference, then one step past the deepest step already "
      "allowed), and undone if the muscle loses by it.",
      [(PAGE_F, "every give-back is tried in its own paired trial (the muscle with and without it, under the same load) and undone if the muscle loses by it"),
       ("omnicompass/verdict.py", "then at one step past the deepest step already")],
      aka=["give-back trial", "give-back", "give-backs"]),
    T("the model gate", P, "Every change to the engine or a live controller runs first in our own models (class S), against the "
      "engine that stands, on the same seeds, before any real run is started. A change goes on to real runs only where it reads "
      "no LOSS there and shows promise; a LOSS there is root-caused and fixed in the model.",
      [("tools/model_gate.py", "against the engine that stands, on the same seeds, before any real run is started")],
      aka=["model gate"]),
    T("the fingerprint and its digest", P, "Every engine version fingerprinted file by file: one SHA-256 per file and one over the "
      "sorted list, its digest. A result belongs to a version only if the commit it ran on carries "
      "exactly that version's bytes; no result is read across versions.",
      [("tools/omni_version.py", "One SHA-256 per file, and one over the sorted list.")],
      aka=["fingerprint", "digest", "fingerprinted"]),
    T("the seal", P, "Every law that exists in Python and in C++, locked together: results/SEAL.json records each twin's Python "
      "and C++ files and the parity test that proved them equal, so a change to either side breaks the seal until its parity "
      "test passes again.",
      [("tools/seal.py", "The seal: every law that exists in Python and in C++, locked together.")], aka=["seal", "sealed"]),
    T("the C++ twin", P, "The engine's laws written again in C++ (the core, the governor, the compass law, the verdict), each held "
      "equal to its Python by a parity test under the seal; the Python's runs fed through the C++ engine give the same digest.",
      [(PAGE_F, "C++ Twin"),
       ("tools/seal.py", "A change to either side of a twin breaks the seal until its parity test passes")],
      aka=["C++ twin", "C++"]),
    T("evidence classes P, L, S", P, "The class every number carries: P a physical meter (a real card's own power meter), L live "
      "software (real Kubernetes on GitHub's machines), S our own models (modelled). A model is a statement about the model; "
      "only a meter speaks for hardware. S is never presented as proof.",
      [(MAN, "The evidence class of a number: a physical meter, live software, our own models."),
       (DIS, "A model is a statement about the model.")], aka=["evidence class", "class P", "class L", "class S"]),
    T("modelled", P, "The word for our own models (class S) in every report; live software is the real thing (class L); a meter is "
      "class P.", [(CL, "they are \"modelled\" (class S)")], aka=["modelled", "our own models"]),
    T("three runs A, B and C", P, "Each benchmark runs three times as separate GitHub runs, A, B and C, on the same frozen engine. "
      "\"GAIN in all three of our runs\" means A, B and C moved the same way with every 95% interval clear of zero; otherwise "
      "a change of 0.5% or more reads by the mean of our three runs, with the count of runs beyond the noise. Run and scored by "
      "The Omni-Compass LLC's own code; no outside party has reviewed or approved these results.",
      [(RD, "**GAIN, LOSS or power given in all three of our runs**: A, B and C moved the same way, "),
       ("tools/confirm_abc.py", "one v1 benchmark run three times as separate GitHub runs on the same")],
      aka=["A, B and C", "three runs", "all three of our runs"]),
    T("the 95% interval on Student's t", P, "Every interval is the two-sided 95% point of Student's t for its degrees of freedom, "
      "computed (no table) by bisection on the distribution's own CDF and rounded to three decimals as the printed tables are.",
      [("omnicompass/student_t.py", "The two-sided 95% point of Student's t distribution, for any number of degrees of freedom, computed (no table).")],
      aka=["95% interval", "Student's t", "Student t"]),
    T("Monte Carlo", P, "The Python's Monte Carlo of the engine's core: N runs from the jump generator, each through the six "
      "states and the RK4 step, controlled, uncontrolled (native), aimed at the wrong basin and with the double well's μ at 0; a "
      "run is conveyed when its U has stayed in one basin for 5 macro steps in a row and certified at 10. One digest, and the "
      "live benchmark engine's own port and the C++ twin held to it. Class S.",
      [("tools/core_runs.py", "The Python's Monte Carlo of the engine's core from the jump generator: N runs, one digest, the live engine's own port held to it.")],
      aka=["Monte Carlo"]),
    T("the jump generator", P, "The seed of run k: seed_k = base + k·0x9E3779B9, mod 2³², feeding a mulberry32 stream (the page's "
      "own generator), so the Python, the C++ and the page draw the same runs and prove each other receipt by receipt.",
      [("tools/engine_runs.py", "One run k draws its seed from the jump generator (seed_k = base + k·0x9E3779B9, mod 2³²)")],
      aka=["jump generator"]),
    T("the injection", G, "One seed of the Python's batch, seed_k = base + k·0x9E3779B9 mod 2³² (the jump generator): every plant of "
      "every organism draws its demand noise, its weather and its disturbances from it, under the climb, for 240 decisions of 15 s. "
      "The same injection reaches every organism and every way, native, Omni-Compass on native, each governor on the organism and "
      "Omni-Compass on top of each governor, so each one's reaction to the same thing is read side by side.",
      [(IGT, "one seed: every plant of every organism draws its demand noise, its weather and its disturbances from it"),
       (IGT, "The same injection reaches every organism and every arm.")], aka=["injection", "injections"]),
    T("the injection batch", G, "One set of the Python's 500 injections, named by its base and by the SHA-256 digest of the Python's "
      "runs of it; the C++ engine runs the same seeds and must give the same digest (section 5a). Every cell of the injection grid is "
      "drawn from one batch; another batch is another run in the key's sense, and three batches make a three-run reading.",
      [(IGT, "The batch. One set of the Python's jump generator (tools/engine_runs.py): base B, 500 injections, injection k drawing its")],
      aka=["injection batch", "batch of 500"]),
    T("the injection grid", G, "Every organism with a plant, each native and with Omni-Compass on native, and each of the fourteen "
      "governors sitting on it, on one injection batch, at 1, 10, 100 and 500 runs × 1, 10, 100 and 500 organisms stacked (section "
      "5c). Run k of a cell stacks M copies, copy c on injection k + c (mod 500); each cell is read by the key over its N runs. The "
      "page re-hashes the record and recomputes every cell's mean from the runs' means. Class S.",
      [(IGT, "The grid. Runs N in 1, 10, 100, 500 and organisms stacked M in 1, 10, 100, 500.")],
      aka=["injection grid"]),
    T("organisms stacked", G, "In the injection grid, M copies of one organism run side by side on one clock, each on its own "
      "injection: separate clusters sharing no power line or room, every gauge the mean of the copies' per muscle. The scale grid "
      "of section 5e stacks its copies in one body instead.",
      [(IGT, "copies are separate clusters on one clock: they share no power line or room, so a stacked run's every gauge is the mean of its")],
      aka=["stacked organisms"]),
    T("a governor's way", A, "The third arm in our models: a governor or orchestrator (the Kubernetes scheduler and its bin-packing "
      "profile, Kueue, Volcano, KAI, Koordinator, CruiseKube, Crane, KubeRay, Gödel, Armada, Karmada, Open Cluster Management, "
      "KubeEdge, Nephio) as the body of the catalog muscles that stand for its knobs, sitting on the organism's clock on the same "
      "injections; Omni-Compass on top of the governor governs both bodies. Read per muscle, like for like. Its knobs run under "
      "their own native controllers, so it reads native's work index by construction; the governors as their projects ship them "
      "run on real Kubernetes in section 4e (class L).",
      [(IGT, "The governors, the third arm. Each of the fourteen governors and orchestrators"),
       (IGT, "Per muscle. Every gauge is read per muscle")], aka=["third arm", "governor's way"]),
    T("a cell's reference", G, "IG/base/organism/way|against/NxM/gauge: the name of one cell of the injection grid (for example "
      "IG/1488855732/tower/on_native|native/500x1/work), printed under the cell, copied by its button and typed back into the "
      "reference box to reach the same cell on any copy of the page that holds that batch.",
      [(IGT, "python3 tools/injection_grid.py [--base B] [--workers N] [--organisms a,b] [--runs 500] [--cache DIR]")],
      aka=["cell reference"]),
    T("the engine that stands", P, "The engine version on main, named on the page's title block and printed by python3 "
      "tools/omni_version.py (this glossary's engine field names it); every benchmark runs again on it.",
      [(MAN, "The engine version on main, named on the page's title block")], aka=["engine that stands"]),
    # ------------------------------------------------------------------------------------- the catalog and the organisms
    T("the organism", C, "A set of muscles stepped together on one clock, each muscle from its own plant model with its own native "
      "controller, the whole fed one demand from one seed, so that the heat the machines make is load on the rooms, the body's "
      "power swing is load on every site's line, and one brain judges every step against every other muscle's cushion.",
      [(THEO, "An organism is a set of muscles stepped together on one clock")], aka=["organism", "organisms"]),
    T("muscle", C, "One setting on one machine that already has its own control: a replica target, a node pool's size, a GPU's "
      "clock ceiling, a chiller's setpoint, a battery's reserve, a joint's effort. Omni-Compass may hold that knob and only that "
      "one; the native controller keeps the rest. The muscle's name is the setting's own name on its controller.",
      [("docs/MUSCLE_CATALOG.md", "is one setting on one machine that already has its own control"),
       ("realms/plants.py", "A muscle is one knob of one plant.")], aka=["muscle", "muscles"]),
    T("realm", C, "One of the four trades the catalog is cut into: Compute / AI / Cloud; Physics / Robotics / Autonomous; Energy / "
      "Facility / Industrial; Distribution / Specialized. A muscle sits in one realm, or, as a spine muscle, in all four; each "
      "realm's organism is its own families on the spine.",
      [("docs/REALMS.md", "each realm's organism (its own families on the spine")], aka=["realm", "realms"]),
    T("family", C, "A group of muscles on one kind of machine with one native controller and one wiring recipe; 70 in the catalog. "
      "docs/wiring_recipes.csv gives each family's native controller, wire out, wire in, restore, and whether that wire has run "
      "live.", [("docs/MUSCLE_CATALOG.md", "Each family's entry says which native controller owns its muscles")],
      aka=["family", "families"]),
    T("template", C, "The plant model a muscle is modelled on, one of five (realms/plants.py): compute_pool, thermal_zone, "
      "energy_storage, motion_axis and process_loop. Each carries its own native controller and runs correctly with no Omni at "
      "all.", [("realms/plants.py", "Five plant models. Each one carries its own native controller and runs correctly with no Omni at all:")],
      aka=["template", "plant model"]),
    T("knob", C, "Which of four kinds of setting a muscle is: capacity (how much of the machine is in service), admission (what is "
      "let in), power (the power share or limit the machine may draw) or setpoint (the target the machine's own loop holds).",
      [("docs/MUSCLE_CATALOG.md", "how much of the machine is in service (replicas, instances, units, speed)")],
      aka=["knob", "knobs"]),
    T("preset", C, "The parameter set of a muscle's plant, one per class of machine (server, node, gpu, data_hall, microgrid, "
      "robot_joint and the rest): round engineering figures for the class of machine, not measurements of any product. The class "
      "also decides how such a muscle is reached in a real stack.",
      [("realms/presets.py", "Values are round engineering figures for the class of machine, not measurements of any product.")],
      aka=["preset", "class of machine"]),
    T("the spine", C, "The muscles every real stack runs on: the 267 of the catalog whose realm list names all four realms, in 13 "
      "families (scheduling, placement, processors and memory, network, storage, observability, security, power and cooling). An "
      "organism in its own right, the seventh: the base every stack runs on, as an operating system is the base of every program.",
      [("docs/THE_SPINE.md", "is the set of muscles every real stack runs on: the 267 muscles of the 1,107-muscle catalog")],
      aka=["the spine", "spine"]),
    T("the stack", C, "The four realms stacked on one clock, every duplicate of the spine kept: 1,908 muscles, the spine once in "
      "each realm's body.", [(CL, "the four stacked (1,908, the spine once in each realm's body)")],
      aka=["the four stacked", "four stacked"]),
    T("the tower", C, "The whole catalog as one body, every muscle once: 1,107 distinct muscles in 70 families.",
      [(CL, "the whole tower (1,107 distinct muscles in 70 families")], aka=["the whole tower", "tower"]),
    T("the orchestra", C, "The eighth organism: every catalog muscle that stands for a knob of the fourteen governors and orchestrators "
      "(the Kubernetes scheduler, Kueue, Volcano, the KAI scheduler, Koordinator, CruiseKube, Crane, KubeRay, Gödel, "
      "Armada, Karmada, Open Cluster Management, KubeEdge, Nephio), each governor's muscles a body of its own and all together "
      "one body, native and with Omni-Compass on top, modelled.",
      [("tools/run_orchestra.py", "every catalog muscle that stands for a knob of a governor or orchestrator")],
      aka=["the orchestra", "orchestra"]),
    T("the seven organisms", C, "The spine, the four realms, the four stacked and the whole tower: each run native and with "
      "Omni-Compass on top of native on the same seed, the same load and the same clock.",
      [(THEO, "Omni-Compass is benchmarked on seven organisms")], aka=["seven organisms"]),
    T("the stress-test model", C, "A model drawn for the page so the body can be stressed by hand (a surge, a blind sense, a "
      "security hold, the kill switch), class S: sixty muscles named from the catalog, each a capacity lever with its own response "
      "time and sensing delay under an HPA-style native controller, run native and Omni-Compass side by side on the same demand.",
      [(PAGE_F, "A model drawn for this page so the body can be stressed by hand")], aka=["stress-test model"]),
    # --------------------------------------------------------------------------------------------- the runs and the grid
    T("the line", G, "The limit a reading must not cross: a response time, a temperature, a feed's rating. Over the line, work is "
      "waiting or failing.", [(PAGE_F, "the limit it must not cross: a response time, a temperature, a feed's rating")],
      aka=["the line", "service line", "response line", "over the line", "past the line", "its line"]),
    T("the climb", G, "A load stepping by one, up and down (1 2 3 2 3 4 …): level 4 is the organism's own load and level 8 twice "
      "it, so the organism is pushed past what native can carry and the most each arm can do shows.",
      [("realms/harness.py", "the climb: the load steps by one, up and down (1 2 3 2 3 4 ...)")], aka=["the climb", "climb"]),
    T("work waiting in line", G, "The third load: work already waiting when the run starts, a quarter of the work the run itself "
      "brings, so the arm that clears it sooner is faster.",
      [("realms/harness.py", "the line: work already waiting when the run starts, a quarter of the work the run itself brings"),
       ("tools/run_realms_v5.py", "the arm that clears it sooner is faster")],
      aka=["work waiting in line", "waiting in line"]),
    T("the grid", G, "Each organism native and with Omni-Compass at 1, 10 and 100 copies × 1, 10 and 100 paired "
      "runs, modelled and with the real cluster inside, both values in every square; the 1,000 tier on GitHub's own machines "
      "only; paid cloud and GPU runs stay at 1, 10 and 100 copies with at most 100 repetitions. Copies is the size of the body one "
      "brain governs; runs is the number of independent paired trials.",
      [(CL, "clustered copies × runs: 63 squares (seven organisms) at 1, 10 and 100 copies × 1, 10 and 100 runs"),
       (THEO, "Copies is the size of the body one brain governs")], aka=["grid", "copies"]),
    T("protocol 4", G, "With the cluster inside, only runs of protocol 4 count: the governor never below the organism's CPU "
      "priority, its decisions counted inside the window; the model of the organism on the runner's last core and the kind nodes "
      "on the others, the same in both arms; the served image pulled onto every worker before each arm.",
      [(CL, "With the cluster inside only runs of protocol 4 count")], aka=["protocol 4"]),
    T("the conductor", G, "The program that starts the runs (scripts/dispatch_grid.py, every 15 minutes): it starts every run not "
      "yet started, reads started runs back from their names, never starts one twice, and keeps the queue at what GitHub runs "
      "plus a margin; it also releases every benchmark's reruns on the engine that stands and the cloud sets.",
      [(CL, "starts every run not yet started, reads started runs back from their names, never starts one twice")],
      aka=["conductor"]),
    T("Omni index", G, "One number for more for the same, or the same for less: every measure of every test turned into a ratio "
      "oriented so that above 1 is a GAIN (work, speed, machines, energy or the bill); a test's index is the geometric mean of "
      "its ratios, minus one, in percent; the headline is the geometric mean of the real categories, each weighted the same. The "
      "modelled muscles are shown beside it, never inside it.",
      [("tools/omni_index.py", "The Omni index: one number for more for the same, or the same for less")], aka=["Omni index"]),
    # ------------------------------------------------------------------------------------------------------------ the page
    T("the benefit board", W, "Every benchmark's measured effect in one board, native against Omni-Compass on top of native, by "
      "domain and by gauge family, with the Omni index that weighs them together; every bar is its table's own word (GAIN green, "
      "STEADY yellow, LOSS red, power given blue) beside its size.",
      [(PAGE_F, "measured effect in one board")], aka=["benefit board"]),
    T("the traffic signal", W, "Every monitor's light, read on its band: green GAINING, low in its "
      "band with room to climb; yellow STEADY, inside its band; red REDLINING, at the top of its band and holding there, blinking red "
      "and black; red OVER THE LINE, past its band, blinking red and white; grey, and said so, where there is no line. On a record "
      "the colour is the reading's word: GAIN green, STEADY yellow, LOSS red. A needle that falls is not a LOSS and one that rises is "
      "not a GAIN: each light reads what its gauge is for. The light moves with its monitor: it reads the series the monitor draws. "
      "Every signal shows all four live words, the lit one bright and the rest dim, on native's side and on Omni-Compass's side "
      "alike: Omni-Compass's redline reflex is built never to let a muscle redline, and the red is still wired, so that if one does "
      "(a fault, a bug) it is seen at once, and the kill switch hands everything back to native in the same instant. The engine "
      "that stands carries the rule in its immune system, knob by knob, landed on 25 October (omnicompass/immune.py and its C++ twin "
      "cpp/src/immune.cpp): over its line three decisions, stuck, and native's twin lower by more than 5%, the knob is handed to "
      "native for 10 decisions, doubling up to 160; where native is not stronger Omni-Compass stays. The page's live model applies "
      "the same rule, with the engine's own numbers, to every muscle it draws.",
      [(PAGE_F, "GAINING: low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN)"),
       (PAGE_F, "STEADY: inside its band, or level with native (STEADY, a change under 0.5%)"),
       (MAN, "| Yellow | STEADY |")], aka=["traffic signal", "traffic light", "light", "lights"]),
    T("GAINING", W, "Green on the traffic signal: low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN).",
      [(PAGE_F, "GAINING: low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN)")], aka=["GAINING"]),
    T("REDLINING", W, "Red on the traffic signal, blinking red and black: at the top of its band and holding there, or Omni-Compass "
      "behind native now (a LOSS). Red means LOSS and the alarm only, never native.",
      [(PAGE_F, "REDLINING: at the top of its band and holding there, blinking red and black, or Omni-Compass behind native now (a LOSS)")],
      aka=["REDLINING"]),
    T("OVER THE LINE", W, "Red on the traffic signal, blinking red and white: past the top of its band, the alarm. Omni-Compass's own "
      "law hands a muscle back toward native before its line (the fail-up at the band's 95% wall), so this light is what a line "
      "crossed looks like, on whichever side crossed it.",
      [(PAGE_F, "OVER THE LINE: past the top of its band, blinking red and white: the alarm")], aka=["OVER THE LINE", "over the line"]),
    T("AWAITING", W, "A dark light, never green: the run that fills this monitor has not landed yet, and the light stays dark until "
      "it does.", [(PAGE_F, "AWAITING: the run that fills this monitor has not landed yet; its light stays dark until it does, never green")],
      aka=["AWAITING"]),
    T("native's colour", W, "Orange (#ff8a1f, the page's --steel): the word native and every line, bar, lane, tile and number that "
      "belongs to native's side wear it. Red is only a LOSS and the alarm.",
      [(PAGE_F, "the sides: --brass is Omni-Compass (blue), --steel is Native (orange; red is only LOSS and the alarm)"),
       (MAN, "| Orange | native |")], aka=["orange"]),
    T("the heartbeat's six buttons", D, "On the page the governor's full decision comes at one of six beats, 10, 15, 30, 60, 90 or "
      "120 s; 10 s shows a beat below the 15 s standard. The factory's beat is the engine's own (60 s on omni-v19). The page's "
      "live model steps every 15 s, so at 10 s two full decisions land in every other step, both on that step's reading.",
      [(PAGE_F, "the heartbeat (10, 15, 30, 60, 90 or 120 s)"), (FP, "Δ ∈ {10, 15, 30, 60, 90, 120} s")],
      aka=["heartbeat buttons", "the six beats", "the five beats"]),
    T("governing engine", A, "The executable mathematical rules that turn observations and internal state into governing decisions.",
      [(FP, "The executable mathematical rules that turn observations and internal state into governing decisions.")],
      aka=["governing engine", "the governing engine"]),
    T("native baseline", A, "The system's documented configuration and behaviour with no Omni-Compass governing it: every muscle "
      "under its own native controller, as its vendor ships it.",
      [(FP, "The system's documented configuration and behaviour with no Omni-Compass governing it")], aka=["native baseline"]),
    T("factory profile", D, "The complete, versioned set of Omni-Compass default settings shipped together: the governing rules, "
      "gains, margins, decision interval and every other default. Selected after the mechanisms are verified, candidates are tested "
      "together and the choice is validated on fresh workloads; frozen at release, while the engine's state, commands and "
      "allocations go on responding. Today's is omni-v19's; the best validated factory profile is not yet established.",
      [(FP, "The complete, versioned set of Omni-Compass default settings shipped together."),
       (FP, "Freezing the factory profile fixes the released rules and default tuning.")], aka=["factory profile", "the factory profile"]),
    T("candidate profile", D, "A proposed combination of settings under evaluation; on the page, the best beat of a sweep with the "
      "factory's other knobs (\"Try the candidate\"). It becomes a factory profile only after validation and a new release.",
      [(FP, "A proposed combination of settings under evaluation."), (PAGE_F, "Try the candidate")], aka=["candidate profile", "candidate"]),
    T("active profile", D, "The settings actually governing the current run, named on the page as factory, candidate or custom with "
      "its fingerprint.", [(FP, "The settings actually governing the current run.")], aka=["active profile"]),
    T("custom profile", D, "An identifiable configuration that differs from the released factory profile; its fingerprint names it "
      "and its results are its own.", [(FP, "An identifiable configuration that differs from the released factory profile.")],
      aka=["custom profile"]),
    T("live tuning bench", W, "The interface that operates the engine's controls and displays their effects through the connected "
      "backend: the live benchmark engine's main control panel.",
      [(FP, "The interface that operates the engine's controls and displays their effects through the connected backend.")],
      aka=["tuning bench", "the bench"]),
    T("harness", P, "The machinery that supplies workloads, executes comparisons, checks requirements and records results.",
      [(FP, "The machinery that supplies workloads, executes comparisons, checks requirements and records results.")], aka=["harness"]),
    T("defensive system", B, "Constraint enforcement, fault detection, containment, recovery and restoration: the bone and the twins, "
      "the lease's walk back, the kill switch.", [(FP, "Constraint enforcement, fault detection, containment, recovery and restoration.")],
      aka=["defensive system"]),
    T("health", R, "The explicit operating requirements: correctness, service limits, resource bounds and every applicable hardware "
      "limit.", [(FP, "The explicit operating requirements: correctness, service limits, resource bounds and every applicable hardware limit.")],
      aka=["health"]),
    T("Restore factory profile", D, "The control that reapplies the released Omni-Compass configuration: every knob of the mechanism "
      "and the heartbeat back to the factory's, Omni-Compass still on.",
      [(FP, "| Restore factory profile | Reapply the released Omni-Compass configuration. |"), (PAGE_F, "Restore factory profile")],
      aka=["Restore factory profile"]),
    T("Return to native", D, "The control that hands governance back and restores the recorded native settings, as the adapter "
      "supports.", [(FP, "| Return to native | Hand governance back and restore the recorded native settings, as the adapter supports. |")],
      aka=["Return to native"]),
    T("observer", W, "A tool that stores readings and draws them and raises an alert when a line is crossed; a person decides. "
      "Prometheus, Grafana, Datadog and the like. Omni-Compass's exporter serves its readings to any of them.",
      [(FP, "| Observer | stores readings and draws them; raises an alert when a line is crossed |")], aka=["observer", "monitoring"]),
    T("collector", W, "A tool that gathers metrics, logs, traces and profiles and forwards them, deciding nothing: Grafana Alloy, "
      "the OpenTelemetry Collector, node_exporter, Kepler.", [(FP, "| Collector | gathers metrics, logs, traces and profiles and forwards them |")],
      aka=["collector", "Alloy"]),
    T("console", W, "One screen to deploy, scale, restart and set rules across clusters, where a person decides: Rancher, Portainer, "
      "Lens, the OpenShift console. The rules set there are the native Omni-Compass sits on top of.",
      [(FP, "| Console | one screen to deploy, scale, restart and set rules across clusters |")], aka=["console", "cluster manager"]),
    T("automatic optimizer", W, "A product that watches one layer and changes its settings itself, mostly for a cloud bill: the "
      "comparable, benchmarked as native with it and then with Omni-Compass on top.",
      [(FP, "| Automatic optimizer | watches a layer and changes its settings itself, mostly for a cloud bill |")], aka=["optimizer"]),
    T("supervisory governor", W, "What Omni-Compass is: it reads the whole body every beat, decides with one law across every muscle, "
      "writes through a two-way plug, reads each write back, audits, hands back gradually and stops at the kill switch, on top of "
      "every native controller.", [(FP, "| Supervisory governor | reads the whole body every beat, decides with one law across every muscle")],
      aka=["supervisory governor", "governor"]),
    T("the dashboards", W, "The page's section 3i: the live benchmark engine in nine forms an operations team reads (a board of panels, a host "
      "map, a graph, an event stream, a cluster console, a one-line diagram, a wall of numbers, the cost by body part, and "
      "Omni-Compass's own two-way pipeline), by muscle, body part or the whole organism.",
      [(PAGE_F, "Dashboards")], aka=["dashboards", "host map"]),
    T("contract, this decision", W, "The decision on screen in the symbols of the factory profile's mathematics: k, Δ, θ, the "
      "settings requested u[req](k), commanded u[cmd](k) = Π[C](u[req](k)) and acknowledged u[ack](k) = R(u[cmd](k)), computed on the "
      "live model.", [(FP, "u[cmd](k) = Π[C](u[req](k))"), (PAGE_F, "contract, this decision")], aka=["the contract"]),
    T("governor request", D, "The row under the fuse box's master switches: after every press, the request "
      "a running governor takes for it through its control panel (tools/omni_control.py), with its role; the page sends nothing.",
      [(PAGE_F, "governor request")], aka=["governor request", "the same press"]),
    T("Prometheus Metrics", W, "The fuse box's tab that prints the live model in Prometheus's text exposition format, with the "
      "series a running system serves beside each one and the PromQL the Grafana wall draws it with.",
      [(PAGE_F, "Prometheus Metrics Endpoint")], aka=["Metrics tab", "Prometheus"]),
    T("Commands", D, "The fuse box's tab that lists every control beside the request a running governor takes for it and its "
      "role; the mechanism's knobs and the plant's conditions have none.",
      [(PAGE_F, "Governor API Commands")], aka=["Commands tab"]),
    T("the monitor wall stack", W, "deploy/wall: Prometheus, Grafana with the Omni-Compass wall loaded, Alertmanager with the "
      "governor's alert rules, node_exporter and the governor's exporter, in one command; it reads and writes nothing.",
      [("deploy/wall/README.md", "One command stands up the wall an operations team already knows how to read")], aka=["deploy/wall"]),
    T("actuation feedback", W, "Each decision's requested settings, those that landed as asked, those held at a muscle's limit, and "
      "those still moving toward their setting; requested, commanded and acknowledged settings are kept distinct.",
      [(FP, "so the requested, the commanded and"), (PAGE_F, "actuation, this decision")], aka=["actuation"]),
    T("the bill of a route", R, "C(r, a) = Σₖ c(r, a, k), the sum of a route's cost components inside the declared boundary, and "
      "the saving S(r, a) = (C(r, native) − C(r, a)) / C(r, native); a component with no recorded price leaves the total unresolved.",
      [(FP, "C(r, a) = Σₖ c(r, a, k),"), (FP, "S(r, a) = (C(r, native) − C(r, a)) / C(r, native),")], aka=["the bill", "deployment route"]),
    T("Omni-Compass's blue", W, "Blue (#4e97d1, the page's --brass and --omni): Omni-Compass's side and its name; on a reading, "
      "blue always means power given. While the master switch is OFF, Omni-Compass's side follows native in a lighter tint of "
      "native's own colour.",
      [(PAGE_F, "the sides: --brass is Omni-Compass (blue)"), (MAN, "| Blue | Omni-Compass; on a reading, power given |"),
       (PAGE_F, "OFF at the master switch: every Omni-Compass side is drawn in native's own colour, a lighter tint of it")],
      aka=["blue"]),
    T("a changed tune's violet", W, "Violet (#c77dff, the page's --tuned): a knob or a profile turned from the factory tune; never "
      "a side and never a reading's colour.",
      [(PAGE_F, "a knob or profile turned from the factory tune: violet, never a side and never a reading's colour")],
      aka=["violet"]),
    T("Mechanism Knobs", W, "The engine's own knobs, live: the four pieces of the brain, the compass law, Omni-Compass's hand on "
      "each muscle (the max's push and lift-off, the tune-down's floor, step and dwell), native's own controller (its target, "
      "tolerance, step and window) and every muscle's scale out, scale in, scale up, response time and sensing delay. They turn "
      "the engine's own equations while it runs, on both governed arms; a knob turned from the factory turns violet, ↺ puts it "
      "back, and the factory button puts every one back. A tune other than the factory's is a variation of the mechanism (class "
      "S).",
      [(PAGE_F, "the engine's own knobs, live"),
       (PAGE_F, "these turn the engine's own equations while it runs")], aka=["mechanism panel", "the mechanism's own knobs"]),
    T("Variation Switchboard", W, "One set of knobs that sets the arm, the organism, the copies, the runs, the run letter and the beat on "
      "every monitor that carries that variation, and names the ones that do not.",
      [(CL, "one switchboard sets the arm, the organism, the copies, the runs, the run letter and the beat on every monitor that carries that variation")],
      aka=["switchboard"]),
    T("the monitor wall", W, "Every monitor of the page in one view (section 0), numbered 1 upward in five blocks of about twelve, "
      "each its own subject (Benefit and Organism; Real Runs on GitHub; Brain and Mechanism; Clouds, Chips, Orchestrators and "
      "Scale; Proof and Telemetry), read left to right; every canvas the page draws is one monitor, its small copy on the wall a tile.",
      [(MAN, "Every monitor of the page in one view"), ("docs/engine/monitors.json", "every canvas the page draws is one monitor")],
      aka=["monitor wall", "the wall", "monitor", "monitors"]),
    T("golden signals", W, "Latency, traffic, errors and saturation: on the wall, the work waiting, the work done, the decisions "
      "past their line and the capacity held.", [(MAN, "Latency, traffic, errors and saturation")], aka=["golden signals"]),
]


# --------------------------------------------------------------------------------------------------- the sources, checked
_NORM = {}
GLOSSARY_RECORD = re.compile(r'"source"\s*:\s*"tools/live_glossary\.py"')
GLOSSARY_SECTION = re.compile(r'<section\b[^>]*\bid="s-(?:gloss|index)[^"]*"')   # the page's own glossary and index, once it has them


def _section_end(page: str, i: int) -> int:
    depth = 0
    for mm in re.finditer(r"<section\b|</section>", page[i:]):
        depth += -1 if mm.group(0) == "</section>" else 1
        if depth == 0:
            return i + mm.end()
    return len(page)


def strip_glossary(page: str) -> str:
    """The page without this glossary in it: its embedded record (the <script> holding this file's JSON) and its own glossary
    and index sections, so that neither a quote's check nor the index ever reads the glossary back as the page's words."""
    while True:
        m = GLOSSARY_RECORD.search(page)
        if not m:
            break
        a, b = page.rfind("<script", 0, m.start()), page.find("</script>", m.end())
        if a < 0 or b < 0:
            break
        page = page[:a] + page[b + len("</script>"):]
    for m in reversed(list(GLOSSARY_SECTION.finditer(page))):
        page = page[:m.start()] + page[_section_end(page, m.start()):]
    return page


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def source_texts(path: str) -> list[str]:
    """The file's words, whitespace folded; for the page also its visible words (tags dropped, entities decoded)."""
    if path not in _NORM:
        raw = (ROOT / path).read_text(encoding="utf-8")
        if path.endswith(".html"):
            raw = strip_glossary(raw)
        out = [_norm(raw)]
        if path.endswith(".html"):
            vis = html.unescape(raw)
            out += [_norm(re.sub(r"<[^>]+>", "", vis)), _norm(re.sub(r"<[^>]+>", " ", vis))]
        _NORM[path] = out
    return _NORM[path]


def quote_found(path: str, quote: str) -> bool:
    q = _norm(quote)
    return any(q in t for t in source_texts(path))


def check_sources(items) -> list[str]:
    """Every source file exists and says the words quoted from it."""
    bad = []
    for it in items:
        name = it.get("term") or it.get("name")
        for s in it.get("sources", []):
            if not (ROOT / s["file"]).is_file():
                bad.append(f"{name}: {s['file']} does not exist")
            elif not quote_found(s["file"], s["quote"]):
                bad.append(f"{name}: {s['file']} does not say {s['quote']!r}")
    return bad


# ------------------------------------------------------------------------------------------------------------ the index
def page_sections(page: str) -> list[dict]:
    """Each <section id="s-..."> of the page in its order: its id, number, title and the words it prints (its visible text,
    its aria label and its monitors' own names and descriptions)."""
    body = re.sub(r"<script\b[^>]*>.*?</script>", " ", page, flags=re.S)
    body = re.sub(r"<style\b[^>]*>.*?</style>", " ", body, flags=re.S)
    try:
        reg = {m["id"]: m for m in json.loads(MONITORS.read_text(encoding="utf-8"))["monitors"]}
    except (OSError, ValueError, KeyError):
        reg = {}
    vis = lambda f: _norm(html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<br\s*/?>", " ", f))))
    out = []
    for m in re.finditer(r'<section\b[^>]*\bid="(s-[^"]+)"[^>]*>', body):
        sec = body[m.start():_section_end(body, m.start())]
        h2 = re.search(r'<h2[^>]*>(?:<span class="sn">([^<]*)</span>)?(.*?)</h2>', sec, re.S)
        label = re.search(r'aria-label="([^"]*)"', m.group(0))
        mons = [reg[c] for c in re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', sec) if c in reg]
        words = " ".join([vis(sec), html.unescape(label.group(1)) if label else ""] +
                         [f"{x.get('name', '')} {x.get('what', '')}" for x in mons])
        out.append({"id": m.group(1), "n": (h2.group(1) or "").strip() if h2 else "",
                    "title": vis(h2.group(2)) if h2 else (html.unescape(label.group(1)) if label else m.group(1)),
                    "words": words})
    return out


def _pattern(alias: str) -> re.Pattern:
    """An alias as the page would print it: whole words at its word ends; case kept for a word in capitals (GAIN, STEADY,
    LOSS, the light's labels, A), folded otherwise."""
    core = re.escape(alias)
    lead = r"(?<![\w-])" if re.match(r"\w", alias) else ""        # a hyphen joins a word: Omni-Compass is not the compass
    tail = r"(?![\w-])" if re.search(r"\w$", alias) else ""
    flags = 0 if (alias.isupper() and len(alias) > 1) or alias in ("A",) else re.I
    return re.compile(lead + core + tail, flags)


GREEK = ("κ", "σ", "ν", "θ")
SKIP = ("A", "h")                             # a bare letter is everywhere on the page: those two are indexed by their words
# terms whose name, or the name without its "the", is also an everyday word on the page (a stack of software, a line of text,
# a chart's key, a max(...) in a formula, a push to GitHub): the index looks for their aliases only, as written
EXACT = {"push", "the stack", "the line", "the key", "the edge", "the max", "the twin", "the cover", "the centre"}


def aliases(name: str, aka) -> list[str]:
    """The words the index looks for: the name, the name without a leading "the", and each alias as written."""
    out = []
    for b in ([] if name in EXACT else [name, re.sub(r"^the ", "", name)]) + list(aka):
        if b and b not in out and b not in SKIP and (len(b) > 1 or b in GREEK):
            out.append(b)
    return out


def build_index(page: str, terms, orgs, arm_list):
    secs = page_sections(page)
    entries, missing = [], []
    items = OrderedDict()                     # a term and an arm of the same name are one entry of the index
    for kind, name, aka in ([("term", t["term"], t["aka"]) for t in terms] + [("organism", o["name"], o["aka"]) for o in orgs]
                            + [("arm", a["name"], a["aka"]) for a in arm_list]):
        it = items.setdefault(name.lower(), {"name": name, "kinds": [], "aliases": []})
        it["kinds"].append(kind)
        it["aliases"] += [x for x in aliases(name, aka) if x not in it["aliases"]]
    for it in items.values():
        pats = [_pattern(a) for a in it["aliases"]]
        anchors = [s["id"] for s in secs if any(p.search(s["words"]) for p in pats)]
        e = {"term": it["name"], "kind": ", ".join(it["kinds"])}
        if anchors:
            entries.append(dict(e, anchors=anchors))
        else:
            missing.append(e)
    key = lambda e: (re.sub(r"^the ", "", e["term"], flags=re.I).lower(), e["kind"])
    entries.sort(key=key)
    missing.sort(key=key)
    return [{"id": s["id"], "n": s["n"], "title": s["title"]} for s in secs], entries, missing


# ------------------------------------------------------------------------------------------------------------- building
def engine() -> dict:
    from tools.omni_version import VERSIONS
    d = json.loads(next(iter(VERSIONS.values())).read_text(encoding="utf-8"))
    return {"version": d["version"], "digest": d["digest"][:16]}


MUSCLE_KEYS = {   # what each field of a muscle's record holds: the record is short, its words are in the tables beside it
    "id": "the catalog's muscle_id",
    "name": "the setting's own name on its controller (realms/catalog_v5.csv, muscle)",
    "family": "its family's id: families[id] holds the family's name, its native controller, its wire out, wire in, restore and whether it has run live (docs/wiring_recipes.csv)",
    "realms": "the realms it sits in (all four: a spine muscle)",
    "template": "its plant: templates[t] holds what the plant is, its native controller, what Omni-Compass reads and moves (realms/plants.py, tools/muscle_catalog.py)",
    "preset": "its class of machine: presets[p] holds what it is and how it is reached in a real stack",
    "knob": "its kind of knob: knobs[k] holds what it is",
    "meaning": "the muscle in one line, in the catalog's words",
    "does": "what the max does with it: an index into does[] (tools/muscle_catalog.py does())",
    "card": "its own card, or global (realms/muscle_cards_v5.csv)",
    "organisms": "every organism it belongs to, by the runners' own rules (spine, the realms, stack, tower, orchestra, sixty)",
    "governors": "the governors whose knob it stands for in the orchestra (tools/governors_page.py CATALOG)",
    "part": "its body part in the live benchmark engine's sixty (docs/engine/export_harness_trace.py)",
}


def build_core() -> dict:
    """Everything but the index: the muscles, the organisms, the arms, the scenarios and the terms."""
    rows = catalog_rows()
    recipes = {r["family"]: r for r in csv.DictReader(RECIPES.open(encoding="utf-8"))}
    missing = sorted({r["family"] for r in rows} - set(recipes))
    if missing:
        raise SystemExit(f"docs/wiring_recipes.csv lacks a recipe for: {', '.join(missing)}")
    cards = load_cards()
    tpl, kn = templates(), knobs()
    mem = memberships(rows)
    grp = groups(rows)
    order = {mid: i for i, mid in enumerate(m for g in grp for f in g["families"] for m in f["muscles"])}
    fams = OrderedDict()
    for r in sorted(rows, key=lambda r: int(r["family_id"])):
        if r["family_id"] in fams:
            fams[r["family_id"]]["n"] += 1
            continue
        rc = recipes[r["family"]]
        fams[r["family_id"]] = {"name": r["family"], "template": r["template"], "preset": r["preset"], "n": 1,
                                "spine": is_spine(r), "native": rc["native_controller"], "read": rc["read"],
                                "write": rc["write"], "restore": rc["restore"], "live": run_live(rc["live"])}
    muscles, does_list = [], []
    for r in sorted(rows, key=lambda r: order[r["muscle_id"]]):
        t, p, k = r["template"], r["preset"], r["knob"]
        pw = PRESET.get(p, (p, "see the manual, section 4.2"))
        m = mem[r["muscle_id"]]
        dz = does(r)
        if dz not in does_list:
            does_list.append(dz)
        rec = {"id": r["muscle_id"], "name": r["muscle"], "family": r["family_id"], "realms": r["realms"].split(";"),
               "template": t, "preset": p, "knob": k, "meaning": f"The {nice(r['muscle'])} setting of {pw[0]}, a {k} knob.",
               "does": does_list.index(dz), "card": card_text(cards.get(r["muscle_id"])),
               "organisms": m["organisms"]}
        if m["governors"]:
            rec["governors"] = m["governors"]
        if m["part"]:
            rec["part"] = m["part"]
        muscles.append(rec)
    orgs = organisms(rows)
    arm_list = arms()
    bad = check_sources(TERMS + orgs + arm_list)
    if bad:
        raise SystemExit("a source no longer says what it is cited for:\n  " + "\n  ".join(bad))
    return {"rows": rows, "templates": tpl, "knobs": kn, "presets": {p: {"what": PRESET[p][0], "wire": PRESET[p][1]}
            for p in sorted({r["preset"] for r in rows}) if p in PRESET},
            "families": fams, "does": does_list, "groups": grp, "muscles": muscles, "organisms": orgs, "arms": arm_list,
            "scenarios": scenarios(orgs, arm_list), "terms": TERMS}


def build() -> dict:
    core = build_core()
    page = strip_glossary(PAGE.read_text(encoding="utf-8"))
    sections, index, unindexed = build_index(page, core["terms"], core["organisms"], core["arms"])
    rows = core.pop("rows")
    out = OrderedDict()
    out["notice"] = PLAIN
    out["title"] = "The live benchmark engine's glossary and index"
    out["source"] = "tools/live_glossary.py"
    out["engine"] = engine()
    out["rule"] = ("Every muscle of realms/catalog_v5.csv once; every organism, arm and term in the repository's own words, each "
                   "term with the file it is drawn from and a quote that file still carries; the index is every section of "
                   "docs/engine/OMNI_COMPASS_LIVE_ENGINE.html that prints a term, an organism or an arm, by its anchor.")
    out["counts"] = {"muscles": len(core["muscles"]), "catalog_rows": len(rows), "families": len(core["families"]),
                     "terms": len(core["terms"]), "organisms": len(core["organisms"]), "arms": len(core["arms"]),
                     "scenarios": len(core["scenarios"]), "sections": len(sections), "index": len(index),
                     "unindexed": len(unindexed)}
    out["keys"] = MUSCLE_KEYS
    out["realms"] = [{"key": k, "name": REALM_NAMES[k]} for k in REALM_KEYS]
    for k in ("templates", "knobs", "presets", "families", "does", "groups", "muscles", "organisms", "arms", "scenarios", "terms"):
        out[k] = core[k]
    out["sections"] = sections
    out["index"] = index
    out["unindexed"] = unindexed
    return out


def to_json(d: dict) -> str:
    """Compact JSON that can sit inside a <script> element: no "</" anywhere (a "/" after "<" is written as \\u002f)."""
    s = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\u002f").replace("<!--", "<\\u0021--")


# ------------------------------------------------------------------------------------------------------- the readable page
def md_cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def to_md(d: dict) -> str:
    sec = {s["id"]: s for s in d["sections"]}
    anchor = lambda a: f"{sec[a]['n']} (#{a})" if sec[a]["n"] else f"#{a}"
    c = d["counts"]
    L = ["# The Live Benchmark Engine's Glossary and Index", "",
         "This is the back of the live benchmark engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`): every term a reader of the page "
         f"meets, the {c['organisms']} organisms it shows, its {c['arms']} arms and their {c['scenarios']} combinations, every one of "
         f"the catalog's {c['muscles']:,} muscles bulked by its realms, and an index of where each term stands on the page. Every "
         "definition is drawn from the file it names, and the file still carries the words quoted from it; nothing here is typed "
         "twice. It is written by `tools/live_glossary.py`, which writes the same content as `docs/engine/glossary.json` for the "
         f"page. Engine: {d['engine']['version']} (digest {d['engine']['digest']}).", "",
         "The organisms and the muscles' plants are our own models (evidence class S) unless a line says otherwise; a model is a "
         "statement about the model, and nothing here is a result. See `DISCLOSURES.md`.", "",
         "## Contents", "", "1. The terms", "2. The arms", "3. The organisms", "4. The scenarios: every organism under every arm",
         "5. The muscles, bulked by their realms", "6. The index", ""]
    L += ["## 1. The terms", ""]
    for g in OrderedDict((t["group"], 1) for t in d["terms"]):
        L += [f"### {g}", ""]
        for t in [t for t in d["terms"] if t["group"] == g]:
            src = "; ".join(f"`{s['file']}`" for s in OrderedDict((s["file"], s) for s in t["sources"]).values())
            L.append(f"- **{t['term']}.** {t['def']} *Source: {src}.*" + (f" *{t['note']}*" if t.get("note") else ""))
        L.append("")
    L += ["## 2. The arms", "", "| Arm | Colour | What it is | Source |", "|---|---|---|---|"]
    for a in d["arms"]:
        src = "; ".join(f"`{s['file']}`" for s in OrderedDict((s["file"], s) for s in a["sources"]).values())
        L.append(f"| **{a['name']}** | {a['colour']} ({a['hex']}) | {md_cell(a['def'])} | {src} |")
    L += ["", "## 3. The organisms", ""]
    for o in d["organisms"]:
        n = f"{o['muscles']:,} muscles" if o["muscles"] is not None else f"{o['layers']} layers"
        L += [f"### {o['name']} ({n})", "", o["meaning"], ""]
        if o["families"]:
            L.append("Families: " + "; ".join(f"{f['name']} ({f['n']})" for f in o["families"]) + ".")
            L.append("")
        if o.get("governors"):
            L.append("Governors: " + "; ".join(f"{g['name']} ({g['muscles']})" for g in o["governors"]) + ".")
            L.append("")
        if o.get("parts"):
            L.append("Body parts: " + "; ".join(f"{p['part']} ({len(p['muscles'])} muscles, the organ {p['organ']}, θ {p['theta']})"
                                               for p in o["parts"]) + ".")
            L.append("")
        if o.get("sectors"):
            L.append("Sectors: " + "; ".join(f"{s['name']} ({', '.join(s['layers'])})" for s in o["sectors"]) + ".")
            L.append("")
            L.append("Every way it is bought: " + "; ".join(w["name"] for w in o["ways"]) + ".")
            L.append("")
        L.append("*Source: " + "; ".join(f"`{s['file']}`" for s in OrderedDict((s["file"], s) for s in o["sources"]).values()) + ".*")
        L.append("")
    L += ["## 4. The scenarios: every organism under every arm", "",
          f"{len(d['organisms'])} organisms × {len(d['arms'])} arms = {len(d['scenarios'])} scenarios.", "",
          "| Scenario | What runs |", "|---|---|"]
    for s in d["scenarios"]:
        L.append(f"| {md_cell(s['name'])} | {md_cell(s['what'])} |")
    L += ["", "## 5. The muscles, bulked by their realms", "",
          "Every muscle of `realms/catalog_v5.csv` once: the spine's families first, then each realm's own. Each family names its "
          "plant, its class of machine, the native controller that runs it and how it is reached; each muscle its knob, what "
          "Omni-Compass does with it (the max, the default) and the organisms it belongs to (spine; the realms; stack; tower; "
          "orchestra, with its governors; the live benchmark engine's sixty, with its body part).", "",
          "**The four kinds of knob.** " + " ".join(f"**{k}**: {v['full']}" for k, v in d["knobs"].items()), "",
          "**The five plants.** " + " ".join(f"`{k}`: {v['what']}; native: {v['native']}." for k, v in d["templates"].items()), ""]
    mus = {m["id"]: m for m in d["muscles"]}
    short = {"spine": "spine", "compute_ai_cloud": "Compute", "physics_robotics_autonomous": "Physics",
             "energy_facility_industrial": "Energy", "distribution_specialized": "Distribution", "stack": "stack",
             "tower": "tower", "orchestra": "orchestra", "sixty": "the sixty"}
    for g in d["groups"]:
        L += [f"### {g['title']}", ""]
        for f in g["families"]:
            fm = d["families"][f["id"]]
            pw = d["presets"].get(fm["preset"], {"what": fm["preset"], "wire": ""})
            L += [f"#### {f['name']} ({len(f['muscles'])} muscles)", "",
                  f"Plant `{fm['template']}`, {d['templates'][fm['template']]['what']}; class `{fm['preset']}`, {pw['what']}, "
                  f"reached through {pw['wire']}. Native: {fm['native']}. Run live? {fm['live']}.", "",
                  "| # | Muscle | Knob | What Omni-Compass does with it | Organisms |", "|---:|---|---|---|---|"]
            for mid in f["muscles"]:
                m = mus[mid]
                orgs = []
                for o in m["organisms"]:
                    if o == "orchestra" and m.get("governors"):
                        orgs.append("orchestra (" + ", ".join(m["governors"]) + ")")
                    elif o == "sixty":
                        orgs.append(f"the sixty ({m.get('part')})")
                    else:
                        orgs.append(short.get(o, o))
                L.append(f"| {m['id']} | {md_cell(nice(m['name']))} | {m['knob']} | {md_cell(d['does'][m['does']])} | {'; '.join(orgs)} |")
            L.append("")
    L += ["## 6. The index", "",
          "Every term, organism and arm with the sections of the page that print it, by the section's number and anchor (the "
          "page's address followed by the anchor opens the section). The sections, in the page's order:", "",
          "| Section | Anchor | Title |", "|---|---|---|"]
    L += [f"| {s['n'] or '—'} | #{s['id']} | {md_cell(s['title'])} |" for s in d["sections"]]
    L += ["", "| Term | Kind | Where on the page |", "|---|---|---|"]
    for e in d["index"]:
        L.append(f"| {md_cell(e['term'])} | {e['kind']} | {md_cell('; '.join(anchor(a) for a in e['anchors']))} |")
    if d["unindexed"]:
        L += ["", "Not printed in the page's own words at this build (defined above, not yet on the page): "
              + "; ".join(e["term"] for e in d["unindexed"]) + "."]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if the files differ from what the repository gives now")
    a = ap.parse_args(argv)
    d = build()
    js, md = to_json(d) + "\n", to_md(d)
    if a.check:
        bad = [str(p.relative_to(ROOT)) for p, s in ((OUT_JSON, js), (OUT_MD, md))
               if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("glossary: " + (", ".join(bad) + " differ from what the repository gives now" if bad else "up to date"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    c = d["counts"]
    print(f"{OUT_JSON.relative_to(ROOT)} ({len(js.encode('utf-8')) / 1024:.0f} KB), {OUT_MD.relative_to(ROOT)}: {c['muscles']} "
          f"muscles, {c['terms']} terms, {c['organisms']} organisms, {c['arms']} arms, {c['scenarios']} scenarios, "
          f"{c['index']} index entries ({c['unindexed']} not on the page), {c['sections']} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
