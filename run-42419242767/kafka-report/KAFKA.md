# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 420 | +22.9% | 77.5 to 79 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.3% | 1.15 to 1.16 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,490 | 10.6 | -99.6% | -2,589 to -2,370 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,496 | 24.7 | -99.3% | -3,746 to -3,197 | GAIN |
| end-to-end latency, median (ms) | 8.45 | 7.57 | -10.4% | -1.02 to -0.728 | GAIN |
| end-to-end latency, mean (ms) | 365 | 7.7 | -97.9% | -358 to -358 | GAIN |
| consumer lag, most messages waiting at once | 1,608 | 14.3 | -99.1% | -1,618 to -1,570 | GAIN |
| consumer lag, mean messages waiting | 158 | 3.15 | -98.0% | -156 to -153 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.04 | +152.2% | 1.45 to 4.64 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.286 | 0.302 | +5.5% | 0.00957 to 0.0218 | power given |
| host CPU-seconds | 204 | 215 | +5.0% | 5.76 to 14.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 2.84 | -14.3% | -0.548 to -0.398 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.6% | 24.9 to 26.8 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00328 to 0.0021 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,569 | 12.6 | -99.5% | -2,678 to -2,434 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,893 | 43.2 | -98.9% | -4,009 to -3,690 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.4% | -0.301 to -0.265 | GAIN |
| end-to-end latency, mean (ms) | 345 | 13.4 | -96.1% | -353 to -311 | GAIN |
| consumer lag, most messages waiting at once | 715 | 99 | -86.2% | -739 to -493 | GAIN |
| consumer lag, mean messages waiting | 62.6 | 2.46 | -96.1% | -63.7 to -56.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.26 | +113.2% | 1.71 to 2.82 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.287 | 0.294 | +2.4% | -0.00128 to 0.0151 | STEADY, no difference beyond the noise |
| host CPU-seconds | 508 | 519 | +2.3% | -2.66 to 25.9 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.66 | 6.67 | -13.0% | -1.22 to -0.774 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 853 | +17.5% | 126 to 128 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.0101 to 0.00392 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,478 | 9.24 | -99.6% | -2,531 to -2,407 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,932 | 13 | -99.7% | -4,000 to -3,838 | GAIN |
| end-to-end latency, median (ms) | 7.88 | 6.09 | -22.7% | -2.4 to -1.18 | GAIN |
| end-to-end latency, mean (ms) | 337 | 6.94 | -97.9% | -336 to -324 | GAIN |
| consumer lag, most messages waiting at once | 3,442 | 122 | -96.5% | -3,620 to -3,020 | GAIN |
| consumer lag, mean messages waiting | 293 | 6.17 | -97.9% | -291 to -283 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.43 | +171.5% | 2.98 to 3.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.345 | 0.392 | +13.6% | 0.0277 to 0.066 | power given |
| host CPU-seconds | 600 | 682 | +13.7% | 48.6 to 116 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.78 | -3.2% | -0.16 to 0.0415 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 963 messages a second; base rate 144.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 364 | 424 | +16.4% | 32.3 to 87.4 | GAIN |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.0082 to 0.0058 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,413 | 9.03 | -99.6% | -5,158 to 350 | STEADY, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,822 | 13.4 | -99.6% | -7,362 to -255 | GAIN |
| end-to-end latency, median (ms) | 8.07 | 6.63 | -17.8% | -1.77 to -1.11 | GAIN |
| end-to-end latency, mean (ms) | 326 | 7.01 | -97.8% | -736 to 98 | STEADY, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 27.7 | -98.4% | -2,979 to -363 | GAIN |
| consumer lag, mean messages waiting | 142 | 3.06 | -97.8% | -315 to 37 | STEADY, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.89 | +194.5% | 3.07 to 4.71 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.282 | 0.296 | +5.0% | -0.00707 to 0.0355 | STEADY, no difference beyond the noise |
| host CPU-seconds | 503 | 527 | +4.9% | -12.1 to 61 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 2.76 | -10.0% | -0.556 to -0.0571 | GAIN |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
