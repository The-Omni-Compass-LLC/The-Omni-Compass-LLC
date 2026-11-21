# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.2% | -3.04 to 1.34 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | -0.0% | -0.0166 to 0.00955 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,281 | 2,282 | +0.0% | -112 to 113 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,655 | 3,647 | -0.2% | -476 to 458 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.74 | 8.6 | -1.6% | -0.362 to 0.0803 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 307 | 308 | +0.5% | -20.4 to 23.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,640 | 1,632 | -0.5% | -90.4 to 74.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 136 | +0.6% | -9.37 to 11 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.7% | -0.0773 to 0.107 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.327 | 0.316 | -3.4% | -0.0295 to 0.00694 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 549 | -3.5% | -53.6 to 14.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.46 | 3.35 | -3.2% | -0.337 to 0.113 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
