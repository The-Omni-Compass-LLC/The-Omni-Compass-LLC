# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 421 | +23.4% | 79.4 to 80.2 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.3% | 1.14 to 1.17 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,582 | 11 | -99.6% | -2,884 to -2,258 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,836 | 33.5 | -99.1% | -4,402 to -3,203 | GAIN |
| end-to-end latency, median (ms) | 9.28 | 7.94 | -14.4% | -2.5 to -0.177 | GAIN |
| end-to-end latency, mean (ms) | 392 | 8.43 | -97.8% | -391 to -375 | GAIN |
| consumer lag, most messages waiting at once | 1,713 | 87.7 | -94.9% | -1,837 to -1,414 | GAIN |
| consumer lag, mean messages waiting | 170 | 3.98 | -97.7% | -172 to -160 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.92 | +146.1% | 1.65 to 4.2 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.305 | 0.323 | +6.1% | 0.00218 to 0.035 | power given |
| host CPU-seconds | 214 | 227 | +5.8% | 0.459 to 24.2 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.48 | 2.99 | -14.0% | -0.676 to -0.3 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 391 messages a second; base rate 58.6/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +16.4% | 23.8 to 24.6 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00174 to 0.00101 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,115 | 11.7 | -99.4% | -2,206 to -2,000 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,285 | 15.4 | -99.5% | -3,479 to -3,061 | GAIN |
| end-to-end latency, median (ms) | 10.7 | 10.6 | -0.3% | -0.127 to 0.0547 | STEADY, no difference beyond the noise |
| end-to-end latency, mean (ms) | 277 | 11.5 | -95.8% | -270 to -261 | GAIN |
| consumer lag, most messages waiting at once | 646 | 62 | -90.4% | -721 to -448 | GAIN |
| consumer lag, mean messages waiting | 51.2 | 2.09 | -95.9% | -49.6 to -48.7 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.1 | +105.0% | -0.809 to 5.01 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.253 | 0.258 | +2.0% | 7.67e-05 to 0.00986 | power given |
| host CPU-seconds | 454 | 462 | +1.9% | -0.277 to 17.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.83 | 5.98 | -12.5% | -0.956 to -0.752 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 856 | +16.7% | 119 to 126 | GAIN |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0102 to 0.0073 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,222 | 8.16 | -99.6% | -2,454 to -1,973 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,423 | 9.8 | -99.7% | -3,619 to -3,207 | GAIN |
| end-to-end latency, median (ms) | 7.66 | 5.33 | -30.4% | -3.33 to -1.33 | GAIN |
| end-to-end latency, mean (ms) | 296 | 5.71 | -98.1% | -312 to -269 | GAIN |
| consumer lag, most messages waiting at once | 3,166 | 42 | -98.7% | -3,241 to -3,006 | GAIN |
| consumer lag, mean messages waiting | 259 | 5.02 | -98.1% | -272 to -237 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.72 | +185.9% | 2.86 to 4.58 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.287 | 0.313 | +8.8% | 0.0224 to 0.0284 | power given |
| host CPU-seconds | 512 | 556 | +8.6% | 38.8 to 49.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.44 | -6.9% | -0.116 to -0.0983 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 965 messages a second; base rate 144.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 364 | 424 | +16.7% | 50.1 to 71.2 | GAIN |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.00677 to 0.00473 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,158 | 9.79 | -99.5% | -3,000 to -1,296 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,376 | 23.9 | -99.3% | -4,247 to -2,458 | GAIN |
| end-to-end latency, median (ms) | 8.23 | 7.2 | -12.6% | -1.27 to -0.797 | GAIN |
| end-to-end latency, mean (ms) | 284 | 8.08 | -97.2% | -394 to -158 | GAIN |
| consumer lag, most messages waiting at once | 1,565 | 112 | -92.9% | -1,999 to -907 | GAIN |
| consumer lag, mean messages waiting | 124 | 3.56 | -97.1% | -170 to -71.7 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.95 | +147.5% | 1.44 to 4.46 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.297 | 0.311 | +4.7% | 0.0127 to 0.0151 | power given |
| host CPU-seconds | 528 | 552 | +4.6% | 22.6 to 25.5 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 2.89 | -10.4% | -0.434 to -0.238 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
