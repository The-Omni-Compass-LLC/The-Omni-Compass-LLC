# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 419 | +23.1% | 74.6 to 82.5 | GAIN |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -2.88 to 2.86 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,641 | 11.4 | -99.6% | -2,821 to -2,438 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,707 | 76.7 | -97.9% | -3,727 to -3,533 | GAIN |
| end-to-end latency, median (ms) | 9.27 | 8.15 | -12.0% | -1.53 to -0.696 | GAIN |
| end-to-end latency, mean (ms) | 393 | 10.6 | -97.3% | -412 to -353 | GAIN |
| consumer lag, most messages waiting at once | 1,700 | 180 | -89.4% | -1,827 to -1,212 | GAIN |
| consumer lag, mean messages waiting | 169 | 4.82 | -97.1% | -177 to -152 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.26 | +163.2% | 2.17 to 4.36 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.324 | 0.341 | +5.2% | 0.00472 to 0.0291 | power given |
| host CPU-seconds | 233 | 244 | +4.4% | 2.74 to 18 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.79 | 3.22 | -15.1% | -0.719 to -0.429 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
