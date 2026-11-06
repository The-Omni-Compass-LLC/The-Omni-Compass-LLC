# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The wiring search (the founder's order of 12 October: every muscle its own wiring and settings, set in stone, so
whoever wires that muscle wires it the same way; whatever hurts a muscle is fixed; a muscle native already runs at its
limit is made faster or given the same work on less energy).

For every muscle, on DEVELOPMENT seeds only (never the preregistered 3000-3009), each candidate card is run through the
engine's own muscle-alone loop (realms/harness.py run_muscle_arm, the official table's loop; only the card it reads is
swapped) under both muscle loads (its own load, and work waiting in line), paired with native seed by seed. A card is:

  max          the engine's default (realms/compass_arm_v5.py V5CFG): the muscle at its own limit for the most work
  max_*        the max with one setting moved (how full a pool runs before it calls for more, how long it remembers a
               peak, the margin a battery keeps under its line)
  save         the tune-down (V5SAVE): native's work on the least energy, held by the engine's own physics floors
  save_*       the tune-down with one guard or permission changed
  compass      the v3 law (realms/compass_arm.py)

The rule, fixed before any result was read (results/development/wiring/WIRING_DEV.md repeats it):
  1. A card is out if the lease did not hand its knob back on every seed, or if under either load it did less work,
     more misses or cleared its line later (95% intervals over the seeds, clear of zero), or if it spent more energy
     with no gain in work, speed or misses.
  2. Gains rank: more work, then faster, then fewer misses, then less energy (the same work, speed and misses on less
     energy: the gain left to a muscle native already runs at its limit).
  3. The card with the best set of gains is chosen; the default (max) is kept wherever it gives that set, so another
     card replaces it only where it adds a gain the max does not give; among other cards with the same set, the larger
     work gain, then the fewer misses, then the lower energy, then the order above.
  4. A muscle no card improves keeps the max, and says why (nothing above native to give, and nothing to save that the
     guards allow).

Nothing here changes the engine. The chosen cards are frozen in results/development/wiring/WIRING_CARDS.json; they enter
the engine only as the next version, run again on the preregistered seeds and reported whatever they show.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import realms.harness as H  # noqa: E402
from realms.compass_arm import compass_apply  # noqa: E402
from realms.compass_arm_v5 import Cfg, V5CFG, V5SAVE, compass_apply_v5  # noqa: E402
from realms.harness import interval, paired, run_muscle_arm  # noqa: E402
from tools.legal import NOTICE, TOP  # noqa: E402
from tools.run_realms_v5 import MUSCLE_LOADS  # noqa: E402

DEV_SEEDS = list(range(7100, 7110))
PREREG = set(range(3000, 3010))


def _cfg(base, **kw):
    c = Cfg()
    c.__dict__.update(base.__dict__)
    c.__dict__.update(kw)
    return c


CARDS = {
    "max": ("max", V5CFG),
    "max_full90": ("max", _cfg(V5CFG, edge_util=0.90)),
    "max_full85": ("max", _cfg(V5CFG, edge_util=0.85)),
    "max_full98": ("max", _cfg(V5CFG, edge_util=0.98)),
    "max_mem10": ("max", _cfg(V5CFG, window=10)),
    "max_mem40": ("max", _cfg(V5CFG, window=40)),
    "max_margin233": ("max", _cfg(V5CFG, line_z=2.33)),
    "max_margin372": ("max", _cfg(V5CFG, line_z=3.72)),
    "save": ("save", V5SAVE),
    "save_nocap": ("save", _cfg(V5SAVE, power_cap=False)),
    "save_shave": ("save", _cfg(V5SAVE, storage_shave=True)),
    "save_precool": ("save", _cfg(V5SAVE, precool=True)),
    "save_free": ("save", _cfg(V5SAVE, target_free=True)),
    "compass": ("compass", None),
}
ORDER = list(CARDS)
GAINS = ("MORE WORK", "FASTER", "FEWER MISSES", "LESS ENERGY")


def run_card(row, seed, card, load):
    """One muscle, one seed, one card, through the official loop: the max cards set the harness's default card, the
    save cards its tune-down, the compass card the v3 law."""
    law, cfg = CARDS[card]
    if law == "max":
        H.V5CFG = cfg
        try:
            return run_muscle_arm(row, seed, "v5", load)
        finally:
            H.V5CFG = V5CFG
    if law == "save":
        keep = H.LAWS["v5save"]
        H.LAWS["v5save"] = lambda p, k, c=cfg: compass_apply_v5(p, k, c)
        try:
            return run_muscle_arm(row, seed, "v5save", load)
        finally:
            H.LAWS["v5save"] = keep
    keep = H.LAWS["compass"]
    H.LAWS["compass"] = compass_apply
    try:
        return run_muscle_arm(row, seed, "compass", load)
    finally:
        H.LAWS["compass"] = keep


def judge(per, runs):
    """Gains and losses of one card under one load, by the official rule (95% intervals over seeds, clear of zero), with
    energy beside them: 'less' and 'more' when its interval is clear of zero."""
    w = interval([c["work"] for c in per])
    v = interval([c["viol_pp"] for c in per])
    e = interval([c["energy"] for c in per])
    gains = {"MORE WORK": w[1] > 1e-12, "FEWER MISSES": v[2] < -1e-12}
    losses = {"LESS WORK": w[2] < -1e-12, "MORE MISSES": v[1] > 1e-12}
    if all("speed" in c for c in per):
        s = interval([c["speed"] for c in per])
        gains["FASTER"], losses["SLOWER"] = s[2] < -1e-12, s[1] > 1e-12
    return {"gains": [g for g, x in gains.items() if x], "losses": [l for l, x in losses.items() if x],
            "energy_less": e[2] < -1e-12, "energy_more": e[1] > 1e-12,
            "work": w[0], "viol_pp": v[0], "energy": e[0], "valid": all(r["restore_ok"] for r in runs),
            "writes": sum(r["writes"] for r in runs) / len(runs)}


def muscle_cards(args):
    """Every card of one muscle under both loads, and the card the rule chooses."""
    row, seeds, cards = args
    t0 = time.time()
    res = {c: {} for c in cards}
    for load in MUSCLE_LOADS:
        arg = None if load == "normal" else load
        nat = [run_muscle_arm(row, s, "native", arg) for s in seeds]
        for c in cards:
            runs = [run_card(row, s, c, arg) for s in seeds]
            per = [paired(a, n) for a, n in zip(runs, nat)]
            if all("line_k" in n for n in nat):
                for p, a, n in zip(per, runs, nat):
                    p["speed"] = (a["line_k"] + 1) / (n["line_k"] + 1) - 1.0
            res[c][load] = judge(per, runs)
    summ = {}
    for c in cards:
        by = res[c].values()
        gains = sorted({g for o in by for g in o["gains"]}, key=GAINS.index)
        losses = sorted({l for o in by for l in o["losses"]})
        less = any(o["energy_less"] for o in by) and not any(o["energy_more"] for o in by)
        more = any(o["energy_more"] for o in by)
        valid = all(o["valid"] for o in by)
        if less and not gains:
            gains = ["LESS ENERGY"]
        elif less:
            gains = gains + ["LESS ENERGY"]
        out = (not valid) or bool(losses) or (more and not [g for g in gains if g != "LESS ENERGY"])
        summ[c] = {"gains": gains, "losses": losses, "valid": valid, "out": out,
                   "work": sum(o["work"] for o in by) / len(res[c]), "viol_pp": sum(o["viol_pp"] for o in by) / len(res[c]),
                   "energy": sum(o["energy"] for o in by) / len(res[c]), "writes": max(o["writes"] for o in by)}
    chosen, why = choose(summ)
    return {"row": row, "cards": summ, "loads": res, "chosen": chosen, "why": why, "seconds": time.time() - t0}


def classes(g):
    return tuple(x in g for x in GAINS)


def choose(summ):
    """The rule (module docstring): the best set of gains; the max kept wherever it gives that set."""
    ok = {c: s for c, s in summ.items() if not s["out"] and s["gains"]}
    if not ok:
        reasons = sorted({l for s in summ.values() for l in s["losses"]})
        return "max", ("no card gains without a loss" + (f" (the others: {', '.join(reasons)})" if reasons else
                                                         ": nothing above native to give, nothing the guards let it save"))
    best = max(classes(s["gains"]) for s in ok.values())
    top = [c for c, s in ok.items() if classes(s["gains"]) == best]
    if "max" in top:
        return "max", "the max gives the best set of gains"
    top.sort(key=lambda c: (-ok[c]["work"], ok[c]["viol_pp"], ok[c]["energy"], ORDER.index(c)))
    return top[0], "adds " + " + ".join(g for g in ok[top[0]]["gains"] if g not in summ["max"]["gains"]) + " to the max"


def label(gains):
    return " + ".join(gains) if gains else "NO GAIN"


def write(out, res, seeds, cards, elapsed):
    out.mkdir(parents=True, exist_ok=True)
    with (out / "WIRING_DEV.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["muscle_id", "family", "muscle", "template", "preset", "knob", "card", "why", "max_gains",
                    "card_gains", "card_work", "card_viol_pp", "card_energy", "card_writes"] + cards)
        for r in res:
            row, s = r["row"], r["cards"]
            ch = s[r["chosen"]]
            w.writerow([row["muscle_id"], row["family"], row["muscle"], row["template"], row["preset"], row["knob"],
                        r["chosen"], r["why"], label(s["max"]["gains"]) if not s["max"]["out"] else "out: " +
                        ", ".join(s["max"]["losses"] or ["no gain, more energy"]), label(ch["gains"]),
                        f"{ch['work']:.5f}", f"{ch['viol_pp']:.4f}", f"{ch['energy']:.5f}", f"{ch['writes']:.1f}"] +
                       [("OUT" if s[c]["out"] else label(s[c]["gains"])) for c in cards])
    cards_out = {r["row"]["muscle_id"]: {"card": r["chosen"], "why": r["why"], "muscle": r["row"]["muscle"],
                                         "template": r["row"]["template"], "knob": r["row"]["knob"]} for r in res}
    (out / "WIRING_CARDS.json").write_text(json.dumps({"seeds": seeds, "cards": {c: CARDS[c][0] + (
        "" if CARDS[c][1] is None else " " + json.dumps({k: v for k, v in CARDS[c][1].__dict__.items()
                                                       if v != getattr(Cfg(), k)})) for c in cards},
        "muscles": cards_out}, indent=1) + "\n")
    n = len(res)
    was = {"gain": 0, "none": 0}
    now = {"gain": 0, "none": 0}
    moved = {}
    for r in res:
        s = r["cards"]
        g0 = bool(s["max"]["gains"]) and not s["max"]["out"]
        g1 = bool(s[r["chosen"]]["gains"]) and not s[r["chosen"]]["out"]
        was["gain" if g0 else "none"] += 1
        now["gain" if g1 else "none"] += 1
        if r["chosen"] != "max":
            k = (r["row"]["template"], r["row"]["knob"], r["chosen"], label(s[r["chosen"]]["gains"]))
            moved[k] = moved.get(k, 0) + 1
    none_left = {}
    for r in res:
        s = r["cards"]
        if not (s[r["chosen"]]["gains"] and not s[r["chosen"]]["out"]):
            k = (r["row"]["template"], r["row"]["knob"])
            none_left[k] = none_left.get(k, 0) + 1
    L = ["# The wiring search, development seeds\n", f"> {TOP}\n",
         f"Seeds {seeds[0]}-{seeds[-1]} (development; the preregistered seeds 3000-3009 untouched), {n} muscles, "
         f"{len(cards)} cards, both muscle loads; {elapsed:.0f} s. Evidence class S (our own models). Nothing here changes "
         "the engine: the cards enter it only as the next version, run again on the preregistered seeds.\n",
         "## The rule (fixed before any result was read)\n",
         "1. A card is out if the lease did not hand its knob back on every seed, if under either load it did less work, "
         "more misses or cleared its line later (95% intervals over the seeds, clear of zero), or if it spent more energy "
         "with no gain in work, speed or misses.",
         "2. Gains rank: more work, then faster, then fewer misses, then less energy (the same work, speed and misses on "
         "less energy).",
         "3. The card with the best set of gains is chosen; the max (the engine's default) is kept wherever it gives that "
         "set, so another card replaces it only where it adds a gain the max does not give.",
         "4. A muscle no card improves keeps the max, and says why.\n",
         "## What it found\n",
         "| | Muscles with a gain | Muscles with none |", "|---|---:|---:|",
         f"| The max alone (every muscle on the default card) | {was['gain']} | {was['none']} |",
         f"| Each muscle on its own card | {now['gain']} | {now['none']} |\n",
         "### Muscles given another card\n", "| Template | Knob | Card | Gains | Muscles |", "|---|---|---|---|---:|"]
    L += [f"| {t} | {k} | `{c}` | {g} | {m} |" for (t, k, c, g), m in sorted(moved.items(), key=lambda x: -x[1])]
    L += ["\n### Muscles no card improves\n", "| Template | Knob | Muscles |", "|---|---|---:|"]
    L += [f"| {t} | {k} | {m} |" for (t, k), m in sorted(none_left.items(), key=lambda x: -x[1])]
    L += ["\nEvery muscle, every card: `WIRING_DEV.csv`; the frozen choice: `WIRING_CARDS.json`.\n",
          "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.\n",
          f"---\n\n*{NOTICE}*\n"]
    (out / "WIRING_DEV.md").write_text("\n".join(L))
    return was, now


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, nargs="+", default=DEV_SEEDS)
    ap.add_argument("--cards", default=",".join(ORDER))
    ap.add_argument("--catalog", default=str(ROOT / "realms" / "catalog_v5.csv"))
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--ids", default="", help="muscle ids, comma separated (a look)")
    ap.add_argument("--out", default=str(ROOT / "results" / "development" / "wiring"))
    a = ap.parse_args(argv)
    if PREREG & set(a.seeds):
        print("the wiring search runs on development seeds only (3000-3009 are the preregistered seeds)")
        return 1
    cards = [c for c in a.cards.split(",") if c]
    assert cards[0] == "max" and all(c in CARDS for c in cards), cards
    rows = H.catalog(a.catalog)
    if a.ids:
        want = set(a.ids.split(","))
        rows = [r for r in rows if r["muscle_id"] in want]
    if a.limit:
        rows = rows[:a.limit]
    t0 = time.time()
    with ProcessPoolExecutor(a.workers) as ex:
        res = []
        for i, r in enumerate(ex.map(muscle_cards, [(row, a.seeds, cards) for row in rows], chunksize=2)):
            res.append(r)
            if (i + 1) % 50 == 0:
                print(f"{i + 1}/{len(rows)} muscles, {time.time() - t0:.0f} s", flush=True)
    was, now = write(Path(a.out), res, a.seeds, cards, time.time() - t0)
    print(f"with a gain: max alone {was['gain']} of {len(res)}; each on its own card {now['gain']} of {len(res)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
