# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.8/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 856 | +17.4% | 126 to 127 | GAIN |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0371 to 0.019 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,486 | 8.96 | -99.6% | -2,556 to -2,398 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,860 | 10.3 | -99.7% | -4,130 to -3,570 | GAIN |
| end-to-end latency, median (ms) | 7.32 | 5.92 | -19.1% | -1.65 to -1.14 | GAIN |
| end-to-end latency, mean (ms) | 326 | 6.02 | -98.1% | -322 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,413 | 20.3 | -99.4% | -3,460 to -3,325 | GAIN |
| consumer lag, mean messages waiting | 283 | 5.25 | -98.1% | -279 to -276 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.2 | +160.1% | 3 to 3.41 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.346 | 0.379 | +9.4% | 0.0267 to 0.0384 | power given |
| host CPU-seconds | 621 | 674 | +8.5% | 39.5 to 66.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.89 | 1.75 | -7.5% | -0.183 to -0.102 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
