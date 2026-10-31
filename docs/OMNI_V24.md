# Omni v24: the base engine at 20 s; the compass's cover a knob read in each setting

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v24 (`OMNI_V24.json`, 65 files) is omni-v23 with the Kubernetes governor's factory beat at 20 s, on the founder's order of
31 October, evening:

> "Heartbeat period says 10, 15, 30, 60, 90, 120. Change that ... 15, 20, 30, 60, 90, 120 ... you are to lock this base engine at
> 20 ... It still says 60 seconds, heartbeat period. Which means it's taking a whole minute to double check itself ... that's way
> too long."

and the standing order that every change lands as the next version, told, not asked. One file of the 65 moves
(`omni_controller/controller.py`); do no harm keeps its strictest form.

## What changes in the engine

- **The factory beat is 20 s** (`--interval`, default 20; 60 s from omni-v17 to omni-v23, 15 s on omni-v16). The governor reads the
  whole body and decides three times a minute; its fast checks stay every 5 s. Every clock counts seconds (omni-v16), so no rule's
  time moves with the beat: the trial's 1,200 s, the wait of 7,200 s after a refusal, the cruise wait of 120 s (never under two
  readings) are each the same minutes at 20 s as at 60 s, in three times as many decisions.
- **The compass's cover is a knob** (`--cover-floor`, default 0.6, the cover every engine before omni-v24 wrote in): the lowest
  share of the operator's own autoscaler target the compass may set; 0.6 asks for up to 1/0.6 of the pods native's target would,
  1.0 leaves the pod count native's. The floor is never above the operator's target, so the compass never asks for fewer pods
  than native would; before omni-v24 an operator's target under 10% put the cover's 10% bound above it (`tests/test_cover_floor.py`).
- **The struck flag leaves the governor**: `--give-back-only`, the cloud's machines-alone rule of 14 October, struck on 31 October;
  the governor now refuses it (`tests/test_cloud_at_the_max.py`).

## What changes around the engine

- **Every place that starts the governor runs it at 20 s**: the rigs (`scripts/kind_bench.sh` `OMNI_INTERVAL`, `kind_paired.sh`,
  `kind_robust.sh`, `kind_levers.sh`, `kind_full.sh`, `kind_pilot.sh`), the install files (`deploy/install/omni-compass.yaml`,
  `deploy/install/omni-compass-cloud.yaml`, `deploy/controller.yaml`), the controller trace (`docs/engine/export_controller_trace.py`);
  the alert rules' staleness bound is three beats, 60 s at 20 s (`deploy/prometheus/omni-compass-rules.yaml`).
- **The live engine opens at 20 s, and its heartbeat has seven buttons**: 10, 15, 20, 30, 60, 90 and 120 s (the first number of the
  founder's list read as 10, the beat he asked for on 24 October); the beat's note reads a beat that is not a multiple of the page's
  15 s step correctly ("3 full decisions land in every 4 steps").
- **The model's stand-in cluster corrected** (`pilot/selfpilot.py`, found by a probe before the second tune search): its pods carried
  none of the metadata a real cluster gives every pod and were one repeated object per workload, and it took only the autoscaler's
  target among the governor's writes; the governor's count of the room beside a workload failed on its first pod (4 to 7 decisions a
  day lost in the pace models, on every engine read before), every running pod of a workload read as on one machine, and the raise of
  the autoscaler's range never landed. Every record read before the correction stands as its own.

## The model gate

[to be read: tools/model_gate.py, omni-v24's candidate against omni-v23 on the corrected model, seeds 1 to 8]

## The second tune search, at 20 s

[to be read: docs/THE_TUNE.md section 4b, results/model_gate/V24_TUNE.md]

## The tests

`tests/test_pace_clocks.py` (the heartbeat 20 s in the governor, every rig and every install file), `tests/test_cover_floor.py`,
`tests/test_cloud_at_the_max.py` (the struck flag refused), `tests/test_tune_study.py` (the second search's grids, a study judged by
its own grids).

## What is run again

Every benchmark runs again on omni-v24 (`scripts/reruns.txt`, A of every entry, then B, then C; the conductor's campaign from its
landing). The omni-v23 runs started before stand as omni-v23's record.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
