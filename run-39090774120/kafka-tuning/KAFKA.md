# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 970 messages a second; base rate 145.5/s; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 364 | -0.2% | -3.22 to 2.05 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 427 | 427 | +0.0% | -0.00267 to 0.00397 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,214 | 2,241 | +1.2% | -222 to 274 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,567 | 3,531 | -1.0% | -181 to 111 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.64 | 8.6 | -0.5% | -0.143 to 0.062 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 296 | 300 | +1.3% | -24 to 31.8 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,600 | 1,629 | +1.8% | -58 to 117 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 131 | 132 | +1.1% | -10.5 to 13.4 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +5.9% | -0.421 to 0.658 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.316 | 0.314 | -0.6% | -0.0172 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 548 | 546 | -0.4% | -28.7 to 24.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.34 | 3.33 | -0.3% | -0.18 to 0.163 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
