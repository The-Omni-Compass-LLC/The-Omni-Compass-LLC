# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1933 messages a second; base rate 289.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 723 | 850 | +17.5% | 126 to 127 | GAIN |
| throughput (messages a second consumed) | 850 | 850 | -0.0% | -0.0183 to -0.00618 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,552 | 10.9 | -99.6% | -2,645 to -2,439 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,971 | 14.3 | -99.6% | -4,090 to -3,824 | GAIN |
| end-to-end latency, median (ms) | 8.52 | 7.01 | -17.7% | -2.13 to -0.886 | GAIN |
| end-to-end latency, mean (ms) | 339 | 7.56 | -97.8% | -349 to -313 | GAIN |
| consumer lag, most messages waiting at once | 3,433 | 82.3 | -97.6% | -3,455 to -3,245 | GAIN |
| consumer lag, mean messages waiting | 292 | 6.69 | -97.7% | -301 to -269 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.03 | +151.7% | 2.72 to 3.34 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.43 | 0.48 | +11.6% | 0.0181 to 0.0816 | power given |
| host CPU-seconds | 751 | 835 | +11.3% | 21 to 149 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.31 | 2.18 | -5.3% | -0.301 to 0.0562 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
