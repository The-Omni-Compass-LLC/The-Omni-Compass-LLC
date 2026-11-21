# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -3.75 to 1.77 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0213 to 0.029 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00234 to 0.00116 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.0% | -0.00565 to 0.00116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.0072 to 0.022 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.74 | +0.3% | -0.0117 to 0.021 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.8 | -3.4% | -3.8 to -0.551 | GAIN |
| memory used, mean (MB) | 57.2 | 55.9 | -2.2% | -2.99 to 0.52 | EVEN, no difference beyond the noise |
| keys evicted | 71,660 | 71,831 | +0.2% | -319 to 662 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.122 | -2.9% | -0.0608 to 0.0536 | EVEN, no difference beyond the noise |
| host CPU-seconds | 83 | 80.3 | -3.2% | -45.8 to 40.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.428 | 0.415 | -3.1% | -0.237 to 0.21 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,288 | +1.7% | 21.2 to 22.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00247 to 0.00211 | EVEN, the same |
| cache hit rate | 0.844 | 0.859 | +1.7% | 0.0139 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0193 to 0.00812 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00953 to 0.0106 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.974 | -7.6% | -0.0875 to -0.0717 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 0.486 to 2.24 | power given |
| memory used, mean (MB) | 61.3 | 62.2 | +1.5% | 0.223 to 1.62 | power given |
| keys evicted | 103,704 | 93,997 | -9.4% | -10,243 to -9,170 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.124 | +3.4% | -0.00537 to 0.0136 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 210 | +4.2% | -9.8 to 26.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.362 | +2.4% | -0.023 to 0.0402 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.1 to 14 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.129 to 0.0497 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00691 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.1% | -0.0183 to 0.0298 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.0166 to 0.0514 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.7% | -0.0585 to -0.0193 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.873 to 1.76 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.89 to 1.45 | power given |
| keys evicted | 243,177 | 236,722 | -2.7% | -14,963 to 2,054 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.14 | -3.6% | -0.0415 to 0.031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 234 | -4.4% | -80.6 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.587 | 0.554 | -5.7% | -0.201 to 0.135 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 13.9 to 16.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 8.43 to 10.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00424 to 0.0019 | EVEN, the same |
| cache hit rate | 0.79 | 0.796 | +0.8% | 0.00564 to 0.00733 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.2% | -0.00354 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | 0.00101 to 0.0393 | LOSS |
| latency, mean (ms) | 1.34 | 1.32 | -2.0% | -0.0309 to -0.0223 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 1.12 to 1.63 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.692 to 1.27 | power given |
| keys evicted | 137,970 | 134,687 | -2.4% | -5,007 to -1,558 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.128 | +8.6% | -0.015 to 0.0353 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 216 | +9.5% | -29.7 to 67.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.402 | +8.7% | -0.0584 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 13.4 to 26.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
