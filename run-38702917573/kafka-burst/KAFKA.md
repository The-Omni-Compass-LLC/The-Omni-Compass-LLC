# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.5/s; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `e842b63d0313`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.1% | -0.857 to -0.076 | LOSS |
| throughput (messages a second consumed) | 418 | 418 | +0.0% | -0.00805 to 0.0137 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,512 | 2,452 | -2.4% | -150 to 31 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,673 | 3,827 | +4.2% | -148 to 455 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 9.66 | 10 | +3.7% | -0.626 to 1.34 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 381 | 383 | +0.3% | -5.97 to 8.59 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,646 | 1,654 | +0.5% | -110 to 128 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 166 | 167 | +0.7% | -2.77 to 5.07 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.297 | 0.292 | -1.9% | -0.0225 to 0.0114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 204 | -1.9% | -15.6 to 7.87 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.38 | 3.32 | -1.7% | -0.247 to 0.131 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
