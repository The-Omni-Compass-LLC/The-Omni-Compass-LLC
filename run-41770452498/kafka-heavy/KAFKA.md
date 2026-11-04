# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 171 | +16.6% | 24.1 to 24.8 | GAIN |
| throughput (messages a second consumed) | 171 | 171 | -0.0% | -0.00323 to 0.00191 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,181 | 12.3 | -99.4% | -2,224 to -2,112 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,420 | 16 | -99.5% | -3,712 to -3,096 | GAIN |
| end-to-end latency, median (ms) | 11.4 | 11.2 | -1.9% | -0.316 to -0.116 | GAIN |
| end-to-end latency, mean (ms) | 287 | 11.8 | -95.9% | -288 to -262 | GAIN |
| consumer lag, most messages waiting at once | 647 | 68 | -89.5% | -637 to -522 | GAIN |
| consumer lag, mean messages waiting | 52.6 | 2.07 | -96.1% | -52.4 to -48.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.48 | +124.1% | -0.0467 to 5.01 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.281 | 0.285 | +1.3% | -0.00303 to 0.0104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 503 | 509 | +1.2% | -5.56 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.6 | 6.59 | -13.2% | -1.22 to -0.788 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
