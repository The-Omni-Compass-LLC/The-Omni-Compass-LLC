# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.3/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.7% | 25.3 to 27 | GAIN |
| throughput (messages a second consumed) | 174 | 174 | +0.0% | -0.00105 to 0.00108 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,654 | 12.6 | -99.5% | -2,708 to -2,574 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,051 | 30.4 | -99.2% | -4,176 to -3,866 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.4% | -0.429 to -0.126 | GAIN |
| end-to-end latency, mean (ms) | 358 | 12.8 | -96.4% | -359 to -333 | GAIN |
| consumer lag, most messages waiting at once | 740 | 70.7 | -90.5% | -810 to -528 | GAIN |
| consumer lag, mean messages waiting | 65.9 | 2.41 | -96.3% | -66.9 to -60 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.22 | +161.0% | 0.825 to 5.61 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.296 | 0.303 | +2.4% | -0.00522 to 0.0197 | STEADY, no difference beyond the noise |
| host CPU-seconds | 523 | 535 | +2.3% | -10 to 34.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.88 | 6.85 | -13.1% | -1.33 to -0.738 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
