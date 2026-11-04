# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.2/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 854 | +17.3% | 123 to 129 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.0203 to -0.0105 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,433 | 9.42 | -99.6% | -2,567 to -2,280 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,853 | 10.9 | -99.7% | -3,947 to -3,737 | GAIN |
| end-to-end latency, median (ms) | 7.47 | 6.15 | -17.7% | -1.94 to -0.707 | GAIN |
| end-to-end latency, mean (ms) | 321 | 6.28 | -98.0% | -327 to -302 | GAIN |
| consumer lag, most messages waiting at once | 3,373 | 48.3 | -98.6% | -3,403 to -3,246 | GAIN |
| consumer lag, mean messages waiting | 278 | 5.62 | -98.0% | -283 to -262 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.12 | +156.0% | 3.1 to 3.14 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.355 | 0.398 | +12.1% | 0.0271 to 0.0587 | power given |
| host CPU-seconds | 636 | 706 | +11.0% | 40.8 to 99.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.94 | 1.84 | -5.3% | -0.201 to -0.00486 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
