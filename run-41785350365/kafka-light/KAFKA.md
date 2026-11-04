# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
