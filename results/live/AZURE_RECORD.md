# Azure: every run that handed in a receipt, each under its own engine

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written by `tools/azure_record.py` from each run's own receipt on the branch `raw` (`run-<id>/live-reps-aks/LIVE_REPS.json`, written by `tools/live_reps.py` in the run's own aggregate job); `results/live/AZURE_RECORD.json` is the same in a form a page reads. The runs' own records (title, commit, start, end, conclusion) are GitHub's, read 2026-11-08T08:20:00Z; each run's engine is the one its commit stands on (`tools/omni_version.py --commit`). Evidence class **L** (live software on Azure Kubernetes Service, the bill metered: Azure's own count of the machines it billed every 15 s, priced at list).

**26 Azure runs handed in a receipt**: 22 counted sets and 4 tuning cases, on 11 engines (no declared engine, omni-v1, omni-v5, omni-v7, omni-v9, omni-v10, omni-v11, omni-v18, omni-v21, omni-v25, omni-v26). Each run's word stands by itself, on its own number, by the one key; no two runs are pooled and no run is read across engines. A set of five repetitions has wide intervals: its words say what it measured, and how many of them stand beyond the noise. The sets before 31 October ran at the tune-down on the machines alone (the founder's order of 14 October, struck on 31 October): there Omni-Compass only parked a machine the cloud already made, so the work could not grow and the service rows read the noise of the same pods. The sets at the max on the work meter start after their tuning cases.

How to read a cell: the word first (GAIN, STEADY, LOSS, power given), then the direction and size of the change against native in words, then whether the run's paired 95% interval stands clear of zero. Why a word reads so: work done: more work is more output from the same organism; work bought with each dollar of the bill: more is more work for the bill; a resource the bill pays for: a fall is a cut, a rise is power given beside what it bought, never a loss; time waited, missed or failed: less helps the system, more hurts it; a count that must never rise: any rise hurts the system and reads LOSS, with no floor.

## Every run, newest first

| Run | Engine | Set | Counts | Paired repetitions | Work inside the line | The bill | 95th percentile | 99th percentile | Failed requests | Time over the line |
|---|---|---|---|---:|---|---|---|---|---|---|
| [42408759289](#run-42408759289) | omni-v26 | the work meter at rates 2 4 6 8 10 12 16 20 a second | tuning case: sets the counted rates, never counted | 1 | GAIN, up 52.5%<br>(one repetition, no interval) | GAIN, down 1.5%<br>(one repetition, no interval) | GAIN, down 0.9%<br>(one repetition, no interval) | GAIN, down 53.0%<br>(one repetition, no interval) | GAIN or STEADY, down 100.0%<br>(one repetition, no interval) | GAIN, down 6.3%<br>(one repetition, no interval) |
| [42400923213](#run-42400923213) | omni-v26 | the work meter at rates 10 20 40 60 80 100 120 140 a second | tuning case: sets the counted rates, never counted | 1 | LOSS, down 14.4%<br>(one repetition, no interval) | power given, up 42.7%<br>(one repetition, no interval) | LOSS, up 224.1%<br>(one repetition, no interval) | LOSS, up 16.6%<br>(one repetition, no interval) | LOSS, up 19.7%<br>(one repetition, no interval) | LOSS, up 29.8%<br>(one repetition, no interval) |
| [41914478995](#run-41914478995) | omni-v25 | the work meter at rates 2 4 6 8 10 12 16 20 a second | tuning case: sets the counted rates, never counted | 1 | GAIN, up 69.3%<br>(one repetition, no interval) | power given, up 30.2%<br>(one repetition, no interval) | GAIN, down 28.1%<br>(one repetition, no interval) | GAIN, down 57.1%<br>(one repetition, no interval) | GAIN or STEADY, down 100.0%<br>(one repetition, no interval) | GAIN, down 52.2%<br>(one repetition, no interval) |
| [41745105583](#run-41745105583) | omni-v25 | the work meter at rates 10 20 40 60 80 100 120 140 a second | tuning case: sets the counted rates, never counted | 1 | LOSS, down 80.9%<br>(one repetition, no interval) | power given, up 14.9%<br>(one repetition, no interval) | GAIN, down 70.4%<br>(one repetition, no interval) | GAIN, down 76.5%<br>(one repetition, no interval) | LOSS, up 49.3%<br>(one repetition, no interval) | LOSS, up 7.9%<br>(one repetition, no interval) |
| [40940616527](#run-40940616527) | omni-v21 | the steady set under the stopping rule | counted set | 73 | — | STEADY<br>(inside the noise) | GAIN, down 1.9%<br>(inside the noise) | GAIN, down 7.0%<br>(inside the noise) | LOSS, up 9.9%<br>(inside the noise) | LOSS, up 1.3%<br>(inside the noise) |
| [40126991719](#run-40126991719) | omni-v18 | the steady set | counted set | 5 | — | power given, up 1.4%<br>(inside the noise) | GAIN, down 11.7%<br>(inside the noise) | GAIN, down 14.2%<br>(inside the noise) | GAIN or STEADY, down 0.2%<br>(inside the noise) | GAIN, down 10.6%<br>(beyond the noise) |
| [40069633316](#run-40069633316) | omni-v18 | the steady set under the stopping rule | counted set | 97 | — | power given, up 1.2%<br>(inside the noise) | GAIN, down 4.0%<br>(inside the noise) | GAIN, down 11.0%<br>(beyond the noise) | LOSS, up 3.9%<br>(inside the noise) | GAIN, down 0.9%<br>(inside the noise) |
| [39236324280](#run-39236324280) | omni-v11 | the steady set under the stopping rule | counted set | 100 | — | GAIN, down 1.3%<br>(inside the noise) | LOSS, up 1.7%<br>(inside the noise) | GAIN, down 11.5%<br>(inside the noise) | GAIN or STEADY, down 8.2%<br>(inside the noise) | STEADY<br>(inside the noise) |
| [39187809233](#run-39187809233) | omni-v11 | the burst 1 4 1 6 1 9 | counted set | 5 | — | GAIN, down 0.6%<br>(inside the noise) | LOSS, up 3.7%<br>(inside the noise) | GAIN, down 25.7%<br>(inside the noise) | LOSS, up 10.9%<br>(inside the noise) | LOSS, up 10.3%<br>(inside the noise) |
| [39162654399](#run-39162654399) | omni-v11 | the steady set | counted set | 5 | — | GAIN, down 1.3%<br>(inside the noise) | GAIN, down 17.6%<br>(inside the noise) | GAIN, down 19.0%<br>(inside the noise) | GAIN or STEADY, down 24.2%<br>(inside the noise) | GAIN, down 6.7%<br>(inside the noise) |
| [39119345316](#run-39119345316) | omni-v10 | the burst 1 4 1 6 1 9 | counted set | 5 | — | power given, up 4.9%<br>(inside the noise) | LOSS, up 21.0%<br>(inside the noise) | LOSS, up 124.6%<br>(inside the noise) | GAIN or STEADY, down 13.7%<br>(inside the noise) | GAIN, down 13.2%<br>(inside the noise) |
| [39100680671](#run-39100680671) | omni-v10 | the steady set | counted set | 5 | — | GAIN, down 4.9%<br>(inside the noise) | GAIN, down 5.3%<br>(inside the noise) | GAIN, down 11.3%<br>(inside the noise) | LOSS, up 2.9%<br>(inside the noise) | GAIN, down 2.0%<br>(inside the noise) |
| [39080133432](#run-39080133432) | omni-v9 | the steady set | counted set | 5 | — | GAIN, down 3.6%<br>(inside the noise) | LOSS, up 25.2%<br>(inside the noise) | GAIN, down 12.7%<br>(inside the noise) | GAIN or STEADY, down 22.2%<br>(inside the noise) | LOSS, up 0.6%<br>(inside the noise) |
| [39014972717](#run-39014972717) | omni-v7 | the burst 1 6 1 8 1 6 | counted set | 5 | — | GAIN, down 5.8%<br>(inside the noise) | LOSS, up 7.7%<br>(inside the noise) | GAIN, down 1.8%<br>(inside the noise) | LOSS, up 1.4%<br>(inside the noise) | STEADY<br>(inside the noise) |
| [38981149348](#run-38981149348) | omni-v7 | the steady set | counted set | 5 | — | power given, up 2.5%<br>(inside the noise) | LOSS, up 4.3%<br>(inside the noise) | LOSS, up 27.3%<br>(inside the noise) | LOSS, up 22.4%<br>(inside the noise) | GAIN, down 4.6%<br>(inside the noise) |
| [38979690890](#run-38979690890) | omni-v7 | the burst 1 4 1 6 1 9 | counted set | 5 | — | power given, up 7.6%<br>(inside the noise) | LOSS, up 28.3%<br>(inside the noise) | LOSS, up 23.3%<br>(inside the noise) | GAIN or STEADY, down 22.7%<br>(inside the noise) | GAIN, down 12.1%<br>(inside the noise) |
| [38652001497](#run-38652001497) | omni-v5 | the burst 1 4 1 6 1 9 | counted set | 5 | — | GAIN, down 1.6%<br>(inside the noise) | LOSS, up 5.2%<br>(inside the noise) | LOSS, up 11.3%<br>(inside the noise) | GAIN or STEADY, down 10.4%<br>(inside the noise) | GAIN, down 9.4%<br>(inside the noise) |
| [38648741673](#run-38648741673) | omni-v5 | the steady set | counted set | 5 | — | GAIN, down 6.5%<br>(inside the noise) | LOSS, up 16.2%<br>(inside the noise) | LOSS, up 28.9%<br>(inside the noise) | LOSS, up 18.6%<br>(inside the noise) | LOSS, up 5.5%<br>(inside the noise) |
| [38582893457](#run-38582893457) | omni-v5 | the burst 1 6 1 8 1 6 | counted set | 5 | — | power given, up 1.0%<br>(inside the noise) | LOSS, up 5.0%<br>(inside the noise) | GAIN, down 13.4%<br>(inside the noise) | GAIN or STEADY, down 8.7%<br>(beyond the noise) | GAIN, down 3.5%<br>(inside the noise) |
| [38561768164](#run-38561768164) | omni-v5 | the real day on 1 to 9 (Google 2011) | counted set | 5 | — | GAIN, down 1.4%<br>(inside the noise) | LOSS, up 22.2%<br>(inside the noise) | LOSS, up 5.0%<br>(inside the noise) | LOSS, up 2.5%<br>(inside the noise) | LOSS, up 2.4%<br>(inside the noise) |
| [38516042470](#run-38516042470) | omni-v5 | the burst 1 4 1 6 1 9 | counted set | 5 | — | power given, up 4.0%<br>(inside the noise) | LOSS, up 1.4%<br>(inside the noise) | GAIN, down 41.5%<br>(inside the noise) | GAIN or STEADY, down 16.4%<br>(inside the noise) | GAIN, down 11.6%<br>(inside the noise) |
| [38516035978](#run-38516035978) | omni-v5 | the steady set | counted set | 5 | — | GAIN, down 1.8%<br>(beyond the noise) | LOSS, up 10.5%<br>(inside the noise) | LOSS, up 3.1%<br>(inside the noise) | GAIN or STEADY, down 17.7%<br>(inside the noise) | GAIN, down 3.0%<br>(inside the noise) |
| [38455383137](#run-38455383137) | omni-v5 | the steady set | counted set | 4 | — | power given, up 51.2%<br>(beyond the noise) | GAIN, down 34.0%<br>(beyond the noise) | GAIN, down 71.7%<br>(beyond the noise) | GAIN or STEADY, down 83.4%<br>(beyond the noise) | GAIN, down 52.6%<br>(beyond the noise) |
| [38339858727](#run-38339858727) | no declared engine | the steady set | counted set | 5 | — | power given, up 9.1%<br>(inside the noise) | GAIN, down 11.8%<br>(inside the noise) | LOSS, up 7.2%<br>(inside the noise) | LOSS, up 10.1%<br>(inside the noise) | LOSS, up 2.5%<br>(inside the noise) |
| [37534538088](#run-37534538088) | omni-v1 | the steady set | counted set | 5 | — | power given, up 5.0%<br>(inside the noise) | LOSS, up 15.0%<br>(inside the noise) | GAIN, down 33.6%<br>(beyond the noise) | GAIN or STEADY, down 30.0%<br>(inside the noise) | STEADY<br>(inside the noise) |
| [37385657374](#run-37385657374) | omni-v1 | the steady set | counted set | 5 | — | GAIN, down 4.7%<br>(inside the noise) | GAIN, down 2.1%<br>(inside the noise) | GAIN, down 5.8%<br>(inside the noise) | GAIN or STEADY, down 32.3%<br>(inside the noise) | LOSS, up 3.3%<br>(inside the noise) |

## Each run, every gauge of its receipt

### Run 42408759289

<a id="run-42408759289"></a>

`aks-metered`, work meter 2 4 6 8 10 12 16 20 dial max eastus Standard_D2s_v4; engine **omni-v26** (commit `e81cb06c22`, branch `main`); started 2026-11-07 19:58 UTC, ended 2026-11-07 21:28 UTC; GitHub's conclusion **success**; 1 paired repetition; the dial max; tuning case: sets the counted rates, never counted. Receipt `raw:run-42408759289/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.532 | 2.769 | up 9.4% | — to — | power given, up 9.4% (one repetition, no interval) |
| node-hours | 0.8525 | 0.9322 | up 9.4% | — to — | power given, up 9.4% (one repetition, no interval) |
| energy, parked workers still on at idle power (Wh) | 107.4 | 158 | up 47.1% | — to — | power given, up 47.1% (one repetition, no interval) |
| energy (Wh) | 95.58 | 101.7 | up 6.4% | — to — | power given, up 6.4% (one repetition, no interval) |
| response time (ms), mean | 374.5 | 347.4 | down 7.2% | — to — | GAIN, down 7.2% (one repetition, no interval) |
| response time (ms), 95th percentile | 827.8 | 820.4 | down 0.9% | — to — | GAIN, down 0.9% (one repetition, no interval) |
| response time (ms), 99th percentile | 2863 | 1344 | down 53.0% | — to — | GAIN, down 53.0% (one repetition, no interval) |
| time over the response line (% of samples) | 22.05 | 20.67 | down 6.3% | — to — | GAIN, down 6.3% (one repetition, no interval) |
| failed requests (%) | 3.288 | 0 | down 100.0% | — to — | GAIN or STEADY, down 100.0% (one repetition, no interval) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19 | 20 | up 5.3% | — to — | LOSS, up 5.3% (one repetition, no interval) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34 | — | — to — | shown, not judged |
| pods with no machine to take them (unschedulable) | 1 | 5 | up 400.0% | — to — | LOSS, up 400.0% (one repetition, no interval) |
| time pods had no machine to take them, pod-minutes | 1.217 | 7.9 | up 549.3% | — to — | LOSS, up 549.3% (one repetition, no interval) |
| pending pods, pod-minutes | 3.733 | 16.1 | up 331.2% | — to — | shown, not judged |
| utilisation (used / allocatable) | 0.3174 | 0.2967 | down 6.5% | — to — | shown, not judged |
| CPU used (cores), mean | 1.527 | 1.561 | up 2.2% | — to — | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0152 | — | — to — | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.527 | 1.576 | up 3.2% | — to — | shown, not judged |
| energy per core-hour (Wh) | 185.9 | 193.4 | up 4.0% | — to — | shown, not judged |
| HPA replicas, mean | 7.35 | 10.18 | up 38.6% | — to — | shown, not judged |
| pods started | 8 | 20 | up 150.0% | — to — | shown, not judged |
| pod start wait, total (s) | 115 | 568 | up 393.9% | — to — | LOSS, up 393.9% (one repetition, no interval) |
| pod start wait, mean (s) | 14.38 | 28.4 | up 97.6% | — to — | LOSS, up 97.6% (one repetition, no interval) |
| machines billed, machine-hours | 0.8606 | 0.8472 | down 1.5% | — to — | GAIN, down 1.5% (one repetition, no interval) |
| compute bill at list price ($) | 0.08261 | 0.08133 | down 1.5% | — to — | GAIN, down 1.5% (one repetition, no interval) |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.476 | 8.35 | up 52.5% | — to — | GAIN, up 52.5% (one repetition, no interval) |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8.18e+04 | 1.244e+05 | up 52.1% | — to — | GAIN, up 52.1% (one repetition, no interval) |

### Run 42400923213

<a id="run-42400923213"></a>

`aks-metered`, work meter 10 20 40 60 80 100 120 140 dial max eastus Standard_D2s_v4; engine **omni-v26** (commit `5d13597b94`, branch `main`); started 2026-11-07 18:21 UTC, ended 2026-11-07 19:44 UTC; GitHub's conclusion **success**; 1 paired repetition; the dial max; tuning case: sets the counted rates, never counted. Receipt `raw:run-42400923213/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 3 | 4.439 | up 48.0% | — to — | power given, up 48.0% (one repetition, no interval) |
| node-hours | 1.003 | 1.496 | up 49.1% | — to — | power given, up 49.1% (one repetition, no interval) |
| energy, parked workers still on at idle power (Wh) | 158 | 291.2 | up 84.3% | — to — | power given, up 84.3% (one repetition, no interval) |
| energy (Wh) | 158 | 277.1 | up 75.3% | — to — | power given, up 75.3% (one repetition, no interval) |
| response time (ms), mean | 709.9 | 1502 | up 111.5% | — to — | LOSS, up 111.5% (one repetition, no interval) |
| response time (ms), 95th percentile | 2673 | 8661 | up 224.1% | — to — | LOSS, up 224.1% (one repetition, no interval) |
| response time (ms), 99th percentile | 8142 | 9496 | up 16.6% | — to — | LOSS, up 16.6% (one repetition, no interval) |
| time over the response line (% of samples) | 65.88 | 85.52 | up 29.8% | — to — | LOSS, up 29.8% (one repetition, no interval) |
| failed requests (%) | 57.06 | 68.28 | up 19.7% | — to — | LOSS, up 19.7% (one repetition, no interval) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 20 | unchanged 0.0% | — to — | STEADY (one repetition, no interval) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22 | — | — to — | shown, not judged |
| pods with no machine to take them (unschedulable) | 0 | 23 | — | — to — | shown, not judged |
| time pods had no machine to take them, pod-minutes | 0 | 106.9 | — | — to — | shown, not judged |
| pending pods, pod-minutes | 0 | 117 | — | — to — | shown, not judged |
| utilisation (used / allocatable) | 0.6519 | 0.7797 | up 19.6% | — to — | shown, not judged |
| CPU used (cores), mean | 3.716 | 6.577 | up 77.0% | — to — | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.01 | — | — to — | shown, not judged |
| CPU used with Omni's own (cores), mean | 3.716 | 6.587 | up 77.3% | — to — | shown, not judged |
| energy per core-hour (Wh) | 127.2 | 125 | down 1.7% | — to — | shown, not judged |
| HPA replicas, mean | 9.929 | 28.42 | up 186.2% | — to — | shown, not judged |
| pods started | 0 | 27 | — | — to — | shown, not judged |
| pod start wait, total (s) | 0 | 6560 | — | — to — | shown, not judged |
| pod start wait, mean (s) | 0 | 243 | — | — to — | shown, not judged |
| machines billed, machine-hours | 0.8533 | 1.218 | up 42.7% | — to — | power given, up 42.7% (one repetition, no interval) |
| compute bill at list price ($) | 0.08192 | 0.1169 | up 42.7% | — to — | power given, up 42.7% (one repetition, no interval) |
| work inside the response line (requests a second; the capacity test's own gauge) | 1.531 | 1.311 | down 14.4% | — to — | LOSS, down 14.4% (one repetition, no interval) |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 2.273e+04 | 1.362e+04 | down 40.1% | — to — | power given, down 40.1% (one repetition, no interval) |

### Run 41914478995

<a id="run-41914478995"></a>

`aks-metered`, work meter 2 4 6 8 10 12 16 20 dial max eastus Standard_D2s_v4; engine **omni-v25** (commit `8ee6cae0da`, branch `main`); started 2026-11-04 21:16 UTC, ended 2026-11-04 22:48 UTC; GitHub's conclusion **success**; 1 paired repetition; the dial max; tuning case: sets the counted rates, never counted. Receipt `raw:run-41914478995/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.532 | 3.098 | up 22.3% | — to — | power given, up 22.3% (one repetition, no interval) |
| node-hours | 0.8469 | 1.035 | up 22.2% | — to — | power given, up 22.2% (one repetition, no interval) |
| energy, parked workers still on at idle power (Wh) | 103.7 | 160.1 | up 54.4% | — to — | power given, up 54.4% (one repetition, no interval) |
| energy (Wh) | 91.99 | 112.5 | up 22.2% | — to — | power given, up 22.2% (one repetition, no interval) |
| response time (ms), mean | 396.4 | 266.2 | down 32.9% | — to — | GAIN, down 32.9% (one repetition, no interval) |
| response time (ms), 95th percentile | 856.6 | 616.3 | down 28.1% | — to — | GAIN, down 28.1% (one repetition, no interval) |
| response time (ms), 99th percentile | 1973 | 846.8 | down 57.1% | — to — | GAIN, down 57.1% (one repetition, no interval) |
| time over the response line (% of samples) | 24.9 | 11.89 | down 52.2% | — to — | GAIN, down 52.2% (one repetition, no interval) |
| failed requests (%) | 3.497 | 0 | down 100.0% | — to — | GAIN or STEADY, down 100.0% (one repetition, no interval) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 16 | down 20.0% | — to — | GAIN, down 20.0% (one repetition, no interval) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 | — | — to — | shown, not judged |
| pods with no machine to take them (unschedulable) | 3 | 18 | up 500.0% | — to — | LOSS, up 500.0% (one repetition, no interval) |
| time pods had no machine to take them, pod-minutes | 2.45 | 16.67 | up 580.3% | — to — | LOSS, up 580.3% (one repetition, no interval) |
| pending pods, pod-minutes | 6.133 | 24.57 | up 300.5% | — to — | shown, not judged |
| utilisation (used / allocatable) | 0.3175 | 0.2686 | down 15.4% | — to — | shown, not judged |
| CPU used (cores), mean | 1.528 | 1.581 | up 3.5% | — to — | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0151 | — | — to — | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.528 | 1.596 | up 4.5% | — to — | shown, not judged |
| energy per core-hour (Wh) | 180 | 212.8 | up 18.2% | — to — | shown, not judged |
| HPA replicas, mean | 7.497 | 13.46 | up 79.6% | — to — | shown, not judged |
| pods started | 8 | 33 | up 312.5% | — to — | shown, not judged |
| pod start wait, total (s) | 195 | 1186 | up 508.2% | — to — | LOSS, up 508.2% (one repetition, no interval) |
| pod start wait, mean (s) | 24.38 | 35.94 | up 47.4% | — to — | LOSS, up 47.4% (one repetition, no interval) |
| machines billed, machine-hours | 0.755 | 0.9828 | up 30.2% | — to — | power given, up 30.2% (one repetition, no interval) |
| compute bill at list price ($) | 0.07248 | 0.09435 | up 30.2% | — to — | power given, up 30.2% (one repetition, no interval) |
| work inside the response line (requests a second; the capacity test's own gauge) | 5.308 | 8.987 | up 69.3% | — to — | GAIN, up 69.3% (one repetition, no interval) |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 9.073e+04 | 1.146e+05 | up 26.3% | — to — | GAIN, up 26.3% (one repetition, no interval) |

### Run 41745105583

<a id="run-41745105583"></a>

`aks-metered`, work meter 10 20 40 60 80 100 120 140 dial max eastus Standard_D2s_v4; engine **omni-v25** (commit `21c08ab53d`, branch `main`); started 2026-11-04 00:12 UTC, ended 2026-11-04 01:32 UTC; GitHub's conclusion **success**; 1 paired repetition; the dial max; tuning case: sets the counted rates, never counted. Receipt `raw:run-41745105583/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 3.116 | 3.989 | up 28.0% | — to — | power given, up 28.0% (one repetition, no interval) |
| node-hours | 1.041 | 1.335 | up 28.3% | — to — | power given, up 28.3% (one repetition, no interval) |
| energy, parked workers still on at idle power (Wh) | 207.9 | 267.1 | up 28.5% | — to — | power given, up 28.5% (one repetition, no interval) |
| energy (Wh) | 160.7 | 241.7 | up 50.4% | — to — | power given, up 50.4% (one repetition, no interval) |
| response time (ms), mean | 1464 | 632.7 | down 56.8% | — to — | GAIN, down 56.8% (one repetition, no interval) |
| response time (ms), 95th percentile | 4412 | 1305 | down 70.4% | — to — | GAIN, down 70.4% (one repetition, no interval) |
| response time (ms), 99th percentile | 5952 | 1397 | down 76.5% | — to — | GAIN, down 76.5% (one repetition, no interval) |
| time over the response line (% of samples) | 90.97 | 98.18 | up 7.9% | — to — | LOSS, up 7.9% (one repetition, no interval) |
| failed requests (%) | 65.16 | 97.27 | up 49.3% | — to — | LOSS, up 49.3% (one repetition, no interval) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 20 | unchanged 0.0% | — to — | STEADY (one repetition, no interval) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22 | — | — to — | shown, not judged |
| pods with no machine to take them (unschedulable) | 3 | 23 | up 666.7% | — to — | LOSS, up 666.7% (one repetition, no interval) |
| time pods had no machine to take them, pod-minutes | 3.3 | 91.27 | up 2665.7% | — to — | LOSS, up 2665.7% (one repetition, no interval) |
| pending pods, pod-minutes | 11.05 | 100.5 | up 810.0% | — to — | shown, not judged |
| utilisation (used / allocatable) | 0.5749 | 0.7485 | up 30.2% | — to — | shown, not judged |
| CPU used (cores), mean | 3.404 | 5.673 | up 66.6% | — to — | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0141 | — | — to — | shown, not judged |
| CPU used with Omni's own (cores), mean | 3.404 | 5.687 | up 67.1% | — to — | shown, not judged |
| energy per core-hour (Wh) | 141.4 | 127.3 | down 10.0% | — to — | shown, not judged |
| HPA replicas, mean | 9.811 | 23.7 | up 141.6% | — to — | shown, not judged |
| pods started | 5 | 34 | up 580.0% | — to — | shown, not judged |
| pod start wait, total (s) | 250 | 5758 | up 2203.2% | — to — | LOSS, up 2203.2% (one repetition, no interval) |
| pod start wait, mean (s) | 50 | 169.4 | up 238.7% | — to — | LOSS, up 238.7% (one repetition, no interval) |
| machines billed, machine-hours | 1.062 | 1.221 | up 14.9% | — to — | power given, up 14.9% (one repetition, no interval) |
| compute bill at list price ($) | 0.102 | 0.1172 | up 14.9% | — to — | power given, up 14.9% (one repetition, no interval) |
| work inside the response line (requests a second; the capacity test's own gauge) | 0.7249 | 0.1381 | down 80.9% | — to — | LOSS, down 80.9% (one repetition, no interval) |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | 8863 | 1425 | down 83.9% | — to — | power given, down 83.9% (one repetition, no interval) |

### Run 40940616527

<a id="run-40940616527"></a>

`aks-metered`, steady replica room 0 to the cap, stopping rule dial save eastus Standard_D2s_v4; engine **omni-v21** (commit `089d4d5c70`, branch `main`); started 2026-10-29 19:29 UTC, ended 2026-11-03 23:40 UTC; GitHub's conclusion **failure**; 73 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-40940616527/live-reps-aks/LIVE_REPS.json`. The record: it ended in failure on 3 November with 27 of its 100 repetitions refused, 26 of them by one fault of the rig's evidence tool (the pod watch's expired history, native and Omni-Compass arms alike; repaired 6 November, `docs/REPAIR_20261106.md`); the refused repetitions stay refused and the set is read in no three-run table.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.797 | 2.792 | down 0.2% | -0.02935 to 0.01914 | STEADY (inside the noise) |
| node-hours | 0.7065 | 0.7048 | down 0.2% | -0.007803 to 0.004355 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 87.92 | 88.19 | up 0.3% | -0.7135 to 1.248 | STEADY (inside the noise) |
| energy (Wh) | 83.82 | 83.99 | up 0.2% | -0.4313 to 0.7779 | STEADY (inside the noise) |
| response time (ms), mean | 540.8 | 525.2 | down 2.9% | -32.55 to 1.485 | GAIN, down 2.9% (inside the noise) |
| response time (ms), 95th percentile | 1345 | 1319 | down 1.9% | -119.2 to 67.37 | GAIN, down 1.9% (inside the noise) |
| response time (ms), 99th percentile | 5373 | 4995 | down 7.0% | -864.6 to 107.4 | GAIN, down 7.0% (inside the noise) |
| time over the response line (% of samples) | 30.68 | 31.07 | up 1.3% | -0.6902 to 1.479 | LOSS, up 1.3% (inside the noise) |
| failed requests (%) | 6.018 | 6.616 | up 9.9% | -0.3399 to 1.535 | LOSS, up 9.9% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.15 | 14.27 | up 0.9% | -0.1224 to 0.369 | LOSS, up 0.9% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.3 | — | 24.44 to 26.17 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.863 | 2.849 | down 0.5% | -0.2248 to 0.1974 | STEADY (inside the noise) |
| time pods had no machine to take them, pod-minutes | 4.411 | 4.525 | up 2.6% | -0.2995 to 0.5282 | LOSS, up 2.6% (inside the noise) |
| pending pods, pod-minutes | 7.613 | 7.596 | down 0.2% | -0.5815 to 0.5482 | shown, not judged |
| utilisation (used / allocatable) | 0.3793 | 0.3817 | up 0.6% | -0.00336 to 0.008039 | shown, not judged |
| CPU used (cores), mean | 2.015 | 2.023 | up 0.4% | -0.01187 to 0.02823 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.005547 | — | 0.00534 to 0.005753 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.015 | 2.028 | up 0.7% | -0.006352 to 0.03381 | shown, not judged |
| energy per core-hour (Wh) | 164.8 | 164.6 | down 0.1% | -1.83 to 1.366 | shown, not judged |
| HPA replicas, mean | 9.372 | 9.383 | up 0.1% | -0.04653 to 0.06784 | shown, not judged |
| pods started | 5.466 | 5.219 | down 4.5% | -0.5666 to 0.0735 | shown, not judged |
| pod start wait, total (s) | 311.1 | 312.5 | up 0.4% | -27.4 to 30.2 | STEADY (inside the noise) |
| pod start wait, mean (s) | 57.73 | 60.24 | up 4.4% | -2.948 to 7.975 | LOSS, up 4.4% (inside the noise) |
| machines billed, machine-hours | 0.5878 | 0.5897 | up 0.3% | -0.009068 to 0.01294 | STEADY (inside the noise) |
| compute bill at list price ($) | 0.05643 | 0.05662 | up 0.3% | -0.0008705 to 0.001242 | STEADY (inside the noise) |

### Run 40126991719

<a id="run-40126991719"></a>

`aks-metered`, steady dial save eastus Standard_D2s_v4; engine **omni-v18** (commit `01eeb7c3b9`, branch `main`); started 2026-10-24 19:48 UTC, ended 2026-10-25 01:44 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-40126991719/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.822 | 2.807 | down 0.6% | -0.0733 to 0.04159 | GAIN, down 0.6% (inside the noise) |
| node-hours | 0.7116 | 0.7082 | down 0.5% | -0.01663 to 0.00985 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 85.21 | 84.88 | down 0.4% | -1.676 to 1.026 | STEADY (inside the noise) |
| energy (Wh) | 81.85 | 81.22 | down 0.8% | -1.553 to 0.2952 | GAIN, down 0.8% (inside the noise) |
| response time (ms), mean | 501.6 | 471.7 | down 6.0% | -104.2 to 44.36 | GAIN, down 6.0% (inside the noise) |
| response time (ms), 95th percentile | 1145 | 1011 | down 11.7% | -270.3 to 2.369 | GAIN, down 11.7% (inside the noise) |
| response time (ms), 99th percentile | 4923 | 4223 | down 14.2% | -5126 to 3725 | GAIN, down 14.2% (inside the noise) |
| time over the response line (% of samples) | 29.33 | 26.23 | down 10.6% | -5.373 to -0.8216 | GAIN, down 10.6% (beyond the noise) |
| failed requests (%) | 4.188 | 4.18 | down 0.2% | -2.061 to 2.045 | GAIN or STEADY, down 0.2% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 | up 7.5% | -0.2415 to 2.241 | LOSS, up 7.5% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 | — | 22.18 to 27.02 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.8 | 3 | up 7.1% | -0.3552 to 0.7552 | LOSS, up 7.1% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.313 | 3.21 | down 3.1% | -1.364 to 1.157 | GAIN, down 3.1% (inside the noise) |
| pending pods, pod-minutes | 4.99 | 5.07 | up 1.6% | -1.204 to 1.364 | shown, not judged |
| utilisation (used / allocatable) | 0.3548 | 0.3526 | down 0.6% | -0.01645 to 0.01204 | shown, not judged |
| CPU used (cores), mean | 1.902 | 1.879 | down 1.2% | -0.06621 to 0.02025 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0049 | — | 0.0034 to 0.0064 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.902 | 1.884 | down 0.9% | -0.06041 to 0.02425 | shown, not judged |
| energy per core-hour (Wh) | 170.7 | 171.3 | up 0.4% | -3.279 to 4.54 | shown, not judged |
| HPA replicas, mean | 9.413 | 9.414 | up 0.0% | -0.3797 to 0.3814 | shown, not judged |
| pods started | 5 | 5 | unchanged 0.0% | 0 to 0 | shown, not judged |
| pod start wait, total (s) | 240.2 | 234.8 | down 2.2% | -89.96 to 79.16 | GAIN, down 2.2% (inside the noise) |
| pod start wait, mean (s) | 48.04 | 46.96 | down 2.2% | -17.99 to 15.83 | GAIN, down 2.2% (inside the noise) |
| machines billed, machine-hours | 0.574 | 0.5819 | up 1.4% | -0.03136 to 0.04714 | power given, up 1.4% (inside the noise) |
| compute bill at list price ($) | 0.0551 | 0.05586 | up 1.4% | -0.003011 to 0.004525 | power given, up 1.4% (inside the noise) |

### Run 40069633316

<a id="run-40069633316"></a>

`aks-metered`, steady replica room 0 to the cap, stopping rule dial save eastus Standard_D2s_v4; engine **omni-v18** (commit `e31395a261`, branch `main`); started 2026-10-24 06:17 UTC, ended 2026-10-29 15:12 UTC; GitHub's conclusion **failure**; 97 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-40069633316/live-reps-aks/LIVE_REPS.json`. The record: 97 of its 100 paired repetitions passed (repetitions 82, 90 and 93 failed); its table is `results/live/AKS_STEADY_100_OMNI_V18.md`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.814 | 2.832 | up 0.7% | -0.009842 to 0.04689 | power given, up 0.7% (inside the noise) |
| node-hours | 0.7104 | 0.715 | up 0.7% | -0.00244 to 0.01172 | power given, up 0.7% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 86.62 | 87.77 | up 1.3% | -0.667 to 2.97 | power given, up 1.3% (inside the noise) |
| energy (Wh) | 82.7 | 83.23 | up 0.6% | -0.2945 to 1.355 | power given, up 0.6% (inside the noise) |
| response time (ms), mean | 517.1 | 503.1 | down 2.7% | -29.76 to 1.881 | GAIN, down 2.7% (inside the noise) |
| response time (ms), 95th percentile | 1245 | 1195 | down 4.0% | -128.5 to 28.56 | GAIN, down 4.0% (inside the noise) |
| response time (ms), 99th percentile | 4744 | 4222 | down 11.0% | -1010 to -34.37 | GAIN, down 11.0% (beyond the noise) |
| time over the response line (% of samples) | 29.06 | 28.81 | down 0.9% | -1.13 to 0.6231 | GAIN, down 0.9% (inside the noise) |
| failed requests (%) | 4.758 | 4.945 | up 3.9% | -0.4799 to 0.8526 | LOSS, up 3.9% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.07 | 13.9 | down 1.2% | -0.4116 to 0.06109 | GAIN, down 1.2% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.92 | — | 24.17 to 25.67 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.598 | 2.392 | down 7.9% | -0.5274 to 0.1151 | GAIN, down 7.9% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 7.018 | 5.993 | down 14.6% | -4.177 to 2.127 | GAIN, down 14.6% (inside the noise) |
| pending pods, pod-minutes | 5.9 | 5.573 | down 5.6% | -0.7542 to 0.09889 | shown, not judged |
| utilisation (used / allocatable) | 0.3622 | 0.3605 | down 0.5% | -0.006925 to 0.003489 | shown, not judged |
| CPU used (cores), mean | 1.935 | 1.937 | up 0.1% | -0.01761 to 0.02085 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.005163 | — | 0.00498 to 0.005346 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.935 | 1.942 | up 0.3% | -0.01246 to 0.02603 | shown, not judged |
| energy per core-hour (Wh) | 169.5 | 170.5 | up 0.6% | -1.158 to 3.091 | shown, not judged |
| HPA replicas, mean | 9.371 | 9.348 | down 0.2% | -0.08016 to 0.03403 | shown, not judged |
| pods started | 5.01 | 4.753 | down 5.1% | -0.7001 to 0.1847 | shown, not judged |
| pod start wait, total (s) | 525.4 | 455.2 | down 13.4% | -278.3 to 137.7 | GAIN, down 13.4% (inside the noise) |
| pod start wait, mean (s) | 98.43 | 89.88 | down 8.7% | -49.24 to 32.14 | GAIN, down 8.7% (inside the noise) |
| machines billed, machine-hours | 0.586 | 0.5931 | up 1.2% | -0.007398 to 0.02162 | power given, up 1.2% (inside the noise) |
| compute bill at list price ($) | 0.05626 | 0.05694 | up 1.2% | -0.0007102 to 0.002076 | power given, up 1.2% (inside the noise) |

### Run 39236324280

<a id="run-39236324280"></a>

`aks-metered`, steady replica room 0 to the cap, stopping rule dial save eastus Standard_D2s_v4; engine **omni-v11** (commit `bdcdf72ee3`, branch `main`); started 2026-10-19 10:16 UTC, ended 2026-10-24 05:00 UTC; GitHub's conclusion **success**; 100 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39236324280/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.831 | 1.831 | down 0.0% | -0.03634 to 0.03578 | STEADY (inside the noise) |
| node-hours | 0.4625 | 0.4632 | up 0.1% | -0.008445 to 0.009773 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 87.16 | 85.85 | down 1.5% | -3.153 to 0.5414 | GAIN, down 1.5% (inside the noise) |
| energy (Wh) | 82.27 | 82.27 | up 0.0% | -0.9954 to 1.001 | STEADY (inside the noise) |
| response time (ms), mean | 506.7 | 498.1 | down 1.7% | -24.36 to 7.156 | GAIN, down 1.7% (inside the noise) |
| response time (ms), 95th percentile | 1172 | 1191 | up 1.7% | -53.92 to 93.1 | LOSS, up 1.7% (inside the noise) |
| response time (ms), 99th percentile | 4523 | 4002 | down 11.5% | -1055 to 13.18 | GAIN, down 11.5% (inside the noise) |
| time over the response line (% of samples) | 28.07 | 28.09 | up 0.1% | -0.9277 to 0.9613 | STEADY (inside the noise) |
| failed requests (%) | 4.394 | 4.035 | down 8.2% | -0.8862 to 0.1693 | GAIN or STEADY, down 8.2% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.92 | 13.97 | up 0.4% | -0.2151 to 0.3151 | STEADY (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.41 | — | 23.74 to 25.08 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.5 | 2.46 | down 1.6% | -0.3219 to 0.2419 | GAIN, down 1.6% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 4.755 | 4.793 | up 0.8% | -2.35 to 2.427 | LOSS, up 0.8% (inside the noise) |
| pending pods, pod-minutes | 5.269 | 5.031 | down 4.5% | -0.665 to 0.188 | shown, not judged |
| utilisation (used / allocatable) | 0.4854 | 0.4845 | down 0.2% | -0.01104 to 0.009332 | shown, not judged |
| CPU used (cores), mean | 1.679 | 1.683 | up 0.2% | -0.01489 to 0.02173 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.004866 | — | 0.004691 to 0.005041 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.679 | 1.688 | up 0.5% | -0.01003 to 0.0266 | shown, not judged |
| energy per core-hour (Wh) | 194.3 | 193.6 | down 0.4% | -3.794 to 2.285 | shown, not judged |
| HPA replicas, mean | 9.317 | 9.362 | up 0.5% | -0.008144 to 0.09799 | shown, not judged |
| pods started | 5.08 | 4.89 | down 3.7% | -0.6436 to 0.2636 | shown, not judged |
| pod start wait, total (s) | 321 | 338.3 | up 5.4% | -138.2 to 172.8 | LOSS, up 5.4% (inside the noise) |
| pod start wait, mean (s) | 60.13 | 66.88 | up 11.2% | -22.63 to 36.12 | LOSS, up 11.2% (inside the noise) |
| machines billed, machine-hours | 0.5971 | 0.5896 | down 1.3% | -0.02339 to 0.008424 | GAIN, down 1.3% (inside the noise) |
| compute bill at list price ($) | 0.05732 | 0.0566 | down 1.3% | -0.002246 to 0.0008087 | GAIN, down 1.3% (inside the noise) |

### Run 39187809233

<a id="run-39187809233"></a>

`aks-metered`, burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v11** (commit `7178928385`, branch `main`); started 2026-10-19 01:59 UTC, ended 2026-10-19 10:15 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39187809233/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.919 | 1.929 | up 0.5% | -0.09141 to 0.1112 | power given, up 0.5% (inside the noise) |
| node-hours | 0.9652 | 0.9674 | up 0.2% | -0.04874 to 0.05318 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 208.2 | 212.6 | up 2.1% | -24.12 to 32.76 | power given, up 2.1% (inside the noise) |
| energy (Wh) | 205.2 | 202.4 | down 1.4% | -16.29 to 10.64 | GAIN, down 1.4% (inside the noise) |
| response time (ms), mean | 450.9 | 432.6 | down 4.0% | -45.12 to 8.594 | GAIN, down 4.0% (inside the noise) |
| response time (ms), 95th percentile | 818.6 | 849.1 | up 3.7% | -145.6 to 206.6 | LOSS, up 3.7% (inside the noise) |
| response time (ms), 99th percentile | 5012 | 3723 | down 25.7% | -3964 to 1385 | GAIN, down 25.7% (inside the noise) |
| time over the response line (% of samples) | 42.66 | 47.04 | up 10.3% | -2.199 to 10.95 | LOSS, up 10.3% (inside the noise) |
| failed requests (%) | 33.14 | 36.74 | up 10.9% | -3.028 to 10.23 | LOSS, up 10.9% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.8 | 29.2 | up 1.4% | -1.266 to 2.066 | LOSS, up 1.4% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40 | — | 34.81 to 45.19 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.2 | 2.8 | up 27.3% | -1.283 to 2.483 | LOSS, up 27.3% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 2.83 | 3.527 | up 24.6% | -1.888 to 3.281 | LOSS, up 24.6% (inside the noise) |
| pending pods, pod-minutes | 4.42 | 6.007 | up 35.9% | -2.889 to 6.062 | shown, not judged |
| utilisation (used / allocatable) | 0.7538 | 0.7337 | down 2.7% | -0.0486 to 0.008327 | shown, not judged |
| CPU used (cores), mean | 2.75 | 2.688 | down 2.3% | -0.2489 to 0.1251 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0041 | — | 0.003381 to 0.004819 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.75 | 2.692 | down 2.1% | -0.2444 to 0.1288 | shown, not judged |
| energy per core-hour (Wh) | 148.5 | 150.2 | up 1.1% | -0.7431 to 4.054 | shown, not judged |
| HPA replicas, mean | 9.64 | 9.686 | up 0.5% | -0.1331 to 0.2255 | shown, not judged |
| pods started | 5.8 | 5 | down 13.8% | -3.021 to 1.421 | shown, not judged |
| pod start wait, total (s) | 215.8 | 263.2 | up 22.0% | -134.4 to 229.2 | LOSS, up 22.0% (inside the noise) |
| pod start wait, mean (s) | 36.24 | 52.64 | up 45.2% | -13.95 to 46.75 | LOSS, up 45.2% (inside the noise) |
| machines billed, machine-hours | 1.118 | 1.111 | down 0.6% | -0.1311 to 0.118 | GAIN, down 0.6% (inside the noise) |
| compute bill at list price ($) | 0.1073 | 0.1067 | down 0.6% | -0.01259 to 0.01133 | GAIN, down 0.6% (inside the noise) |

### Run 39162654399

<a id="run-39162654399"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v11** (commit `4143dc4168`, branch `main`); started 2026-10-18 20:17 UTC, ended 2026-10-19 01:46 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39162654399/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.813 | 1.826 | up 0.8% | -0.05306 to 0.08071 | power given, up 0.8% (inside the noise) |
| node-hours | 0.4574 | 0.4606 | up 0.7% | -0.01392 to 0.02025 | power given, up 0.7% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 86.21 | 85.88 | down 0.4% | -2.351 to 1.687 | STEADY (inside the noise) |
| energy (Wh) | 82.66 | 82.59 | down 0.1% | -1.075 to 0.9367 | STEADY (inside the noise) |
| response time (ms), mean | 562.6 | 514.6 | down 8.5% | -86.8 to -9.34 | GAIN, down 8.5% (beyond the noise) |
| response time (ms), 95th percentile | 1402 | 1155 | down 17.6% | -647.2 to 154 | GAIN, down 17.6% (inside the noise) |
| response time (ms), 99th percentile | 5371 | 4351 | down 19.0% | -3779 to 1739 | GAIN, down 19.0% (inside the noise) |
| time over the response line (% of samples) | 31.77 | 29.63 | down 6.7% | -5.599 to 1.32 | GAIN, down 6.7% (inside the noise) |
| failed requests (%) | 5.853 | 4.437 | down 24.2% | -4.663 to 1.831 | GAIN or STEADY, down 24.2% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 | up 1.4% | -0.8387 to 1.239 | LOSS, up 1.4% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 | — | 22.04 to 31.56 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 | down 7.7% | -2.421 to 2.021 | GAIN, down 7.7% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.15 | 2.413 | down 23.4% | -3.252 to 1.778 | GAIN, down 23.4% (inside the noise) |
| pending pods, pod-minutes | 4.993 | 4.387 | down 12.2% | -2.529 to 1.316 | shown, not judged |
| utilisation (used / allocatable) | 0.5085 | 0.4996 | down 1.8% | -0.03789 to 0.01999 | shown, not judged |
| CPU used (cores), mean | 1.751 | 1.733 | down 1.1% | -0.07133 to 0.03442 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00508 | — | 0.003907 to 0.006253 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.751 | 1.738 | down 0.8% | -0.06725 to 0.04051 | shown, not judged |
| energy per core-hour (Wh) | 187.2 | 189.3 | up 1.1% | -2.218 to 6.322 | shown, not judged |
| HPA replicas, mean | 9.209 | 9.289 | up 0.9% | -0.2558 to 0.4154 | shown, not judged |
| pods started | 6.2 | 5 | down 19.4% | -3.24 to 0.8399 | shown, not judged |
| pod start wait, total (s) | 379.2 | 177.2 | down 53.3% | -608.6 to 204.6 | GAIN, down 53.3% (inside the noise) |
| pod start wait, mean (s) | 68.72 | 35.44 | down 48.4% | -118.2 to 51.62 | GAIN, down 48.4% (inside the noise) |
| machines billed, machine-hours | 0.5801 | 0.5727 | down 1.3% | -0.04988 to 0.03499 | GAIN, down 1.3% (inside the noise) |
| compute bill at list price ($) | 0.05569 | 0.05498 | down 1.3% | -0.004788 to 0.003359 | GAIN, down 1.3% (inside the noise) |

### Run 39119345316

<a id="run-39119345316"></a>

`aks-metered`, burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v10** (commit `faaaff3142`, branch `main`); started 2026-10-18 10:27 UTC, ended 2026-10-18 18:59 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39119345316/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.87 | 1.933 | up 3.3% | -0.1491 to 0.2738 | power given, up 3.3% (inside the noise) |
| node-hours | 0.9414 | 0.9694 | up 3.0% | -0.0808 to 0.1368 | power given, up 3.0% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 205.3 | 222.6 | up 8.4% | -29.16 to 63.74 | power given, up 8.4% (inside the noise) |
| energy (Wh) | 200.4 | 205 | up 2.3% | -7.43 to 16.62 | power given, up 2.3% (inside the noise) |
| response time (ms), mean | 381.5 | 416.6 | up 9.2% | -75.78 to 145.9 | LOSS, up 9.2% (inside the noise) |
| response time (ms), 95th percentile | 805.3 | 974.5 | up 21.0% | -178.9 to 517.2 | LOSS, up 21.0% (inside the noise) |
| response time (ms), 99th percentile | 1974 | 4434 | up 124.6% | -92.6 to 5012 | LOSS, up 124.6% (inside the noise) |
| time over the response line (% of samples) | 48.25 | 41.9 | down 13.2% | -18.46 to 5.746 | GAIN, down 13.2% (inside the noise) |
| failed requests (%) | 38.58 | 33.31 | down 13.7% | -16.17 to 5.625 | GAIN or STEADY, down 13.7% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29 | down 2.0% | -2.015 to 0.8155 | GAIN, down 2.0% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | — | 35.13 to 45.27 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.4 | 3 | up 25.0% | -1.283 to 2.483 | LOSS, up 25.0% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 19.87 | 3.667 | down 81.5% | -63.61 to 31.2 | GAIN, down 81.5% (inside the noise) |
| pending pods, pod-minutes | 6.74 | 7.563 | up 12.2% | -1.483 to 3.13 | shown, not judged |
| utilisation (used / allocatable) | 0.7536 | 0.741 | down 1.7% | -0.07606 to 0.05082 | shown, not judged |
| CPU used (cores), mean | 2.677 | 2.71 | up 1.2% | -0.06814 to 0.1333 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00386 | — | 0.002958 to 0.004762 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.677 | 2.713 | up 1.4% | -0.06372 to 0.1366 | shown, not judged |
| energy per core-hour (Wh) | 148.8 | 150.9 | up 1.4% | -5.6 to 9.84 | shown, not judged |
| HPA replicas, mean | 9.495 | 9.622 | up 1.3% | -0.3935 to 0.6471 | shown, not judged |
| pods started | 5.2 | 3.8 | down 26.9% | -6.993 to 4.193 | shown, not judged |
| pod start wait, total (s) | 1229 | 1075 | down 12.5% | -4230 to 3922 | GAIN, down 12.5% (inside the noise) |
| pod start wait, mean (s) | 240.4 | 259.1 | up 7.8% | -886.7 to 924.2 | LOSS, up 7.8% (inside the noise) |
| machines billed, machine-hours | 1.122 | 1.176 | up 4.9% | -0.1759 to 0.2849 | power given, up 4.9% (inside the noise) |
| compute bill at list price ($) | 0.1077 | 0.1129 | up 4.9% | -0.01688 to 0.02735 | power given, up 4.9% (inside the noise) |

### Run 39100680671

<a id="run-39100680671"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v10** (commit `7ce34b63cf`, branch `main`); started 2026-10-18 05:28 UTC, ended 2026-10-18 20:05 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39100680671/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.844 | 1.809 | down 1.9% | -0.1524 to 0.08339 | GAIN, down 1.9% (inside the noise) |
| node-hours | 0.4662 | 0.4562 | down 2.1% | -0.03821 to 0.01821 | GAIN, down 2.1% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 85.92 | 85.15 | down 0.9% | -2.277 to 0.7295 | GAIN, down 0.9% (inside the noise) |
| energy (Wh) | 82.96 | 81.54 | down 1.7% | -3.773 to 0.9415 | GAIN, down 1.7% (inside the noise) |
| response time (ms), mean | 492.4 | 486.8 | down 1.1% | -95.71 to 84.51 | GAIN, down 1.1% (inside the noise) |
| response time (ms), 95th percentile | 1083 | 1025 | down 5.3% | -182.9 to 67.2 | GAIN, down 5.3% (inside the noise) |
| response time (ms), 99th percentile | 4604 | 4085 | down 11.3% | -5624 to 4585 | GAIN, down 11.3% (inside the noise) |
| time over the response line (% of samples) | 27.81 | 27.25 | down 2.0% | -5.731 to 4.62 | GAIN, down 2.0% (inside the noise) |
| failed requests (%) | 4.38 | 4.507 | up 2.9% | -3.272 to 3.526 | LOSS, up 2.9% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 | up 7.5% | -0.7557 to 2.756 | LOSS, up 7.5% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.4 | — | 23.68 to 29.12 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 | up 8.3% | -1.16 to 1.56 | LOSS, up 8.3% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 10.61 | 10.49 | down 1.1% | -33.5 to 33.26 | GAIN, down 1.1% (inside the noise) |
| pending pods, pod-minutes | 4.843 | 5.01 | up 3.4% | -2.013 to 2.346 | shown, not judged |
| utilisation (used / allocatable) | 0.4776 | 0.4924 | up 3.1% | -0.03671 to 0.06629 | shown, not judged |
| CPU used (cores), mean | 1.668 | 1.692 | up 1.4% | -0.0735 to 0.1204 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0044 | — | 0.003249 to 0.005551 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.668 | 1.696 | up 1.7% | -0.06863 to 0.1243 | shown, not judged |
| energy per core-hour (Wh) | 197 | 191.2 | down 3.0% | -23.07 to 11.38 | shown, not judged |
| HPA replicas, mean | 9.307 | 9.336 | up 0.3% | -0.3693 to 0.4292 | shown, not judged |
| pods started | 6 | 4.4 | down 26.7% | -4.32 to 1.12 | shown, not judged |
| pod start wait, total (s) | 671 | 659.6 | down 1.7% | -1980 to 1957 | GAIN, down 1.7% (inside the noise) |
| pod start wait, mean (s) | 128.6 | 141.6 | up 10.2% | -382.9 to 409 | LOSS, up 10.2% (inside the noise) |
| machines billed, machine-hours | 0.6096 | 0.5799 | down 4.9% | -0.1259 to 0.06643 | GAIN, down 4.9% (inside the noise) |
| compute bill at list price ($) | 0.05852 | 0.05567 | down 4.9% | -0.01208 to 0.006377 | GAIN, down 4.9% (inside the noise) |

### Run 39080133432

<a id="run-39080133432"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v9** (commit `3c44945806`, branch `main`); started 2026-10-17 23:43 UTC, ended 2026-10-18 05:23 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39080133432/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.805 | 1.836 | up 1.8% | -0.03706 to 0.1002 | power given, up 1.7% (inside the noise) |
| node-hours | 0.4545 | 0.4637 | up 2.0% | -0.007267 to 0.02571 | power given, up 2.0% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 85.72 | 85.39 | down 0.4% | -3.508 to 2.85 | STEADY (inside the noise) |
| energy (Wh) | 82.03 | 82.3 | up 0.3% | -1.723 to 2.247 | STEADY (inside the noise) |
| response time (ms), mean | 519.7 | 519.3 | down 0.1% | -70.66 to 69.78 | STEADY (inside the noise) |
| response time (ms), 95th percentile | 1110 | 1389 | up 25.2% | -180.1 to 738.5 | LOSS, up 25.2% (inside the noise) |
| response time (ms), 99th percentile | 4834 | 4221 | down 12.7% | -3761 to 2534 | GAIN, down 12.7% (inside the noise) |
| time over the response line (% of samples) | 28.95 | 29.13 | up 0.6% | -4.741 to 5.095 | LOSS, up 0.6% (inside the noise) |
| failed requests (%) | 4.778 | 3.719 | down 22.2% | -4.266 to 2.148 | GAIN or STEADY, down 22.2% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 13.4 | down 4.3% | -1.28 to 0.07998 | GAIN, down 4.3% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 | — | 20.71 to 28.49 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.6 | 2.6 | unchanged 0.0% | -1.963 to 1.963 | STEADY (inside the noise) |
| time pods had no machine to take them, pod-minutes | 2.91 | 2.787 | down 4.2% | -2.712 to 2.465 | GAIN, down 4.2% (inside the noise) |
| pending pods, pod-minutes | 5.55 | 4.347 | down 21.7% | -4.269 to 1.862 | shown, not judged |
| utilisation (used / allocatable) | 0.4971 | 0.4866 | down 2.1% | -0.05969 to 0.03872 | shown, not judged |
| CPU used (cores), mean | 1.704 | 1.696 | down 0.5% | -0.1244 to 0.1086 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00482 | — | 0.004068 to 0.005572 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.704 | 1.701 | down 0.2% | -0.119 to 0.1129 | shown, not judged |
| energy per core-hour (Wh) | 191.2 | 192.3 | up 0.6% | -8.299 to 10.44 | shown, not judged |
| HPA replicas, mean | 9.322 | 9.368 | up 0.5% | -0.2005 to 0.2912 | shown, not judged |
| pods started | 5.6 | 5.2 | down 7.1% | -1.08 to 0.28 | shown, not judged |
| pod start wait, total (s) | 216.8 | 206.6 | down 4.7% | -188.9 to 168.5 | GAIN, down 4.7% (inside the noise) |
| pod start wait, mean (s) | 39.15 | 39.53 | up 1.0% | -28.06 to 28.81 | LOSS, up 1.0% (inside the noise) |
| machines billed, machine-hours | 0.5806 | 0.5596 | down 3.6% | -0.06695 to 0.02495 | GAIN, down 3.6% (inside the noise) |
| compute bill at list price ($) | 0.05573 | 0.05372 | down 3.6% | -0.006427 to 0.002395 | GAIN, down 3.6% (inside the noise) |

### Run 39014972717

<a id="run-39014972717"></a>

`aks-metered`, burst 1 6 1 8 1 6 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v7** (commit `6e5cea729d`, branch `main`); started 2026-10-17 07:47 UTC, ended 2026-10-17 23:43 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-39014972717/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.899 | 1.915 | up 0.8% | -0.08652 to 0.1177 | power given, up 0.8% (inside the noise) |
| node-hours | 0.9554 | 0.9612 | up 0.6% | -0.04394 to 0.05549 | power given, up 0.6% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 218 | 216.5 | down 0.7% | -15.06 to 11.93 | GAIN, down 0.7% (inside the noise) |
| energy (Wh) | 214.2 | 213.3 | down 0.5% | -17.16 to 15.23 | STEADY (inside the noise) |
| response time (ms), mean | 368.6 | 397.7 | up 7.9% | -94.06 to 152.4 | LOSS, up 7.9% (inside the noise) |
| response time (ms), 95th percentile | 682.7 | 735.1 | up 7.7% | -38.7 to 143.5 | LOSS, up 7.7% (inside the noise) |
| response time (ms), 99th percentile | 3651 | 3585 | down 1.8% | -6412 to 6280 | GAIN, down 1.8% (inside the noise) |
| time over the response line (% of samples) | 45.33 | 45.37 | up 0.1% | -4.691 to 4.775 | STEADY (inside the noise) |
| failed requests (%) | 37.07 | 37.6 | up 1.4% | -1.359 to 2.428 | LOSS, up 1.4% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29.6 | unchanged 0.0% | -1.241 to 1.241 | STEADY (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | — | 31.55 to 40.05 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2 | 2.8 | up 40.0% | -0.8187 to 2.419 | LOSS, up 40.0% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 2.51 | 3.567 | up 42.1% | -0.9744 to 3.088 | LOSS, up 42.1% (inside the noise) |
| pending pods, pod-minutes | 4.23 | 6.783 | up 60.4% | -0.7303 to 5.837 | shown, not judged |
| utilisation (used / allocatable) | 0.8239 | 0.8216 | down 0.3% | -0.06856 to 0.06395 | shown, not judged |
| CPU used (cores), mean | 2.975 | 2.99 | up 0.5% | -0.3181 to 0.3479 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00376 | — | 0.003123 to 0.004397 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.975 | 2.993 | up 0.6% | -0.314 to 0.3513 | shown, not judged |
| energy per core-hour (Wh) | 143.3 | 142.2 | down 0.8% | -6.214 to 3.97 | shown, not judged |
| HPA replicas, mean | 9.515 | 9.679 | up 1.7% | -0.1351 to 0.463 | shown, not judged |
| pods started | 5.2 | 5 | down 3.8% | -0.7552 to 0.3552 | shown, not judged |
| pod start wait, total (s) | 190.2 | 262.8 | up 38.2% | -72.38 to 217.6 | LOSS, up 38.2% (inside the noise) |
| pod start wait, mean (s) | 36.12 | 52.56 | up 45.5% | -11.32 to 44.2 | LOSS, up 45.5% (inside the noise) |
| machines billed, machine-hours | 1.147 | 1.081 | down 5.8% | -0.1743 to 0.04233 | GAIN, down 5.8% (inside the noise) |
| compute bill at list price ($) | 0.1101 | 0.1037 | down 5.8% | -0.01674 to 0.004064 | GAIN, down 5.8% (inside the noise) |

### Run 38981149348

<a id="run-38981149348"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v7** (commit `cf8dccec06`, branch `main`); started 2026-10-16 23:23 UTC, ended 2026-10-17 15:38 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38981149348/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.827 | 1.795 | down 1.7% | -0.07202 to 0.008843 | GAIN, down 1.7% (inside the noise) |
| node-hours | 0.4599 | 0.4508 | down 2.0% | -0.01635 to -0.001758 | GAIN, down 2.0% (beyond the noise) |
| energy, parked workers still on at idle power (Wh) | 84.8 | 85.56 | up 0.9% | -0.8982 to 2.403 | power given, up 0.9% (inside the noise) |
| energy (Wh) | 81.53 | 81.69 | up 0.2% | -1.437 to 1.767 | STEADY (inside the noise) |
| response time (ms), mean | 495.7 | 516.7 | up 4.2% | -47.16 to 89.2 | LOSS, up 4.2% (inside the noise) |
| response time (ms), 95th percentile | 1127 | 1176 | up 4.3% | -213.4 to 311.4 | LOSS, up 4.3% (inside the noise) |
| response time (ms), 99th percentile | 3908 | 4977 | up 27.3% | -761.3 to 2899 | LOSS, up 27.3% (inside the noise) |
| time over the response line (% of samples) | 29.76 | 28.39 | down 4.6% | -6.684 to 3.935 | GAIN, down 4.6% (inside the noise) |
| failed requests (%) | 4.04 | 4.945 | up 22.4% | -0.261 to 2.071 | LOSS, up 22.4% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.6 | down 1.4% | -1.819 to 1.419 | GAIN, down 1.4% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | — | 19.28 to 26.72 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.8 | 2.4 | down 14.3% | -2.283 to 1.483 | GAIN, down 14.3% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.317 | 2.763 | down 16.7% | -3.04 to 1.933 | GAIN, down 16.7% (inside the noise) |
| pending pods, pod-minutes | 5.57 | 5.317 | down 4.5% | -1.761 to 1.254 | shown, not judged |
| utilisation (used / allocatable) | 0.487 | 0.5045 | up 3.6% | -0.007273 to 0.04235 | shown, not judged |
| CPU used (cores), mean | 1.69 | 1.72 | up 1.8% | -0.03716 to 0.09814 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0045 | — | 0.003609 to 0.005391 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.69 | 1.725 | up 2.1% | -0.033 to 0.103 | shown, not judged |
| energy per core-hour (Wh) | 191.7 | 189.1 | down 1.4% | -9.46 to 4.277 | shown, not judged |
| HPA replicas, mean | 9.397 | 9.305 | down 1.0% | -0.3433 to 0.1574 | shown, not judged |
| pods started | 5.2 | 4.4 | down 15.4% | -3.188 to 1.588 | shown, not judged |
| pod start wait, total (s) | 244.6 | 202.4 | down 17.3% | -231.2 to 146.8 | GAIN, down 17.3% (inside the noise) |
| pod start wait, mean (s) | 47.85 | 38.96 | down 18.6% | -47.58 to 29.8 | GAIN, down 18.6% (inside the noise) |
| machines billed, machine-hours | 0.5687 | 0.5831 | up 2.5% | -0.01743 to 0.0462 | power given, up 2.5% (inside the noise) |
| compute bill at list price ($) | 0.05459 | 0.05597 | up 2.5% | -0.001673 to 0.004436 | power given, up 2.5% (inside the noise) |

### Run 38979690890

<a id="run-38979690890"></a>

`aks-metered`, burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v7** (commit `cf8dccec06`, branch `main`); started 2026-10-16 23:07 UTC, ended 2026-10-17 07:46 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38979690890/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.926 | 2.088 | up 8.4% | -0.5238 to 0.8485 | power given, up 8.4% (inside the noise) |
| node-hours | 0.9673 | 1.047 | up 8.2% | -0.266 to 0.4254 | power given, up 8.2% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 220.7 | 219.6 | down 0.5% | -67.66 to 65.56 | STEADY (inside the noise) |
| energy (Wh) | 202.8 | 215.4 | up 6.2% | -29.91 to 55.17 | power given, up 6.2% (inside the noise) |
| response time (ms), mean | 412.1 | 439.2 | up 6.6% | -63.77 to 118 | LOSS, up 6.6% (inside the noise) |
| response time (ms), 95th percentile | 847.9 | 1088 | up 28.3% | -651 to 1131 | LOSS, up 28.3% (inside the noise) |
| response time (ms), 99th percentile | 2777 | 3425 | up 23.3% | -3244 to 4539 | LOSS, up 23.3% (inside the noise) |
| time over the response line (% of samples) | 46.69 | 41.06 | down 12.1% | -19.33 to 8.057 | GAIN, down 12.1% (inside the noise) |
| failed requests (%) | 37.35 | 28.88 | down 22.7% | -23.66 to 6.733 | GAIN or STEADY, down 22.7% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 27.6 | down 6.8% | -6.561 to 2.561 | GAIN, down 6.8% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.4 | — | 31.72 to 39.08 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | down 30.8% | -3.344 to 1.744 | GAIN, down 30.8% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.377 | 2.32 | down 31.3% | -4.272 to 2.159 | GAIN, down 31.3% (inside the noise) |
| pending pods, pod-minutes | 7.087 | 4.583 | down 35.3% | -8.111 to 3.104 | shown, not judged |
| utilisation (used / allocatable) | 0.7306 | 0.7197 | down 1.5% | -0.155 to 0.1331 | shown, not judged |
| CPU used (cores), mean | 2.664 | 2.772 | up 4.1% | -0.1569 to 0.3747 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00416 | — | 0.003667 to 0.004653 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.664 | 2.777 | up 4.2% | -0.1523 to 0.3784 | shown, not judged |
| energy per core-hour (Wh) | 151.6 | 154.5 | up 1.9% | -16.93 to 22.75 | shown, not judged |
| HPA replicas, mean | 9.576 | 9.484 | down 1.0% | -0.5493 to 0.3651 | shown, not judged |
| pods started | 4.8 | 5 | up 4.2% | -0.8387 to 1.239 | shown, not judged |
| pod start wait, total (s) | 250 | 175.4 | down 29.8% | -304.2 to 155 | GAIN, down 29.8% (inside the noise) |
| pod start wait, mean (s) | 52.09 | 35.08 | down 32.7% | -55.26 to 21.24 | GAIN, down 32.7% (inside the noise) |
| machines billed, machine-hours | 1.155 | 1.243 | up 7.6% | -0.3291 to 0.5037 | power given, up 7.6% (inside the noise) |
| compute bill at list price ($) | 0.1109 | 0.1193 | up 7.6% | -0.0316 to 0.04835 | power given, up 7.6% (inside the noise) |

### Run 38652001497

<a id="run-38652001497"></a>

`aks-metered`, burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v5** (commit `ff0cb55d18`, branch `main`); started 2026-10-14 23:06 UTC, ended 2026-10-15 07:15 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38652001497/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.945 | 1.921 | down 1.3% | -0.08191 to 0.0328 | GAIN, down 1.3% (inside the noise) |
| node-hours | 0.9762 | 0.9636 | down 1.3% | -0.04157 to 0.01635 | GAIN, down 1.3% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 220.7 | 214.3 | down 2.9% | -53.68 to 40.93 | GAIN, down 2.9% (inside the noise) |
| energy (Wh) | 203.6 | 203.8 | up 0.1% | -5.127 to 5.608 | STEADY (inside the noise) |
| response time (ms), mean | 450.8 | 454.5 | up 0.8% | -97.68 to 105.2 | LOSS, up 0.8% (inside the noise) |
| response time (ms), 95th percentile | 991.3 | 1043 | up 5.2% | -454 to 556.9 | LOSS, up 5.2% (inside the noise) |
| response time (ms), 99th percentile | 4925 | 5481 | up 11.3% | -3317 to 4429 | LOSS, up 11.3% (inside the noise) |
| time over the response line (% of samples) | 46.29 | 41.92 | down 9.4% | -9.957 to 1.216 | GAIN, down 9.4% (inside the noise) |
| failed requests (%) | 36.41 | 32.61 | down 10.4% | -10.61 to 3.006 | GAIN or STEADY, down 10.4% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 28.2 | down 4.7% | -2.815 to 0.01549 | GAIN, down 4.7% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 | — | 36.37 to 42.03 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 | down 7.7% | -2.041 to 1.641 | GAIN, down 7.7% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.35 | 3.38 | up 0.9% | -2.593 to 2.653 | LOSS, up 0.9% (inside the noise) |
| pending pods, pod-minutes | 7.757 | 6.537 | down 15.7% | -7.841 to 5.401 | shown, not judged |
| utilisation (used / allocatable) | 0.7256 | 0.7508 | up 3.5% | -0.06182 to 0.1124 | shown, not judged |
| CPU used (cores), mean | 2.676 | 2.741 | up 2.4% | -0.2057 to 0.3366 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00462 | — | 0.00379 to 0.00545 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.676 | 2.746 | up 2.6% | -0.2007 to 0.3408 | shown, not judged |
| energy per core-hour (Wh) | 151.8 | 148.3 | down 2.3% | -15.12 to 8.209 | shown, not judged |
| HPA replicas, mean | 9.641 | 9.685 | up 0.5% | -0.03498 to 0.1227 | shown, not judged |
| pods started | 5.8 | 5.2 | down 10.3% | -3.02 to 1.82 | shown, not judged |
| pod start wait, total (s) | 251.6 | 250.6 | down 0.4% | -186.5 to 184.5 | STEADY (inside the noise) |
| pod start wait, mean (s) | 45.16 | 47.98 | up 6.2% | -36.05 to 41.68 | LOSS, up 6.2% (inside the noise) |
| machines billed, machine-hours | 1.129 | 1.11 | down 1.6% | -0.1298 to 0.09332 | GAIN, down 1.6% (inside the noise) |
| compute bill at list price ($) | 0.1083 | 0.1066 | down 1.6% | -0.01246 to 0.008959 | GAIN, down 1.6% (inside the noise) |

### Run 38648741673

<a id="run-38648741673"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v5** (commit `ff0cb55d18`, branch `main`); started 2026-10-14 22:35 UTC, ended 2026-10-15 04:05 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38648741673/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.923 | 1.838 | down 4.4% | -0.3624 to 0.1924 | GAIN, down 4.4% (inside the noise) |
| node-hours | 0.4827 | 0.4629 | down 4.1% | -0.08939 to 0.04973 | GAIN, down 4.1% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 88.6 | 85.79 | down 3.2% | -14.32 to 8.694 | GAIN, down 3.2% (inside the noise) |
| energy (Wh) | 83.39 | 82.74 | down 0.8% | -7.078 to 5.766 | GAIN, down 0.8% (inside the noise) |
| response time (ms), mean | 500.4 | 535.6 | up 7.0% | -76.33 to 146.8 | LOSS, up 7.0% (inside the noise) |
| response time (ms), 95th percentile | 1178 | 1369 | up 16.2% | -159.4 to 541.7 | LOSS, up 16.2% (inside the noise) |
| response time (ms), 99th percentile | 3147 | 4055 | up 28.9% | -1996 to 3812 | LOSS, up 28.9% (inside the noise) |
| time over the response line (% of samples) | 29.57 | 31.21 | up 5.5% | -1.985 to 5.264 | LOSS, up 5.5% (inside the noise) |
| failed requests (%) | 3.731 | 4.425 | up 18.6% | -1.929 to 3.318 | LOSS, up 18.6% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 | up 1.4% | -0.3552 to 0.7552 | LOSS, up 1.4% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.6 | — | 22.25 to 28.95 | shown, not judged |
| pods with no machine to take them (unschedulable) | 1.8 | 2 | up 11.1% | -1.84 to 2.24 | LOSS, up 11.1% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 2.15 | 2.11 | down 1.9% | -2.543 to 2.463 | GAIN, down 1.9% (inside the noise) |
| pending pods, pod-minutes | 4.647 | 5.203 | up 12.0% | -3.641 to 4.754 | shown, not judged |
| utilisation (used / allocatable) | 0.4673 | 0.4984 | up 6.7% | -0.04517 to 0.1074 | shown, not judged |
| CPU used (cores), mean | 1.684 | 1.74 | up 3.3% | -0.04963 to 0.1618 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00514 | — | 0.004196 to 0.006084 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.684 | 1.745 | up 3.6% | -0.04517 to 0.1676 | shown, not judged |
| energy per core-hour (Wh) | 198.3 | 189.1 | down 4.6% | -34.71 to 16.37 | shown, not judged |
| HPA replicas, mean | 9.39 | 9.385 | down 0.1% | -0.194 to 0.1844 | shown, not judged |
| pods started | 4.6 | 4.4 | down 4.3% | -2.24 to 1.84 | shown, not judged |
| pod start wait, total (s) | 157.6 | 160.8 | up 2.0% | -169.3 to 175.7 | LOSS, up 2.0% (inside the noise) |
| pod start wait, mean (s) | 31.28 | 29.74 | down 4.9% | -38.99 to 35.91 | GAIN, down 4.9% (inside the noise) |
| machines billed, machine-hours | 0.5992 | 0.5603 | down 6.5% | -0.1171 to 0.03925 | GAIN, down 6.5% (inside the noise) |
| compute bill at list price ($) | 0.05753 | 0.05379 | down 6.5% | -0.01125 to 0.003768 | GAIN, down 6.5% (inside the noise) |

### Run 38582893457

<a id="run-38582893457"></a>

`aks-metered`, burst 1 6 1 8 1 6 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v5** (commit `c016cbfc34`, branch `main`); started 2026-10-14 14:42 UTC, ended 2026-10-14 23:00 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38582893457/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.89 | 1.876 | down 0.7% | -0.09945 to 0.07295 | GAIN, down 0.7% (inside the noise) |
| node-hours | 0.9495 | 0.9432 | down 0.7% | -0.05126 to 0.0387 | GAIN, down 0.7% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 217.3 | 213.5 | down 1.7% | -11.54 to 3.962 | GAIN, down 1.7% (inside the noise) |
| energy (Wh) | 213.2 | 208.9 | down 2.0% | -15.2 to 6.636 | GAIN, down 2.0% (inside the noise) |
| response time (ms), mean | 395.8 | 404.5 | up 2.2% | -71.23 to 88.64 | LOSS, up 2.2% (inside the noise) |
| response time (ms), 95th percentile | 699.4 | 734.2 | up 5.0% | -34.8 to 104.3 | LOSS, up 5.0% (inside the noise) |
| response time (ms), 99th percentile | 2946 | 2550 | down 13.4% | -2465 to 1673 | GAIN, down 13.4% (inside the noise) |
| time over the response line (% of samples) | 52.47 | 50.62 | down 3.5% | -5.202 to 1.497 | GAIN, down 3.5% (inside the noise) |
| failed requests (%) | 45.89 | 41.89 | down 8.7% | -6.446 to -1.539 | GAIN or STEADY, down 8.7% (beyond the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.4 | 29.6 | up 0.7% | -0.8387 to 1.239 | LOSS, up 0.7% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | — | 30.66 to 35.74 | shown, not judged |
| pods with no machine to take them (unschedulable) | 3.2 | 2.2 | down 31.2% | -3.15 to 1.15 | GAIN, down 31.2% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 20.95 | 3.29 | down 84.3% | -61.33 to 26.01 | GAIN, down 84.3% (inside the noise) |
| pending pods, pod-minutes | 9.793 | 7.33 | down 25.2% | -5.731 to 0.8045 | shown, not judged |
| utilisation (used / allocatable) | 0.8359 | 0.8124 | down 2.8% | -0.05089 to 0.003885 | shown, not judged |
| CPU used (cores), mean | 3.001 | 2.895 | down 3.5% | -0.3376 to 0.1246 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00438 | — | 0.003381 to 0.005379 | shown, not judged |
| CPU used with Omni's own (cores), mean | 3.001 | 2.899 | down 3.4% | -0.3328 to 0.1284 | shown, not judged |
| energy per core-hour (Wh) | 141.5 | 143.5 | up 1.5% | -1.714 to 5.881 | shown, not judged |
| HPA replicas, mean | 9.644 | 9.558 | down 0.9% | -0.4035 to 0.2318 | shown, not judged |
| pods started | 6.2 | 5.4 | down 12.9% | -1.839 to 0.2387 | shown, not judged |
| pod start wait, total (s) | 1640 | 238.2 | down 85.5% | -3915 to 1111 | GAIN, down 85.5% (inside the noise) |
| pod start wait, mean (s) | 221.9 | 41.93 | down 81.1% | -466.4 to 106.6 | GAIN, down 81.1% (inside the noise) |
| machines billed, machine-hours | 1.1 | 1.11 | up 1.0% | -0.07252 to 0.09352 | power given, up 1.0% (inside the noise) |
| compute bill at list price ($) | 0.1056 | 0.1066 | up 1.0% | -0.006962 to 0.008978 | power given, up 1.0% (inside the noise) |

### Run 38561768164

<a id="run-38561768164"></a>

`aks-metered`, burst 2 3 3 4 3 4 4 3 2 2 2 2 2 3 2 3 4 5 4 5 6 7 6 5 replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v5** (commit `bfdb5ad2c2`, branch `main`); started 2026-10-14 12:09 UTC, ended 2026-10-14 22:35 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38561768164/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.932 | 1.936 | up 0.2% | -0.01041 to 0.01927 | STEADY (inside the noise) |
| node-hours | 1.395 | 1.398 | up 0.2% | -0.009991 to 0.01532 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 305.3 | 305 | down 0.1% | -4.9 to 4.239 | STEADY (inside the noise) |
| energy (Wh) | 301.6 | 301.5 | down 0.0% | -4.426 to 4.248 | STEADY (inside the noise) |
| response time (ms), mean | 945.7 | 1067 | up 12.8% | -190.2 to 432.9 | LOSS, up 12.8% (inside the noise) |
| response time (ms), 95th percentile | 3500 | 4276 | up 22.2% | -664.9 to 2216 | LOSS, up 22.2% (inside the noise) |
| response time (ms), 99th percentile | 6979 | 7325 | up 5.0% | -1558 to 2252 | LOSS, up 5.0% (inside the noise) |
| time over the response line (% of samples) | 86.43 | 88.49 | up 2.4% | -1.219 to 5.331 | LOSS, up 2.4% (inside the noise) |
| failed requests (%) | 76.53 | 78.48 | up 2.5% | -0.3527 to 4.252 | LOSS, up 2.5% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 43.2 | 43.2 | unchanged 0.0% | -0.8778 to 0.8778 | STEADY (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 | — | 55.14 to 63.26 | shown, not judged |
| pods with no machine to take them (unschedulable) | 3 | 3 | unchanged 0.0% | 0 to 0 | STEADY (inside the noise) |
| time pods had no machine to take them, pod-minutes | 4.017 | 3.76 | down 6.4% | -1.245 to 0.7312 | GAIN, down 6.4% (inside the noise) |
| pending pods, pod-minutes | 7.373 | 7.697 | up 4.4% | -1.296 to 1.943 | shown, not judged |
| utilisation (used / allocatable) | 0.7876 | 0.7869 | down 0.1% | -0.01704 to 0.01559 | shown, not judged |
| CPU used (cores), mean | 2.891 | 2.895 | up 0.1% | -0.04592 to 0.0538 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00396 | — | 0.003088 to 0.004832 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.891 | 2.899 | up 0.3% | -0.04222 to 0.05801 | shown, not judged |
| energy per core-hour (Wh) | 144.5 | 144.3 | down 0.1% | -1.292 to 0.9209 | shown, not judged |
| HPA replicas, mean | 9.793 | 9.79 | down 0.0% | -0.0976 to 0.0918 | shown, not judged |
| pods started | 5.8 | 5.4 | down 6.9% | -2.283 to 1.483 | shown, not judged |
| pod start wait, total (s) | 285.8 | 270 | down 5.5% | -75.86 to 44.26 | GAIN, down 5.5% (inside the noise) |
| pod start wait, mean (s) | 51.92 | 50.27 | down 3.2% | -17.73 to 14.44 | GAIN, down 3.2% (inside the noise) |
| machines billed, machine-hours | 1.535 | 1.513 | down 1.4% | -0.08306 to 0.03973 | GAIN, down 1.4% (inside the noise) |
| compute bill at list price ($) | 0.1473 | 0.1452 | down 1.4% | -0.007974 to 0.003814 | GAIN, down 1.4% (inside the noise) |

### Run 38516042470

<a id="run-38516042470"></a>

`aks-metered`, burst 1 4 1 6 1 9 replica room 0 dial save eastus Standard_D2_v4; engine **omni-v5** (commit `82c0570a63`, branch `v5`); started 2026-10-14 05:19 UTC, ended 2026-10-14 14:31 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38516042470/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.888 | 1.884 | down 0.2% | -0.1117 to 0.1042 | STEADY (inside the noise) |
| node-hours | 0.9482 | 0.9489 | up 0.1% | -0.05196 to 0.05329 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 204.9 | 205.3 | up 0.2% | -7.365 to 8.063 | STEADY (inside the noise) |
| energy (Wh) | 200.7 | 200.9 | up 0.1% | -10.92 to 11.31 | STEADY (inside the noise) |
| response time (ms), mean | 467.5 | 422.3 | down 9.7% | -112.7 to 22.33 | GAIN, down 9.7% (inside the noise) |
| response time (ms), 95th percentile | 801.6 | 812.8 | up 1.4% | -161.6 to 184.1 | LOSS, up 1.4% (inside the noise) |
| response time (ms), 99th percentile | 4431 | 2594 | down 41.5% | -5217 to 1544 | GAIN, down 41.5% (inside the noise) |
| time over the response line (% of samples) | 50.97 | 45.04 | down 11.6% | -16.4 to 4.548 | GAIN, down 11.6% (inside the noise) |
| failed requests (%) | 40.5 | 33.85 | down 16.4% | -16.78 to 3.488 | GAIN or STEADY, down 16.4% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.8 | 29.6 | down 0.7% | -0.7552 to 0.3552 | GAIN, down 0.7% (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 | — | 35.11 to 40.49 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | down 30.8% | -2.84 to 1.24 | GAIN, down 30.8% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 4.37 | 2.913 | down 33.3% | -4.854 to 1.941 | GAIN, down 33.3% (inside the noise) |
| pending pods, pod-minutes | 9.293 | 7.46 | down 19.7% | -9.514 to 5.848 | shown, not judged |
| utilisation (used / allocatable) | 0.7403 | 0.7465 | up 0.8% | -0.02896 to 0.0413 | shown, not judged |
| CPU used (cores), mean | 2.656 | 2.673 | up 0.7% | -0.2008 to 0.2358 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.004 | — | 0.002932 to 0.005068 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.656 | 2.677 | up 0.8% | -0.1971 to 0.2401 | shown, not judged |
| energy per core-hour (Wh) | 150.5 | 149.4 | down 0.8% | -4.913 to 2.645 | shown, not judged |
| HPA replicas, mean | 9.614 | 9.471 | down 1.5% | -0.5098 to 0.2246 | shown, not judged |
| pods started | 5.4 | 3.8 | down 29.6% | -3.266 to 0.0656 | shown, not judged |
| pod start wait, total (s) | 316.8 | 211.8 | down 33.1% | -350.7 to 140.7 | GAIN, down 33.1% (inside the noise) |
| pod start wait, mean (s) | 58.53 | 42.9 | down 26.7% | -68.18 to 36.92 | GAIN, down 26.7% (inside the noise) |
| machines billed, machine-hours | 1.101 | 1.145 | up 4.0% | -0.03216 to 0.1202 | power given, up 4.0% (inside the noise) |
| compute bill at list price ($) | 0.1057 | 0.1099 | up 4.0% | -0.003087 to 0.01154 | power given, up 4.0% (inside the noise) |

### Run 38516035978

<a id="run-38516035978"></a>

`aks-metered`, steady replica room 0 dial save eastus Standard_D2s_v4; engine **omni-v5** (commit `82c0570a63`, branch `v5`); started 2026-10-14 05:19 UTC, ended 2026-10-14 12:01 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial save (the tune-down, the machines alone); counted set. Receipt `raw:run-38516035978/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.795 | 1.793 | down 0.1% | -0.04299 to 0.03902 | STEADY (inside the noise) |
| node-hours | 0.4527 | 0.4516 | down 0.3% | -0.01083 to 0.0085 | STEADY (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 85.5 | 84.59 | down 1.1% | -1.709 to -0.1043 | GAIN, down 1.1% (beyond the noise) |
| energy (Wh) | 81.62 | 80.68 | down 1.1% | -1.89 to 0.01842 | GAIN, down 1.1% (inside the noise) |
| response time (ms), mean | 549.2 | 563.3 | up 2.6% | -30.79 to 59.06 | LOSS, up 2.6% (inside the noise) |
| response time (ms), 95th percentile | 1281 | 1415 | up 10.5% | -332.8 to 601.7 | LOSS, up 10.5% (inside the noise) |
| response time (ms), 99th percentile | 5657 | 5832 | up 3.1% | -1792 to 2142 | LOSS, up 3.1% (inside the noise) |
| time over the response line (% of samples) | 31.37 | 30.44 | down 3.0% | -3.15 to 1.291 | GAIN, down 3.0% (inside the noise) |
| failed requests (%) | 5.613 | 4.621 | down 17.7% | -3.033 to 1.048 | GAIN or STEADY, down 17.7% (inside the noise) |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.8 | unchanged 0.0% | -1.963 to 1.963 | STEADY (inside the noise) |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.4 | — | 20.42 to 28.38 | shown, not judged |
| pods with no machine to take them (unschedulable) | 1.8 | 3.2 | up 77.8% | -0.4828 to 3.283 | LOSS, up 77.8% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 10.15 | 4.777 | down 52.9% | -26.41 to 15.66 | GAIN, down 52.9% (inside the noise) |
| pending pods, pod-minutes | 7.943 | 8.5 | up 7.0% | -1.112 to 2.225 | shown, not judged |
| utilisation (used / allocatable) | 0.4987 | 0.5011 | up 0.5% | -0.01565 to 0.02035 | shown, not judged |
| CPU used (cores), mean | 1.7 | 1.707 | up 0.4% | -0.05166 to 0.06512 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.00586 | — | 0.004604 to 0.007116 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.7 | 1.713 | up 0.7% | -0.04584 to 0.07103 | shown, not judged |
| energy per core-hour (Wh) | 190.4 | 187.7 | down 1.4% | -8.345 to 2.989 | shown, not judged |
| HPA replicas, mean | 9.361 | 9.4 | up 0.4% | -0.1424 to 0.2201 | shown, not judged |
| pods started | 4.6 | 5.2 | up 13.0% | -3.384 to 4.584 | shown, not judged |
| pod start wait, total (s) | 631.8 | 336.2 | down 46.8% | -1549 to 957.4 | GAIN, down 46.8% (inside the noise) |
| pod start wait, mean (s) | 120.3 | 64.41 | down 46.5% | -317.2 to 205.3 | GAIN, down 46.5% (inside the noise) |
| machines billed, machine-hours | 0.583 | 0.5727 | down 1.8% | -0.01908 to -0.001587 | GAIN, down 1.8% (beyond the noise) |
| compute bill at list price ($) | 0.05597 | 0.05498 | down 1.8% | -0.001832 to -0.0001524 | GAIN, down 1.8% (beyond the noise) |

### Run 38455383137

<a id="run-38455383137"></a>

`aks-metered`, steady eastus Standard_D2s_v4; engine **omni-v5** (commit `7d56c81f02`, branch `v5`); started 2026-10-13 19:30 UTC, ended 2026-10-14 04:42 UTC; GitHub's conclusion **cancelled**; 4 paired repetitions; the dial the engine's default of the day; counted set. Receipt `raw:run-38455383137/live-reps-aks/LIVE_REPS.json`. The record: cancelled on 14 October before the set's end; its receipt reads the repetitions it finished.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.797 | 2.971 | up 65.4% | 0.9815 to 1.367 | power given, up 65.4% (beyond the noise) |
| node-hours | 0.4506 | 0.7517 | up 66.8% | 0.2503 to 0.3519 | power given, up 66.8% (beyond the noise) |
| energy, parked workers still on at idle power (Wh) | 85.56 | 129.7 | up 51.6% | 42.81 to 45.42 | power given, up 51.6% (beyond the noise) |
| energy (Wh) | 81.75 | 110.2 | up 34.8% | 24.13 to 32.71 | power given, up 34.8% (beyond the noise) |
| response time (ms), mean | 493.1 | 322.7 | down 34.6% | -221.7 to -119.2 | GAIN, down 34.6% (beyond the noise) |
| response time (ms), 95th percentile | 1099 | 725.5 | down 34.0% | -526.4 to -219.8 | GAIN, down 34.0% (beyond the noise) |
| response time (ms), 99th percentile | 4446 | 1257 | down 71.7% | -5269 to -1109 | GAIN, down 71.7% (beyond the noise) |
| time over the response line (% of samples) | 29.31 | 13.9 | down 52.6% | -18.23 to -12.6 | GAIN, down 52.6% (beyond the noise) |
| failed requests (%) | 5.425 | 0.9023 | down 83.4% | -6.335 to -2.711 | GAIN or STEADY, down 83.4% (beyond the noise) |
| pods with no machine to take them (unschedulable) | 2.75 | 11.25 | up 309.1% | -1.77 to 18.77 | LOSS, up 309.1% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 12.95 | 13.75 | up 6.2% | -38.99 to 40.6 | LOSS, up 6.2% (inside the noise) |
| pending pods, pod-minutes | 7.625 | 29.65 | up 288.8% | 11.05 to 32.99 | shown, not judged |
| utilisation (used / allocatable) | 0.5068 | 0.2923 | down 42.3% | -0.2525 to -0.1765 | shown, not judged |
| CPU used (cores), mean | 1.73 | 1.646 | down 4.9% | -0.1942 to 0.02578 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.01405 | — | 0.01053 to 0.01757 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.73 | 1.66 | down 4.1% | -0.1786 to 0.03833 | shown, not judged |
| energy per core-hour (Wh) | 188.4 | 265.1 | up 40.7% | 48.68 to 104.8 | shown, not judged |
| HPA replicas, mean | 9.424 | 19.65 | up 108.5% | 8.64 to 11.82 | shown, not judged |
| pods started | 6 | 16.75 | up 179.2% | -8.092 to 29.59 | shown, not judged |
| pod start wait, total (s) | 814 | 994.2 | up 22.1% | -2325 to 2685 | LOSS, up 22.1% (inside the noise) |
| pod start wait, mean (s) | 109.1 | 60.03 | down 45.0% | -217.1 to 119 | GAIN, down 45.0% (inside the noise) |
| machines billed, machine-hours | 0.5822 | 0.8804 | up 51.2% | 0.2352 to 0.3613 | power given, up 51.2% (beyond the noise) |
| compute bill at list price ($) | 0.05589 | 0.08452 | up 51.2% | 0.02258 to 0.03469 | power given, up 51.2% (beyond the noise) |

### Run 38339858727

<a id="run-38339858727"></a>

`aks-metered`, the steady set; engine **no declared engine (its commit matches no declared fingerprint)** (commit `148565d255`, branch `main`); started 2026-10-13 03:03 UTC, ended 2026-10-13 09:23 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial the engine's default of the day; counted set. Receipt `raw:run-38339858727/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.813 | 1.92 | up 5.9% | -0.05529 to 0.2704 | power given, up 5.9% (inside the noise) |
| node-hours | 0.4567 | 0.4846 | up 6.1% | -0.01435 to 0.07013 | power given, up 6.1% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 85.65 | 93.77 | up 9.5% | -4.641 to 20.9 | power given, up 9.5% (inside the noise) |
| energy (Wh) | 82.11 | 84.69 | up 3.1% | -0.7226 to 5.877 | power given, up 3.1% (inside the noise) |
| response time (ms), mean | 516 | 515.7 | down 0.1% | -132.2 to 131.5 | STEADY (inside the noise) |
| response time (ms), 95th percentile | 1336 | 1178 | down 11.8% | -978.1 to 662.2 | GAIN, down 11.8% (inside the noise) |
| response time (ms), 99th percentile | 4154 | 4455 | up 7.2% | -2147 to 2749 | LOSS, up 7.2% (inside the noise) |
| time over the response line (% of samples) | 29.6 | 30.34 | up 2.5% | -6.062 to 7.528 | LOSS, up 2.5% (inside the noise) |
| failed requests (%) | 4.373 | 4.812 | up 10.1% | -1.424 to 2.303 | LOSS, up 10.1% (inside the noise) |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 | up 8.3% | -1.641 to 2.041 | LOSS, up 8.3% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.423 | 3.277 | down 4.3% | -2.647 to 2.353 | GAIN, down 4.3% (inside the noise) |
| pending pods, pod-minutes | 6.567 | 6.713 | up 2.2% | -1.938 to 2.231 | shown, not judged |
| utilisation (used / allocatable) | 0.4983 | 0.484 | down 2.9% | -0.07239 to 0.0439 | shown, not judged |
| CPU used (cores), mean | 1.715 | 1.755 | up 2.3% | -0.08662 to 0.1664 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.01362 | — | 0.0123 to 0.01494 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.715 | 1.769 | up 3.1% | -0.07356 to 0.1806 | shown, not judged |
| energy per core-hour (Wh) | 190.2 | 192 | up 0.9% | -11.33 to 14.87 | shown, not judged |
| HPA replicas, mean | 9.357 | 9.488 | up 1.4% | -0.2331 to 0.496 | shown, not judged |
| pods started | 5.4 | 4.2 | down 22.2% | -4.031 to 1.631 | shown, not judged |
| pod start wait, total (s) | 243.4 | 220.2 | down 9.5% | -243.3 to 196.9 | GAIN, down 9.5% (inside the noise) |
| pod start wait, mean (s) | 45.92 | 42.32 | down 7.8% | -50.15 to 42.95 | GAIN, down 7.8% (inside the noise) |
| machines billed, machine-hours | 0.5733 | 0.6254 | up 9.1% | -0.04102 to 0.1452 | power given, up 9.1% (inside the noise) |
| compute bill at list price ($) | 0.05504 | 0.06004 | up 9.1% | -0.003938 to 0.01394 | power given, up 9.1% (inside the noise) |

### Run 37534538088

<a id="run-37534538088"></a>

`aks-metered`, the steady set; engine **omni-v1** (commit `f162ce8d74`, branch `omni-v1`); started 2026-10-06 21:31 UTC, ended 2026-10-07 06:47 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial the engine's default of the day; counted set. Receipt `raw:run-37534538088/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.908 | 1.946 | up 2.0% | -0.03781 to 0.1138 | power given, up 2.0% (inside the noise) |
| node-hours | 0.9581 | 0.9779 | up 2.1% | -0.01685 to 0.05652 | power given, up 2.1% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 183.1 | 186 | up 1.6% | -0.005012 to 5.762 | power given, up 1.6% (inside the noise) |
| energy (Wh) | 179.7 | 184 | up 2.4% | -0.8413 to 9.457 | power given, up 2.4% (inside the noise) |
| response time (ms), mean | 500.3 | 498.6 | down 0.3% | -85.06 to 81.63 | STEADY (inside the noise) |
| response time (ms), 95th percentile | 1090 | 1254 | up 15.0% | -579.3 to 907.1 | LOSS, up 15.0% (inside the noise) |
| response time (ms), 99th percentile | 5975 | 3967 | down 33.6% | -3672 to -344.7 | GAIN, down 33.6% (beyond the noise) |
| time over the response line (% of samples) | 34.94 | 35 | up 0.2% | -4.175 to 4.292 | STEADY (inside the noise) |
| failed requests (%) | 22.27 | 15.58 | down 30.0% | -18.74 to 5.363 | GAIN or STEADY, down 30.0% (inside the noise) |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | down 30.8% | -3.491 to 1.891 | GAIN, down 30.8% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.67 | 2.22 | down 39.5% | -5.351 to 2.451 | GAIN, down 39.5% (inside the noise) |
| pending pods, pod-minutes | 5.733 | 3.357 | down 41.5% | -7.642 to 2.889 | shown, not judged |
| utilisation (used / allocatable) | 0.5854 | 0.5845 | down 0.2% | -0.025 to 0.02319 | shown, not judged |
| CPU used (cores), mean | 2.122 | 2.16 | up 1.8% | -0.01065 to 0.08666 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.0099 | — | 0.007312 to 0.01249 | shown, not judged |
| CPU used with Omni's own (cores), mean | 2.122 | 2.17 | up 2.3% | -0.002528 to 0.09834 | shown, not judged |
| energy per core-hour (Wh) | 168.6 | 169.5 | up 0.5% | -3.593 to 5.315 | shown, not judged |
| HPA replicas, mean | 9.702 | 9.701 | down 0.0% | -0.09167 to 0.08921 | shown, not judged |
| pods started | 5.2 | 5.2 | unchanged 0.0% | -0.8778 to 0.8778 | shown, not judged |
| pod start wait, total (s) | 257.4 | 165 | down 35.9% | -350.8 to 166 | GAIN, down 35.9% (inside the noise) |
| pod start wait, mean (s) | 50.85 | 31.13 | down 38.8% | -71.89 to 32.43 | GAIN, down 38.8% (inside the noise) |
| machines billed, machine-hours | 1.088 | 1.141 | up 5.0% | -0.03082 to 0.1387 | power given, up 5.0% (inside the noise) |
| compute bill at list price ($) | 0.1044 | 0.1096 | up 5.0% | -0.002959 to 0.01332 | power given, up 5.0% (inside the noise) |

### Run 37385657374

<a id="run-37385657374"></a>

`aks-metered`, the steady set; engine **omni-v1** (commit `f162ce8d74`, branch `main`); started 2026-10-05 22:57 UTC, ended 2026-10-06 20:42 UTC; GitHub's conclusion **success**; 5 paired repetitions; the dial the engine's default of the day; counted set. Receipt `raw:run-37385657374/live-reps-aks/LIVE_REPS.json`.

| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.849 | 1.902 | up 2.8% | -0.3088 to 0.414 | power given, up 2.8% (inside the noise) |
| node-hours | 0.4648 | 0.4831 | up 3.9% | -0.07144 to 0.1079 | power given, up 3.9% (inside the noise) |
| energy, parked workers still on at idle power (Wh) | 94.1 | 93.73 | down 0.4% | -38.87 to 38.12 | STEADY (inside the noise) |
| energy (Wh) | 83.75 | 84.24 | up 0.6% | -11.42 to 12.41 | power given, up 0.6% (inside the noise) |
| response time (ms), mean | 503.6 | 507.2 | up 0.7% | -110.3 to 117.4 | LOSS, up 0.7% (inside the noise) |
| response time (ms), 95th percentile | 1079 | 1056 | down 2.1% | -405.6 to 360.1 | GAIN, down 2.1% (inside the noise) |
| response time (ms), 99th percentile | 4918 | 4634 | down 5.8% | -4823 to 4256 | GAIN, down 5.8% (inside the noise) |
| time over the response line (% of samples) | 27.21 | 28.09 | up 3.3% | -3.523 to 5.298 | LOSS, up 3.3% (inside the noise) |
| failed requests (%) | 5.144 | 3.485 | down 32.3% | -4.266 to 0.948 | GAIN or STEADY, down 32.3% (inside the noise) |
| pods with no machine to take them (unschedulable) | 2.8 | 3 | up 7.1% | -0.3552 to 0.7552 | LOSS, up 7.1% (inside the noise) |
| time pods had no machine to take them, pod-minutes | 3.21 | 3.69 | up 15.0% | -1.091 to 2.051 | LOSS, up 15.0% (inside the noise) |
| pending pods, pod-minutes | 6.337 | 6.55 | up 3.4% | -1.521 to 1.947 | shown, not judged |
| utilisation (used / allocatable) | 0.4831 | 0.4675 | down 3.2% | -0.107 to 0.07583 | shown, not judged |
| CPU used (cores), mean | 1.682 | 1.681 | down 0.0% | -0.03797 to 0.03726 | shown, not judged |
| Omni's own CPU (cores), mean | 0 | 0.01446 | — | 0.01296 to 0.01596 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.682 | 1.696 | up 0.8% | -0.02439 to 0.05261 | shown, not judged |
| energy per core-hour (Wh) | 198 | 197.3 | down 0.3% | -31.62 to 30.36 | shown, not judged |
| HPA replicas, mean | 9.294 | 9.564 | up 2.9% | -0.1062 to 0.6459 | shown, not judged |
| pods started | 5.2 | 5 | down 3.8% | -0.7552 to 0.3552 | shown, not judged |
| pod start wait, total (s) | 231.2 | 263 | up 13.8% | -58.05 to 121.7 | LOSS, up 13.8% (inside the noise) |
| pod start wait, mean (s) | 44.95 | 52.6 | up 17.0% | -11.6 to 26.9 | LOSS, up 17.0% (inside the noise) |
| machines billed, machine-hours | 0.6622 | 0.6312 | down 4.7% | -0.2911 to 0.2291 | GAIN, down 4.7% (inside the noise) |
| compute bill at list price ($) | 0.06357 | 0.06059 | down 4.7% | -0.02794 to 0.02199 | GAIN, down 4.7% (inside the noise) |

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
