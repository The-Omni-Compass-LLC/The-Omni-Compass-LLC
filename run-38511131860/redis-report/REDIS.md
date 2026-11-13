# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,068 | 1,068 | -0.0% | -4 to 3.68 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.296 to 0.198 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000644 to 0.00023 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.15 | 5.88 | -4.3% | -1.44 to 0.908 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9 | 8.64 | -4.1% | -2.25 to 1.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.88 | 1.84 | -1.9% | -0.212 to 0.139 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.7 | -5.1% | -4.23 to -2.35 | GAIN |
| memory used, mean (MB) | 57.2 | 54.8 | -4.2% | -3.39 to -1.36 | GAIN |
| keys evicted | 71,988 | 72,037 | +0.1% | -92.5 to 191 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.15 | +2.9% | -0.0319 to 0.0404 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 107 | +4.5% | -24.2 to 33.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.533 | 0.557 | +4.5% | -0.127 to 0.175 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,332 | +5.1% | -10.7 to 140 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0059 to 0.00287 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.888 | +5.1% | -0.00731 to 0.0937 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.71 | -0.2% | -0.042 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | -0.0% | -0.0268 to 0.0219 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.812 | -22.4% | -0.52 to 0.05 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 71.1 | +11.1% | 0.579 to 13.6 | power given |
| memory used, mean (MB) | 61.3 | 66.1 | +7.9% | -1.99 to 11.7 | EVEN, no difference beyond the noise |
| keys evicted | 103,471 | 74,806 | -27.7% | -62,176 to 4,846 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.109 | +4.8% | -0.0195 to 0.0295 | EVEN, no difference beyond the noise |
| host CPU-seconds | 172 | 183 | +6.3% | -33.7 to 55.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.302 | 0.306 | +1.3% | -0.0869 to 0.0949 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 37.7 |  | 23.5 to 51.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -1.97 to -0.956 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0198 to 0.00296 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00122 to -0.000689 | LOSS |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.1% | -0.0041 to 0.0114 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.0018 to 0.019 | LOSS |
| latency, mean (ms) | 2.26 | 2.27 | +0.3% | 0.00197 to 0.0134 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | 0.318 to 1.1 | power given |
| memory used, mean (MB) | 60.7 | 60.6 | -0.1% | -0.813 to 0.678 | EVEN, no difference beyond the noise |
| keys evicted | 243,133 | 244,891 | +0.7% | -2,738 to 6,254 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.135 | -5.9% | -0.0597 to 0.0428 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 226 | -6.7% | -116 to 83.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.582 | 0.544 | -6.6% | -0.279 to 0.202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.3 |  | 14 to 34.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,179 | 1,230 | +4.3% | -6.51 to 107 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00729 to 0.00106 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.822 | +4.2% | -0.00457 to 0.0709 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.84 | 5.79 | -0.8% | -0.159 to 0.0631 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.55 | 7.59 | -11.3% | -1.54 to -0.38 | GAIN |
| latency, mean (ms) | 1.46 | 1.25 | -14.5% | -0.397 to -0.026 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.4 | +19.4% | -6.75 to 31.6 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 71.3 | +16.6% | -5.71 to 26 | EVEN, no difference beyond the noise |
| keys evicted | 138,452 | 117,445 | -15.2% | -46,681 to 4,668 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.126 | -14.1% | -0.0459 to 0.00445 | EVEN, no difference beyond the noise |
| host CPU-seconds | 247 | 208 | -15.9% | -88.1 to 9.77 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.466 | 0.376 | -19.2% | -0.166 to -0.0128 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29.7 |  | 12.2 to 47.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
