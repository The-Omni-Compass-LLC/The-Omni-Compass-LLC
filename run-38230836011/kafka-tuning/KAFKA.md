# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 370 | 369 | -0.1% | -2.86 to 2.12 | no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00943 to 0.00846 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,663 | 1,658 | -0.3% | -85.3 to 75 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,600 | 2,534 | -2.5% | -127 to -4.6 | better |
| end-to-end latency, median (ms) | 8.51 | 8.47 | -0.4% | -0.118 to 0.0435 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 226 | 227 | +0.4% | -2.3 to 3.95 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,168 | 1,143 | -2.2% | -72.4 to 21.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 101 | 101 | +0.1% | -1.44 to 1.63 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.24 | +11.8% | -0.293 to 0.766 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.31 | 0.308 | -0.6% | -0.0129 to 0.00911 | no difference beyond the noise |
| host CPU-seconds | 359 | 358 | -0.4% | -15.8 to 12.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.23 | -0.3% | -0.147 to 0.127 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
