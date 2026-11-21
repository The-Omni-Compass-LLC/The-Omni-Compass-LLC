# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.0625 an hour, reading the coming hour from the same hour of the past 7 days, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

## baeda_3dem: 4 buildings, 2,928 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.3109 | 1.3109 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.3784 | 1.3784 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.0854 | 1.0854 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 0.8848 | 0.8848 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.1344 | 1.1344 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7120 | 0.7120 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6930 | 0.6930 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 1.4067 | 1.4067 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8142 | 0.8142 | +0.00% | same |

## ca_alameda_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.0205 | 1.8800 | -6.95% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.4165 | 2.2009 | -8.92% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2582 | 1.2029 | -4.40% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.3828 | 1.2390 | -10.40% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7972 | 0.7753 | -2.75% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8053 | 0.7909 | -1.79% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 9.8346 | 9.8265 | -0.08% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.7607 | 0.7607 | +0.00% | same |

## citylearn_challenge_2022_phase_all_demand_response: not run to the end

- native: ValueError: demand_response.enabled=true requires interface='entity'.
- omni: ValueError: demand_response.enabled=true requires interface='entity'.

## citylearn_challenge_2022_phase_all_plus_evs: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

## citylearn_challenge_2022_phase_all_robustness: 17 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1008 | 0.9442 | -14.22% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1938 | 1.0157 | -14.92% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1494 | 0.9987 | -13.11% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1392 | 0.9020 | -20.82% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0272 | 0.9991 | -2.73% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2231 | 1.0690 | -12.60% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0084 | 0.9346 | -7.32% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9892 | 0.9666 | -2.29% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1312 | 1.1001 | -2.76% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 720 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8431 | 1.8431 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.9002 | 1.9002 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.8899 | 1.8899 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.3288 | 1.3288 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9236 | 0.9236 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7080 | 0.7080 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8341 | 0.8341 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 1.9420 | 1.9420 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0175 | 0.0175 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9466 | 0.9466 | +0.00% | same |

## citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1270 | 2.1270 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.2130 | 2.2130 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.2157 | 2.2157 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.4144 | 1.4144 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9463 | 0.9463 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6825 | 0.6825 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2387 | 2.2387 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0048 | 0.0048 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9889 | 0.9889 | +0.00% | same |

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1257 | 2.1257 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.2118 | 2.2118 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.2146 | 2.2146 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.4122 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9456 | 0.9456 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6831 | 0.6831 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2484 | 2.2484 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0070 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9863 | +0.00% | same |

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1288 | 2.1288 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.2124 | 2.2124 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2152 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.4148 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9474 | 0.9474 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6834 | 0.6834 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2403 | 2.2403 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0043 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9879 | +0.00% | same |

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1117 | 2.1117 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.1912 | 2.1912 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.1970 | 2.1970 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5367 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9721 | 0.9721 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6461 | 0.6461 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7298 | 0.7298 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2516 | 2.2516 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0154 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9828 | +0.00% | same |

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1119 | 2.1119 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.1877 | 2.1877 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.1918 | 2.1918 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5404 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9763 | 0.9763 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6467 | 0.6467 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7316 | 0.7316 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2432 | 2.2432 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0130 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9875 | +0.00% | same |

## citylearn_challenge_2023_phase_3_3: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1116 | 2.1116 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.1890 | 2.1890 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 2.1930 | 2.1930 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.5391 | 1.5391 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9799 | 0.9799 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6520 | 0.6520 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7288 | 0.7288 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.2353 | 2.2353 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0109 | 0.0109 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9844 | 0.9844 | +0.00% | same |

## citylearn_three_phase_dynamic_asset_changes_demo_15s_parquet: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_dynamic_assets_only_demo: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_dynamic_assets_only_demo_15s_parquet: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_dynamic_topology_demo: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_electrical_service_demo: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

## citylearn_three_phase_electrical_service_demo_15s_parquet: not run to the end

- native: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.
- omni: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.

## quebec_neighborhood_with_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |
| time uncomfortable (`discomfort_proportion`) | 0.8176 | 0.8195 | +0.24% | higher: more time uncomfortable |

## quebec_neighborhood_without_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |
| time uncomfortable (`discomfort_proportion`) | 0.8092 | 0.8110 | +0.23% | higher: more time uncomfortable |

## tx_travis_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 3.8416 | 3.6896 | -3.96% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 3.1689 | 2.9814 | -5.92% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.3727 | 1.3727 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.1329 | 1.0470 | -7.58% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.5655 | 0.5501 | -2.71% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6057 | 0.5938 | -1.96% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.6732 | -4.6814 | -0.18% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8454 | 0.8454 | +0.00% | same |

## vt_chittenden_county_neighborhood: 47 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.6684 | 2.5986 | -2.61% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 3.7796 | 3.6933 | -2.28% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.1374 | 1.1374 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.4785 | 1.4344 | -2.99% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.4318 | 0.4289 | -0.65% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.5042 | 0.5014 | -0.56% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.7935 | -4.8117 | -0.38% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8552 | 0.8552 | +0.00% | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 1 of 14 | 0 of 14 | -1.02% |
| electricity bought | 4 of 14 | 0 of 14 | -2.03% |
| carbon | 1 of 14 | 0 of 14 | -0.94% |
| daily peak draw | 4 of 14 | 0 of 14 | -2.71% |
| highest peak | 2 of 14 | 0 of 14 | -0.51% |
| ramping (swings hour to hour) | 4 of 14 | 0 of 14 | -2.40% |
| daily load unevenness | 4 of 14 | 0 of 14 | -0.96% |
| monthly load unevenness | 4 of 14 | 0 of 14 | -0.47% |
| distance from zero net energy | 4 of 14 | 0 of 14 | -0.24% |
| energy not served | 0 of 11 | 0 of 11 | +0.00% |
| time uncomfortable | 0 of 13 | 2 of 13 | +0.04% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
