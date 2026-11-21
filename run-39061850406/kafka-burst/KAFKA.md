# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 339 | -0.8% | -10.3 to 4.57 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 419 | 419 | +0.0% | -0.00747 to 0.0123 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,491 | 2,563 | +2.9% | -449 to 592 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,582 | 3,843 | +7.3% | -109 to 632 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.87 | 8.7 | -2.0% | -1.52 to 1.17 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 373 | 392 | +5.3% | -28.2 to 67.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,607 | 1,688 | +5.1% | -187 to 350 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 161 | 170 | +5.5% | -9.86 to 27.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.01 | +0.4% | -0.0957 to 0.11 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.284 | -0.3% | -0.0135 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | -0.3% | -9.45 to 8.41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.31 | 3.33 | +0.6% | -0.0579 to 0.0974 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
