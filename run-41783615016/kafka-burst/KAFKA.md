# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 421 | +23.3% | 77.1 to 81.7 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.1% | -1.29 to 2.06 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,582 | 11.1 | -99.6% | -2,701 to -2,441 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,971 | 44.4 | -98.9% | -4,267 to -3,587 | GAIN |
| end-to-end latency, median (ms) | 9.35 | 7.95 | -15.1% | -2.14 to -0.683 | GAIN |
| end-to-end latency, mean (ms) | 395 | 8.61 | -97.8% | -389 to -385 | GAIN |
| consumer lag, most messages waiting at once | 1,731 | 88.3 | -94.9% | -1,864 to -1,421 | GAIN |
| consumer lag, mean messages waiting | 171 | 3.93 | -97.7% | -167 to -167 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.31 | +165.3% | 2.42 to 4.19 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.305 | 0.326 | +6.8% | 0.00439 to 0.0371 | power given |
| host CPU-seconds | 215 | 229 | +6.6% | 3.44 to 25.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 3.02 | -13.4% | -0.656 to -0.279 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
