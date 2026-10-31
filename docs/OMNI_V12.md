# Omni v12: a refused raise is held, and the swarm's reflex acts at once (the engine that stood 19 to 20 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v12 stood on main from 19 to 20 October; on the evening of 20 October Omni v13 (`docs/OMNI_V13.md`) took its place, which
is omni-v12 with the conveyance's hand-back. This page stays as omni-v12's record, read beside no other engine's. The founder's
order behind it, of the night of 19 October: "Of course I want you to land version 12. I want you to keep fixing and building
and straightening and enhancing and benchmarking and defensibility, and every time you do that ... it becomes a new version." It is omni-v11 (`docs/OMNI_V11.md`) with two faults fixed, both found on
the omni-v11 runs on 19 October: one in the Kubernetes governor's conveyance, one in the swarm's wire. Every setting, gain,
preset and muscle is omni-v11's, and so is every rule but these two.

Its fingerprint is `OMNI_V12.json` (digest `d38b58fbe28939b8`, 47 files). Forty-six files are omni-v11's bytes; one differs,
the governor's muscles (`omni_controller/muscles.py`). The swarm's wire (`tools/run_swarm.py`) sits outside the fingerprint's
scope, as the data-store wires do (it is versioned by git and tested); its change is declared here as part of omni-v12, and a
swarm table counts only on a commit that carries it. Both changes were proven in their tests and in the model gate before they
landed (`results/model_gate/V12_VS_V11.md`, `results/model_gate/V12_SWARM_REFLEX.md`). Every benchmark runs again on omni-v12, A, B
and C, from the conductor's campaign of 20 October, 00:30 UTC. Every earlier table stands as its own engine's result until its
three runs on v12 land, and results from two versions are never pooled. The readings below are our own models (evidence class
S), never a benchmark result. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these
results.

| # | Change | Where | The fault it fixes |
|---|---|---|---|
| 1 | A raise the cluster's admission refuses is not written again until the pod's limit changes, the raise shrinks, or a wait passes (5 minutes, doubled at each refusal up to an hour) | `omni_controller/muscles.py`, the conveyance | omni-v11 capacity test: admission refused every CPU-limit raise (`exceeded quota: omni-cap`) and the governor wrote it again at every fast check, about 9 refused writes a minute, 970 to 1,000 an hour (`results/STEERING.md`) |
| 2 | The swarm's proximity reflex hands back the planner's cruise in the tick it is triggered; its reach grows with the square of the speed (0.5 m at the planner's cruise, as before) | `tools/run_swarm.py`, `Drone.step` | the omni-v11 reflex let the override fall 0.01 a tick, so a drone kept flying fast about a second after it saw a neighbour; on one mission draw outside the counted cells two drones came within 0.083 m (`results/model_gate/V12_SWARM_REFLEX.md`) |

## 1. The refused raise

On the kind rig the governor's role cannot read the namespace's quota. As written since omni-v7, an unreadable quota is "no
budget known", and the cluster's admission is the authority. In the omni-v11 capacity test admission refused each raise; the
refusal was read back and audited, so nothing wrong was ever set, and the table read STEADY. But the governor asked again at every
fast check: a controller that repeats a refused command every few seconds loads the API server and fills its own audit. In
omni-v12 the refusal is the authority's answer. The same raise is held until something changes: the pod's limit (another writer
moved it), a smaller raise (the budget moved), or the wait (5 minutes, then 10, 20, 40, 60, never longer). An accepted raise
clears the hold. The audit records each hold and its wait (`held_s`), and `omni_errors_total` and `omni_writes_total`
(`tools/omni_exporter.py`) show it to the operator.

The model gate's `convey_refused` model (the quota unreadable and every raise past the operator's limit refused, seeds 1 to 8):
omni-v12 wrote **49.75 commands a day against omni-v11's 1,985.5 (−97.5%, GAIN)**, and every other gauge was identical to
omni-v11's to the last digit: requests served, pod start wait, p95, alert minutes, host busy, CPU given and pod-seconds. On the
convey models with a readable quota and with an unreadable quota that admission accepts, omni-v12 and omni-v11 are identical on
every gauge. Tests: `tests/test_refused_raise.py`.

## 2. The swarm's reflex

`results/model_gate/V12_SWARM_REFLEX.md` holds the whole reading on gym-pybullet-drones, an outside simulator, on the counted
cells and on mission draws the wire was never run on. With the fix, every drone stays at or outside the keep-out on every cell
and draw tried, and 49% to 92% of omni-v11's energy cut is kept. That is the price of the reflex acting at once: on the long
cell the energy cut falls from −19.8% to −14.5% against native, power given back to the margin between the drones.

## 3. The model gate against omni-v11

`results/model_gate/V12_VS_V11.md` (seeds 1 to 8; the cluster models at 60 s and 15 s and with the blink, the three convey models and
the verdict model at 20 and 200 pieces of work a decision): omni-v12 reads **identical to omni-v11 on every gauge of every model but
one**, the convey model whose every raise is refused, where it writes 97.5% fewer commands (GAIN). No reading of omni-v12 against
omni-v11 is a LOSS. The standing engine's own readings against native in these models are omni-v11's and unchanged.

## 4. Studied and left out: the verdict's upper end (branch `v12-verdict-study`)

The candidate as first built also carried a stricter verdict: a step kept only when the upper end of every 95% interval of its
change in cost is inside the 2% allowance, each phase measuring as many pieces of work as a free step needs to show that, and a
trial that could not be read in its time never started. It answers a real fault (omni-v11 keeps a step whose interval reaches
past the allowance on its estimate alone: on noisy work a step that truly costs 3% is kept about a quarter of the time). On
work fast enough to read a step it kept a free step 98% of the time against omni-v11's 66%, and a 3% step 0% against 26%. But in
the model cluster set from a real run's regime the governor reads about 80 requests a decision and the rule needs about 4,000 a
phase: 1,102 of its give-back trials never started, no step was allowed, and the governor read identical to native, omni-v11's
machine-hour and energy cuts gone (shown under each cluster table of `V12_VS_V11.md`). On the data stores (one cost sample a
second, 40 to 120 a phase; 432 to 23,430 needed, read from the omni-v11 audits) every knob would stay native. Refused as
written; the fault stays on the next version's list (`docs/CHANGE_CONTROL.md`) until a trial design that reads a 2% step in a
trial's time is shown in the model gate.

## 5. What stays omni-v11's

Every other engine file, rule, gain, preset and muscle; the verdict (`omnicompass/verdict.py`) byte for byte; the control
panel, the gauges feed, the alert rules and the steering report, which sit outside the engine and read or drive it only through
the interfaces it already has (`docs/OBSERVABILITY.md`). The next version's list (`docs/CHANGE_CONTROL.md`) carries what is still
to fix: the power cap's band, the after-kill window widened to 300 s, the Redis harness's brain in its own process, the commands
without a shell, every governor wire in the fingerprint, the Kubernetes governor counting a worker an add-on marks while it
serves, and the verdict's reading of a step. The kind rig's governor role still cannot read the namespace's quotas: the
Operator's Manual, section 5.5, makes that grant optional, and the omni-v12 capacity rerun reads the hold in the real cluster.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
