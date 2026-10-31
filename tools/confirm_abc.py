# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C three-run table (docs/OMNI_V1.md): one v1 benchmark run three times as separate GitHub runs on the same
frozen engine, A the result, B and C the replications. Every judged row gets one of three readings, all three runs shown:
GAIN or LOSS in all three of our runs (judged by what the gauge is for, never by the sign of its number; a resource spent
that rose reads power given, never a loss: tools/readings.py, the founder's order of 13 October) when all three runs move
the same way and each run's 95% interval of the paired difference (omni minus native) is clear of zero; STEADY, no
difference beyond the noise, when a run's interval includes zero (native and omni could not be told apart on that measure,
which is itself the result, with the count of such runs); the runs disagree when runs clear of the noise point different
ways (the test itself is then unstable, and is looked into).
Rows that are shown but never judged (tools/live_reps.py NEUTRAL) stay unjudged. Every row is reported, losses included.
Usage: python tools/confirm_abc.py "TITLE" A_DIR B_DIR C_DIR --out results/live/V1_<NAME>.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding live-reps/LIVE_REPS.json, or one native setup's folder
  inside an add-on run (results/live/raw/addons-run-<id>/<setup>/); its engine is checked."""
from __future__ import annotations

import argparse, json, re, subprocess, sys
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.readings import OWN_RUNS, receipt_key, in_all_three, word, aim, EVEN_SAME, even_noise, SHOWN, three_run_reading, run_word, LOWER as AIMS_LOWER, HIGHER as AIMS_HIGHER  # noqa: E402
from tools.repo import NAME as REPO_NAME  # noqa: E402  (the repository's name, written once)
from tools.live_reps import KEYS, LABEL, NEUTRAL, SAME_REL
from tools.readings import by_word, interval_by_word, word_sign, reading_kind

ARMS = ("compass", "bowl")        # the Omni arm's name in the run files (bench-bowl-N folders predate the rename)
# --pair: one comparison of the four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6), "first|second" as
# tools/live_reps.py keys it, each cell the first against the second; unset, the Omni arm against native
PAIR = None
PAIR_WORDS = {"nativebare": "the organism alone", "compassbare": "Omni-Compass on the organism alone",
              "native": "the orchestrator as shipped", "compass": "Omni-Compass on top of the orchestrator",
              # the decision pace, the heartbeat dial (docs/PACE_PREREGISTRATION.md): compass5|compass, compass5 (against
              # native) and so on; the compass arm decides at its engine's default (every 60 s from omni-v17, every 15 s on
              # omni-v16), its beat read from the runs' own receipts (BEATS)
              **{f"compass{p}": f"Omni-Compass deciding every {p} s" for p in (5, 10, 15, 30, 60, 75, 90, 120)}}
BEATS = {}   # run id -> {arm: [the beats it ran at]}, from each run's LIVE_REPS.json (tools/live_reps.py, omni-v17 on)
CAPACITY = "work inside the response line (requests a second; the capacity test's own gauge)"
from tools.omni_index import CAPACITY as CAPACITY_RECORDED  # noqa: E402  (the same row's name in the tables written before 13 October)
AIM_HIGHER = {CAPACITY, CAPACITY_RECORDED}


def robust_rows(runs):
    """The robustness test's own rows (docs/ROBUSTNESS_PREREGISTRATION.md), from each run's `robust` block (omni arm only, so
    not paired): every setting back within the allowance in every repetition, the seconds it took, the second governor, the
    governor's memory. Returns table lines and the rows as data; empty when no run carries the block."""
    blocks = []
    for _, _, _, rb in runs:
        arm = next((a for a in ARMS if rb and a in rb), None)
        blocks.append(rb[arm] if arm else None)
    if any(b is None for b in blocks):
        return [], {}
    L, rows = [], {}
    kill = all(b.get("kill_repetitions") for b in blocks)
    if kill:
        ok = all(b.get("handed_back_within_allowance_all") for b in blocks)
        v = "**handed back within the allowance in every repetition, in all three of our runs**" if ok else "**LOSS: not handed back within the allowance in a repetition**"
        cells = [f"{'yes' if b['handed_back_within_allowance_all'] else 'NO'} ({b['kill_repetitions']} reps; mean {b['handed_back_s_mean']:.0f} s, max {b['handed_back_s_max']:.0f} s"
                 + (f", never: {b['never_handed_back']}" if b.get('never_handed_back') else "") + ")" if b['handed_back_s_mean'] is not None else f"NO (never handed back in {b['never_handed_back']} reps)" for b in blocks]
        k = f"robust: every setting back at the operator's within {blocks[0]['allowance_s']:.0f} s of the kill, every repetition (the governor killed outright; the watchdog's hand-back)"
        L.append(f"| {k} | {cells[0]} | {cells[1]} | {cells[2]} | {v} |"); rows[k] = {"reading": v.strip("*"), "runs": blocks}
        sg = all(b.get("second_governor_all") for b in blocks)
        v2 = "**the same in all three of our runs**" if sg else "**LOSS: no second governor in a repetition**"
        k2 = "robust: a second governor started after the hand-back and governed to the end, every repetition"
        L.append(f"| {k2} | {'yes' if blocks[0]['second_governor_all'] else 'NO'} | {'yes' if blocks[1]['second_governor_all'] else 'NO'} | {'yes' if blocks[2]['second_governor_all'] else 'NO'} | {v2} |")
        rows[k2] = {"reading": v2.strip("*"), "runs": [b.get("second_governor_all") for b in blocks]}
    if all(b.get("memory_ratio_max") is not None for b in blocks):
        lim = blocks[0]["memory_limit"]
        leak = any(b["memory_ratio_max"] > lim for b in blocks)
        v3 = "**LOSS: over the preregistered memory limit (a leak)**" if leak else f"no leak (every repetition under {lim})"
        k3 = "robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions"
        L.append(f"| {k3} | {blocks[0]['memory_ratio_max']:.3f} | {blocks[1]['memory_ratio_max']:.3f} | {blocks[2]['memory_ratio_max']:.3f} | {v3} |")
        rows[k3] = {"reading": v3.strip("*"), "runs": [b["memory_ratio_max"] for b in blocks]}
    if all(b.get("decisions_share_min") is not None for b in blocks):
        # the long run's own rows (docs/ROBUSTNESS_PREREGISTRATION.md, scenario 2): decisions made of expected, failed decisions,
        # the decision time's growth, the hand-back at the end
        lim = blocks[0]["decision_share_limit"]
        bad = any(b["decisions_share_min"] < lim for b in blocks)
        v4 = f"**INVALID: a repetition made fewer decisions than {lim:.0%} of the expected**" if bad else f"valid (every repetition at {lim:.0%} of the expected or more)"
        k4 = f"robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window ({blocks[0]['decisions_expected']:.0f})"
        L.append(f"| {k4} | {blocks[0]['decisions_share_min']:.1%} | {blocks[1]['decisions_share_min']:.1%} | {blocks[2]['decisions_share_min']:.1%} | {v4} |")
        rows[k4] = {"reading": v4.strip("*"), "runs": [b["decisions_share_min"] for b in blocks]}
        fails = [b.get("failed_decisions_total", 0) for b in blocks]
        reasons = sorted({r for b in blocks for r in (b.get("failed_reasons") or [])})
        # preregistered as shown, not judged: a failed decision is a decision the governor could not make (the cluster API did not
        # answer), held through and resumed; each is shown with its reason, here and in the run's live report
        v5 = ("shown, not judged: " + ("; ".join(reasons) if reasons else "no reason recorded") + "; the governor held and resumed") if any(fails) else "none in any repetition"
        k5 = "robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason"
        L.append(f"| {k5} | {fails[0]} | {fails[1]} | {fails[2]} | {v5} |")
        rows[k5] = {"reading": v5, "runs": fails}
        if all(b.get("decision_time_ratio_max") is not None for b in blocks):
            g = blocks[0]["cycle_growth_limit"]
            grew = any(b["decision_time_ratio_max"] > g for b in blocks)
            v6 = "**LOSS: the decision time grew by more than half**" if grew else f"no growth beyond the limit (every repetition under {g})"
            k6 = "robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions"
            L.append(f"| {k6} | {blocks[0]['decision_time_ratio_max']:.2f} | {blocks[1]['decision_time_ratio_max']:.2f} | {blocks[2]['decision_time_ratio_max']:.2f} | {v6} |")
            rows[k6] = {"reading": v6.strip("*"), "runs": [b["decision_time_ratio_max"] for b in blocks]}
        if all(b.get("handed_back_end_all") is not None for b in blocks):
            ok = all(b["handed_back_end_all"] for b in blocks)
            v7 = "**every setting handed back at the end of every repetition, in all three of our runs**" if ok else "**LOSS: a repetition not handed back at the end**"
            k7 = "robust: every setting handed back at the end and read back at the operator's, no record left, every repetition"
            L.append(f"| {k7} | {'yes' if blocks[0]['handed_back_end_all'] else 'NO'} | {'yes' if blocks[1]['handed_back_end_all'] else 'NO'} | {'yes' if blocks[2]['handed_back_end_all'] else 'NO'} | {v7} |")
            rows[k7] = {"reading": v7.strip("*"), "runs": [b["handed_back_end_all"] for b in blocks]}
    return L, rows


def load(d):
    """(run id, the paired table of the Omni arm against native, repetitions) from an archived run folder."""
    f = next(Path(d).rglob("LIVE_REPS.json"), None)
    if f is None:
        raise SystemExit(f"{d}: no LIVE_REPS.json")
    j = json.loads(f.read_text())
    arm = PAIR if PAIR else next((a for a in ARMS if a in j["paired"]), None)
    if arm is None or arm not in j["paired"]:
        raise SystemExit(f"{f}: no {PAIR or 'compass'} comparison in the paired table ({sorted(j['paired'])})")
    # the run id from the run's own folder: run-<id>, or addons-run-<id> with one folder per native setup inside it
    run = next((q.name.rsplit("run-", 1)[1] for q in [Path(d).resolve(), *Path(d).resolve().parents]
                if q.name.rsplit("run-", 1)[-1].isdigit() and "run-" in q.name), Path(d).resolve().name.replace("run-", ""))
    reps = j.get("repetitions") or {}
    first, second = arm.split("|") if "|" in arm else (arm, "native")
    n = len(set(reps.get(second, [])) & set(reps.get(first, []))) if isinstance(reps, dict) else reps
    paired = dict(j["paired"][arm])
    BEATS[run] = j.get("beats") or {}
    cap = j.get("capacity")                                # the capacity test (a rising load): its own block in the run file
    if cap and arm in cap and "capacity_rps" in cap.get("native", {}):
        nat, om = cap["native"]["capacity_rps"], cap[arm]["capacity_rps"]
        paired[CAPACITY] = {"native": nat, "omni": om, "diff": om - nat, "ci95": list(cap[arm]["ci95"]),
                            "significant": cap[arm]["ci95"][0] > 0 or cap[arm]["ci95"][1] < 0}
    return run, paired, n, j.get("robust")


def raw_pct(x, digits=1):
    """A raw change with its true sign: + for a rise, − for a fall, whatever the gauge is for (the referee's work order of
    25 October: a raw change is never turned to wear the verdict's sign)."""
    v = round(x, digits)   # the sign of the number as printed: a change that rounds to zero prints ±0.0, never −0.0
    return f"{'+' if v > 0 else '−' if v < 0 else '±'}{abs(x):.{digits}f}"


def num(x):
    """A measured value as it stands, four significant figures."""
    return f"{x:.4g}"


def cell(r, word=None):
    """One run, in separate fields: native's value → Omni-Compass's, the raw change (Omni − native) / native with its true sign
    and its 95% interval, and the run's own word. A native under one unit or at zero is shown with the change in the gauge's own
    unit beside the percent, because a percent of a near-zero base reads as nothing."""
    nat, omni, diff, lo, hi = r["native"], r.get("omni"), r["diff"], r["ci95"][0], r["ci95"][1]
    if omni is None:
        omni = nat + diff
    w = f"; {word}" if word else ""
    none = not all(isinstance(x, (int, float)) and x == x for x in (lo, hi))      # one pair: no interval
    if nat:
        iv = "no interval, one pair" if none else f"{raw_pct(100 * lo / abs(nat))}% to {raw_pct(100 * hi / abs(nat))}%"
        unit = f", {raw_pct(diff, 4)} in the gauge's unit" if abs(nat) < 1 else ""
        return f"{num(nat)} → {num(omni)}; raw {raw_pct(100 * diff / abs(nat))}% (95%: {iv}){unit}{w}"
    iv = "no interval, one pair" if none else f"{raw_pct(lo, 4)} to {raw_pct(hi, 4)}"
    return f"{num(nat)} → {num(omni)}; raw {raw_pct(diff, 4)} in the gauge's unit (95%: {iv}){w}"


def aim_of_row(k):
    """What the row's gauge is for: work aims higher; time waited, missed or failed aims lower; a resource spent or held is
    spent (tools/readings.py)."""
    return aim(AIMS_HIGHER if k in AIM_HIGHER else AIMS_LOWER, k)


def verdict(k, rs):
    """The row's reading over the three runs, by rule: GAIN, LOSS or power given in all three of our runs (by what the gauge
    is for), STEADY (no difference the test can measure, or the same), or a disagreement between runs. Every judged row gets
    exactly one."""
    if k in NEUTRAL:
        return SHOWN
    if all(abs(r["diff"]) <= SAME_REL * abs(r["native"]) for r in rs):
        return EVEN_SAME
    signs = [(r["diff"] > 0) - (r["diff"] < 0) for r in rs]
    # a run of one pair has no interval (the 24-hour robustness run: one pair a rented machine): three such runs are read by
    # their signs alone and said to be single pairs, never read as the same in all three of our runs
    single = [any(isinstance(x, float) and x != x for x in r["ci95"]) for r in rs]
    if all(single):
        if len(set(signs)) > 1:
            return "single pairs point different ways (one pair a run, no interval)"
        return f"three single pairs agree: {word(signs[0] == -1, aim_of_row(k))} (one pair a run, no interval, so the noise cannot be judged)"
    return three_run_reading(rs, aim_of_row(k), SAME_REL)


def rig(d):
    """The rig a run ran on, from its arms' preflight records: on kind, the served image pulled onto every worker before each
    arm (amendment of 18 October, docs/POD_START_WAIT.md), or pulled by each node at each start (the rig before it, and every
    cloud machine). Three runs on two rigs are never one table."""
    seen = set()
    for p in Path(d).rglob("preflight.txt"):
        lines = p.read_text(errors="replace").splitlines()
        img = next((ln.split("=", 1)[1] for ln in lines if ln.startswith("images=")), "pulled by each node at each start")
        # the batch rig's cores (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 5): the governor on its own core, or not
        core = "; the governor on its own core" if any(ln.startswith("cores: ") and "governor alone" in ln for ln in lines) else ""
        seen.add(img + core)
    return " / ".join(sorted(seen)) if seen else "not recorded"


def engine(run):
    """The Omni version the run's commit carries (tools/omni_version.py), from the GitHub run record."""
    try:
        sha = subprocess.run(["gh", "api", f"repos/{REPO_NAME}/actions/runs/{run}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            return "?", "unknown"                          # a run whose commit cannot be read is never called v1
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=120).stdout.strip().splitlines()
        return sha[:12], (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "?", "unknown"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title"); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--out", required=True)
    ap.add_argument("--pair", default=None, help="one comparison of the four ways, first|second (tools/live_reps.py)")
    a = ap.parse_args(argv)
    global PAIR
    PAIR = a.pair
    BEATS.clear()
    runs = [load(d) for d in (a.a, a.b, a.c)]
    title = re.sub(r":\s*the A/B/C (?:confirmation|three-run table) \(Omni v\d\)\s*$", "", a.title)   # never twice
    L = [f"# {title}: the A/B/C three-run table (Omni v1)", "", *receipt_key(), "",
         "Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C "
         "are the replications. Each cell is omni against native, the paired change in percent of native with its 95% "
         "interval. Every judged row gets one of three readings. **GAIN** or **LOSS in all three of our runs**: all three "
         "runs move the same way and every interval is clear of zero, and the word says what that means for the gauge's "
         "declared aim, never the sign of its number (a response time that fell is GAIN; a resource spent that fell is a cut, "
         "a GAIN, and one that rose is **power given**, never a loss: the key, `docs/HOW_TO_READ_THE_RESULTS.md`). **STEADY, no "
         "difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told "
         "apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so "
         "the test itself is unstable there. Every row is shown, LOSS included.", "", OWN_RUNS, ""]
    if PAIR and "|" in PAIR:                               # one comparison of the four ways: the cells name its two arms
        first, second = PAIR.split("|")
        pace = first.startswith("compass") and first[7:].isdigit()
        src = ("the decision pace, `docs/PACE_PREREGISTRATION.md`" if pace
               else "the four ways, `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6")
        own = {b for r in BEATS.values() for b in r.get("compass", [])}
        default = (f"Omni-Compass at its default, deciding every {next(iter(own)):g} s" if len(own) == 1 else
                   "Omni-Compass at its engine's default beat (every 60 s from omni-v17, every 15 s on omni-v16)")
        words2 = default if pace and second == "compass" else PAIR_WORDS.get(second, second)
        L += [f"**The comparison.** In this table \"omni\" stands for {PAIR_WORDS.get(first, first)} and \"native\" for "
              f"{words2}: each cell is the first against the second, paired within one repetition "
              f"({src}), and each word is read by the gauge's aim for the first.", ""]
    L += ["| Run | GitHub run | Commit | Engine | Paired repetitions |", "|---|---|---|---|---:|"]
    off, meta = [], []
    for tag, (run, _, n, _) in zip("ABC", runs):
        sha, ver = engine(run)
        if not ver.startswith("omni-v"):                     # a fingerprinted engine (docs/OMNI_V2.md; v1 runs keep reading as v1)
            off.append(f"{tag} (run {run}: {ver})")
        meta.append({"tag": tag, "run": run, "commit": sha, "engine": ver, "paired_repetitions": n})
        L.append(f"| {tag} | {run} | `{sha}` | {ver} | {n if n is not None else '?'} |")
    # the title names the engine the three runs carry (one engine, or it says they differ): never read across versions
    seen = [m["engine"].split(" ")[0] for m in meta]
    label = f"Omni {seen[0][5:]}" if len(set(seen)) == 1 and seen[0].startswith("omni-v") else "the runs' engines differ"
    L[0] = L[0].replace("(Omni v1)", f"({label})")
    if len({r for r, _, _, _ in runs}) < 3:
        off.append("A, B and C must be three separate runs")
    if len({m["engine"].split(" ")[0] for m in meta}) > 1:
        off.append("A, B and C are not all on the same engine: " + ", ".join(m["engine"].split(" ")[0] for m in meta))
    for m, d in zip(meta, (a.a, a.b, a.c)):
        m["rig"] = rig(d)
    if len({m["rig"] for m in meta}) > 1:
        off.append("A, B and C are not all on the same rig: " + "; ".join(f"{m['tag']} {m['rig']}" for m in meta))
    if off:
        L[2:2] = [f"**Not three runs of one engine on one rig: {'; '.join(off)}.** The readings below compare runs that differ.", ""]
    L += ["", "| Measure | A | B | C | Reading |", "|---|---|---|---|---|"]
    tally, rows = {}, {}
    for k in [CAPACITY] + KEYS:
        rs = [p.get(k) for _, p, _, _ in runs]
        if any(r is None for r in rs):
            continue
        v = verdict(k, rs)
        tally[reading_kind(v)] = tally.get(reading_kind(v), 0) + 1
        rows[k] = {"reading": v.strip("*"), "aim": aim_of_row(k) if k not in NEUTRAL else None,
                   "runs": [{"native": r["native"], "omni": r["omni"], "diff": r["diff"], "ci95": list(r["ci95"])} for r in rs]}
        a_ = aim_of_row(k) if k not in NEUTRAL else None
        L.append(f"| {LABEL.get(k, k)} | " + " | ".join(cell(r, run_word(r, a_)) for r in rs) + f" | {v} |")
    rob_l, rob_rows = robust_rows(runs)           # the robustness test's own rows (omni only, by rule, not paired)
    for line in rob_l:
        v = line.rsplit("|", 2)[-2].strip(); tally[v] = tally.get(v, 0) + 1
    L += rob_l; rows.update(rob_rows)
    L += ["", "Readings: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())) + "."]
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(_legal_stamp(L)) + "\n")
    # the same table as data, for the Omni index (tools/omni_index.py): every run's values and the reading, by rule
    out.with_suffix(".json").write_text(json.dumps({"title": a.title, "v1": not off, "runs": meta, "rows": rows}, indent=1) + "\n")
    print(f"{out}: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
