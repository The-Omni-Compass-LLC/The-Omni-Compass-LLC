# Omni v1: the frozen engine, and every result checked against it

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Superseded on 2026-10-06 by Omni v2** (`docs/OMNI_V2.md`, `OMNI_V2.json`): the same law, controllers and runners byte
> for byte, with the muscle catalog grown from 656 to 945. Every result in this file is a v1 result and stays one; nothing
> is read across versions.

## What is frozen

Omni v1 is the engine as it stands at commit `a004a8f` and is unchanged through `f162ce8`, with one addition inside the
version: the power-grid runner (`tools/run_pandapower.py`) was written at `8eab01c` without touching any other engine
file. A commit before it holds 37 of the 38 files, every one v1 bytes, and `tools/omni_version.py` says exactly that
("omni-v1 (37 of 38 files, all v1 bytes; not yet in this commit: tools/run_pandapower.py)"): a v1 result for every test
but the power grid, which could not have run there. It covers:

- the compass law (`omnicompass/compass_law.py`);
- the live controllers (`omni_controller/`);
- the realms with their 656 muscles and six organisms (`realms/`);
- the runners of the independent simulators (`tools/run_kil.py`, `tools/run_citylearn.py`, `tools/run_pandapower.py`).

`OMNI_V1.json` holds one SHA-256 for each of these 38 files, plus one digest over all of them: `ccc7fbdf8b312ed7…`.

```
python3 tools/omni_version.py                    # this checkout: prints "omni-v1", or every file that differs
python3 tools/omni_version.py --commit <sha>     # the engine at the commit any result ran on
```

A result counts as a v1 result only if the commit it ran on carries exactly these bytes. Every GitHub Actions run
records its commit, so anyone can check any result in one command.

## What is the same in every muscle, and what is not

The law is one function. It reads the service as a position between calm (0) and its line (1). It pulls the position
toward the middle and pushes against whatever is driving it. Its force is smoothed by tanh, and past the wall it goes
to full force at once. The gains are the same on every muscle: pull 1.0, add 0.10, take back 0.02, release −0.2.

Results differ from domain to domain for three declared reasons, never because the gains were changed per domain:

1. **The machine underneath** (`realms/presets.py`): boot time, idle and peak power, heat capacity, battery size,
   motor torque. These are fixed engineering figures for the class of machine.
2. **The room native leaves.** Omni can only win back what the native controller wastes.
3. **The guard rules each live adapter carries**, all listed in the preregistrations:
   - Kubernetes: rules 1–8 and amendments 9 and 12;
   - the grid: one whole tap per move, and a week of evidence before stepping down.

   Some knobs are left native by a physics test computed from the machine's own figures (`MECHANISM_OF_ACTION.md`
   §9.6), such as a power cap where idle power dominates, or a UPS reserve.

## The change rule

v1 does not change. A new rule, a new gain or a new guard makes a new version (v2) with its own fingerprint, and every
result is run again on it. No result is ever read across versions.

## Every result, by version

**Status of each result**

| Result | Ran on | v1? | v1 run |
|---|---|---|---|
| Kubernetes: fairness (`results/live/FAIRNESS.md`) | `3539036` | no | **A, B, C done: [`V1_FAIRNESS.md`](../results/live/V1_FAIRNESS.md)** |
| Kubernetes: faults (`results/live/FAULTS.md`) | `3539036` | no | **A, B, C done: [`V1_FAULTS.md`](../results/live/V1_FAULTS.md)** |
| Kubernetes: steady (`results/live/STEADY.md`) | `3539036` | no | **A, B, C done: [`V1_STEADY.md`](../results/live/V1_STEADY.md)** |
| Kubernetes: wandering (`results/live/WANDERING.md`) | `3539036` | no | **A, B, C done: [`V1_WANDERING.md`](../results/live/V1_WANDERING.md)** |
| Kubernetes: all four in one run (`results/live/ALL_FOUR.md`) | `3539036` | no | **A, B, C done: [`V1_ALL_FOUR.md`](../results/live/V1_ALL_FOUR.md)**: work inside the line +42% to +48% in all three |
| Kubernetes: batch queue (`results/live/BATCH.md`) | `a0ebaff` | no | **A, B, C done: [`V1_BATCH.md`](../results/live/V1_BATCH.md)** |
| Kubernetes: the six organisms with the real cluster inside (1 to 1,000 copies) | `a004a8f` | **yes** | **done: [`V1_SIX_KUBE.md`](../results/live/V1_SIX_KUBE.md)** (run 37359815637, 98 of 100 cells: 1, 10 and 100 copies of all six and 1,000 copies of the four realms and the tower, 5 paired repetitions each (3 at 1,000); the two 1,000-copy stack cells were cut off by GitHub's six-hour job limit). Every organism: p95 and time over the line GAIN in every cell, 0 gauges LOSS beyond the noise except a rounding-level work loss (−0.0003%) in the 10-, 100- and 1,000-copy cells and HPA replicas +0.7% in one cell; the cluster's machines stay at 6 in both arms (no autoscaler under kind); off the clock (the organism ended more than 5% of the window late, its last steps seeing a cluster at rest) in 2 of 3 repetitions of the Physics realm at 1,000 copies (up to 290 s) and of the tower at 1,000 copies (up to 3,820 s): GitHub's 4-core runners are too slow for those sizes; the pairing stands and the cells are marked |
| Kubernetes: the big organisms (1,000 copies on a rented Azure machine) | `a004a8f` | **yes** | **done: [`V1_BIG_ORGANISM.md`](../results/live/V1_BIG_ORGANISM.md)** (run 37359820055): the tower at 1,000 copies, 3 of 3 repetitions: p95 −95% (4.1 s → 0.2 s) and time over the line −99.7% (64% → 0.2%), both clear of the noise; failed requests 22% → 0 inside the noise; machines 6 in both arms; organism energy −0.2% lower, organism work −0.0% (rounding-level, reads higher); off the clock in repetition 3 (up to 2,392 s past the 2,880 s window, marked); the stack at 1,000 copies, 3 of 3 repetitions from the detached machine (collection run 37575930111, `f162ce8`): p95 −74% (274 ms → 70 ms) and p99 −83%, both clear of the noise; time over the line 0.7% → 0 (inside the noise); machines 6 in both arms; organism energy −0.2% lower, organism work rounding-level lower; the compass arm ended 300 to 615 s after the 2,880 s window in all three repetitions (marked OFF THE CLOCK; native kept the clock), which is why the v3 stack runs with a 10,800 s window |
| Azure AKS steady (`AKS_BILL.md`) | `5b2832f` | no | **done: [`V1_AKS_STEADY.md`](../results/live/V1_AKS_STEADY.md)** (run 37385657374 on `f162ce8`, 5 paired repetitions): no difference beyond the noise on any gauge, the bill −4.7% with its interval across zero; Omni's own CPU 0.014 cores; a single run read by `tools/live_reps.py`'s paired interval, B and C to follow |
| Azure AKS burst | `8199e3a` | no | **done: [`V1_AKS_BURST.md`](../results/live/V1_AKS_BURST.md)** (run 37534538088 on `f162ce8`, **5 paired repetitions**; repetition 4 lost its native cluster to an Azure API error in the first attempt and was run again by itself): the bill +5.0% with its interval across zero, machines, p95 and failed requests (22% → 16%) inside the noise; p99 −34% (6.0 s → 4.0 s) clear of the noise in this one run; a single run read by `tools/live_reps.py`'s paired interval, B and C to follow; the 4-worker fleet cannot show a machine (the fleet runs are next) |
| The 656 muscles and six organisms, modelled (`results/realms/`) | `9c5d417` | **yes** | **A, B, C done**: runs 37359815637's realms check, 37385660330 and 37393204931 each reproduced the published table byte for byte (a deterministic model: reproduced in 3 of 3) |
| The organisms at 1 / 10 / 100 / 1,000 copies, modelled (`results/scale/v1/GRID.md`) | `a8548b6` | no | to run after the six-kube queue clears |
| CityLearn, every district | `ac39b16` | no | **A, B, C done: [`V1_CITYLEARN.md`](../results/live/V1_CITYLEARN.md)** (runs 37384954241, 37393198549, 37399402398): 11 districts with batteries, every score reproduced in 3 of 3 except the comfort score, which CityLearn itself varies between runs; 3 districts with nothing to move; 8 CityLearn cannot run |
| Power grid, pandapower and SimBench | `8eab01c` | **yes** | **A, B, C done: [`V1_PANDAPOWER.md`](../results/live/V1_PANDAPOWER.md)** (runs 37377029333, 37397142210, 37412578757; 11 untouched grids, both load models, every gauge reproduced in 3 of 3): with ZIP loads the energy the loads drew is GAIN in all three of our runs in all 11 grids (−1.3% to −1.5%) and the net import in all 11; losses GAIN in all three of our runs in 7 and power given in 4 (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fewer in 10 grids, 4 → 8 a year in one rural grid (power given in all three of our runs, the declared cost); no grid ever more often outside its band, 2 less often |
| Robot arms, MuJoCo Menagerie (`docs/ROBOTICS_PREREGISTRATION.md`) | new on v1 | **yes** | **A, B, C done: [`V1_MUJOCO.md`](../results/live/V1_MUJOCO.md) (UR5e, iiwa 14, Gen3) and [`V1_MUJOCO_PANDA.md`](../results/live/V1_MUJOCO_PANDA.md) (the tuning robot)**: reproduced in 3 of 3; where Omni moved (Gen3, Panda) the arm hit its points more accurately with less force on its motors inside the same takt: peak torque −29% and −10%, tracking error −21% on both, energy per takt −0.8% and −0.5%, all GAIN in all three of our runs; the Panda's copper loss +14% power given in all three of our runs; UR5e and iiwa left native by the paired physics trial, nothing for Omni to move |
| Databases: PostgreSQL behind PgBouncer, pgbench (`docs/POSTGRES_PREREGISTRATION.md`) | new on v1 | **yes** | preregistered 2026-10-06; the tuning workload runs first, then the three untouched workloads, A, B and C (workflow `pgbench`) |
| GPU, one card and the card in the organisms | earlier card controller | no | new runs on real cards (founder) |
| Muscle studies, power budgets, PlanetLab fleet, tower off and on | September engines | no | marked old |

## How each result is read across three runs

Every v1 benchmark runs three times, as separate GitHub Actions runs on the same frozen bytes:

- **A** is the result.
- **B** and **C** are the replications.

Every judged row gets one of three readings, and all three runs are shown beside it:

- **GAIN** or **LOSS in all three of our runs** (a resource spent that rose reads **power given**, never a loss): the same sign in all three runs, each with its 95% interval clear of zero.
- **No difference beyond the noise**: in at least one run the interval includes zero, so native and omni could not be
  told apart on that measure. That is the result, stated as such, with the count of runs it holds in.
- **The runs disagree**: runs clear of the noise point different ways. The test itself is then unstable on that measure,
  and it is looked into before anything is claimed.

Every row is reported, losses included.

The table is made by rule, never by hand:

```
python3 tools/confirm_abc.py "Steady load" results/live/raw/run-<A> results/live/raw/run-<B> results/live/raw/run-<C> \
    --out results/live/V1_STEADY.md
```

It checks each run's commit against the v1 fingerprint, and heads the table with a warning if any run is not v1 or if the
three are not separate runs. CityLearn has its own table (`tools/citylearn_abc.py`): the simulator is deterministic, so
its three runs must reproduce each other, and a score reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when they do, same under
one part in a million, and "the runs differ" when they do not; a district with no electric battery is listed as nothing
for Omni to move, and a district CityLearn cannot run is listed with CityLearn's own error. `tests/test_confirm_abc.py`, run by `verify.py`, proves the rule: an interval over zero
reads no difference beyond the noise, a flipped sign clear of the noise reads disagreement, a rounding-level change reads
same, and a loss in all three reads higher.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
