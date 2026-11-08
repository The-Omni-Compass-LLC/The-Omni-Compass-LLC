# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 421 | +23.4% | 79.4 to 80.2 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.3% | 1.14 to 1.17 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,582 | 11 | -99.6% | -2,884 to -2,258 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,836 | 33.5 | -99.1% | -4,402 to -3,203 | GAIN |
| end-to-end latency, median (ms) | 9.28 | 7.94 | -14.4% | -2.5 to -0.177 | GAIN |
| end-to-end latency, mean (ms) | 392 | 8.43 | -97.8% | -391 to -375 | GAIN |
| consumer lag, most messages waiting at once | 1,713 | 87.7 | -94.9% | -1,837 to -1,414 | GAIN |
| consumer lag, mean messages waiting | 170 | 3.98 | -97.7% | -172 to -160 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.92 | +146.1% | 1.65 to 4.2 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.305 | 0.323 | +6.1% | 0.00218 to 0.035 | power given |
| host CPU-seconds | 214 | 227 | +5.8% | 0.459 to 24.2 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.48 | 2.99 | -14.0% | -0.676 to -0.3 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
