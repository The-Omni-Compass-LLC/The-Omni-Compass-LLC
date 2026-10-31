# Omni v18: Omni direct in the engine; the three arms

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v18 (`OMNI_V18.json`, digest `1cb92edb64c4391d`, 62 files) stood on main from 23 October, night, to 25 October, when omni-v19 (`docs/OMNI_V19.md`) landed. The founder's orders of
the same evening: "Native is Kubernetes on the muscles. Omni on native is Omni on top of Kubernetes on top of the muscles. And
then Omni direct is simply Omni on top of the muscles, no Kubernetes ... they all need to be written in code and toned in ...
and push it all"; and, once it was pushed, "It should be not 17 anymore, it should be 18 ... Give me this new live engine wired
up now to where you're at".

omni-v18 is omni-v17 (`docs/OMNI_V17.md`) with Omni direct taken into the engine: the seven files of Omni-Compass's own
orchestrator that hold its rules are fingerprinted like every other wire, so no rule of Omni direct can change without the
version changing (the principle omni-v15 set for the eight wires it took in). 55 of its 62 files are omni-v17's bytes; the
seven new ones are `omni_orchestrator/__init__.py`, `agent.py` (the machine's hand), `brain.py` (the brain), `cgroup.py` (the
walls), `control.py` (the control plane), `front.py` (the front) and `scheduler.py` (the room rule). The showing's workload and
clients (`omni_orchestrator/workload.py`, `load.py`) are the harness and stay outside. A version declared before omni-v18 is read
without the seven (`tools/omni_version.py`, `ORCHESTRATOR_WIRES`), so every earlier commit keeps the version it ran on.

## The three arms

Every organism the orchestrator runs is shown three ways, all three in one showing and every pair read by the one key, paired
by step (`tools/orchestrator_show.py`, `.github/workflows/orchestrator.yml`, `docs/OMNI_ORCHESTRATOR.md`):

| arm | what moves the muscles | brain |
|---|---|---|
| native | Kubernetes' published autoscaling rule, written by us, every machine on, units spread | `yardstick` |
| Omni on native | that rule's units, never fewer; Omni's reflex and fail-up above it; Omni's conveyance, busy room rule, packing and machines on top; no fold, no verdict (the engine's strict form, as on the kind rigs) | `omni_native` |
| Omni direct | Omni alone on the muscles, no Kubernetes: everything Omni on native does, and the fold below the rule's count under the verdict | `omni` |

## What Omni direct carries

Every mechanism in Omni direct's brain is the engine's own, so the same gain goes to Omni on top of native:

- **conveyance** (omni-v7, omni-v13): each unit's processor wall set to the room its machine can spare under 75% busy, shared
  among the service's units there, never under the request, handed back between 70% and 75% and at the top beside another
  workload's room; journaled, written to the hand, read back from the kernel's `cpu.max`;
- **the reflex**: work waiting in line adds as many units as there are requests waiting, up to the step, in the same beat;
- **the twin**: Kubernetes' rule read on the same readings, each unit's use counted no higher than its request, as Kubernetes
  would see it; Omni never holds fewer units than the twin unless the verdict allowed the step;
- **the fold under the verdict** (`omnicompass/verdict.py`): a unit fewer than the twin tried on the service's own response
  times, under the same traffic (a trial whose arrivals move more than 15% is abandoned), kept only where it reads no LOSS
  within 2%; work waiting hands a step back at once (the immune reaction);
- **the hold on trials the traffic keeps abandoning** (new with omni-v18): a trial the traffic abandons holds the next off for
  6 beats, doubled at each abandonment in a row up to the verdict's recheck (24 beats), cleared by a trial judged to its end; a
  phase counts its step from the higher of the twin it found and the twin now. Found on the first three-arm showing, where every
  trial was abandoned yet each held a unit below the twin while it ran (Omni direct against Omni on native, work LOSS, down
  5.2%); fixed before the version landed (`docs/OMNI_ORCHESTRATOR.md`, section 2d);
- **the busy room rule** (omni-v7, `omni_controller/capacity.py`): no unit placed onto a machine at 75% of its measured busy
  share; the units packed onto the fewest machines, machines parked and woken;
- **the journal and the kill switch**: every change journaled before it is acted on and replayed when the control plane starts
  again; the kill switch holds the declared state and hands every conveyed wall back.

## What it read before it landed

Our own showing on one host, class L, one run of each arm (`docs/OMNI_ORCHESTRATOR.md`, sections 2c and 2d):

- **The three arms, quick form** (six steps of 15 s, after the fix): Omni on native against native, work GAIN, up 8.3%; Omni
  direct against native, work GAIN, up 9.1%; Omni direct against Omni on native, the 95th percentile GAIN, down 13.2%, and units
  GAIN, a cut, down 9.5%. No LOSS in any pair; nothing failed or wrong in any arm, the batch job or the drills.
- **Omni direct against native, full form** (18 steps of 25 s): work GAIN, up 4.7%; the 95th percentile GAIN, down 9.9%; units
  GAIN, a cut, down 10.3%; machines STEADY, down 1.7%; 0 failed and 0 wrong in 20,452 requests.

The model gate against omni-v17 (`results/model_gate/V18_VS_V17.md`): every model reads omni-v17's numbers, because none of omni-v17's
55 files moved; the gate's models do not run the orchestrator, whose own gate is the showing above.

And after it landed, the three runs on GitHub's machines (the full form, A, B and C from one commit) read Omni on native against native work GAIN in all three (up 5.2% to 7.4%) and the 95th percentile GAIN in all three (down 7.5% to 12.1%), Omni direct against native work GAIN in all three (up 5.7% to 9.4%) and the 95th percentile GAIN in all three (down 9.8% to 15.7%), machines STEADY, the units power given or STEADY, and Omni direct against Omni on native STEADY on every gauge; no LOSS in any pair in any run (`results/orchestrator/V18_THREE_ARMS_ABC.md`).

## What runs on it

Every benchmark runs again on omni-v18: the conductor's campaign counts from 02:51 UTC on 24 October, when the engine reached main, and only runs whose own commit carries `OMNI_V18.json` (`scripts/dispatch_grid.py`,
`scripts/reruns.txt`), and the clouds' sets run on it once each cloud's own $0 check passes. In the clouds nothing changes: Omni
on top of the cloud's Kubernetes at the tune-down, on the machines alone (the order of 14 October). Omni direct runs on GitHub's
own machines, three runs from one commit (`orchestrator.yml`). Omni direct is ready on a rented machine in each cloud and runs
there only on the founder's word: the test `direct` on the one-machine buttons (`big-organism-detached.yml` on Azure,
`cloud-organism.yml` on Google and Amazon; `scripts/organism_detached.sh`) rents one 8-processor machine, ships it the exact
commit, runs the same full form `reps` times one after another, brings every run's files back and gives the machine back; a
dry run (the default) shows the price and rents nothing. The GPU runs on Lambda start from `gpu-omni-v18`, one exact commit.

## What it does not claim

The three-run reading is the full form on GitHub's machines from one commit, on one host each; no cloud machine has run it yet. The comparison of Omni direct against Kubernetes itself on the kind rig is the next
step. The trade between muscles judged on the organism stays the next version's work, through the model gate. Run and scored by
The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
