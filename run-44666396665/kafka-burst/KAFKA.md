# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.5/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 423 | +23.1% | 77.6 to 80.9 | GAIN |
| throughput (messages a second consumed) | 422 | 423 | +0.2% | -0.916 to 2.48 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,576 | 10.4 | -99.6% | -2,661 to -2,471 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,875 | 49 | -98.7% | -3,878 to -3,775 | GAIN |
| end-to-end latency, median (ms) | 9.36 | 7.36 | -21.4% | -3.64 to -0.362 | GAIN |
| end-to-end latency, mean (ms) | 392 | 8.08 | -97.9% | -387 to -381 | GAIN |
| consumer lag, most messages waiting at once | 1,695 | 38.3 | -97.7% | -1,710 to -1,603 | GAIN |
| consumer lag, mean messages waiting | 172 | 3.54 | -97.9% | -172 to -164 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.4 | +170.1% | 0.498 to 6.3 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.273 | 0.282 | +3.3% | -0.00449 to 0.0223 | STEADY, no difference beyond the noise |
| host CPU-seconds | 196 | 201 | +2.9% | -3.99 to 15.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.15 | 2.64 | -16.3% | -0.668 to -0.359 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
