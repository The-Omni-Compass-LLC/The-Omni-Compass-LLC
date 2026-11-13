# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 392 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 149 | 148 | -0.4% | -1.24 to 0.121 | no difference beyond the noise |
| throughput (messages a second consumed) | 172 | 172 | -0.0% | -0.00176 to 0.000579 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,531 | 1,556 | +1.7% | -86.9 to 138 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,423 | 2,430 | +0.3% | -42.2 to 56.4 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11 | 11 | -0.4% | -0.416 to 0.329 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 209 | 215 | +2.7% | -5.9 to 17.3 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 472 | 457 | -3.2% | -66.6 to 36.6 | no difference beyond the noise |
| consumer lag, mean messages waiting | 39 | 40.1 | +2.8% | -0.808 to 2.98 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2.02 | +0.9% | -0.0431 to 0.0808 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.265 | 0.263 | -0.6% | -0.012 to 0.00875 | no difference beyond the noise |
| host CPU-seconds | 317 | 315 | -0.6% | -14.4 to 10.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.08 | 7.06 | -0.2% | -0.318 to 0.285 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 5.33 | +166.7% | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
