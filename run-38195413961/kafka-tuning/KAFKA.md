# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 370 | 368 | -0.4% | -4.15 to 1.09 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0045 to 0.00779 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,569 | 1,638 | +4.4% | -36.8 to 174 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,534 | 2,555 | +0.8% | -304 to 345 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.56 | 8.53 | -0.3% | -0.0956 to 0.0503 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 217 | 224 | +2.9% | -9.27 to 22.1 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,145 | 1,152 | +0.6% | -9.58 to 24.2 | no difference beyond the noise |
| consumer lag, mean messages waiting | 97.3 | 99.8 | +2.5% | -3.18 to 8.12 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.5% | -0.00997 to -0.00997 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.311 | 0.311 | +0.1% | -0.0122 to 0.0129 | no difference beyond the noise |
| host CPU-seconds | 360 | 361 | +0.4% | -13.7 to 16.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.26 | +0.8% | -0.131 to 0.185 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
