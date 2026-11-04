# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 421 | +23.3% | 77.1 to 81.7 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.1% | -1.29 to 2.06 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,582 | 11.1 | -99.6% | -2,701 to -2,441 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,971 | 44.4 | -98.9% | -4,267 to -3,587 | GAIN |
| end-to-end latency, median (ms) | 9.35 | 7.95 | -15.1% | -2.14 to -0.683 | GAIN |
| end-to-end latency, mean (ms) | 395 | 8.61 | -97.8% | -389 to -385 | GAIN |
| consumer lag, most messages waiting at once | 1,731 | 88.3 | -94.9% | -1,864 to -1,421 | GAIN |
| consumer lag, mean messages waiting | 171 | 3.93 | -97.7% | -167 to -167 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.31 | +165.3% | 2.42 to 4.19 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.305 | 0.326 | +6.8% | 0.00439 to 0.0371 | power given |
| host CPU-seconds | 215 | 229 | +6.6% | 3.44 to 25.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.02 | -13.4% | -0.656 to -0.279 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 59.0/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 172 | +17.5% | 25.1 to 26.1 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00205 to 0.000368 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,552 | 13.1 | -99.5% | -2,759 to -2,319 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,739 | 17.3 | -99.5% | -3,816 to -3,627 | GAIN |
| end-to-end latency, median (ms) | 11.7 | 11.5 | -1.3% | -0.337 to 0.0385 | STEADY, no difference beyond the noise |
| end-to-end latency, mean (ms) | 335 | 13.7 | -95.9% | -338 to -303 | GAIN |
| consumer lag, most messages waiting at once | 705 | 118 | -83.2% | -671 to -502 | GAIN |
| consumer lag, mean messages waiting | 61.4 | 2.5 | -95.9% | -62.4 to -55.3 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.56 | +77.9% | 1.03 to 2.08 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.303 | 0.312 | +3.0% | -0.00827 to 0.0263 | STEADY, no difference beyond the noise |
| host CPU-seconds | 544 | 558 | +2.7% | -14.7 to 43.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 8.22 | 7.18 | -12.6% | -1.41 to -0.665 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1928 messages a second; base rate 289.2/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 847 | +16.8% | 120 to 124 | GAIN |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.0279 to 0.00333 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,270 | 9.56 | -99.6% | -2,332 to -2,189 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,593 | 11.3 | -99.7% | -3,597 to -3,566 | GAIN |
| end-to-end latency, median (ms) | 7.7 | 6.17 | -19.8% | -1.58 to -1.48 | GAIN |
| end-to-end latency, mean (ms) | 298 | 7.47 | -97.5% | -298 to -282 | GAIN |
| consumer lag, most messages waiting at once | 3,224 | 256 | -92.0% | -3,146 to -2,788 | GAIN |
| consumer lag, mean messages waiting | 257 | 6.63 | -97.4% | -258 to -242 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.1 | +155.2% | 2.52 to 3.69 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.371 | 0.417 | +12.4% | 0.0216 to 0.0706 | power given |
| host CPU-seconds | 661 | 737 | +11.6% | 33.4 to 120 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.02 | 1.93 | -4.5% | -0.207 to 0.0258 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 147.0/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 431 | +17.3% | 60.6 to 66.3 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00738 to 0.00734 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,454 | 9.98 | -99.6% | -2,536 to -2,353 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,775 | 17.4 | -99.5% | -3,880 to -3,635 | GAIN |
| end-to-end latency, median (ms) | 8.2 | 7.07 | -13.7% | -1.33 to -0.925 | GAIN |
| end-to-end latency, mean (ms) | 325 | 9.21 | -97.2% | -332 to -299 | GAIN |
| consumer lag, most messages waiting at once | 1,725 | 220 | -87.2% | -2,013 to -996 | GAIN |
| consumer lag, mean messages waiting | 144 | 4.19 | -97.1% | -146 to -133 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.91 | +145.6% | 1.41 to 4.41 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.299 | 0.315 | +5.2% | 0.00859 to 0.0223 | power given |
| host CPU-seconds | 532 | 559 | +5.1% | 13.9 to 40 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 2.89 | -10.4% | -0.394 to -0.277 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
