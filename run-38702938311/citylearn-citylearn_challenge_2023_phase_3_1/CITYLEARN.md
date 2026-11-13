# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

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

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.26% |
| electricity bought | 1 of 1 | 0 of 1 | -0.10% |
| carbon | 1 of 1 | 0 of 1 | -0.13% |
| daily peak draw | 1 of 1 | 0 of 1 | -2.20% |
| highest peak | 0 of 1 | 1 of 1 | +2.53% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +4.51% |
| daily load unevenness | 1 of 1 | 0 of 1 | -3.96% |
| monthly load unevenness | 1 of 1 | 0 of 1 | -1.18% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.02% |
| energy not served | 0 of 1 | 1 of 1 | +1.97% |
| time uncomfortable | 0 of 1 | 1 of 1 | +0.02% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
