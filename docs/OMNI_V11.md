# Omni v11: a reading with no machine in service is blind, never an overload (the engine that stood 18 to 19 October)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v11 stood on main from 18 to 19 October; on the night of 19 October Omni v12 (`docs/OMNI_V12.md`) took its place, which
is omni-v11 with a refused raise held and the swarm's reflex acting at once. This page stays as omni-v11's
record, read beside no other engine's; its 23 three-run tables (`results/live/V11_*.md`) are its own. The founder's order behind
it: every fault found is fixed, none set aside. It is omni-v10 (`docs/OMNI_V10.md`) with one guard added to the Kubernetes governor. When the cluster's reading shows no
machine in service, the governor holds. It records why, decides nothing from that reading, writes nothing, and keeps the last
reading that had machines. Every setting, gain, preset and muscle is omni-v10's, and so is every rule but this guard.

Its fingerprint is `OMNI_V11.json` (digest `745aa53ec8eeb67b`, 47 files). Forty-six files are omni-v10's bytes; one differs, the
Kubernetes governor (`omni_controller/controller.py`). The change was proven in a unit test that reproduces the fault and in the
model gate before it was pushed. Every benchmark runs again on it. Every earlier table stands as its own engine's result until its
three runs on v11 land, and results from two versions are never pooled. Run and scored by The Omni-Compass LLC's own code. No
outside party has reviewed or approved these results.

| # | Change | Where | What it does |
|---|---|---|---|
| 1 | A decision whose reading shows no machine in service holds: it is recorded as held, with its reason, and nothing is decided from it or written | `omni_controller/controller.py`, the decision | the engine is never fed a load measured against no capacity; the decision never divides by zero |
| 2 | The fast floor check returns at once on the same reading | `omni_controller/controller.py`, the floor check | no machine is added from a blind reading |
| 3 | The last reading with machines stays the one the conveyance is bounded by | `omni_controller/controller.py` | a blind moment never lifts the bound on the CPU each pod may be given |

## 1. The fault, found in a real run

In the omni-v10 CruiseKube test (run 39120444653, repetition 8, the arm with Omni-Compass on top), every worker of the kind
cluster left service for two minutes. All six workers sit as containers on one GitHub runner. Eight of the capture's readings
show no machine in service, while the service answered every one of its probes (no failed request in any minute of the window).
In that reading the machines' capacity was zero. omni-v10's governor fed the engine a load measured against that zero capacity,
read as the highest overload its scale allows (a load ratio of 2). It then divided by the capacity when it computed the machine
floor. Two of its fifteen decisions and one floor check ended in a division by zero. Each wrote nothing, as the audit shows,
and the cluster kept the settings it had. But the engine's own state had been given a false overload. The words of the rig
named neither: they said the governor was not running.

omni-v11 reads such a reading as blind. The engine is not stepped, the floor is not computed and no machine is added. The audit
says "held: the cluster's reading shows no machine in service; nothing decided, nothing written". When the machines return, the
next decision reads them and the governor takes up where it was. `tests/test_blind_reading.py` builds the same cluster:
two workers serving, then both out of service in the reading. On omni-v10 both of its tests end in the division by zero; on
omni-v11 both pass, with no write and no error.

The rig was repaired beside it (no engine file; `docs/K8S_COMPASS_PREREGISTRATION.md`, amendment of 18 October). A window whose
capture shows no machine in service is refused in either arm, because its machine count is wrong. A failed decision is named by
its error. The capture records each node's taints and conditions at the moment it sees no machine in service.

## 2. The model gate

The candidate was run against omni-v10 on seeds 1 to 8 in our own models (`tools/model_gate.py`; `results/model_gate/V11_VS_V10.md`),
on every model: the cluster at a decision every 60 s and every 15 s, the new blink model, conveyance with the quota readable and
unreadable, and the verdict on noisy work. This is the first gate in which each arm is proven to import its own checkout's
engine. From omni-v9's gate on, the gate had put its own tree first, so both arms ran the candidate; omni-v9 and omni-v10
changed no file a model runs, so their readings hold by construction, and each page carries the correction.

| Model | Gauges identical to omni-v10 | Decisions that failed (omni-v10 / omni-v11) | Decisions held (omni-v10 / omni-v11) |
|---|---:|---:|---:|
| the cluster, a decision every 60 s | 6 of 6 | 0 / 0 | 0 / 0 |
| the cluster, a decision every 15 s | 6 of 6 | 0 / 0 | 0 / 0 |
| the blink: every machine out of service in the reading for 2 minutes every 6 hours | 6 of 6 | 64 / 0 | 0 / 64 |
| conveyance, the quota readable | 8 of 8 | (no decision of the governor) | |
| conveyance, the quota unreadable | 8 of 8 | (no decision of the governor) | |
| the verdict on noisy work | 5 of 5 | (no decision of the governor) | |

Every gauge and every count is identical. A decision that failed and one that held both write nothing, so nothing the models
measure moves; what moves is the record (a reason where there was an error) and the engine's own state, which a blind reading
no longer reaches. Against native, the two engines read the same, and four rows read LOSS in both: the pod start wait under
conveyance (+9.0% mean, +10.0% at the 95th percentile), the pending-pod minutes and the response time at a decision every 15 s
(+111.7%, +0.33%; no run decides that often), and the alert minutes in the blink model (+2.35%). They are not this change's; they
are the next version's work, in the gate first. The first is the test machine, not the governor: the model's pod start time was
fitted to the empty-node image unpacking of the single kind host (`docs/POD_START_WAIT.md`, section 8), and the kind rig now
pre-pulls the image. These are our own models (class S), never a benchmark result.

## 3. What runs again on it

Everything runs again, A, B and C, from the moment v11 lands (`scripts/reruns.txt`, the omni-v11 campaign, released by the
conductor a few at a time each tick). The grid runs on its own manifest (`results/grid_v11/`), and every Azure set starts again
from A. The omni-v10 runs already started run to their end as omni-v10's record; nothing is cancelled, and no table pools the
two. Google Cloud and Amazon run the same four sets from A once their queues are switched back on (Google's key stored whole,
Amazon's account on its Paid plan). The GPU runs on Lambda wait for the founder's word and one exact commit.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
