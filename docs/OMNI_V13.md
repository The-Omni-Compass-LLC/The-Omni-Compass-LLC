# Omni v13: no other muscle's room is conveyed (the engine that stood 20 to 21 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v13 stood on main from 20 to 21 October; on 21 October Omni v14 (`docs/OMNI_V14.md`) took its place, which is omni-v13
with a knob for every muscle and the operator's commands run without a shell. This page stays as omni-v13's record, read beside no other engine's. The founder's order behind
it, of 19 October, night: every fault found is
fixed, and every fix is the next version, told, not asked. It is omni-v12 (`docs/OMNI_V12.md`) with one fault fixed, found on
the omni-v12 runs of KubeRay's rig on 20 October: the governor's conveyance, which hands a machine's idle processor to the
serving pods on it, kept handing it on a shared host after the host had none left, and the batch muscle beside the web paid.
Every setting, gain, preset and muscle is omni-v12's, and so is every rule but this one.

Its fingerprint is `OMNI_V13.json` (digest `0088837333c6f0fc`, 47 files). Forty-six files are omni-v12's bytes; one differs, the governor's muscles
(`omni_controller/muscles.py`). The change was proven in its tests (`tests/test_convey_handback.py`) and in the model gate before
it landed (`results/model_gate/V13_VS_V12.md`). Every benchmark runs again on omni-v13, A, B and C. Every earlier table stands as
its own engine's result until its three runs on v13 land, and results from two versions are never pooled. The readings from
the model gate below are our own models (evidence class S), never a benchmark result. Run and scored by The Omni-Compass LLC's
own code. No outside party has reviewed or approved these results.

| # | Change | Where | The fault it fixes |
|---|---|---|---|
| 1 | On a shared host (kind) at its top (busy at or over 75%), while another workload there has room of its own (a pod, not a serving one, whose limit is above its request), every limit given goes back to the operator's; it is conveyed again only under 70%, the band's 5% cushion below the top | `omni_controller/muscles.py`, the conveyance | KubeRay's rig, the organism alone (`results/live/V12_KUBERAY_4W_BARE.md`): the web pods' limits were raised to 3,700m in the queue's first half minute and kept through the saturated queue; the batch queue finished 0.6% to 0.8% later and the web's 99th percentile rose 4% to 13%, LOSS in all three runs |
| 2 | Every other pod on a machine is counted by what it may use: its own limit where it has one, its request where it has none | the same | omni-v12 counted requests alone, so a batch pod's room between its request (500m) and its limit (1 core) read as idle and was conveyed |

## 1. What the KubeRay runs show

The table's two LOSS rows were first put down to the give-back, the governor parking machines during the queue (the batch
preregistration, amendment 10). The repetitions' own files say otherwise (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 11).
Twenty-nine paired repetitions of the organism alone, A, B and C:

- **The cost sits where the host was saturated.** In 16 repetitions the native queue ran past 760 s: the runner's processor was
  slower and the batch filled the kind cores (the host's busy share 0.78 through the queue, 95% of readings at or over 0.75).
  There, each batch pod hashed its work in 63.1 s with Omni-Compass on top against 59.2 s natively, **+7.6%**, and the queue
  finished 1.1% later. In the other 13, where the host kept room, the same pods read +0.3% and the queue +0.1%.
- **No machine was parked during a saturated queue.** Six workers were in service through the queue in both arms in all 16;
  the machines Omni-Compass gave back were given back after the queue. The give-back is not the cause.
- **The web's limits were raised at the queue's start and kept.** In 15 of the 16 the conveyance raised the web pods' limits
  to 3,700m at 33 s (one at 65 s), on a reading of the host's busy share averaged over the 15 s since the governor's previous
  reading, which caught the dip as the stream's first pods started. From then on the host was at its top, so omni-v7's guard
  held every further raise, but limits already given stayed, for 92% to 96% of the queue.
- **The web gained nothing while the queue ran.** Pooled over the 29 repetitions, the web's median while the queue ran was
  266 ms with Omni-Compass on top against 253 ms natively, its 99th percentile 3,429 ms against 3,226 ms, and the requests
  served the same (14,454 against 14,480). After the queue, with the host free, the conveyance did what it is for: the median
  fell from 114 ms to 69 ms and the 99th percentile from 194 ms to 113 ms.

So the lifted quota bought the web no processor on a host with none to spare (the kernel shares a saturated host by the
weights of the requests, and the web's share there sat under its operator's limit), and the batch pods lost work per processor
second while it was lifted. One saturated repetition had no raise during its queue and still read +4.0% on hashing: one
repetition is not a reading, and the omni-v13 runs read what remains of the governor's other costs on the shared cores.

## 2. The rule

A limit above the operator's is idle processor conveyed. On a host at its top there is none, and what the serving pods take
there beyond their operator's limit can only come out of what another muscle may use. omni-v13 hands it back. The hold is on a
shared host only, where the nodes are containers on one machine and the machine's busy share is read directly; on separate
machines each node's own arithmetic bounds the conveyance, now with every other pod counted by its limit, so every muscle on
the machine can reach its own limit at the same moment as the serving pods reach theirs. A host where no other workload has
room of its own (a web-only rig: system pods with no CPU limit, or a limit equal to the request) keeps omni-v7's rule: raises
held at the top, limits given stay, because what the serving pods use there is the host's own idle and no other muscle's room.
A host whose busy share cannot be read is blind, never at its top (omni-v11): raises held, nothing handed back. The audit names
each hand-back (`"convey": "handed back"`) and each write gives the reason and the host's busy share.

## 3. The model gate against omni-v12

`results/model_gate/V13_VS_V12.md` (seeds 1 to 8). A new model, `convey_batch`, sets the batch muscle of KubeRay's rig beside the
serving one on the batch rig's host: the kind nodes on 3 of 4 cores and the governor on the fourth, the stream of 24 jobs
(one every 30 s, ten pods each, five at a time, 500m requested and a 1-core limit), each pod's work set so the native queue
finishes where the saturated runners' did (834 s), the processor shared between cgroups by the weights of their requests, the
pods' measured start lag (2.66 s) and the governor's own windowed reading of the host. The batch pods' loss of work while a
serving pod's quota is lifted on a host at its top is the saturated repetitions' own (+7.6% hashing time, 0.071 of the work).

Against omni-v12, on the same seeds, **no reading is a LOSS in any model**:

- The three cluster models (a decision every 60 s, every 15 s, and with the machines blinking out of the reading) and the
  verdict model at 20 and 200 pieces of work a decision: identical to omni-v12 on every gauge, to the last digit. The cloud
  setting conveys nothing, and the verdict is omni-v11's byte for byte.
- The three web-only convey models (the quota readable and empty, unreadable, and refusing every raise): identical on every
  gauge. No other workload there has room of its own, so omni-v7's rule holds unchanged.
- `convey_batch`: against omni-v12, the batch queue finishes **1.48% sooner** and the job turnaround is **9.59% shorter**
  (GAIN), the web's 95th percentile **17.4% lower**, the requests served 0.43% more, the pod start wait 1.46% shorter, the
  commands written 15% fewer, the CPU given 1.2% less and the host's busy share 0.5% less (GAIN); the pod-seconds +0.84%,
  power given; the alert minutes identical.

Against native in `convey_batch`, omni-v12 read LOSS on six gauges: the queue +1.50%, the job turnaround +10.7%, the 95th
percentile +14.8%, the requests served −2.5%, the pod start wait +1.9% and the alert minutes +9.8%. omni-v13 reads the queue
identical to native's, the 95th percentile (−5.3%) and the start wait STEADY, and three LOSS rows. The job turnaround +0.05%
(0.04 to 0.17 s a job): the queue's first reading spans the seconds before the batch pods ran, so the web's limits are raised
once and handed back 15 s later; the rule that closes it is on the next version's list. The requests served −2.1% and the
alert minutes +9.8%: both engines read the same way with no batch at all on this 3-core host, while the real KubeRay runs
served 4% more after the queue, so the model's web model is out of its regime there (section 4). These are our own models,
class S.

## 4. What stays omni-v12's

Every other engine file, rule, gain, preset and muscle; the verdict (`omnicompass/verdict.py`) byte for byte; the refused-raise
hold; the swarm's reflex. The next version's list (`docs/CHANGE_CONTROL.md`) carries what is still to fix, with one item added:
the model's web model on the batch rig's 3-core host, where both engines read fewer requests served than native (section 3)
while the real runs read more after the queue, is to be brought to that host's regime from a real run's files.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
