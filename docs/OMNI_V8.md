# Omni v8: the battery that carries its building through an outage stays native (the engine of 17 October)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v8 stood on main on 17 October; later that day it was followed by Omni v9 (`docs/OMNI_V9.md`), omni-v8 with the
CityLearn battery wire reading the coming hour, which cuts the one row this page names (section 3; printed LOSS, power given by
the key, `docs/OMNI_V9.md`, section 1), and on 18 October by Omni v10 (`docs/OMNI_V10.md`), the engine that stands. This page
stays as omni-v8's record, read beside no other engine's.

Omni v8 was the engine that stood on main from 17 October (the founder's order: "there's a new version 8 ... push in all and
update all"). It is omni-v7 (`docs/OMNI_V7.md`) with one change to one wire, made because a three-run table of omni-v7 read LOSS
and the cause was found to be ours. Its fingerprint is `OMNI_V8.json` (digest `f93d233136a1f902`, 46 files); of those 46 files,
45 are omni-v7's bytes, and the one that differs is the CityLearn runner. Every benchmark runs again on it (`scripts/reruns.txt`;
the conductor's reruns, grid and Azure queues restarted on it the same day), and every omni-v7 table stands as omni-v7's result
until its three runs on v8 land; results from two versions are never pooled. Run and scored by The Omni-Compass LLC's own code.
No outside party has reviewed or approved these results.

| # | Change | Where | What it tightens |
|---|---|---|---|
| 1 | A battery whose building simulates power outages stays native: Omni-Compass moves only the batteries with no second duty | `tools/run_citylearn.py` | do no harm where the battery's charge is also its building's reserve |

## 1. What omni-v7 read, and why

The omni-v7 CityLearn table (`results/live/V7_CITYLEARN.md`; runs 38937540021, 38949618073, 38959444615) read GAIN in all three
of our runs on the electricity bought and the daily peak in all ten battery districts, and **LOSS in all three of our runs in the
seven 2023 districts** on the energy not served (+2.0% to +9.8%) and the time uncomfortable (+0.01% to +0.15%), beside the
ramping +4.5% to +6.2%, the highest peak +2.5% (three districts) and the monthly unevenness +0.07% (one), power held and so power
given by the key (the table printed those three LOSS too, until the CityLearn tool was corrected on 17 October).

The cause was found on CityLearn itself (version 3.0.2, the version the runs installed), run locally on the same district files
and reproducing the omni-v7 numbers of `citylearn_challenge_2023_phase_2_local_evaluation` to the last digit:

- The seven 2023 districts are the only districts CityLearn ships whose buildings simulate power outages (every building in each:
  3, 3, 3, 3, 6, 6 and 6; every other district none, read from each district's own `schema.json`). CityLearn counts the energy not
  served only in outage hours (`citylearn/cost_function.py`, `normalized_unserved_energy`), and the time uncomfortable rises when an
  islanded building cannot run its cooling.
- The battery wire read the district's draw alone. It did not see the outage hours, and it did not see that in these buildings
  the battery has a second duty: carrying the building through the outage. A command that moves the battery for the district's
  draw during an outage asks for energy the islanded building cannot have.
- Three narrower repairs were tried on the tuning district first and refused there: charging only (the energy not served
  unchanged at +5.96%, LOSS, the ramping +3.5%); handing the battery back to native only during outage hours (the energy not
  served −2.7% and the discomfort −0.13%, both GAIN, with the ramping +7.0% and the monthly unevenness +0.06% beside them); and
  moving no more energy than the draw's excess over its band (the daily peak +0.5% and the ramping +2.6%). With peaks, swings and
  unevenness then read as misses, each was refused. By the key (17 October) those rises are power given, so the second, native
  only in outage hours, reads GAIN on both misses; it is studied again for the next engine version.

## 2. The change

The wire now leaves native every battery whose building simulates power outages (CityLearn's own `simulate_power_outage`, read
from the building), as a water tank was left native in round 2: a battery that is also its building's reserve is a muscle with a
second duty, which needs its own wire and its own reading (the outage risk) before Omni-Compass moves it. Every other battery is
moved exactly as before: the compass law, its gain, its response, its glide, its band and its hand-back are unchanged. An action
list the wire cannot place on its buildings moves nothing. The hour count of the file counts only hours where a command moved,
and each district's file says how many batteries were left native for outages (`batteries_left_native_for_outages`).

## 3. What it does, read on CityLearn before any GitHub run

On the seven 2023 districts the omni arm is native's to the last digit (every battery left native; checked on
`citylearn_challenge_2023_phase_2_local_evaluation` and `citylearn_challenge_2023_phase_3_1`). On every district without outage
buildings the wire's commands are the same bytes as omni-v7's, so their results are omni-v7's (checked to the digit on
`citylearn_challenge_2022_phase_all_robustness`, every gauge of both arms identical to omni-v7's GitHub run 38937540021, no
battery left native). So v8 removes every LOSS of the 2023 districts and, with them, their small GAINs (the electricity bought
−0.1% to −0.3%, the daily peak −1.3% to −2.6%), which were bought with the LOSS beside them.

One row the table printed LOSS remains, and it is said here: in `citylearn_challenge_2022_phase_all_robustness` (no outage
buildings) the monthly unevenness rose 0.11% in all three of our runs (power given by the key: a ratio of the power held), beside the bill −8.6%, the electricity bought −14.7%, carbon −11.9%, the
daily peak −14.0% and the highest peak −2.7%, all GAIN. The score is a ratio (one minus each month's mean over its peak), and it
rose because the energy fell faster than each month's top hours, which sit at the batteries' limit. Its repair is looked into on
its own, in the model gate first; v8 does not change it.

## 4. The model gate and the trial

The change touches no Kubernetes, card or cloud controller, so the model gate's models (`tools/model_gate.py`) read the same on both
checkouts by construction; the gate was run all the same, omni-v8 against omni-v7 on the same seeds, and is recorded in
`results/model_gate/V8_VS_V7.md`: seeds 1 to 8, a day each, every gauge of every model (the cluster at 60 s and at 15 s, conveyance
with the quota readable and unreadable, the verdict on noisy work) identical between omni-v8 and omni-v7, to the last digit and
in every count (steps allowed and refused, trials abandoned, machines parked, errors). The models' readings against native are
omni-v7's and stay disclosed in `docs/OMNI_V7.md`, section 6 (at a decision every 15 s the cloud setting makes pods wait longer
than native, which is why the decision period stays 60 s). These are our own models (class S), never a benchmark result.

The trial is the CityLearn benchmark itself, A, B and C on the v8 commit, read by `tools/citylearn_abc.py` into
results/live/V8_CITYLEARN.md when they land: it must read no LOSS in the 2023 districts and the same table as omni-v7 everywhere else. The
disclosure every amendment carries: every CityLearn district has now been seen, so no untouched district remains for this
amendment; it was fixed on one district (`citylearn_challenge_2023_phase_2_local_evaluation`) and is reported on all
(`docs/CITYLEARN_PREREGISTRATION.md`, amendment of 17 October).

## 5. What runs again on it

Everything, A, B and C, from the moment it landed (`scripts/reruns.txt`, released by the conductor a few a tick: A of every
benchmark, then B, then C); the grid on its own manifest (`results/grid_v8/`); every Azure set from A again
(`scripts/azure_queue.txt`). The omni-v7 runs already started run to their end (nothing is cancelled) and stay as omni-v7's
record. Google Cloud and Amazon carry the same sets behind their switches, off until the founder turns them on; the GPU runs on
Lambda wait for his word and one exact commit. The organisms are the seven of 16 October, the spine first (`docs/THE_SPINE.md`).

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
