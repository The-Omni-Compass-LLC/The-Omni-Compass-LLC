# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1119 | 2.1159 | +0.19% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1877 | 2.1856 | -0.10% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1918 | 2.1891 | -0.12% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5068 | -2.18% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9763 | 1.0241 | +4.89% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6467 | 0.6199 | -4.14% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7316 | 0.7278 | -0.53% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2432 | 2.2440 | +0.04% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0136 | +4.14% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9884 | +0.09% | WORSE: more time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.19% |
| electricity bought | 1 of 1 | 0 of 1 | -0.10% |
| carbon | 1 of 1 | 0 of 1 | -0.12% |
| daily peak draw | 1 of 1 | 0 of 1 | -2.18% |
| highest peak | 0 of 1 | 1 of 1 | +2.53% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +4.89% |
| daily load unevenness | 1 of 1 | 0 of 1 | -4.14% |
| monthly load unevenness | 1 of 1 | 0 of 1 | -0.53% |
| distance from zero net energy | 0 of 1 | 1 of 1 | +0.04% |
| energy not served | 0 of 1 | 1 of 1 | +4.14% |
| time uncomfortable | 0 of 1 | 1 of 1 | +0.09% |
