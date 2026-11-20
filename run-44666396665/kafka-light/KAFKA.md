# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1943 messages a second; base rate 291.4/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 854 | +17.1% | 122 to 127 | GAIN |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.0231 to 0.0028 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,387 | 8.76 | -99.6% | -2,549 to -2,208 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,631 | 10.3 | -99.7% | -3,895 to -3,347 | GAIN |
| end-to-end latency, median (ms) | 7.34 | 5.77 | -21.4% | -1.85 to -1.29 | GAIN |
| end-to-end latency, mean (ms) | 312 | 6.17 | -98.0% | -333 to -279 | GAIN |
| consumer lag, most messages waiting at once | 3,296 | 81.7 | -97.5% | -3,312 to -3,117 | GAIN |
| consumer lag, mean messages waiting | 271 | 5.5 | -98.0% | -288 to -242 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.97 | +148.3% | 2.11 to 3.82 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.323 | 0.357 | +10.3% | 0.0192 to 0.0474 | power given |
| host CPU-seconds | 574 | 632 | +10.1% | 33.4 to 82.3 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.64 | -6.0% | -0.155 to -0.0562 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
