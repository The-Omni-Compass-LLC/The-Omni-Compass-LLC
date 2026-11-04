# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.2 to 25.9 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00279 to 0.000727 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 14.2 | -99.4% | -2,473 to -2,397 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,741 | 21.3 | -99.4% | -3,944 to -3,496 | GAIN |
| end-to-end latency, median (ms) | 11.7 | 11.5 | -2.0% | -0.388 to -0.0738 | GAIN |
| end-to-end latency, mean (ms) | 328 | 12.4 | -96.2% | -326 to -305 | GAIN |
| consumer lag, most messages waiting at once | 721 | 59 | -91.8% | -846 to -477 | GAIN |
| consumer lag, mean messages waiting | 60.6 | 2.22 | -96.3% | -60.2 to -56.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.58 | +79.2% | 0.624 to 2.54 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.298 | 0.305 | +2.2% | -0.00255 to 0.0157 | STEADY, no difference beyond the noise |
| host CPU-seconds | 527 | 538 | +2.1% | -4.68 to 27.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.96 | 6.92 | -13.0% | -1.3 to -0.762 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
