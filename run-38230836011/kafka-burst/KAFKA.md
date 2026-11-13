# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 347 | 347 | -0.2% | -3.12 to 1.41 | no difference beyond the noise |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0262 to 0.0505 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,695 | 1,685 | -0.6% | -107 to 87.6 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,534 | 2,539 | +0.2% | -321 to 331 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.82 | 8.77 | -0.6% | -0.167 to 0.0604 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 260 | 264 | +1.4% | -1.44 to 8.65 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,123 | 1,119 | -0.4% | -59.5 to 50.8 | no difference beyond the noise |
| consumer lag, mean messages waiting | 114 | 115 | +0.8% | -5.75 to 7.6 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -1.2% | -0.0248 to -0.0248 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.312 | 0.306 | -2.0% | -0.0305 to 0.0182 | no difference beyond the noise |
| host CPU-seconds | 149 | 146 | -2.0% | -14.6 to 8.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.56 | 3.5 | -1.7% | -0.363 to 0.238 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
