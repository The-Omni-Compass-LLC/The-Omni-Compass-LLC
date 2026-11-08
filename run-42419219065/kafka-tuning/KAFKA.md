# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.3/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 432 | +17.1% | 61.7 to 64.6 | GAIN |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.0035 to 0.002 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,335 | 8.75 | -99.6% | -2,508 to -2,145 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,689 | 10.7 | -99.7% | -3,863 to -3,493 | GAIN |
| end-to-end latency, median (ms) | 7.97 | 6.47 | -18.8% | -1.69 to -1.31 | GAIN |
| end-to-end latency, mean (ms) | 314 | 6.9 | -97.8% | -322 to -292 | GAIN |
| consumer lag, most messages waiting at once | 1,676 | 27.3 | -98.4% | -1,739 to -1,559 | GAIN |
| consumer lag, mean messages waiting | 140 | 3.04 | -97.8% | -144 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.22 | +161.0% | 2.76 to 3.68 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.27 | 0.284 | +5.4% | 0.00602 to 0.0232 | power given |
| host CPU-seconds | 481 | 506 | +5.3% | 11 to 39.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.9 | 2.6 | -10.1% | -0.384 to -0.203 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
