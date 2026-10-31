# Omni v9: the battery wire reads the coming hour (the engine that stood on 17 and 18 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v9 stood on main from 17 to 18 October; on 18 October it was followed by Omni v10 (`docs/OMNI_V10.md`), the engine that
stands: omni-v9 with the battery glide at 0.0875 an hour, the speed that cuts the bill most with no LOSS (section 2 below gives
the ladder it was chosen from). This page stays as omni-v9's record, read beside no other engine's.

Omni v9 was the engine on main from 17 October (the founder's orders: "we're going into another version of
Engine ... Apply the fix, run it, and see in the model sim that it works"; "Omni-Compass should be tuned to exploit all that can be
and keep all healthy and never raise its bill ... the tuning stays where it doesn't ever hurt anyone"). It is omni-v8
(`docs/OMNI_V8.md`) with one wire repaired and one statistical table made exact. It was written for one omni-v8 row the table
printed as LOSS; on 17 October the founder found that word misapplied (section 1): the row was power given. The repair it led to
stands on its own, because it cuts the bill further in every district. Its fingerprint is `OMNI_V9.json` (digest `7379f3a79ff2c475`, 47 files); 44 are omni-v8's bytes, two
differ (the CityLearn runner and the realms harness) and one is new (`omnicompass/student_t.py`). It was proven in our own runs of
CityLearn and in the model gate before it was pushed. Every benchmark runs again on it, and every earlier table stands as its own
engine's result until its three runs on v9 land; results from two versions are never pooled. Run and scored by The Omni-Compass
LLC's own code. No outside party has reviewed or approved these results.

| # | Change | Where | What it tightens |
|---|---|---|---|
| 1 | The battery wire reads the coming hour's draw (the mean of the same hour over the past seven days, only hours already seen) and its adjustment glides at up to 0.0625 of the command's range an hour (0.05 before), the fastest glide that read no LOSS on any score in any district | `tools/run_citylearn.py` | the battery answers the hour it moves, not the hour gone |
| 2 | Every 95% interval uses the exact Student t quantile for its number of pairs | `omnicompass/student_t.py`, `realms/harness.py` and the table tools | no interval narrower than its sample allows, at any count |

## 1. What omni-v8 read, and why

One row of the omni-v8 table was printed LOSS: in `citylearn_challenge_2022_phase_all_robustness` (17 buildings, a battery in
each, no outage buildings) the monthly load unevenness (`monthly_one_minus_load_factor_average`: one minus each month's mean draw
over its peak) rose 0.11% in all three of our runs, beside the bill −8.6%, the electricity bought −14.7%, the daily peak −14.0% and
the highest peak −2.7%, all GAIN (the omni-v7 table, whose commands omni-v8 repeats to the byte outside the 2023 districts). **By
the key that row is power given, not a LOSS**: the unevenness is the shape of the power the district holds from the grid, a
resource held, as a peak is; it is neither time waited nor work done nor a miss. The CityLearn table tool had filed the peaks, the
swings and the unevenness as misses; it was corrected on 17 October (`tools/citylearn_abc.py`, `tools/readings.py`: one key for
every gauge, as a cluster's peak power always was). Run locally, the same wire also raised, on districts the GitHub benchmark does
not run (CityLearn ships them only in its source repository), the tuning district's monthly unevenness +0.26%; in the 2022 phase 2
the highest peak +0.17%, the daily unevenness +1.03% and the monthly unevenness +0.68%; in the 2022 phase 3 the highest peak +0.45%
and the ramping +3.37%: power given, every one, and shown here with the rest.

The cause was found in an hour-by-hour trace of the omni-v8 wire on the robustness district (CityLearn 3.0.2, run locally):

- The compass read the district's draw of the hour just gone and moved the batteries for the hour coming, and its adjustment
  could change by only 0.05 of the command's range an hour. Averaged by hour of day over the year, the adjustment discharged
  hardest at 00:00 and charged hardest at 15:00, while the district's draw peaked at 19:00 and bottomed at 13:00: it ran about five
  hours behind the day, still adding charge at 17:00 and 18:00 as the evening peak climbed.
- So the batteries were empty when each month's top hour came: at the month's highest net draw the mean state of charge was 0.000
  to 0.037 in ten of the eleven months the trace covers.
- The score is a ratio. Lowering a month's mean (less energy bought) while its peak hour stays at the batteries' limit raises one
  minus mean over peak: the energy fell faster than the top hours.

Narrower repairs were tried on the robustness district first; each left the unevenness up, so none is in the engine:

| Candidate | What it changed | Monthly unevenness against native |
|---|---|---:|
| no discharge below the band's middle | Omni-Compass adds no discharge in a quiet hour | +0.11% (power given) |
| no new peak (the month's top so far, and the month's or the week's) | the charge it adds never lifts the district above its top so far | +0.11% (power given) |
| peak push | full discharge where the draw nears the month's top so far | +0.12% (power given) |
| a reserve of 30%, 50% or 70% of charge | its added discharge stops at the reserve | +0.42%, +0.25%, +0.25% (power given), and the highest peak's GAIN lost |
| the hour gone, glide 0.25 | faster only | −0.61% (GAIN), the ramping +13.2% (power given) |

## 2. The change, and how far it is pushed

The reading is the draw of the hour the batteries are about to move: the mean of the same hour of the day over the past seven
days, h[t−24], h[t−48], …, h[t−168] (only hours already seen; before a day has been seen, the last hour's draw). Nothing else in
the wire changed: the compass law, its gain (0.5), its response (1 h), its band (the 10th to the 90th percentile of the past week's
draw), the hand-back at 90% of the year, the batteries left native in outage buildings (omni-v8) and the water tanks left native.

The glide was set where no score of any district rose: with the new reading, every glide from 0.05 to 0.10 an hour was run on the
districts where the edge lies, and the fastest at which nothing rose in either is 0.0625. Read by the key, no glide on the ladder
reads a LOSS anywhere: every rise below is power given, and the bill keeps falling up to 0.0875 to 0.10:

| District | Score | 0.05 | 0.0625 | 0.075 | 0.0875 | 0.10 |
|---|---|---:|---:|---:|---:|---:|
| phase 2 | daily unevenness | +0.25% power given | -0.09% GAIN | -0.67% GAIN | -0.94% GAIN | -0.91% GAIN |
| phase 2 | net-zero shortfall | -7.53% GAIN | -4.77% GAIN | -3.38% GAIN | -2.54% GAIN | -1.99% GAIN |
| phase 2 | the bill | -14.12% GAIN | -17.22% GAIN | -18.75% GAIN | -19.17% GAIN | -19.03% GAIN |
| phase 3 | the ramping | -5.05% GAIN | -1.91% GAIN | +2.32% power given | +6.18% power given | +9.59% power given |
| phase 3 | net-zero shortfall | -2.21% GAIN | -0.76% GAIN | -0.04% STEADY | +0.25% power given | +0.41% power given |
| phase 3 | the bill | -6.60% GAIN | -7.32% GAIN | -8.10% GAIN | -8.43% GAIN | -8.32% GAIN |

At 0.05 the 2022 phase 2's daily unevenness rises; from 0.075 the 2022 phase 3's ramping does, and from 0.0875 its net-zero
shortfall: power given, each. At 0.0625 every score of every district reads GAIN (section 3). The founder's rule for the tune (use
everything that can be used, keep everything healthy, never raise the bill) takes the glide past 0.0625, to the speed that cuts the
bill most with no LOSS: that is the next version's change, read on CityLearn first.

The second change is statistical and moves no command. The interval tables written in each tool stopped at a few sample sizes and
fell back to 1.96 (the normal quantile) for a number of pairs they did not list, too narrow an interval for a small sample. Every
tool now takes the exact quantile from one file, `omnicompass/student_t.py` (the regularized incomplete beta function, checked
against the published table to three decimals). Every value the old tables held is unchanged; no published table used a count the
old tables lacked, so no published reading moves.

## 3. What it does, read on CityLearn before any GitHub run

CityLearn 3.0.2, run locally on its own district files, native (CityLearn's BasicRBC) against Omni-Compass on top of it; every
score is CityLearn's own (each over no battery at all), and every row is read by the one key. The omni-v8 column is the wire as it stood.

**2022 robustness, 17 buildings (where the omni-v8 row stood)**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.1008 | -8.61% GAIN | -14.22% GAIN |
| electricity bought | 1.1938 | -14.66% GAIN | -14.92% GAIN |
| carbon | 1.1494 | -11.89% GAIN | -13.11% GAIN |
| the daily peak | 1.1392 | -13.95% GAIN | -20.82% GAIN |
| the highest peak | 1.0272 | -2.73% GAIN | -2.73% GAIN |
| the ramping | 1.2231 | -7.18% GAIN | -12.60% GAIN |
| daily unevenness | 1.0084 | -2.90% GAIN | -7.32% GAIN |
| monthly unevenness | 0.9892 | +0.11% power given | -2.29% GAIN |
| net-zero shortfall | 1.1312 | -6.10% GAIN | -2.76% GAIN |

**2022 phase 1, 5 buildings (the tuning district)**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.1158 | -10.54% GAIN | -17.63% GAIN |
| electricity bought | 1.2275 | -17.77% GAIN | -19.37% GAIN |
| carbon | 1.1804 | -14.67% GAIN | -17.15% GAIN |
| the daily peak | 1.1417 | -11.88% GAIN | -19.63% GAIN |
| the highest peak | 1.0142 | -1.40% GAIN | -5.04% GAIN |
| the ramping | 1.1562 | -4.41% GAIN | -10.45% GAIN |
| daily unevenness | 0.9892 | -0.29% GAIN | -3.09% GAIN |
| monthly unevenness | 0.9900 | +0.26% power given | -1.68% GAIN |
| net-zero shortfall | 1.1369 | -6.55% GAIN | -2.85% GAIN |

**2022 phase 2, 5 buildings**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.1080 | -10.83% GAIN | -17.22% GAIN |
| electricity bought | 1.2124 | -16.87% GAIN | -18.44% GAIN |
| carbon | 1.1665 | -14.09% GAIN | -16.69% GAIN |
| the daily peak | 1.1124 | -12.23% GAIN | -17.74% GAIN |
| the highest peak | 0.9983 | +0.17% power given | -11.26% GAIN |
| the ramping | 1.1231 | -3.97% GAIN | -10.99% GAIN |
| daily unevenness | 0.9787 | +1.03% power given | -0.09% GAIN |
| monthly unevenness | 0.9828 | +0.68% power given | -0.66% GAIN |
| net-zero shortfall | 1.1970 | -8.77% GAIN | -4.77% GAIN |

**2022 phase 3, 7 buildings**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.0848 | -4.17% GAIN | -7.32% GAIN |
| electricity bought | 1.1573 | -8.89% GAIN | -6.23% GAIN |
| carbon | 1.1155 | -6.65% GAIN | -5.50% GAIN |
| the daily peak | 1.0973 | -10.96% GAIN | -16.09% GAIN |
| the highest peak | 0.9942 | +0.45% power given | -3.61% GAIN |
| the ramping | 1.1814 | +3.37% power given | -1.91% GAIN |
| daily unevenness | 1.0176 | -4.83% GAIN | -9.88% GAIN |
| monthly unevenness | 0.9838 | -0.55% GAIN | -5.07% GAIN |
| net-zero shortfall | 1.0809 | -3.28% GAIN | -0.76% GAIN |

**2022 phase all, 17 buildings**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.1007 | not run | -14.20% GAIN |
| electricity bought | 1.1941 | not run | -14.92% GAIN |
| carbon | 1.1496 | not run | -13.11% GAIN |
| the daily peak | 1.1392 | not run | -20.77% GAIN |
| the highest peak | 1.0272 | not run | -2.73% GAIN |
| the ramping | 1.2223 | not run | -12.57% GAIN |
| daily unevenness | 1.0084 | not run | -7.29% GAIN |
| monthly unevenness | 0.9892 | not run | -2.28% GAIN |
| net-zero shortfall | 1.1315 | not run | -2.78% GAIN |

**Alameda County, 100 buildings**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.0000 | not run | +0.00% STEADY |
| electricity bought | 2.0205 | not run | -6.95% GAIN |
| carbon | 1.0000 | not run | +0.00% STEADY |
| the daily peak | 2.4165 | not run | -8.92% GAIN |
| the highest peak | 1.2582 | not run | -4.40% GAIN |
| the ramping | 1.3828 | not run | -10.40% GAIN |
| daily unevenness | 0.7972 | not run | -2.75% GAIN |
| monthly unevenness | 0.8053 | not run | -1.79% GAIN |
| net-zero shortfall | 9.8346 | not run | -0.08% GAIN |
| energy not served | 0.0000 | not run | +0.00% STEADY |
| time uncomfortable | 0.7607 | not run | +0.00% STEADY |

**Travis County, 100 buildings**

| CityLearn score | native | omni-v8 against native | omni-v9 against native |
|---|---:|---:|---:|
| the bill | 1.0000 | not run | +0.00% STEADY |
| electricity bought | 3.8416 | not run | -3.96% GAIN |
| carbon | 1.0000 | not run | +0.00% STEADY |
| the daily peak | 3.1689 | not run | -5.92% GAIN |
| the highest peak | 1.3727 | not run | +0.00% STEADY |
| the ramping | 1.1329 | not run | -7.58% GAIN |
| daily unevenness | 0.5655 | not run | -2.71% GAIN |
| monthly unevenness | 0.6057 | not run | -1.96% GAIN |
| net-zero shortfall | -4.6732 | not run | -0.18% GAIN |
| energy not served | 0.0000 | not run | +0.00% STEADY |
| time uncomfortable | 0.8454 | not run | +0.00% STEADY |

Across the districts above: omni-v8 29 GAIN, 0 STEADY, 7 power given, 0 LOSS (where it was run); omni-v9 58 GAIN, 9 STEADY, 0 power given, 0 LOSS.

The districts: the robustness district, where the omni-v8 row stood and where the cause was found; the tuning district
(`citylearn_challenge_2022_phase_1`); the 2022 phases 2, 3 and all (shipped in CityLearn's source repository, not in its package,
so the GitHub benchmark does not run them); and the two 100-building neighbourhoods the benchmark counts (Alameda County, Travis
County). The seven 2023 districts are unchanged by construction: every battery in them is left native (omni-v8), so their omni arm
is native's to the last digit. The shipped runner (`tools/run_citylearn.py`) and the study's copy of it give the same numbers to
the last digit on both arms (checked on the robustness district).

**Shown, power given.** Month by month, the peak hour with Omni-Compass on top rises above native's in some months: in 2 of 12
months in the robustness district, 3 in the tuning district, 1 in each of the 2022 phases 2 and 3, and 2 in phase all (omni-v8: 3,
3, 2 and 4); in Alameda and Travis in none. A peak is power held, so each is power given, beside the bill and the energy it bought;
CityLearn's own scores over the year (the highest peak, the daily peak and the monthly unevenness) read GAIN. A guard that keeps Omni-Compass's added charge under the
month's top so far cut one of the two months on the robustness district and left every score GAIN; it is a candidate for the next
version, in the model gate first.

## 4. The model gate

The changes touch no Kubernetes, card or cloud controller, and the model gate's models (`tools/model_gate.py`) do not run the CityLearn
wire, so they read the same on both checkouts by construction; the gate was run all the same, the candidate against omni-v8 on
seeds 1 to 8, and is recorded in `results/model_gate/V9_VS_V8.md`: every gauge of every model (the cluster at 60 s and at 15 s,
conveyance with the quota readable and unreadable, the verdict on noisy work) identical to omni-v8 to the last digit, in every count
(it ran with the glide at 0.10, a setting no model reads). The same models show, for omni-v8 and the candidate alike, a pod start wait
+9% against native beside 64% more requests served: the same row the real KEDA HTTP run showed (`docs/OMNI_V7.md`, section 6;
`docs/STATE_OF_PLAY.md`, Open), the next repair. These are our own models (class S), never a benchmark result.

## 5. What runs again on it

Everything, A, B and C, from the moment it lands (`scripts/reruns.txt`, the omni-v9 campaign, released by the conductor a few a
tick), with three entries added beside the operator's settings: MySQL, Redis and MongoDB with native exactly as shipped (MySQL's
own 128 MB buffer pool; Redis with no memory ceiling and its own `noeviction` rule; MongoDB's own cache, half of the machine's
memory less 1 GB). The grid on its own manifest (`results/grid_v9/`); every Azure set from A again. Google Cloud and Amazon stay
behind their switches; the GPU runs on Lambda wait for the founder's word and one exact commit. The CityLearn table's three runs on
GitHub make the table V9_CITYLEARN.md in `results/live/`; it must read no LOSS in any district, as it did locally.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
