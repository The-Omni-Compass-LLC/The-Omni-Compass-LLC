# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Records the stacks the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) replays one at a time beside the
live controller: each stack's own model in the repository, run as the repository runs it, native first and then
Omni-Compass on top of native, the same load on the same seed, second by second.

  gpu     realms/gpu_card.py (inside the omni-v7 fingerprint): one card on its own physics and its own firmware (boost a
          bin while there is work, knocked down three while the draw is over the power limit). Native is the card as
          shipped (150 W) or under an operator's cap (105 W); omni is the same card with the two-wire plug on top (the
          clock ceiling and the power limit), the compass law and the verdict, as run() wires them. Two kinds of work:
          AI token generation (memb 0.85) and compute-bound work (memb 0). Seeds 5100, 5101 and 5102 (runs A, B and C,
          the model's untouched seeds). Every verdict event is recorded with the cost the trial measured.

Readings: the paired change per second over blocks of 30 s, Student's t, in each run; the three-run rule
(tools/readings.py), the word by the gauge's aim. Evidence class S (our own models). Usage:
python3 docs/engine/export_scenarios.py OUT.json
"""
from __future__ import annotations

import json
import math
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import realms.gpu_card as G                                              # noqa: E402
from omnicompass.verdict import Verdict                                  # noqa: E402

GPU_SEEDS = (5100, 5101, 5102)
from omnicompass.student_t import t95 as _t95    # noqa: E402  (the exact two-sided 95% point of Student's t, omni-v9)
from tools.readings import relative_runs_reading  # noqa: E402  (the one key, written once)


def reading(runs, aim):
    """The three-run rule, the one key's (tools/readings.py, the founder's order of 24 October 2026: a change of 0.5% or more,
    the mean of the runs, is a change, read by the gauge's aim; STEADY only under 0.5%)."""
    return relative_runs_reading(runs, aim)


def paired(a, b, block):
    """The paired change of b against a, per sample, averaged over blocks, with its 95% interval, relative to a's mean."""
    d = [y - x for x, y in zip(a, b)]
    bl = [sum(d[i:i + block]) / block for i in range(0, len(d) - block + 1, block)]
    m = st.mean(bl); sd = st.stdev(bl) if len(bl) > 1 else 0.0
    half = _t95(len(bl) - 1) * sd / math.sqrt(len(bl))
    base = st.mean(a) or 1e-12
    return {"native": st.mean(a), "omni": st.mean(b), "change": m / base, "lo": (m - half) / base, "hi": (m + half) / base}


# ---- the GPU card ----------------------------------------------------------------------------------------------------
class AuditedVerdict(Verdict):
    """realms/gpu_card.py's verdict, unchanged; every event it returns is kept for the page with the decision it came at."""
    log = []

    def tick(self, calm):
        r = super().tick(calm)
        if r[2]:
            ev = dict(r[2]); ev["t"] = self.t
            if "cost_native" in ev:
                ev["rise"] = ev["cost_step"] / ev["cost_native"] - 1.0
            AuditedVerdict.log.append(ev)
        return r


def gpu_run(seed, arm, memb):
    """One run of realms/gpu_card.run, the card read every tick and kept per second (50 ticks)."""
    per = int(round(1.0 / G.TICK))
    acc = {"p": 0.0, "f": 0.0, "T": 0.0, "q": 0.0, "w": 0.0, "srv": 0.0, "over": 0}
    sec = {k: [] for k in ("power", "clock", "ceiling", "limit", "temp", "queue", "resp_ms", "served", "over")}
    orig = G.Card.tick

    def tick(card):
        s0 = card.m["served"]
        orig(card)
        w = card.resp[-1][0]
        acc["p"] += card.last_p; acc["f"] += card.f; acc["T"] += card.T; acc["q"] += card.Q; acc["w"] += w
        acc["srv"] += card.m["served"] - s0; acc["over"] += w > G.SLO_S
        if card.k % per == 0:
            sec["power"].append(round(acc["p"] / per, 2)); sec["clock"].append(round(acc["f"] / per, 4))
            sec["temp"].append(round(acc["T"] / per, 2)); sec["queue"].append(round(acc["q"] / per, 3))
            sec["resp_ms"].append(round(1000 * acc["w"] / per, 3)); sec["served"].append(round(acc["srv"], 3))
            sec["over"].append(round(acc["over"] / per, 3))
            sec["ceiling"].append(round(card.ceiling, 4)); sec["limit"].append(round(card.limit, 2))
            for k in acc:
                acc[k] = 0.0
    G.Card.tick, G.Verdict = tick, AuditedVerdict
    AuditedVerdict.log = []
    try:
        summary = G.run(seed, arm, 600.0, memb)
    finally:
        G.Card.tick, G.Verdict = orig, Verdict
    sec["events"] = AuditedVerdict.log
    sec["summary"] = {k: summary[k] for k in ("energy_j", "served", "work_per_kj", "p50_ms", "p95_ms", "p99_ms", "viol_share",
                                              "hammer_per_s", "clock_mean", "t_peak", "writes", "restored")}
    return sec


GPU_GAUGES = {   # name: (aim, per-second series, label)
    "work": ("up", "served", "requests served"),
    "energy": ("spent", "power", "energy (the card's draw)"),
    "resp": ("down", "resp_ms", "response time"),
    "over": ("down", "over", "share of time over the service line"),
}


def gpu():
    out = {"seeds": list(GPU_SEEDS), "slo_ms": 1000 * G.SLO_S, "kill_s": 0.9 * 600, "settings": {}}
    for key, (base, top, memb) in {"ai": ("native", "omni", 0.85), "compute": ("native", "omni", 0.0),
                                   "ai_cap": ("cap", "cap_omni", 0.85), "compute_cap": ("cap", "cap_omni", 0.0)}.items():
        sec = {"memb": memb, "limit_w": G.LIMIT_MIN if base == "cap" else G.LIMIT_DEFAULT, "runs": {}, "readings": {}}
        for sd in GPU_SEEDS:
            n, o = gpu_run(sd, base, memb), gpu_run(sd, top, memb)
            sec["runs"][str(sd)] = {"native": n, "omni": o}
            for g, (aim, s, _) in GPU_GAUGES.items():
                sec["readings"].setdefault(g, {"aim": aim, "runs": []})["runs"].append(paired(n[s], o[s], 30))
            wpk = (o["summary"]["work_per_kj"] / n["summary"]["work_per_kj"]) - 1.0
            # requests per kJ: the ratio of two judged rows, one number a run with no interval of its own, so shown, not judged
            sec["readings"].setdefault("wpk", {"aim": "shown", "runs": []})["runs"].append(
                {"native": n["summary"]["work_per_kj"], "omni": o["summary"]["work_per_kj"], "change": wpk, "lo": wpk, "hi": wpk})
        for g, v in sec["readings"].items():
            v["reading"] = reading(v["runs"], v["aim"])
            print(f"gpu {key:12s} {g:7s} {v['reading']:16s} " + "  ".join(f"{r['change']*100:+.3f}%" for r in v["runs"]))
        out["settings"][key] = sec
    return out


# ---- Linux: conveyance of the CFS quota on one host ------------------------------------------------------------------
LINUX_SEEDS = (3000, 3001, 3002)
LINUX_GAUGES = {   # name: (aim, per-second series)
    "work": ("up", "lam"),
    "resp": ("down", "ms"),
    "busy": ("spent", "busy"),
    "limit": ("spent", "limit_m"),
    "pods": ("spent", "pods"),
}


def linux_run(seed, arm):
    """One run of tools/model_gate.py worker_convey, unchanged: its own locals read at the end of every one-second tick
    (sys.settrace on the line that adds up the tick), and its own result line."""
    import contextlib
    import inspect
    import io
    import tempfile
    from tools import model_gate as TG
    src, first = inspect.getsourcelines(TG.worker_convey)
    mark = first + next(i for i, s in enumerate(src) if s.strip().startswith("busy_sum += busy"))
    code = TG.worker_convey.__code__
    sec = {k: [] for k in ("lam", "ms", "busy", "pods", "ready", "limit_m", "backlog")}

    def local(frame, event, arg):
        if event == "line" and frame.f_lineno == mark:
            L = frame.f_locals
            sec["lam"].append(round(L["lam"], 3)); sec["ms"].append(round(L["mean_ms"], 2)); sec["busy"].append(round(L["busy"], 4))
            sec["pods"].append(len(L["pods"])); sec["ready"].append(sum(1 for p in L["pods"] if p["ready"]))
            sec["limit_m"].append(sum(p["limit"] for p in L["pods"])); sec["backlog"].append(round(L["backlog"], 3))
        return local

    def call(frame, event, arg):
        return local if frame.f_code is code else None
    buf = io.StringIO()
    with tempfile.TemporaryDirectory() as td, contextlib.redirect_stdout(buf):
        sys.settrace(call)
        try:
            TG.worker_convey(arm, seed, td)
        finally:
            sys.settrace(None)
    sec["summary"] = json.loads(buf.getvalue().strip().splitlines()[-1])
    # the checkout the engine was imported from, as tools/model_gate.py checks it: this one, checked here and never recorded (a
    # machine's own path would make the record differ from one machine to the next)
    got = sec["summary"].pop("engine_tree", None)
    if got is not None and Path(got).resolve() != ROOT.resolve():
        raise RuntimeError(f"the engine was imported from {got}, not from this checkout {ROOT}")
    return sec


def linux():
    out = {"seeds": list(LINUX_SEEDS), "step_s": 150, "steps": [1, 2, 3, 1, 2, 1] * 4, "runs": {}, "readings": {}}
    for sd in LINUX_SEEDS:
        n, o = linux_run(sd, "native"), linux_run(sd, "omni")
        out["runs"][str(sd)] = {"native": n, "omni": o}
        for g, (aim, s) in LINUX_GAUGES.items():
            out["readings"].setdefault(g, {"aim": aim, "runs": []})["runs"].append(paired(n[s], o[s], 150))
        for g, aim in (("start_wait_s", "down"), ("p95_ms", "down"), ("alert_minutes", "down")):
            a, b = n["summary"][g], o["summary"][g]
            c = (b - a) / a if a else 0.0
            out["readings"].setdefault(g, {"aim": aim, "runs": [], "single": True})["runs"].append(
                {"native": a, "omni": b, "change": c, "lo": c, "hi": c})
    for g, v in out["readings"].items():
        # one value a run is no interval: three single values that agree cannot be judged (tools/confirm_abc.py verdict), so
        # the gauge is shown, never GAIN or LOSS
        v["reading"] = "shown, not judged (one value a run, no interval)" if v.get("single") else reading(v["runs"], v["aim"])
        print(f"linux {g:14s} {v['reading']:16s} " + "  ".join(f"{r['change']*100:+.2f}%" for r in v["runs"]))
    for sd in map(str, LINUX_SEEDS):                                   # the page draws every fifth second
        for arm in ("native", "omni"):
            r = out["runs"][sd][arm]
            for k in ("lam", "ms", "busy", "pods", "ready", "limit_m", "backlog"):
                r[k] = r[k][::5]
    return out


# ---- every three-run table, found by itself ----------------------------------------------------------------------------
FIRST_ENGINE = 8   # tables from omni-v8 on; older engines' tables are the road (docs/history), never on the page
SIM_STACK = {"CITYLEARN": "Energy and the grid", "PANDAPOWER": "Energy and the grid", "MUJOCO": "Physics and robotics",
             "SWARM": "Physics and robotics"}   # the outside simulators' stacks, by the simulator a table names in its file name
STACK_ORDER = ("Kubernetes", "Linux services", "Energy and the grid", "Physics and robotics", "Other")


def tables():
    """Every benchmark's newest three-run table (results/live/V<n>_<BENCHMARK>.md, n from FIRST_ENGINE), found by itself, with
    its stack and evidence class read from its own files: a table whose JSON holds its workloads is a Linux service and one
    whose JSON holds its rows is Kubernetes (both real software, class L); a table with no JSON beside it is an outside
    simulator driven by our own runner (class S). Nothing is listed by hand: a table that lands is on the page at the next
    build, and a later engine's table replaces an earlier one's the moment it lands with a reading (tools/readings.py, landed:
    a table whose three runs share no workload leaves the older engine's table standing; two engines are never pooled)."""
    import re
    from tools.readings import landed
    best = {}
    for f in (ROOT / "results" / "live").glob("V*_*.md"):
        m = re.fullmatch(r"V(\d+)_([A-Z0-9_]+)", f.stem)
        if not m or int(m.group(1)) < FIRST_ENGINE or "three-run table" not in f.read_text(encoding="utf-8").split("\n", 1)[0]:
            continue
        n, base, ok = int(m.group(1)), m.group(2), landed(f)
        if base not in best or (ok, n) > (best[base][2], best[base][0]):
            best[base] = (n, f.stem, ok)
    out = []
    for base, (n, stem, _) in best.items():
        j = ROOT / "results" / "live" / f"{stem}.json"
        meta = json.loads(j.read_text(encoding="utf-8")) if j.exists() else None
        if isinstance(meta, dict) and "workloads" in meta:
            stack, cls, kind = "Linux services", "L", "db"
        elif isinstance(meta, dict) and "rows" in meta:
            stack, cls, kind = "Kubernetes", "L", "k8s"
        else:
            stack, cls, kind = SIM_STACK.get(base, "Other"), "S", None
        out.append({"base": base, "n": n, "stem": stem, "stack": stack, "cls": cls, "kind": kind})
    return sorted(out, key=lambda t: (STACK_ORDER.index(t["stack"]), t["base"]))


def table_title(stem):
    """A table's own title, with what tells two tables of one benchmark apart: the verdict's objective it names, and native
    exactly as the vendor ships it (a _SHIPPED table)."""
    text = (ROOT / "results" / "live" / f"{stem}.md").read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("# ").split(": the A/B/C")[0].strip()
    for obj in ("service", "resource"):
        if f"(the objective: {obj})" in text:
            title += f", {obj} objective"
    if stem.endswith("_SHIPPED") and "as shipped" not in title:
        title += ", native as shipped"
    return title


def receipt_word(rd):
    """A reading's word, from the key's one reader (tools/readings.py word_of); a row shown and not judged reads "shown"."""
    from tools.readings import word_of
    return word_of(rd) or "shown"


NUM = r"[-+\u2212=]?\d[\d,]*(?:\.\d+)?(?:e[-+]?\d+)?"   # a cell beside STEADY carries "=" (the key's sign rule, 20 October)


def even_reason(abc):
    """Why a STEADY row is STEADY, read from its three runs' own cells (each 'change (low to high)', or a change alone): the
    kind and the bound. 'same': every run reads zero with a zero-wide interval (Omni-Compass held it native); 'split': a run
    is clear of zero but not all three the same way (STEADY by the three-run rule); else the largest change any run's interval
    still allows: 'tight' within 2%, 'within' within 10%, 'wide' past 10% (too noisy to tell at these repetitions); a table
    that prints no interval: 'changes', the largest change read."""
    import re
    f = lambda x: float(x.replace(",", "").replace("\u2212", "-").lstrip("="))
    runs, pct = [], False
    for c in abc:
        if not c:
            continue
        m = re.match(rf"\s*({NUM})\s*(%?)\s*(?:[A-Za-z/]+\s*)?(?:\(({NUM})\s*to\s*({NUM})\))?", c)
        if not m:
            continue
        pct = pct or bool(m.group(2))
        runs.append((f(m.group(1)), f(m.group(3)) if m.group(3) else None, f(m.group(4)) if m.group(4) else None))
    if not runs:
        return {"kind": "unread", "bound": None, "pct": pct}
    if all(ch == 0 and (lo in (None, 0) and hi in (None, 0)) for ch, lo, hi in runs):
        return {"kind": "same", "bound": 0.0, "pct": pct}
    if all(lo is not None for _, lo, _ in runs):
        if any(lo > 0 or hi < 0 for _, lo, hi in runs):
            return {"kind": "split", "bound": max(max(abs(lo), abs(hi)) for _, lo, hi in runs), "pct": pct}
        b = max(max(abs(lo), abs(hi)) for _, lo, hi in runs)
        kind = ("tight" if b <= 2 else "within" if b <= 10 else "wide") if pct else "within"
        return {"kind": kind, "bound": b, "pct": pct}
    return {"kind": "changes", "bound": max(abs(ch) for ch, _, _ in runs), "pct": pct}


AIM_CODE = {"higher": "up", "lower": "down", "spent": "spent", "work per resource": "per", "never more": "never", "never less": "up"}


def runs_of(src, rows):
    """Each judged row's aim and each run's own word and raw change, from the table's JSON twin (the mathematics seat of 24
    October): since tools/reread.py rewrote the kind tables, each run's printed number wears that run's word's sign, so a page
    that read the cell's sign as the gauge's direction printed the opposite word. The JSON holds every run's native, difference
    and interval; each row is matched to its gauge in order by its reading, as tools/reread.py patch_md matches them. A row of a
    table with no JSON twin (an outside simulator's) is left as printed: its cells carry the gauge's own direction.
      aim  up, down, spent, per or never (tools/readings.py HIGHER, LOWER, SPENT, WORK_PER, NEVER_MORE)
      rw   each run's own word (tools/readings.py run_word: 0.5% or more read by the aim, STEADY under it; None for never more)
      rv   each run's raw change as [change, low, high, in percent of native]: percent where native is not zero, else the
           gauge's own unit"""
    j = Path(src).with_suffix(".json")
    if not j.exists():
        return
    from tools.reread import gauges, bare
    from tools.readings import aim as aim_of, run_word
    try:
        data = json.loads(j.read_text(encoding="utf-8"))
    except ValueError:
        return
    if not isinstance(data, dict):
        return
    i = 0
    for path, g in gauges(data):
        rd, aim_raw, rs = bare(g.get("reading")), g.get("aim"), g.get("runs")
        while i < len(rows):
            row = rows[i]; i += 1
            if bare(row["r"].split("shown and not counted: ")[-1]) == rd:
                row["key"] = path[-1]                     # the gauge's own name in the table's JSON (for the key's resource list)
                a = aim_of(aim_raw) if aim_raw else None
                if a in AIM_CODE and isinstance(rs, list) and len(rs) == 3 and all(isinstance(r, dict) and r.get("diff") is not None
                                                                                  and r.get("native") is not None for r in rs):
                    row["aim"] = AIM_CODE[a]
                    row["rw"] = [run_word(r, a) for r in rs]
                    rv = []
                    for r in rs:
                        nat, d = r["native"], r["diff"]
                        lo, hi = (list(r.get("ci95") or []) + [None, None])[:2]
                        ok = lambda v: isinstance(v, (int, float)) and v == v
                        if nat:
                            rv.append([round(100 * d / abs(nat), 4), round(100 * lo / abs(nat), 4) if ok(lo) else None,
                                       round(100 * hi / abs(nat), 4) if ok(hi) else None, True])
                        else:
                            rv.append([round(d, 6), round(lo, 6) if ok(lo) else None, round(hi, 6) if ok(hi) else None, False])
                    row["rv"] = rv
                    from tools.readings import evidence
                    ev = evidence(rs, a)        # the evidence apart from the word (the referee's work order of 25 October)
                    row["ev"] = {k: (round(v, 4) if isinstance(v, float) else [round(x, 4) for x in v] if k == "mean_ci95_pct" else v)
                                 for k, v in ev.items() if k in ("strength", "steady", "disagree", "runs", "clear", "clear_with_mean",
                                                                 "with_mean", "mean_pct", "mean_ci95_pct") and v is not None}
                break


def receipt(name, path=None):
    """Every judged row of results/live/<name>.md as written (or of the table at path, written by the same tool): its table's
    heading, the gauge, runs A, B and C, the reading."""
    import re
    rows, hdr, sect, title, tuning = [], None, "", "", False
    src = Path(path) if path else ROOT / "results" / "live" / f"{name}.md"
    for ln in src.read_text(encoding="utf-8").splitlines():
        if ln.startswith("# ") and not title:
            title = ln[2:].split(": the A/B/C")[0].strip()
        if ln.startswith("#"):
            sect, hdr = ln.lstrip("# ").strip(), None
            tuning = bool(re.search(r"not counted|\(the tuning", sect))   # the case the rules were frozen on: shown, never counted
            continue
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells[-1] == "Reading":
            hdr = cells
            continue
        if hdr is None or re.fullmatch(r"[|\-: ]+", ln) or len(cells) != len(hdr):
            continue
        d = dict(zip(hdr, cells))
        gauge = cells[0] if hdr[0] != "Cap (cores)" else f"cap {cells[0]} cores: {cells[1]}"
        w = receipt_word(d["Reading"])
        rows.append({"s": sect, "g": gauge.replace("`", ""), "abc": [d.get(k, "") for k in "ABC"],
                     "r": ("the tuning case, shown and not counted: " if tuning else "") + d["Reading"].replace("**", ""),
                     "w": "tuning" if tuning else w})
    count = {}
    for r in rows:
        count[r["w"]] = count.get(r["w"], 0) + 1
    runs_of(src, rows)
    title = table_title(name) if not path else title
    even = [{"s": r["s"], "g": r["g"], "abc": r["abc"], "r": r["r"], **{k: r[k] for k in ("aim", "rw", "rv") if k in r}, **even_reason(r["abc"])}
            for r in rows if r["w"] == "STEADY"]
    # the rows a table shows and does not judge (its preregistration's own rule), kept so their sizes are seen: a resource a
    # table only shows, CPU used beside a response time, is the price of the work
    # a shown row carries no aim of its own (its table does not judge it); whether it is a resource spent or held is the key's own list
    # (tools/readings.py SPENT_GAUGES, by the gauge's name in the table's JSON), never a guess from its words: a row of a table with no
    # JSON twin carries no such mark
    from tools.readings import SPENT_GAUGES
    shown = [{"s": r["s"], "g": r["g"], "abc": r["abc"], "r": r["r"], **({"tuning": True} if r["w"] == "tuning" else {}),
              **({"key": r["key"], "spent": r["key"] in SPENT_GAUGES} if "key" in r else {})}
             for r in rows if r["w"] in ("shown", "tuning")]
    return {"file": f"results/live/{name}.md" if not path else None, "title": title, "rows": [r for r in rows if r["w"] not in ("STEADY", "shown", "tuning")],
            "count": count, "even": even, "shown": shown}


COMMON = {"Kubernetes", "Omni-Compass", "Omni", "The", "With", "Native", "Real", "Linux", "GitHub"}
# the pages written from every table (the manuals, the state of play, the levels, the power page, the deviations register, the
# benefit sheet, the wiring verdicts, the dossier, the summaries): each names every table and gauge, and none is a table's cause
AGGREGATE = __import__("re").compile(r"MANUAL|STATE_OF_PLAY|LEVELS|POWER|DEVIATIONS|BENEFIT_SHEET|WIRING_VERDICTS|DOSSIER|REFEREE_SUMMARY|"
                                     r"THE_RECEIPTS|ENGINE_COVERAGE|EVIDENCE_LEDGER|REGISTER|CHANGELOG|LIMITATIONS")


def causes(r):
    """The repository's own pages on the cause of a table's LOSS rows: a page in docs/ whose title names the gauge and whose
    text names the benchmark (a word of the table's title that only it carries, as KEDA), as docs/POD_START_WAIT.md is for
    the pod start wait under KEDA's HTTP add-on. Read from the pages themselves; a row with no such page names none."""
    import re
    docs = []
    for f in sorted((ROOT / "docs").glob("*.md")):
        if AGGREGATE.search(f.name):
            continue                     # a page written from every table names them all and is no table's cause
        t = f.read_text(encoding="utf-8")
        h = next((ln[2:].strip() for ln in t.splitlines() if ln.startswith("# ")), "")
        docs.append((f, h, t))
    tokens = {w for w in re.findall(r"[A-Z][A-Za-z0-9-]{2,}", r["title"]) if w not in COMMON}
    out = []
    for row in r["rows"]:
        if row["w"] != "LOSS":
            continue
        base = re.split(r"[,(]", row["g"])[0].strip()
        hit = next(({"gauge": base, "file": str(f.relative_to(ROOT)), "title": h} for f, h, t in docs
                    if base.lower() in h.lower() and any(tok in t for tok in tokens)), None)
        if hit is None:
            # else a section of a page that names this table's own file and the gauge's own word, as the preregistration's
            # amendment does for the batch rig: its heading is the cause's title
            key = base.split()[-1].lower(); stem = Path(r["file"]).stem
            for f, h, t in docs:
                for sec in re.split(r"\n(?=## )", t):
                    if f"{stem}.md" in sec and key in sec.lower():
                        hit = {"gauge": base, "file": str(f.relative_to(ROOT)), "title": sec.splitlines()[0].lstrip("# ").strip()}
                        break
                if hit:
                    break
        if hit:
            out.append(hit)
    return out


def receipts():
    out = []
    for t in tables():
        r = receipt(t["stem"]); r.update(stack=t["stack"], cls=t["cls"], engine=f"omni-v{t['n']}", causes=causes(r)); out.append(r)
        print(f"receipt {t['stem']:22s} {r['engine']} {t['stack']:20s} {r['count']}")
    return out


# ---- every muscle of the catalog and the seven organisms, on the engine that stands -----------------------------------
ORGANISMS = {"spine": "Spine", "compute_ai_cloud": "Compute / AI / Cloud",
             "physics_robotics_autonomous": "Physics / Robotics / Autonomous", "energy_facility_industrial": "Energy / Facility / Industrial",
             "distribution_specialized": "Distribution / Specialized", "stack": "Four Stacked",
             "tower": "Whole Tower"}
REALM_CODE = {"compute_ai_cloud": "C", "physics_robotics_autonomous": "P", "energy_facility_industrial": "E", "distribution_specialized": "D"}


def realms():
    """results/realms_v5/REALMS_V5.json as the realms runner wrote it: the seven organisms under three loads and every
    muscle alone under two, native against Omni-Compass on top, seeds 3000 to 3009."""
    d = json.loads((ROOT / "results" / "realms_v5" / "REALMS_V5.json").read_text(encoding="utf-8"))
    r4 = lambda x: round(x, 6)
    orgs = {}
    for load, by in d["organisms"].items():
        orgs[load] = [{"key": k, "name": ORGANISMS[k], "n": v["n"], "label": v["label"], "viol_native": v["totals"]["viol_native"],
                       "viol_max": v["totals"]["viol_max"], "steps": v["totals"]["steps"],
                       "work": [r4(x) for x in v["summary"]["work"]], "energy": [r4(x) for x in v["summary"]["energy"]],
                       "viol_pp": [r4(x) for x in v["summary"]["viol_pp"]], "flagged": len(v.get("plants_flagged") or [])}
                      for k, v in by.items()]
    musc = []
    for m in d["muscles"]:
        row, out = m["row"], []
        for load in ("normal", "line"):
            v = m["loads"][load]
            ln = v.get("line") or [None, None, None, None]
            out.append([v["label"], v["viol_native"], v["viol_max"], r4(v["summary"]["work"][0]), r4(v["summary"]["energy"][0]),
                        ln[0], ln[1]])
        musc.append([row["muscle"], row["family"], REALM_CODE[row["realm"]], row["template"], row["knob"], m["label"], out])
    run = {k: d["run"][k] for k in ("started", "commit", "seeds", "engine", "engine_digest", "dial", "muscles")}
    print(f"realms {run['engine']} {len(musc)} muscles, {len(orgs)} loads")
    return {"run": run, "organisms": orgs, "muscles": musc}


def main(out):
    data = {"gpu": gpu(), "linux": linux(), "receipts": receipts(), "realms": realms()}
    Path(out).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "scenarios.json")
