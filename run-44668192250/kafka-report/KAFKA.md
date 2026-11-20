# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 982 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 343 | 422 | +23.1% | 78.2 to 80.4 | GAIN |
| throughput (messages a second consumed) | 422 | 422 | +0.1% | -1.3 to 2.07 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,651 | 12.1 | -99.5% | -2,898 to -2,379 | GAIN |
| end-to-end latency, 99th percentile (ms) | 4,020 | 51.8 | -98.7% | -4,381 to -3,556 | GAIN |
| end-to-end latency, median (ms) | 10.2 | 7.85 | -22.9% | -3.15 to -1.52 | GAIN |
| end-to-end latency, mean (ms) | 397 | 8.71 | -97.8% | -394 to -383 | GAIN |
| consumer lag, most messages waiting at once | 1,744 | 45.7 | -97.4% | -1,755 to -1,641 | GAIN |
| consumer lag, mean messages waiting | 173 | 3.96 | -97.7% | -173 to -166 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.24 | +161.9% | 1.67 to 4.81 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.316 | 0.315 | -0.3% | -0.0903 to 0.0884 | STEADY, no difference beyond the noise |
| host CPU-seconds | 225 | 223 | -1.1% | -59.2 to 54.4 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.64 | 2.93 | -19.6% | -1.51 to 0.0891 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 173 | +17.6% | 25.5 to 26.4 | GAIN |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.000637 to 0.000169 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,563 | 12.6 | -99.5% | -2,758 to -2,343 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,926 | 22.9 | -99.4% | -4,074 to -3,732 | GAIN |
| end-to-end latency, median (ms) | 11.7 | 11.3 | -3.1% | -0.571 to -0.161 | GAIN |
| end-to-end latency, mean (ms) | 347 | 13.3 | -96.2% | -347 to -321 | GAIN |
| consumer lag, most messages waiting at once | 724 | 108 | -85.1% | -866 to -366 | GAIN |
| consumer lag, mean messages waiting | 63.4 | 2.36 | -96.3% | -65.6 to -56.5 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.01 | +150.4% | -0.389 to 6.4 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.299 | 0.302 | +0.9% | -0.00154 to 0.00676 | STEADY, no difference beyond the noise |
| host CPU-seconds | 529 | 533 | +0.7% | -3.47 to 11 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.99 | 6.84 | -14.4% | -1.24 to -1.06 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1938 messages a second; base rate 290.8/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 726 | 853 | +17.5% | 122 to 132 | GAIN |
| throughput (messages a second consumed) | 853 | 853 | -0.0% | -0.0217 to 0.00131 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,503 | 9.18 | -99.6% | -2,703 to -2,285 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,795 | 10.8 | -99.7% | -4,202 to -3,367 | GAIN |
| end-to-end latency, median (ms) | 7.93 | 6.02 | -24.0% | -2.29 to -1.52 | GAIN |
| end-to-end latency, mean (ms) | 332 | 6.43 | -98.1% | -352 to -299 | GAIN |
| consumer lag, most messages waiting at once | 3,387 | 64.7 | -98.1% | -3,488 to -3,156 | GAIN |
| consumer lag, mean messages waiting | 289 | 5.65 | -98.0% | -302 to -264 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.79 | +189.7% | 2.61 to 4.98 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.351 | 0.401 | +14.1% | 0.031 to 0.0681 | power given |
| host CPU-seconds | 610 | 698 | +14.5% | 58.6 to 118 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.87 | 1.82 | -2.5% | -0.129 to 0.0347 | STEADY, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 368 | 430 | +16.9% | 60.9 to 63.4 | GAIN |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.0163 to 0.0113 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,254 | 9.28 | -99.6% | -2,310 to -2,179 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,621 | 12.7 | -99.6% | -3,790 to -3,427 | GAIN |
| end-to-end latency, median (ms) | 8.04 | 6.64 | -17.4% | -1.9 to -0.893 | GAIN |
| end-to-end latency, mean (ms) | 301 | 7.17 | -97.6% | -302 to -285 | GAIN |
| consumer lag, most messages waiting at once | 1,645 | 45.7 | -97.2% | -1,689 to -1,510 | GAIN |
| consumer lag, mean messages waiting | 133 | 3.22 | -97.6% | -132 to -128 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.77 | +188.4% | 1.91 to 5.63 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.283 | 0.298 | +5.1% | -0.00428 to 0.0333 | STEADY, no difference beyond the noise |
| host CPU-seconds | 505 | 530 | +4.9% | -8 to 57.6 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.05 | 2.74 | -10.3% | -0.487 to -0.139 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
