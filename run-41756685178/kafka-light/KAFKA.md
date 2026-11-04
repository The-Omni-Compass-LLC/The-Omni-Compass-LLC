# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1923 messages a second; base rate 288.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 845 | +15.9% | 111 to 120 | GAIN |
| throughput (messages a second consumed) | 846 | 846 | -0.0% | -0.0305 to 0.0236 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,976 | 8.98 | -99.5% | -2,019 to -1,915 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,301 | 20.1 | -99.4% | -3,553 to -3,008 | GAIN |
| end-to-end latency, median (ms) | 7.43 | 5.77 | -22.4% | -1.86 to -1.46 | GAIN |
| end-to-end latency, mean (ms) | 261 | 9.02 | -96.5% | -263 to -241 | GAIN |
| consumer lag, most messages waiting at once | 2,955 | 361 | -87.8% | -3,829 to -1,358 | GAIN |
| consumer lag, mean messages waiting | 225 | 7.68 | -96.6% | -227 to -208 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.39 | +169.4% | 2.83 to 3.95 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.32 | 0.357 | +11.3% | 0.0297 to 0.0426 | power given |
| host CPU-seconds | 568 | 631 | +11.1% | 52 to 73.9 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.73 | 1.66 | -4.1% | -0.107 to -0.0362 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
