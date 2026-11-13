# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

## baeda_3dem: 4 buildings, 2,928 hours

Omni-Compass moved the commands in 2,606 hours; every command handed back at 90%: yes.

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

Omni-Compass moved the commands in 7,860 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.0205 | 1.9018 | -5.88% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.4165 | 2.3293 | -3.61% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2582 | 1.2199 | -3.05% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.3828 | 1.3283 | -3.94% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7972 | 0.7895 | -0.97% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8053 | 0.7995 | -0.72% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 9.8346 | 9.8251 | -0.10% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.7607 | 0.7607 | +0.00% | same |

## citylearn_challenge_2022_phase_all_demand_response: not run to the end

- native: ValueError: demand_response.enabled=true requires interface='entity'.
- omni: ValueError: demand_response.enabled=true requires interface='entity'.

## citylearn_challenge_2022_phase_all_plus_evs: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

## citylearn_challenge_2022_phase_all_robustness: 17 buildings, 8,760 hours

Omni-Compass moved the commands in 7,851 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1008 | 1.0060 | -8.61% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1938 | 1.0188 | -14.66% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1494 | 1.0128 | -11.89% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1392 | 0.9802 | -13.95% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0272 | 0.9991 | -2.73% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2231 | 1.1353 | -7.18% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0084 | 0.9792 | -2.90% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9892 | 0.9903 | +0.11% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1312 | 1.0622 | -6.10% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 720 hours

Omni-Compass moved the commands in 625 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8431 | 1.8496 | +0.35% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.9002 | 1.8951 | -0.27% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.8899 | 1.8866 | -0.17% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.3288 | 1.3074 | -1.61% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9236 | 0.9813 | +6.24% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7080 | 0.6878 | -2.86% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8341 | 0.8347 | +0.07% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.9420 | 1.9408 | -0.06% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0175 | 0.0185 | +5.96% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9466 | 0.9477 | +0.12% | higher: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1270 | 2.1342 | +0.34% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2130 | 2.2098 | -0.15% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2157 | 2.2122 | -0.16% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4144 | 1.3954 | -1.34% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9463 | 0.9989 | +5.56% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6825 | 0.6685 | -2.05% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7542 | -1.88% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2387 | 2.2371 | -0.07% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0048 | 0.0051 | +5.50% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9889 | 0.9891 | +0.02% | higher: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1257 | 2.1326 | +0.32% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2118 | 2.2078 | -0.18% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2146 | 2.2109 | -0.17% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.3937 | -1.30% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9456 | 0.9986 | +5.60% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6831 | 0.6718 | -1.67% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2484 | 2.2468 | -0.07% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0075 | +6.25% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9877 | +0.15% | higher: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1288 | 2.1352 | +0.30% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2124 | 2.2087 | -0.17% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2112 | -0.18% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.3931 | -1.54% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9474 | 0.9990 | +5.45% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6834 | 0.6680 | -2.26% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2403 | 2.2389 | -0.06% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0047 | +9.80% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9878 | -0.01% | lower: less time uncomfortable |

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1117 | 2.1171 | +0.26% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1912 | 2.1889 | -0.10% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1970 | 2.1941 | -0.13% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5029 | -2.20% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9721 | 1.0159 | +4.51% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6461 | 0.6205 | -3.96% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7298 | 0.7212 | -1.18% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2516 | 2.2511 | -0.02% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0157 | +1.97% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9830 | +0.02% | higher: more time uncomfortable |

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1119 | 2.1159 | +0.19% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1877 | 2.1856 | -0.10% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1918 | 2.1891 | -0.12% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5068 | -2.18% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9763 | 1.0241 | +4.89% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6467 | 0.6199 | -4.14% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7316 | 0.7278 | -0.53% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2432 | 2.2440 | +0.04% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0136 | +4.14% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9884 | +0.09% | higher: more time uncomfortable |

## citylearn_challenge_2023_phase_3_3: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1116 | 2.1170 | +0.26% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1890 | 2.1876 | -0.07% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1930 | 2.1912 | -0.08% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5391 | 1.4997 | -2.56% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9799 | 1.0269 | +4.79% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6520 | 0.6215 | -4.68% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7288 | 0.7218 | -0.96% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2353 | 2.2351 | -0.01% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0109 | 0.0111 | +2.22% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9844 | 0.9844 | +0.01% | higher: more time uncomfortable |

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

Omni-Compass moved the commands in 1,914 hours; every command handed back at 90%: yes.

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
| time uncomfortable (`discomfort_proportion`) | 0.8162 | 0.8184 | +0.26% | higher: more time uncomfortable |

## quebec_neighborhood_without_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 1,914 hours; every command handed back at 90%: yes.

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
| time uncomfortable (`discomfort_proportion`) | 0.8121 | 0.8141 | +0.24% | higher: more time uncomfortable |

## tx_travis_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,860 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 3.8416 | 3.7262 | -3.00% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 3.1689 | 3.1095 | -1.88% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.3727 | 1.3727 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.1329 | 1.1000 | -2.91% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.5655 | 0.5590 | -1.15% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6057 | 0.6014 | -0.71% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.6732 | -4.7001 | -0.58% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8454 | 0.8454 | +0.00% | same |

## vt_chittenden_county_neighborhood: 47 buildings, 8,760 hours

Omni-Compass moved the commands in 7,860 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.6684 | 2.6112 | -2.14% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 3.7796 | 3.7479 | -0.84% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.1374 | 1.1374 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.4785 | 1.4597 | -1.27% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.4318 | 0.4304 | -0.31% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.5042 | 0.5031 | -0.23% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | -4.7935 | -4.8095 | -0.33% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8552 | 0.8552 | +0.00% | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 1 of 14 | 7 of 14 | -0.47% |
| electricity bought | 11 of 14 | 0 of 14 | -1.91% |
| carbon | 8 of 14 | 0 of 14 | -0.92% |
| daily peak draw | 11 of 14 | 0 of 14 | -2.36% |
| highest peak | 5 of 14 | 3 of 14 | -0.62% |
| ramping (swings hour to hour) | 4 of 14 | 7 of 14 | +1.55% |
| daily load unevenness | 11 of 14 | 0 of 14 | -1.92% |
| monthly load unevenness | 9 of 14 | 2 of 14 | -0.70% |
| distance from zero net energy | 10 of 14 | 1 of 14 | -0.53% |
| energy not served | 0 of 11 | 7 of 11 | +3.26% |
| time uncomfortable | 1 of 13 | 8 of 13 | +0.07% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
