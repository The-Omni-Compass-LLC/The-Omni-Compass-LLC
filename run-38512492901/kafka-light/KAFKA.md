# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1923 messages a second; base rate 288.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 720 | -0.6% | -18 to 8.82 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 846 | 846 | +0.0% | -0.0191 to 0.0216 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,156 | 2,204 | +2.2% | -58.8 to 155 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,438 | 3,456 | +0.5% | -103 to 140 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.2 | 7.95 | -3.1% | -0.841 to 0.325 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 291 | 299 | +2.9% | -15.8 to 32.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,117 | 3,143 | +0.8% | -70.9 to 122 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 252 | 258 | +2.5% | -16.6 to 29 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.5% | -0.293 to 0.793 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 3 | +50.0% | 1 to 1 | power given |
| host CPU busy (share of the run) | 0.33 | 0.329 | -0.3% | -0.0148 to 0.0128 | EVEN, no difference beyond the noise |
| host CPU-seconds | 567 | 566 | -0.2% | -27 to 24.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | +0.4% | -0.0432 to 0.0577 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
