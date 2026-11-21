# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 724 | 725 | +0.1% | -11.5 to 13.1 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 852 | 852 | -0.0% | -0.0129 to 0.0101 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,507 | 2,497 | -0.4% | -1,011 to 990 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,815 | 3,922 | +2.8% | -1,256 to 1,470 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.44 | 7.35 | -1.2% | -0.155 to -0.0168 | GAIN |
| end-to-end latency, mean (ms) | 336 | 338 | +0.6% | -138 to 142 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,396 | 3,432 | +1.1% | -1,261 to 1,332 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 293 | 294 | +0.4% | -126 to 128 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.03 | +1.6% | -0.136 to 0.201 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.314 | 0.311 | -1.1% | -0.00873 to 0.00156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 561 | 555 | -1.0% | -13.9 to 2.64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.72 | 1.7 | -1.1% | -0.0718 to 0.0334 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
