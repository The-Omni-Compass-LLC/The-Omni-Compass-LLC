# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `99e540785d0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 149 | 149 | -0.1% | -0.992 to 0.681 | no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.0118 to 0.0139 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,639 | 1,623 | -1.0% | -37.9 to 6.14 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 2,444 | 2,444 | -0.0% | -174 to 173 | no difference beyond the noise |
| end-to-end latency, median (ms) | 11.6 | 11.6 | -0.2% | -0.0563 to 0.019 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 221 | 222 | +0.4% | -3.11 to 4.93 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 483 | 467 | -3.2% | -117 to 86 | no difference beyond the noise |
| consumer lag, mean messages waiting | 41.9 | 41.7 | -0.6% | -1.44 to 0.954 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 2 | +0.2% | -0.0575 to 0.0664 | no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | no difference beyond the noise |
| host CPU busy (share of the run) | 0.282 | 0.282 | -0.2% | -0.0102 to 0.00919 | no difference beyond the noise |
| host CPU-seconds | 331 | 331 | -0.1% | -11.6 to 10.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.42 | 7.42 | -0.0% | -0.293 to 0.293 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
