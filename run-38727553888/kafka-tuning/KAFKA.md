# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.2/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 367 | +0.1% | -1.24 to 2.25 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 431 | 431 | +0.0% | -0.529 to 0.845 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,490 | 2,477 | -0.6% | -157 to 130 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,908 | 3,782 | -3.2% | -254 to 3.28 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.16 | 8.11 | -0.5% | -0.0771 to -0.00491 | GAIN |
| end-to-end latency, mean (ms) | 330 | 327 | -0.9% | -23.1 to 17.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,745 | 1,725 | -1.1% | -93.8 to 54.5 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 146 | 145 | -0.5% | -10.1 to 8.56 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.296 | -0.2% | -0.00872 to 0.00726 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 530 | -0.1% | -16.3 to 14.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.21 | 3.2 | -0.2% | -0.12 to 0.104 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
