# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 983 messages a second; base rate 110.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 342 | -0.2% | -8.48 to 7.23 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | -0.0% | -0.0121 to 0.0106 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,571 | 2,682 | +4.3% | 17.1 to 206 | LOSS |
| end-to-end latency, 99th percentile (ms) | 3,904 | 3,865 | -1.0% | -453 to 375 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.9 | 14.2 | +18.9% | -7.84 to 12.3 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 403 | 408 | +1.2% | -47.3 to 56.6 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,697 | 1,734 | +2.1% | -155 to 228 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 177 | 179 | +1.3% | -21.4 to 26 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.263 | 0.262 | -0.5% | -0.0148 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 188 | -0.5% | -10.4 to 8.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.05 | 3.04 | -0.3% | -0.165 to 0.146 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
