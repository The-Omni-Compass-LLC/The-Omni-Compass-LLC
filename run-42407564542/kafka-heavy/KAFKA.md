# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.6 to 25.8 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00108 to 0.00164 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,500 | 12.5 | -99.5% | -2,555 to -2,419 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,830 | 36.5 | -99.0% | -4,011 to -3,576 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.5% | -0.291 to -0.28 | GAIN |
| end-to-end latency, mean (ms) | 335 | 11.9 | -96.5% | -325 to -322 | GAIN |
| consumer lag, most messages waiting at once | 715 | 45 | -93.7% | -767 to -573 | GAIN |
| consumer lag, mean messages waiting | 61.2 | 2.08 | -96.6% | -60.9 to -57.3 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.75 | +137.5% | 2.51 to 2.99 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.288 | 0.296 | +2.8% | 0.00308 to 0.0132 | power given |
| host CPU-seconds | 509 | 523 | +2.7% | 4.83 to 22.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 7.67 | 6.71 | -12.5% | -1.13 to -0.797 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
