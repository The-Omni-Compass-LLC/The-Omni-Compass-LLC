# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.3 to 25.9 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00122 to 0.000835 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,537 | 12.6 | -99.5% | -2,607 to -2,443 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,933 | 28.3 | -99.3% | -4,039 to -3,770 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.3% | -0.349 to -0.194 | GAIN |
| end-to-end latency, mean (ms) | 342 | 14.6 | -95.7% | -329 to -325 | GAIN |
| consumer lag, most messages waiting at once | 726 | 139 | -80.8% | -721 to -452 | GAIN |
| consumer lag, mean messages waiting | 62.7 | 2.73 | -95.6% | -60.5 to -59.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.02 | +150.9% | -0.238 to 6.27 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.289 | 0.296 | +2.6% | -0.00355 to 0.0188 | STEADY, no difference beyond the noise |
| host CPU-seconds | 510 | 523 | +2.5% | -6.26 to 31.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.69 | 6.72 | -12.7% | -1.25 to -0.698 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
