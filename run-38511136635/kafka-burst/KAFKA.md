# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 343 | +0.1% | -3.3 to 3.95 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | +0.0% | -0.0182 to 0.0218 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,544 | 2,525 | -0.7% | -258 to 221 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,819 | 3,830 | +0.3% | -41 to 61.9 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 12.2 | 11.7 | -3.8% | -5.2 to 4.27 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 396 | 396 | -0.2% | -22.3 to 20.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,700 | 1,677 | -1.4% | -71.7 to 24.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 174 | +0.3% | -8.13 to 9.33 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | -1.0% | -0.0229 to 0.0178 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 189 | -0.9% | -16.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.05 | -1.0% | -0.245 to 0.183 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
