# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.35 to 0.464 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00513 to 0.0203 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00159 to 0.000357 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.00628 to 0.00506 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.00621 to 0.0126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.74 | +0.3% | -0.00119 to 0.0109 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.77 to -1.22 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% | -0.874 to -0.297 | GAIN |
| keys evicted | 71,600 | 71,793 | +0.3% | -94.3 to 480 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.128 | -11.0% | -0.0727 to 0.0408 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.1 | 85.9 | -12.5% | -56 to 31.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.506 | 0.443 | -12.4% | -0.289 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,263 | 1,283 | +1.6% | 9.34 to 30.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.231 to 0.371 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00756 to 0.018 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0118 to 0.00375 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.24 | -0.1% | -0.0278 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.892 | 0.822 | -7.8% | -0.117 to -0.0223 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.224 to 2.31 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.3% | -0.556 to 0.963 | EVEN, no difference beyond the noise |
| keys evicted | 103,620 | 95,124 | -8.2% | -11,992 to -5,000 | shown, not judged |
| host CPU busy (share of the run) | 0.0565 | 0.0543 | -4.0% | -0.0383 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.4 | 95.7 | -3.8% | -71.4 to 64 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.175 | 0.166 | -5.3% | -0.126 to 0.107 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 21.2 to 24.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 9.86 to 14.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0338 to 0.02 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00759 to 0.00871 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0129 to 0.00953 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.29 | -0.4% | -0.171 to 0.132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.01 | -2.1% | -0.0651 to -0.0231 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.45 to 1.73 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.25 to 1.37 | power given |
| keys evicted | 243,333 | 234,692 | -3.6% | -9,091 to -8,191 | shown, not judged |
| host CPU busy (share of the run) | 0.0617 | 0.0546 | -11.4% | -0.0407 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 95.4 | -12.1% | -76 to 49.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.261 | 0.226 | -13.3% | -0.185 to 0.116 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.9% | 4.58 to 16.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00394 to 0.00525 | EVEN, the same |
| cache hit rate | 0.79 | 0.796 | +0.9% | 0.00319 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.00866 to 0.00546 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | 0.00153 to 0.012 | LOSS |
| latency, mean (ms) | 1.34 | 1.31 | -2.6% | -0.0558 to -0.0151 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.661 to 2.17 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | 0.699 to 1.35 | power given |
| keys evicted | 138,022 | 134,169 | -2.8% | -6,372 to -1,334 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.12 | -3.5% | -0.0195 to 0.0108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 200 | -4.0% | -36.6 to 20.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.39 | 0.371 | -4.8% | -0.0719 to 0.0345 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
