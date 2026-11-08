# Omni-Compass on top of CityLearn's own controller

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.2.0 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.0875 an hour, reading the coming hour from the same hour of the past 7 days, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, read by the one key: a fall is a GAIN; a rise in energy not served or time uncomfortable is a LOSS, a rise in any other score (a resource spent or held) is power given. Evidence class: an independent recognized simulator (not our model).

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

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts where it fell | Districts where it rose | Mean change | A rise reads |
|---|---:|---:|---:|---|
| electricity bill | 1 of 1 | 0 of 1 | -16.09% | power given |
| electricity bought | 1 of 1 | 0 of 1 | -13.58% | power given |
| carbon | 1 of 1 | 0 of 1 | -12.07% | power given |
| daily peak draw | 1 of 1 | 0 of 1 | -16.92% | power given |
| highest peak | 1 of 1 | 0 of 1 | -2.73% | power given |
| ramping (swings hour to hour) | 1 of 1 | 0 of 1 | -9.41% | power given |
| daily load unevenness | 1 of 1 | 0 of 1 | -6.02% | power given |
| monthly load unevenness | 1 of 1 | 0 of 1 | -1.59% | power given |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.96% | power given |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
