# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.7/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 418 | +22.6% | 67.5 to 86.4 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.903 to 2.44 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,602 | 11.6 | -99.6% | -2,623 to -2,558 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,795 | 352 | -90.7% | -4,478 to -2,407 | GAIN |
| end-to-end latency, median (ms) | 9.21 | 8.1 | -12.0% | -1.9 to -0.309 | GAIN |
| end-to-end latency, mean (ms) | 385 | 16.9 | -95.6% | -400 to -336 | GAIN |
| consumer lag, most messages waiting at once | 1,684 | 328 | -80.5% | -2,164 to -548 | GAIN |
| consumer lag, mean messages waiting | 166 | 7.43 | -95.5% | -173 to -144 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.3% | 2.15 to 3.9 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.313 | 0.333 | +6.4% | 0.00394 to 0.0365 | power given |
| host CPU-seconds | 221 | 234 | +6.1% | 1.31 to 25.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.58 | 3.11 | -13.2% | -0.695 to -0.252 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
