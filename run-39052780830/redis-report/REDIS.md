# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,075 | -0.1% | -1.97 to -0.164 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0197 to 0.0278 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00115 to -5.62e-05 | LOSS |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0162 to 0.0156 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.00386 to 0.0232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | 0.00611 to 0.0123 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.1% | -2.2 to -0.527 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.8% | -1.22 to 0.249 | EVEN, no difference beyond the noise |
| keys evicted | 71,687 | 71,866 | +0.3% | 9.42 to 350 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.121 | -12.7% | -0.0826 to 0.0476 | EVEN, no difference beyond the noise |
| host CPU-seconds | 92.9 | 79.2 | -14.7% | -63.1 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.479 | 0.409 | -14.7% | -0.325 to 0.184 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 5.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 10.4 to 24.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00113 to 0.00297 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00706 to 0.0164 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0139 to 0.0096 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.00918 to 0.00996 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.988 | -5.9% | -0.0878 to -0.0366 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.3% | 0.0871 to 1.62 | power given |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | 0.187 to 1.02 | power given |
| keys evicted | 103,335 | 95,663 | -7.4% | -10,807 to -4,535 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.114 | +0.0% | -0.033 to 0.0331 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 191 | +0.2% | -62 to 62.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.331 | -1.2% | -0.11 to 0.102 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 9.88 to 14.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0182 to 0.00505 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00667 to 0.00944 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | -0.0029 to 0.011 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.00385 to 0.0312 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0498 to -0.0274 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.19 to 1.98 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.987 to 1.38 | power given |
| keys evicted | 243,130 | 237,761 | -2.2% | -12,635 to 1,897 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.141 | +3.5% | -0.0298 to 0.0393 | EVEN, no difference beyond the noise |
| host CPU-seconds | 227 | 236 | +4.0% | -58.4 to 76.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.544 | 0.559 | +2.7% | -0.145 to 0.174 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 10.7 to 17.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0253 to 0.0658 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00749 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.0109 to 0.00125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.1% | -0.0555 to 0.0473 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -4.6% | -0.0732 to -0.0336 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.22 to 2.12 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 1.02 to 1.42 | power given |
| keys evicted | 138,226 | 132,920 | -3.8% | -6,401 to -4,211 | shown, not judged |
| host CPU busy (share of the run) | 0.0688 | 0.0596 | -13.3% | -0.0843 to 0.066 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 106 | -13.9% | -159 to 125 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.231 | 0.197 | -14.9% | -0.301 to 0.232 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
