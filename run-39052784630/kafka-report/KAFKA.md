# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 341 | -0.1% | -2.09 to 1.26 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 420 | 420 | -0.0% | -0.00893 to -5.18e-05 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,509 | 2,546 | +1.5% | -115 to 188 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,778 | 3,744 | -0.9% | -550 to 483 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.74 | 8.63 | -1.2% | -0.417 to 0.203 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 378 | 382 | +1.0% | -4.09 to 11.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,667 | 1,658 | -0.6% | -88 to 68.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 163 | 164 | +0.3% | -2.29 to 3.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.299 | 0.296 | -0.9% | -0.00805 to 0.00254 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 212 | -0.9% | -5.36 to 1.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.47 | 3.45 | -0.8% | -0.0679 to 0.0136 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 148 | 147 | -0.3% | -1.35 to 0.543 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.000429 to 0.0005 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,277 | 2,326 | +2.2% | -139 to 238 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,615 | 3,604 | -0.3% | -371 to 349 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 10.7 | 10.6 | -0.2% | -0.0284 to -0.00493 | GAIN |
| end-to-end latency, mean (ms) | 308 | 313 | +1.7% | -19.1 to 29.4 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 694 | 699 | +0.7% | -35.9 to 45.9 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 56.8 | 58.1 | +2.2% | -4.21 to 6.69 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.254 | 0.253 | -0.2% | -0.00421 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 455 | 454 | -0.2% | -7.7 to 5.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 6.84 | 6.85 | +0.1% | -0.131 to 0.141 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1934 messages a second; base rate 290.2/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 728 | 727 | -0.2% | -1.96 to -0.658 | LOSS |
| throughput (messages a second consumed) | 851 | 851 | -0.0% | -0.015 to 0.00602 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,270 | 2,263 | -0.3% | -165 to 149 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,579 | 3,693 | +3.2% | 78.7 to 149 | LOSS |
| end-to-end latency, median (ms) | 7.61 | 7.6 | -0.2% | -0.214 to 0.182 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 302 | 306 | +1.1% | -3.33 to 9.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,199 | 3,250 | +1.6% | 11 to 91 | LOSS |
| consumer lag, mean messages waiting | 263 | 265 | +0.8% | -2.73 to 6.82 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.12 | +6.1% | -0.433 to 0.678 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.339 | 0.337 | -0.6% | -0.0147 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 602 | 598 | -0.6% | -25.9 to 18.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.84 | 1.83 | -0.4% | -0.0775 to 0.0617 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 978 messages a second; base rate 146.7/s; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -3.28 to 3.61 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 430 | 430 | -0.0% | -0.00499 to -0.000929 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,474 | 2,448 | -1.1% | -355 to 301 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,904 | 3,908 | +0.1% | -418 to 427 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 8.54 | 8.59 | +0.5% | -0.369 to 0.459 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 336 | 333 | -0.9% | -45.8 to 39.9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,745 | 1,730 | -0.8% | -203 to 174 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 149 | 147 | -1.2% | -19.6 to 16.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.307 | 0.318 | +3.4% | -0.036 to 0.057 | EVEN, no difference beyond the noise |
| host CPU-seconds | 533 | 554 | +3.8% | -62 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.24 | 3.36 | +3.7% | -0.407 to 0.648 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
