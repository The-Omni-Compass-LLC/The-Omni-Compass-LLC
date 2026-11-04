# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1942 messages a second; base rate 291.3/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 854 | +17.5% | 125 to 130 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.022 to 0.00454 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,490 | 9.21 | -99.6% | -2,554 to -2,407 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,854 | 11.1 | -99.7% | -4,040 to -3,646 | GAIN |
| end-to-end latency, median (ms) | 7.82 | 6.06 | -22.6% | -2.09 to -1.44 | GAIN |
| end-to-end latency, mean (ms) | 336 | 6.58 | -98.0% | -342 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,426 | 62.7 | -98.2% | -3,494 to -3,234 | GAIN |
| consumer lag, mean messages waiting | 293 | 5.75 | -98.0% | -297 to -277 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.78 | +189.2% | 2.45 to 5.12 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.347 | 0.393 | +13.2% | 0.0441 to 0.0472 | power given |
| host CPU-seconds | 603 | 684 | +13.4% | 74.7 to 86.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.78 | -3.5% | -0.073 to -0.0578 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
