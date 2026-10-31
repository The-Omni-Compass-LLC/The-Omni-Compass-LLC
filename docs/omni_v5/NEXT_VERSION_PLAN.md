# The next engine version: what goes in, and in what order

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 13 October 2026 (night), before any of it is built, on the founder's orders of 13 October. The engine that stands
is omni-v5, digest `6093b2b88aa911b9`. Everything below changes the engine, so it lands as the next declared version, and
every benchmark then runs again on it, A, B and C. Nothing here is a result.

## Update, 15 October 2026

The v6 capacity repair and non-GPU rerun campaign are now implemented in `docs/OMNI_V6.md`. The repair does not declare every proposal in this historical plan complete. Google, Amazon and physical GPU launches remain deferred.

## 1. GAIN, STEADY and LOSS as the code that steers the brain

Today the words are in every report (`tools/readings.py`) and the engine already acts on the same aims: the verdict
(`omnicompass/verdict.py`) keeps a step only where the muscle's own cost per piece of work is no higher, and the body's
guard refuses a step that pushes another part past its cushion. The next version makes the three words the brain's own
vocabulary: every gauge a muscle reports carries its declared aim (lower, higher, spent), and every trial is judged in the
words the reports use, GAIN, STEADY, LOSS or power given, for the muscle and for the body. A trial that reads LOSS anywhere is
undone; power given is kept only beside the work or speed it bought. One table of aims serves the brain and the reports, so
they can never disagree.

## 2. The muscles the catalog does not yet name

The catalog holds 1,107 muscles in 70 families. Read against the founder's list, these controls everybody runs are not yet
muscles of their own (each is a setting the native system already exposes to its operator):

| New family or addition | Muscles |
|---|---|
| SCADA and supervisory control | RTU and PLC polling interval (Modbus, DNP3), historian sampling rate, alarm-flood suppression window, supervisory setpoint push rate, OPC UA subscription rate |
| Control loops and estimation | PID gain schedule, setpoint ramp rate, controller output limit, anti-windup clamp, MPC prediction horizon, MPC move-suppression weight, MPC constraint softening, Kalman process-noise scale, estimator innovation gate, sensor-fusion rate |
| LLM and agent orchestration | agent concurrency, tool-call budget, token budget per task, model tier routing, context-cache budget, semantic-cache threshold, retry and timeout policy, parallel tool calls |
| ML optimizers and training schedule | learning-rate scale (Adam and its kin), warm-up steps, learning-rate schedule, gradient clipping, optimizer-state offload, ZeRO / FSDP sharding stage, evaluation interval |
| Cloud management and infrastructure as code | cloud quota guard, cost-budget gate, Terraform / OpenTofu apply parallelism, Crossplane reconcile rate, multi-cloud placement weight |
| Source control and developer platforms | GitLab and Bitbucket runner pools, Git LFS cache, repository mirror sync rate, code-review bot concurrency |

Each is added under the same rule as every muscle before it: tuned on development seeds only, kept only when it wins twice
and never falls behind native on any seed, and placed in every realm that runs that domain.

## 3. The whole tower and the four stacked at 100 copies: the cause found, and the fix

The long-window rerun on GitHub's four-core machine read the tower's 95th-percentile response time +45.9%, a LOSS (run
38423471888). Protocol 3 then gave the organism's model its own core, ten paired repetitions each (runs 38464343379,
38462289297, 38462280620; omni-v5, digest `6093b2b8`). The LOSS stayed, so the model's own processor time is not its cause:

| At 100 copies | 95th percentile | 99th percentile | Time over the line | Failed requests | HPA replicas | Host CPU busy |
|---|---|---|---|---|---|---|
| The whole tower | +47.7%, LOSS | STEADY | -3.2%, GAIN | STEADY | +54% (power given) | 80.4% to 88.6% (+10.1%) |
| The four stacked | +87.2%, LOSS | +32.1%, LOSS | STEADY | STEADY | +47% (power given) | +12.9% |
| The four realms, each | STEADY | STEADY | GAIN in Physics (-3.1%), STEADY in three | STEADY | +40% to +54% | +6.6% to +11.7% |

**The cause.** In both arms the four-core machine was already about 80% busy and the cluster was failing about half of
its requests: the load at 100 copies is beyond what six kind nodes on four cores can serve. The max read the replica
muscle's capacity from the autoscaler's own range and raised the replicas 40% to 54%; the nodes under them could not grow
(kind has no machine autoscaler), so every added pod competed for the same four cores, the host's busy time rose 6.6% to
12.9%, and the tail of the two largest organisms grew. More copies on a saturated host are not more capacity.

**The fix, inside the newest engine** (the founder's rule of 13 October: every muscle up to one click under its own
capacity, read live, and where the brain's own math shares the machine it counts in the body's load): the replica
muscle's live capacity becomes the smaller of its autoscaler range and the headroom of the machines under it, read from
the nodes' own allocatable and used processor (and, under kind, the host's busy share). Where the nodes have no headroom,
the max adds no replica; where a machine autoscaler can add a node, the headroom includes the node it can add. The same
read applies to every capacity muscle that shares a host. It is tested on development seeds and on the kind rig at 100
copies before it is declared, and the founder is told before the version is declared.

**Still to read.** The tower at 100 copies on three eight-core Azure machines (starts 38476930989, 38476939068,
38476947839; about 04:00 to 05:30 UTC on 14 October) shows how much of the LOSS the four-core machine carries; the fix is
made either way, because a saturated host can occur in production too.

## 4. Also in this version (announced earlier)

- The GPU's heat line: never over 83 C, and the headroom under it used where it buys work.
- Micro steps inside each decision (fourth-order Runge-Kutta for the plants' motion, Monte Carlo over their uncertainty).
- The body's hormones and immune system carried into every organism.
- **In a cloud, give back only** (the founder's order of 14 October, night): done from that night with existing settings
  (`OMNI_MACHINES_ONLY=1`: the governor moves the machines alone, the pods exactly native's, so the bill can only fall or
  stay). This version names it as one setting of the governor's own instead of three, so an operator sets it in one word.
  The max keeps its push where the machines are paid for.
- **No alert minute in the cloud** (the founder's order of 14 October, night): a minute over the line wakes a person,
  so the omni arm's alert minutes must read 0. Today the max halved the time over the line on Azure's steady load
  (30.3% to 14.6%, three repetitions of run 38455383137); the minute-by-minute record of that run says where the rest
  sits. The changes, inside the same bill: act on the climb as well as the level, early enough to cover the minutes a
  new machine takes to join; decide every 5 seconds once every rule now counted in decisions counts in seconds (a give-back trial's phase, the breach
  cool-down, cruise, the trial spacing; at 5 s today a trial would be abandoned and the bill could not fall), the fast
  checks on their own clock instead of between decisions, and read the response time
  over a window short enough for the decision to see the climb (today the reading averages the last 60 seconds);
  give the serving pods the idle processor the machines already have. Where native is short of machines, the receipt says how many more keep the line.
- **The chip at native's heat** (the founder's order of 14 October): on a GPU the gain is more work inside the chip at
  native's own temperature, never hotter; the clock and power ceilings move only where the card's heat stays at or
  under native's.

## 5. Every LOSS that stands today, and what this version does about each

The founder's order of 13 October: a LOSS row is never cut; its cause is found and fixed and the test run again. These are
the LOSS rows on the newest tables (the grid page is the card version, digest `5648f290`; the grid on `6093b2b8` is
running now):

| Where | The LOSS | What it shows | In this version |
|---|---|---|---|
| The grid with the cluster inside (`results/grid_v5/GRID.md`) | the organism's work per energy, in 21 of 36 squares of 10 and 100 repetitions | the max gave the organism power (its energy reads power given) and the work waiting in line was done either way, so each unit of work took more energy; the power bought fewer misses (time over the line reads GAIN in all 36) | the decision code counts the body's work per energy as a gauge of its own: a power step that buys no work and no fewer misses is undone; where it buys fewer misses, the step stays only while the body's work per energy stays STEADY, so the row reads STEADY or GAIN |
| The four stacked at 100 copies, 100 repetitions | 95th and 99th percentile response time | the organism ran past its window in 49 of 100 repetitions (up to 635 s): GitHub's four-core machine could not step that many muscles in time | section 3: the cause found (replicas added on a saturated host); the fix is the replica muscle's live headroom |
| The whole tower at 100 copies, 100 repetitions | 95th and 99th percentile response time | the same machine; the long-window rerun read +45.9% at the 95th percentile | section 3: the same cause and fix |
| CityLearn (`results/live/V1_CITYLEARN.md`, `V3_CITYLEARN.md`) | energy not served and time uncomfortable in several districts | older engines' tables; not yet run on omni-v5 | run on this version, A, B and C; a district that still reads LOSS has its cause found before the table goes up |

## 6. Order

1. The runs on the current engine that answer section 3 finish and are read.
2. The version is built and tested on development seeds; the founder is told what changed before it is declared.
3. Declared, then every benchmark runs again on it, A, B and C, on GitHub and on Azure; Google, Amazon and the GPU chips
   wait for the founder's word.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
