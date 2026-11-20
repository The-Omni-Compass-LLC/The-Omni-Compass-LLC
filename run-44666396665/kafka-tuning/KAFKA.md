# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.8/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 430 | +17.6% | 62.6 to 66.1 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0117 to 0.00236 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,528 | 10.3 | -99.6% | -2,598 to -2,437 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,859 | 13.2 | -99.7% | -4,132 to -3,559 | GAIN |
| end-to-end latency, median (ms) | 8.51 | 7.38 | -13.3% | -1.32 to -0.935 | GAIN |
| end-to-end latency, mean (ms) | 337 | 8.11 | -97.6% | -343 to -316 | GAIN |
| consumer lag, most messages waiting at once | 1,764 | 109 | -93.8% | -1,894 to -1,416 | GAIN |
| consumer lag, mean messages waiting | 149 | 3.69 | -97.5% | -152 to -139 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.31 | +165.5% | 2.38 to 4.24 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.328 | 0.345 | +5.2% | 0.0065 to 0.0278 | power given |
| host CPU-seconds | 573 | 604 | +5.4% | 11.5 to 50.2 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.48 | 3.12 | -10.4% | -0.484 to -0.239 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
