# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.52 to 0.597 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00781 to 0.00978 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00104 to 0.000445 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.65 | 5.64 | -0.1% | -0.0238 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.0255 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.65 | 1.64 | -0.1% | -0.0131 to 0.00912 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.81 to -1.73 | GAIN |
| memory used, mean (MB) | 57.2 | 55.4 | -3.1% | -2.99 to -0.534 | GAIN |
| keys evicted | 71,722 | 71,800 | +0.1% | -115 to 271 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.114 | +6.5% | 0.00241 to 0.0115 | power given |
| host CPU-seconds | 75.3 | 81 | +7.6% | 1.86 to 9.6 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.418 | +7.7% | 0.00951 to 0.05 | power given |
| ceiling changes written (the knob's moves) | 0 | 9.67 |  | 8.23 to 11.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,331 | +5.1% | 2.68 to 125 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00224 to 0.00248 | EVEN, the same |
| cache hit rate | 0.845 | 0.888 | +5.0% | 0.00203 to 0.0832 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.3% | -0.0365 to -0.000294 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0295 to 0.0175 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.817 | -22.5% | -0.465 to -0.00838 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71 | +11.0% | -1.7 to 15.7 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 66 | +7.6% | -1.87 to 11.2 | EVEN, no difference beyond the noise |
| keys evicted | 103,336 | 75,073 | -27.4% | -55,502 to -1,023 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.112 | -3.2% | -0.042 to 0.0346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 188 | -2.9% | -79.3 to 67.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.315 | -7.6% | -0.161 to 0.109 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36 |  | 27 to 45 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 924 | -0.0% | -12 to 11.7 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0253 to -0.0027 | LOSS |
| cache hit rate | 0.617 | 0.617 | -0.0% | -0.00764 to 0.00732 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.00279 to 0.00256 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.3 | +0.7% | -0.183 to 0.257 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.05 | +0.0% | -0.0501 to 0.0519 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71.2 | +11.3% | 3.57 to 10.9 | power given |
| memory used, mean (MB) | 60.7 | 65 | +7.1% | 3.23 to 5.4 | power given |
| keys evicted | 243,289 | 247,142 | +1.6% | -6,721 to 14,427 | shown, not judged |
| host CPU busy (share of the run) | 0.0559 | 0.0543 | -2.9% | -0.0518 to 0.0486 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.1 | 95.4 | -2.8% | -96.1 to 90.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.236 | 0.23 | -2.7% | -0.233 to 0.22 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27 |  | 19.5 to 34.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,248 | +5.4% | 39.2 to 88.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00314 to 0.00638 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.832 | +5.4% | 0.0262 to 0.0589 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.013 to -0.00279 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.00237 to 0.00318 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.12 | -17.4% | -0.328 to -0.142 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 83.8 | +31.0% | 0.815 to 38.9 | power given |
| memory used, mean (MB) | 61.2 | 76.5 | +25.0% | 2.56 to 28 | power given |
| keys evicted | 138,187 | 110,015 | -20.4% | -42,237 to -14,106 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.11 | -3.0% | -0.0276 to 0.0209 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 182 | -2.6% | -50.7 to 41.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.351 | 0.325 | -7.6% | -0.104 to 0.0509 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 43.3 |  | 8.43 to 78.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
