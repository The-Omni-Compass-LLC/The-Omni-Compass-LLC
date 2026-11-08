# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.3/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 432 | +17.5% | 63.1 to 65.5 | GAIN |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.00525 to 0.00313 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,477 | 9.13 | -99.6% | -2,570 to -2,365 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,895 | 11.8 | -99.7% | -4,142 to -3,625 | GAIN |
| end-to-end latency, median (ms) | 8.06 | 6.67 | -17.2% | -1.54 to -1.24 | GAIN |
| end-to-end latency, mean (ms) | 334 | 7.14 | -97.9% | -339 to -315 | GAIN |
| consumer lag, most messages waiting at once | 1,737 | 35.7 | -97.9% | -1,750 to -1,653 | GAIN |
| consumer lag, mean messages waiting | 149 | 3.1 | -97.9% | -149 to -143 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.27 | +163.3% | 2.79 to 3.74 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.278 | 0.299 | +7.6% | 0.0149 to 0.0271 | power given |
| host CPU-seconds | 496 | 532 | +7.4% | 24.7 to 48.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.99 | 2.74 | -8.6% | -0.301 to -0.213 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
