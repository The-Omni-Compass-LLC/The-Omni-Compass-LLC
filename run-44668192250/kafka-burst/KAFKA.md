# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 422 | +23.1% | 78.2 to 80.4 | GAIN |
| throughput (messages a second consumed) | 422 | 422 | +0.1% | -1.3 to 2.07 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,651 | 12.1 | -99.5% | -2,898 to -2,379 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,020 | 51.8 | -98.7% | -4,381 to -3,556 | GAIN |
| end-to-end latency, median (ms) | 10.2 | 7.85 | -22.9% | -3.15 to -1.52 | GAIN |
| end-to-end latency, mean (ms) | 397 | 8.71 | -97.8% | -394 to -383 | GAIN |
| consumer lag, most messages waiting at once | 1,744 | 45.7 | -97.4% | -1,755 to -1,641 | GAIN |
| consumer lag, mean messages waiting | 173 | 3.96 | -97.7% | -173 to -166 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.24 | +161.9% | 1.67 to 4.81 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.316 | 0.315 | -0.3% | -0.0903 to 0.0884 | STEADY, no difference beyond the noise |
| host CPU-seconds | 225 | 223 | -1.1% | -59.2 to 54.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.64 | 2.93 | -19.6% | -1.51 to 0.0891 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
