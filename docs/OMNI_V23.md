# Omni v23: Omni direct keeps every muscle Omni-Compass cannot be: a knob whose writes are refused goes back to native's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v23 (`OMNI_V23.json`, digest `c96ea4105d8747db`, 65 files) is omni-v22 with one guard in the Kubernetes governor's pod muscle of its
own (`omni_controller/controller.py`, `_own_pods` and `_own_refused`), on the founder's order of 31 October, given on reading that
the arm by itself had read like native:

> "Omni direct is directly to muscles, but Omni direct still might need an autoscaler like Kubernetes ... we still might need a
> muscle or two we're using. We're going straight into all the muscles as the brain and orchestrator, scheduler and all that, but
> what Omni-Compass can't do and needs the muscle for has to be achieved even in direct, so that it can work and do everything else
> ... Don't just embed some shit and fail the whole system because we don't have the muscle to do something ... any muscle that we
> don't have, Omni-Compass cannot be it: it has to be there, if that's Kubernetes or whatever."

64 of its 65 files are omni-v22's bytes. No gain, preset, card or law moves; do no harm keeps its strictest form.

**What "direct" can and cannot mean** (the founder's analysis, the same day: "Omni-Compass would have to become the Kubernetes
mechanism to be what's considered direct"). On a Kubernetes stack Omni-Compass is a brain with no organs: Kubernetes' scheduler
places every pod and the kubelet runs every container, in every arm. The arm by itself there is Omni-Compass's own pod rule in place
of the autoscaler's arithmetic and nothing else, so it is never called direct; it is a mechanism test kept in the record, not a
product arm, and the product has two sides, native and Omni-Compass on native (the founder's order of 25 October). The one test
where the word holds is the orchestrator showing without Kubernetes (`docs/OMNI_ORCHESTRATOR.md`), where Omni-Compass's own small
orchestrator is the organs; its three arms read, run by run: Omni-Compass on native the strongest in all three (the most work, the
fastest response in two, fewer machines in all), native the weakest, the arm by itself between them (level with Omni-Compass on
native in run A, behind it in B and C). This guard serves every arm: wherever Omni-Compass's own rule cannot move a knob, the organ
that can gets it back.

## What was found

Every arm by itself run on kind from omni-v19 (24 October) to omni-v22 had the governor's pod writes refused by the rig's own
identity: `kubectl scale` patches the scale subresource, `deployments/scale`, a resource of its own under Kubernetes' RBAC, and the
rig's role granted `patch` on `deployments` by name and never the subresource. Fifteen of fifteen decisions a window ended
Forbidden, in every repetition; the workload stayed at the operator's count; the machine and conveyance muscles wrote as always, so
the window's no-write check never fired. omni-v21's three runs of the entry were admitted and are read in no table; omni-v22's two
were marked invalid by a second rig fault. Both rig faults are fixed (`docs/SOLO_PREREGISTRATION.md`, amendment 1). What the engine
lacked is this version: when Omni-Compass cannot be a knob's muscle, the knob must go back to the muscle that can, so the organism
never runs with a knob nobody moves (amendment 2, the founder's order above).

## What changes in the engine

- A write of a workload's own scale that the cluster refuses (its permission, its admission, its API) is recorded in the audit
  (`own_replicas`, `refused` n, the cluster's words) and the decision goes on; the cluster keeps the last count that landed. Before
  omni-v23 the exception ended the decision (`decision failed (n in a row)`) and nothing else happened, decision after decision.
- At `OWN_REFUSALS` (3) refusals in a row Omni-Compass cannot be that knob's muscle: it makes native's own pod autoscaler from the
  operator's own target and range recorded on the workload (`kubectl autoscale deployment NAME --cpu-percent=T --min=lo --max=hi`;
  with no range recorded, from one to ten times the operator's count), audits the hand-back (`handed_back`, `after_refusals`,
  `target`, `range`), and leaves the workload to it for the rest of the run: the snapshot's governed set holds it from the next
  decision on, and the reset leaves native's autoscaler standing. A hand-back the cluster refuses too is audited
  (`hand_back_refused`) and tried at the next refusal.
- A write that lands ends the run of refusals.
- Every other arm is untouched: Omni-Compass on native never removes native's controller, so a refused write there leaves native's
  own controller moving the knob as before; the machines, the conveyance, the power cap and the batch muscles are omni-v22's bytes.

## What changes in the rig, not the engine

The kind identity (`deploy/kind/rbac-omni.yaml`) gains `create` on `horizontalpodautoscalers` in the default namespace, for the
hand-back alone, and the preflight proves it; a window of the arm by itself in which the knob was handed back is refused as a
result of that arm (the organism was kept whole, but Omni-Compass did not run the arm by itself): `INVALID RUN: by itself, the knob
... was handed back to native's own autoscaler`. `tests/test_kind_rig_rbac.py` fails a rig without either.

## The model gate

`results/model_gate/V23_VS_V22.md` (class S, our own models; `tools/model_gate.py`, seeds 1 to 8, the engine that stood, omni-v22,
the candidate omni-v23): every one of the 95 gauge rows of the 11 models reads identical on every seed, the counts identical, no LOSS. No model refuses a write of the cluster, so the guard never fires in the models and the
candidate reads identical to omni-v22 on every gauge; its proof is the tests below and the arm's own files when the entry runs again.

## The tests

`tests/test_own_replicas.py`, `HandBack`: a cluster that refuses the scale write three times in a row gets native's own autoscaler
at the operator's 50% target and 1 to 10 range, the muscle writes nothing more to that workload, the count the cluster kept stands
(never a knob nobody moves); a write that lands after two refusals ends the run of refusals and no autoscaler is made; with no range
recorded the autoscaler's ceiling is ten times the operator's count. The unit-test suite, the function tests and the release check
pass on the tree; no C++ twin changes (the Kubernetes governor has none).

## What is run again

Every benchmark runs again on omni-v23 from 20:00 UTC on 31 October 2026 (`scripts/reruns.txt`, A of every entry, then B, then C; the conductor's
campaign, `scripts/dispatch_grid.py`). The omni-v22 runs started before that moment run to their end as omni-v22's record; nothing is
cancelled. The entry `kubernetes by itself` runs on the rig as amended, three arms, its table kept in the record and not carried on
the front page (the founder's order of 25 October).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
