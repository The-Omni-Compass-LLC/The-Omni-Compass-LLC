# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words every table uses: GAIN, STEADY and LOSS (the founder's order of 13 October 2026, night).

Better, same and worse became GAIN, STEADY and LOSS wherever they lived, and where they used to live. A reading is never
decided by the plus or minus sign of its number: it is decided by what the gauge is for, its declared aim. A response time
that fell is a GAIN; work that fell is a LOSS; a bill, an energy draw or a count of machines that fell is a cut, and a cut
is a GAIN; a resource that rose to buy work or speed is power given (the founder's order of 12 October), shown beside what
it bought and never called a loss. KEY says what each word means, letter by letter, and why it was chosen; it stands at
the front of the manual, in the README, in docs/HOW_TO_READ_THE_RESULTS.md and in the summary anyone prints after pulling
the repository (python3 tools/summary.py). This module is the one place the words are written.

Nobody outside The Omni-Compass LLC has checked or approved these results, so no table says "confirmed": a reading that
holds the same way in runs A, B and C, with every 95% interval clear of zero, says "in all three of our runs", and every
table carries OWN_RUNS. classify() reads a reading in any words the repository has used (GAIN/STEADY/LOSS; lower and higher
of 13 October; toward and away; better, worse and "confirmed" of the older tables) so every scorer reads every table alike.

  python3 tools/readings.py --key      the key, as plain text
  python3 tools/readings.py --check    exit 1 if a page that must carry the key does not carry it word for word
  python3 tools/readings.py --fix      write the key into those pages, and "How to read this receipt" into every standing table
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GAIN, STEADY, LOSS = "GAIN", "STEADY", "LOSS"
EVEN = STEADY       # the word before 25 October ("I like even to become steady", the founder's words): kept as a name for the
                    # engine files that import it until the next engine version, and read wherever an older record says it
OLD_EVEN = "EVEN"   # what an engine file locked by its fingerprint still writes (omnicompass/verdict.py); read as STEADY
GIVEN = "power given"                       # a resource spent or held rose: shown beside what it bought, never a LOSS
DISAGREE = "the runs disagree"              # runs clear of the noise point different ways: the test is unstable there
DIFFER = "**the runs differ**"              # a deterministic simulator's runs did not reproduce
SHOWN = "shown, not judged"                 # declared in advance as shown only
IN_ALL_THREE = "in all three of our runs"
SAME_IN_ALL_THREE = "the same in all three of our runs"
OWN_RUNS = ("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. "
            "Preregistered means the rules were written down in our own repository before the runs; nothing was filed "
            "with any outside body.")

# ------------------------------------------------------------------------------------------------- what a gauge is for
# A gauge's declared aim, as each preregistration writes it:
LOWER = "lower"              # an amount waited, missed or failed (a response time, time over the line): a fall is GAIN, a rise LOSS
HIGHER = "higher"            # work done (work inside the line, throughput, a hit rate): a rise is GAIN, a fall LOSS
SPENT = "spent"              # a resource spent or held (energy, power and its peaks, machines, memory, processor time, a bill, wear): a fall is a
                             # cut, and a cut is GAIN; a rise is power given
NEVER_MORE = "never more"    # a count that must never rise (failed requests, lost messages): any rise in any run is LOSS
NEVER_LESS = "never less"    # a count that must never fall
SHOWN_AIM = "shown"          # shown, never judged
WORK_PER = "work per resource"   # work bought with each unit of a resource (work per energy): a rise is a cut in what each unit
                                 # of work took, a GAIN; a fall is power given (17 October: it falls when more power is given)

# The gauges of a resource spent or held, by the names the tables and the runners give them. A table written before this
# module knew the word "spent" declared them "lower"; aim() reads them as spent wherever they are named.
SPENT_GAUGES = frozenset({
    # Kubernetes (tools/live_reps.py, pilot/bench_report.py)
    "worker nodes in service, mean", "node-hours", "power (W), mean", "power (W), peak", "energy (Wh)",
    "energy, parked workers still on at idle power (Wh)", "energy, the machine's own meter (Wh)", "node-hours per core-hour",
    "HPA replicas, mean", "pods started", "batch: worker machines in service after the queue finished, mean",
    "machines billed, machine-hours", "compute bill at list price ($)",
    # the organisms with the cluster inside (tools/six_kube_report.py)
    "organism energy (J)",
    # the stacks (tools/run_*.py)
    "servers_alive_mean", "servers_alive_max", "consumers_mean", "consumers_max", "maxmemory_mb_mean", "used_mb_mean",
    "cache_mb_mean", "cache_used_mb_mean", "pool_mb_mean", "pool_used_mb_mean", "cpu_busy_share", "cpu_seconds",
    "cpu_s_per_1k_inside", "energy_j", "power_w_mean", "j_per_1k_inside", "wall_j",
    # the independent simulators (pandapower, MuJoCo, the swarms, CityLearn)
    "load_energy_mwh", "losses_mwh", "energy_in_mwh", "tap_operations", "copper_j", "mechanical_j", "standing_j",
    "peak_torque_nm", "mean_abs_torque_nm", "energy_per_mission_j", "fleet_energy_j", "cost_total",
    "electricity_consumption_total", "carbon_emissions_total", "zero_net_energy",
    # CityLearn's peaks, swings and unevenness are the power the district holds from the grid and the wear of moving it, as a
    # Kubernetes cluster's peak power is above (the founder's order of 17 October: one key for every gauge)
    "all_time_peak_average", "daily_peak_average", "ramping_average", "monthly_one_minus_load_factor_average",
    "daily_one_minus_load_factor_average",
    # the Omni index's own measures
    "machines", "energy",
})


def aim(direction, key=None):
    """A gauge's aim from its declared direction: LOWER, HIGHER, SPENT, NEVER_MORE, NEVER_LESS, or None (shown only). A
    gauge declared "lower" whose name is a resource spent or held (SPENT_GAUGES) is SPENT."""
    if direction in (None, SHOWN_AIM, "shown, not judged"):
        return None
    if direction == LOWER and key in SPENT_GAUGES:
        return SPENT
    return direction


aim_of = aim


def word(fell: bool, aim_: str) -> str:
    """The word for a number that went the same way in all three runs (fell, or rose), judged by the gauge's aim, never by
    its sign: GAIN, LOSS, or power given."""
    if aim_ in (HIGHER, NEVER_LESS):
        return LOSS if fell else GAIN
    if aim_ == SPENT:
        return GAIN if fell else GIVEN
    if aim_ == WORK_PER:
        return GIVEN if fell else GAIN
    return GAIN if fell else LOSS                     # lower, never more


SIZE_FLOOR = 0.005           # the founder's floor of 20 October 2026 (and 24 October): a mean change under half of one percent either way reads STEADY
EVEN_FLOOR = f"{STEADY}, under the floor"              # held the same way in all three runs, every run's change under SIZE_FLOOR
SIGN_OF = {GAIN: "+", LOSS: "−", STEADY: "="}          # kept for readers of tables written before 25 October; no number is printed with it now


MEAN_OF_THREE = "by the mean of our three runs"   # the founder's order of 24 October 2026: a change of 0.5% or more is a change
EXACT_REL = 1e-9             # "the same" only where every run's two values agree to nine decimal places of the value: the referee's work
                             # order of 25 October (exact equality at 9 to 10 decimals); a smaller change is STEADY, under the floor, never "the same"


def significant(r) -> bool:
    """A run's paired change stands beyond the noise: its 95% interval clear of zero (or the run's own flag, where it gives one)."""
    if "significant" in r:
        return bool(r["significant"])
    lo, hi = (r.get("ci95") or [float("nan"), float("nan")])[:2]
    return lo > 0 or hi < 0


def three_run_reading(rs, aim_, same_rel=EXACT_REL):
    """The reading of one gauge over three runs, by the founder's order of 24 October 2026: any change of 0.5% or more is a
    GAIN, a LOSS or power given by the gauge's aim; STEADY only under 0.5%. rs: the three runs' paired results, each with
    "native" and "diff" and its 95% interval ("ci95") or a "significant" flag. The change is the mean of the runs' changes in
    percent of native. Every run the same way and clear of zero reads "in all three of our runs"; otherwise "by the mean of
    our three runs", with the count of runs beyond the noise. Runs that moved 0.5% or more in opposite directions disagree.
    A gauge whose native stands at zero in a run is read by its signs: any change is a change. "The same" is held to EXACT_REL
    whatever a caller passes (a runner's older one part in a million is tightened, never loosened)."""
    if any(r is None for r in rs):
        return "no value"
    if aim_ is None:
        return SHOWN
    if aim_ == NEVER_MORE:
        if any(r["diff"] > 0 for r in rs):
            return f"**{NEVER_MORE_UP}**"
        return EVEN_SAME if all(abs(r["diff"]) <= 1e-12 for r in rs) else f"**{NEVER_MORE_HELD}**"
    if exactly_same(rs, same_rel):
        return EVEN_SAME
    sig = [significant(r) for r in rs]
    signs = [int(r["diff"] > 0) - int(r["diff"] < 0) for r in rs]
    if all(r["native"] for r in rs):
        rel = [r["diff"] / abs(r["native"]) for r in rs]
        mean = sum(rel) / len(rel)
        moving = {s for s, x in zip(signs, rel) if abs(x) >= SIZE_FLOOR}
        if len(moving) > 1:
            return f"**{DISAGREE}**"
        if abs(mean) < SIZE_FLOOR:
            return f"{EVEN_FLOOR} (the three runs' mean {100 * abs(mean):.2f}%)"
        fell = mean < 0
    else:
        moving = {s for s in signs if s}
        if len(moving) > 1:
            return f"**{DISAGREE}**"
        fell = sum(r["diff"] for r in rs) < 0
    if all(sig) and len(set(signs)) == 1:
        return f"**{word(fell, aim_)} {IN_ALL_THREE}**"
    return f"**{word(fell, aim_)} {MEAN_OF_THREE}, beyond the noise in {sum(sig)} of {len(rs)}**"


def exactly_same(rs, same_rel=EXACT_REL) -> bool:
    """Every run's two values agree to EXACT_REL of the value (or to 1e-12 where native stands at zero): "STEADY, the same"."""
    tol = min(same_rel, EXACT_REL)
    return all(abs(r["diff"]) <= tol * max(abs(r["native"]), 1e-12) for r in rs)


STRONG, MODERATE, WEAK, INCONCLUSIVE = "strong", "moderate", "weak", "inconclusive"
EXACT, UNDER_FLOOR, NO_DIFF = "exactly the same", "under the floor", "no difference beyond the noise"
UNRESOLVED = "unresolved"
EVIDENCE_RULE = ("Evidence strength is shown beside the word and never changes it: strong, every run the mean's way and beyond "
                 "its noise (its 95% interval clear of zero); moderate, all but one; weak, one run beyond its noise; inconclusive, "
                 "no run beyond its noise (a mean of 0.5% or more, not a change any one run could tell from its noise). STEADY is "
                 "of three kinds: exactly the same (every run's values equal to nine decimal places), under the floor (a measured "
                 "change, the three runs' mean under 0.5%) and no difference beyond the noise (a table read by an older key). The "
                 "runs disagree is unresolved, never a final word: opposite directions each beyond its noise, or opposite "
                 "directions inside overlapping noise.")


def evidence(rs, aim_):
    """The evidence behind one gauge's reading over its runs, apart from the word (the referee's work order of 25 October, items 5
    to 7): the mean change in percent of native (None where a native stands at zero), each run's raw change in percent, how
    many runs point the mean's way, how many stand beyond their noise (and of those how many the mean's way), whether the runs
    agree, the strength (strong, moderate, weak, inconclusive), the kind of a STEADY (exactly the same, under the floor) and the
    cause of a disagreement. Where the runs carry a mean of three or more, the interval of the runs' mean by Student t with n − 1
    degrees of freedom (the runs as replicates; omnicompass/student_t.py). rs as three_run_reading reads them."""
    out = {"runs": len(rs), "mean_pct": None, "run_pct": [], "with_mean": 0, "clear": 0, "clear_with_mean": 0,
           "agree": True, "strength": None, "steady": None, "disagree": None, "mean_ci95_pct": None}
    if not rs or any(r is None for r in rs) or aim_ is None:
        return out
    sig = [significant(r) for r in rs]
    signs = [(r["diff"] > 0) - (r["diff"] < 0) for r in rs]
    rel = [r["diff"] / abs(r["native"]) if r["native"] else None for r in rs]
    out["run_pct"] = [None if x is None else 100 * x for x in rel]
    out["clear"] = sum(sig)
    if all(x is not None for x in rel):
        mean = sum(rel) / len(rel)
        out["mean_pct"] = 100 * mean
        if len(rel) >= 3:
            from omnicompass.student_t import t95
            sd = (sum((x - mean) ** 2 for x in rel) / (len(rel) - 1)) ** 0.5
            half = t95(len(rel) - 1) * sd / len(rel) ** 0.5
            out["mean_ci95_pct"] = [100 * (mean - half), 100 * (mean + half)]
        way = (mean > 0) - (mean < 0)
        moving = {s for s, x in zip(signs, rel) if abs(x) >= SIZE_FLOOR}
    else:
        tot = sum(r["diff"] for r in rs)
        way = (tot > 0) - (tot < 0)
        moving = {s for s in signs if s}
    out["with_mean"] = sum(1 for s in signs if s == way and way)
    out["clear_with_mean"] = sum(1 for s, g in zip(signs, sig) if g and s == way and way)
    if aim_ == NEVER_MORE:
        out["strength"] = STRONG if any(r["diff"] > 0 for r in rs) else None
        return out
    if exactly_same(rs):
        out["steady"] = EXACT
        return out
    if len(moving) > 1:
        out["agree"] = False
        opp = [g for s, g, x in zip(signs, sig, rel) if s and (x is None or abs(x) >= SIZE_FLOOR)]
        both = {s for s, g, x in zip(signs, sig, rel) if g and s and (x is None or abs(x) >= SIZE_FLOOR)}
        out["strength"] = UNRESOLVED
        out["disagree"] = ("opposite directions, each beyond its noise" if len(both) > 1
                           else "opposite directions inside overlapping noise")
        return out
    if out["mean_pct"] is not None and abs(out["mean_pct"]) < 100 * SIZE_FLOOR:
        out["steady"] = UNDER_FLOOR
        return out
    n, k = len(rs), out["clear_with_mean"]
    if k == n and out["with_mean"] == n:
        out["strength"] = STRONG
    elif k == 0:
        out["strength"] = INCONCLUSIVE
    elif k == n - 1:
        out["strength"] = MODERATE
    else:
        out["strength"] = WEAK
    return out


def relative_runs_reading(runs, aim):
    """The three-run reading of runs that carry their change relative to native ("change", with its 95% interval "lo" and "hi",
    both fractions of native), as the live page's exporters write them (docs/engine/export_scenarios.py,
    export_controller_trace.py): the one rule above, its words without the tables' bold. aim: up, down, spent, per or shown."""
    if aim == "shown":
        return SHOWN
    if not runs:
        return STEADY
    aim_ = {"up": HIGHER, "down": LOWER, "spent": SPENT, "per": WORK_PER}[aim]
    rs = [{"native": 1.0, "diff": float(r["change"]), "ci95": [float(r["lo"]), float(r["hi"])]} for r in runs]
    return three_run_reading(rs, aim_).replace("**", "")


def reproduced_reading(changes, aim_):
    """The reading of a deterministic simulator's gauge whose three runs reproduce one another (CityLearn, pandapower, MuJoCo,
    the swarms): their changes, each in percent of native as a fraction, all one way. Under the floor (the mean under 0.5%) it
    reads STEADY, under the floor; from 0.5% up, GAIN, LOSS or power given in all three of our runs (no noise to stand beyond)."""
    mean = sum(changes) / len(changes)
    if abs(mean) < SIZE_FLOOR and aim_ not in (NEVER_MORE, NEVER_LESS):   # a count that must never move one way has no floor
        return f"{EVEN_FLOOR} (the three runs' mean {100 * abs(mean):.2f}%)"
    return f"**{word(mean < 0, aim_)} {IN_ALL_THREE}**"


def reading_kind(reading: str) -> str:
    """A reading's kind for a count under a table: its words without the sizes and counts after them ('STEADY, under the floor',
    'GAIN by the mean of our three runs', 'STEADY, no difference beyond the noise')."""
    r = (reading or "").strip().strip("*").strip()
    return r.split(" (")[0].split(", beyond the noise in ")[0].strip("*").strip()


def run_word(r, aim_):
    """One run's own word, for the number beside it: its change of 0.5% or more read by the gauge's aim, STEADY under it."""
    if aim_ in (None, NEVER_MORE) or r is None:
        return None
    nat, d = r.get("native"), r.get("diff")
    if d is None or (nat and abs(d) / abs(nat) < SIZE_FLOOR) or d == 0:
        return STEADY
    return word(d < 0, aim_)


def even_floor(size: float) -> str:
    """The reading of a change that held the same way in all three runs but under the floor in every one of them."""
    return f"{EVEN_FLOOR} (every run under {100 * SIZE_FLOOR:g}%; the largest {100 * size:.2f}%)"


def in_all_three(fell: bool, aim_: str, size: float | None = None) -> str:
    """The three-run reading of a number that went the same way in all three runs, every interval clear of zero. size, where the
    caller has it, is the largest run's relative change: under the founder's floor in every run the reading is STEADY, under the floor."""
    if size is not None and size < SIZE_FLOOR:
        return even_floor(size)
    return f"**{word(fell, aim_)} {IN_ALL_THREE}**"


def cut_or_up(fell: bool) -> str:
    """The plain verb for which way a number went, beside its word: cut or up."""
    return "cut" if fell else "up"


EVEN_SAME = f"{STEADY}, the same"                     # every run's two values equal to nine decimal places (EXACT_REL; the referee's work order of 25 October)
EVEN_NOISE = f"{STEADY}, no difference beyond the noise"


def even_noise(detail: str = "") -> str:
    """No difference beyond the noise: in the runs counted the interval includes zero, so native and Omni could not be told
    apart on that gauge; that is the result. detail names the runs, '2 of 3 runs'."""
    return f"{EVEN_NOISE} ({detail})" if detail else EVEN_NOISE


NEVER_MORE_UP = f"{LOSS} in at least one of our runs"            # a count that must never rise rose in a run
NEVER_MORE_HELD = f"{GAIN} or {STEADY} {IN_ALL_THREE}"              # ... and rose in none, and fell in at least one

STACK_RULE = ("Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, "
              "the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and "
              "clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our "
              "three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its "
              "sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the "
              "floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**.")


def never_more_rule(what: str) -> str:
    """The rule sentence for a count that must never rise."""
    return f"{what}: any rise in any run reads **{NEVER_MORE_UP}**."


def stack_reading(rs, direction, same_rel, key=None):
    """The three-run reading of one gauge of a stack's A/B/C table (PostgreSQL, Kafka, Redis, MongoDB, MySQL, the machine's
    frequency ceiling), from its three within-run paired results ({"native", "diff", "significant"}). direction is the
    gauge's declared aim (LOWER, HIGHER, SPENT, NEVER_MORE, or SHOWN_AIM); key is its name, for the resources declared
    "lower" before the word "spent" was written."""
    if any(r is None for r in rs):
        return "no value"
    return three_run_reading(rs, aim(direction, key), same_rel)


# --------------------------------------------------------------------------------------------- reading any table's words
_DIRECTION = (("lower or the same in all three of our runs", True), ("lower in all three of our runs", True),
              ("higher in all three of our runs", False), ("higher in at least one of our runs", False),
              ("higher in a repetition", False), ("confirmed lower", True), ("confirmed higher", False))


def classify(reading, aim_=None):
    """A reading in one word for the scorers: "gain", "loss", "given", "noise", "same", "disagree" or "unjudged". Reads every
    table's words: GAIN/STEADY/LOSS and power given; the direction words of 13 October (lower, higher; aim_ turns them into a
    word, and is then required); toward and away from the aim; better, worse and "confirmed" of the older tables. A reading
    that moved away from its aim on a resource spent (aim_ SPENT) is power given."""
    r = (reading or "").strip().strip("*").strip()
    lo = r.lower()
    if not lo or lo.startswith(("shown", "no value", "not taken", "n/a")):
        return "unjudged"
    if lo.startswith(("gain or steady", "gain or even", "gain")):
        return "gain"
    if lo.startswith("loss"):
        return "loss"
    if lo.startswith(GIVEN):
        return "given"
    if lo.startswith(("steady", "even")):
        return "noise" if "noise" in lo else "same"
    if lo.startswith("no difference"):
        return "noise"
    if "disagree" in lo or "runs differ" in lo or "different ways" in lo:
        return "disagree"
    away = ("given" if aim_ in (SPENT, WORK_PER) else "loss")
    for old, cls in (("better", "gain"), ("worse", away), ("toward", "gain"), ("away", away)):   # older tables, kept as written
        if lo.startswith(old) or lo.startswith(f"confirmed {old}") or lo.startswith(f"**{old}"):
            return cls
    for w, fell in _DIRECTION:
        if lo.startswith(w):
            if aim_ is None:
                raise ValueError(f"the reading {reading!r} says a direction; its gauge's aim is needed to give it a word")
            return {GAIN: "gain", LOSS: "loss", GIVEN: "given"}[word(fell, aim_)]
    if lo.startswith("same"):
        return "same"
    # a receipt of its own kind (the robustness test's "the same in all three of our runs" for a hand-back held, "handed back
    # within the allowance ..."): a fact about the governor, not a gauge against native; the caller decides what it is
    raise ValueError(f"unknown reading: {reading!r}")


WORD_OF_CLASS = {"gain": GAIN, "loss": LOSS, "given": GIVEN, "same": STEADY, "noise": STEADY}


def word_of(reading, aim_=None):
    """A reading's one word, the single place every page, record and chart takes it from (the referee's work order of 25
    October, item 14: no word read twice by two hands): GAIN, LOSS, power given, STEADY, "the runs disagree", "the runs
    differ", or None for a row shown and not judged. Reads every table's words, the older ones' included (classify)."""
    r = (reading or "").strip().strip("*").strip().lower()
    if "runs differ" in r:
        return "the runs differ"
    try:
        c = classify(reading, aim_)
    except ValueError:
        return None
    if c == "disagree":
        return "the runs disagree"
    return WORD_OF_CLASS.get(c)


def landed(table) -> bool:
    """Whether a three-run table carries a result (whole): a gauge row, or a workload beside the tuning one (the table writers
    write a workload only where every run holds it). A table written from runs that failed (its workloads or rows empty: 20
    October, the omni-v12 MongoDB table) has not taken its benchmark's place: the same benchmark's table on an older engine
    stands as that engine's result until the newer engine's three runs land. The one rule every tool that picks a benchmark's
    newest table reads (tools/omni_index.py, tools/benefit_sheet.py, tools/levels.py, tools/power.py, the live benchmark engine's
    docs/engine/export_scenarios.py). A Markdown table is read through its JSON twin; one kept only in Markdown, or whose JSON
    is another table's shape (neither rows nor workloads), reads as whole."""
    import json
    p = Path(table)
    if p.suffix == ".md":
        if not p.with_suffix(".json").exists():
            return True
        p = p.with_suffix(".json")
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    if not isinstance(d, dict):
        return False
    # a table whose runs ran on two engines is no three-run result of either (24 October: ten omni-v17 tables held a C run on
    # omni-v18, and the index and the benefit sheet counted them); the benchmark stands on its newest table on one engine
    if len({str(r.get("engine", "")).split(" ")[0] for r in d.get("runs") or [] if isinstance(r, dict) and r.get("engine")}) > 1:
        return False
    if "rows" not in d and "workloads" not in d:
        return True                      # another table's shape (the organisms, a cloud set's repetitions): its own writer decides
    if d.get("rows"):
        return True
    return any(wl != "tuning" for wl in (d.get("workloads") or {}))


def judged(reading: str) -> bool:
    """A judged reading: GAIN, LOSS or power given in all three runs (every interval clear of zero) or by the mean of the three
    runs (a change of 0.5% or more, the founder's order of 24 October 2026), an older table's words for the same, or a count
    that must never rise and rose in a run."""
    r = (reading or "").strip().strip("*").strip()
    lo = r.lower()
    return (lo.startswith("confirmed") or IN_ALL_THREE in r or MEAN_OF_THREE in r or lo.startswith(NEVER_MORE_UP.lower())
            or lo.startswith("higher in at least one of our runs"))


def toward_aim(reading: str, aim_):
    """For the tools that score the headline: True when a judged reading moved the gauge toward its declared aim (GAIN),
    False when away from it (LOSS or power given), None when it is not judged. aim_ may be True (the aim is lower) or False
    (higher), the way the older scorers named it, or an aim word."""
    if not judged(reading):
        return None
    a = {True: LOWER, False: HIGHER}.get(aim_, aim_) if isinstance(aim_, bool) else aim_
    c = classify(reading, a)
    return True if c == "gain" else False if c in ("loss", "given") else None


def in_gel_words(reading: str, diffs, aim_) -> str:
    """A judged reading in GAIN/STEADY/LOSS, whatever words its table was written in: a direction becomes its word by the
    gauge's aim; an older table's better or worse becomes GAIN, LOSS or power given by the same aim (a judged reading has
    the same sign in every run)."""
    r = (reading or "").strip().strip("*")
    if not judged(r):
        return r
    try:
        c = classify(r, aim_)
    except ValueError:
        signs = {(d > 0) - (d < 0) for d in diffs if d is not None}
        if len(signs) != 1 or aim_ is None:
            return r
        c = {GAIN: "gain", LOSS: "loss", GIVEN: "given"}[word(signs == {-1}, aim_)]
    w = {"gain": GAIN, "loss": LOSS, "given": GIVEN}.get(c)
    if w is None:
        return r
    return NEVER_MORE_UP if r.lower().startswith(("higher in at least one", NEVER_MORE_UP.lower())) else f"{w} {IN_ALL_THREE}"


def row_gain(v) -> bool:
    """Whether a row of an organism report (tools/six_kube_report.py) is a GAIN: its field gain, or, in the receipts written
    before, the fields they kept for the same thing (toward_aim since 13 October, better before)."""
    for k in ("gain", "toward_aim", "better"):
        if k in v:
            return bool(v[k])
    return False


row_toward = row_gain


# ---------------------------------------------------------------------------------------- labels written by a rule
GAIN_AND_LOSS = f"{GAIN} AND {LOSS}"        # a muscle with one aim toward and one away: both stand in the table
GAIN_GIVEN = f"{GAIN}, {GIVEN}"             # service toward its aim, bought with a resource spent
# The words for the labels the rules write (the realms of v5, tools/run_realms_v5.py; the engine harness's and the card
# bench's preregistered labels, realms/harness.py and tools/gpu_reps.py, which keep their recorded wording until the
# engine's next version), and for the names the older results used.
LABEL_WORDS = {
    "TOWARD ITS AIMS": GAIN, "BOTH WAYS": GAIN_AND_LOSS, "MIXED": GAIN_AND_LOSS, "AWAY FROM ITS AIMS": LOSS, "WORSE": LOSS,
    "SAME AS NATIVE": STEADY, "AT ITS LIMIT ON NATIVE": STEADY,
    "SUPERIOR WITHIN GUARDRAILS": GAIN, "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": GAIN_AND_LOSS,
    "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": GAIN_GIVEN, "NONINFERIOR / INCONCLUSIVE": STEADY, "NOT ESTABLISHED": STEADY,
    "AWAY FROM ITS AIM": LOSS, "INVALID": "INVALID",
}
GAIN_PARTS = ("MORE WORK", "FASTER", "FEWER MISSES", "LESS ENERGY")


def gel_of_label(label):
    """GAIN, STEADY, LOSS, GAIN AND LOSS, "GAIN, power given" or INVALID for a label a rule wrote; None if it is no label."""
    lab = (label or "").replace("**", "").strip()
    if lab in LABEL_WORDS:
        return LABEL_WORDS[lab]
    if lab in (GAIN, STEADY, LOSS, GAIN_AND_LOSS, GAIN_GIVEN):
        return lab
    parts = [x.strip() for x in lab.split("+")]
    if lab and all(x in GAIN_PARTS for x in parts):        # the gains a muscle showed, joined: MORE WORK + FASTER ...
        return GAIN
    return None


LABEL_SHOWN = {
    "TOWARD ITS AIMS": GAIN, "BOTH WAYS": GAIN_AND_LOSS, "MIXED": GAIN_AND_LOSS, "AWAY FROM ITS AIMS": LOSS, "WORSE": LOSS,
    "SAME AS NATIVE": f"{STEADY} (the same as native)", "AT ITS LIMIT ON NATIVE": f"{STEADY} (at its limit on native)",
    "SUPERIOR WITHIN GUARDRAILS": f"{GAIN} (within the guardrails)",
    "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": f"{GAIN_AND_LOSS} (energy cut, service traded for it)",
    "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": f"{GAIN_GIVEN} (service GAIN, energy given for it)",
    "NONINFERIOR / INCONCLUSIVE": f"{STEADY} (inside the noise, within the guardrails)",
    "NOT ESTABLISHED": f"{STEADY} (not established: inside the noise, a guardrail crossed on the mean)",
    "AWAY FROM ITS AIM": LOSS, "INVALID": "INVALID",
}


def labelled(label) -> str:
    """A label as a table shows it, its word first: "GAIN (fewer misses)", "STEADY (at its limit on native)", "LOSS"."""
    lab = (label or "").replace("**", "").strip()
    if lab in LABEL_SHOWN:
        return LABEL_SHOWN[lab]
    w = gel_of_label(lab)
    if w is None or w == lab:
        return lab
    return f"{w} ({lab.lower()})"


# ------------------------------------------------------------------------------------- the count under a three-run table
class Tally:
    """The count under a three-run table: judged gauge-rows that read GAIN, LOSS and power given in all three of our runs,
    rows that read STEADY, and rows where the runs disagree."""

    def __init__(self):
        self.gain = self.loss = self.given = self.even = self.disagree = 0

    def add(self, reading, direction, key=None):
        c = classify(reading, aim(direction, key))
        self.gain += c == "gain"
        self.loss += c == "loss"
        self.given += c == "given"
        self.even += c in ("noise", "same")
        self.disagree += c == "disagree"

    def sentence(self, n, what="workloads"):
        return (f"**Across {n} {what}: {self.gain} gauge-rows GAIN, {self.loss} LOSS, {self.given} power given (each in all three "
                f"of our runs, or by the mean of the three: a change of 0.5% or more), {self.even} STEADY, {self.disagree} where the "
                f"runs disagree.**")

    def counts(self):
        return f"{self.gain} GAIN, {self.loss} LOSS, {self.given} power given, {self.even} STEADY, {self.disagree} disagree"


DETERMINISTIC_RULE = ("a gauge reads **GAIN** or **LOSS in all three of our runs** when all three runs give the same sign and their "
                      "mean change is 0.5% or more, judged by what the gauge is for and never by its sign (a resource spent that rose "
                      "reads **power given**); a mean under 0.5% reads **STEADY, under the floor**")
ACROSS_HEAD = "GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ"
ACROSS_RULE = "|---|---:|---:|---:|---:|---:|"


def across_cells(t, direction=None, key=None) -> str:
    """One gauge's cells under a deterministic simulator's three-run tables ({reading: [cases]}): how many cases read GAIN,
    LOSS and power given in all three of our runs (the cases named where they read LOSS or power given), then the cases
    STEADY and the cases where the runs differ."""
    a = aim(direction, key)
    by = {"gain": [], "loss": [], "given": [], "even": [], "disagree": []}
    for reading, cases in t.items():
        c = classify(reading, a)
        by["even" if c in ("noise", "same") else c if c in by else "even"].extend(cases)
    cell = lambda xs, named: f"{len(xs)}" + (f" ({', '.join(xs)})" if named and xs else "")
    return (f"{cell(by['gain'], False)} | {cell(by['loss'], True)} | {cell(by['given'], True)} | {len(by['even'])} | "
            f"{len(by['disagree'])}")


def across_counts(tally, direction_of):
    """(gain, loss, given, differ) over a simulator's tally ({gauge: {reading: [cases]}}): case-rows that read GAIN, LOSS
    and power given in all three of our runs, and where the runs differ. direction_of(gauge) gives the gauge's direction."""
    g = l_ = gv = d = 0
    for k, t in tally.items():
        a = aim(direction_of(k), k)
        for reading, cases in t.items():
            c = classify(reading, a)
            g += len(cases) * (c == "gain"); l_ += len(cases) * (c == "loss"); gv += len(cases) * (c == "given")
            d += len(cases) * (c == "disagree")
    return g, l_, gv, d


def with_own_runs(lines):
    """A table's lines with OWN_RUNS under its title (the legal notice is stamped around them afterwards)."""
    return list(lines[:1]) + ["", OWN_RUNS] + list(lines[1:])


# ------------------------------------------------------------------------------------------------------------- the key
def word_sign(word):
    """The sign a number carries beside its word (the founder's order of 20 October, said again on 22 October: the word GAIN can
    never have a minus beside it): GAIN '+', LOSS '−', STEADY '=', power given '+' (what Omni put in); a reading with no word of
    its own (shown, tuning, the runs disagree) keeps the number's own direction."""
    w = str(word or "")
    if w.startswith("GAIN") or w.startswith("power given"):
        return "+"
    if w.startswith("LOSS"):
        return "−"
    if w.startswith(("STEADY", OLD_EVEN)):
        return "="
    return None


def by_word(x, word, unit="%", digits=1):
    """A change beside its word: the size alone, with no sign ('GAIN 73.0%', 'LOSS 16.8%', 'STEADY 0.9%'), because a sign beside
    a word was read as the raw direction (the referee's work order of 25 October: a raw change is never turned to wear the
    verdict's sign); with no word of its own, the raw change with its true sign. The raw change is printed apart, labelled raw."""
    if x is None or x != x:
        return "—"
    size = f"{abs(x):.{digits}f}{unit}"
    return size if word_sign(word) else f"{'+' if x > 0 else '−' if x < 0 else '±'}{size}"


def interval_by_word(lo, hi, word, unit="%", digits=1):
    """The 95% interval of a raw change, always as it lies, each end with its true sign ('raw −5.0% to −1.8%'), labelled raw
    beside a word so that it is never read as the verdict's own size (the referee's work order of 25 October)."""
    f = lambda v: f"{abs(v):.{digits}f}{unit}"
    raw = lambda v: f"{'+' if v > 0 else '−' if v < 0 else '±'}{f(v)}"
    return f"{'raw ' if word_sign(word) else ''}{raw(lo)} to {raw(hi)}"


KEY_TITLE = "The key: GAIN, STEADY and LOSS"
KEY_BEGIN = "<!-- the key: GAIN, STEADY and LOSS (tools/readings.py) -->"
KEY_END = "<!-- end of the key -->"
LETTERS = (
    (GAIN, "surplus and positive variance", (("G", "Growth", "asset appreciation"), ("A", "Advantage", "risk reduction"),
                                             ("I", "Improvement", "margin expansion"), ("N", "Net-positive", "profitable outcome")),
     "the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a "
     "resource cut"),
    (STEADY, "the par baseline: equilibrium", (("S", "Stable", "zero variance"), ("T", "True to baseline", "expected norm"),
                                                    ("E", "Equilibrium", "balanced risk"), ("A", "At par", "no net change"),
                                                    ("D", "Drift-free", "within the 0.5% floor"), ("Y", "Yield held", "nothing lost")),
     "native and Omni-Compass within 0.5% of each other: the mean of the three runs' changes under the 0.5% floor, or no "
     "change at all; a knob native already runs at the top of its range is STEADY, at its limit on native"),
    (LOSS, "actuarial deficit and exposure", (("L", "Leakage", "capital drain"), ("O", "Off-track", "adverse selection"),
                                              ("S", "Setback", "claim liability"), ("S", "Subpar", "negative variance")),
     "the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures"),
)


def key_lines():
    """The key as Markdown lines (the manual's front matter, the README, the reading guide and the summary carry it)."""
    L = [f"## {KEY_TITLE}", "",
         "Every judged reading in Omni-Compass is one of three words: **GAIN**, **STEADY** or **LOSS**. Better, same and worse "
         "are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: "
         "who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before "
         "the runs.", "",
         "| Word | What each letter stands for | Its sense in underwriting | What it means in a table |", "|---|---|---|---|"]
    for w, sense, letters, meaning in LETTERS:
        L.append(f"| **{w}** | " + "; ".join(f"**{a}** {b} ({c})" for a, b, c in letters) + f" | {sense} | {meaning} |")
    L += ["", "How the sign of a number becomes a word:", "",
          "- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.",
          "- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.",
          "- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a "
          "bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work "
          "and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the "
          "founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak "
          "that rose is power given, in a data centre and in a building alike (17 October).",
          "- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; "
          "a fall is power given, because it falls when more power is given for the same work.",
          "- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).",
          "- **The floor, and every change above it** (the founder's orders of 20 and 24 October 2026): a change of half of one "
          "percent (0.5%) or more either way is a change, and reads **GAIN** or **LOSS** (or **power given**) by what the gauge "
          "is for; STEADY is kept for a change under 0.5%. The change is the mean of the three runs' changes, each in percent of "
          "native. Where every run moved the same way with its 95% interval clear of zero, the word reads **in all three of our "
          "runs**; otherwise it reads **by the mean of our three runs** and says in how many of the three runs it stood beyond "
          "the noise, so a reader sees how firmly it stands. Where runs moved 0.5% or more in opposite directions, the reading is "
          "**the runs disagree**. A mean under 0.5% reads **STEADY, under the floor**, with its size.",
          "- **Two numbers, never mixed** (the referee's work order of 25 October): every row shows native's value and "
          "Omni-Compass's, the **raw change** (Omni-Compass − native) / native with its true sign, + for a rise and − for a fall "
          "whatever the gauge is for, labelled raw, and apart from it the word with its size and no sign. A bill cut 3% reads "
          "raw −3.0%, GAIN 3.0%; failed requests up 2% read raw +2.0%, LOSS 2.0%; a pod start wait from 0.22 s to 0.83 s reads "
          "raw +275.0%, LOSS 275.0%; a change under the 0.5% floor reads STEADY 0.3%. No raw sign is ever turned to match a word.", "",
          "Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN "
          "GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: "
          + "; ".join(f"{k} reads {v}" for k, v in LABEL_SHOWN.items() if k not in ("WORSE", "MIXED", "AWAY FROM ITS AIM", "INVALID"))
          + ". A run that breaks its own validity checks reads INVALID and carries no word.", "",
          "Every reading is one of these. **GAIN, LOSS or power given in all three of our runs**: A, B and C moved the same way, "
          "every 95% interval clear of zero. **GAIN, LOSS or power given by the mean of our three runs**: the runs' mean moved "
          "0.5% or more, with the count of runs that stood beyond the noise beside it. **STEADY, under the floor**: the mean moved "
          "less than 0.5%. **STEADY, the same**: no change at all. **The runs disagree**: runs moved 0.5% or more in opposite "
          "directions, so the test is unstable there and is looked into. **Shown, not judged**: a gauge declared in advance as "
          "shown only, such as the knob's own setting.", "",
          "Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as "
          "surplus, par or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never "
          "to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (STEADY). Its first rule is do no "
          "harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less "
          "than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit "
          "(`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause "
          "is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.", "",
          "Disclosure and disclaimer: GAIN, STEADY and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention "
          "for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or "
          "insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs "
          "measured against native under the declared aims, not a promise about any other system; every number stands beside "
          "its word, so a reader can judge it by any other convention. " + OWN_RUNS]
    return L


def key_block():
    """The key between its two markers, as a page carries it."""
    return [KEY_BEGIN] + key_lines() + [KEY_END]


def key_text() -> str:
    """The key as plain text, for a terminal."""
    out = []
    for ln in key_lines():
        if ln.startswith("|---"):
            continue
        if ln.startswith("| **"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            out += [f"{cells[0]}: {cells[1]}", f"    underwriting: {cells[2]}", f"    in a table: {cells[3]}"]
            continue
        if ln.startswith("| Word"):
            continue
        out.append(ln)
    return re.sub(r"\*\*|`", "", "\n".join(out)).replace("## ", "")


# ---------------------------------------------------------------------------------- how to read this receipt
RECEIPT_BEGIN = "<!-- how to read this receipt (tools/readings.py) -->"
RECEIPT_END = "<!-- end: how to read this receipt -->"


def receipt_key_lines():
    """The short reading instruction every receipt and table carries under its title (the founder's order of 16 October,
    night: whoever reads a report must know, before the first number, how a plus, a minus or a zero becomes a word)."""
    return [
        "**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by "
        "the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, "
        "a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other "
        "(the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. "
        "**LOSS**: the "
        "gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, "
        "the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one "
        "that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and "
        "never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus "
        "can read GAIN (a "
        "response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' "
        "changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every "
        "interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; "
        "**the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not "
        "judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring "
        "and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, "
        "section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. " + OWN_RUNS,
    ]


def receipt_key():
    """The block between its markers, as every table writer emits it under the title."""
    return [RECEIPT_BEGIN, *receipt_key_lines(), RECEIPT_END]


# The standing tables that must carry the block: every page a reader is sent to for a result on the engine that stands.
RECEIPT_PAGES = ("results/live/V7_*.md", "results/realms_v5/REALMS_V5.md", "results/grid_v5/GRID.md", "docs/BENEFIT_SHEET.md",
                 "docs/WIRING_VERDICTS.md", "docs/STATE_OF_PLAY.md")


def receipt_pages(root: Path = ROOT):
    out = []
    for pat in RECEIPT_PAGES:
        out += sorted(str(p.relative_to(root)) for p in root.glob(pat))
    return out


def _with_receipt_key(text: str) -> str:
    """The text with the block in place: replaced where its markers stand, else inserted after the notice under the title."""
    block = "\n".join(receipt_key())
    if RECEIPT_BEGIN in text and RECEIPT_END in text:
        a = text.index(RECEIPT_BEGIN)
        b = text.index(RECEIPT_END) + len(RECEIPT_END)
        return text[:a] + block + text[b:]
    lines = text.split("\n")
    at = None
    for i, ln in enumerate(lines[:12]):
        if ln.startswith("> ©"):                       # the legal notice under the title: the block goes right after it
            at = i + 1
            break
    if at is None:
        for i, ln in enumerate(lines[:4]):
            if ln.startswith("# "):
                at = i + 1
                break
    if at is None:
        return text
    while at < len(lines) and lines[at].strip() == "":
        at += 1
    return "\n".join(lines[:at] + [block, ""] + lines[at:])


def check_receipts(root: Path = ROOT):
    """The standing tables that do not carry the reading block word for word."""
    bad = []
    for p in receipt_pages(root):
        t = (root / p).read_text()
        if RECEIPT_BEGIN not in t or RECEIPT_END not in t or _with_receipt_key(t) != t:
            bad.append(p)
    return bad


KEY_PAGES = ("README.md", "docs/HOW_TO_READ_THE_RESULTS.md", "docs/OMNI_COMPASS_MANUAL.md",
             "docs/OMNI_COMPASS_OWNERS_MANUAL.md", "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md")


def _with_key(text: str) -> str:
    block = "\n".join(key_block())
    if KEY_BEGIN in text and KEY_END in text:
        a = text.index(KEY_BEGIN)
        b = text.index(KEY_END) + len(KEY_END)
        return text[:a] + block + text[b:]
    return text


def check_pages(root: Path = ROOT):
    """The pages that must carry the key and do not carry it word for word."""
    bad = []
    for p in KEY_PAGES:
        f = root / p
        if not f.exists():
            continue
        t = f.read_text()
        if KEY_BEGIN not in t or KEY_END not in t or _with_key(t) != t:
            bad.append(p)
    return bad


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--key", action="store_true"); g.add_argument("--check", action="store_true"); g.add_argument("--fix", action="store_true")
    a = ap.parse_args(argv)
    if a.key:
        print(key_text())
        return 0
    if a.fix:
        for p in KEY_PAGES:
            f = ROOT / p
            if f.exists():
                t = f.read_text(); n = _with_key(t)
                if n != t:
                    f.write_text(n); print(f"the key rewritten in {p}")
        for p in receipt_pages():
            f = ROOT / p
            t = f.read_text(); n = _with_receipt_key(t)
            if n != t:
                f.write_text(n); print(f"how to read this receipt written in {p}")
        return 0
    bad = check_pages()
    for p in bad:
        print(f"{p}: the key (between {KEY_BEGIN} and {KEY_END}) is missing or not word for word")
    for p in check_receipts():
        bad.append(p)
        print(f"{p}: the block 'How to read this receipt' (between {RECEIPT_BEGIN} and {RECEIPT_END}) is missing or not word for word")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
