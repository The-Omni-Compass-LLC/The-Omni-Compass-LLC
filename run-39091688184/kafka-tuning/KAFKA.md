# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -0.704 to 0.908 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.0123 to 0.00796 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,386 | 2,383 | -0.1% | -90.5 to 84.8 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,771 | 3,696 | -2.0% | -400 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.51 | 8.54 | +0.3% | -0.134 to 0.178 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 322 | 319 | -0.9% | -17.4 to 11.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,689 | 1,675 | -0.9% | -42.6 to 13.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 141 | -0.7% | -9.02 to 7.08 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.309 | 0.308 | -0.4% | -0.0153 to 0.0131 | EVEN, no difference beyond the noise |
| host CPU-seconds | 537 | 534 | -0.6% | -29.4 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.26 | 3.24 | -0.6% | -0.185 to 0.147 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
