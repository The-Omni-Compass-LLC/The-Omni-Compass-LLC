# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## burst: 2.0 ms of work a message, 256 B, steps 1 6 1 8 1 6 × 30.0 s

Native capacity 976 messages a second; base rate 109.8/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 341 | 340 | -0.3% | -1.55 to -0.163 | **WORSE** |
| throughput (messages a second consumed) | 419 | 419 | -0.0% | -0.0158 to 0.0154 | same |
| end-to-end latency, 95th percentile (ms) | 2,528 | 2,596 | +2.7% | -127 to 264 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,672 | 3,640 | -0.9% | -406 to 342 | no difference beyond the noise |
| end-to-end latency, median (ms) | 9.16 | 8.94 | -2.4% | -0.914 to 0.478 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 382 | 385 | +0.7% | -3.13 to 8.24 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,672 | 1,663 | -0.5% | -40.1 to 22.1 | no difference beyond the noise |
| consumer lag, mean messages waiting | 165 | 165 | +0.0% | -4.51 to 4.61 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% | -0.0167 to -0.0164 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.304 | 0.301 | -1.1% | -0.0189 to 0.0123 | no difference beyond the noise |
| host CPU-seconds | 218 | 215 | -1.1% | -13.4 to 8.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.54 | 3.51 | -0.8% | -0.215 to 0.158 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1930 messages a second; base rate 289.5/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 736 | 732 | -0.5% | -17.2 to 9.99 | no difference beyond the noise |
| throughput (messages a second consumed) | 849 | 849 | -0.0% | -0.0181 to 0.0106 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 1,940 | 1,981 | +2.1% | -244 to 326 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,133 | 3,255 | +3.9% | -456 to 701 | no difference beyond the noise |
| end-to-end latency, median (ms) | 12.9 | 10.1 | -21.4% | -13 to 7.44 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 264 | 266 | +0.8% | -23.4 to 27.5 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 2,952 | 2,953 | +0.0% | -296 to 298 | no difference beyond the noise |
| consumer lag, mean messages waiting | 231 | 232 | +0.4% | -15.7 to 17.4 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.278 | 0.31 | +11.5% | -0.0392 to 0.103 | no difference beyond the noise |
| host CPU-seconds | 497 | 553 | +11.3% | -67.6 to 180 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.5 | 1.68 | +11.9% | -0.225 to 0.582 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

## tuning: 2.0 ms of work a message, 256 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Native capacity 975 messages a second; base rate 146.3/s; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365 | 365 | -0.1% | -2.65 to 1.71 | no difference beyond the noise |
| throughput (messages a second consumed) | 429 | 429 | +0.0% | -0.0238 to 0.0291 | no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,364 | 2,403 | +1.7% | -99.9 to 178 | no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,761 | 3,746 | -0.4% | -205 to 175 | no difference beyond the noise |
| end-to-end latency, median (ms) | 8.63 | 8.62 | -0.0% | -0.0512 to 0.0432 | no difference beyond the noise |
| end-to-end latency, mean (ms) | 320 | 325 | +1.4% | -12.2 to 21 | no difference beyond the noise |
| consumer lag, most messages waiting at once | 1,686 | 1,702 | +1.0% | -95.7 to 128 | no difference beyond the noise |
| consumer lag, mean messages waiting | 142 | 144 | +1.4% | -5.2 to 9.09 | no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00667 to -0.00663 | better |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | same |
| host CPU busy (share of the run) | 0.317 | 0.315 | -0.8% | -0.0101 to 0.0052 | no difference beyond the noise |
| host CPU-seconds | 551 | 547 | -0.7% | -15.9 to 8.56 | no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.33 | -0.5% | -0.112 to 0.0764 | no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
