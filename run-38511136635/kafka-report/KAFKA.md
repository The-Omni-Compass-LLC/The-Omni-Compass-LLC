# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 981 messages a second; base rate 110.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 342 | 343 | +0.1% | -3.3 to 3.95 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 422 | 422 | +0.0% | -0.0182 to 0.0218 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,544 | 2,525 | -0.7% | -258 to 221 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,819 | 3,830 | +0.3% | -41 to 61.9 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 12.2 | 11.7 | -3.8% | -5.2 to 4.27 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 396 | 396 | -0.2% | -22.3 to 20.7 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,700 | 1,677 | -1.4% | -71.7 to 24.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 173 | 174 | +0.3% | -8.13 to 9.33 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.265 | 0.263 | -1.0% | -0.0229 to 0.0178 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 189 | -0.9% | -16.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.08 | 3.05 | -1.0% | -0.245 to 0.183 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 393 messages a second; base rate 58.9/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | +0.1% | -0.491 to 0.645 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | +0.0% | -0.00132 to 0.00142 | EVEN, the same |
| end-to-end latency, 95th percentile (ms) | 2,516 | 2,501 | -0.6% | -70.1 to 40 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,812 | 3,784 | -0.7% | -433 to 377 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.8 | 11.9 | +0.8% | -0.225 to 0.423 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 338 | 335 | -0.8% | -12 to 6.33 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 711 | 701 | -1.5% | -45.8 to 25.2 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 61.6 | 60.7 | -1.5% | -3.03 to 1.2 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.291 | 0.297 | +1.8% | -0.00345 to 0.0141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 514 | 524 | +1.9% | -5.84 to 25.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.77 | 7.92 | +1.9% | -0.0644 to 0.355 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1947 messages a second; base rate 292.1/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 731 | 730 | -0.1% | -0.916 to -0.277 | LOSS |
| throughput (messages a second consumed) | 857 | 857 | -0.0% | -0.0243 to 0.0108 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,378 | 2,386 | +0.3% | -58 to 72.9 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,807 | 3,702 | -2.8% | -552 to 341 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.18 | 7.05 | -1.8% | -0.25 to -0.0131 | GAIN |
| end-to-end latency, mean (ms) | 316 | 317 | +0.2% | -1.61 to 2.58 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,339 | 3,327 | -0.4% | -39.3 to 15.3 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 275 | 275 | +0.1% | -2.94 to 3.24 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2 | +0.1% | -0.0384 to 0.0443 | EVEN, no difference beyond the noise |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.32 | 0.319 | -0.2% | -0.00741 to 0.00627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 571 | 571 | +0.0% | -12.7 to 12.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.74 | 1.74 | +0.1% | -0.0367 to 0.0402 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 976 messages a second; base rate 146.4/s; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366 | 366 | +0.0% | -1.42 to 1.45 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.00208 to 0.00405 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,430 | 2,379 | -2.1% | -141 to 41 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,766 | 3,677 | -2.4% | -120 to -58.7 | GAIN |
| end-to-end latency, median (ms) | 8.52 | 8.5 | -0.2% | -0.187 to 0.15 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 325 | 320 | -1.5% | -18.8 to 9 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,709 | 1,688 | -1.2% | -68.1 to 27.4 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 144 | 142 | -1.0% | -5.82 to 2.81 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.303 | 0.301 | -0.4% | -0.0152 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 525 | 523 | -0.4% | -30.7 to 26.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.19 | 3.18 | -0.4% | -0.185 to 0.16 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
