# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 1932 messages a second; base rate 289.8/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 733 | 733 | +0.1% | -3.51 to 4.57 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | +0.0% | -0.0405 to 0.0673 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,565 | 1,557 | -0.5% | -81.4 to 65.9 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,418 | 2,429 | +0.5% | -162 to 185 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.37 | 7.76 | -7.2% | -0.833 to -0.373 | better |
| end-to-end latency, mean (ms) | 218 | 215 | -1.5% | -21.7 to 15.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,225 | 2,218 | -0.3% | -54.6 to 40.6 | no difference beyond the noise |
| consumer lag, mean messages waiting | 192 | 188 | -2.5% | -20.5 to 10.8 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.37 | +18.5% | 0.357 to 0.382 | **WORSE** |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | **WORSE** |
| host CPU busy (share of the run) | 0.333 | 0.335 | +0.7% | -0.0187 to 0.0234 | no difference beyond the noise |
| host CPU-seconds | 381 | 384 | +0.8% | -22.8 to 29.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.74 | +0.8% | -0.104 to 0.13 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
