# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 420 | +22.9% | 77.5 to 79 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.3% | 1.15 to 1.16 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,490 | 10.6 | -99.6% | -2,589 to -2,370 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,496 | 24.7 | -99.3% | -3,746 to -3,197 | GAIN |
| end-to-end latency, median (ms) | 8.45 | 7.57 | -10.4% | -1.02 to -0.728 | GAIN |
| end-to-end latency, mean (ms) | 365 | 7.7 | -97.9% | -358 to -358 | GAIN |
| consumer lag, most messages waiting at once | 1,608 | 14.3 | -99.1% | -1,618 to -1,570 | GAIN |
| consumer lag, mean messages waiting | 158 | 3.15 | -98.0% | -156 to -153 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.04 | +152.2% | 1.45 to 4.64 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.286 | 0.302 | +5.5% | 0.00957 to 0.0218 | power given |
| host CPU-seconds | 204 | 215 | +5.0% | 5.76 to 14.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 2.84 | -14.3% | -0.548 to -0.398 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
