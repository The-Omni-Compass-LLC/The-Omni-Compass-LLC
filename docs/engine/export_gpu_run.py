# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The one metered chip run, second by second, for the live benchmark engine's GPU card monitor (class P: the card's own meter).

results/gpu/run-20261024T091235Z is the NVIDIA A100 (SXM4, 40 GB) run of 24 October on Lambda (workflow run 40079645681: 10
paired repetitions, 600 s an arm, the card governor of omni-v18 at commit e3b05dc on the branch gpu-omni-v18): the engine that
stands on a real card, its own meter recording native beside Omni-Compass. The monitor replays it as it was recorded: every
arm's power draw, enforced power limit, clock and temperature from nvidia-smi (200 ms samples, binned to 2 s), its requests
served and 95th-percentile response in 10 s windows, and the governor's decisions from its own audit. Nothing is modelled; a
lane with no file stays empty. The run's total table is carried as GPU_REPS.md prints it, each row re-read by the one key that
stands (a change of 0.5% or more either way is a change, STEADY only under it; tools/readings.py), so the words follow the gauge's
aim. The A10 run of 2 October (results/gpu/run-20261002T082232Z, the card controller of commit c908054) stays as its own record.

  python3 docs/engine/export_gpu_run.py OUT.json
"""
from __future__ import annotations

import csv
import datetime
import json
import subprocess
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from tools.readings import SIZE_FLOOR, reading_kind, word_of  # noqa: E402  (the one floor, the reading's kind and its one word, written once)

RUN = ROOT / "results" / "gpu" / "run-20261024T091235Z"
ARMS = ("native", "watch", "omni")
BIN_S = 2.0
REQ_BIN_S = 10.0
# every gauge of the run's total table by what it is for (the one key): time waited is LOWER, work is HIGHER, a resource is SPENT
AIMS = {"work per energy": "WORK_PER", "work per wall energy": "WORK_PER", "energy": "SPENT", "power": "SPENT", "requests served": "HIGHER",
        "requests not served": "LOWER", "response time": "LOWER", "temperature": "SPENT", "power-capped share": "SHOWN"}


def _aim(gauge: str) -> str:
    g = gauge.lower().strip("* ")
    for k, v in sorted(AIMS.items(), key=lambda kv: -len(kv[0])):     # the longest name first: "power-capped share" before "power"
        if g.startswith(k):
            return v
    return "SHOWN"


def _word(aim: str, change: str, interval: str) -> str:
    """The word by the gauge's aim and the one key that stands: the row's change in percent of native, 0.5% or more either way
    a change by its sign (SIZE_FLOOR), STEADY only under it; a row printed with no percent (a count from zero) is read by its own
    interval, clear of zero or not."""
    if aim == "SHOWN":
        return "shown, not judged"
    pct = re.fullmatch(r"\s*([-+]?\d+(?:\.\d+)?)%\s*", change.replace("−", "-"))
    if pct:
        rel = float(pct.group(1)) / 100.0
        if abs(rel) < SIZE_FLOOR:
            return "STEADY"
        up = rel > 0
    else:
        m = re.findall(r"[-+]?\d[\d,]*(?:\.\d+)?(?:e[-+]?\d+)?", interval.replace("−", "-"))
        if len(m) < 2:
            return "unread"
        lo, hi = float(m[0].replace(",", "")), float(m[1].replace(",", ""))
        if lo <= 0 <= hi:
            return "STEADY"
        up = hi > 0
    if aim == "HIGHER":
        return "GAIN" if up else "LOSS"
    if aim == "LOWER":
        return "LOSS" if up else "GAIN"
    if aim == "WORK_PER":
        return "GAIN" if up else "power given"
    return "power given" if up else "GAIN"          # SPENT: a resource that rose is power given, one that fell a cut


def _stamp(s: str) -> float:
    return datetime.datetime.strptime(s.strip(), "%Y/%m/%d %H:%M:%S.%f").timestamp()


def smi(path: Path) -> dict:
    """nvidia-smi's 200 ms samples binned to BIN_S: mean draw (W), the power limit as written and the limit the card enforced at the
    bin's end (W), mean SM clock (MHz), mean temperature (C), mean utilisation (%), the time axis from the arm's first sample."""
    rows = []
    with path.open(encoding="utf-8") as f:
        for ln in f:
            c = [x.strip() for x in ln.split(",")]
            if len(c) < 8 or not c[0][:4].isdigit():
                continue
            try:
                rows.append((_stamp(c[0]), float(c[2]), float(c[3]), float(c[4]), float(c[7]), float(c[6]), float(c[5])))
            except ValueError:
                continue
    if not rows:
        return {}
    t0 = rows[0][0]
    bins: dict[int, list] = {}
    for t, draw, temp, util, lim, clk, plim in rows:
        bins.setdefault(int((t - t0) // BIN_S), []).append((draw, temp, util, lim, clk, plim))
    ks = sorted(bins)
    mean = lambda xs: round(sum(xs) / len(xs), 2)
    return {"t": [round(k * BIN_S, 1) for k in ks],
            "draw_w": [mean([r[0] for r in bins[k]]) for k in ks],
            "temp_c": [mean([r[1] for r in bins[k]]) for k in ks],
            "util": [mean([r[2] for r in bins[k]]) for k in ks],
            "enforced_w": [bins[k][-1][3] for k in ks],
            "limit_w": [bins[k][-1][5] for k in ks],
            "clock_mhz": [mean([r[4] for r in bins[k]]) for k in ks],
            "samples": len(rows)}


def requests(path: Path, offset: float) -> dict:
    """Requests in REQ_BIN_S windows on the arm's own axis: served, failed, the 95th-percentile and mean response (ms)."""
    bins: dict[int, list] = {}
    served = failed = 0
    with path.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                done = float(r["done_s"]) + offset
                lat = float(r["latency_ms"])
                ok = int(float(r.get("ok", "1")))
            except (KeyError, ValueError):
                continue
            bins.setdefault(int(done // REQ_BIN_S), []).append((lat, ok))
            served += ok
            failed += 1 - ok
    ks = sorted(bins)
    p95 = lambda xs: sorted(xs)[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]
    return {"t": [round((k + 1) * REQ_BIN_S, 1) for k in ks],
            "served": [sum(o for _, o in bins[k]) for k in ks],
            "p95_ms": [round(p95([l for l, o in bins[k] if o]) if any(o for _, o in bins[k]) else 0.0, 1) for k in ks],
            "mean_ms": [round(sum(l for l, o in bins[k] if o) / max(1, sum(o for _, o in bins[k])), 1) for k in ks],
            "served_total": served, "failed_total": failed}


def audit(path: Path, t_start: float) -> dict:
    """The governor's decisions from its own audit: the limit it wanted (W) and what decided it; every limit write (W) and every
    clock write (the SM clock range it locked, MHz), each on the arm's own axis."""
    out, writes, clocks, kinds, last = [], [], [], {}, None
    with path.open(encoding="utf-8") as f:
        for ln in f:
            try:
                d = json.loads(ln)
            except json.JSONDecodeError:
                continue
            t = round(float(d.get("time", 0)) - t_start, 1)
            for k in d:
                if k != "time":
                    kinds[k] = kinds.get(k, 0) + 1
            dec = (d.get("decision") or {}).get("0")
            if dec:
                want, by = dec.get("want_w"), dec.get("decided_by") or ""
                if want is not None and (last is None or want != last or len(out) % 10 == 0):
                    out.append([t, want, by])
                    last = want
            w = d.get("write")
            if isinstance(w, list) and "-pl" in w:
                try:
                    writes.append([t, float(w[w.index("-pl") + 1])])
                except (ValueError, IndexError):
                    pass
            cw = d.get("clock_write")
            if isinstance(cw, list) and "-lgc" in cw:
                try:
                    lo, hi = cw[cw.index("-lgc") + 1].split(",")
                    clocks.append([t, float(lo), float(hi)])
                except (ValueError, IndexError):
                    pass
    return {"decisions": out, "limit_writes": writes, "clock_writes": clocks, "records": kinds}


def total_table(md: str) -> list[dict]:
    rows, grab = [], False
    for ln in md.split("\n"):
        if ln.startswith("## Total"):
            grab = True
            continue
        if grab and ln.startswith("## "):
            break
        if grab and ln.startswith("|") and not ln.startswith("|---") and "Gauge" not in ln:
            c = [x.strip() for x in ln.strip("|").split("|")]
            if len(c) >= 6:
                aim = _aim(c[0])
                rows.append({"gauge": c[0].strip("* "), "primary": "(primary)" in c[0], "native": c[1], "omni": c[2], "change": c[3],
                             "interval": c[4], "verdict_as_printed": c[5], "aim": aim, "word": _word(aim, c[3], c[4]) if c[1] != "UNAVAILABLE" else "no meter"})
    return rows


HEADS = ("GAIN", "LOSS", "STEADY", "power given", "the runs disagree", "the runs differ", "shown, not judged")


def _head(reading: str) -> str:
    """A three-run reading's word alone, by the key's one reader (tools/readings.py word_of): GAIN, LOSS, STEADY, power given, the
    runs disagree or the runs differ; a row shown and not judged (one repetition in a run, no interval) is "shown, not judged"; any
    other reading keeps its own kind, never another word."""
    w = word_of(reading)
    if w:
        return w
    k = reading_kind(reading)
    return "shown, not judged" if "shown, not judged" in k or not k else k


def card_tables() -> list:
    """The newest engine's three-run card tables (results/gpu/V*_ABC.json, tools/gpu_abc.py and tools/hil_abc.py), each read
    from its own file: its title, engine, runs and every row's word counted; for the stacked box, the card's own primary
    measure counted size by size. Nothing typed: a table that is not on disk is not on the page."""
    def version(f):
        m = re.match(r"V(\d+)_", f.name)
        return int(m.group(1)) if m else -1
    found = sorted((ROOT / "results" / "gpu").glob("V*_ABC.json"), key=lambda f: (version(f), f.name))
    newest = [f for f in found if found and version(f) == version(found[-1])]
    out = []
    for f in newest:
        rec = json.loads(f.read_text(encoding="utf-8"))
        eng = rec.get("engine"); eng = " ".join(eng) if isinstance(eng, list) else (eng or "")
        m = re.search(r"(omni-v\d+)", eng); d = re.search(r"dial: (\w+)", eng)
        t = {"file": str(f.with_suffix(".md").relative_to(ROOT)), "title": rec.get("title", f.stem), "engine": m.group(1) if m else None,
             "dial": d.group(1) if d else None, "runs": rec.get("runs")}
        rows = rec.get("rows", {})
        if isinstance(rows, list):                  # the stacked box: the card's own meter, its primary measure, size by size
            sizes, reps, counts, by_part, flagged = {}, {}, {}, {}, []
            for r in rows:
                h = _head(r.get("reading", ""))
                counts[h] = counts.get(h, 0) + 1
                bp = by_part.setdefault(str(r.get("part")), {}); bp[h] = bp.get(h, 0) + 1
                if r.get("part") == "card" and r.get("measure") == "primary":
                    c = sizes.setdefault(str(r["copies"]), {}); c[h] = c.get(h, 0) + 1
                    k = str(r["copies"]); reps[k] = min([reps.get(k, 10 ** 9)] + list(r.get("repetitions") or []))
                if h in ("GAIN", "LOSS", "power given", "the runs disagree", "the runs differ"):
                    # every judged row that is not STEADY, named by its organism, size, part and measure, with each run's raw change in
                    # percent of native (None where native stood at zero), so a LOSS row is listed, never only counted
                    pcs = [None if not isinstance(x.get("native"), (int, float)) or not x.get("native") or not isinstance(x.get("diff"), (int, float))
                           else round(100 * x["diff"] / abs(x["native"]), 4) for x in (r.get("runs") or [])]
                    flagged.append({"organism": r.get("organism"), "copies": r.get("copies"), "part": r.get("part"), "measure": r.get("measure"),
                                    "w": h, "rd": r.get("reading", ""), "pct": pcs})
            t["kind"] = "stacks"; t["card_primary_by_copies"] = sizes; t["counts"] = counts; t["by_part"] = by_part; t["flagged"] = flagged
            t["reps_by_copies"] = {k: v for k, v in reps.items() if v < 10 ** 9}   # the fewest paired repetitions any run made at that size
        else:
            counts, by, judged = {}, {}, []
            for gauge, r in rows.items():
                h = _head(r.get("reading", "")); counts[h] = counts.get(h, 0) + 1; by.setdefault(h, []).append(gauge)
                # each row as its table writes it: its word, its reading and each run's raw change in percent of native (None where
                # native stood at zero), so a LOSS row is shown with its sizes and its engine, never only by name
                pcs = [None if not isinstance(x.get("native"), (int, float)) or not x.get("native") or not isinstance(x.get("diff"), (int, float))
                       else round(100 * x["diff"] / abs(x["native"]), 4) for x in (r.get("runs") or [])]
                judged.append({"g": gauge, "w": h, "rd": r.get("reading", ""), "pct": pcs})
            t["kind"] = "card"; t["counts"] = counts; t["gauges_by_word"] = by; t["rows"] = judged
        out.append(t)
    return out


def chip_ledger() -> dict:
    """Every chip run's state as docs/RUN_LEDGER.md section 1 records it (read from GitHub's own run records): for each GitHub run its
    row's "What", "Finished?", "What came back" and "Receipt" cells, and whether the run was measured to its end ("Yes" or "To its
    deadline"); a row that names a span of runs ("14 runs, 24 Oct 02:57 to 08:41") is kept as that span, matched on the page by each
    run's start. Nothing is decided here: the page prints the ledger's own words, with no person named."""
    f = ROOT / "docs" / "RUN_LEDGER.md"
    if not f.exists():
        return {"file": None, "runs": {}, "spans": []}
    lines, grab = f.read_text(encoding="utf-8").splitlines(), False
    runs, spans, head = {}, [], None
    clean = lambda c: re.sub(r"\*\*|`", "", c).strip()
    for ln in lines:
        if ln.startswith("## 1."):
            grab = True
            continue
        if grab and ln.startswith("## "):
            break
        if not grab or not ln.startswith("|") or ln.startswith("|---"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if head is None:
            head = cells
            continue
        row = dict(zip(head, cells))
        fin = clean(row.get("Finished?", "")).replace(" on the founder's decision", "")   # the ledger's words, nobody's name in them
        rec = {"what": clean(row.get("What", "")), "finished": fin, "came_back": clean(row.get("What came back", "")), "receipt": clean(row.get("Receipt", "")),
               "measured": bool(re.match(r"(Yes|To its deadline)\b", fin))}
        ids = re.findall(r"\b(\d{11})\b", row.get("GitHub run", ""))
        if ids:
            for i in ids:
                runs[i] = rec
        else:
            m = re.match(r"(\d+) runs, (\d+) (\w{3}) (\d\d:\d\d) to (\d\d:\d\d)", clean(row.get("GitHub run", "")))
            if m:
                mon = {"Oct": "10", "Nov": "11", "Sep": "09"}.get(m.group(3), "10")
                day = f"2026-{mon}-{int(m.group(2)):02d}"
                spans.append(rec | {"n": int(m.group(1)), "from": f"{day}T{m.group(4)}:00Z", "to": f"{day}T{m.group(5)}:59Z"})
    return {"file": str(f.relative_to(ROOT)), "runs": runs, "spans": spans}


def main(out: str) -> None:
    if not RUN.exists():
        Path(out).write_text(json.dumps({"missing": str(RUN.relative_to(ROOT))}), encoding="utf-8")
        return
    receipt = json.loads((RUN / "receipt.json").read_text(encoding="utf-8"))
    md = (RUN / "GPU_REPS.md").read_text(encoding="utf-8")
    reps = []
    for rd in sorted(RUN.glob("rep-*"), key=lambda p: int(p.name.split("-")[1])):
        rep = {"rep": int(rd.name.split("-")[1]), "arms": {}}
        for arm in ARMS:
            ad = rd / arm
            if not (ad / "smi.csv").exists():
                continue
            ws = float((ad / "window_start.txt").read_text().strip()) if (ad / "window_start.txt").exists() else None
            summ = json.loads((ad / "summary.json").read_text(encoding="utf-8")) if (ad / "summary.json").exists() else {}
            offset = (float(summ["t0_epoch"]) - ws) if ws is not None and "t0_epoch" in summ else 0.0
            a = {"smi": smi(ad / "smi.csv"), "req": requests(ad / "requests.csv", offset) if (ad / "requests.csv").exists() else {},
                 "limit_start_w": (ad / "limit_start.txt").read_text().strip() if (ad / "limit_start.txt").exists() else None,
                 "limit_end_w": (ad / "limit_end.txt").read_text().strip() if (ad / "limit_end.txt").exists() else None,
                 "served": summ.get("served"), "not_served": summ.get("not_served"), "duration_s": summ.get("duration_s")}
            if arm != "native" and (ad / "audit.jsonl").exists() and ws is not None:
                a["audit"] = audit(ad / "audit.jsonl", ws)
            rep["arms"][arm] = a
        reps.append(rep)
    ver = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", receipt.get("git") or ""],
                         capture_output=True, text=True, cwd=ROOT).stdout     # the engine its commit carries, by the version tool
    eng = re.search(r"(omni-v\d+) \(digest", ver)
    data = {"source": str(RUN.relative_to(ROOT)), "table": str((RUN / "GPU_REPS.md").relative_to(ROOT)),
            "card": receipt.get("gpu_name"), "driver": receipt.get("driver"), "engine_commit": receipt.get("git"), "engine": eng.group(1) if eng else None,
            "engine_note": ("omni-v18's card governor (commit e3b05dc, the branch gpu-omni-v18) at the factory tune, the max: on this "
                            "card native already runs both knobs at their top (the power limit 400 W of 400 W, the clock unlocked to "
                            "1,410 MHz), so in its 3,050 decisions the governor asked for exactly that and wrote nothing: at its limit "
                            "on native. Lambda workflow run 40079645681, 24 October"),
            "reps_n": receipt.get("reps"), "duration_s": receipt.get("duration_s"), "sample_ms": receipt.get("sample_ms"),
            "limit_default_w": receipt.get("power_limit_default_w"), "limit_min_w": receipt.get("power_limit_min_w"), "envelope": receipt.get("envelope"),
            "workload": receipt.get("workload"), "bin_s": BIN_S, "req_bin_s": REQ_BIN_S, "arms": list(ARMS),
            "arm_words": {"native": "the card as shipped, its own driver governing", "watch": "Omni-Compass wired, watching only (the switch OFF: it reads, writes nothing)",
                          "omni": "Omni-Compass governing the power limit"},
            "total": total_table(md), "reps": reps, "tables": card_tables(), "chip_ledger": chip_ledger()}
    Path(out).write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "gpu_run.json")
