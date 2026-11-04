# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 419 | +23.1% | 74.6 to 82.5 | GAIN |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -2.88 to 2.86 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,641 | 11.4 | -99.6% | -2,821 to -2,438 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,707 | 76.7 | -97.9% | -3,727 to -3,533 | GAIN |
| end-to-end latency, median (ms) | 9.27 | 8.15 | -12.0% | -1.53 to -0.696 | GAIN |
| end-to-end latency, mean (ms) | 393 | 10.6 | -97.3% | -412 to -353 | GAIN |
| consumer lag, most messages waiting at once | 1,700 | 180 | -89.4% | -1,827 to -1,212 | GAIN |
| consumer lag, mean messages waiting | 169 | 4.82 | -97.1% | -177 to -152 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.26 | +163.2% | 2.17 to 4.36 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.324 | 0.341 | +5.2% | 0.00472 to 0.0291 | power given |
| host CPU-seconds | 233 | 244 | +4.4% | 2.74 to 18 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.79 | 3.22 | -15.1% | -0.719 to -0.429 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.4% | 25.2 to 25.9 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00279 to 0.000727 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 14.2 | -99.4% | -2,473 to -2,397 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,741 | 21.3 | -99.4% | -3,944 to -3,496 | GAIN |
| end-to-end latency, median (ms) | 11.7 | 11.5 | -2.0% | -0.388 to -0.0738 | GAIN |
| end-to-end latency, mean (ms) | 328 | 12.4 | -96.2% | -326 to -305 | GAIN |
| consumer lag, most messages waiting at once | 721 | 59 | -91.8% | -846 to -477 | GAIN |
| consumer lag, mean messages waiting | 60.6 | 2.22 | -96.3% | -60.2 to -56.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.58 | +79.2% | 0.624 to 2.54 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.298 | 0.305 | +2.2% | -0.00255 to 0.0157 | STEADY, no difference beyond the noise |
| host CPU-seconds | 527 | 538 | +2.1% | -4.68 to 27.1 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.96 | 6.92 | -13.0% | -1.3 to -0.762 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1941 messages a second; base rate 291.2/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 854 | +17.3% | 123 to 129 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.0203 to -0.0105 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,433 | 9.42 | -99.6% | -2,567 to -2,280 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,853 | 10.9 | -99.7% | -3,947 to -3,737 | GAIN |
| end-to-end latency, median (ms) | 7.47 | 6.15 | -17.7% | -1.94 to -0.707 | GAIN |
| end-to-end latency, mean (ms) | 321 | 6.28 | -98.0% | -327 to -302 | GAIN |
| consumer lag, most messages waiting at once | 3,373 | 48.3 | -98.6% | -3,403 to -3,246 | GAIN |
| consumer lag, mean messages waiting | 278 | 5.62 | -98.0% | -283 to -262 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.12 | +156.0% | 3.1 to 3.14 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.355 | 0.398 | +12.1% | 0.0271 to 0.0587 | power given |
| host CPU-seconds | 636 | 706 | +11.0% | 40.8 to 99.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.94 | 1.84 | -5.3% | -0.201 to -0.00486 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `e29ad045b2ac`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 429 | +17.3% | 61.7 to 64.9 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0115 to 0.00554 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,450 | 10.5 | -99.6% | -2,532 to -2,348 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,773 | 16.6 | -99.6% | -3,976 to -3,537 | GAIN |
| end-to-end latency, median (ms) | 8.52 | 7.44 | -12.6% | -1.27 to -0.884 | GAIN |
| end-to-end latency, mean (ms) | 325 | 8.83 | -97.3% | -322 to -311 | GAIN |
| consumer lag, most messages waiting at once | 1,714 | 120 | -93.0% | -2,014 to -1,174 | GAIN |
| consumer lag, mean messages waiting | 144 | 3.87 | -97.3% | -142 to -137 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.36 | +167.8% | 2.44 to 4.27 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.326 | 0.347 | +6.4% | 0.0098 to 0.0319 | power given |
| host CPU-seconds | 571 | 607 | +6.4% | 17.6 to 55.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.14 | -9.3% | -0.424 to -0.22 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
