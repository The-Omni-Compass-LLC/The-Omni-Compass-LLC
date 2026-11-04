# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 980 messages a second; base rate 110.2/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 419 | +22.5% | 71.9 to 82 | GAIN |
| throughput (messages a second consumed) | 421 | 422 | +0.3% | 1.16 to 1.17 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,654 | 11.4 | -99.6% | -2,830 to -2,456 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,911 | 494 | -87.4% | -4,532 to -2,301 | GAIN |
| end-to-end latency, median (ms) | 9.49 | 8.06 | -15.0% | -2.23 to -0.627 | GAIN |
| end-to-end latency, mean (ms) | 399 | 21.9 | -94.5% | -399 to -355 | GAIN |
| consumer lag, most messages waiting at once | 1,717 | 460 | -73.2% | -2,115 to -400 | GAIN |
| consumer lag, mean messages waiting | 173 | 9.36 | -94.6% | -172 to -155 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.28 | +163.8% | 1.45 to 5.1 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.308 | 0.332 | +8.0% | -0.00522 to 0.0542 | STEADY, no difference beyond the noise |
| host CPU-seconds | 217 | 233 | +7.5% | -4.32 to 37 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.51 | 3.09 | -12.0% | -0.733 to -0.108 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
