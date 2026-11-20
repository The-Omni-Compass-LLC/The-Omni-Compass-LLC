# Omni-Compass on top of CityLearn's own controller

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

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
| electricity bought (`electricity_consumption_total`) | 1.8886 | 1.7540 | -7.13% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.3173 | 2.1631 | -6.65% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.1196 | 1.0707 | -4.37% | GAIN: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.4066 | 1.2643 | -10.12% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8304 | 0.8127 | -2.13% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8239 | 0.8129 | -1.34% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 7.0355 | 7.0401 | +0.06% | power given: more distance from zero net energy |
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
| electricity bill (`cost_total`) | 1.8442 | 1.8442 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 1.9015 | 1.9015 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.8913 | 1.8913 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.3289 | 1.3289 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9460 | 0.9460 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7227 | 0.7227 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8369 | 0.8369 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 1.9111 | 1.9111 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0175 | 0.0175 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9466 | 0.9466 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1271 | 2.1271 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2132 | 2.2132 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2159 | 2.2159 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4144 | 1.4144 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9526 | 0.9526 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6864 | 0.6864 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7696 | 0.7696 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2268 | 2.2268 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0048 | 0.0048 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9889 | 0.9889 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1258 | 2.1258 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2119 | 2.2119 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2147 | 2.2147 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.4122 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9521 | 0.9521 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6879 | 0.6879 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7702 | 0.7702 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2253 | 2.2253 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0070 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9863 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1289 | 2.1289 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.2125 | 2.2125 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2152 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.4148 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.2188 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9526 | 0.9526 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6864 | 0.6864 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7698 | 0.7698 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2261 | 2.2261 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0043 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9879 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1126 | 2.1126 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1918 | 2.1918 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1977 | 2.1977 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5367 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9943 | 0.9943 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6596 | 0.6596 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7347 | 0.7347 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2108 | 2.2108 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0154 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9828 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1129 | 2.1129 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1883 | 2.1883 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1924 | 2.1924 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5404 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9965 | 0.9965 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6613 | 0.6613 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7359 | 0.7359 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2072 | 2.2072 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0130 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9875 | +0.00% | STEADY |

## citylearn_challenge_2023_phase_3_3: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1125 | 2.1125 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1896 | 2.1896 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1935 | 2.1935 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5392 | 1.5392 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9946 | 0.9946 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6602 | 0.6602 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7319 | 0.7319 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2087 | 2.2087 | +0.00% | STEADY |
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

## pt_rec_100: not run to the end

- native: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.
- omni: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.

## pt_rec_15: not run to the end

- native: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.
- omni: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.

## pt_rec_30: not run to the end

- native: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.
- omni: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.

## pt_rec_4: not run to the end

- native: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.
- omni: ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV files in the schema.

## quebec_neighborhood_with_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.9392 | 1.9392 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.4969 | 2.4969 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.5160 | 2.5160 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.1151 | 1.1151 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 2.4386 | 2.4386 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0238 | 1.0238 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4919 | 0.4919 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.4969 | 2.4969 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8287 | 0.8287 | +0.00% | STEADY |

## quebec_neighborhood_without_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.9392 | 1.9392 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.4969 | 2.4969 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 2.5160 | 2.5160 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.1151 | 1.1151 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 2.4386 | 2.4386 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0238 | 1.0238 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4919 | 0.4919 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.4969 | 2.4969 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8231 | 0.8231 | +0.00% | STEADY |

## tx_travis_county_neighborhood: 100 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.6459 | 2.5392 | -4.03% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 3.0869 | 2.8670 | -7.12% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.1549 | 1.1549 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.6161 | 1.4764 | -8.65% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7805 | 0.7547 | -3.31% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7595 | 0.7420 | -2.31% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 12.2144 | 12.2364 | +0.18% | power given: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8454 | 0.8454 | +0.00% | STEADY |

## vt_chittenden_county_neighborhood: 47 buildings, 8,760 hours

Omni-Compass moved the commands in 7,861 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.3387 | 2.2697 | -2.95% | GAIN: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 3.7340 | 3.6159 | -3.16% | GAIN: less daily peak draw |
| highest peak (`all_time_peak_average`) | 0.9662 | 0.9662 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 1.9584 | 1.8921 | -3.39% | GAIN: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6555 | 0.6498 | -0.88% | GAIN: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6802 | 0.6750 | -0.77% | GAIN: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 8.7459 | 8.7882 | +0.48% | power given: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.8551 | 0.8551 | +0.00% | STEADY |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts where it fell | Districts where it rose | Mean change | A rise reads |
|---|---:|---:|---:|---|
| electricity bill | 1 of 14 | 0 of 14 | -1.15% | power given |
| electricity bought | 4 of 14 | 0 of 14 | -1.98% | power given |
| carbon | 1 of 14 | 0 of 14 | -0.86% | power given |
| daily peak draw | 4 of 14 | 0 of 14 | -2.42% | power given |
| highest peak | 2 of 14 | 0 of 14 | -0.51% | power given |
| ramping (swings hour to hour) | 4 of 14 | 0 of 14 | -2.25% | power given |
| daily load unevenness | 4 of 14 | 0 of 14 | -0.88% | power given |
| monthly load unevenness | 4 of 14 | 0 of 14 | -0.43% | power given |
| distance from zero net energy | 1 of 14 | 3 of 14 | -0.02% | power given |
| energy not served | 0 of 11 | 0 of 11 | +0.00% | LOSS |
| time uncomfortable | 0 of 13 | 0 of 13 | +0.00% | LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
