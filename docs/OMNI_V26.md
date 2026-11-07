# Omni v26: another workload's waiting pods hold native's target; the fail-up no longer flips with a batch queue

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v26 (`OMNI_V26.json`, digest `75d3c22eed4473b9`, 65 files) is omni-v25 with one fault fixed in the Kubernetes governor
(`omni_controller/controller.py`). Do no harm keeps its strictest form. On the founder's standing order that every fault found is
fixed and lands as the next version, told, not asked, and his order of 6 November ("Just get everything else push, and push").

## The fault

Read from the omni-v25 runs' own files (`docs/LOSS_CAUSES_2026-11-06.md`). On the batch rigs a batch queue shares the cluster with
the web service, and its pods wait, on and off, as its normal queueing. While the web service is past its line, the governor's
decision chooses between the cover's floor for its autoscaler target (30%, more pods: the fail-up) and native's own target (50%):
the fail-up only while no pod in the cluster waits, native's target otherwise. The count of waiting pods is the whole cluster's by
design, since a pod of any workload waiting means the room is spoken for and Omni-Compass's extra pods may not hold it.

The rule that keeps native's target while pods wait is the immune hand-back's hold (omni-v19: ten minutes, doubled for each hold
in a row). Only the fast check started it, and only while the target still stood below native's. The decision had already put the
target back at native's by then, so the hold almost never started, and the next decision that found no pod waiting failed up again.
On the KAI scheduler's four ways the target flipped 304 times over 30 repetitions, and the hold caught on 21 times. Kubernetes'
autoscaler takes a lower target at once and a higher one only after its five-minute window, so the flips kept extra web pods in
room the queue was owed: in the 15 repetitions where the queue ran long, it finished 0.1% to 6.8% later, and the web service's
minutes at 1 to 5 s lasted as long. On every batch rig read, the more the target flipped, the larger the web service's rise.

## What changes

- When the decision returns a service's target to native's because pods wait while the target stood below native's, and some of
  the waiting pods are another workload's, it starts the hand-back's hold itself (`_hold_for_waiting`), on the hand-back's own
  clock. The fail-up is then not taken again while the hold runs.
- Another workload's waiting pods (`_others_waiting`): every Pending pod that is not one of the service's own (its scale target's
  selector) and not a DaemonSet's. A DaemonSet's pod belongs to its node: it waits for a machine that is joining, never for another
  workload's room, so a machine being added never starts the hold. Where the selector cannot be read, every other waiting pod counts.
- Where only the service's own new pods wait (a machine still coming for them), the decision keeps omni-v25's rule unchanged.
- The snapshot hands its pod list on (`snapshot`, `pods`), so the rule reads the pods the decision already read: no extra list.

## The tests and the model gate

`tests/test_neighbour_hold.py`: a web service past its line beside a batch queue whose pods wait on and off, through the governor's
whole decision on the stand-in cluster. omni-v25 writes the target 30, 50, 30, 50, 30; omni-v26 writes 30, 50 and holds. A new
machine's DaemonSet pod never starts the hold, another governed service's waiting pods keep omni-v25's rule, and so do the
service's own.

The model gate against omni-v25 (`results/model_gate/V26_VS_V25.md`, class S, our own models; `tools/model_gate.py`, seeds 1 to 8):
all twelve models identical to omni-v25 on every gauge and every seed, 104 readings and none different, so no LOSS against omni-v25. In them the decision's new branch never fires: in the cloud and on-site cluster models every waiting pod belongs to a service an autoscaler governs, and the conveyance, card and verdict models never reach the decision.

A first form of the change counted another governed service's waiting pods as well. The gate refused it: in the cloud model at a decision every 15 s the 95th percentile read up 2.7%, beyond the seeds' noise, and at 60 s the pods waiting up 0.8% by the mean, because one service's new pods waiting for a machine started the hold for another. That form is not in omni-v26; the form that stands leaves another governed service to its own rule, the fast check's hand-back of omni-v19. A DaemonSet's pod, which waits for a machine that is joining, never starts the hold either (a refinement written before the gate's final run, held by its own test).

The batch queue's replay (`results/model_gate/V26_BATCH_FLIP.md`, class S, `tools/batch_flip_model.py`): the native arm's own
timelines of the KAI scheduler's four ways (30 repetitions: the cluster's waiting pods and the web service's 95th percentile),
replayed open loop through both governors at the factory beat on site. The writes of the web service's target fell from 16.13 to
2.67 a repetition (GAIN, down 83.5%), the changes of the target after the first from 15.20 to 1.73 (GAIN, down 88.6%), and the
seconds the target stood below native's while another workload's pods waited from 22.17 to 4.83 (GAIN, down 78.2%); the holds
started rose from 0.03 to 1.43 (power given: the hold is the fix itself). Open loop, it reads the decision rule alone; the service's
and the queue's own gauges are read only by the benchmarks' runs.

## What is run again

Every benchmark runs again on omni-v26 from 14:31 UTC on 7 November 2026 (`scripts/reruns.txt`, A of every entry, then B, then C; the conductor's campaign,
`scripts/dispatch_grid.py`). The omni-v25 runs started before that moment run to their end as omni-v25's record; nothing is
cancelled.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
