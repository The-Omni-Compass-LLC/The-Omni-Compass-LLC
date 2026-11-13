# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 973 messages a second; base rate 146.0/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 365 | -0.1% | -0.702 to 0.143 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00599 to 0.00239 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,346 | 2,344 | -0.1% | -153 to 150 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,634 | 3,640 | +0.2% | -75.5 to 87.4 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.71 | 8.67 | -0.5% | -0.28 to 0.193 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 310 | 309 | -0.2% | -13.4 to 12.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,678 | +0.5% | -92.2 to 109 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 136 | 136 | -0.2% | -6.31 to 5.87 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.0% | -0.423 to 0.662 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.328 | 0.321 | -2.0% | -0.0396 to 0.0264 | EVEN, no difference beyond the noise |
| host CPU-seconds | 568 | 558 | -1.8% | -70.6 to 50.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.45 | 3.39 | -1.7% | -0.429 to 0.312 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
