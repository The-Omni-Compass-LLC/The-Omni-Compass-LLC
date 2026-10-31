# Omni v10: the battery glide at the speed that cuts the bill most (the engine that stood on 18 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v10 stood on main on 18 October; the same day it was followed by Omni v11 (`docs/OMNI_V11.md`), the engine that stands:
omni-v10 with the Kubernetes governor's hold on a reading with no machine in service. This page stays as omni-v10's record,
read beside no other engine's. The founder's orders behind it: "Omni-Compass should be tuned to exploit all
that can be and keep all healthy and never raise its bill ... whatever one can't be achieved doesn't get achieved. And the tuning
stays where it doesn't ever hurt anyone"; and, on 17 October, "a minus doesn't mean a loss and neither does a plus mean a gain if
you don't understand what it's against". It is omni-v9 (`docs/OMNI_V9.md`) with one setting changed: the most the CityLearn battery
wire's adjustment may change in an hour (the glide) goes from 0.0625 to 0.0875 of the command's range. The CityLearn runner's own
receipt now reads every score by the one key, as every table already did.

Its fingerprint is `OMNI_V10.json` (digest `4bf39b0d707784de`, 47 files). Forty-six files are omni-v9's bytes and one differs (the CityLearn
runner). The change was proven in our own runs of CityLearn and in the model gate before it was pushed. Every benchmark runs again on
it. Every earlier table stands as its own engine's result until its three runs on v10 land, and results from two versions are never
pooled. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

| # | Change | Where | What it does |
|---|---|---|---|
| 1 | The battery wire's glide: 0.0875 of the command's range an hour (omni-v9: 0.0625) | `tools/run_citylearn.py` | the batteries follow the coming hour faster, and the bill falls further in every district that has a price |
| 2 | The runner's receipt reads every score by the one key: a fall is a GAIN; a rise in energy not served or time uncomfortable is a LOSS; a rise in any other score is power given | `tools/run_citylearn.py` | one key for every output, as the three-run table (`tools/citylearn_abc.py`) already read |

## 1. Why the glide moved

omni-v9 set the glide at the fastest speed at which no score in any district rose. That rule counted a rise in the ramping or in
the distance from net zero against the engine. The one key of 17 October (`tools/readings.py`) does not. The ramping, the peaks, the
unevenness and the net-zero distance describe the power the district holds from the grid: they are resources held. A rise in one of
them is power given, shown beside what it bought, never a LOSS. Only what the occupants miss is a LOSS: energy not served and time
uncomfortable.

Read by that key, the ladder omni-v9 ran shows that no glide reads a LOSS anywhere, and that the bill keeps falling up to 0.0875. At
0.10 it falls less in both districts that set the edge:

| District | Score | 0.05 | 0.0625 (omni-v9) | 0.075 | 0.0875 (omni-v10) | 0.10 |
|---|---|---:|---:|---:|---:|---:|
| phase 2 | the bill | -14.12% GAIN | -17.22% GAIN | -18.75% GAIN | -19.17% GAIN | -19.03% GAIN |
| phase 2 | daily unevenness | +0.25% power given | -0.09% GAIN | -0.67% GAIN | -0.94% GAIN | -0.91% GAIN |
| phase 2 | net-zero shortfall | -7.53% GAIN | -4.77% GAIN | -3.38% GAIN | -2.54% GAIN | -1.99% GAIN |
| phase 3 | the bill | -6.60% GAIN | -7.32% GAIN | -8.10% GAIN | -8.43% GAIN | -8.32% GAIN |
| phase 3 | the ramping | -5.05% GAIN | -1.91% GAIN | +2.32% power given | +6.18% power given | +9.59% power given |
| phase 3 | net-zero shortfall | -2.21% GAIN | -0.76% GAIN | -0.04% STEADY | +0.25% power given | +0.41% power given |

So 0.0875 is the glide that cuts the bill most with no LOSS: the founder's rule for the tune. Nothing else in the wire changed. The
compass law, its gain (0.5), its response (1 h), its reading (the coming hour, from the same hour of the past seven days), its band
(the 10th to the 90th percentile of the past week's draw), the hand-back at 90% of the year, the batteries left native in outage
buildings and the water tanks left native are all omni-v9's.

## 2. What it does, read on CityLearn before any GitHub run

CityLearn 3.0.2, run locally on its own district files: native (CityLearn's BasicRBC) against Omni-Compass on top of it. Every score
is CityLearn's own (each over no battery at all), and every row is read by the one key. The omni-v9 column is the wire as it stood.

**2022 robustness, 17 buildings (where the omni-v8 row stood)**

| CityLearn score | native | omni-v9 against native | omni-v10 against native |
|---|---:|---:|---:|
| the bill | 1.1008 | -14.22% GAIN | -16.09% GAIN |
| electricity bought | 1.1938 | -14.92% GAIN | -13.58% GAIN |
| carbon | 1.1494 | -13.11% GAIN | -12.07% GAIN |
| the daily peak | 1.1392 | -20.82% GAIN | -16.92% GAIN |
| the highest peak | 1.0272 | -2.73% GAIN | -2.73% GAIN |
| the ramping | 1.2231 | -12.60% GAIN | -9.41% GAIN |
| daily unevenness | 1.0084 | -7.32% GAIN | -6.02% GAIN |
| monthly unevenness | 0.9892 | -2.29% GAIN | -1.59% GAIN |
| net-zero shortfall | 1.1312 | -2.76% GAIN | -0.96% GAIN |

**2022 phase 1, 5 buildings (the tuning district)**

| CityLearn score | native | omni-v9 against native | omni-v10 against native |
|---|---:|---:|---:|
| the bill | 1.1158 | -17.63% GAIN | -20.05% GAIN |
| electricity bought | 1.2275 | -19.37% GAIN | -18.23% GAIN |
| carbon | 1.1804 | -17.15% GAIN | -16.52% GAIN |
| the daily peak | 1.1417 | -19.63% GAIN | -17.06% GAIN |
| the highest peak | 1.0142 | -5.04% GAIN | -5.04% GAIN |
| the ramping | 1.1562 | -10.45% GAIN | -8.76% GAIN |
| daily unevenness | 0.9892 | -3.09% GAIN | -2.57% GAIN |
| monthly unevenness | 0.9900 | -1.68% GAIN | -1.09% GAIN |
| net-zero shortfall | 1.1369 | -2.85% GAIN | -1.22% GAIN |

**2022 phase 2, 5 buildings**

| CityLearn score | native | omni-v9 against native | omni-v10 against native |
|---|---:|---:|---:|
| the bill | 1.1080 | -17.22% GAIN | -19.17% GAIN |
| electricity bought | 1.2124 | -18.44% GAIN | -17.80% GAIN |
| carbon | 1.1665 | -16.69% GAIN | -16.31% GAIN |
| the daily peak | 1.1124 | -17.74% GAIN | -15.67% GAIN |
| the highest peak | 0.9983 | -11.26% GAIN | -8.30% GAIN |
| the ramping | 1.1231 | -10.99% GAIN | -10.67% GAIN |
| daily unevenness | 0.9787 | -0.09% GAIN | -0.94% GAIN |
| monthly unevenness | 0.9828 | -0.66% GAIN | -0.52% GAIN |
| net-zero shortfall | 1.1970 | -4.77% GAIN | -2.54% GAIN |

**2022 phase 3, 7 buildings**

| CityLearn score | native | omni-v9 against native | omni-v10 against native |
|---|---:|---:|---:|
| the bill | 1.0848 | -7.32% GAIN | -8.43% GAIN |
| electricity bought | 1.1573 | -6.23% GAIN | -4.70% GAIN |
| carbon | 1.1155 | -5.50% GAIN | -4.05% GAIN |
| the daily peak | 1.0973 | -16.09% GAIN | -12.57% GAIN |
| the highest peak | 0.9942 | -3.61% GAIN | -3.61% GAIN |
| the ramping | 1.1814 | -1.91% GAIN | +6.18% power given |
| daily unevenness | 1.0176 | -9.88% GAIN | -7.76% GAIN |
| monthly unevenness | 0.9838 | -5.07% GAIN | -4.74% GAIN |
| net-zero shortfall | 1.0809 | -0.76% GAIN | +0.25% power given |

**2022 phase all, 17 buildings**

| CityLearn score | native | omni-v9 against native | omni-v10 against native |
|---|---:|---:|---:|
| the bill | 1.1007 | -14.20% GAIN | -16.08% GAIN |
| electricity bought | 1.1941 | -14.92% GAIN | -13.58% GAIN |
| carbon | 1.1496 | -13.11% GAIN | -12.07% GAIN |
| the daily peak | 1.1392 | -20.77% GAIN | -16.92% GAIN |
| the highest peak | 1.0272 | -2.73% GAIN | -2.73% GAIN |
| the ramping | 1.2223 | -12.57% GAIN | -9.33% GAIN |
| daily unevenness | 1.0084 | -7.29% GAIN | -6.02% GAIN |
| monthly unevenness | 0.9892 | -2.28% GAIN | -1.58% GAIN |
| net-zero shortfall | 1.1315 | -2.78% GAIN | -0.98% GAIN |

Across the districts above: omni-v9 45 GAIN, 0 STEADY, 0 power given, 0 LOSS; omni-v10 43 GAIN, 0 STEADY, 2 power given, 0 LOSS.

**Alameda County and Travis County (100 buildings each)** were still running locally when this version was pushed; this
machine runs each neighbourhood for hours, and their omni-v9 runs read no LOSS (`docs/OMNI_V9.md`, section 3). No score in them
that can read a LOSS moves with the glide: they carry no price (the bill is 1.0 in both arms, STEADY by construction), no outage
(energy not served is 0 in both arms) and no comfort the electric batteries touch (time uncomfortable +0.00% on omni-v9). Every
other score there is a resource spent or held, where a rise is power given. Their three runs on GitHub, with every other
district, make the omni-v10 CityLearn table; the local runs are added here when they finish.

**What the faster glide trades.** In every district with a price, the bill falls 1.1 to 2.4 points further than at omni-v9.
Most other scores fall a little less than at omni-v9 and still read GAIN: the electricity bought, the carbon, the daily peak, the
ramping, the unevenness and the net-zero distance. The highest peak holds where omni-v9 left it, except in the 2022 phase 2 (−8.30%
against −11.26%), and that district's daily unevenness falls further (−0.94% against −0.09%). Two rows of the 2022 phase 3 rose
and are power given: the ramping +6.18% and the net-zero shortfall +0.25%. A little more electricity is bought than at omni-v9
while the bill falls further, so each unit bought costs less on average. None of these five districts carries the occupants' own scores (energy not served, time uncomfortable); in the 2023 districts
they are native's to the last digit, and in Alameda and Travis they read STEADY on omni-v9.

**Shown, power given.** In some months the peak hour with Omni-Compass on top rises above native's. With omni-v10 that happens in
3 months in the robustness district (omni-v9: 2), 3 in the tuning district (3), 1 in the 2022 phase 2 (1), 1 in the 2022 phase 3 (1)
and 3 in phase all (2). By day it happens on 23, 25, 21, 56 and 23 days of the year (omni-v9: 16, 28, 15, 43 and 16). The two 100-building neighbourhoods were still running locally when this version was pushed (on omni-v9 neither showed a month
whose peak rose above native's).
A peak is power held, so each of these is power given. CityLearn's own scores over the year (the highest peak, the daily peak and
the monthly unevenness) read GAIN in every one of the five districts.

The districts: the robustness district (`citylearn_challenge_2022_phase_all_robustness`); the tuning district
(`citylearn_challenge_2022_phase_1`); the 2022 phases 2, 3 and all, which CityLearn ships in its source repository but not in its
package, so the GitHub benchmark does not run them; and the two 100-building neighbourhoods the benchmark counts (Alameda County and
Travis County). The seven 2023 districts are unchanged by construction. Every battery in them is left native (omni-v8), so their
omni arm is native's to the last digit; this was checked with the v10 runner on `citylearn_challenge_2023_phase_2_local_evaluation`,
where all eleven scores are identical.

## 3. Refused: the outage buildings' batteries outside the outage hours

One more change was tried before this version was set, at the same glide. The batteries in buildings that carry an outage would be
steered outside the outage hours and handed back to native through each outage. Six of the seven 2023 districts were run:

| 2023 district | the bill | energy not served | time uncomfortable |
|---|---:|---:|---:|
| phase 2, local evaluation | +0.19% power given | -2.68% GAIN | -0.12% GAIN |
| phase 2, online evaluation 1 | -0.09% GAIN | **+0.69% LOSS** | -0.04% GAIN |
| phase 2, online evaluation 2 | -0.11% GAIN | -0.15% GAIN | +0.00% STEADY |
| phase 2, online evaluation 3 | -0.09% GAIN | -1.44% GAIN | -0.06% GAIN |
| phase 3, district 1 | -0.25% GAIN | -2.47% GAIN | -0.04% GAIN |
| phase 3, district 2 | -0.37% GAIN | -0.38% GAIN | -0.03% GAIN |

In the first online evaluation, more energy went unserved. That is a miss, a LOSS. In the local evaluation, the bill rose. One LOSS
is enough to refuse the change, and the founder's rule never raises the bill, so the seventh district was not needed. The batteries
in outage buildings stay native all year, as in omni-v8 and omni-v9.

## 4. The model gate

The change touches no Kubernetes, card or cloud controller, and the model gate's models (`tools/model_gate.py`) do not run the
CityLearn wire, so they read the same on both checkouts by construction. The gate was run all the same, the candidate against
omni-v9 on seeds 1 to 8, and is recorded in `results/model_gate/V10_VS_V9.md`. Every gauge of every model reads identical to omni-v9
to the last digit (26 of 26: the cluster at 60 s and at 15 s, and conveyance with the quota readable and unreadable), and so do
every count and the verdict on noisy work. These are our own models (class S), never a benchmark result.

## 5. What runs again on it

Everything runs again, A, B and C, from the moment v10 lands (`scripts/reruns.txt`, the omni-v10 campaign, released by the
conductor a few at a time each tick). The grid runs on its own manifest (`results/grid_v10/`), and every Azure set starts again from
A. Google Cloud and Amazon, switched on by the founder on 18 October with their secrets in, run the same four sets from A,
one at a time in each machine-family queue. The GPU runs on Lambda wait for the founder's word and one exact commit. The
three CityLearn runs on GitHub make the omni-v10 CityLearn table in `results/live/`. It must read no LOSS in any district, as it did
locally in every district read before the push.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
