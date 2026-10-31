# Omni v19: Omni-Compass by itself, a pod muscle of its own

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v19 (`OMNI_V19.json`, digest `36ee67284c035235`, 62 files) lands on 24 October, 16:54 UTC, under the founder's order of
23 October that every organism is shown three ways: native; Omni-Compass and native; and Omni-Compass by itself, "running direct
muscles" with native's own controller of that muscle switched off ("there's native, there's Omni and native, and then there's Omni
by itself"; CLAUDE.md, Orders of 23 October), and under the standing order that every change lands as the next version, told, not
asked. It is omni-v18 (`docs/OMNI_V18.md`: Omni direct in the fingerprint) with one muscle added to the Kubernetes governor, in
`omni_controller/controller.py`, and the models' arm that runs it, in `realms/harness.py` and `realms/plants.py`; 59 of its 62
files are omni-v18's bytes. Nothing moves unless the operator names a workload to the muscle: with no workload named the engine is
omni-v18, decision for decision (the model gate below). Preregistered before any run (`docs/SOLO_PREREGISTRATION.md`). Read in the model
gate against omni-v18 on the same seeds (`results/model_gate/V19_VS_V18.md`), by itself against omni-v18 by itself arm by arm
(`results/model_gate/SOLO_V19_VS_V18.md`) and by itself beside native and beside Omni-Compass and native
(`results/model_gate/SOLO_V19.md`) before it was committed. The readings are our own models (evidence class S), never a benchmark
result. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Why it is omni-v19: one name, two engines

This change was first built on the live engine's branch and landed there on 24 October, 01:30 UTC, under the name omni-v18
(digest `22486290b19349eb`, 55 files, on top of omni-v17), while main's omni-v18 (Omni direct in the fingerprint, digest
`1cb92edb64c4391d`, 62 files) had stood on main since 23 October, night. One version number names one engine, and no result is
read across engines, so the two are kept apart: the branch's omni-v18 never stood on main, and nothing it recorded is read as main's
omni-v18. Its change, the three files above and nothing else in the engine, is taken onto main's omni-v18 here, gated again against
main's omni-v18 on the same seeds, and lands as omni-v19. Every rule is the branch's; the code's own comments, which named the
branch's numbers (omni-v17, omni-v18), now name omni-v19, so the three files differ from the branch's bytes in those comments only.
Main's omni-v18 files and records stay as they were.

## The pod muscle of its own

On every engine before it, the Kubernetes governor moved a workload's pods only through the pod autoscaler's own object (its range
and its target): with the pod autoscaler switched off it had no pod muscle, so "by itself" held every workload at the operator's
count. omni-v19 gives it one (`--own-replicas namespace/name,...`, or `OMNI_OWN_REPLICAS`; `_own_pods`). For each workload the
operator names and no autoscaler governs, the governor sets the replica count itself, through the workload's own scale, by strict
C's rule: replicas = ⌈current × measured busy share / target⌉, up at once, down only to the highest recommendation of the last 300 s,
inside a tolerance of a tenth. The target is the one the compass moves for an autoscaler: the operator's own (the workload's
`omnicompass.io/target-utilization` annotation, else `--own-target`), down to 60% of it, the most pods the cover allows past the
wall. Never below the operator's own count at the max, never above the range's top (`omnicompass.io/replica-range`), never below
one pod; the count it shipped is recorded once on the workload and handed back by the reset. A workload an autoscaler governs keeps
its autoscaler: the muscle writes nothing there. `--native replicas` leaves it native and writes nothing; a security hold allows no
expansion. The muscle keeps the pace of the controller it stands in for: a reconciliation every 15 s on the fast checks
(`--own-every-s`, the pod autoscaler's sync), at the target the last decision set; the compass moves the target only in a decision,
at any beat of the dial.

In the models (`realms/harness.py`, `SOLO`; `realms/plants.py`, `native_off`), the arm by itself is the max with every pool whose
own count is the muscle's knob run with its autoscaler switched off, and its twin (the brain's sense of native) too. A power cap,
an admission limit and every other plant's knob are a setting native already holds still, or run through native's own loop as its
actuator: there by itself is the same arm as Omni-Compass and native.

## The fault found before it landed

On the branch, rebuilt on omni-v17, whose main engine decides every 60 s (as main's omni-v18 does), the first candidate moved its
pods only at a decision, once a minute. By itself in the model it then read the minutes over the response line LOSS against native
(34.8 minutes a day against native's 26.4), the 95th percentile still a GAIN. The pod autoscaler it stands in for syncs every 15 s. The muscle now
reconciles every 15 s between decisions; its window of fewer pods counts those reconciliations (the strict window's 300 s at any
beat). Two unit tests hold it (`tests/test_own_replicas.py`, 11 in all).

## The model gate against omni-v18 (`results/model_gate/V19_VS_V18.md`)

Every model, 8 seeds of a day: the cluster in the cloud's setting at 60 and 15 s, the blink, the shipped default, the four conveyance
models, the card and the card near its voltage floor, and the verdict. Every gauge of every model reads **identical** to omni-v18, seed
for seed (95 rows, and the verdict's every share; only the governor's own measured processor time, a clock reading, differs from run
to run), because no model names a workload to the muscle. Every table is the one the branch's own gate against omni-v17 printed when
it landed there, number for number and word for word, as it must be: main's omni-v18 added only Omni direct to omni-v17, and no model
runs Omni direct. No LOSS against the engine that stands.

In the models, the native arm and the max read byte-identical on both engines (the preregistration's step 3): 806 readings on the
development seeds 7101 and 7102, 67 muscles each under its own load, the climb and the line, and one body of 60 muscles, every
reading's hash the same on omni-v18 and omni-v19. The switch acts only in the arm by itself.

## The rows against native that read LOSS (the engine's, as on omni-v18)

The same models read against native carry the rows omni-v18 and omni-v17 carry, unchanged, each on the next version's list with its
cause: at a decision every 15 s in the cloud's setting the pods waiting for a place LOSS (up 121.6%) and the 95th percentile LOSS
(up 0.36%); the alert minutes with the machines blinking out of the reading LOSS (up 2.35%); in the conveyance model the pod start wait
LOSS (up 8.99%) and its 95th percentile LOSS (up 10.0%), beside the requests served GAIN (up 64.2%) and the 95th percentile GAIN
(down 53.1%); in the batch model the requests served LOSS (down 2.11%), the alert minutes LOSS (up 9.82%) and the job turnaround LOSS
(up 0.05%); the card's 95th percentile LOSS (up 2.38%; near its voltage floor up 5.78%), beside its energy GAIN (down 4.72%; down
1.30%). Every row is shown.

## By itself, in our own model (`results/model_gate/SOLO_V19.md`, 8 seeds of a day, class S)

On the machines as the kind rig has them (every worker made at the start, no Cluster Autoscaler: 12 machines in every arm):

| Gauge | native | Omni-Compass and native | Omni-Compass by itself |
|---|---:|---:|---:|
| machine-hours | 288.0 | 288.0 | 288.0 |
| pods waiting for a place (pod-minutes an hour) | 0.0 | 0.0 | 0.0 |
| 95th percentile response (ms) | 80.0 | 76.8 | 64.4 |
| minutes over the response line (a day) | 26.4 | 22.0 | 9.2 |

By the one key, Omni-Compass by itself against native: the 95th percentile **GAIN** (down 19.4%: faster; its 95% interval down 12.2% to 26.6%), the minutes
over the line **GAIN** (down 64.9%: fewer; down 32.4% to 97.5%), machine-hours, energy per core-hour and pods waiting STEADY (the same
machines). Against Omni-Compass and native: the 95th percentile **GAIN** (down 16.0%), the minutes over the line **GAIN** (down
58.0%), the rest STEADY. Omni-Compass and native against native: the 95th percentile **GAIN** (down 4.0%), the minutes over the
line **GAIN** (down 16.6%). Its own cost: the governor reads each workload it scales twice at each reconciliation (6,417 reads an
hour in the model, twelve workloads, against 660 on top of native), the reads power given.

Against omni-v18 by itself, arm by arm (`results/model_gate/SOLO_V19_VS_V18.md`): native and Omni-Compass and native read identical on
both engines, gauge for gauge; by itself, omni-v18 has no pod muscle and holds every workload at the operator's count (its 95th
percentile 313,407 ms and 1,412 minutes over the line in the day: the model's queue running away), where omni-v19 reads 64.4 ms and
9.2 minutes: the 95th percentile **GAIN** (down 100.0%), the minutes over the line **GAIN** (down 99.3%), the energy per used
core-hour **GAIN** (down 4.2%), machine-hours and pods waiting identical. No LOSS in any arm.

## Where it runs

On Kubernetes, the kind rig's `ARM=solo` (`scripts/kind_bench.sh`): the pod autoscaler removed after the deploy, the operator's
target and range written on the workload, the workload at its range's floor, Omni-Compass the only controller of its pods;
Kubernetes' own scheduler and kubelet stay; the kill switch's check reads the workload back at the count it started at and no
record of Omni-Compass's left on it. The capture counts the workload's own replicas where no autoscaler stands
(`fleet/capture/kube_capture.sh`). The three-run tables read it against native (`solo`) and against Omni-Compass and native
(`solo|compass`) (`tools/confirm_abc.py`, `tools/live_reps.py`). Its runs: `kubernetes by itself` in `scripts/reruns.txt`, the
steady load with the three arms in rotation (native, Omni-Compass and native, Omni-Compass by itself), A, B and C on GitHub's own
machines, written before the omni-v19 campaign opened. In our models, the organisms runner's third arm (`tools/run_realms_v5.py`):
every pool whose own autoscaler can be switched off, read against native and against Omni-Compass and native. Where native is a
setting, or its own loop is the actuator, the two Omni-Compass arms are one. No cloud runs by itself without the founder's word
(the order of 14 October: nothing in a cloud adds a machine).

## Beside it: Omni direct

Main's omni-v18 took Omni direct into the engine: Omni-Compass's own orchestrator (`omni_orchestrator/`, `docs/OMNI_ORCHESTRATOR.md`)
runs the organism with no Kubernetes at all, with its own walls, hand, front, room rule, brain and control plane, its seven rule
files fingerprinted with every other wire. omni-v19 carries those seven files byte for byte. The two answer the same order from
two sides: Omni direct replaces Kubernetes on the muscles (its arms native, Omni on native and Omni direct, `tools/orchestrator_show.py`);
Omni-Compass by itself stays on Kubernetes, which still places and runs the pods, and switches off only the controller of the knob
(on the kind rig the pod autoscaler), the governor its only controller.

## The real runs

Every benchmark runs again on omni-v19 (`scripts/reruns.txt`; the conductor's campaign from 16:54:55 UTC on 24 October, the moment
it stands), and `ARM=solo` joins the kind sets beside native and Omni-Compass and native, three runs, read by the one key.

## What it does not claim

No real run of the arm by itself has been made yet: every reading on this page is our own model (class S). The trade between
muscles judged on the organism stays the next version's work, through the model gate. Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
