# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 964 messages a second; base rate 144.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | -0.0% | -2.37 to 2.08 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.835 to 0.519 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,989 | 1,925 | -3.2% | -252 to 124 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,213 | 3,224 | +0.3% | -241 to 264 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.57 | 8.53 | -0.5% | -0.109 to 0.0194 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 260 | 258 | -0.6% | -19.7 to 16.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,501 | 1,486 | -1.0% | -53 to 22.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 114 | 113 | -0.5% | -8.99 to 7.95 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.6% | -0.306 to 0.811 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.306 | 0.303 | -1.2% | -0.017 to 0.00991 | EVEN, no difference beyond the noise |
| host CPU-seconds | 532 | 526 | -1.1% | -30.6 to 18.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.23 | 3.2 | -1.1% | -0.175 to 0.102 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
