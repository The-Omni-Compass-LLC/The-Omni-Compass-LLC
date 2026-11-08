# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.2/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `b806aadd5bbb`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 428 | +16.9% | 59.7 to 64 | GAIN |
| throughput (messages a second consumed) | 429 | 429 | -0.0% | -0.00374 to 0.00373 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,305 | 9.85 | -99.6% | -2,334 to -2,257 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,562 | 18.1 | -99.5% | -3,763 to -3,326 | GAIN |
| end-to-end latency, median (ms) | 8.3 | 7.1 | -14.5% | -1.92 to -0.491 | GAIN |
| end-to-end latency, mean (ms) | 301 | 8.94 | -97.0% | -302 to -283 | GAIN |
| consumer lag, most messages waiting at once | 1,645 | 128 | -92.2% | -2,002 to -1,033 | GAIN |
| consumer lag, mean messages waiting | 133 | 3.98 | -97.0% | -133 to -125 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.97 | +148.6% | 0.789 to 5.15 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.308 | 0.322 | +4.3% | -0.0124 to 0.0391 | STEADY, no difference beyond the noise |
| host CPU-seconds | 549 | 571 | +4.1% | -23.2 to 68.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.33 | 2.96 | -10.9% | -0.616 to -0.109 | GAIN |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
