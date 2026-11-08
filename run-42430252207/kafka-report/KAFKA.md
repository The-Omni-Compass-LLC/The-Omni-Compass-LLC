# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 420 | +23.2% | 74.8 to 83.2 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.893 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,547 | 10.8 | -99.6% | -2,759 to -2,313 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,832 | 65.2 | -98.3% | -4,180 to -3,355 | GAIN |
| end-to-end latency, median (ms) | 8.86 | 7.66 | -13.5% | -1.65 to -0.74 | GAIN |
| end-to-end latency, mean (ms) | 385 | 8.72 | -97.7% | -400 to -353 | GAIN |
| consumer lag, most messages waiting at once | 1,711 | 119 | -93.0% | -1,982 to -1,202 | GAIN |
| consumer lag, mean messages waiting | 166 | 4.18 | -97.5% | -172 to -153 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.92 | +146.0% | 2.31 to 3.53 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.289 | 0.307 | +6.2% | 0.00113 to 0.0349 | power given |
| host CPU-seconds | 207 | 219 | +5.9% | 0.961 to 23.3 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 2.89 | -13.9% | -0.6 to -0.332 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.2% | 24.5 to 26.3 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.002 to 0.00211 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,440 | 11.9 | -99.5% | -2,577 to -2,279 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,711 | 15.8 | -99.6% | -3,933 to -3,459 | GAIN |
| end-to-end latency, median (ms) | 10.8 | 10.7 | -1.3% | -0.58 to 0.302 | STEADY, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 12.6 | -96.1% | -336 to -285 | GAIN |
| consumer lag, most messages waiting at once | 699 | 82.7 | -88.2% | -704 to -530 | GAIN |
| consumer lag, mean messages waiting | 59 | 2.21 | -96.2% | -61 to -52.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.11 | +105.6% | -0.359 to 4.58 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.262 | 0.268 | +2.4% | -0.0069 to 0.0195 | STEADY, no difference beyond the noise |
| host CPU-seconds | 468 | 479 | +2.3% | -12.5 to 34 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.05 | 6.15 | -12.7% | -1.31 to -0.482 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 851 | +17.4% | 120 to 132 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0254 to 0.0064 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,569 | 9.92 | -99.6% | -2,617 to -2,502 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,876 | 13.9 | -99.6% | -3,927 to -3,798 | GAIN |
| end-to-end latency, median (ms) | 8.14 | 6.42 | -21.1% | -2.13 to -1.3 | GAIN |
| end-to-end latency, mean (ms) | 339 | 9.36 | -97.2% | -342 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,425 | 413 | -87.9% | -4,638 to -1,386 | GAIN |
| consumer lag, mean messages waiting | 293 | 8.25 | -97.2% | -296 to -273 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.52 | +176.2% | 2.17 to 4.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.377 | 0.448 | +18.7% | 0.0591 to 0.082 | power given |
| host CPU-seconds | 655 | 780 | +19.0% | 104 to 145 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.01 | 2.04 | +1.4% | -0.0366 to 0.0933 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.0% | 61.7 to 63.4 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00674 to 0.0055 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,324 | 8.95 | -99.6% | -2,442 to -2,187 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,584 | 13.2 | -99.6% | -3,834 to -3,307 | GAIN |
| end-to-end latency, median (ms) | 8.08 | 6.56 | -18.8% | -1.63 to -1.41 | GAIN |
| end-to-end latency, mean (ms) | 309 | 7.19 | -97.7% | -306 to -297 | GAIN |
| consumer lag, most messages waiting at once | 1,658 | 84 | -94.9% | -1,790 to -1,358 | GAIN |
| consumer lag, mean messages waiting | 137 | 3.27 | -97.6% | -136 to -132 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.42 | +170.8% | 2.49 to 4.35 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.285 | 0.294 | +3.2% | -0.00445 to 0.023 | STEADY, no difference beyond the noise |
| host CPU-seconds | 508 | 524 | +3.1% | -8.94 to 40.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 2.7 | -11.9% | -0.515 to -0.215 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
