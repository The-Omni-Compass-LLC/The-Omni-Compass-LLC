# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 973 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -2 to -0.209 | LOSS |
| throughput (messages a second consumed) | 419 | 418 | -0.1% | -2.04 to 1.28 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,521 | 2,478 | -1.7% | -108 to 21.4 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,594 | 3,738 | +4.0% | 111 to 176 | LOSS |
| end-to-end latency, median (ms) | 9.41 | 9.63 | +2.4% | -0.582 to 1.04 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 378 | 380 | +0.6% | -1.45 to 5.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,619 | 1,630 | +0.7% | -94.2 to 116 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.4% | -0.464 to 1.62 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.298 | 0.292 | -1.9% | -0.0238 to 0.0126 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 204 | -1.8% | -16.4 to 8.99 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.33 | -1.6% | -0.246 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
