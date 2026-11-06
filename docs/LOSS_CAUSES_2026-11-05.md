# The omni-v25 batch queue's LOSS rows, read from their own files: 5 November 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The omni-v25 campaign's three-run tables landed on 5 November (`results/live/V25_*.md`). Every row is in them and in the LOSS
ledger (`docs/LOSS_LEDGER.md`), and no cause written for an older engine is carried onto an omni-v25 row unread
(`tools/loss_ledger.py`, `WRITTEN_FOR`). This page reads the one LOSS that runs through the batch tables, the queue finishing
later, from the runs' own files on the branch `raw`.

## 1. The plain batch stream: the queue finished later in all three runs

`results/live/V25_BATCH.md`, runs 41753030885, 41768876462, 41781968016. The row: batch: queue finished, 2.6%, 2.7% and 2.9%
later than native (17.6 s, 17.8 s and 18.3 s), each run's 95% interval clear of zero. On omni-v21 the same row read STEADY,
under the floor (0.13%).

**What Omni-Compass did during the queue.** Nothing to the machines, the pods or their limits. Its writes, from its own audit
(`audit.jsonl`, run 41753030885, repetitions 1 to 3): the service's rollout paused in the first 12 s (the step before an
in-place resize), then nothing until the queue's last seconds: the limits it handed back came at 716.6 s against a queue of
716 s, at 726.3 s against 730 s and at 582.6 s against 578 s, and the node pool it parked after the queue's end. All six
workers stood in service through the queue in both arms (`capture.csv`).

**What it cost.** The governor's own processor. Its audit's overhead record reads 134.8, 157.4 and 111.0 processor-seconds in
windows of 1,514, 1,523 and 1,491 s: 0.089, 0.103 and 0.075 of a core on average. On omni-v21 at the 60 s beat the same record
read 20.0, 22.2 and 23.6 processor-seconds in 1,441 s: 0.014 to 0.016 of a core (run 40230821800). The factory beat on site is
10 s since omni-v24 (`docs/OMNI_V24.md`), so the governor reads and decides six times as often, and its own work rose about six
times with it.

**Why that lands on the queue.** On GitHub's runner every kind node and the governor share the same four cores, and this rig
gives the governor no core of its own (`scripts/kind_bench.sh` pins it only where a batch scheduler is installed). The batch
pods are bound by the runner's processor: the pods used about 3.6 of the four cores through the queue (`capture.csv`, the used
column), so a governor using 0.09 of a core takes about 2.5% of the batch pods' processor, the size of the queue's rise. At
omni-v21's 0.015 of a core the same arithmetic gives 0.4%, under the floor, which is what that table read.

**Where it lives.** In the engine's own load on a shared machine. On a real cluster the governor runs on its own machine and the
workers do not pay for its reads; on this test machine they do. The founder's order of 13 October stands over it: where the
brain's own math shares the machine, it counts in the body's load. The engine that stands does not yet count its own processor
when it sets its beat.

**What decides it.** The next version, through the model gate first: the governor's own processor counted in the body's load
on a shared host, so its beat costs the organism less than the floor; then the benchmark's three runs on that engine.

## 2. The batch schedulers: the queue finished later on most rigs (suspected, not yet measured)

The four ways through the KAI scheduler, Kueue, Volcano, the bin-packing profile, KubeRay, Gödel, Karmada, Open Cluster
Management and Armada, and the batch stream through each scheduler (`results/live/V25_<SYSTEM>_4W_<WAY>.md`,
`results/live/V25_<SYSTEM>.md`), read the queue finishing later with Omni-Compass on top on most rigs, and the jobs' turnaround
longer; on the KAI scheduler's four ways, 1.0% to 2.8% later in all three runs, with the turnaround 5% to 14% longer.

On these rigs the governor has its own core (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 5), so its own processor does not
come out of the pods' cores. The control plane that answers its reads does: the API server runs in the kind control-plane node,
on the cores the batch pods use, and at the 10 s beat the governor asks it for the cluster six times as often as at 60 s.
That is the suspected cause, and it is not yet measured: these runs record the governor's processor, not the control plane's.
omni-v12's four ways at the 60 s beat read the KAI scheduler's queue LOSS by the mean of its three runs as well, so the beat is
not the whole of it.

**What decides it.** The control plane's processor read beside the queue in the next runs, and the next version through the
model gate (the same count of the governor's own load, its reads included).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
