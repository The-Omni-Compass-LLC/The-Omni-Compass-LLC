# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.8 to 0.505 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0201 to 0.0124 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00121 to 0.000388 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.58 | +0.1% | -0.011 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.66 | +0.1% | -0.00928 to 0.0191 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.63 | +0.3% | -0.00401 to 0.0149 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.69 to -1.13 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.8% | -0.701 to -0.253 | GAIN |
| keys evicted | 71,669 | 71,803 | +0.2% | -56.9 to 326 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.109 | +4.5% | -0.00492 to 0.0143 | EVEN, no difference beyond the noise |
| host CPU-seconds | 74.3 | 77.9 | +4.9% | -3.91 to 11.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.383 | 0.402 | +5.0% | -0.0197 to 0.0576 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.6% | 18.7 to 22.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00949 to 0.00543 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0126 to 0.0152 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.00371 to -0.000347 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | 0.00223 to 0.00455 | LOSS |
| latency, mean (ms) | 1.05 | 0.973 | -7.1% | -0.0804 to -0.0686 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | -0.593 to 2.76 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -0.14 to 1.34 | EVEN, no difference beyond the noise |
| keys evicted | 103,447 | 94,263 | -8.9% | -10,150 to -8,218 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.109 | -13.9% | -0.0567 to 0.0217 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 181 | -15.5% | -107 to 40.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.312 | -16.8% | -0.191 to 0.0653 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 10.9 to 12.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0298 to 0.0185 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00744 to 0.00806 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | 0.000445 to 0.00634 | LOSS |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.0102 to 0.0173 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0412 to -0.0348 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.36 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.18 to 1.25 | power given |
| keys evicted | 243,247 | 234,861 | -3.4% | -8,592 to -8,180 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.139 | -9.3% | -0.0383 to 0.00979 | EVEN, no difference beyond the noise |
| host CPU-seconds | 259 | 232 | -10.6% | -74 to 18.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.622 | 0.549 | -11.7% | -0.183 to 0.0374 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 11.7 |  | 8.8 to 14.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +0.9% | 3.63 to 18.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00193 to 0.00364 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00252 to 0.0123 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.2% | -0.0217 to -0.00216 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.1% | -0.0162 to 0.00597 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -3.1% | -0.069 to -0.0135 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -0.167 to 3.02 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -0.212 to 2.25 | EVEN, no difference beyond the noise |
| keys evicted | 138,126 | 133,934 | -3.0% | -7,503 to -881 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.123 | -1.6% | -0.0159 to 0.0119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 207 | -1.3% | -28.5 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.393 | 0.384 | -2.2% | -0.0593 to 0.042 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
