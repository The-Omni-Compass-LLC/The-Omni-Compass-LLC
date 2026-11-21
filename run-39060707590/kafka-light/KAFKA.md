# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1959 messages a second; base rate 293.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 732 | -0.2% | -2.61 to -0.00155 | LOSS |
| throughput (messages a second consumed) | 862 | 862 | -0.0% | -0.0452 to 0.0326 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,496 | 2,540 | +1.8% | -145 to 234 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,871 | 3,870 | -0.0% | -335 to 334 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9 | 11.5 | +28.2% | -13 to 18.1 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 343 | 347 | +1.2% | -7.22 to 15.3 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,468 | 3,476 | +0.2% | -244 to 262 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 302 | 306 | +1.5% | -6.88 to 15.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.292 | 0.292 | +0.2% | -0.0378 to 0.0391 | EVEN, no difference beyond the noise |
| host CPU-seconds | 520 | 522 | +0.4% | -63.3 to 67.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.58 | 1.58 | +0.5% | -0.19 to 0.208 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
