# Kafka, a consumer group's operator-set size: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any increase in any run is WORSE. The tuning workload is shown and not counted. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37697222651 | `a0b5d2381e9e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 37697239400 | `a0b5d2381e9e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 37697255445 | `a0b5d2381e9e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 975, 976, 969 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369.4 | 428.5 | +16.0% (+15.2 to +16.9) | +16.3% (+15.0 to +17.6) | +15.4% (+14.5 to +16.2) | **confirmed better** |
| throughput (messages a second consumed) | 428.7 | 428.7 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 1,617 | 10.2 | -99.4% (-107.8 to -91.0) | -99.4% (-131.5 to -67.4) | -99.3% (-104.3 to -94.4) | **confirmed better** |
| end-to-end latency, 99th percentile (ms) | 2,500 | 12.1 | -99.5% (-107.0 to -92.0) | -99.5% (-123.4 to -75.7) | -99.5% (-106.9 to -92.1) | **confirmed better** |
| end-to-end latency, median (ms) | 8.52 | 7.31 | -14.2% (-16.8 to -11.6) | -14.3% (-15.9 to -12.6) | -15.1% (-15.8 to -14.4) | **confirmed better** |
| end-to-end latency, mean (ms) | 220.6 | 7.92 | -96.4% (-107.5 to -85.3) | -96.8% (-126.8 to -66.8) | -96.2% (-104.9 to -87.5) | **confirmed better** |
| consumer lag, most messages waiting at once | 1,142 | 67.0 | -94.1% (-101.0 to -87.2) | -96.0% (-117.1 to -75.0) | -95.7% (-101.6 to -89.8) | **confirmed better** |
| consumer lag, mean messages waiting | 98.6 | 3.47 | -96.5% (-106.2 to -86.7) | -96.9% (-126.5 to -67.3) | -96.3% (-103.5 to -89.2) | **confirmed better** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 7.27 | +263.5% (+121.5 to +405.5) | +296.6% (+296.3 to +296.8) | +296.5% (+296.2 to +296.7) | **confirmed WORSE** |
| consumers running, most at once | 2 | 7.33 | +266.7% (+123.2 to +410.1) | +300.0% (+300.0 to +300.0) | +300.0% (+300.0 to +300.0) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.308 | 0.329 | +6.9% (+4.7 to +9.2) | +5.1% (+2.7 to +7.6) | +8.6% (+3.7 to +13.6) | **confirmed WORSE** |
| host CPU-seconds | 356.9 | 381.4 | +6.9% (+4.9 to +8.9) | +4.9% (+2.9 to +6.9) | +8.7% (+4.0 to +13.4) | **confirmed WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 2.97 | -7.9% (-10.9 to -4.9) | -9.8% (-11.1 to -8.5) | -5.8% (-10.8 to -0.8) | **confirmed better** |
| consumer changes written (the knob's moves) | 2 | 14.7 | +633.3% (+346.5 to +920.2) | +700.0% (+700.0 to +700.0) | +700.0% (+700.0 to +700.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 974, 975, 977 messages a second; steps 1 6 1 8 1 6 × 20.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 347.5 | 418.8 | +20.5% (+20.1 to +20.9) | +20.2% (+19.9 to +20.5) | +20.8% (+20.6 to +20.9) | **confirmed better** |
| throughput (messages a second consumed) | 417.5 | 419.2 | +0.4% (+0.4 to +0.4) | -0.0% (-0.0 to +0.0) | +0.4% (+0.4 to +0.4) | no difference beyond the noise (1 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 1,671 | 10.9 | -99.3% (-104.5 to -94.2) | -99.4% (-108.3 to -90.5) | -99.4% (-106.1 to -92.6) | **confirmed better** |
| end-to-end latency, 99th percentile (ms) | 2,462 | 13.6 | -99.4% (-112.7 to -86.2) | -99.5% (-104.1 to -94.8) | -99.5% (-104.0 to -94.9) | **confirmed better** |
| end-to-end latency, median (ms) | 10.2 | 7.96 | -22.0% (-33.7 to -10.3) | -18.9% (-23.6 to -14.3) | -20.7% (-30.7 to -10.7) | **confirmed better** |
| end-to-end latency, mean (ms) | 262.1 | 9.11 | -96.5% (-99.5 to -93.5) | -96.7% (-97.3 to -96.1) | -96.7% (-98.8 to -94.5) | **confirmed better** |
| consumer lag, most messages waiting at once | 1,102 | 49.7 | -95.5% (-101.0 to -90.0) | -96.3% (-103.3 to -89.2) | -96.3% (-101.0 to -91.5) | **confirmed better** |
| consumer lag, mean messages waiting | 116.2 | 3.82 | -96.7% (-100.3 to -93.1) | -96.9% (-97.7 to -96.0) | -96.9% (-102.7 to -91.1) | **confirmed better** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 5.84 | +191.9% (+166.6 to +217.2) | +207.5% (+94.5 to +320.5) | +183.3% (+153.0 to +213.7) | **confirmed WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% (+300.0 to +300.0) | +266.7% (+123.2 to +410.1) | +300.0% (+300.0 to +300.0) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.318 | +7.3% (-1.2 to +15.8) | +8.3% (+4.8 to +11.7) | +6.4% (-1.6 to +14.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 138.4 | 147.8 | +6.7% (-1.8 to +15.2) | +8.0% (+4.4 to +11.6) | +5.7% (-2.2 to +13.6) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.3 | 2.94 | -11.0% (-19.8 to -2.3) | -10.1% (-14.9 to -5.4) | -12.1% (-19.9 to -4.2) | **confirmed better** |
| consumer changes written (the knob's moves) | 2 | 16.0 | +700.0% (+700.0 to +700.0) | +633.3% (+346.5 to +920.2) | +700.0% (+700.0 to +700.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 392, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148.4 | 172.2 | +16.0% (+15.0 to +17.1) | +15.8% (+15.1 to +16.5) | +15.8% (+15.5 to +16.1) | **confirmed better** |
| throughput (messages a second consumed) | 172.5 | 172.3 | -0.1% (-0.3 to +0.1) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 1,608 | 14.2 | -99.1% (-109.6 to -88.7) | -99.2% (-103.6 to -94.9) | -98.6% (-104.7 to -92.6) | **confirmed better** |
| end-to-end latency, 99th percentile (ms) | 2,545 | 18.4 | -99.3% (-110.7 to -87.9) | -99.3% (-107.0 to -91.7) | -88.3% (-94.8 to -81.7) | **confirmed better** |
| end-to-end latency, median (ms) | 11.6 | 11.5 | -1.3% (-8.9 to +6.3) | -0.6% (-4.6 to +3.4) | -1.1% (-2.7 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 222.6 | 12.1 | -94.6% (-108.3 to -80.9) | -94.4% (-101.7 to -87.0) | -91.8% (-94.5 to -89.1) | **confirmed better** |
| consumer lag, most messages waiting at once | 487.0 | 27.3 | -94.4% (-101.4 to -87.4) | -90.1% (-112.9 to -67.2) | -73.2% (-81.2 to -65.2) | **confirmed better** |
| consumer lag, mean messages waiting | 42.1 | 2.1 | -95.0% (-106.8 to -83.2) | -94.8% (-103.2 to -86.3) | -91.7% (-96.7 to -86.8) | **confirmed better** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 5.83 | +191.7% (+190.2 to +193.2) | +184.4% (+121.2 to +247.5) | +158.3% (+149.8 to +166.9) | **confirmed WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% (+300.0 to +300.0) | +300.0% (+300.0 to +300.0) | +300.0% (+300.0 to +300.0) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.296 | 0.324 | +9.4% (-10.6 to +29.4) | +4.2% (-3.8 to +12.2) | +2.3% (-3.0 to +7.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 351.8 | 383.5 | +9.0% (-9.8 to +27.8) | +4.0% (-3.9 to +11.9) | +2.2% (-3.0 to +7.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.9 | 7.41 | -6.1% (-23.2 to +10.9) | -10.1% (-17.4 to -2.9) | -11.7% (-16.5 to -6.9) | no difference beyond the noise (1 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 18.0 | +800.0% (+369.7 to +1230.3) | +800.0% (+369.7 to +1230.3) | +700.0% (+700.0 to +700.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,929, 1,952, 1,937 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 732.4 | 847.8 | +15.8% (+15.2 to +16.3) | +16.4% (+15.9 to +17.0) | +16.2% (+15.2 to +17.3) | **confirmed better** |
| throughput (messages a second consumed) | 848.2 | 848.2 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to -0.0) | no difference beyond the noise (1 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 1,581 | 9.32 | -99.4% (-102.4 to -96.5) | -99.5% (-104.3 to -94.7) | -99.4% (-107.4 to -91.4) | **confirmed better** |
| end-to-end latency, 99th percentile (ms) | 2,440 | 10.7 | -99.6% (-105.5 to -93.7) | -99.6% (-107.5 to -91.7) | -99.6% (-112.2 to -87.0) | **confirmed better** |
| end-to-end latency, median (ms) | 8.36 | 6.03 | -27.9% (-28.1 to -27.7) | -20.1% (-21.4 to -18.7) | -27.1% (-28.3 to -25.8) | **confirmed better** |
| end-to-end latency, mean (ms) | 218.3 | 6.79 | -96.9% (-101.9 to -91.9) | -97.2% (-102.5 to -91.9) | -97.1% (-108.6 to -85.6) | **confirmed better** |
| consumer lag, most messages waiting at once | 2,189 | 128.3 | -94.1% (-95.9 to -92.4) | -94.3% (-101.1 to -87.4) | -96.0% (-103.8 to -88.2) | **confirmed better** |
| consumer lag, mean messages waiting | 190.9 | 5.9 | -96.9% (-100.0 to -93.8) | -97.3% (-102.3 to -92.2) | -97.1% (-109.1 to -85.1) | **confirmed better** |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| consumers running, mean (the resources held) | 2 | 7.93 | +296.5% (+296.5 to +296.5) | +285.9% (+269.2 to +302.6) | +255.0% (+158.5 to +351.4) | **confirmed WORSE** |
| consumers running, most at once | 2 | 8 | +300.0% (+300.0 to +300.0) | +300.0% (+300.0 to +300.0) | +300.0% (+300.0 to +300.0) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.34 | 0.405 | +19.2% (+15.1 to +23.2) | +10.4% (+7.4 to +13.4) | +16.0% (+8.5 to +23.5) | **confirmed WORSE** |
| host CPU-seconds | 389.8 | 465.8 | +19.5% (+15.3 to +23.7) | +10.3% (+7.0 to +13.5) | +16.5% (+8.6 to +24.4) | **confirmed WORSE** |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.83 | +3.2% (-0.3 to +6.8) | -5.3% (-7.9 to -2.6) | +0.3% (-7.0 to +7.5) | no difference beyond the noise (2 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 16.0 | +700.0% (+700.0 to +700.0) | +700.0% (+700.0 to +700.0) | +700.0% (+700.0 to +700.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 21 gauge-rows confirmed better, 8 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
