# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 171 | +16.8% | 23.9 to 25.3 | GAIN |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00128 to 0.00164 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,181 | 12.7 | -99.4% | -2,262 to -2,074 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,445 | 17.1 | -99.5% | -3,615 to -3,241 | GAIN |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -1.4% | -0.313 to -0.0109 | GAIN |
| end-to-end latency, mean (ms) | 288 | 12.3 | -95.7% | -293 to -258 | GAIN |
| consumer lag, most messages waiting at once | 660 | 58 | -91.2% | -650 to -555 | GAIN |
| consumer lag, mean messages waiting | 52.6 | 2.18 | -95.9% | -53 to -47.9 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.45 | +72.7% | 0.438 to 2.47 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.286 | 0.292 | +2.2% | -0.00571 to 0.018 | STEADY, no difference beyond the noise |
| host CPU-seconds | 515 | 525 | +2.0% | -10.8 to 31.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.79 | 6.81 | -12.7% | -1.26 to -0.713 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
