#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Benefit against native: is Omni-Compass a benefit against native, by how much, in the
three ways it runs, and what the two bills say, at the top of the README and of the live engine page.

Every number is read from a result file of the engine that stands, never typed: the three ways from the newest three-arm record
on GitHub's machines (results/orchestrator/V*_THREE_ARMS_ABC.json: native, Omni-Compass on top of native, Omni-Compass direct;
three runs, class L), each scenario's signal from its own rows by the one key (tools/readings.py: red, the stop-sign octagon,
REDLINING, when a row reads LOSS; green, the circle, GAINING, when a row reads GAIN and none LOSS; yellow, the diamond,
STEADY, when every row reads STEADY). The two bills are the two ways a stack is bought (docs/engine/export_whole.py): on-site,
the software on the owner's bare metal; through the cloud, where the cloud is the wire between the two ends. A bill's part that
the engine that stands has not measured is written "not yet measured on <engine>", never filled in, and no price is assumed: a
bill is the measured change in what it is made of (the founder's choice of 24 October: percent, no dollar price). The totals
composed from earlier engines' tables stand beside it, named by their engines and never read as the engine that stands.

  python3 tools/headline.py            write the block into README.md and the live engine page
  python3 tools/headline.py --check    exit 1 when either differs from what the files give
"""
from __future__ import annotations

import html
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import readings as K          # noqa: E402  (the one key)

README = ROOT / "README.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
WHOLE = ROOT / "results" / "WHOLE_SYSTEM.json"
BEGIN, END = "<!-- headline: written by tools/headline.py from the result files; never edited by hand -->", "<!-- end headline -->"
# the signal words are the live engine page's one vocabulary (GAINING, STEADY, REDLINING; the referee of 30 October); the files keep
# their names
SIGNAL = {"red": ("REDLINING", "docs/engine/signals/redlining.svg", "the red stop-sign octagon"),
          "lead": ("STEADY", "docs/engine/signals/steady.svg", "the yellow yield diamond"),
          "ok": ("GAINING", "docs/engine/signals/accelerating.svg", "the green circle")}
SHEET = ROOT / "results" / "BENEFIT_SHEET.json"
INDEX_FILE = "results/OMNI_INDEX.md"
# the two sides, and only two (the founder's order of 25 October 2026: Omni-Compass is never by itself); a record's other pairs
# stay in the record itself, every row shown there
PAIRS = (("Omni-Compass on top of native", "Omni on native against native",
          "never fewer units than the rule"),)   # the rest of each arm's words is the record's own (arm_words)
# native and Omni-Compass on native are the only two sides (the founder's order of 25 October: Omni-Compass is never by itself);
# the record's third arm, Omni direct, stays in its own table as the road and is not read here
WORD_ORDER = (K.GAIN, K.GAIN_GIVEN, K.GAIN_AND_LOSS, K.STEADY, K.LOSS)
GAUGES = (("requests", "Work"), ("p95", "Response (95th percentile)"), ("machines", "Machines"), ("units", "Units"))


def newest_record():
    recs = sorted(ROOT.glob("results/orchestrator/V*_THREE_ARMS_ABC.json"), key=lambda p: int(re.match(r"V(\d+)", p.name).group(1)))
    if not recs:
        raise SystemExit("headline: no three-arm record in results/orchestrator/")
    return recs[-1], json.loads(recs[-1].read_text(encoding="utf-8"))


def row_of(rec, pair, gauge):
    for r in rec["rows"]:
        if r["pair"] == pair and r["gauge"].startswith(gauge):
            return r
    return None


def word_of(reading: str) -> str:
    for w in (K.LOSS, K.GIVEN, K.GAIN):
        if reading.startswith(w):
            return w
    return K.STEADY if reading.startswith(("STEADY", "STEADY")) else reading


def mean_change(r) -> float:
    return sum(r["runs"][k]["rel"] for k in sorted(r["runs"])) / len(r["runs"])


def raw(x: float) -> str:
    """A raw change, Omni-Compass − native over native, with its true sign."""
    return "±0.0%" if abs(x) < 0.0005 else f"{'+' if x > 0 else '−'}{100 * abs(x):.1f}%"


# each gauge's move in words, (when the raw change rises, when it falls), the size first and no sign beside the word (a time that
# fell is shorter, never "faster by" a percent of time: the referee of 30 October)
MOVE = {"requests": ("{} more work", "{} less work"), "p95": ("the time {} longer", "the time {} shorter"),
        "machines": ("{} more", "{} fewer"), "units": ("{} more", "{} fewer")}


def said(r, gauge) -> str:
    """A row by the key: the word with its size and no sign, then the raw change apart, with its true sign and labelled raw: the
    mean of the three runs and each run's own."""
    m = mean_change(r)
    up, down = MOVE[gauge]
    move = "unchanged" if abs(m) < 0.0005 else (up if m > 0 else down).format(f"{100 * abs(m):.1f}%")
    runs = ", ".join(f"{k} {raw(r['runs'][k]['rel'])}" for k in sorted(r["runs"]))
    return f"{r['reading']}: {move}; raw {raw(m)} (runs {runs})"


def signal(rows) -> str:
    words = [word_of(r["reading"]) for r in rows if r]
    if K.LOSS in words:
        return "red"
    return "ok" if K.GAIN in words else "lead"


def whole_beside():
    """The composed totals of earlier engines' tables (tools/whole_system.py), named by their engines."""
    if not WHOLE.exists():
        return None
    d = json.loads(WHOLE.read_text(encoding="utf-8"))
    engines = sorted({t.get("engine", "") for name, ts in d["layers"].items() if not name.startswith("1.") for t in ts},
                     key=lambda e: (len(e), e))
    tot = (d.get("totals") or {}).get("without the card (the cluster, the services and the cloud) | index") or {}
    pct = lambda mu: None if mu is None else 100.0 * (math.exp(mu) - 1.0)     # each total is a log ratio toward the gauge's aim
    g = {k: pct(v[0]) if v else None for k, v in (tot.get("total") or {}).items()}
    # the evidence classes of the layers this scope composes, read from the layers' own names ("..., class L"): the scope without
    # the card holds no class P layer (the referee of 30 October)
    classes = sorted({m.group(1) for k in (tot.get("by_layer") or {}) for m in [re.search(r"class (\w)\s*$", k)] if m})
    # the bill with every interval carried: the cloud's one-run tests enter as exactly 1 by the index's rule, so the bill there is
    # not counted; carried, it reads its own word, and whether its interval includes no change
    car = ((d.get("totals") or {}).get("without the card (the cluster, the services and the cloud) | carried") or {}).get("total") or {}
    cb = car.get("bill")
    bill_carried = None
    if cb:
        mu, sd = cb
        w = K.STEADY if abs(math.exp(mu) - 1.0) < K.SIZE_FLOOR else (K.GAIN if mu > 0 else K.GIVEN)
        bill_carried = {"word": w, "size": 100.0 * abs(math.exp(mu) - 1.0), "includes_none": (mu - 1.96 * sd) < 0.0 < (mu + 1.96 * sd)}
    return {"engines": [e for e in engines if e], "index": pct((tot.get("index") or {}).get("mu")), "classes": classes,
            "work": g.get("work"), "speed": g.get("speed"), "machines": g.get("machines"), "energy": g.get("energy"), "bill": g.get("bill") or 0.0,
            "bill_carried": bill_carried}


def the_engine_that_stands() -> str:
    return "omni-v" + re.search(r'VERSIONS = \{"v(\d+)"', (ROOT / "tools" / "omni_version.py").read_text()).group(1)


def standing(stands: str):
    """The engine that stands across every benchmark, from the benefit sheet (tools/benefit_sheet.py): the Omni index's row, the
    benchmarks read on its own three-run tables with the count of each word, and those still on an older engine."""
    rows = json.loads(SHEET.read_text(encoding="utf-8"))["rows"]
    idx = next((r for r in rows if r.get("file") == INDEX_FILE), None)
    bench = [r for r in rows if r.get("file") != INDEX_FILE]
    on = [r for r in bench if r.get("engine") == stands]
    words = {}
    for r in on:
        words[r["benefit"]] = words.get(r["benefit"], 0) + 1
    order = [w for w in WORD_ORDER if w in words] + sorted(w for w in words if w not in WORD_ORDER)
    older = sorted({r.get("engine", "not named") for r in bench if r.get("engine") != stands}, key=lambda e: (len(e), e))
    return {"index": idx, "bench": len(bench), "on": len(on), "words": [(w, words[w]) for w in order],
            "older": len(bench) - len(on), "older_engines": older}


def arm_words(path: Path) -> dict:
    """Each arm as the record itself describes it (its .md: "Native is ...; Omni on native is ...;"), and where it ran, in the words
    of the orchestrator it ran on (omni_orchestrator/__init__.py's first line): never typed here, so the answer can never call the
    yardstick Kubernetes itself. "written by us" is said as whose it is, The Omni-Compass LLC."""
    md = path.with_suffix(".md").read_text(encoding="utf-8")
    nat = re.search(r"Native is (.+?);", md)
    onn = re.search(r"Omni on native is (.+?);", md)
    if not nat or not onn:
        raise SystemExit(f"headline: {path.with_suffix('.md').name} does not say what its arms are")
    doc = (ROOT / "omni_orchestrator" / "__init__.py").read_text(encoding="utf-8")
    head = re.search(r'"""(.+?)(?: \(|\.)', doc).group(1)            # "Omni-Compass's own orchestrator: the organism run without Kubernetes"
    who, what = head.split(": ", 1)
    return {"native": nat.group(1).replace(", written by us", ", as written by The Omni-Compass LLC"),
            "on_native": onn.group(1).replace("that rule", "the same rule"),
            "where": f"{who} (`omni_orchestrator`), {what}"}


def loss_ledger():
    """The LOSS ledger's own counts (docs/LOSS_LEDGER.md, its head): every LOSS row of the newest tables, and those of Omni-Compass
    against its own native, the rows do no harm is judged by."""
    f = ROOT / "docs" / "LOSS_LEDGER.md"
    if not f.exists():
        return None
    t = f.read_text(encoding="utf-8")
    a = re.search(r"Rows that read LOSS across their three runs: \*\*(\d+)\*\*", t)
    b = re.search(r"Against my own native, the readings do no harm is judged by: \*\*(\d+)\*\*", t)
    return {"all": int(a.group(1)), "native": int(b.group(1))} if a and b else None


def azure_now(stands: str):
    """Where the Azure sets stand, from the run ledger's own row (docs/RUN_LEDGER.md, section 3), never typed here: the newest set
    it names with its engine and run, its state, and whether the engine that stands's sets queue behind it."""
    f = ROOT / "docs" / "RUN_LEDGER.md"
    if not f.exists():
        return None
    row = next((ln for ln in f.read_text(encoding="utf-8").splitlines() if ln.startswith("| Azure |")), None)
    if not row:
        return None
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if len(cells) < 3:
        return None
    sets = re.findall(r"[Tt]he (omni-v\d+) ([^()|]*?)set[^()|]*?\(run (\d+)", cells[2])
    if not sets:
        return None
    eng, name, rid = sets[-1]
    return {"state": cells[1].replace("**", "").strip(), "engine": eng, "name": name.strip(), "run": rid,
            "behind": f"the {stands} sets queue behind it" in cells[2]}


def model():
    path, rec = newest_record()
    engine = rec["engine"].split(" (")[0]
    scen = []
    for name, pair, how in PAIRS:
        rows = {g: row_of(rec, pair, g) for g, _ in GAUGES}
        scen.append({"name": name, "how": how, "signal": signal([rows["requests"], rows["p95"]]), "rows": rows,
                     "work": mean_change(rows["requests"]), "p95": mean_change(rows["p95"])})
    azure_v = sorted(ROOT.glob(f"results/live/{engine.upper().replace('OMNI-', '')}_AKS*.md"))
    stands = the_engine_that_stands()
    return {"path": path.relative_to(ROOT).as_posix(), "rec": rec, "engine": engine, "scen": scen, "azure": azure_v, "whole": whole_beside(),
            "arms": arm_words(path), "ledger": loss_ledger(), "azure_now": azure_now(stands),
            "stands": stands, "standing": standing(stands)}


def index_word(pct: float) -> str:
    """The Omni index's own word: above one is a GAIN by its construction (results/OMNI_INDEX.md), STEADY under the floor."""
    return K.STEADY if abs(pct) < 100 * K.SIZE_FLOOR else (K.GAIN if pct > 0 else K.LOSS)



# the newest real runs on the engine that stands lead the answer (the founder's words of 27 October: "Haven't we got new benchmarks
# with newer dates?"): the Kubernetes tests' own three-run tables on that engine, each gauge as its table read it, every run's raw
# change beside the word with its true sign
STANDING_TESTS = (("ALL_FOUR", "Kubernetes, all four loads at once"), ("STEADY", "Kubernetes, steady work"),
                  ("WANDERING", "Kubernetes, demand that wanders"), ("FAULTS", "Kubernetes, faults injected"))
STANDING_GAUGES = (("work inside the response line", "Work inside the line"), ("response time (ms), 95th percentile", "Response, 95th percentile"),
                   ("failed requests", "Failed requests"), ("worker nodes in service", "Machines in service"))


def standing_block(stands: str) -> list:
    v = stands.split("-v")[1]
    rows = []
    for key, name in STANDING_TESTS:
        f = ROOT / "results" / "live" / f"V{v}_{key}.json"
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        cells = []
        for g, _ in STANDING_GAUGES:
            k = next((x for x in d["rows"] if x.startswith(g)), None)
            if not k:
                cells.append("not a gauge of this test")
                continue
            r = d["rows"][k]
            raws = []
            for x in r.get("runs") or []:
                if x.get("native"):
                    c = 100 * x["diff"] / abs(x["native"])
                    raws.append("±0.0%" if abs(c) < 0.05 else f"{'+' if c > 0 else '−'}{abs(c):.1f}%")
                elif x.get("native") == 0:
                    raws.append(f"{x['native']:g} → {x['omni']:g}" if "omni" in x else f"{x['diff']:+g}")
            word = (r.get("reading") or "").replace("**", "")
            cells.append(f"{word} (raw {', '.join(raws)})" if raws else word)
        runs = " · ".join(f"{x['tag']} {x['run']}" for x in d.get("runs", []))
        rows.append(f"| **{name}** ([`{f.with_suffix('.md').relative_to(ROOT).as_posix()}`]({f.with_suffix('.md').relative_to(ROOT).as_posix()})) | "
                    + " | ".join(cells) + f" | {runs} |")
    if not rows:
        return []
    return [f"### Newest Real Runs on {stands}", "",
            f"Three separate runs (A, B and C) of each preregistered test on GitHub's own machines (class L, live software), native against "
            f"Omni-Compass on top of native, every run on {stands}. Each cell is the table's own reading, then each run's raw change, "
            "Omni-Compass against native, with its true sign.", "",
            "| Test | " + " | ".join(n for _, n in STANDING_GAUGES) + " | GitHub runs |",
            "|---|" + "---|" * len(STANDING_GAUGES) + "---|"] + rows + [""]


# The two places and the two arms (the founder's order of 1 November 2026: "native against bare metal, native against the cloud,
# Omni-Compass on native against bare metal, and Omni-Compass on native on the cloud. That's the only places people will ever run
# it"): each place's receipt beside the work done, native and Omni-Compass on top of native, read from the result files.
CARD_ROWS = (("work per energy (served requests per kJ)", "work per joule"), ("energy, GPU (J)", "the chip's bill, its energy"),
             ("requests served", "the work done"), ("response time, 95th percentile (ms)", "the 95th-percentile response"))


def _card(stands: str, mode: str):
    """The newest card table of the engine that stands for a mode (cap, cap-full), else None."""
    v = stands.split("-v")[1]
    fs = sorted(ROOT.glob(f"results/gpu/V{v}_*_{mode.upper().replace('-', '_')}_ABC.json"))
    fs = [f for f in fs if f.name.endswith(f"_{mode.upper().replace('-', '_')}_ABC.json") and (mode != "cap" or "_FULL_" not in f.name)]
    return (fs[-1], json.loads(fs[-1].read_text(encoding="utf-8"))) if fs else None


def _raws(r) -> str:
    out = []
    for L, x in zip("123", r.get("runs") or []):
        if x.get("native"):
            c = 100 * x["diff"] / abs(x["native"])
            out.append(f"run {L} {'±0.0' if abs(c) < 0.005 else ('+' if c > 0 else '−') + format(abs(c), '.2f')}%")
    return ", ".join(out)


def _cat_word(x: float, sv) -> str:
    """A category's word by the key: under the 0.5% floor STEADY; a fall is a LOSS where its service reading fell too, else power given."""
    if abs(x) < 100 * K.SIZE_FLOOR:
        return K.STEADY
    return K.GAIN if x > 0 else (K.LOSS if sv is not None and sv < 0 else K.GIVEN)


def _switch(name: str) -> str:
    f = ROOT / "scripts" / f"{name}_queue.txt"
    t = f.read_text(encoding="utf-8") if f.exists() else ""
    m = re.search(r"^switch=(\w+)", t, re.M)
    return m.group(1) if m else "not set"


NOT_RENTED = "not yet run; every rental on the founder's word"


def places_block(m) -> list:
    stands = m["stands"]
    tb = json.loads((ROOT / "results" / "TWO_BILLS.json").read_text(encoding="utf-8")) if (ROOT / "results" / "TWO_BILLS.json").exists() else {}
    chip, cl = tb.get("chip") or {}, tb.get("cloud") or {}
    L = ["### Two Places, Two Arms: the Bill and the Work", "",
         f"On the engine that stands ({stands}), Omni-Compass runs in one of two places: **on bare metal**, a chip run directly, its bill the machine's own (here the rental, "
         "the chip's own meter beside it); or **through a cloud**, its bill the cloud's, the cloud's chips and back end inside its price "
         "and out of Omni-Compass's reach (it governs what the cloud gives, through the cloud's own Kubernetes). In each place two arms "
         "only: **native**, and **Omni-Compass on top of native**. Each box is that place's bill beside the work done inside it; the "
         "reading is the work for each dollar. The bill should hold; the benefit is the work inside it. The two places are never added "
         "together: a system runs in one or the other. The four arms, A and B on the chip, C and D in the cloud, are written once in "
         "[`results/TWO_BILLS.md`](results/TWO_BILLS.md) (`tools/two_bills.py`); these boxes read it.", ""]
    money = lambda x: f"${x:.4f}"
    if chip.get("per_run"):
        pr = chip["per_run"]
        card = re.sub(r"^.*three runs on (an? )?", "", chip.get("title", "")).strip() or "the card"
        eng = chip.get("engine", "").split(" (")[0]
        arm = lambda k: (f"the bill {', '.join(money(r[k]['bill']) for r in pr)}; the work done "
                         f"{', '.join(f'{r[k]['work']:,.0f}' for r in pr)} requests served (runs 1, 2, 3)")
        nat = f"one {card} card on Lambda, {eng}, an operator's power cap underneath, fully loaded: {arm('native')}"
        on = f"the same runs: {arm('omni')}"
        reads = []
        for key, name in (("bill ($, the rental for the arm's window)", "the bill"), ("work done (requests served)", "the work done"),
                          ("work per dollar (requests served per $)", "work per dollar"), ("energy per served request (J)", "the chip's energy for each request served"),
                          ("response time, 95th percentile (ms)", "the 95th-percentile response")):
            r = (chip.get("rows") or {}).get(key)
            if r:
                reads.append(f"{name} **{(r.get('reading') or '').replace('**', '')}** (raw {_raws(r)})")
        bare_read = "; ".join(reads)
    else:
        nat = on = bare_read = f"not yet read on {stands}"
    if cl.get("bill"):
        b, mh, ce = cl["bill"], cl.get("machine_hours") or {}, cl.get("engine", "")
        pct = 100 * b["diff"] / b["native"]
        noise = "beyond the noise" if b.get("significant") else "inside the noise"
        word = K.STEADY if abs(pct) < 100 * K.SIZE_FLOOR else (K.GAIN if pct < 0 else K.GIVEN)   # the word by the floor, the noise said beside it (results/TWO_BILLS.md)
        cnat = (f"Kubernetes on Azure's AKS, {ce}, {cl.get('repetitions')} paired repetitions (`{cl.get('page')}`): the bill "
                f"{money(b['native'])} a window at list price, {mh.get('native', 0):.3f} machine-hours; the work done not counted in that set")
        con = f"the same set: the bill {money(b['omni'])} a window, {mh.get('omni', 0):.3f} machine-hours"
        cread = (f"the bill {'up' if pct > 0 else 'down'} {abs(pct):.2f}%, **{word}**, {noise}; work per dollar waits for the set on {stands} "
                 f"(the cloud's work meter came after 31 October), Azure's sets at the max queued (`scripts/azure_queue.txt`, its switch "
                 f"{_switch('azure')}); Google and Amazon wired, Google's switch {_switch('google')}, Amazon's {_switch('amazon')}")
        if ce != stands:
            cread += f"; a set of {ce}, never read as {stands}'s"
    else:
        cnat = con = f"not yet read on {stands}"
        cread = f"work per dollar: not yet read on {stands}"
    L += ["| | Bare metal: the chip, its bill and its work | Through the cloud: the cloud's bill and its work |", "|---|---|---|",
          f"| **A and C: native** | {nat} | {cnat} |",
          f"| **B and D: Omni-Compass on top of native** | {on} | {con} |",
          f"| **Omni-Compass on native against native** | {bare_read} | {cread} |", ""]
    cap = _card(stands, "cap")
    if cap:
        f, d = cap
        r = d["rows"].get("work per energy (served requests per kJ)") or {}
        L += [f"At the usual load (`{f.relative_to(ROOT).as_posix()}`) every request is served in both arms, so the work is fixed by the "
              f"load: work per joule **{(r.get('reading') or '').replace('**', '')}** (raw {_raws(r)}).", ""]
    full = _card(stands, "cap-full")
    stacks = sorted(ROOT.glob("results/gpu/V*_STACKS_*_ABC.json"), key=lambda p: int(re.match(r"V(\d+)", p.name).group(1)))
    if stacks:
        sd = json.loads(stacks[-1].read_text(encoding="utf-8"))
        words = {}
        for r in (sd.get("rows") or {}).values() if isinstance(sd.get("rows"), dict) else (sd.get("rows") or []):
            t = str(r.get("reading", "")).replace("**", "")
            w = next((x for x in (K.STEADY, K.GAIN, K.LOSS, K.GIVEN, "the runs disagree") if t.startswith(x)), "shown, not judged (one repetition in a run)")
            words[w] = words.get(w, 0) + 1
        eng = (sd.get("engine") or "").split(" (")[0]
        org_txt = (f"on {eng} (`{stacks[-1].relative_to(ROOT).as_posix()}`): " + ", ".join(f"{n} row{'' if n == 1 else 's'} {w}" for w, n in sorted(words.items(), key=lambda kv: -kv[1]))
                   + (f"; not yet run on {stands}" if eng != stands else ""))
    else:
        org_txt = "not yet run"
    eight = sorted(ROOT.glob("results/gpu/V*_8*CARD*_ABC.json"))
    v = stands.split("-v")[1]
    az = sorted(ROOT.glob(f"results/live/V{v}_AKS*.json"))
    L += ["| Place | What runs there | Native against Omni-Compass on native |", "|---|---|---|",
          f"| Bare metal, one card | the card's own workload, at the usual load and fully loaded | {'three runs on ' + stands + ', above' if full else 'not yet run on ' + stands} |",
          f"| Bare metal, one card | the seven organisms (the spine, the four realms, the four stacked, the whole catalog) at 1, 10 and 100 copies | {org_txt} |",
          f"| Bare metal, the eight-card machine | the seven organisms at 1, 10 and 100 copies | {('read in `' + eight[-1].relative_to(ROOT).as_posix() + '`') if eight else NOT_RENTED} |",
          f"| Through the cloud: Azure | the cloud's own cluster and autoscaler, the whole engine at the max, the work meter | {'read in `' + az[-1].relative_to(ROOT).as_posix() + '`' if az else 'queued, its switch ' + _switch('azure') + '; not yet read on ' + stands} |",
          f"| Through the cloud: Google and Amazon | the same harness as Azure | wired, Google's switch {_switch('google')}, Amazon's {_switch('amazon')}; not yet run |", ""]
    # the seven organisms in the four arms (the founder's words of 1 November: "seven organisms ... ran native and with Omni-Compass on
    # them ... each in each arm ... A, B, C and D"): each organism's state in each arm, read from the newest organisms-on-the-card table
    # and the cloud's records; nothing typed
    ORG = (("spine", "The spine"), ("compute_ai_cloud", "Compute, AI and cloud"), ("physics_robotics_autonomous", "Physics, robotics and autonomous"),
           ("energy_facility_industrial", "Energy, facility and industrial"), ("distribution_specialized", "Distribution and specialized"),
           ("stack", "The four realms stacked"), ("tower", "The whole catalog (the tower)"))
    by_org = {}
    if stacks:
        for r in sd.get("rows") or []:
            o = by_org.setdefault(r.get("organism"), {"words": {}, "copies": set()})
            t = str(r.get("reading", "")).replace("**", "")
            w = next((x for x in (K.STEADY, K.GAIN, K.LOSS, K.GIVEN, "the runs disagree") if t.startswith(x)), None)
            if w:
                o["words"][w] = o["words"].get(w, 0) + 1
            o["copies"].add(r.get("copies"))
    seng = (sd.get("engine") or "").split(" (")[0] if stacks else ""
    org_cloud = sorted(ROOT.glob(f"results/live/V{v}_*ORGANISM*.json"))
    cloud_cell = (f"read in `{org_cloud[-1].relative_to(ROOT).as_posix()}`" if org_cloud else
                  f"not yet run (Azure queued, its switch {_switch('azure')}; Google's switch {_switch('google')}, Amazon's {_switch('amazon')}, each behind its $0 check)")
    L += ["**The seven organisms in the four arms.** Each organism runs native and with Omni-Compass on native, in each place: fourteen "
          "runs on bare metal (A and B) and fourteen through the cloud (C and D), each read by its bill and the work inside it. On bare "
          "metal each organism runs with one card inside at 1, 10 and 100 copies, and on the eight-card machine at 1, 10 and 100 copies "
          f"({NOT_RENTED.replace('not yet run; ', '')}).", "",
          "| Organism | A: bare metal, native | B: bare metal, Omni-Compass on native | C: the cloud, native | D: the cloud, Omni-Compass on native |",
          "|---|---|---|---|---|"]
    for key, name in ORG:
        o = by_org.get(key)
        if o:
            cps = ", ".join(str(c) for c in sorted(x for x in o["copies"] if x is not None))
            a = f"run with one A10 inside at {cps} copies, on {seng}" + (f"; not yet on {stands}" if seng != stands else "")
            b = (", ".join(f"{n} row{'' if n == 1 else 's'} {w}" for w, n in sorted(o["words"].items(), key=lambda kv: -kv[1]))
                 + f" against A (`{stacks[-1].relative_to(ROOT).as_posix()}`)")
        else:
            a = b = "not yet run"
        L.append(f"| {name} | {a} | {b} | {cloud_cell} | {cloud_cell} |")
    L.append("")
    ix = json.loads((ROOT / "results" / "OMNI_INDEX.json").read_text(encoding="utf-8"))
    h, sv = float(ix["headline_pct"]), float(ix.get("service_headline_pct") or 0)
    idx_eng = (m["standing"]["index"] or {}).get("engine", "its tables' engines")
    cats, svc = ix.get("categories") or {}, ix.get("service_categories") or {}
    def short(k):
        mm = re.search(r"\(([^)]*?)(?:, GitHub)?\)$", k)
        return mm.group(1) if mm and mm.group(1) != "GitHub" else re.sub(r"^Real | \(GitHub\)$", "", k)
    cat_txt = "; ".join(f"{short(k)} {_cat_word(x, svc.get(k))} {abs(x):.1f}%" for k, x in sorted(cats.items(), key=lambda kv: -kv[1]) if x is not None)
    w = m["whole"]
    L += [f"**The software both places carry.** Whichever the place, the same software end goes with Omni-Compass, and that is where "
          f"its benefit is measured so far: real software on GitHub's own computers (class L), never bare metal and never a cloud, and "
          f"with no bill in it. **The one number: {_cat_word(h, sv)} {abs(h):.1f}%**, the Omni index, every real product counted once, "
          f"work, speed and machines scored (`{INDEX_FILE}`, on {idx_eng}). By product: {cat_txt}. The same runs read on work and speed "
          f"alone, the machines left out, give {_cat_word(sv, sv)} {abs(sv):.1f}%"
          + (f"; multiplied layer by layer (Kubernetes, then the services on it) they compose to {index_word(w['index'])} {abs(w['index']):.1f}% "
             f"(`results/WHOLE_SYSTEM.md`, class S of class L tables)" if w and w.get("index") is not None else "")
          + ". These are one set of tests read three ways, so they never add; none of them is a bare-metal or a cloud bill: those are the "
          "boxes above. Whether the software's gain and the chip's add up on one machine is not yet measured: the organisms on the card "
          "and in the cloud measure it.", ""]
    return L


def markdown(m) -> str:
    rec, eng = m["rec"], m["engine"]
    img = lambda lv: f'<img src="{SIGNAL[lv][1]}" alt="{SIGNAL[lv][2]}" height="14">'
    L = [BEGIN, "", "## Benefit Against Native", ""]
    L += places_block(m)
    stands, st = m["stands"], m["standing"]
    idx = st["index"]
    if idx and idx.get("engine") == stands:
        w = index_word(float(idx["pct"]))
        way = "unchanged" if w == K.STEADY else f"{'up' if idx['pct'] > 0 else 'down'} {abs(idx['pct']):.1f}%"
        counts = "; ".join(f"{n} {word}" for word, n in st["words"])
        older = (f" {st['older']} still stand on an older engine ({', '.join(st['older_engines'])}) until their {stands} runs land."
                 if st["older"] else "")
        L.append(f"**On the engine that stands ({stands}), the Omni index reads {w}, {way}**, every real "
                 f"test together ([`{INDEX_FILE}`]({INDEX_FILE})), each benchmark run three times (A, B and C) on GitHub's own "
                 f"machines. Of the {st['bench']} benchmarks on the benefit sheet ([`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md)), "
                 f"{st['on']} read {stands}'s own three-run table: {counts}; every LOSS row is named with its cause in "
                 f"[`docs/LOSS_LEDGER.md`](docs/LOSS_LEDGER.md).{older}")
    else:
        led = m["ledger"]
        on_its = ""
        if idx and idx.get("pct") is not None:
            w = index_word(float(idx["pct"]))
            on_its = (f" On {idx.get('engine')}, the figure of record reads **{w} {abs(float(idx['pct'])):.1f}%**, every real test together "
                      f"by the index's own rule, its tables holding {idx.get('gain', 0)} rows GAIN, {idx.get('loss', 0)} LOSS and "
                      f"{idx.get('given', 0)} power given (the benefit sheet reads it {idx.get('benefit')}), never read as {stands}'s.")
        ledger = (f" The LOSS ledger ([`docs/LOSS_LEDGER.md`](docs/LOSS_LEDGER.md)) lists every LOSS row of the newest tables, "
                  f"{led['all']} in all, {led['native']} of them Omni-Compass against its own native, the rows do no harm is judged by, "
                  f"each with its cause where one is written." if led else "")
        L.append(f"**Not yet read on the engine that stands ({stands})**: the Omni index stands on "
                 f"{(idx or {}).get('engine', 'no engine')} until {stands}'s tables land ([`{INDEX_FILE}`]({INDEX_FILE})).{on_its}{ledger}")
    L += [""] + standing_block(stands)
    s0 = m["scen"][0]
    where = (f"on the engine that stands ({eng})" if eng == stands else
             f"on {eng}, the newest engine with its three runs in (the engine that stands, {stands}, runs it again)")
    A = m["arms"]
    L += ["", f"One real test of the whole loop, {where}, three runs on GitHub's own machines, on {A['where']}: native is "
          f"{A['native']}, and the other side is {A['on_native']}. It is one test, not the figure of record. On top of native, "
          f"Omni-Compass did {100 * s0['work']:.1f}% more work than native, its 95th-percentile response time "
          f"{100 * abs(s0['p95']):.1f}% {'shorter' if s0['p95'] < 0 else 'longer'}."]
    L += ["", "| Arm | Signal | Work | Response, 95th percentile | Machines | Units |", "|---|---|---|---|---|---|",
          f"| **Native**: {A['native']}, on {A['where']} | {img('lead')} the baseline | the baseline | the baseline | the baseline | the baseline |"]
    for s in m["scen"]:
        r = s["rows"]
        L.append(f"| **{s['name']}**: {A['on_native']}, {s['how']} | {img(s['signal'])} **{SIGNAL[s['signal']][0]}** | "
                 + " | ".join(said(r[g], g) if r[g] else "not read" for g, _ in GAUGES) + " |")
    L += ["", f"The signals: {img('ok')} GAINING, a GAIN and no LOSS; {img('lead')} STEADY, every row STEADY; {img('red')} "
          "REDLINING, a LOSS. Each word carries its size with no sign; the raw change, Omni-Compass − native over native, stands apart "
          "with its true sign, labelled raw. Units are the service's own copies: Omni-Compass adds them to buy the work and the speed, power given, "
          f"never a LOSS. Source: [`{m['path']}`]({m['path']}), three runs on GitHub's own machines (A, B and C from one commit); runs "
          f"{', '.join(f'{k} {v}' for k, v in rec['runs'].items())}; commit `{rec['commit'][:12]}`. The record's other arm, Omni-Compass "
          "alone on the muscles, stays in the record and is not carried here.", ""]
    L += ["### Bill by Route", "",
          "Through the cloud the whole engine runs at the max on the cloud's own cluster, on top of the cloud's own autoscaler, from 31 October; "
          "the cloud is the wire, so a cloud set shows whether Omni-Compass holds there: the bill read beside the work it bought, as the work per dollar "
          "(the work answered within the line divided by the bill), a bill that rises power given and the work rising more.", "",
          "Each route's bill is its native total cost, then Omni-Compass's, then the saving: 1 − (the Omni-Compass total ÷ the native total), "
          "each total the sum of its non-overlapping cost components inside the declared boundary, on a matched workload "
          "(`docs/THE_TUNE.md`, section 8). A component's own percent is a supporting measurement, never the bill. Where a price or a "
          "component is missing the bill reads unresolved; no price is assumed.", "",
          "| Route | Bill, native → Omni-Compass → saving | Supporting measurements |", "|---|---|---|"]
    on = m["scen"][0]["rows"]["machines"]
    L.append(f"| **On-site**: the software on your own bare metal | **unresolved** in dollars: no machine-hour or energy price is declared; "
             f"the chip's own energy on {m['stands']} is in the bare-metal box above | machines, Omni-Compass on top of native: {said(on, 'machines')} |")
    az = m["azure_now"]
    az_txt = (f"on Azure the {az['engine']} {az['name'] + ' ' if az['name'] else ''}set (run {az['run']}) runs first, one set at a time"
              + (f", and the {m['stands']} sets queue behind it" if az["behind"] else "")
              + " (`docs/RUN_LEDGER.md`, section 3; `scripts/azure_queue.txt`)") if az else f"no {m['stands']} Azure set has run yet (`scripts/azure_queue.txt`)"
    cloud = (f"read in [`{m['azure'][-1].relative_to(ROOT).as_posix()}`]({m['azure'][-1].relative_to(ROOT).as_posix()})" if m["azure"]
             else f"**unresolved**: not yet measured on {m['stands']}; {az_txt}; Google, Amazon "
                  "and the clouds a tester builds are wired and not yet run")
    L.append(f"| **Through the cloud**: the cloud's build, its bare metal at the back end, the software | {cloud} | the software end's, as on-site; "
             f"the provider's energy is not metered to the tenant |")
    w = m["whole"]
    if w and w["index"] is not None:
        cls = " and ".join(f"class {c}" for c in w.get("classes") or []) or "the tables'"
        sp, mc = 1 + w["speed"] / 100, 1 + w["machines"] / 100           # both native's over Omni-Compass's
        L += ["", f"Beside it: the whole organism at the software end, composed from the tables that stand, each on its own engine "
              f"([`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md), `tools/whole_system.py`; {', '.join(w['engines'])}), the cluster and "
              f"the services on it, by the rule that counts only what held in all three runs: work {w['work']:.1f}% more, the "
              f"95th-percentile response time {100 * (1 - 1 / sp):.1f}% shorter (native's time over Omni-Compass's, ×{sp:.3f}), machines "
              f"{100 * (1 - 1 / mc):.1f}% fewer (native's machines over Omni-Compass's, ×{mc:.3f}); the index over work, speed and machines "
              f"{index_word(w['index'])} {abs(w['index']):.1f}%. The energy and the cloud's bill are held at native's and never counted: the "
              "same power and the same bill (on the cluster the energy is a declared model of the machines, never a meter; the cloud is the "
              "wire), and the chip enters that composition as exactly 1 (the A100's three runs on omni-v21 read it STEADY); the chip's own receipt on "
              f"{stands} is the bare-metal box above. What the benefit "
              "cost the chip, the energy and the wire is listed row by row in section 3b of `results/WHOLE_SYSTEM.md`. A composition across engines "
              f"(class S over {cls} tables), never read as one engine's result; each total follows its tables as every benchmark runs again "
              f"on {stands}."]
    L += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "", END]
    return "\n".join(L)


def page_html(m) -> str:
    """The same answer, as the live engine page's first section (#s-answer)."""
    md = markdown(m)
    body = md.split("\n", 1)[1].rsplit("\n", 1)[0]
    out, table = [], []
    def flush():
        if table:
            head, rows = table[0], table[2:]
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            hs = cells(head)
            out.append('<div class="tableWrap"><table class="ans"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in hs)
                       + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f'<td data-h="{html.escape(hs[i] if i < len(hs) else "", quote=True)}">{inline(c)}</td>'
                                                                         for i, c in enumerate(cells(r))) + "</tr>" for r in rows)
                       + "</tbody></table></div>")
            table.clear()
    for ln in body.split("\n"):
        if ln.startswith("|"):
            table.append(ln); continue
        flush()
        if ln.startswith("## "):
            continue
        if ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
    flush()
    return ('<section class="stack" id="s-answer" aria-label="Benefit Against Native">\n  <h2><span class="sn">2b</span>Benefit Against Native</h2>\n  '
            + "\n  ".join(out) + "\n</section>")


def inline(s: str) -> str:
    keep = []
    def stash(x):
        keep.append(x); return f"\x00{len(keep) - 1}\x00"
    s = re.sub(r'<img src="docs/engine/signals/(\w+)\.svg" alt="([^"]+)" height="14">',
               lambda mm: stash(f'<span class="mlamp lv-{ {"redlining": "red", "steady": "even", "accelerating": "ok"}[mm.group(1)] }" title="{mm.group(2)}"></span>'), s)
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\[`([^`]+)`\]\(([^)]+)\)", r"<code>\1</code>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return re.sub("\x00(\\d+)\x00", lambda mm: keep[int(mm.group(1))], s)


SVG = {"accelerating": '<circle cx="7" cy="7" r="6" fill="#50c878"/>',
       "steady": '<path d="M7 1 L13 7 L7 13 L1 7 Z" fill="#f5c518"/>',
       "redlining": '<path d="M4.5 1 H9.5 L13 4.5 V9.5 L9.5 13 H4.5 L1 9.5 V4.5 Z" fill="#ff4d55"/>'}


def signals():
    d = ROOT / "docs" / "engine" / "signals"
    want = {f"{k}.svg": f'<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" role="img" aria-label="{k}">{v}</svg>\n' for k, v in SVG.items()}
    return d, want


def place(text: str, block: str, anchor: str) -> str:
    if BEGIN in text:
        a = text.index(BEGIN); z = text.index(END, a) + len(END)
        return text[:a] + block + text[z:]
    i = text.index(anchor)
    return text[:i] + block + "\n\n" + text[i:]


def place_readme(text: str, block: str) -> str:
    """The answer in the README: straight under the notice and the one line that says what Omni-Compass is."""
    if BEGIN in text:
        a = text.index(BEGIN); z = text.index(END, a) + len(END)
        return text[:a] + block + text[z:]
    tag = "**More work, faster, on fewer machines, for the same energy and the same bill, on top of the stack you already run.**"
    i = text.index(tag) + len(tag)
    return text[:i] + "\n\n" + block + text[i:]


def place_after_title(page: str, block: str) -> str:
    """The answer on the live engine page: its own section, where its markers stand (since 31 October straight after the title page,
    so the page reads in the order its table of contents numbers it: the wall 0, the title ii, the answer iii, the bottom line iv);
    on a page without the markers, under the legal notice."""
    if BEGIN in page:
        a = page.index(BEGIN); z = page.index(END, a) + len(END)
        return page[:a] + block + page[z:]
    n = page.index('id="notice"'); i = page.index("</p>", n) + len("</p>")
    return page[:i] + "\n" + block + page[i:]


def main(argv) -> int:
    check, m = "--check" in argv, model()
    md = markdown(m)
    new_readme = place_readme(README.read_text(encoding="utf-8"), md)
    page = PAGE.read_text(encoding="utf-8")
    sec = page_html(m)
    blk = f"{BEGIN}\n{sec}\n{END}"
    new_page = place_after_title(page, blk)
    d, svgs = signals()
    differ = [n for n, new, old in (("README.md", new_readme, README.read_text(encoding="utf-8")),
                                    ("the live engine page", new_page, page)) if new != old]
    differ += [f"docs/engine/signals/{f}" for f, s in svgs.items() if not (d / f).exists() or (d / f).read_text(encoding="utf-8") != s]
    if check:
        print("headline: " + ("the README and the live engine page give the answer the files give" if not differ else f"{', '.join(differ)} differ: run python3 tools/headline.py"))
        return 1 if differ else 0
    README.write_text(new_readme, encoding="utf-8"); PAGE.write_text(new_page, encoding="utf-8")
    d.mkdir(parents=True, exist_ok=True)
    for f, s in svgs.items():
        (d / f).write_text(s, encoding="utf-8")
    print(f"headline: written from {m['path']} ({m['engine']}): " + "; ".join(f"{s['name']} {SIGNAL[s['signal']][0]}, work {100 * s['work']:+.1f}%" for s in m["scen"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
