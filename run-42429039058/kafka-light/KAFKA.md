# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 856 | +16.7% | 119 to 126 | GAIN |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0102 to 0.0073 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,222 | 8.16 | -99.6% | -2,454 to -1,973 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,423 | 9.8 | -99.7% | -3,619 to -3,207 | GAIN |
| end-to-end latency, median (ms) | 7.66 | 5.33 | -30.4% | -3.33 to -1.33 | GAIN |
| end-to-end latency, mean (ms) | 296 | 5.71 | -98.1% | -312 to -269 | GAIN |
| consumer lag, most messages waiting at once | 3,166 | 42 | -98.7% | -3,241 to -3,006 | GAIN |
| consumer lag, mean messages waiting | 259 | 5.02 | -98.1% | -272 to -237 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.72 | +185.9% | 2.86 to 4.58 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.287 | 0.313 | +8.8% | 0.0224 to 0.0284 | power given |
| host CPU-seconds | 512 | 556 | +8.6% | 38.8 to 49.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.55 | 1.44 | -6.9% | -0.116 to -0.0983 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
