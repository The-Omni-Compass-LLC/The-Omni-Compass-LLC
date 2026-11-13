# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1929 messages a second; base rate 289.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 760 | +4.2% | -112 to 174 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 848 | 848 | -0.0% | -0.014 to 0.00343 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,111 | 1,529 | -27.5% | -3,528 to 2,365 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,390 | 2,702 | -20.3% | -4,363 to 2,987 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.41 | 7.11 | -4.0% | -1.48 to 0.893 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 281 | 211 | -24.8% | -427 to 288 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,114 | 2,786 | -10.5% | -2,183 to 1,527 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 244 | 183 | -25.0% | -369 to 246 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.32 | +16.1% | -0.435 to 1.08 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | -1.48 to 3.48 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.316 | +1.2% | -0.0151 to 0.0225 | EVEN, no difference beyond the noise |
| host CPU-seconds | 557 | 564 | +1.2% | -29 to 41.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.65 | -2.7% | -0.25 to 0.159 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
