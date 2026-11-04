# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.1% | 61.9 to 64.2 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00588 to 0.0023 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,342 | 9.17 | -99.6% | -2,531 to -2,136 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,688 | 11.2 | -99.7% | -3,902 to -3,452 | GAIN |
| end-to-end latency, median (ms) | 8.1 | 6.8 | -16.0% | -1.93 to -0.655 | GAIN |
| end-to-end latency, mean (ms) | 315 | 6.95 | -97.8% | -322 to -293 | GAIN |
| consumer lag, most messages waiting at once | 1,686 | 25.3 | -98.5% | -1,731 to -1,591 | GAIN |
| consumer lag, mean messages waiting | 140 | 3.14 | -97.8% | -144 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.87 | +143.5% | 2.1 to 3.64 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.281 | 0.301 | +7.0% | -0.0169 to 0.0561 | STEADY, no difference beyond the noise |
| host CPU-seconds | 502 | 535 | +6.7% | -31.2 to 98.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.03 | 2.76 | -8.9% | -0.62 to 0.0794 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
