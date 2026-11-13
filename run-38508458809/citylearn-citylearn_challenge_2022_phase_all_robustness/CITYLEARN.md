# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

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

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 1 of 1 | 0 of 1 | -8.61% |
| electricity bought | 1 of 1 | 0 of 1 | -14.66% |
| carbon | 1 of 1 | 0 of 1 | -11.89% |
| daily peak draw | 1 of 1 | 0 of 1 | -13.95% |
| highest peak | 1 of 1 | 0 of 1 | -2.73% |
| ramping (swings hour to hour) | 1 of 1 | 0 of 1 | -7.18% |
| daily load unevenness | 1 of 1 | 0 of 1 | -2.90% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +0.11% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -6.10% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
