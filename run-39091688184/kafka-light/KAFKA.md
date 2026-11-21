# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.1/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 726 | +0.1% | -1.4 to 3 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 851 | 851 | +0.0% | -0.0239 to 0.0438 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,377 | 2,309 | -2.9% | -275 to 139 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,662 | 3,667 | +0.1% | -350 to 360 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.48 | 8.5 | +0.3% | -0.343 to 0.391 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 323 | 316 | -2.0% | -15.4 to 2.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,308 | 3,279 | -0.9% | -83.1 to 23.8 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 281 | 275 | -2.0% | -12.5 to 1.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.332 | 0.326 | -1.7% | -0.0259 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 569 | 559 | -1.7% | -43.1 to 24.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.71 | -1.8% | -0.136 to 0.074 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
