# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.6% | 25.5 to 26.4 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.000637 to 0.000169 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,563 | 12.6 | -99.5% | -2,758 to -2,343 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,926 | 22.9 | -99.4% | -4,074 to -3,732 | GAIN |
| end-to-end latency, median (ms) | 11.7 | 11.3 | -3.1% | -0.571 to -0.161 | GAIN |
| end-to-end latency, mean (ms) | 347 | 13.3 | -96.2% | -347 to -321 | GAIN |
| consumer lag, most messages waiting at once | 724 | 108 | -85.1% | -866 to -366 | GAIN |
| consumer lag, mean messages waiting | 63.4 | 2.36 | -96.3% | -65.6 to -56.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.01 | +150.4% | -0.389 to 6.4 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.299 | 0.302 | +0.9% | -0.00154 to 0.00676 | STEADY, no difference beyond the noise |
| host CPU-seconds | 529 | 533 | +0.7% | -3.47 to 11 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.99 | 6.84 | -14.4% | -1.24 to -1.06 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
