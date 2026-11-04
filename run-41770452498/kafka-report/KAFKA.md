# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 974 messages a second; base rate 109.6/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 420 | +23.1% | 78.2 to 79.4 | GAIN |
| throughput (messages a second consumed) | 419 | 420 | +0.3% | 1.15 to 1.18 | GAIN |
| end-to-end latency, 95th percentile (ms) | 2,484 | 11.2 | -99.5% | -2,515 to -2,431 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,715 | 61.2 | -98.4% | -3,907 to -3,402 | GAIN |
| end-to-end latency, median (ms) | 9.13 | 7.97 | -12.6% | -1.77 to -0.532 | GAIN |
| end-to-end latency, mean (ms) | 378 | 8.95 | -97.6% | -373 to -365 | GAIN |
| consumer lag, most messages waiting at once | 1,654 | 61.7 | -96.3% | -1,719 to -1,466 | GAIN |
| consumer lag, mean messages waiting | 164 | 3.84 | -97.7% | -161 to -159 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.19 | +159.7% | 1.51 to 4.88 | power given |
| consumers running, most at once | 2 | 7 | +250.0% | 0.697 to 9.3 | power given |
| host CPU busy (share of the run) | 0.304 | 0.324 | +6.6% | 0.00986 to 0.0303 | power given |
| host CPU-seconds | 214 | 227 | +6.3% | 6.15 to 20.8 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3 | -13.4% | -0.594 to -0.335 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | -2.91 to 26.9 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 390 messages a second; base rate 58.5/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 171 | +16.6% | 24.1 to 24.8 | GAIN |
| throughput (messages a second consumed) | 171 | 171 | -0.0% | -0.00323 to 0.00191 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,181 | 12.3 | -99.4% | -2,224 to -2,112 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,420 | 16 | -99.5% | -3,712 to -3,096 | GAIN |
| end-to-end latency, median (ms) | 11.4 | 11.2 | -1.9% | -0.316 to -0.116 | GAIN |
| end-to-end latency, mean (ms) | 287 | 11.8 | -95.9% | -288 to -262 | GAIN |
| consumer lag, most messages waiting at once | 647 | 68 | -89.5% | -637 to -522 | GAIN |
| consumer lag, mean messages waiting | 52.6 | 2.07 | -96.1% | -52.4 to -48.6 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 4.48 | +124.1% | -0.0467 to 5.01 | STEADY, no difference beyond the noise |
| consumers running, most at once | 2 | 6 | +200.0% | -0.303 to 8.3 | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.281 | 0.285 | +1.3% | -0.00303 to 0.0104 | STEADY, no difference beyond the noise |
| host CPU-seconds | 503 | 509 | +1.2% | -5.56 to 17.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.6 | 6.59 | -13.2% | -1.22 to -0.788 | GAIN |
| consumer changes written (the knob's moves) | 2 | 10 | +400.0% | -0.606 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1942 messages a second; base rate 291.3/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 727 | 854 | +17.5% | 125 to 130 | GAIN |
| throughput (messages a second consumed) | 854 | 854 | -0.0% | -0.022 to 0.00454 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,490 | 9.21 | -99.6% | -2,554 to -2,407 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,854 | 11.1 | -99.7% | -4,040 to -3,646 | GAIN |
| end-to-end latency, median (ms) | 7.82 | 6.06 | -22.6% | -2.09 to -1.44 | GAIN |
| end-to-end latency, mean (ms) | 336 | 6.58 | -98.0% | -342 to -317 | GAIN |
| consumer lag, most messages waiting at once | 3,426 | 62.7 | -98.2% | -3,494 to -3,234 | GAIN |
| consumer lag, mean messages waiting | 293 | 5.75 | -98.0% | -297 to -277 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.78 | +189.2% | 2.45 to 5.12 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.347 | 0.393 | +13.2% | 0.0441 to 0.0472 | power given |
| host CPU-seconds | 603 | 684 | +13.4% | 74.7 to 86.4 | power given |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.78 | -3.5% | -0.073 to -0.0578 | GAIN |
| consumer changes written (the knob's moves) | 2 | 14 | +600.0% | 12 to 12 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 968 messages a second; base rate 145.3/s; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 426 | +16.6% | 59.6 to 61.8 | GAIN |
| throughput (messages a second consumed) | 426 | 426 | -0.0% | -0.0135 to 0.00958 | STEADY, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,169 | 10.2 | -99.5% | -2,208 to -2,109 | GAIN |
| end-to-end latency, 99th percentile (ms) | 3,387 | 12.7 | -99.6% | -3,682 to -3,067 | GAIN |
| end-to-end latency, median (ms) | 8.62 | 7.34 | -14.9% | -1.42 to -1.14 | GAIN |
| end-to-end latency, mean (ms) | 282 | 7.86 | -97.2% | -285 to -264 | GAIN |
| consumer lag, most messages waiting at once | 1,583 | 67.7 | -95.7% | -1,555 to -1,475 | GAIN |
| consumer lag, mean messages waiting | 124 | 3.57 | -97.1% | -125 to -117 | GAIN |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 5.86 | +192.9% | 2.54 to 5.18 | power given |
| consumers running, most at once | 2 | 8 | +300.0% | 6 to 6 | power given |
| host CPU busy (share of the run) | 0.323 | 0.34 | +5.3% | 0.0157 to 0.0183 | power given |
| host CPU-seconds | 565 | 595 | +5.3% | 25.9 to 34.2 | power given |
| host CPU-seconds per 1,000 messages inside the line | 3.43 | 3.1 | -9.7% | -0.348 to -0.316 | GAIN |
| consumer changes written (the knob's moves) | 2 | 16 | +700.0% | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
