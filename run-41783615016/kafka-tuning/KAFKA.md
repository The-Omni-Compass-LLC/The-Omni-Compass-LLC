# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 980 messages a second; base rate 147.0/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 367 | 431 | +17.3% | 60.6 to 66.3 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00738 to 0.00734 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,454 | 9.98 | -99.6% | -2,536 to -2,353 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,775 | 17.4 | -99.5% | -3,880 to -3,635 | GAIN |
| end-to-end latency, median (ms) | 8.2 | 7.07 | -13.7% | -1.33 to -0.925 | GAIN |
| end-to-end latency, mean (ms) | 325 | 9.21 | -97.2% | -332 to -299 | GAIN |
| consumer lag, most messages waiting at once | 1,725 | 220 | -87.2% | -2,013 to -996 | GAIN |
| consumer lag, mean messages waiting | 144 | 4.19 | -97.1% | -146 to -133 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.91 | +145.6% | 1.41 to 4.41 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.299 | 0.315 | +5.2% | 0.00859 to 0.0223 | power given |
| host CPU-seconds | 532 | 559 | +5.1% | 13.9 to 40 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.22 | 2.89 | -10.4% | -0.394 to -0.277 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
