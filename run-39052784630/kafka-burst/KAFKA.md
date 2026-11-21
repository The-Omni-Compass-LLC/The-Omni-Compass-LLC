# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.1% | -2.09 to 1.26 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00893 to -5.18e-05 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,509 | 2,546 | +1.5% | -115 to 188 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,778 | 3,744 | -0.9% | -550 to 483 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.74 | 8.63 | -1.2% | -0.417 to 0.203 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 378 | 382 | +1.0% | -4.09 to 11.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,658 | -0.6% | -88 to 68.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.3% | -2.29 to 3.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -0.9% | -0.00805 to 0.00254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 212 | -0.9% | -5.36 to 1.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.45 | -0.8% | -0.0679 to 0.0136 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
