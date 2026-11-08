# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1940 messages a second; base rate 290.9/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 853 | +17.3% | 123 to 128 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0272 to 0.0142 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,403 | 8.74 | -99.6% | -2,626 to -2,162 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,796 | 12.3 | -99.7% | -4,234 to -3,334 | GAIN |
| end-to-end latency, median (ms) | 7.37 | 5.74 | -22.2% | -1.84 to -1.43 | GAIN |
| end-to-end latency, mean (ms) | 322 | 6.64 | -97.9% | -354 to -276 | GAIN |
| consumer lag, most messages waiting at once | 3,351 | 92 | -97.3% | -3,773 to -2,745 | GAIN |
| consumer lag, mean messages waiting | 279 | 5.75 | -97.9% | -308 to -239 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.51 | +175.3% | 2.76 to 4.25 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.318 | 0.35 | +10.0% | 0.0252 to 0.0388 | power given |
| host CPU-seconds | 565 | 621 | +10.0% | 43.8 to 68.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.62 | -6.3% | -0.142 to -0.0736 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
