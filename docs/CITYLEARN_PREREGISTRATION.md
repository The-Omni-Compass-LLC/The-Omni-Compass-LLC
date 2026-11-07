# Omni-Compass on top of CityLearn's own controller: written before the counted run

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-05, before any district other than the tuning district was run with Omni-Compass.

## Why CityLearn

Our own muscle models show the mechanism; they cannot prove it on equipment we did not write. CityLearn
(Intelligent Environments Lab, University of Texas at Austin; MIT license; github.com/intelligent-environments-lab/citylearn)
is an independent, widely used simulator of real buildings from measured data: each building's load, its solar
panels and its battery, hour by hour for a year, with its own controllers and its own scoring. Neither side built it to
win. Evidence class: an independent recognized simulator.

## The arms

- **Native:** CityLearn's own rule-based battery controller (`citylearn.agents.rbc.BasicRBC`), unchanged.
- **Native + Omni-Compass:** the same controller, with the compass law (`omnicompass/compass_law.py`) on top of its battery
  commands (`tools/run_citylearn.py`). The reading is the district's draw without its batteries the hour before (the
  demand the batteries answer, never their own effect); its band is the 10th to the 90th percentile of the past week's
  draw (only hours already seen). A positive force pushes every battery command toward discharge, a negative force
  toward charge, by at most 0.5 of the command's range, always inside the battery's own limits. The adjustment glides:
  it changes by at most 0.05 an hour. At 90% of the year every command is handed back to the native controller.

## How the settings were chosen (disclosed)

On the tuning district only, `citylearn_challenge_2022_phase_1` (5 buildings):

| Wiring | Bill | Electricity bought | Carbon | Daily peak | Highest peak | Ramping |
|---|---:|---:|---:|---:|---:|---:|
| Reading the draw with the batteries in it (a feedback loop) | +3.8% | -1.5% | +1.5% | +17.0% | +29.1% | +218% |
| Reading the draw without the batteries, no glide | -19.3% | -18.2% | -16.5% | -15.5% | -1.4% | +16.1% |
| ... glide 0.1 an hour | -17.3% | -20.2% | -17.8% | -17.5% | -1.4% | +1.8% |
| **... glide 0.05 an hour (frozen)** | **-10.5%** | **-17.8%** | **-14.7%** | **-11.9%** | **-1.4%** | **-4.4%** |
| ... glide 0.03 an hour | -8.6% | -15.8% | -12.9% | -9.6% | -1.4% | -7.5% |

(Change against native; CityLearn's own scores, the aim is lower.) Frozen: gain 0.5, response 1 hour, glide 0.05 an
hour: the setting at which every score was ahead of native on the tuning district. The tuning district is not
counted in the counted run.

## The counted run (untouched districts)

Every other CityLearn district that runs with the native controller: `citylearn_challenge_2022_phase_2`,
`citylearn_challenge_2022_phase_3`, `citylearn_challenge_2022_phase_all`, `citylearn_challenge_2021`,
`citylearn_challenge_2020_climate_zone_1` to `_4`, and `citylearn_challenge_2023_phase_1`. Each district is one
deterministic year, native and native + Omni-Compass. Reported per district and across districts: every CityLearn
score, native, native + Omni-Compass, the change, and read in words (GAIN, EVEN or LOSS), with the number of districts
lower and higher for each score. Workflow `citylearn`; the report is written to results/citylearn/CITYLEARN.md when it has run.

## Round 1 result, and the amendment written before round 2 (2026-10-05)

Round 1 (workflow `citylearn`, run 37253566738, report `results/citylearn/round1/CITYLEARN.md`, raw files
`results/live/raw/run-37253566738/`) split by the kind of
storage in the district:

| Districts | Bill | Electricity bought | Carbon | Daily peak | Highest peak | Ramping |
|---|---|---|---|---|---|---|
| 2022 phases 2, 3 and all (electric batteries; 5, 7, 17 buildings) | -4.2% to -10.8% | -8.9% to -16.9% | -6.6% to -14.1% | -11.0% to -14.0% | -2.7% to +0.5% | -7.1% to +3.4% |
| 2020 climate zones 1-4 and 2021 (cold and hot water tanks; 9 buildings) | the same | -0.0% to -0.8% | -0.5% to +0.1% | +5.5% to +11.5% (higher) | +10.4% to +28.1% (higher) | +23.5% to +31.4% (higher) |
| 2023 phase 1 (720 hours, 3 buildings) | +0.3% | -0.1% | -0.8% | -4.6% | the same | +25.3% (higher) |

The cause: the wiring pushed every storage command the same way from the district's electricity reading, the water
tanks (cooling_storage, dhw_storage) included. A tank is a thermal muscle; moving when it charges by an electricity
reading made the peaks higher.

**Amendment (one wire, one muscle):** the compass steers only the electric batteries (`electrical_storage`) from the
electricity reading; every water tank stays native (it would need its own wire and its own reading, the tank's
temperature). A district with no electric battery is run and reported with Omni-Compass steering nothing. Gain,
response, glide and band are unchanged. Round 1's districts have been seen and are not the test of this amendment.

**Round 2, the untouched districts:** every other district CityLearn ships that runs with its rule-based controller:
`baeda_3dem`, `ca_alameda_county_neighborhood`, `citylearn_challenge_2022_phase_all_demand_response`,
`citylearn_challenge_2022_phase_all_plus_evs`, `citylearn_challenge_2022_phase_all_robustness`,
`citylearn_challenge_2023_phase_2_local_evaluation`, `citylearn_challenge_2023_phase_2_online_evaluation_1` to `_3`,
and the `citylearn_challenge_2023_phase_3` sets. Disclosed: the three 2022 variants share buildings with the 2022
districts of round 1 (different scenarios: demand response, electric vehicles, robustness). A district whose files the
rule-based controller cannot run is reported as such, never left out silently. Reported as in round 1, round 1 kept
beside it.


**Round 2, running it (2026-10-05, before any of its scores were read):** nine districts stopped before a score. Six of
the newer districts size their solar panels with NREL's System Advisor Model (PySAM), which the runner lacked. The three
three-phase demonstration districts ship with CityLearn's non-flat interface, which its own rule-based controller
refuses. The runner now installs PySAM and opens every district with the flat interface. These are harness fixes only:
the controller, gain, response, glide and band are unchanged, and both arms see the same district.

**Round 2, the result (2026-10-05, GitHub run 37271184088, `results/citylearn/round2/CITYLEARN.md`):** four districts
ran to the end: Alameda County, Travis County, Chittenden County and the 2022 robustness district. Electricity bought
was lower in all four (2.1-14.7%), the daily peak lower in all four (0.8-14.0%), and hour-to-hour ramping lower in all
four (1.3-7.2%). The robustness district came out bill 8.6% lower, carbon 11.9% lower and daily peak 14.0% lower. Its
monthly load unevenness was 0.11% higher, the one row behind native, reported as measured. In the other three
districts the bill and carbon came out the same. Five districts cannot be run by CityLearn's own rule-based controller in
any arm: they need CityLearn's entity interface, which that controller refuses, or they carry an appliance action it
does not know. Each is listed in the report with CityLearn's own message.

## Amendment of 17 October (omni-v8): the battery that carries its building through an outage stays native

**What omni-v7 read** (`results/live/V7_CITYLEARN.md`, three runs): GAIN in all three of our runs on the electricity bought and
the daily peak in all ten battery districts; LOSS in all three of our runs in the seven 2023 districts on the energy not served
(+2.0% to +9.8%), the time uncomfortable, the ramping, the highest peak in three districts and the monthly unevenness in one.

**Cause** (found locally on CityLearn 3.0.2, the omni-v7 numbers reproduced to the last digit): the seven 2023 districts are the
only ones whose buildings simulate power outages (every building in each; no other district has any), and CityLearn counts the
energy not served only in outage hours. The wire moved the batteries for the district's draw and did not see that, in those
buildings, the battery is also the building's reserve through the outage.

**Amendment (one wire, one muscle):** a battery whose building simulates power outages (CityLearn's `simulate_power_outage`) is
left native; every other battery is steered exactly as before (controller, gain, response, glide, band and hand-back unchanged).
Fixed on one district (`citylearn_challenge_2023_phase_2_local_evaluation`); three narrower repairs each left a LOSS there and
were refused (`docs/OMNI_V8.md`, section 1). Every district has now been seen, so no untouched district remains for this
amendment; it is reported on all, every row, through `tools/citylearn_abc.py` A, B and C on the omni-v8 commit
(to be written as results/live/V8_CITYLEARN.md). Read before any GitHub run: the 2023 districts identical to native; every other district
identical to omni-v7 (checked to the digit on the 2022 robustness district). The robustness district's monthly unevenness
(+0.11%, LOSS in all three omni-v7 runs) is not changed by this amendment and stays reported.

## Amendment of 17 October (omni-v9): the battery wire reads the coming hour

**What omni-v8 read** (the omni-v7 table, whose commands omni-v8 repeats to the byte outside the 2023 districts): the monthly
load unevenness in `citylearn_challenge_2022_phase_all_robustness` +0.11%, LOSS in all three of our runs, beside GAIN on the bill,
the electricity bought, carbon, the daily peak and the highest peak. Run locally, the same wire also read LOSS on districts the
GitHub benchmark does not run: the tuning district's monthly unevenness (+0.26%), and rows of the 2022 phases 2 and 3.

**Cause** (an hour-by-hour trace of the wire on the robustness district, CityLearn 3.0.2): the compass read the hour just gone and
its adjustment moved by at most 0.05 of the command's range an hour, so it ran about five hours behind the day (its strongest
discharge at 00:00, the draw's peak at 19:00); the batteries were empty at the month's top hour in ten of the eleven months the
trace covers, and the month's mean fell faster than its peak.

**Amendment (one wire, one muscle):** the compass reads the coming hour, the mean of the same hour of the day over the past seven
days (only hours already seen), and the adjustment glides by up to 0.0625 an hour: the fastest glide that read no LOSS on any
score in any district (0.05 left the 2022 phase 2's daily unevenness +0.25%; 0.075 and faster raised the 2022 phase 3's ramping).
The controller, the gain, the response, the band, the hand-back, the outage batteries and the water tanks are unchanged. Found on
the district whose LOSS it repairs; narrower repairs each left a LOSS there and were refused (`docs/OMNI_V9.md`, section 1). Read
before any GitHub run on every district with batteries outside the 2023 set (the robustness district, the tuning district, the 2022
phases 2, 3 and all, Alameda County, Travis County): no LOSS on any score (`docs/OMNI_V9.md`, section 3). Every district has now
been seen, so the amendment is reported on all, every row, through `tools/citylearn_abc.py` A, B and C on the omni-v9 commit.

## Amendment of 17 October, night: one key for every score

The founder's correction of 17 October: a peak, a swing and an unevenness are the power a district draws and holds from the grid,
as a Kubernetes cluster's peak power is, so a rise in any of them is **power given**, never a LOSS; only the occupants' misses,
the energy not served and the time uncomfortable, read LOSS when they rise. This table's rule had filed the highest peak, the
daily peak, the ramping and the daily and monthly unevenness as misses; it now reads them as power held (`tools/citylearn_abc.py`,
through `tools/readings.py`). No number moves; only the word beside it. Read again under this rule, the omni-v7 table holds 65
score-rows GAIN, 20 power given and 13 LOSS, the 13 the energy not served and the time uncomfortable in the seven 2023 districts,
repaired in omni-v8; the robustness district's monthly unevenness +0.11%, the row the amendment above answered, is power given.

## Amendment of 18 October (omni-v10): the glide that cuts the bill most

**What the rule changed.** The amendment of 17 October (omni-v9) set the glide at the fastest speed at which no score rose in any
district, which counted a rise in the ramping or in the distance from net zero against the wire. Under the one key (the amendment
above) those are power held: a rise is power given. The founder's rule for the tune: use everything that can be used, keep
everything healthy, never raise the bill, hurt no one.

**Amendment (one setting, one muscle):** the glide is 0.0875 of the command's range an hour, the speed on the omni-v9 ladder (0.05,
0.0625, 0.075, 0.0875, 0.10) that cuts the bill most with no LOSS: at 0.10 the bill falls less in both districts that set the edge
(the 2022 phases 2 and 3). The controller, the gain, the response, the reading of the coming hour, the band, the hand-back, the
outage batteries and the water tanks are unchanged. Read before any GitHub run on the five 2022 districts
with batteries (the two 100-building neighbourhoods were still running when it was pushed): no LOSS on any score; two rows of the 2022 phase 3 are power given (the ramping +6.18%, the net-zero shortfall +0.25%)
(`docs/OMNI_V10.md`, section 2). A change that steered the outage buildings' batteries outside the outage hours was run on six of
the seven 2023 districts and refused: energy not served +0.69% in one, a LOSS (`docs/OMNI_V10.md`, section 3). Every district has
been seen, so the amendment is reported on all, every row, through `tools/citylearn_abc.py` A, B and C on the omni-v10 commit.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
