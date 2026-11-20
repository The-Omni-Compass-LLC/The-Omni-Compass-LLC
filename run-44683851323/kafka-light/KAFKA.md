# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1882 messages a second; base rate 282.3/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 743 | 827 | +11.3% | 82 to 86.2 | GAIN |
| throughput (messages a second consumed) | 828 | 828 | -0.0% | -0.0156 to 0.00373 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,314 | 8.53 | -99.4% | -1,366 to -1,246 | GAIN |
| end-to-end latency, 99th percentile (ms) | 2,294 | 9.89 | -99.6% | -2,347 to -2,221 | GAIN |
| end-to-end latency, median (ms) | 6.8 | 5.52 | -18.8% | -1.51 to -1.04 | GAIN |
| end-to-end latency, mean (ms) | 159 | 6.69 | -95.8% | -154 to -149 | GAIN |
| consumer lag, most messages waiting at once | 2,220 | 128 | -94.3% | -2,450 to -1,735 | GAIN |
| consumer lag, mean messages waiting | 135 | 5.54 | -95.9% | -132 to -127 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.46 | +173.2% | 1.36 to 5.56 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.326 | 0.346 | +6.1% | 0.0132 to 0.0265 | power given |
| host CPU-seconds | 597 | 622 | +4.3% | 13.8 to 38.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.78 | 1.67 | -6.3% | -0.142 to -0.0817 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
