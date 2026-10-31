# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every muscle its own card: the automatic search that finds each muscle's own settings for the max
(realms/muscle_cards_v5.csv, docs/FORMAL_V5.md section 5). Development seeds only; the preregistered seeds 3000-3009 are
never read here.

  search    every muscle whose settings can change what the max does (a machine pool's edge utilisation and window, a
            battery's line margin and window, an axis's heat head and strain) tries every candidate on the seeds, both of
            its loads; today's global setting is always one of them. A candidate is kept only if it beats the global
            setting beyond the noise on those seeds (fewer misses, more work or faster, each a 95% interval of the paired
            difference clear of zero) and moves none of the three the other way against it, and never falls behind
            native: on no seed and under no load over its line more often, doing less work or clearing its line later. Among those, the fewest misses,
            then the most work, then the fastest, then the least energy.
  confirm   each kept card against the global setting again, on other development seeds, under the same rule.
  write     the cards that won on both sets of seeds, into realms/muscle_cards_v5.csv (a muscle without a row runs the
            global setting).
  organisms the organisms on three loads with the cards and without, every plant against native.
  report    results/cards_v5/CARDS.md from the files the steps above wrote.

  python3 tools/tune_cards.py search    --seeds 7100 7110 --out results/cards_v5/search_7100.json [--wide]
  python3 tools/tune_cards.py confirm   --search results/cards_v5/search_7100.json --seeds 7200 7210 \\
                                        --out results/cards_v5/confirm_7200.json
  python3 tools/tune_cards.py write     --search results/cards_v5/search_7100.json --confirm results/cards_v5/confirm_7200.json
  python3 tools/tune_cards.py organisms --seeds 7200 7210 --out results/cards_v5/organisms_7200.json
  python3 tools/tune_cards.py report"""
from __future__ import annotations

import argparse
import collections
import csv
import itertools
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from realms import harness as H, compass_arm_v5 as L      # noqa: E402
from tools import run_realms_v5 as RR                      # noqa: E402

PREREG = set(range(3000, 3010))
WTOL = 1e-4          # less work than native beyond this share is a harm (tests/test_compass_arm_v5.py)
CATALOG = ROOT / "realms" / "catalog_v5.csv"
COLUMNS = ["muscle_id", "muscle", "template", "knob", *L.CARD_KEYS]


def candidates(row, wide=True):
    """The settings a muscle may choose from (today's global setting among them); none where the max writes nothing a
    setting can change (a room alone, a process loop, every knob native already runs at its limit)."""
    t, k = row["template"], row["knob"]
    if t == "compute_pool" and k in ("capacity", "setpoint"):
        eu = (0.70, 0.75, 0.80, 0.85, 0.90, 0.95) if wide else (0.85, 0.90, 0.95)
        ws = (10, 20, 40, 60) if wide else (10, 20, 40)
        return [dict(edge_util=e, window=w) for e, w in itertools.product(eu, ws)]
    if t == "energy_storage" and k == "power":
        zs = (0.0, 0.5, 1.0, 2.0, 3.09) if wide else (1.0, 2.0, 3.09)
        ws = (3, 5, 10, 20) if wide else (5, 10, 20)
        ms = (0.0, 0.02, 0.05, 0.10) if wide else (0.0, 0.05, 0.10)
        return [dict(line_z=z, hold_window=w, hold_margin=m) for z, w, m in itertools.product(zs, ws, ms)]
    if t == "energy_storage" and k in ("setpoint", "capacity"):
        zs = (0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.09, 4.0) if wide else (1.0, 1.5, 2.0, 2.5, 3.09, 4.0)
        return [dict(line_z=z) for z in zs]
    if t == "motion_axis" and k == "capacity":
        return [dict(heat_head=h, strain=s) for h, s in itertools.product((0.8, 0.9, 0.95), (0.5, 0.7, 0.9))]
    return []


def global_of(row):
    """Today's global setting, in the shape of the muscle's candidates."""
    g = L.V5CFG
    t, k = row["template"], row["knob"]
    if t == "compute_pool":
        return dict(edge_util=g.edge_util, window=g.window)
    if t == "energy_storage" and k == "power":
        return dict(line_z=g.line_z, hold_window=g.window if g.hold_window is None else g.hold_window,
                    hold_margin=g.hold_margin)
    if t == "energy_storage":
        return dict(line_z=g.line_z)
    return dict(heat_head=g.heat_head, strain=g.strain)


def evaluate(row, params, seeds):
    """Both loads of one muscle alone with one card: per load the per-seed contrasts against native, and the label."""
    H.CARDS.clear()
    H.CARDS[row["muscle_id"]] = dict(params)
    try:
        by = {ld: RR.muscle_load(row, seeds, ld) for ld in RR.MUSCLE_LOADS}
    finally:
        H.CARDS.clear()
    gains, losses = set(), set()
    for o in by.values():
        g, l = RR.gains_losses(o["per_seed"])
        gains.update(g)
        losses.update(l)
    valid = all(o["valid"] for o in by.values())
    label = ("INVALID" if not valid else (RR.BOTH if gains else RR.AWAY) if losses else
             (" + ".join(g for g in RR.GAINS if g in gains) if gains else "SAME"))
    per = {ld: [{k: c.get(k) for k in ("work", "viol_pp", "speed", "energy")} for c in o["per_seed"]]
           for ld, o in by.items()}
    # do no harm, seed by seed: a seed and load on which the card is over its line more often than native, does less work
    # (beyond a ten-thousandth) or clears its line later is a harm whatever the mean says (the engine's own no-harm tests)
    harms = sum(1 for o in by.values() for c in o["per_seed"]
                if c["viol_pp"] > 1e-12 or c["work"] < -WTOL or (c.get("speed") or 0.0) > 1e-12)
    return {"params": dict(params), "label": label, "per": per, "seed_harms": harms}


def beats(c, d):
    """Card c against the global setting d on the same seeds: (a GAIN somewhere beyond the noise, a LOSS somewhere); the
    aims: fewer misses, more work, faster."""
    toward = away = False
    for ld in c["per"]:
        a, b = c["per"][ld], d["per"][ld]
        pairs = (("viol_pp", -1), ("work", 1)) + ((("speed", -1),) if all(x.get("speed") is not None for x in a + b)
                                                  else ())
        for key, aim in pairs:
            m, lo, hi = H.interval([x[key] - y[key] for x, y in zip(a, b)])
            toward |= (hi < -1e-12) if aim < 0 else (lo > 1e-12)
            away |= (lo > 1e-12) if aim < 0 else (hi < -1e-12)
    return toward, away


def score(c):
    """The order the search keeps (lowest first): the misses (summed over loads), then less work, then slower, then more
    energy."""
    s = [0.0, 0.0, 0.0, 0.0]
    for a in c["per"].values():
        n = len(a)
        s[0] += sum(x["viol_pp"] for x in a) / n
        s[1] -= sum(x["work"] for x in a) / n
        if all(x.get("speed") is not None for x in a):
            s[2] += sum(x["speed"] for x in a) / n
        s[3] += sum((x.get("energy") or 0.0) for x in a) / n
    return tuple(s)


def _search_job(args):
    row, seeds, wide = args
    cands = [evaluate(row, p, seeds) for p in candidates(row, wide)]
    g = global_of(row)
    d = next(c for c in cands if c["params"] == g)
    ok = [c for c in cands if c is not d and RR.kind_of(c["label"]) not in (RR.AWAY, RR.BOTH, "INVALID") and c["seed_harms"] == 0]
    win = [c for c in ok if (lambda bw: bw[0] and not bw[1])(beats(c, d))]
    best = min(win, key=score) if win else None
    return {"muscle_id": row["muscle_id"], "muscle": row["muscle"], "template": row["template"], "knob": row["knob"],
            "global": g, "global_label": d["label"], "card": best["params"] if best else None,
            "card_label": best["label"] if best else None, "candidates": len(cands)}


def _confirm_job(args):
    row, card, seeds = args
    d = evaluate(row, global_of(row), seeds)
    c = evaluate(row, card, seeds)
    toward, away = beats(c, d)
    return {"muscle_id": row["muscle_id"], "card": card, "card_label": c["label"], "global_label": d["label"],
            "toward": toward, "away": away, "seed_harms": c["seed_harms"],
            "won": toward and not away and RR.kind_of(c["label"]) not in (RR.AWAY, RR.BOTH, "INVALID") and c["seed_harms"] == 0}


def _seeds(a):
    s = list(range(a.seeds[0], a.seeds[1]))
    if set(s) & PREREG:
        sys.exit("the preregistered seeds 3000-3009 are never used to choose a card")
    return s


def cmd_search(a):
    seeds = _seeds(a)
    rows = [r for r in H.catalog(str(CATALOG)) if candidates(r, a.wide)]
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(_search_job, [(r, seeds, a.wide) for r in rows], chunksize=2))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump({"seeds": seeds, "wide": a.wide, "muscles": res}, open(a.out, "w"), indent=1)
    t = collections.Counter((r["template"], r["knob"], "own card" if r["card"] else "global") for r in res)
    for k, v in sorted(t.items()):
        print(*k, v)


def cmd_confirm(a):
    seeds = _seeds(a)
    s = json.load(open(a.search))
    if set(seeds) & set(s["seeds"]):
        sys.exit("a card is confirmed on seeds other than the ones it was chosen on")
    rows = {r["muscle_id"]: r for r in H.catalog(str(CATALOG))}
    jobs = [(rows[m["muscle_id"]], m["card"], seeds) for m in s["muscles"] if m["card"]]
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(_confirm_job, jobs, chunksize=2))
    json.dump({"seeds": seeds, "search": a.search, "muscles": res}, open(a.out, "w"), indent=1)
    t = collections.Counter("won again" if r["won"] else ("LOSS against the global setting" if r["away"] else "STEADY with the global setting")
                            for r in res)
    print(dict(t))


def cmd_write(a):
    s = json.load(open(a.search))
    c = {m["muscle_id"]: m for m in json.load(open(a.confirm))["muscles"]}
    out = []
    for m in s["muscles"]:
        if m["card"] and c.get(m["muscle_id"], {}).get("won"):
            out.append({"muscle_id": m["muscle_id"], "muscle": m["muscle"], "template": m["template"], "knob": m["knob"],
                        **{k: m["card"].get(k, "") for k in L.CARD_KEYS}})
    with open(a.cards, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(f"{a.cards}: {len(out)} muscles with a card of their own; every other muscle runs the global setting")


def _organism_job(args):
    name, rows, seed, load, use = args
    H.CARDS.clear()                                  # (a worker runs many jobs: the cards are set afresh for each)
    if use:
        H.CARDS.update(L.load_cards())
    ids = ([f"{r['muscle_id']}@{realm}" for realm, rs in zip(RR.REALMS, rows) for r in rs] if name == H.STACK
           else [r["muscle_id"] for r in rows])
    nat = RR.organism_run(name, rows, seed, "native", load)
    mx = RR.organism_run(name, rows, seed, "v5", load)
    return {"organism": name, "seed": seed, "load": load, "cards": use, "harms": RR.plant_harms(mx, nat, ids),
            "viol_native": sum(p["viol"] for p in nat["plants"]), "viol_max": sum(p["viol"] for p in mx["plants"]),
            "work_native": sum(p["work"] for p in nat["plants"]), "work_max": sum(p["work"] for p in mx["plants"]),
            "energy_native": sum(p["energy_j"] for p in nat["plants"]),
            "energy_max": sum(p["energy_j"] for p in mx["plants"]),
            "steps": sum(p["steps"] for p in nat["plants"]), "restore_ok": mx["restore_ok"]}


def cmd_organisms(a):
    seeds = _seeds(a)
    rows = H.catalog(str(CATALOG))
    orgs = {realm: [r for r in rows if realm in r["realms"].split(";")] for realm in RR.REALMS}
    orgs[H.STACK] = [orgs[realm] for realm in RR.REALMS]
    orgs[H.TOWER] = rows
    jobs = [(n, rs, s, ld, use) for n, rs in orgs.items() for ld in RR.ORGANISM_LOADS for s in seeds
            for use in (False, True)]
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(_organism_job, jobs))
    json.dump({"seeds": seeds, "cards": len(L.CARDS), "runs": res}, open(a.out, "w"), indent=1)
    agg = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in res:
        g = agg[(r["organism"], r["load"], r["cards"])]
        for k in ("viol_native", "viol_max", "steps", "work_native", "work_max", "energy_native", "energy_max"):
            g[k] += r[k]
        g["harms"] += len(r["harms"])
    print(f"{'organism':30} {'load':6} {'misses native':>13} {'global':>8} {'cards':>8} {'harms':>7} "
          f"{'power given g/c':>17}")
    for (n, ld) in sorted({(n, ld) for n, ld, _ in agg}, key=lambda x: (str(x[0]), x[1])):
        g0, g1 = agg[(n, ld, False)], agg[(n, ld, True)]
        st = g0["steps"]
        print(f"{RR.NAMES.get(n, n)[:30]:30} {ld:6} {g0['viol_native'] / st * 100:12.3f}% "
              f"{g0['viol_max'] / st * 100:7.3f}% {g1['viol_max'] / st * 100:7.3f}% "
              f"{int(g0['harms']):3}/{int(g1['harms']):<3} "
              f"{(g0['energy_max'] / g0['energy_native'] - 1) * 100:+7.3f}%/{(g1['energy_max'] / g1['energy_native'] - 1) * 100:+.3f}%")


def _org_rows(path):
    d = json.load(open(path))
    agg = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in d["runs"]:
        g = agg[(r["load"], r["cards"])]
        for k in ("viol_native", "viol_max", "steps", "work_native", "work_max", "energy_native", "energy_max"):
            g[k] += r[k]
        g["harms"] += len(r["harms"])
        g["runs"] += 1
    return d["seeds"], agg


def cmd_report(a):
    from tools.legal import stamp
    out = ROOT / "results" / "cards_v5"
    s = json.load(open(out / "search_7100.json"))
    c = json.load(open(out / "confirm_7200.json"))
    won = {m["muscle_id"] for m in c["muscles"] if m["won"]}
    kinds = collections.OrderedDict()
    for m in s["muscles"]:
        k = kinds.setdefault((m["template"], m["knob"]), collections.Counter())
        k["searched"] += 1
        k["won once"] += bool(m["card"])
        k["won twice"] += m["muscle_id"] in won
    md = ["# Every muscle its own card: the search, the confirmation and the bodies", "",
         "The engine's cards (`realms/muscle_cards_v5.csv`) and how they were found (`tools/tune_cards.py`,",
         "`docs/FORMAL_V5.md` section 5). Development seeds only: chosen on seeds "
         f"{s['seeds'][0]}-{s['seeds'][-1]}, confirmed on seeds {c['seeds'][0]}-{c['seeds'][-1]}; the preregistered seeds",
         "3000-3009 were never read. A card is kept only if it read GAIN against today's global setting on both sets (fewer",
         "misses, more work or faster, beyond the noise), read LOSS on none of the three, and never fell behind native: on no",
         "seed of either set and under no load over its line more often, doing less work or clearing its line later (the key",
         "to the words: `docs/HOW_TO_READ_THE_RESULTS.md`). Evidence class **S** (modelled).", "",
         "| Plant | Knob | Muscles searched | Won on the first seeds | Won again (the engine's cards) |",
         "|---|---|---:|---:|---:|"]
    tot = collections.Counter()
    for (t, k), n in kinds.items():
        md.append(f"| {t} | {k} | {n['searched']} | {n['won once']} | {n['won twice']} |")
        tot.update(n)
    md += [f"| **All** | | **{tot['searched']}** | **{tot['won once']}** | **{tot['won twice']}** |", ""]
    chosen = collections.defaultdict(collections.Counter)
    for m in s["muscles"]:
        if m["muscle_id"] in won:
            for key, v in m["card"].items():
                chosen[(m["template"], key)][v] += 1
    md += ["**What the cards chose** (the number of muscles at each setting; the global setting in brackets):", ""]
    g0 = L.V5CFG
    glob = {"edge_util": g0.edge_util, "window": g0.window, "line_z": g0.line_z,
            "hold_window": g0.window if g0.hold_window is None else g0.hold_window, "hold_margin": g0.hold_margin}
    for (t, key), cnt in sorted(chosen.items()):
        md.append(f"- {t}, {key} ({glob.get(key, '')}): " + ", ".join(f"{v:g}: {n}" for v, n in sorted(cnt.items())))
    md += ["", "**Inside the organisms** (every plant against native; misses: the share of plant decisions over their",
          "line, removed against native, in percentage points):", "",
          "| Seeds | Load | Misses removed, global setting | Misses removed, cards | Plants with less work or more misses, global / cards | "
          "Power given, global / cards |", "|---|---|---:|---:|---:|---:|"]
    for f in ("organisms_7100.json", "organisms_7200.json"):
        seeds, agg = _org_rows(out / f)
        for ld in RR.ORGANISM_LOADS:
            g, k = agg[(ld, False)], agg[(ld, True)]
            md.append(f"| {seeds[0]}-{seeds[-1]} | {ld} | {(g['viol_native'] - g['viol_max']) / g['steps'] * 100:.3f} | "
                     f"{(k['viol_native'] - k['viol_max']) / k['steps'] * 100:.3f} | {int(g['harms'])} / {int(k['harms'])} | "
                     f"{(g['energy_max'] / g['energy_native'] - 1) * 100:+.3f}% / {(k['energy_max'] / k['energy_native'] - 1) * 100:+.3f}% |")
    md += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."]
    (out / "CARDS.md").write_text("\n".join(stamp(md)) + "\n", encoding="utf-8")
    print(out / "CARDS.md")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("search", "confirm", "organisms"):
        p = sub.add_parser(name)
        p.add_argument("--seeds", type=int, nargs=2, required=True, metavar=("FIRST", "END"))
        p.add_argument("--out", required=True)
        p.add_argument("--workers", type=int, default=4)
        if name == "search":
            p.add_argument("--wide", action="store_true", help="the wider candidate set (beyond the first edges)")
        if name == "confirm":
            p.add_argument("--search", required=True)
    sub.add_parser("report")
    p = sub.add_parser("write")
    p.add_argument("--search", required=True)
    p.add_argument("--confirm", required=True)
    p.add_argument("--cards", default=str(L.CARD_FILE))
    a = ap.parse_args(argv)
    {"search": cmd_search, "confirm": cmd_confirm, "write": cmd_write, "organisms": cmd_organisms,
     "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    main()
