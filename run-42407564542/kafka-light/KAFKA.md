# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1923 messages a second; base rate 288.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 845 | +16.6% | 116 to 125 | GAIN |
| throughput (messages a second consumed) | 846 | 846 | -0.0% | -0.0326 to 0.0134 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,185 | 9.25 | -99.6% | -2,216 to -2,137 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,510 | 11.3 | -99.7% | -3,809 to -3,189 | GAIN |
| end-to-end latency, median (ms) | 7.83 | 6.08 | -22.3% | -2.03 to -1.47 | GAIN |
| end-to-end latency, mean (ms) | 290 | 7.9 | -97.3% | -295 to -268 | GAIN |
| consumer lag, most messages waiting at once | 3,131 | 194 | -93.8% | -3,491 to -2,382 | GAIN |
| consumer lag, mean messages waiting | 250 | 6.95 | -97.2% | -256 to -231 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.72 | +185.9% | 2.46 to 4.97 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.343 | 0.391 | +14.2% | 0.0401 to 0.0569 | power given |
| host CPU-seconds | 594 | 681 | +14.6% | 72.5 to 100 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.82 | 1.79 | -1.8% | -0.0798 to 0.0155 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
