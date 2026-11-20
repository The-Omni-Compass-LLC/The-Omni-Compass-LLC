# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.2% | 61.3 to 65.1 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00671 to -0.000368 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,365 | 9.54 | -99.6% | -2,424 to -2,287 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,704 | 11.1 | -99.7% | -3,986 to -3,401 | GAIN |
| end-to-end latency, median (ms) | 8.07 | 6.91 | -14.4% | -1.93 to -0.404 | GAIN |
| end-to-end latency, mean (ms) | 318 | 7.43 | -97.7% | -327 to -295 | GAIN |
| consumer lag, most messages waiting at once | 1,679 | 105 | -93.7% | -2,030 to -1,118 | GAIN |
| consumer lag, mean messages waiting | 141 | 3.32 | -97.7% | -146 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.3% | 1.48 to 4.57 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.279 | 0.309 | +10.8% | 0.000657 to 0.0598 | power given |
| host CPU-seconds | 497 | 550 | +10.6% | 0.37 to 105 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3 | 2.83 | -5.6% | -0.462 to 0.123 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
