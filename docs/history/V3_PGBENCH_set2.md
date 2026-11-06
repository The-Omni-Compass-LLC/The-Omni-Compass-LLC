# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any increase in any run is WORSE. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37858494179 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 37858496620 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 37858499033 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 35,851, 25,657, 15,708 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 15,772 | 15,771 | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.2) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 15,772 | 15,771 | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.2) | -0.0% (-0.3 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 0.333 | 0.293 | -11.8% (-42.2 to +18.6) | +22.6% (-13.1 to +58.2) | +17.6% (-2.5 to +37.8) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 1.14 | 1.87 | +64.5% (-311.0 to +440.0) | +29.5% (+16.4 to +42.6) | +175.2% (+25.9 to +324.4) | no difference beyond the noise (1 of 3 runs) |
| latency, median (ms) | 0.158 | 0.152 | -3.8% (-9.5 to +1.9) | +0.9% (+0.4 to +1.5) | +0.7% (-3.3 to +4.7) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 0.201 | 0.284 | +41.5% (-55.1 to +138.1) | +15.5% (+1.5 to +29.5) | +46.0% (+24.8 to +67.1) | no difference beyond the noise (1 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 11.9 | -38.4% (-51.2 to -25.6) | -35.7% (-54.9 to -16.6) | -38.3% (-60.8 to -15.7) | **confirmed better** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.352 | 0.34 | -3.3% (-10.7 to +4.1) | +0.9% (+0.4 to +1.4) | +2.4% (-4.9 to +9.7) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 399.3 | 386.4 | -3.2% (-10.3 to +3.8) | +0.9% (+0.1 to +1.8) | +2.8% (-5.4 to +11.0) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0844 | 0.0817 | -3.2% (-10.3 to +3.9) | +1.0% (+0.3 to +1.7) | +2.9% (-5.4 to +11.2) | no difference beyond the noise (2 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.77 | 2.2 | +24.4% (+17.1 to +31.6) | +37.6% (+35.3 to +39.8) | +54.3% (+45.2 to +63.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 14.1 | -29.5% (-40.5 to -18.5) | -30.9% (-33.4 to -28.4) | -29.9% (-30.2 to -29.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,610, 7,872, 2,570 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3,105 | 3,080 | -0.8% (-5.0 to +3.4) | -2.5% (-6.8 to +1.9) | +1.4% (-15.4 to +18.3) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 3,340 | 3,341 | +0.0% (-0.8 to +0.9) | -0.0% (-1.2 to +1.2) | +0.2% (+0.1 to +0.3) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 201.0 | 260.1 | +29.4% (-46.1 to +104.8) | +54.8% (-74.2 to +183.7) | -10.0% (-207.9 to +187.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 572.9 | 636.2 | +11.0% (-34.4 to +56.5) | -2.1% (-22.0 to +17.9) | -27.9% (-123.3 to +67.4) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.03 | 1.04 | +1.1% (+0.6 to +1.6) | +1.0% (-4.1 to +6.2) | -0.3% (-5.8 to +5.2) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 26.7 | 31.1 | +16.6% (-60.1 to +93.3) | +30.1% (-51.3 to +111.5) | -18.4% (-164.1 to +127.2) | no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 21.6 | +7.8% (+3.0 to +12.6) | +10.3% (-3.6 to +24.1) | +9.3% (-3.4 to +22.1) | no difference beyond the noise (2 of 3 runs) |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+55.2 to +104.8) | +78.3% (+71.2 to +85.5) | +71.7% (+52.7 to +90.6) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.414 | 0.421 | +1.7% (+0.5 to +2.9) | +2.7% (-0.4 to +5.8) | +1.7% (+1.5 to +1.9) | no difference beyond the noise (1 of 3 runs) |
| host CPU-seconds | 476.3 | 485.1 | +1.8% (+0.6 to +3.1) | +2.7% (-0.3 to +5.8) | +1.6% (+1.1 to +2.2) | no difference beyond the noise (1 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.512 | 0.525 | +2.6% (-2.5 to +7.7) | +5.3% (+0.2 to +10.5) | +0.2% (-17.0 to +17.4) | no difference beyond the noise (2 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.644 | 1.06 | +65.0% (+62.9 to +67.2) | +86.9% (+73.9 to +99.8) | +116.3% (+108.5 to +124.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.1 | +10.3% (+7.0 to +13.7) | +12.3% (-0.8 to +25.3) | +11.1% (-1.9 to +24.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,103, 1,835, 1,851 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 531.6 | 382.2 | -28.1% (-102.5 to +46.3) | +0.1% (-0.0 to +0.2) | -0.2% (-0.6 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 878.0 | 885.9 | +0.9% (-7.1 to +8.9) | +0.1% (-0.0 to +0.2) | -0.2% (-0.6 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 2,402 | 2,522 | +5.0% (-92.6 to +102.5) | +11.3% (+6.2 to +16.5) | +5.4% (-14.3 to +25.1) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 3,806 | 3,311 | -13.0% (-111.7 to +85.6) | +60.4% (+16.7 to +104.0) | +49.5% (+13.6 to +85.4) | no difference beyond the noise (1 of 3 runs) |
| latency, median (ms) | 28.5 | 135.3 | +375.2% (-563.7 to +1314.2) | +0.7% (-3.1 to +4.4) | +1.0% (-0.7 to +2.6) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 455.9 | 610.2 | +33.9% (-108.3 to +176.0) | +9.6% (+2.3 to +16.8) | +7.9% (+0.6 to +15.1) | no difference beyond the noise (1 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 21.0 | +5.1% (+1.2 to +9.1) | -46.1% (-58.2 to -34.0) | -48.5% (-60.9 to -36.0) | **the runs disagree** |
| server connections alive, most at once | 20.0 | 30.0 | +50.0% (+28.5 to +71.5) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.224 | 0.237 | +5.8% (-0.1 to +11.8) | +2.4% (-2.6 to +7.4) | +2.3% (-0.9 to +5.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 262.6 | 278.6 | +6.1% (+0.2 to +12.0) | +2.5% (-2.7 to +7.7) | +2.4% (-0.9 to +5.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.73 | 2.46 | +42.6% (-41.3 to +126.4) | +2.5% (-2.8 to +7.8) | +2.6% (-0.4 to +5.6) | no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.411 | 0.821 | +100.1% (+95.5 to +104.6) | +154.8% (+145.1 to +164.4) | +157.6% (+148.4 to +166.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.7% (-3.4 to +4.7) | -40.6% (-45.8 to -35.3) | -42.9% (-48.3 to -37.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

**Across 3 workloads: 1 gauge-rows confirmed better, 1 confirmed worse, 1 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
