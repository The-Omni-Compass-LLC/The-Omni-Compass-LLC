# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 978 messages a second; base rate 110.0/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 421 | +23.2% | 77.1 to 81.5 | GAIN |
| throughput (messages a second consumed) | 420 | 421 | +0.1% | -1.26 to 2.03 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,606 | 11.1 | -99.6% | -2,775 to -2,414 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,850 | 32.5 | -99.2% | -4,396 to -3,239 | GAIN |
| end-to-end latency, median (ms) | 9.31 | 7.93 | -14.8% | -1.5 to -1.24 | GAIN |
| end-to-end latency, mean (ms) | 395 | 8.32 | -97.9% | -392 to -381 | GAIN |
| consumer lag, most messages waiting at once | 1,725 | 59.3 | -96.6% | -1,844 to -1,488 | GAIN |
| consumer lag, mean messages waiting | 172 | 3.55 | -97.9% | -171 to -166 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 6.3 | +215.1% | 3.09 to 5.52 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.306 | 0.329 | +7.4% | 0.00507 to 0.0405 | power given |
| host CPU-seconds | 216 | 232 | +7.3% | 3.89 to 27.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.5 | 3.05 | -12.8% | -0.63 to -0.269 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 171 | +16.8% | 23.9 to 25.3 | GAIN |
| throughput (messages a second consumed) | 171 | 171 | +0.0% | -0.00128 to 0.00164 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,181 | 12.7 | -99.4% | -2,262 to -2,074 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,445 | 17.1 | -99.5% | -3,615 to -3,241 | GAIN |
| end-to-end latency, median (ms) | 11.4 | 11.3 | -1.4% | -0.313 to -0.0109 | GAIN |
| end-to-end latency, mean (ms) | 288 | 12.3 | -95.7% | -293 to -258 | GAIN |
| consumer lag, most messages waiting at once | 660 | 58 | -91.2% | -650 to -555 | GAIN |
| consumer lag, mean messages waiting | 52.6 | 2.18 | -95.9% | -53 to -47.9 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 3.45 | +72.7% | 0.438 to 2.47 | power given |
| consumers running, most at once | 2 | 5 | +150.0% | 3 to 3 | power given |
| host CPU busy (share of the run) | 0.286 | 0.292 | +2.2% | -0.00571 to 0.018 | STEADY, no difference beyond the noise |
| host CPU-seconds | 515 | 525 | +2.0% | -10.8 to 31.3 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.79 | 6.81 | -12.7% | -1.26 to -0.713 | GAIN |
| consumer changes written (the knob's moves) | 2 | 8 | +300.0% | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1945 messages a second; base rate 291.8/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 856 | +17.4% | 126 to 127 | GAIN |
| throughput (messages a second consumed) | 856 | 856 | -0.0% | -0.0371 to 0.019 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,486 | 8.96 | -99.6% | -2,556 to -2,398 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,860 | 10.3 | -99.7% | -4,130 to -3,570 | GAIN |
| end-to-end latency, median (ms) | 7.32 | 5.92 | -19.1% | -1.65 to -1.14 | GAIN |
| end-to-end latency, mean (ms) | 326 | 6.02 | -98.1% | -322 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,413 | 20.3 | -99.4% | -3,460 to -3,325 | GAIN |
| consumer lag, mean messages waiting | 283 | 5.25 | -98.1% | -279 to -276 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.2 | +160.1% | 3 to 3.41 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.346 | 0.379 | +9.4% | 0.0267 to 0.0384 | power given |
| host CPU-seconds | 621 | 674 | +8.5% | 39.5 to 66.6 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.89 | 1.75 | -7.5% | -0.183 to -0.102 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 982 messages a second; base rate 147.3/s; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 369 | 432 | +17.1% | 61.7 to 64.6 | GAIN |
| throughput (messages a second consumed) | 432 | 432 | -0.0% | -0.0035 to 0.002 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,335 | 8.75 | -99.6% | -2,508 to -2,145 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,689 | 10.7 | -99.7% | -3,863 to -3,493 | GAIN |
| end-to-end latency, median (ms) | 7.97 | 6.47 | -18.8% | -1.69 to -1.31 | GAIN |
| end-to-end latency, mean (ms) | 314 | 6.9 | -97.8% | -322 to -292 | GAIN |
| consumer lag, most messages waiting at once | 1,676 | 27.3 | -98.4% | -1,739 to -1,559 | GAIN |
| consumer lag, mean messages waiting | 140 | 3.04 | -97.8% | -144 to -130 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.22 | +161.0% | 2.76 to 3.68 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.27 | 0.284 | +5.4% | 0.00602 to 0.0232 | power given |
| host CPU-seconds | 481 | 506 | +5.3% | 11 to 39.7 | power given |
| host CPU-seconds per 1,000 messages inside the line | 2.9 | 2.6 | -10.1% | -0.384 to -0.203 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
