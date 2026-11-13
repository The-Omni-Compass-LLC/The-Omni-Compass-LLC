# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.1% | -0.916 to -0.277 | LOSS |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0243 to 0.0108 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,378 | 2,386 | +0.3% | -58 to 72.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,807 | 3,702 | -2.8% | -552 to 341 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.18 | 7.05 | -1.8% | -0.25 to -0.0131 | GAIN |
| end-to-end latency, mean (ms) | 316 | 317 | +0.2% | -1.61 to 2.58 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,339 | 3,327 | -0.4% | -39.3 to 15.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 275 | 275 | +0.1% | -2.94 to 3.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.32 | 0.319 | -0.2% | -0.00741 to 0.00627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 571 | +0.0% | -12.7 to 12.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | +0.1% | -0.0367 to 0.0402 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
