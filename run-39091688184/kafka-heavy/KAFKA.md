# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.34 to 0.924 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.0035 to 0.00242 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,539 | 2,575 | +1.4% | -102 to 175 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,923 | 3,818 | -2.7% | -582 to 373 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.5 | 11.6 | +0.4% | -0.116 to 0.201 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 346 | 347 | +0.2% | -32.6 to 34.2 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 725 | 737 | +1.7% | -14.3 to 38.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 63.6 | 64.1 | +0.8% | -5.17 to 6.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.281 | 0.281 | +0.1% | -0.0115 to 0.0118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 494 | +0.1% | -20.3 to 20.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.45 | 7.46 | +0.2% | -0.239 to 0.268 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
