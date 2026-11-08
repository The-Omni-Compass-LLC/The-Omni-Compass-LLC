# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 417 | +22.5% | 70 to 83.4 | GAIN |
| throughput (messages a second consumed) | 418 | 419 | +0.2% | -0.9 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,516 | 11.7 | -99.5% | -2,685 to -2,323 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,690 | 299 | -91.9% | -4,643 to -2,140 | GAIN |
| end-to-end latency, median (ms) | 9.16 | 8.14 | -11.1% | -1.28 to -0.763 | GAIN |
| end-to-end latency, mean (ms) | 378 | 16.2 | -95.7% | -393 to -331 | GAIN |
| consumer lag, most messages waiting at once | 1,651 | 291 | -82.4% | -2,174 to -545 | GAIN |
| consumer lag, mean messages waiting | 163 | 7.08 | -95.7% | -169 to -143 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.17 | +158.6% | 1.76 to 4.58 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.316 | 0.337 | +6.9% | 0.00479 to 0.0386 | power given |
| host CPU-seconds | 222 | 237 | +6.5% | 2.08 to 27 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.61 | 3.15 | -12.9% | -0.605 to -0.326 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
