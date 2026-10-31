# CityLearn, every district: the A/B/C three-run table (Omni v1)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

CityLearn (University of Texas at Austin) is an independent, deterministic simulator of real buildings with its own controller (BasicRBC) and its own scores; every score reads the aim is lower. Native is that controller; omni is the same controller with the compass law on top of its electric battery commands only (`tools/run_citylearn.py`). The same districts ran three times as separate GitHub runs on the same frozen engine. Because the simulator is deterministic, the runs must reproduce each other: a score reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)) when all three runs give the same sign, **STEADY, the same** when the change is under one part in a million, and **the runs differ** when they do not reproduce, which is a finding about the simulator or the harness and is said so. A district with no electric battery gets nothing from Omni (a water tank stays native), so any native/omni difference in it is CityLearn's own run-to-run variation, never an Omni result. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Districts in the run |
|---|---|---|---|---:|
| A | 37384954241 | `f162ce8d74e8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 22 |
| B | 37393198549 | `31aa85c3c46e` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 22 |
| C | 37399402398 | `62fc47335ac8` | omni-v1 (digest ccc7fbdf8b312ed7, 38 files) | 22 |

## Districts with electric batteries: omni against native, each run

### ca_alameda_county_neighborhood: 100 buildings, 100 batteries, 4 water tanks left native, 8,760 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -5.88% | -5.88% | -5.88% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -3.61% | -3.61% | -3.61% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.05% | -3.05% | -3.05% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -3.94% | -3.94% | -3.94% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -0.97% | -0.97% | -0.97% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.72% | -0.72% | -0.72% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.10% | -0.10% | -0.10% | STEADY, under the floor (the three runs' mean 0.10%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2022_phase_all_robustness: 17 buildings, 17 batteries, 0 water tanks left native, 8,760 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | -8.61% | -8.61% | -8.61% | **GAIN in all three of our runs** |
| electricity bought (`electricity_consumption_total`) | -14.66% | -14.66% | -14.66% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | -11.89% | -11.89% | -11.89% | **GAIN in all three of our runs** |
| daily peak draw (`daily_peak_average`) | -13.95% | -13.95% | -13.95% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -2.73% | -2.73% | -2.73% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -7.18% | -7.18% | -7.18% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.90% | -2.90% | -2.90% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.11% | +0.11% | +0.11% | STEADY, under the floor (the three runs' mean 0.11%) |
| distance from zero net energy (`zero_net_energy`) | -6.10% | -6.10% | -6.10% | **GAIN in all three of our runs** |

### citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 3 batteries, 3 water tanks left native, 720 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.35% | +0.35% | +0.35% | STEADY, under the floor (the three runs' mean 0.35%) |
| electricity bought (`electricity_consumption_total`) | -0.27% | -0.27% | -0.27% | STEADY, under the floor (the three runs' mean 0.27%) |
| carbon (`carbon_emissions_total`) | -0.17% | -0.17% | -0.17% | STEADY, under the floor (the three runs' mean 0.17%) |
| daily peak draw (`daily_peak_average`) | -1.61% | -1.61% | -1.61% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +6.24% | +6.24% | +6.24% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.86% | -2.86% | -2.86% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.07% | +0.07% | +0.07% | STEADY, under the floor (the three runs' mean 0.07%) |
| distance from zero net energy (`zero_net_energy`) | -0.06% | -0.06% | -0.06% | STEADY, under the floor (the three runs' mean 0.06%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +5.96% | +5.96% | +5.96% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.12% | +0.12% | +0.12% | STEADY, under the floor (the three runs' mean 0.12%) |

### citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.34% | +0.34% | +0.34% | STEADY, under the floor (the three runs' mean 0.34%) |
| electricity bought (`electricity_consumption_total`) | -0.15% | -0.15% | -0.15% | STEADY, under the floor (the three runs' mean 0.15%) |
| carbon (`carbon_emissions_total`) | -0.16% | -0.16% | -0.16% | STEADY, under the floor (the three runs' mean 0.16%) |
| daily peak draw (`daily_peak_average`) | -1.34% | -1.34% | -1.34% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.56% | +5.56% | +5.56% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.05% | -2.05% | -2.05% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.07% | -0.07% | -0.07% | STEADY, under the floor (the three runs' mean 0.07%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +5.50% | +5.50% | +5.50% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.02% | +0.02% | +0.02% | STEADY, under the floor (the three runs' mean 0.02%) |

### citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.32% | +0.32% | +0.32% | STEADY, under the floor (the three runs' mean 0.32%) |
| electricity bought (`electricity_consumption_total`) | -0.18% | -0.18% | -0.18% | STEADY, under the floor (the three runs' mean 0.18%) |
| carbon (`carbon_emissions_total`) | -0.17% | -0.17% | -0.17% | STEADY, under the floor (the three runs' mean 0.17%) |
| daily peak draw (`daily_peak_average`) | -1.30% | -1.30% | -1.30% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.60% | +5.60% | +5.60% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -1.67% | -1.67% | -1.67% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.07% | -0.07% | -0.07% | STEADY, under the floor (the three runs' mean 0.07%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +6.25% | +6.25% | +6.25% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.15% | +0.15% | +0.15% | STEADY, under the floor (the three runs' mean 0.15%) |

### citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.30% | +0.30% | +0.30% | STEADY, under the floor (the three runs' mean 0.30%) |
| electricity bought (`electricity_consumption_total`) | -0.17% | -0.17% | -0.17% | STEADY, under the floor (the three runs' mean 0.17%) |
| carbon (`carbon_emissions_total`) | -0.18% | -0.18% | -0.18% | STEADY, under the floor (the three runs' mean 0.18%) |
| daily peak draw (`daily_peak_average`) | -1.54% | -1.54% | -1.54% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.45% | +5.45% | +5.45% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.26% | -2.26% | -2.26% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.06% | -0.06% | -0.06% | STEADY, under the floor (the three runs' mean 0.06%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +9.80% | +9.80% | +9.80% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | -0.01% | -0.01% | -0.01% | STEADY, under the floor (the three runs' mean 0.01%) |

### citylearn_challenge_2023_phase_3_1: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.26% | +0.26% | +0.26% | STEADY, under the floor (the three runs' mean 0.26%) |
| electricity bought (`electricity_consumption_total`) | -0.10% | -0.10% | -0.10% | STEADY, under the floor (the three runs' mean 0.10%) |
| carbon (`carbon_emissions_total`) | -0.13% | -0.13% | -0.13% | STEADY, under the floor (the three runs' mean 0.13%) |
| daily peak draw (`daily_peak_average`) | -2.20% | -2.20% | -2.20% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.51% | +4.51% | +4.51% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -3.96% | -3.96% | -3.96% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.18% | -1.18% | -1.18% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.02% | -0.02% | -0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +1.97% | +1.97% | +1.97% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.02% | +0.02% | +0.02% | STEADY, under the floor (the three runs' mean 0.02%) |

### citylearn_challenge_2023_phase_3_2: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.19% | +0.19% | +0.19% | STEADY, under the floor (the three runs' mean 0.19%) |
| electricity bought (`electricity_consumption_total`) | -0.10% | -0.10% | -0.10% | STEADY, under the floor (the three runs' mean 0.10%) |
| carbon (`carbon_emissions_total`) | -0.12% | -0.12% | -0.12% | STEADY, under the floor (the three runs' mean 0.12%) |
| daily peak draw (`daily_peak_average`) | -2.18% | -2.18% | -2.18% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.89% | +4.89% | +4.89% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -4.14% | -4.14% | -4.14% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.53% | -0.53% | -0.53% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | +0.04% | +0.04% | +0.04% | STEADY, under the floor (the three runs' mean 0.04%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +4.14% | +4.14% | +4.14% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.09% | +0.09% | +0.09% | STEADY, under the floor (the three runs' mean 0.09%) |

### citylearn_challenge_2023_phase_3_3: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.26% | +0.26% | +0.26% | STEADY, under the floor (the three runs' mean 0.26%) |
| electricity bought (`electricity_consumption_total`) | -0.07% | -0.07% | -0.07% | STEADY, under the floor (the three runs' mean 0.07%) |
| carbon (`carbon_emissions_total`) | -0.08% | -0.08% | -0.08% | STEADY, under the floor (the three runs' mean 0.08%) |
| daily peak draw (`daily_peak_average`) | -2.56% | -2.56% | -2.56% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.79% | +4.79% | +4.79% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -4.68% | -4.68% | -4.68% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.96% | -0.96% | -0.96% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.01% | -0.01% | -0.01% | STEADY, under the floor (the three runs' mean 0.01%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +2.22% | +2.22% | +2.22% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.01% | +0.01% | +0.01% | STEADY, under the floor (the three runs' mean 0.01%) |

### tx_travis_county_neighborhood: 100 buildings, 100 batteries, 39 water tanks left native, 8,760 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -3.00% | -3.00% | -3.00% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | -2.91% | -2.91% | -2.91% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -1.15% | -1.15% | -1.15% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.71% | -0.71% | -0.71% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.58% | -0.58% | -0.58% | **GAIN in all three of our runs** |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | **the runs differ** |

### vt_chittenden_county_neighborhood: 47 buildings, 47 batteries, 11 water tanks left native, 8,760 hours

| CityLearn score (the aim is lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -2.14% | -2.14% | -2.14% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -0.84% | -0.84% | -0.84% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | -1.27% | -1.27% | -1.27% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -0.31% | -0.31% | -0.31% | STEADY, under the floor (the three runs' mean 0.31%) |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.23% | -0.23% | -0.23% | STEADY, under the floor (the three runs' mean 0.23%) |
| distance from zero net energy (`zero_net_energy`) | -0.33% | -0.33% | -0.33% | STEADY, under the floor (the three runs' mean 0.33%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | **the runs differ** |

## Across the districts with batteries

A district counts only when all three runs agree.

| CityLearn score | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---:|---:|---:|---:|---:|
| electricity bill | 1 | 0 | 7 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_2_online_evaluation_3, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 3 | 0 |
| electricity bought | 11 | 0 | 0 | 0 | 0 |
| carbon | 8 | 0 | 0 | 3 | 0 |
| daily peak draw | 11 | 0 | 0 | 0 | 0 |
| highest peak | 5 | 0 | 3 (citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 3 | 0 |
| ramping (swings hour to hour) | 4 | 0 | 7 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_2_online_evaluation_3, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 0 | 0 |
| daily load unevenness | 11 | 0 | 0 | 0 | 0 |
| monthly load unevenness | 9 | 2 (citylearn_challenge_2022_phase_all_robustness, citylearn_challenge_2023_phase_2_local_evaluation) | 0 | 0 | 0 |
| distance from zero net energy | 10 | 0 | 1 (citylearn_challenge_2023_phase_3_2) | 0 | 0 |
| energy not served | 0 | 7 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_2_online_evaluation_3, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 0 | 3 | 0 |
| time uncomfortable | 1 | 6 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 0 | 1 | 2 |

## Districts with no electric battery: nothing for Omni to move

The runner changes only `electrical_storage` commands, so in these districts omni applied nothing. Any difference between the arms is CityLearn's own run-to-run variation and says nothing about Omni; where the two arms agree, the simulator is deterministic there.

| District | Buildings | Water tanks (native) | Scores where native and omni differ in A | Reproduced over A, B, C |
|---|---:|---:|---|---|
| baeda_3dem | 4 | 7 | none | yes |
| quebec_neighborhood_with_demand_response_set_points | 20 | 0 | time uncomfortable -0.86% | no |
| quebec_neighborhood_without_demand_response_set_points | 20 | 0 | time uncomfortable +0.25% | no |

## Districts CityLearn cannot run with its own controller

The same for native and omni; listed, never dropped.

| District | CityLearn's own error |
|---|---|
| citylearn_challenge_2022_phase_all_demand_response | `ValueError: demand_response.enabled=true requires interface='entity'.` |
| citylearn_challenge_2022_phase_all_plus_evs | `ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1` |
| citylearn_three_phase_dynamic_asset_changes_demo_15s_parquet | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_assets_only_demo | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_assets_only_demo_15s_parquet | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_topology_demo | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_electrical_service_demo | `ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1` |
| citylearn_three_phase_electrical_service_demo_15s_parquet | `FileNotFoundError: [Errno 2] Failed to open local file '/tmp/cl/data/datasets/citylearn_three_phase_electrical_service_d` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
