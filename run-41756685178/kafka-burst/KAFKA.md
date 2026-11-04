# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 420 | +23.4% | 77.9 to 81.3 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.934 to 2.45 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,575 | 11.2 | -99.6% | -2,813 to -2,314 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,702 | 36.9 | -99.0% | -3,757 to -3,573 | GAIN |
| end-to-end latency, median (ms) | 9.26 | 8.05 | -13.1% | -1.95 to -0.468 | GAIN |
| end-to-end latency, mean (ms) | 388 | 8.89 | -97.7% | -409 to -350 | GAIN |
| consumer lag, most messages waiting at once | 1,685 | 54.7 | -96.8% | -1,809 to -1,451 | GAIN |
| consumer lag, mean messages waiting | 168 | 4.03 | -97.6% | -177 to -150 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.78 | +139.0% | 1.54 to 4.02 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.309 | 0.329 | +6.7% | 0.0079 to 0.0335 | power given |
| host CPU-seconds | 217 | 231 | +6.4% | 5.28 to 22.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.06 | -13.6% | -0.632 to -0.331 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
