# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

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

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.35% |
| electricity bought | 1 of 1 | 0 of 1 | -0.27% |
| carbon | 1 of 1 | 0 of 1 | -0.17% |
| daily peak draw | 1 of 1 | 0 of 1 | -1.61% |
| highest peak | 0 of 1 | 0 of 1 | +0.00% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +6.24% |
| daily load unevenness | 1 of 1 | 0 of 1 | -2.86% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +0.07% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.06% |
| energy not served | 0 of 1 | 1 of 1 | +5.96% |
| time uncomfortable | 0 of 1 | 1 of 1 | +0.12% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
