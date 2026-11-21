# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 964 messages a second; base rate 108.4/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 337 | -0.6% | -8.77 to 4.74 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 414 | 414 | -0.0% | -0.00746 to 0.0011 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,167 | 2,241 | +3.4% | -154 to 302 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,215 | 3,374 | +4.9% | -101 to 418 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.6 | 8.49 | -1.2% | -0.589 to 0.376 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 328 | 337 | +2.7% | -18.8 to 36.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,442 | 1,445 | +0.2% | -16 to 21.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 140 | 144 | +2.6% | -8.74 to 16.1 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.7% | -0.0226 to -0.00684 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.285 | 0.285 | -0.0% | -0.0186 to 0.0186 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | +0.1% | -13.1 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 3.35 | +0.7% | -0.172 to 0.215 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
