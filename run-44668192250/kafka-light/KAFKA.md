# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 853 | +17.5% | 122 to 132 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0217 to 0.00131 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,503 | 9.18 | -99.6% | -2,703 to -2,285 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,795 | 10.8 | -99.7% | -4,202 to -3,367 | GAIN |
| end-to-end latency, median (ms) | 7.93 | 6.02 | -24.0% | -2.29 to -1.52 | GAIN |
| end-to-end latency, mean (ms) | 332 | 6.43 | -98.1% | -352 to -299 | GAIN |
| consumer lag, most messages waiting at once | 3,387 | 64.7 | -98.1% | -3,488 to -3,156 | GAIN |
| consumer lag, mean messages waiting | 289 | 5.65 | -98.0% | -302 to -264 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.79 | +189.7% | 2.61 to 4.98 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.351 | 0.401 | +14.1% | 0.031 to 0.0681 | power given |
| host CPU-seconds | 610 | 698 | +14.5% | 58.6 to 118 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.87 | 1.82 | -2.5% | -0.129 to 0.0347 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
