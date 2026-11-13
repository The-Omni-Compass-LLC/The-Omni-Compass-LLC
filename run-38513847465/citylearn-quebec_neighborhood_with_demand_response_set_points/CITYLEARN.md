# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

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

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% |
| electricity bought | 0 of 1 | 0 of 1 | +0.00% |
| carbon | 0 of 1 | 0 of 1 | +0.00% |
| daily peak draw | 0 of 1 | 0 of 1 | +0.00% |
| highest peak | 0 of 1 | 0 of 1 | +0.00% |
| ramping (swings hour to hour) | 0 of 1 | 0 of 1 | +0.00% |
| daily load unevenness | 0 of 1 | 0 of 1 | +0.00% |
| monthly load unevenness | 0 of 1 | 0 of 1 | +0.00% |
| distance from zero net energy | 0 of 1 | 0 of 1 | +0.00% |
| time uncomfortable | 0 of 1 | 1 of 1 | +0.26% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
