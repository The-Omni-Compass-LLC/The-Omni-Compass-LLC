# Omni v2: the frozen engine, and every result checked against it

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Superseded on 2026-10-06 by Omni v3** (`docs/OMNI_V3.md`, `OMNI_V3.json`): the slack gate on speed knobs and the marine
> preset, nothing else. The v2 realms table stays a v2 result.

## What is frozen

Omni v2 is the engine as it stands at the commit that carries `OMNI_V2.json`. It covers the same files as v1
(`docs/OMNI_V1.md`):

- the compass law (`omnicompass/compass_law.py`), **unchanged from v1 byte for byte**;
- the live controllers (`omni_controller/`), **unchanged from v1 byte for byte**;
- the realms with their muscles and six organisms (`realms/`): **the catalog grew from 656 muscles in 46 families to 945
  in 59**, with thirteen new presets for the thirteen new families, and two count-free organism names (`tower`, `stack`);
- the runners of the independent simulators (`tools/run_kil.py`, `tools/run_citylearn.py`, `tools/run_pandapower.py`),
  unchanged except for the organism names in `run_kil.py`'s usage text.

`OMNI_V2.json` holds one SHA-256 for each of the 40 files, plus one digest over all of them: `4fc223939c4fab03…`. (The first
write of the file, in commit `ce5eb80`, had missed the two catalog source files because the fingerprint tool listed the last
commit's tree rather than the checkout; corrected the same morning, before any v2 table was published, and the tool now
lists every tracked or staged file. The engine's bytes did not change: every commit from `ce5eb80` on reads omni-v2.)

```
python3 tools/omni_version.py                    # this checkout: prints "omni-v2", "omni-v1", or every file that differs from v2
python3 tools/omni_version.py --commit <sha>     # the engine at the commit any result ran on
```

A result counts as a v2 result only if the commit it ran on carries exactly these bytes. A v1 result stays a v1 result:
nothing is read across versions.

## Why there is a v2

The founder's order of 6 October: make v2, add every missing muscle family, don't be cheap. The realm study had found
118 real controls the tower lacked, and whole domains had no family: hospitals and clinical systems, farms, pipelines,
rail, ships and ports, mines, district heat, power plants, renewables and inverters, elevators, pharmaceutical and food
plants. All of them are in now, each muscle with its real system, its setting and its source
(`docs/REALMS_PREREGISTRATION.md`, the v2 section; `realms/wave4_families.csv`; `docs/realm_study/TRUE_MUSCLES.csv`).

## What is the same in every muscle, and what is not

As in v1: one law, the same gains on every muscle. Results differ from domain to domain for the three declared reasons
(the machine underneath, the room native leaves, the guard rules each adapter carries), never because a gain was changed
per domain. The thirteen new presets are machine figures (`realms/presets.py`), not gains.

| Organism | v1 | v2 |
|---|---:|---:|
| Compute / AI / Cloud | 345 | 430 |
| Physics / Robotics / Autonomous | 262 | 376 |
| Energy / Facility / Industrial | 282 | 470 |
| Distribution / Specialized | 337 | 440 |
| The four stacked, every duplicate kept (`stack`) | 1,226 | 1,716 |
| The whole tower, every muscle once (`tower`) | 656 | 945 |
| The shared spine, in all four realms | 190 | 257 |

## The change rule

v2 does not change. A new rule, a new gain, a new guard or a new muscle makes v3 with its own fingerprint, and every
result is run again on it.

## Every result, by version

| Result | v1 | v2 |
|---|---|---|
| The muscles and six organisms, modelled | A, B, C done, reproduced byte for byte ([`results/realms/v1/REALMS.md`](../results/realms/v1/REALMS.md)) | **A, B, C done** (runs 37422832244, 37422840154, 37422847697; reproduced to the last digit in 3 of 3): [`results/realms/REALMS.md`](../results/realms/REALMS.md); 945 muscles, 0 LOSS or power given; Physics and the whole tower read energy improvement with a service tradeoff, carried by three rail traction speed muscles (see the register, row 24) |
| The organisms at 1 / 10 / 100 / 1,000 copies (v1: `results/scale/v1/GRID.md`) | partly (1,000x at 100 and 1,000 runs beyond the machines) | **to run** (workflow `six`) |
| Kubernetes: the six organisms with the real cluster inside | running (37359815637) | **to run** (workflow `six-kube`) |
| Kubernetes: the big organisms on Azure | running (37359820055) | **to run after** |
| Kubernetes: steady, wandering, all four, fairness, faults, batch | A, B, C done (`results/live/V1_*.md`) | to run again as the queue allows; the controller is byte for byte v1's |
| Azure AKS steady and burst | steady reps 1-2 done, 3-5 wait on quota | to run after the big organisms |
| CityLearn, the power grid, the robot arms | A, B, C done (grid C running) | to run again as the queue allows; the runners are byte for byte v1's |
| Databases (PostgreSQL behind PgBouncer) | none | tuning run done (37420052827, not counted; register row 30); the untouched workloads running, then A, B, C |
| GPU, one card and the card in the organisms | none on v1 | the founder's rerun on Lambda, on v2 |

## How each result is read across three runs

Exactly as v1: three separate GitHub runs on the same frozen bytes; every judged row reads GAIN in all three of our runs, LOSS in all three of our runs, no difference beyond the noise (with the count of runs), or the runs disagree; every row is reported, losses
included; the tables are made by rule (`tools/confirm_abc.py`, `tools/citylearn_abc.py`, `tools/pandapower_abc.py`,
`tools/mujoco_abc.py`), each checking every run's commit against the fingerprints and refusing to mix engines.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
