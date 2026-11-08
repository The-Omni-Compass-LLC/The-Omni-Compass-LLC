# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 420 | +23.2% | 74.8 to 83.2 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.893 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,547 | 10.8 | -99.6% | -2,759 to -2,313 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,832 | 65.2 | -98.3% | -4,180 to -3,355 | GAIN |
| end-to-end latency, median (ms) | 8.86 | 7.66 | -13.5% | -1.65 to -0.74 | GAIN |
| end-to-end latency, mean (ms) | 385 | 8.72 | -97.7% | -400 to -353 | GAIN |
| consumer lag, most messages waiting at once | 1,711 | 119 | -93.0% | -1,982 to -1,202 | GAIN |
| consumer lag, mean messages waiting | 166 | 4.18 | -97.5% | -172 to -153 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.92 | +146.0% | 2.31 to 3.53 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.289 | 0.307 | +6.2% | 0.00113 to 0.0349 | power given |
| host CPU-seconds | 207 | 219 | +5.9% | 0.961 to 23.3 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 2.89 | -13.9% | -0.6 to -0.332 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
