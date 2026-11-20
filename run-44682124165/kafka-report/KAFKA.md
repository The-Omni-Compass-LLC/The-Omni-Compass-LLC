# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 962 messages a second; base rate 108.3/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 339 | 414 | +22.2% | 74.6 to 76 | GAIN |
| throughput (messages a second consumed) | 414 | 414 | +0.1% | -1.27 to 2.02 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,305 | 10.9 | -99.5% | -2,979 to -1,610 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,442 | 54.1 | -98.4% | -4,124 to -2,652 | GAIN |
| end-to-end latency, median (ms) | 8.62 | 7.73 | -10.3% | -0.915 to -0.867 | GAIN |
| end-to-end latency, mean (ms) | 343 | 8.46 | -97.5% | -407 to -262 | GAIN |
| consumer lag, most messages waiting at once | 1,483 | 24.3 | -98.4% | -1,738 to -1,179 | GAIN |
| consumer lag, mean messages waiting | 147 | 3.35 | -97.7% | -173 to -114 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.87 | +143.4% | 1.63 to 4.11 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.29 | 0.31 | +6.8% | 0.0195 to 0.0202 | power given |
| host CPU-seconds | 208 | 221 | +6.5% | 13.1 to 14 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.39 | 2.96 | -12.8% | -0.459 to -0.408 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 395 messages a second; base rate 59.3/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.7% | 25.3 to 27 | GAIN |
| throughput (messages a second consumed) | 174 | 174 | +0.0% | -0.00105 to 0.00108 | STEADY, the same |
| end-to-end latency, 95th percentile (ms) | 2,654 | 12.6 | -99.5% | -2,708 to -2,574 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,051 | 30.4 | -99.2% | -4,176 to -3,866 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.3 | -2.4% | -0.429 to -0.126 | GAIN |
| end-to-end latency, mean (ms) | 358 | 12.8 | -96.4% | -359 to -333 | GAIN |
| consumer lag, most messages waiting at once | 740 | 70.7 | -90.5% | -810 to -528 | GAIN |
| consumer lag, mean messages waiting | 65.9 | 2.41 | -96.3% | -66.9 to -60 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.22 | +161.0% | 0.825 to 5.61 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.296 | 0.303 | +2.4% | -0.00522 to 0.0197 | STEADY, no difference beyond the noise |
| host CPU-seconds | 523 | 535 | +2.3% | -10 to 34.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.88 | 6.85 | -13.1% | -1.33 to -0.738 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1952 messages a second; base rate 292.9/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730 | 858 | +17.4% | 119 to 136 | GAIN |
| throughput (messages a second consumed) | 859 | 859 | -0.0% | -0.0279 to 0.0229 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,571 | 8.84 | -99.7% | -2,798 to -2,326 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,904 | 25.6 | -99.3% | -4,092 to -3,663 | GAIN |
| end-to-end latency, median (ms) | 7.35 | 5.81 | -21.0% | -1.79 to -1.3 | GAIN |
| end-to-end latency, mean (ms) | 339 | 9.05 | -97.3% | -369 to -291 | GAIN |
| consumer lag, most messages waiting at once | 3,457 | 647 | -81.3% | -4,686 to -934 | GAIN |
| consumer lag, mean messages waiting | 296 | 8.41 | -97.2% | -323 to -253 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.03 | +201.4% | 3.3 to 4.76 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.323 | 0.356 | +10.1% | 0.0312 to 0.0342 | power given |
| host CPU-seconds | 574 | 630 | +9.8% | 55.1 to 57.1 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.75 | 1.63 | -6.5% | -0.13 to -0.0986 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 981 messages a second; base rate 147.1/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.1% | 62.7 to 63.3 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.000915 to -0.000267 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,435 | 10.1 | -99.6% | -2,582 to -2,268 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,748 | 12.4 | -99.7% | -3,953 to -3,518 | GAIN |
| end-to-end latency, median (ms) | 8.01 | 7.02 | -12.4% | -1.24 to -0.751 | GAIN |
| end-to-end latency, mean (ms) | 322 | 9.32 | -97.1% | -322 to -305 | GAIN |
| consumer lag, most messages waiting at once | 1,706 | 266 | -84.4% | -1,478 to -1,402 | GAIN |
| consumer lag, mean messages waiting | 143 | 4.29 | -97.0% | -143 to -134 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.4 | +69.8% | 1.07 to 1.73 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.314 | 0.317 | +0.8% | -0.0122 to 0.0172 | STEADY, no difference beyond the noise |
| host CPU-seconds | 578 | 577 | -0.1% | -26.2 to 25.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.49 | 2.98 | -14.7% | -0.656 to -0.37 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
