# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.1/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 853 | +17.5% | 126 to 128 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.0101 to 0.00392 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,478 | 9.24 | -99.6% | -2,531 to -2,407 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,932 | 13 | -99.7% | -4,000 to -3,838 | GAIN |
| end-to-end latency, median (ms) | 7.88 | 6.09 | -22.7% | -2.4 to -1.18 | GAIN |
| end-to-end latency, mean (ms) | 337 | 6.94 | -97.9% | -336 to -324 | GAIN |
| consumer lag, most messages waiting at once | 3,442 | 122 | -96.5% | -3,620 to -3,020 | GAIN |
| consumer lag, mean messages waiting | 293 | 6.17 | -97.9% | -291 to -283 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.43 | +171.5% | 2.98 to 3.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.345 | 0.392 | +13.6% | 0.0277 to 0.066 | power given |
| host CPU-seconds | 600 | 682 | +13.7% | 48.6 to 116 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.78 | -3.2% | -0.16 to 0.0415 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
