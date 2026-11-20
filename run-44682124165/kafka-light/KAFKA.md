# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1952 messages a second; base rate 292.9/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 858 | +17.4% | 119 to 136 | GAIN |
| throughput (messages a second consumed) | 859 | 859 | -0.0% | -0.0279 to 0.0229 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,571 | 8.84 | -99.7% | -2,798 to -2,326 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,904 | 25.6 | -99.3% | -4,092 to -3,663 | GAIN |
| end-to-end latency, median (ms) | 7.35 | 5.81 | -21.0% | -1.79 to -1.3 | GAIN |
| end-to-end latency, mean (ms) | 339 | 9.05 | -97.3% | -369 to -291 | GAIN |
| consumer lag, most messages waiting at once | 3,457 | 647 | -81.3% | -4,686 to -934 | GAIN |
| consumer lag, mean messages waiting | 296 | 8.41 | -97.2% | -323 to -253 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.03 | +201.4% | 3.3 to 4.76 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.323 | 0.356 | +10.1% | 0.0312 to 0.0342 | power given |
| host CPU-seconds | 574 | 630 | +9.8% | 55.1 to 57.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.63 | -6.5% | -0.13 to -0.0986 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
