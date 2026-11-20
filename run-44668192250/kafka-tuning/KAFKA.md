# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 430 | +16.9% | 60.9 to 63.4 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0163 to 0.0113 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,254 | 9.28 | -99.6% | -2,310 to -2,179 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,621 | 12.7 | -99.6% | -3,790 to -3,427 | GAIN |
| end-to-end latency, median (ms) | 8.04 | 6.64 | -17.4% | -1.9 to -0.893 | GAIN |
| end-to-end latency, mean (ms) | 301 | 7.17 | -97.6% | -302 to -285 | GAIN |
| consumer lag, most messages waiting at once | 1,645 | 45.7 | -97.2% | -1,689 to -1,510 | GAIN |
| consumer lag, mean messages waiting | 133 | 3.22 | -97.6% | -132 to -128 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.77 | +188.4% | 1.91 to 5.63 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.283 | 0.298 | +5.1% | -0.00428 to 0.0333 | STEADY, no difference beyond the noise |
| host CPU-seconds | 505 | 530 | +4.9% | -8 to 57.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.05 | 2.74 | -10.3% | -0.487 to -0.139 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
