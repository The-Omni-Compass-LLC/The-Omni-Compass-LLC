# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 20.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 348 | 346 | -0.4% | -2.6 to -0.00113 | **WORSE** |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.0417 to 0.07 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,682 | 1,711 | +1.8% | -29.5 to 88.6 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,471 | 2,488 | +0.7% | -96.5 to 130 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.45 | 9.77 | +3.4% | -0.0235 to 0.669 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 262 | 268 | +2.2% | 0.959 to 10.6 | **WORSE** |
| consumer lag, most messages waiting at once | 1,100 | 1,130 | +2.7% | 17.2 to 42.2 | **WORSE** |
| consumer lag, mean messages waiting | 115 | 117 | +1.7% | -0.731 to 4.75 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -1.2% | -0.0249 to -0.0244 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.295 | 0.29 | -1.7% | -0.0297 to 0.0196 | no difference beyond the noise |
| host CPU-seconds | 138 | 136 | -1.7% | -13.8 to 9.24 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.29 | 3.25 | -1.3% | -0.306 to 0.222 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
