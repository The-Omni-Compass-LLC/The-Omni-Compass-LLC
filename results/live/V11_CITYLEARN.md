# CityLearn, every district: the A/B/C three-run table (Omni v11)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

CityLearn (University of Texas at Austin) is an independent, deterministic simulator of real buildings with its own controller (BasicRBC) and its own scores; every score is one CityLearn itself aims lower. Native is that controller; omni is the same controller with the compass law on top of its electric battery commands only (`tools/run_citylearn.py`). The same districts ran three times as separate GitHub runs on the same frozen engine. Because the simulator is deterministic, the runs must reproduce each other: a score reads **GAIN** or **LOSS in all three of our runs** when all three runs give the same sign, judged by what the score is for and never by its sign: the electricity bought, the bill, the carbon, the peaks, the swings and the unevenness are the power the district draws and holds and the wear of moving it, so a fall is a cut, a GAIN, and a rise is **power given**; a rise in the energy not served or the time uncomfortable (the occupants' misses) is a LOSS. **STEADY, the same** when the change is under one part in a million, and **the runs differ** when they do not reproduce, which is a finding about the simulator or the harness and is said so. A district with no electric battery gets nothing from Omni (a water tank stays native), so any native/omni difference in it is CityLearn's own run-to-run variation, never an Omni result. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Districts in the run |
|---|---|---|---|---:|
| A | 39151678885 | `f4e831f73695` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 22 |
| B | 39160214971 | `773cd59cfdd2` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 22 |
| C | 39169874537 | `2b4c11e3aee0` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 22 |

## Districts with electric batteries: omni against native, each run

### ca_alameda_county_neighborhood: 100 buildings, 100 batteries, 4 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -7.12% | -7.12% | -7.12% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -6.62% | -6.62% | -6.62% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -4.36% | -4.36% | -4.36% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -10.13% | -10.13% | -10.13% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.11% | -2.11% | -2.11% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.32% | -1.32% | -1.32% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | +0.02% | +0.02% | +0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | **the runs differ** |

### citylearn_challenge_2022_phase_all_robustness: 17 buildings, 17 batteries, 0 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | -16.09% | -16.09% | -16.09% | **GAIN in all three of our runs** |
| electricity bought (`electricity_consumption_total`) | -13.58% | -13.58% | -13.58% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | -12.07% | -12.07% | -12.07% | **GAIN in all three of our runs** |
| daily peak draw (`daily_peak_average`) | -16.92% | -16.92% | -16.92% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -2.73% | -2.73% | -2.73% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -9.41% | -9.41% | -9.41% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -6.02% | -6.02% | -6.02% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.59% | -1.59% | -1.59% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.96% | -0.96% | -0.96% | **GAIN in all three of our runs** |

### citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 3 batteries, 3 water tanks left native, 720 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_3_1: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_3_2: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### citylearn_challenge_2023_phase_3_3: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| distance from zero net energy (`zero_net_energy`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

### tx_travis_county_neighborhood: 100 buildings, 100 batteries, 39 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -4.03% | -4.03% | -4.03% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -7.13% | -7.13% | -7.13% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | -8.65% | -8.65% | -8.65% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -3.32% | -3.32% | -3.32% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -2.30% | -2.30% | -2.30% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.15% | -0.15% | -0.15% | STEADY, under the floor (the three runs' mean 0.15%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | **the runs differ** |

### vt_chittenden_county_neighborhood: 47 buildings, 47 batteries, 11 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| electricity bought (`electricity_consumption_total`) | -2.96% | -2.96% | -2.96% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| daily peak draw (`daily_peak_average`) | -3.16% | -3.16% | -3.16% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| ramping (swings hour to hour) (`ramping_average`) | -3.40% | -3.40% | -3.40% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -0.88% | -0.88% | -0.88% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.77% | -0.77% | -0.77% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.44% | -0.44% | -0.44% | STEADY, under the floor (the three runs' mean 0.44%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | STEADY, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | STEADY, the same |

## Across the districts with batteries

A district counts only when all three runs agree.

| CityLearn score | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---:|---:|---:|---:|---:|
| electricity bill | 1 | 0 | 0 | 10 | 0 |
| electricity bought | 4 | 0 | 0 | 7 | 0 |
| carbon | 1 | 0 | 0 | 10 | 0 |
| daily peak draw | 4 | 0 | 0 | 7 | 0 |
| highest peak | 2 | 0 | 0 | 9 | 0 |
| ramping (swings hour to hour) | 4 | 0 | 0 | 7 | 0 |
| daily load unevenness | 4 | 0 | 0 | 7 | 0 |
| monthly load unevenness | 4 | 0 | 0 | 7 | 0 |
| distance from zero net energy | 3 | 0 | 1 (ca_alameda_county_neighborhood) | 7 | 0 |
| energy not served | 0 | 0 | 0 | 10 | 0 |
| time uncomfortable | 0 | 0 | 0 | 8 | 2 |

Where **the runs differ** above with native and omni equal in every run, CityLearn's own value moved between the runs by the same amount in both arms; the paired change is exactly zero in A, B and C, so the row says nothing about Omni-Compass, and it stays as the preregistered rule reads it: ca_alameda_county_neighborhood, time uncomfortable (moved by at most 2.1e-05 between runs); tx_travis_county_neighborhood, time uncomfortable (moved by at most 3.6e-05 between runs).

## Districts with no electric battery: nothing for Omni to move

The runner changes only `electrical_storage` commands, so in these districts omni applied nothing. Any difference between the arms is CityLearn's own run-to-run variation and says nothing about Omni; where the two arms agree, the simulator is deterministic there.

| District | Buildings | Water tanks (native) | Scores where native and omni differ in A | Reproduced over A, B, C |
|---|---:|---:|---|---|
| baeda_3dem | 4 | 7 | none | yes |
| quebec_neighborhood_with_demand_response_set_points | 20 | 0 | time uncomfortable +0.00% | no |
| quebec_neighborhood_without_demand_response_set_points | 20 | 0 | time uncomfortable +0.07% | no |

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
| citylearn_three_phase_electrical_service_demo_15s_parquet | `ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV f` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
