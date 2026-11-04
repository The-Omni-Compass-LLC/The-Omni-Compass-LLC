# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 419 | +22.5% | 71.9 to 82 | GAIN |
| throughput (messages a second consumed) | 421 | 422 | +0.3% | 1.16 to 1.17 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,654 | 11.4 | -99.6% | -2,830 to -2,456 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,911 | 494 | -87.4% | -4,532 to -2,301 | GAIN |
| end-to-end latency, median (ms) | 9.49 | 8.06 | -15.0% | -2.23 to -0.627 | GAIN |
| end-to-end latency, mean (ms) | 399 | 21.9 | -94.5% | -399 to -355 | GAIN |
| consumer lag, most messages waiting at once | 1,717 | 460 | -73.2% | -2,115 to -400 | GAIN |
| consumer lag, mean messages waiting | 173 | 9.36 | -94.6% | -172 to -155 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.28 | +163.8% | 1.45 to 5.1 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.308 | 0.332 | +8.0% | -0.00522 to 0.0542 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 233 | +7.5% | -4.32 to 37 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.51 | 3.09 | -12.0% | -0.733 to -0.108 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 392 messages a second; base rate 58.8/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +16.8% | 23.8 to 25.6 | GAIN |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00188 to 0.00137 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,348 | 12.8 | -99.5% | -2,471 to -2,198 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,574 | 69.4 | -98.1% | -3,641 to -3,368 | GAIN |
| end-to-end latency, median (ms) | 11.3 | 11.1 | -1.3% | -0.239 to -0.0479 | GAIN |
| end-to-end latency, mean (ms) | 309 | 16.1 | -94.8% | -309 to -277 | GAIN |
| consumer lag, most messages waiting at once | 668 | 174 | -73.9% | -607 to -380 | GAIN |
| consumer lag, mean messages waiting | 56.6 | 3.09 | -94.5% | -57.3 to -49.8 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.77 | +88.6% | 0.947 to 2.6 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.276 | 0.282 | +2.2% | 0.00232 to 0.00964 | power given |
| host CPU-seconds | 493 | 503 | +2.1% | 3.8 to 16.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.44 | 6.5 | -12.6% | -1.01 to -0.865 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 852 | +17.3% | 124 to 127 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0348 to 0.0104 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,413 | 9.28 | -99.6% | -2,538 to -2,270 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,846 | 11.1 | -99.7% | -4,016 to -3,653 | GAIN |
| end-to-end latency, median (ms) | 7.83 | 6.16 | -21.3% | -1.74 to -1.59 | GAIN |
| end-to-end latency, mean (ms) | 325 | 6.75 | -97.9% | -324 to -312 | GAIN |
| consumer lag, most messages waiting at once | 3,350 | 87.7 | -97.4% | -3,328 to -3,196 | GAIN |
| consumer lag, mean messages waiting | 283 | 5.82 | -97.9% | -281 to -273 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.52 | +175.9% | 2.73 to 4.31 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.342 | 0.389 | +13.6% | 0.0395 to 0.0538 | power given |
| host CPU-seconds | 594 | 677 | +14.0% | 70.7 to 95.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.76 | -2.9% | -0.0936 to -0.00989 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 429 | +17.2% | 61.7 to 64.5 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0123 to 0.0113 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,420 | 10.3 | -99.6% | -2,462 to -2,357 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,754 | 13.1 | -99.7% | -3,845 to -3,638 | GAIN |
| end-to-end latency, median (ms) | 8.49 | 7.39 | -13.0% | -1.3 to -0.909 | GAIN |
| end-to-end latency, mean (ms) | 323 | 8.38 | -97.4% | -322 to -307 | GAIN |
| consumer lag, most messages waiting at once | 1,694 | 105 | -93.8% | -1,971 to -1,208 | GAIN |
| consumer lag, mean messages waiting | 143 | 3.75 | -97.4% | -142 to -136 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.8 | +189.8% | 1.71 to 5.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.318 | 0.338 | +6.3% | 0.0157 to 0.0244 | power given |
| host CPU-seconds | 557 | 593 | +6.4% | 27 to 44.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.07 | -9.2% | -0.373 to -0.252 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
