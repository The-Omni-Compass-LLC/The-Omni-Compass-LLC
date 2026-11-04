# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.7% | 25.9 to 26.1 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00872 to 0.00371 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,509 | 12.5 | -99.5% | -2,599 to -2,394 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,037 | 14.1 | -99.7% | -4,326 to -3,721 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.4 | -1.8% | -0.363 to -0.0436 | GAIN |
| end-to-end latency, mean (ms) | 342 | 11.2 | -96.7% | -334 to -327 | GAIN |
| consumer lag, most messages waiting at once | 723 | 36.7 | -94.9% | -706 to -666 | GAIN |
| consumer lag, mean messages waiting | 62.5 | 1.98 | -96.8% | -60.7 to -60.3 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.58 | +228.9% | 4.56 to 4.6 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.299 | 0.308 | +3.0% | -0.000185 to 0.0181 | STEADY, no difference beyond the noise |
| host CPU-seconds | 538 | 553 | +2.8% | -0.704 to 30.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 8.11 | 7.09 | -12.7% | -1.26 to -0.794 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
