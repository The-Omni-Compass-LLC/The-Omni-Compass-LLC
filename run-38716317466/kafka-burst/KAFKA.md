# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9888ce5c575a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.1% | -2.02 to 1.08 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00537 to 0.00246 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,560 | 2,488 | -2.8% | -227 to 81 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,795 | 3,854 | +1.6% | -459 to 578 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.67 | 8.51 | -1.9% | -0.706 to 0.371 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 384 | 381 | -0.8% | -18.4 to 12.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,670 | 1,660 | -0.6% | -78.9 to 60.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 164 | -0.8% | -9.23 to 6.45 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0166 to -0.0166 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.287 | 0.283 | -1.3% | -0.0137 to 0.00647 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 203 | -1.2% | -9.55 to 4.68 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.3 | -1.0% | -0.151 to 0.0812 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
