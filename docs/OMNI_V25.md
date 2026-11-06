# Omni v25: the Kafka wire's producer started before the governor's thread; a stalled producer stops its workload, never the job's clock

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v25 (`OMNI_V25.json`, digest `cf56fc0a7b707452`, 65 files) is omni-v24 with one fault fixed in the Kafka wire
(`tools/run_kafka.py`, one of the eight runners in the fingerprint since omni-v15) and one comment corrected in the Kubernetes
governor (`omni_controller/controller.py`). No rule, gain, guard, preset, card or law moves; do no harm keeps its strictest form;
the governor's decisions are byte for byte omni-v24's. On the founder's standing order that every fault found is fixed and lands
as the next version, told, not asked, and his order of 3 November ("go into the GitHub ... grade and see where it's at ... keep
pushing").

## The fault

From omni-v22 (30 October) no Kafka run on GitHub finished. Every workload's job ran to its 150-minute limit inside "Run the
workload, native and omni" and handed in nothing; from 2 November, 20:03 UTC, 16 runs in a row ended so (runs 168 to 183 of the
`kafka` workflow; run 41601163807 is one), where omni-v21's took 14 to 32 minutes a workload (run 40400868003). The job's own log
could not say where it stood: the runner wrote its progress only to a file the job uploads.

Reproduced here on Kafka 3.9.1 as the workflow installs it (one KRaft broker, `kafka-python-ng`; the light workload, one
repetition, 5 s a notch): the native arm finished; in the omni arm the producer process was single-threaded and waiting on a
futex, before it had opened its log or sent a message, the main process waited on it, and the governor's audit read no arrivals
for 540 s, when the load lasts 75 s.

The cause: a fork copies only the thread that calls it. From omni-v22 the governor's thread opens its own Kafka client at its
start (the reader of each partition's arrivals, `Offsets`, the twin's input), while the main thread forks the producer an
instant later. A lock that thread holds at that instant (its first import of the client, its first connection) stays held in
the child for ever, and the producer blocked on it. The native arm has no governor's thread, so it never stalled, and omni-v21's
governor opened no client of its own, so it never stalled either.

## What changes

- The producer is forked before the governor's thread starts (`run_arm`); the Kafka client is loaded once, in the main thread,
  before any thread or child starts (`run_workload`).
- A producer still running 120 s past its own schedule is stopped and its workload fails with the reason (`join_producer`,
  `PRODUCER_GRACE_S`), in the arms and in the capacity reading, so a stalled child can never again hold a job to its time limit.
- The governor's decisions are untouched: 53 of the wire's 58 definitions are byte-identical to omni-v24's, the brain (`Brain`),
  its twin (`RateTwin`), the decision rule (`decide`), the governor's loop (`Omni`), the arrivals' reader (`Offsets`), the group,
  the producer and the consumers among them; the three that change (`run_arm`, `capacity`, `run_workload`) start and wait on
  processes, and the two added (`join_producer`, `PRODUCER_GRACE_S`) bound that wait.
- `omni_controller/controller.py`: a comment named the omni-v23 ladder's file (`V23_LADDER.md`, read on the model's faulty
  stand-in) where it means the corrected one (`V23_LADDER_CORRECTED.md`); no statement moves.

Outside the engine, with it: `.github/workflows/kafka.yml` prints the runner's progress into the job's log as it runs, so a
stall shows where it stands.

## The model gate

The model gate against omni-v24 (`results/model_gate/V25_VS_V24.md`, class S, our own models; `tools/model_gate.py`, seeds 1 to 8,
the standing engine omni-v24 and the candidate this tree): all twelve models identical to omni-v24 on every gauge and every seed,
104 readings and none different, so no LOSS against omni-v24. The Kubernetes governor's one change is a comment. The Kafka wire's
decisions are the same code as omni-v24's (53 of its 58 definitions byte-identical, every one the governor decides with), and what
changed (when its processes start, how long the main thread waits on the producer) is not a decision any model or replay of the
archived seconds reads; the closed-loop Kafka model (`tools/kafka_model.py`) gates a change in the decisions against the omni-v21
loop and has nothing to read here.

The same light workload on the candidate, on the same broker: both arms finished, the omni arm's every message consumed and every
consumer handed back at its end (a check of the repair on one repetition, not a benchmark result).

## What is run again

Every benchmark runs again on omni-v25 from 21:00 UTC on 3 November 2026 (`scripts/reruns.txt`, A of every entry, then B, then C; the conductor's
campaign, `scripts/dispatch_grid.py`), Kafka among them for the first time since omni-v21. The omni-v24 runs started before that
moment run to their end as omni-v24's record; nothing is cancelled.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
