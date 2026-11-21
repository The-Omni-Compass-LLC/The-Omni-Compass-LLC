# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -3.28 to 3.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00499 to -0.000929 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,474 | 2,448 | -1.1% | -355 to 301 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,904 | 3,908 | +0.1% | -418 to 427 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.59 | +0.5% | -0.369 to 0.459 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 336 | 333 | -0.9% | -45.8 to 39.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,745 | 1,730 | -0.8% | -203 to 174 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 149 | 147 | -1.2% | -19.6 to 16.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.318 | +3.4% | -0.036 to 0.057 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 554 | +3.8% | -62 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.36 | +3.7% | -0.407 to 0.648 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
