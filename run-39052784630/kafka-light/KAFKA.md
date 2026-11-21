# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 727 | -0.2% | -1.96 to -0.658 | LOSS |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.015 to 0.00602 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,270 | 2,263 | -0.3% | -165 to 149 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,579 | 3,693 | +3.2% | 78.7 to 149 | LOSS |
| end-to-end latency, median (ms) | 7.61 | 7.6 | -0.2% | -0.214 to 0.182 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 302 | 306 | +1.1% | -3.33 to 9.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,250 | +1.6% | 11 to 91 | LOSS |
| consumer lag, mean messages waiting | 263 | 265 | +0.8% | -2.73 to 6.82 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.1% | -0.433 to 0.678 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.339 | 0.337 | -0.6% | -0.0147 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 602 | 598 | -0.6% | -25.9 to 18.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.83 | -0.4% | -0.0775 to 0.0617 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
