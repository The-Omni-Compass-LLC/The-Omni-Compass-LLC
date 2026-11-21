# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,074 | -0.1% | -2.15 to 0.0548 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0765 to 0.0395 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00181 to 0.000473 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.025 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.0% | -0.0318 to 0.0341 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.53 | +0.3% | -0.00422 to 0.0137 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -2.21 to -0.544 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.9% | -1.19 to 0.203 | EVEN, no difference beyond the noise |
| keys evicted | 71,633 | 71,828 | +0.3% | -109 to 499 | shown, not judged |
| host CPU busy (share of the run) | 0.0627 | 0.0522 | -16.8% | -0.0541 to 0.0331 | EVEN, no difference beyond the noise |
| host CPU-seconds | 44.4 | 36.7 | -17.2% | -39.2 to 24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.229 | 0.19 | -17.1% | -0.202 to 0.124 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 5.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,283 | +1.5% | 11.7 to 25.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0252 to 0.0363 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00646 to 0.0187 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.2% | -0.0305 to 0.0133 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.27 | -1.1% | -0.287 to 0.167 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.9 | 0.831 | -7.6% | -0.078 to -0.0591 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | -2.22 to 4.75 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -1.58 to 2.8 | EVEN, no difference beyond the noise |
| keys evicted | 103,696 | 95,334 | -8.1% | -12,811 to -3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.0583 | 0.0621 | +6.4% | -0.0261 to 0.0335 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 109 | +7.1% | -49.7 to 64.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.179 | 0.19 | +5.6% | -0.09 to 0.11 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 19.5 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 938 | +1.3% | 11.1 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.025 to 0.00889 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00732 to 0.00923 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.0219 to 0.0302 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.77 | +0.3% | -0.0165 to 0.051 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.8% | -0.0612 to -0.0209 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.31 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.831 to 1.38 | power given |
| keys evicted | 243,204 | 238,739 | -1.8% | -13,000 to 4,068 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.151 | +0.8% | -0.0441 to 0.0463 | EVEN, no difference beyond the noise |
| host CPU-seconds | 252 | 254 | +0.9% | -85.2 to 90 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.604 | 0.602 | -0.4% | -0.212 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `a00031b9149c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.5% | -0.0773 to 11.9 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.000723 to 0.00217 | EVEN, the same |
| cache hit rate | 0.789 | 0.793 | +0.5% | -3.32e-05 to 0.00808 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.0122 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.1% | -0.00522 to 0.0208 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.4% | -0.0383 to 0.00182 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -0.348 to 1.64 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.6 | +0.7% | -0.521 to 1.35 | EVEN, no difference beyond the noise |
| keys evicted | 138,157 | 136,544 | -1.2% | -5,347 to 2,123 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.126 | +5.6% | -0.0578 to 0.0713 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 213 | +6.5% | -112 to 138 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.397 | +6.0% | -0.21 to 0.255 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18 |  | 11.4 to 24.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
