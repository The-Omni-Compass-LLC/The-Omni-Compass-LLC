# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 421 | +23.2% | 77.1 to 81.5 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.1% | -1.26 to 2.03 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,606 | 11.1 | -99.6% | -2,775 to -2,414 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,850 | 32.5 | -99.2% | -4,396 to -3,239 | GAIN |
| end-to-end latency, median (ms) | 9.31 | 7.93 | -14.8% | -1.5 to -1.24 | GAIN |
| end-to-end latency, mean (ms) | 395 | 8.32 | -97.9% | -392 to -381 | GAIN |
| consumer lag, most messages waiting at once | 1,725 | 59.3 | -96.6% | -1,844 to -1,488 | GAIN |
| consumer lag, mean messages waiting | 172 | 3.55 | -97.9% | -171 to -166 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.3 | +215.1% | 3.09 to 5.52 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.306 | 0.329 | +7.4% | 0.00507 to 0.0405 | power given |
| host CPU-seconds | 216 | 232 | +7.3% | 3.89 to 27.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.5 | 3.05 | -12.8% | -0.63 to -0.269 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
