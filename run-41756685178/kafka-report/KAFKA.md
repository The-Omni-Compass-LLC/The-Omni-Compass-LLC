# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 975 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340 | 420 | +23.4% | 77.9 to 81.3 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.2% | -0.934 to 2.45 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,575 | 11.2 | -99.6% | -2,813 to -2,314 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,702 | 36.9 | -99.0% | -3,757 to -3,573 | GAIN |
| end-to-end latency, median (ms) | 9.26 | 8.05 | -13.1% | -1.95 to -0.468 | GAIN |
| end-to-end latency, mean (ms) | 388 | 8.89 | -97.7% | -409 to -350 | GAIN |
| consumer lag, most messages waiting at once | 1,685 | 54.7 | -96.8% | -1,809 to -1,451 | GAIN |
| consumer lag, mean messages waiting | 168 | 4.03 | -97.6% | -177 to -150 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.78 | +139.0% | 1.54 to 4.02 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.309 | 0.329 | +6.7% | 0.0079 to 0.0335 | power given |
| host CPU-seconds | 217 | 231 | +6.4% | 5.28 to 22.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.06 | -13.6% | -0.632 to -0.331 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.7% | 25.9 to 26.1 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00872 to 0.00371 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,509 | 12.5 | -99.5% | -2,599 to -2,394 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,037 | 14.1 | -99.7% | -4,326 to -3,721 | GAIN |
| end-to-end latency, median (ms) | 11.6 | 11.4 | -1.8% | -0.363 to -0.0436 | GAIN |
| end-to-end latency, mean (ms) | 342 | 11.2 | -96.7% | -334 to -327 | GAIN |
| consumer lag, most messages waiting at once | 723 | 36.7 | -94.9% | -706 to -666 | GAIN |
| consumer lag, mean messages waiting | 62.5 | 1.98 | -96.8% | -60.7 to -60.3 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.58 | +228.9% | 4.56 to 4.6 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.299 | 0.308 | +3.0% | -0.000185 to 0.0181 | STEADY, no difference beyond the noise |
| host CPU-seconds | 538 | 553 | +2.8% | -0.704 to 30.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 8.11 | 7.09 | -12.7% | -1.26 to -0.794 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

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

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 979 messages a second; base rate 146.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 431 | +17.1% | 61.9 to 64.2 | GAIN |
| throughput (messages a second consumed) | 431 | 431 | -0.0% | -0.00588 to 0.0023 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,342 | 9.17 | -99.6% | -2,531 to -2,136 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,688 | 11.2 | -99.7% | -3,902 to -3,452 | GAIN |
| end-to-end latency, median (ms) | 8.1 | 6.8 | -16.0% | -1.93 to -0.655 | GAIN |
| end-to-end latency, mean (ms) | 315 | 6.95 | -97.8% | -322 to -293 | GAIN |
| consumer lag, most messages waiting at once | 1,686 | 25.3 | -98.5% | -1,731 to -1,591 | GAIN |
| consumer lag, mean messages waiting | 140 | 3.14 | -97.8% | -144 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.87 | +143.5% | 2.1 to 3.64 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.281 | 0.301 | +7.0% | -0.0169 to 0.0561 | STEADY, no difference beyond the noise |
| host CPU-seconds | 502 | 535 | +6.7% | -31.2 to 98.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.03 | 2.76 | -8.9% | -0.62 to 0.0794 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 12 | +500.0% | 1.39 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
