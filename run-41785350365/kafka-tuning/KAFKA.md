# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 977 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 429 | +17.2% | 61.7 to 64.5 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0123 to 0.0113 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,420 | 10.3 | -99.6% | -2,462 to -2,357 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,754 | 13.1 | -99.7% | -3,845 to -3,638 | GAIN |
| end-to-end latency, median (ms) | 8.49 | 7.39 | -13.0% | -1.3 to -0.909 | GAIN |
| end-to-end latency, mean (ms) | 323 | 8.38 | -97.4% | -322 to -307 | GAIN |
| consumer lag, most messages waiting at once | 1,694 | 105 | -93.8% | -1,971 to -1,208 | GAIN |
| consumer lag, mean messages waiting | 143 | 3.75 | -97.4% | -142 to -136 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.8 | +189.8% | 1.71 to 5.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.318 | 0.338 | +6.3% | 0.0157 to 0.0244 | power given |
| host CPU-seconds | 557 | 593 | +6.4% | 27 to 44.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.07 | -9.2% | -0.373 to -0.252 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
