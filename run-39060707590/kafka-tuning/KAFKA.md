# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 972 messages a second; base rate 145.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -2.27 to 1.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 428 | 428 | -0.0% | -0.00556 to 0.00334 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,258 | 2,285 | +1.2% | -174 to 228 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,628 | 3,569 | -1.6% | -318 to 200 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.53 | 8.52 | -0.2% | -0.1 to 0.0737 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 306 | 304 | -0.5% | -30.3 to 27.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,653 | 1,638 | -0.9% | -75.9 to 45.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 135 | 135 | -0.5% | -12.8 to 11.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.305 | 0.304 | -0.4% | -0.0137 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 531 | 529 | -0.2% | -26 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.22 | -0.2% | -0.141 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
