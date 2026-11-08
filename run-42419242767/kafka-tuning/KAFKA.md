# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 963 messages a second; base rate 144.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 364 | 424 | +16.4% | 32.3 to 87.4 | GAIN |
| throughput (messages a second consumed) | 424 | 424 | -0.0% | -0.0082 to 0.0058 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,413 | 9.03 | -99.6% | -5,158 to 350 | STEADY, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,822 | 13.4 | -99.6% | -7,362 to -255 | GAIN |
| end-to-end latency, median (ms) | 8.07 | 6.63 | -17.8% | -1.77 to -1.11 | GAIN |
| end-to-end latency, mean (ms) | 326 | 7.01 | -97.8% | -736 to 98 | STEADY, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,699 | 27.7 | -98.4% | -2,979 to -363 | GAIN |
| consumer lag, mean messages waiting | 142 | 3.06 | -97.8% | -315 to 37 | STEADY, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.89 | +194.5% | 3.07 to 4.71 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.282 | 0.296 | +5.0% | -0.00707 to 0.0355 | STEADY, no difference beyond the noise |
| host CPU-seconds | 503 | 527 | +4.9% | -12.1 to 61 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.07 | 2.76 | -10.0% | -0.556 to -0.0571 | GAIN |
| consumer changes written (the knob's moves) | 2 | 18 | +800.0% | 7.39 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
