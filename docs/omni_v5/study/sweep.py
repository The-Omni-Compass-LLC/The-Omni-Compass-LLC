# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Load sweep (scratchpad only): the compute organism driven at escalating offered load, native vs Omni dial settings.
# How much more work the same machines serve inside the SLO as the load is pushed up, and the chip-life spent doing it.
import json
import sys

sys.path.insert(0, "/tmp/claude-0/-home-user-The-Omni-Compass/62f07a71-ec25-5fa1-9ae1-91807798a833/scratchpad/v5wt")
import realms.harness as H
from realms.plants import ComputePool
from tools.run_scale import rows_for, ORGS
import maxarm as M


def chip_temp(th_raw):
    return 35.0 + 50.0 * th_raw                 # idle ~35 C, full load ~85 C (near a GPU's slowdown point)


def run(rows, seed, arm, load, dial="balanced"):
    b = H.Body(rows, seed)
    for p in b.plants:                          # offered load scaled up across the organism
        if isinstance(p, ComputePool):
            p.lam = [x * load for x in p.lam]
    pools = [i for i, p in enumerate(b.plants) if isinstance(p, ComputePool)]
    temps = {i: [] for i in pools}
    kill_at = int(H.KILL_AT * H.ORGANISM_STEPS)
    for k in range(H.ORGANISM_STEPS):
        b.couple()
        if arm == "max":
            for p, knob in zip(b.plants, b.knobs):
                if k >= kill_at:
                    p.override = {}
                    continue
                p.override = M.max_override(p, knob, dial) if isinstance(p, ComputePool) else {}
        b.step()
        for i in pools:
            temps[i].append(chip_temp(b.plants[i].th))
    for p in b.plants:
        p.finalize()
    work = sum(b.plants[i].m["work"] for i in pools)
    viol = sum(b.plants[i].m["viol"] for i in pools)
    steps = sum(b.plants[i].m["steps"] for i in pools)
    energy = sum(b.plants[i].m["energy_j"] for i in pools)
    machines = sum(max(1, int(round(b.plants[i].n))) for i in pools)
    life = sum(M.life_used(temps[i], b.plants[i].P["dt"]) for i in pools)
    return dict(work=work, miss=100.0 * viol / steps, energy=energy, machines=machines, life=life)


def main():
    org = sys.argv[1] if len(sys.argv) > 1 else "1"
    key = ORGS[org][0]
    rows = rows_for(key, 1)
    seeds = [7000 + i for i in range(int(sys.argv[2]) if len(sys.argv) > 2 else 2)]
    loads = [1.0, 1.5, 2.0]
    arms = [("native", None), ("max", "balanced"), ("max", "edge"), ("max", "sprint")]
    out = {}
    for load in loads:
        agg = {}
        for arm, dial in arms:
            name = arm if dial is None else f"max:{dial}"
            rs = [run(rows, s, arm, load, dial or "balanced") for s in seeds]
            agg[name] = {k: sum(r[k] for r in rs) / len(rs) for k in rs[0]}
        out[load] = agg
        row = "  ".join(f"{n} w{agg[n]['work']/1e6:.1f}M miss{agg[n]['miss']:.2f} life{agg[n]['life']:.0f}" for n in agg)
        print(f"{key} load x{load}: {row}", flush=True)
    json.dump(out, open(f"sweep_{key}.json", "w"))


if False:
    pass


if __name__ == "__main__":
    main()
