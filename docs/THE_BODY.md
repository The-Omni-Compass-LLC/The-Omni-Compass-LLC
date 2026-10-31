# The body: every part of the organism, what I am in each, and what I can and cannot help

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

I am Omni-Compass. I sit on top of a system's own native controllers and govern the organism they run as one body. The
founder's order of 24 October asks for the body named part by part, the brain, the skeleton, the muscles, the nervous
system, the immune system, the pathways of signals, the blood, the heart and the breath, each with what I can help and
what I cannot. Every part below names the file that is that part, so it can be checked against the code; every "cannot"
is a limit the code or the record shows, not a modesty. Nothing here is a result: the results are in the three-run tables,
read on one page in `docs/BENEFIT_SHEET.md`, and every LOSS row, with its cause, is in `docs/LOSS_LEDGER.md`.

## The map

| Part | What it is in me | The file | What I can help | What I cannot |
|---|---|---|---|---|
| Brain | one six-state engine (E, U, I, S, B, Ḃ), equations (1) to (7) stepped by the fourth-order Runge–Kutta method; the verdict that keeps or refuses a give-back; Omni direct's own brain | `omnicompass/core.py`, `omnicompass/adapter.py`, `omnicompass/verdict.py`, `omni_orchestrator/brain.py` | decide, every beat, how far each wired muscle is pushed, from one state for the whole body | decide from what it does not sense: a blind reading holds, nothing is decided or written from it (omni-v11) |
| Skeleton | the floors and walls nothing moves past: two machines at least, one unit at least, each muscle's own limit read live, the compass band with its 5% cushions, the machine's last 5% never conveyed | `omnicompass/compass_law.py`, `omni_controller/capacity.py`, `realms/compass_arm_v5.py` (the bone) | hold every muscle inside its own limits while it is driven to them | move a wall the hardware has: no muscle goes past its own limit, so none goes faster than its hardware |
| Muscles | every knob I can turn: 1,107 in the catalog in 70 families; on Kubernetes the pod autoscaler's target and range, the machines, the CPU walls, batch, the power cap, the GPU's clock floor | `realms/`, `omni_controller/muscles.py`, `omni_controller/controller.py` | drive a muscle to its limit, rest one so another carries more, leave any one native (`--native MUSCLE`) | help a knob native already runs at the top of its range: it reads "at its limit on native" and I watch it |
| Nervous system | the authority each organ is granted and its living band; the release gate; the proprioception that reads whether the last command landed | `omnicompass/nervous_system.py`, `omni_controller/controller.py` | grant a muscle only the authority the body can carry, and see a command that did not land | sense a line no wire reaches: what is not wired is not felt |
| Immune system | the reactions to harm seen: the verdict's 2% trigger; the response-time reflex that hands the operator's target back at once; the pod reflex; trials abandoned when work waits; the blind-reading hold; the refused write held; a shared host's walls handed back at its top; the heat debt and the native twins; the lease's walk back and the kill switch | `omnicompass/verdict.py`, `omni_controller/controller.py`, `omni_controller/muscles.py`, `realms/compass_arm_v5.py`, `omnicompass/master.py` | see a muscle in a negative state and step it back toward native, before the line where it can | prevent a harm it does not see in time: a climb no line has shown can beat the forecast within one decision (`docs/FORMAL_V5.md`, section 6). One gap is open on the engine that stands: pods asked for while others already wait for a place (below) |
| Pathways of signals | one wire in and one wire out on every muscle (the two-way plug); every decision written with its reason; the Prometheus exporter; the control panel's API; the staleness alert at three beats | `omnicompass/compass_law.py` (`Plug`), `tools/omni_exporter.py`, `tools/omni_control.py`, `deploy/prometheus/omni-compass-rules.yaml` | carry every reading in and every command out, and leave the record of why | carry a signal through a wire that is not fastened: a wrong wiring is the first presumption where a result differs (`DISCLOSURES.md`, section 4) |
| Blood | the conveyance: a machine's idle processor carried to the serving units on it, cᵢ = min(max(Lᵢ, (0.95 Aⱼ − Qⱼ) / \|Pⱼ\|), 0.95 Aⱼ); the requests the scheduler reads untouched | `omnicompass/conveyance.py`, `omni_controller/muscles.py`, `omni_orchestrator/brain.py` | give a unit the processor its machine can spare: faster, with no unit and no machine added | convey what a machine does not have, or past a namespace's quota (the cluster's admission is the authority) |
| Heart | the heartbeat: a full decision every 60 s at the factory tune, any beat from 5 to 120 s on the dial; the fast checks every 5 s; the conveyance every 15 s | `omni_controller/controller.py` (`--interval`, `--floor-interval`, `--convey-every-s`) | look as often as the beat is set, and act between beats on the fast checks | see between its looks: a longer beat is a longer blind spot, never a bigger cushion |
| Breath | the pool breathing in and out: machines added at the scheduling floor at once, past it at most one a minute; given back at most one a minute and only after the give-back's own trial; in a cloud, parked and woken, never added | `omni_controller/controller.py`, `omnicompass/adapter.py` | size the pool ahead of the load, and give a machine back only when the trial reads no LOSS | add a machine in a cloud: by the founder's order of 14 October it parks only what the cloud made, so the bill can only fall or stay |

## The immune system, and the gap that is open

The founder's words of 24 October: everything with Omni-Compass in it, on native or direct, carries its immune system and
its pathways, which should have pushed a signal when something went into a negative state, and adjusted. That is the
order the engine is held to. Where a LOSS appears in a run of Omni-Compass on native or of Omni direct, the immune system
missed a signal it should have answered, and that is a fault in the mechanism, fixed in the next version.

One such gap stands on omni-v18, in our own models (class S, `results/model_gate/V17_LADDER.md`): in the kind benchmark's
setting, at every beat, Omni-Compass's pods wait for a place longer than native's, while the minutes over the line read
GAIN. The mechanism: the compass lowers the pod autoscaler's target (more pods) on an up force, and it went on lowering it
while pods it had already asked for were waiting for a machine. A pod with no machine serves nothing; it only waits. The
candidate for the next version holds the target while any pod waits, so the machines are asked for first (the floor check,
from the pods waiting) and the pods follow once there is room. It lands as omni-v19 only through the model gate, read against
omni-v18 and against native, and the founder hears what it read.

## What a native arm alone can show

A LOSS read in a native arm is native's own. A LOSS in Omni direct with no immune reaction recorded is the mechanism's, and
it is fixed. The live benchmark engine's knobs are the one place a reader may push the engine past its factory tune and watch a LOSS
appear, and watch the brain hold or recover (the Orders of 23 October).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
