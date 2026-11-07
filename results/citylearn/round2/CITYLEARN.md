# Omni-Compass on top of CityLearn's own controller

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, the aim is lower for every row. Evidence class: an independent recognized simulator (not our model).

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

## citylearn_three_phase_dynamic_assets_only_demo: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_dynamic_topology_demo: not run to the end

- native: ValueError: topology_mode='dynamic' requires interface='entity'.
- omni: ValueError: topology_mode='dynamic' requires interface='entity'.

## citylearn_three_phase_electrical_service_demo: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

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
| electricity bill | 1 of 4 | 0 of 4 | -2.15% |
| electricity bought | 4 of 4 | 0 of 4 | -6.42% |
| carbon | 1 of 4 | 0 of 4 | -2.97% |
| daily peak draw | 4 of 4 | 0 of 4 | -5.07% |
| highest peak | 2 of 4 | 0 of 4 | -1.45% |
| ramping (swings hour to hour) | 4 of 4 | 0 of 4 | -3.82% |
| daily load unevenness | 4 of 4 | 0 of 4 | -1.33% |
| monthly load unevenness | 3 of 4 | 1 of 4 | -0.39% |
| distance from zero net energy | 4 of 4 | 0 of 4 | -1.78% |
| energy not served | 0 of 3 | 0 of 3 | +0.00% |
| time uncomfortable | 0 of 3 | 0 of 3 | +0.00% |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
