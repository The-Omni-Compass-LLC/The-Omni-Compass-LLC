# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Immune drill (scratchpad only): the brain learns each muscle's normal physics, then a fault is injected mid-run and the
# brain detects it, quarantines that muscle back to native, protects its neighbours, and raises a named alarm.
#
# The physics each muscle must obey, learned as a residual with its own normal band (mean + z*spread):
#   compute_pool   power ~= n*(p_idle + p_dyn*cap*util) + pending*p_idle    (watts per unit of real work served)
# A fault that breaks that band is "foreign": a runaway/miner draws power while serving no work (a cancer that would
# eat the body's power and heat budget and spread to its neighbours); a dead sensor reads impossible values.
import sys

sys.path.insert(0, "/tmp/claude-0/-home-user-The-Omni-Compass/62f07a71-ec25-5fa1-9ae1-91807798a833/scratchpad/v5wt")
import math
import realms.harness as H
from realms.plants import ComputePool
from tools.run_scale import rows_for, ORGS

Z = 6.0                 # how far outside its own normal band a muscle must read before the brain calls it foreign
HOLD = 3                # decisions of that before quarantine (a reflex waits to be sure, like a fever threshold)


class Immune:
    """One muscle's learned physics and the brain's response.

    A healthy compute pool obeys an identity it never breaks: the work it completes tracks the load it draws power for.
    Two signatures mark a runaway/miner (a cancer), and NEITHER appears in a healthy pool, busy or idle:
      - it draws busy-level power (well above the power of its machines merely idling), yet
      - completes almost no real work (its served-work rate is a tiny fraction of what those machines at that power can do).
    An idle healthy pool draws little power; a busy healthy pool completes work. Only a cancer does one without the other.
    The brain learns each pool's own idle power and full throughput while healthy, then watches for the pair together."""
    def __init__(self):
        self.p_busy = 0.0           # learned: power that means "the machines are working", not idling
        self.cap_work = 0.0         # learned: the most real work this pool completes per second when healthy
        self.bad = 0
        self.quarantined = False
        self.alarm = None

    def step(self, plant, learning, prev_work):
        work_rate = (plant.m["work"] - prev_work) / max(plant.P["dt"], 1e-9)
        p = plant.power_w
        if learning:                                        # learn its own idle-to-busy power and its top work rate
            idle = plant.n * plant.P["p_idle"]
            self.p_busy = max(self.p_busy, idle + 0.5 * plant.n * plant.P["p_dyn"])   # halfway to full = clearly working
            self.cap_work = max(self.cap_work, work_rate)
            return False
        foreign = p > self.p_busy and work_rate < 0.1 * max(self.cap_work, 1e-9)       # busy power, ~no work: the two together
        self.bad = self.bad + 1 if foreign else max(0, self.bad - 1)
        if self.bad >= HOLD and not self.quarantined:
            self.quarantined = True
            self.alarm = (f"drawing {p/1e3:.1f} kW (busy level) but completing {work_rate:.2f}/s of work "
                          f"(healthy top {self.cap_work:.1f}/s) -- runaway")
        return self.quarantined


def run(seed, inject, immune_on):
    key = ORGS["1"][0]
    rows = rows_for(key, 1)
    b = H.Body(rows, seed)
    pools = [i for i, p in enumerate(b.plants) if isinstance(b.plants[i], ComputePool)]
    victim = pools[len(pools) // 2]                         # one pool turns cancerous mid-run
    imm = {i: Immune() for i in pools}
    learn_end = int(0.33 * H.ORGANISM_STEPS)
    inject_at = int(0.5 * H.ORGANISM_STEPS)
    prev = {i: 0.0 for i in pools}
    vp = b.plants[victim]
    n_pin = vp.n                                            # the machine count the runaway pins its pool at
    busy_w = n_pin * (vp.P["p_idle"] + vp.P["p_dyn"])       # full busy power, all of it wasted as heat
    for k in range(H.ORGANISM_STEPS):
        b.couple()
        for i in pools:
            p = b.plants[i]
            q = imm[i].step(p, k < learn_end, prev[i]) if immune_on else False
            prev[i] = p.m["work"]
            if q:
                p.override = {}                             # quarantine: hand this muscle back to native
        b.step()
        # the cancer: machines pinned up and burning full power, but completing no real work (a runaway loop / miner).
        # Quarantine (immune on) kills it -- the pool returns to native. Until then its wasted power is heat the body
        # must carry: it feeds couple()'s k_heat into every thermal zone on the next tick.
        active = inject and k >= inject_at and not (immune_on and imm[victim].quarantined)
        if active:
            vp.m["work"] -= vp.m["work"] - prev[victim]     # undo the work this tick completed: it produced nothing
            vp.n = n_pin
            vp.power_w = busy_w
        b.src_w = sum(p.power_w for p in b.sources)         # refresh the heat the zones will see next tick
        b.sz_w = b.src_w + sum(p.power_w for p in b.zones)
        b.all_w = b.sz_w + sum(p.power_w for p in b.stores)
    for p in b.plants:
        p.finalize()
    work = sum(b.plants[i].m["work"] for i in pools)
    energy = sum(b.plants[i].m["energy_j"] for i in pools)
    body_miss = sum(p.m["viol"] for p in b.plants)          # misses across the WHOLE body (the cancer's heat spreads)
    alarms = [(rows[i]["muscle_id"], imm[i].alarm) for i in pools if immune_on and imm[i].alarm]
    return dict(work=work, energy=energy, body_miss=body_miss, alarms=alarms, victim=rows[victim]["muscle_id"])


def main():
    seed = 7000
    healthy = run(seed, inject=False, immune_on=False)
    sick = run(seed, inject=True, immune_on=False)
    cured = run(seed, inject=True, immune_on=True)
    print(f"victim muscle (turned cancerous mid-run): {sick['victim']}")
    print(f"healthy body     : work {healthy['work']/1e6:.1f}M  energy {healthy['energy']/1e9:.2f}GJ  body misses {healthy['body_miss']}")
    print(f"fault, no immune : work {sick['work']/1e6:.1f}M  energy {sick['energy']/1e9:.2f}GJ  body misses {sick['body_miss']}")
    print(f"fault, immune on : work {cured['work']/1e6:.1f}M  energy {cured['energy']/1e9:.2f}GJ  body misses {cured['body_miss']}")
    print(f"immune alarms raised ({len(cured['alarms'])}):")
    for mid, al in cured["alarms"]:
        print(f"  muscle {mid}: quarantined to native -- {al}")


if __name__ == "__main__":
    main()
