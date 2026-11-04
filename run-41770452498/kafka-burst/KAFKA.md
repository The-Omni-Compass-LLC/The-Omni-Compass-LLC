# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 420 | +23.1% | 78.2 to 79.4 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.3% | 1.15 to 1.18 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,484 | 11.2 | -99.5% | -2,515 to -2,431 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,715 | 61.2 | -98.4% | -3,907 to -3,402 | GAIN |
| end-to-end latency, median (ms) | 9.13 | 7.97 | -12.6% | -1.77 to -0.532 | GAIN |
| end-to-end latency, mean (ms) | 378 | 8.95 | -97.6% | -373 to -365 | GAIN |
| consumer lag, most messages waiting at once | 1,654 | 61.7 | -96.3% | -1,719 to -1,466 | GAIN |
| consumer lag, mean messages waiting | 164 | 3.84 | -97.7% | -161 to -159 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.19 | +159.7% | 1.51 to 4.88 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.304 | 0.324 | +6.6% | 0.00986 to 0.0303 | power given |
| host CPU-seconds | 214 | 227 | +6.3% | 6.15 to 20.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3 | -13.4% | -0.594 to -0.335 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
