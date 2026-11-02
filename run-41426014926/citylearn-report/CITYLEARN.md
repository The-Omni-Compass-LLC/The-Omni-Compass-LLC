# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.0875 an hour, reading the coming hour from the same hour of the past 7 days, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, read by the one key: a fall is a GAIN; a rise in energy not served or time uncomfortable is a LOSS, a rise in any other score (a resource spent or held) is power given. Evidence class: an independent recognized simulator (not our model).

## baeda_3dem: 4 buildings, 2,928 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.3109 | 1.3109 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 1.3784 | 1.3784 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.0854 | 1.0854 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 0.8848 | 0.8848 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.1344 | 1.1344 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7120 | 0.7120 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6930 | 0.6930 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 1.4067 | 1.4067 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8142 | 0.8142 | +0.00% | STEADY |

## ca_alameda_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.0205 | 1.8766 | -7.12% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.4165 | 2.2564 | -6.62% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2582 | 1.2034 | -4.36% | GAIN: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.3828 | 1.2428 | -10.13% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7972 | 0.7804 | -2.11% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8053 | 0.7947 | -1.32% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 9.8346 | 9.8369 | +0.02% | power given: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.7607 | 0.7607 | +0.00% | STEADY |

## citylearn_challenge_2022_phase_all_demand_response: not run to the end

- native: ValueError: demand_response.enabled=true requires interface='entity'.
- omni: ValueError: demand_response.enabled=true requires interface='entity'.

## citylearn_challenge_2022_phase_all_plus_evs: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

## citylearn_challenge_2022_phase_all_robustness: 17 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1008 | 0.9236 | -16.09% | GAIN: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1938 | 1.0317 | -13.58% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1494 | 1.0106 | -12.07% | GAIN: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1392 | 0.9465 | -16.92% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0272 | 0.9991 | -2.73% | GAIN: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2231 | 1.1080 | -9.41% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0084 | 0.9477 | -6.02% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9892 | 0.9735 | -1.59% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1312 | 1.1203 | -0.96% | GAIN: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | STEADY |

## citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 720 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8431 | 1.8431 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 1.9002 | 1.9002 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.8899 | 1.8899 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.3288 | 1.3288 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9236 | 0.9236 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7080 | 0.7080 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8341 | 0.8341 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 1.9420 | 1.9420 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0175 | 0.0175 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9466 | 0.9466 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1270 | 2.1270 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2130 | 2.2130 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2157 | 2.2157 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4144 | 1.4144 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9463 | 0.9463 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6825 | 0.6825 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2387 | 2.2387 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0048 | 0.0048 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9889 | 0.9889 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1257 | 2.1257 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2118 | 2.2118 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2146 | 2.2146 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.4122 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9456 | 0.9456 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6831 | 0.6831 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2484 | 2.2484 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0070 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9863 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1288 | 2.1288 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2124 | 2.2124 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2152 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.4148 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9474 | 0.9474 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6834 | 0.6834 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7687 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2403 | 2.2403 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0043 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9879 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1117 | 2.1117 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1912 | 2.1912 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1970 | 2.1970 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5367 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9721 | 0.9721 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6461 | 0.6461 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7298 | 0.7298 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2516 | 2.2516 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0154 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9828 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1119 | 2.1119 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1877 | 2.1877 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1918 | 2.1918 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5404 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9763 | 0.9763 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6467 | 0.6467 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7316 | 0.7316 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2432 | 2.2432 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0130 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9875 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_3: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1116 | 2.1116 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1890 | 2.1890 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1930 | 2.1930 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5391 | 1.5391 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9799 | 0.9799 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6520 | 0.6520 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7288 | 0.7288 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2353 | 2.2353 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0109 | 0.0109 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9844 | 0.9844 | +0.00% | STEADY |

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

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8172 | 0.8174 | +0.02% | LOSS: more time uncomfortable |

## quebec_neighborhood_without_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8105 | 0.8085 | -0.25% | GAIN: less time uncomfortable |

## tx_travis_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 3.8416 | 3.6867 | -4.03% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 3.1689 | 2.9428 | -7.13% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.3727 | 1.3727 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.1329 | 1.0349 | -8.65% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.5655 | 0.5467 | -3.32% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6057 | 0.5918 | -2.30% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.6732 | -4.6800 | -0.15% | GAIN: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8454 | 0.8454 | +0.00% | STEADY |

## vt_chittenden_county_neighborhood: 47 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.6684 | 2.5893 | -2.96% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 3.7796 | 3.6600 | -3.16% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.1374 | 1.1374 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.4785 | 1.4283 | -3.40% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.4318 | 0.4280 | -0.88% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.5042 | 0.5003 | -0.77% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.7935 | -4.8146 | -0.44% | GAIN: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8552 | 0.8552 | +0.00% | STEADY |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts where it fell | Districts where it rose | Mean change | A rise reads |
|---|---:|---:|---:|---|
| electricity bill | 1 of 14 | 0 of 14 | -1.15% | power given |
| electricity bought | 4 of 14 | 0 of 14 | -1.98% | power given |
| carbon | 1 of 14 | 0 of 14 | -0.86% | power given |
| daily peak draw | 4 of 14 | 0 of 14 | -2.42% | power given |
| highest peak | 2 of 14 | 0 of 14 | -0.51% | power given |
| ramping (swings hour to hour) | 4 of 14 | 0 of 14 | -2.26% | power given |
| daily load unevenness | 4 of 14 | 0 of 14 | -0.88% | power given |
| monthly load unevenness | 4 of 14 | 0 of 14 | -0.43% | power given |
| distance from zero net energy | 3 of 14 | 1 of 14 | -0.11% | power given |
| energy not served | 0 of 11 | 0 of 11 | +0.00% | LOSS |
| time uncomfortable | 1 of 13 | 1 of 13 | -0.02% | LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
