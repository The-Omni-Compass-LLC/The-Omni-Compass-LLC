# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.43 to 1.04 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0625 to 0.0405 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00146 to 0.000419 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0116 to 0.00166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.95 | 5.86 | -1.4% | -0.5 to 0.329 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.76 | 1.76 | +0.1% | -0.0194 to 0.0223 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.6 | -3.8% | -5.8 to 0.914 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.4 | -3.0% | -4.24 to 0.769 | EVEN, no difference beyond the noise |
| keys evicted | 71,703 | 71,848 | +0.2% | -131 to 420 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.142 | +9.9% | -0.00562 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.4 | 95.5 | +11.8% | -3.46 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.441 | 0.493 | +11.8% | -0.0182 to 0.123 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,324 | +4.5% | 24.5 to 90.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00337 to 0.00297 | EVEN, the same |
| cache hit rate | 0.845 | 0.883 | +4.5% | 0.0165 to 0.0602 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.3% | -0.0444 to 0.0147 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0319 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.842 | -20.1% | -0.34 to -0.0832 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 69.3 | +8.4% | -0.93 to 11.6 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 65.3 | +6.6% | -0.521 to 8.61 | EVEN, no difference beyond the noise |
| keys evicted | 103,587 | 78,139 | -24.6% | -40,305 to -10,590 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.109 | -9.7% | -0.0442 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 182 | -10.1% | -82.7 to 42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.305 | -14.0% | -0.157 to 0.058 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36 |  | 22.9 to 49.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -3.15 to 0.000696 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0177 to 0.00917 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00205 to 7.52e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.0% | -0.0145 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.00265 to 0.0254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.28 | +0.4% | -0.00647 to 0.0234 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | -1.14 to 3.78 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.7 | -0.1% | -0.57 to 0.506 | EVEN, no difference beyond the noise |
| keys evicted | 243,138 | 244,398 | +0.5% | -336 to 2,857 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.152 | +9.3% | -0.0178 to 0.0437 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 257 | +10.9% | -35.2 to 85.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.557 | 0.618 | +11.1% | -0.0838 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 13.9 to 31.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,233 | +4.1% | -2.61 to 100 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00753 to 0.00501 | EVEN, the same |
| cache hit rate | 0.789 | 0.822 | +4.1% | -0.00159 to 0.067 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.0106 to 0.00198 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | +0.1% | -0.00316 to 0.00902 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.16 | -13.2% | -0.367 to 0.0148 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.3 | +19.3% | -4.52 to 29.2 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 70.4 | +15.0% | -1.44 to 19.8 | EVEN, no difference beyond the noise |
| keys evicted | 138,178 | 118,310 | -14.4% | -41,832 to 2,096 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.107 | -4.0% | -0.0427 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 177 | -3.8% | -79.1 to 65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.32 | -7.6% | -0.148 to 0.0957 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 34 |  | 16.8 to 51.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
