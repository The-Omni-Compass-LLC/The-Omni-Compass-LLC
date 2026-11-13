# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1257 | 2.1326 | +0.32% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2118 | 2.2078 | -0.18% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2146 | 2.2109 | -0.17% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.3937 | -1.30% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | better: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9456 | 0.9986 | +5.60% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6831 | 0.6718 | -1.67% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2484 | 2.2468 | -0.07% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0075 | +6.25% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9877 | +0.15% | WORSE: more time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.32% |
| electricity bought | 1 of 1 | 0 of 1 | -0.18% |
| carbon | 1 of 1 | 0 of 1 | -0.17% |
| daily peak draw | 1 of 1 | 0 of 1 | -1.30% |
| highest peak | 1 of 1 | 0 of 1 | -3.49% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +5.60% |
| daily load unevenness | 1 of 1 | 0 of 1 | -1.67% |
| monthly load unevenness | 1 of 1 | 0 of 1 | -1.88% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.07% |
| energy not served | 0 of 1 | 1 of 1 | +6.25% |
| time uncomfortable | 0 of 1 | 1 of 1 | +0.15% |
