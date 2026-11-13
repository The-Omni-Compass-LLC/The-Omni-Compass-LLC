# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1944 messages a second; base rate 291.6/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 728 | +0.1% | -4.02 to 5.06 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | +0.0% | -0.0906 to 0.132 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,475 | 2,437 | -1.5% | -324 to 248 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,889 | 3,770 | -3.1% | -224 to -14 | GAIN |
| end-to-end latency, median (ms) | 7.45 | 7.33 | -1.6% | -0.17 to -0.0627 | GAIN |
| end-to-end latency, mean (ms) | 337 | 328 | -2.8% | -43.4 to 24.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,408 | 3,376 | -0.9% | -145 to 82.1 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 294 | 285 | -2.9% | -37.6 to 20.8 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.7% | -0.308 to 0.815 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.67 | +33.3% | -0.768 to 2.1 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.315 | 0.315 | -0.1% | -0.00864 to 0.00816 | EVEN, no difference beyond the noise |
| host CPU-seconds | 561 | 561 | +0.0% | -13.2 to 13.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.71 | 1.71 | -0.0% | -0.0375 to 0.0359 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
