# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 736 | 732 | -0.5% | -17.2 to 9.99 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0181 to 0.0106 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,940 | 1,981 | +2.1% | -244 to 326 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,133 | 3,255 | +3.9% | -456 to 701 | no difference beyond the noise |
| end-to-end latency, median (ms) | 12.9 | 10.1 | -21.4% | -13 to 7.44 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 264 | 266 | +0.8% | -23.4 to 27.5 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,952 | 2,953 | +0.0% | -296 to 298 | no difference beyond the noise |
| consumer lag, mean messages waiting | 231 | 232 | +0.4% | -15.7 to 17.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.278 | 0.31 | +11.5% | -0.0392 to 0.103 | no difference beyond the noise |
| host CPU-seconds | 497 | 553 | +11.3% | -67.6 to 180 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.5 | 1.68 | +11.9% | -0.225 to 0.582 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
