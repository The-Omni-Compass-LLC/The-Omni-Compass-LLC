# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1926 messages a second; base rate 288.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 721 | -0.5% | -20.4 to 12.6 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 847 | 847 | -0.0% | -0.0158 to 0.00724 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,228 | 2,819 | +26.5% | -2,352 to 3,534 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,502 | 4,489 | +28.2% | -3,021 to 4,994 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.39 | 8.24 | -1.8% | -0.663 to 0.363 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 298 | 381 | +27.9% | -290 to 457 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,158 | 3,777 | +19.6% | -2,267 to 3,505 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 259 | 329 | +26.7% | -243 to 381 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00666 to -0.00662 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.326 | 0.326 | +0.0% | -0.00111 to 0.00135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 560 | 560 | +0.1% | -3.45 to 4.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.73 | +0.6% | -0.0394 to 0.0606 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
