# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.3% | -1.35 to 0.543 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000429 to 0.0005 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,277 | 2,326 | +2.2% | -139 to 238 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,615 | 3,604 | -0.3% | -371 to 349 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.6 | -0.2% | -0.0284 to -0.00493 | GAIN |
| end-to-end latency, mean (ms) | 308 | 313 | +1.7% | -19.1 to 29.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 694 | 699 | +0.7% | -35.9 to 45.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.8 | 58.1 | +2.2% | -4.21 to 6.69 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.254 | 0.253 | -0.2% | -0.00421 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 455 | 454 | -0.2% | -7.7 to 5.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.84 | 6.85 | +0.1% | -0.131 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
