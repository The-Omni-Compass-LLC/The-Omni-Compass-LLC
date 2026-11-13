# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -1.73 to 1.14 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0547 to 0.0265 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000667 to 1.99e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0062 to 0.0114 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.31 | +0.7% | -0.0459 to 0.122 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.54 | +0.1% | -0.00134 to 0.00494 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61 | -4.7% | -4 to -2.01 | GAIN |
| memory used, mean (MB) | 57.1 | 55.1 | -3.6% | -2.93 to -1.19 | GAIN |
| keys evicted | 71,676 | 71,763 | +0.1% | 20.8 to 153 | shown, not judged |
| host CPU busy (share of the run) | 0.079 | 0.0789 | -0.1% | -0.0389 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 56.7 | 56.4 | -0.5% | -30.9 to 30.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.293 | 0.292 | -0.4% | -0.159 to 0.157 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,349 | +6.5% | 35.9 to 129 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00112 to 0.00175 | EVEN, the same |
| cache hit rate | 0.845 | 0.9 | +6.5% | 0.0242 to 0.0856 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.0% | -0.111 to -0.000583 | GAIN |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0512 to 0.00986 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.96 | 0.666 | -30.6% | -0.464 to -0.123 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 75.2 | +17.4% | 0.957 to 21.4 | power given |
| memory used, mean (MB) | 61.3 | 69.1 | +12.7% | 2.05 to 13.5 | power given |
| keys evicted | 103,336 | 66,796 | -35.4% | -57,182 to -15,897 | shown, not judged |
| host CPU busy (share of the run) | 0.0985 | 0.0962 | -2.4% | -0.0203 to 0.0156 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 169 | -2.1% | -37.7 to 30.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.303 | 0.278 | -8.1% | -0.0899 to 0.0411 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 37.7 |  | 8.87 to 66.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -3.28 to -0.637 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0481 to 0.0156 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.616 | -0.2% | -0.00196 to -0.00055 | LOSS |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0192 to 0.0175 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | -0.0158 to 0.0371 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.27 | +0.3% | -0.0115 to 0.0263 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.536 to 1.2 | power given |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.107 to 0.123 | power given |
| keys evicted | 243,039 | 243,940 | +0.4% | 417 to 1,384 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.15 | +4.6% | -0.0179 to 0.0312 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 253 | +5.4% | -34.2 to 60.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.576 | 0.608 | +5.6% | -0.0815 to 0.146 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 19.5 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,236 | +4.5% | -5.11 to 112 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0365 to 0.0556 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.825 | +4.6% | -0.00438 to 0.0763 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.0% | -0.0132 to 0.00921 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.0476 to 0.0457 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 0.985 | -15.6% | -0.37 to 0.00505 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.6 | +22.8% | -7.71 to 36.9 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 73.1 | +19.5% | -5.81 to 29.7 | EVEN, no difference beyond the noise |
| keys evicted | 138,173 | 115,008 | -16.8% | -51,523 to 5,193 | shown, not judged |
| host CPU busy (share of the run) | 0.0541 | 0.0471 | -13.0% | -0.0332 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.9 | 82.1 | -13.5% | -60.5 to 34.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.148 | -17.1% | -0.118 to 0.0573 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 40 |  | 8.97 to 71 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
