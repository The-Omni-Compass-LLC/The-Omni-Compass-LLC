# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.7/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725 | 851 | +17.4% | 120 to 132 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0254 to 0.0064 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,569 | 9.92 | -99.6% | -2,617 to -2,502 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,876 | 13.9 | -99.6% | -3,927 to -3,798 | GAIN |
| end-to-end latency, median (ms) | 8.14 | 6.42 | -21.1% | -2.13 to -1.3 | GAIN |
| end-to-end latency, mean (ms) | 339 | 9.36 | -97.2% | -342 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,425 | 413 | -87.9% | -4,638 to -1,386 | GAIN |
| consumer lag, mean messages waiting | 293 | 8.25 | -97.2% | -296 to -273 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.52 | +176.2% | 2.17 to 4.88 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.377 | 0.448 | +18.7% | 0.0591 to 0.082 | power given |
| host CPU-seconds | 655 | 780 | +19.0% | 104 to 145 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.01 | 2.04 | +1.4% | -0.0366 to 0.0933 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
