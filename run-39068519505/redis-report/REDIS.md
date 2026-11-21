# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -1.2 to 0.428 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0317 to 0.0197 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000763 to 0.000304 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.69 | +0.1% | -0.0121 to 0.0288 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | 0.00179 to 0.0244 | LOSS |
| latency, mean (ms) | 1.67 | 1.68 | +0.7% | -0.00612 to 0.0279 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.8 | -1.9% | -2.3 to -0.191 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.8% | -0.747 to -0.165 | GAIN |
| keys evicted | 71,696 | 71,772 | +0.1% | -56.6 to 208 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.127 | +15.1% | -0.0258 to 0.0591 | EVEN, no difference beyond the noise |
| host CPU-seconds | 76.9 | 89.6 | +16.5% | -20.7 to 46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.397 | 0.462 | +16.5% | -0.106 to 0.237 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,284 | +1.4% | 0.908 to 33.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0223 to 0.0136 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000907 to 0.0224 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0239 to 0.0162 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.83 | 5.83 | +0.0% | -0.0155 to 0.0177 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1 | -5.7% | -0.121 to -0.000324 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.8% | -0.434 to 2.75 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.1 | +1.4% | -0.231 to 1.89 | EVEN, no difference beyond the noise |
| keys evicted | 103,389 | 95,749 | -7.4% | -14,840 to -440 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.115 | -4.8% | -0.0114 to -0.000208 | GAIN |
| host CPU-seconds | 201 | 190 | -5.4% | -20.2 to -1.43 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.329 | -6.6% | -0.0429 to -0.00394 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 9.94 to 27.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.1 to 13.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0133 to -0.00463 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.0066 to 0.00879 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | -0.0% | -0.00858 to 0.00614 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.0% | -0.00421 to 0.00862 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.11 | -1.9% | -0.0519 to -0.0304 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 0.899 to 2.58 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.999 to 1.47 | power given |
| keys evicted | 243,164 | 235,612 | -3.1% | -10,361 to -4,741 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.108 | +1.7% | -0.0514 to 0.055 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 189 | +2.3% | -101 to 109 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.444 | 0.448 | +1.0% | -0.245 to 0.253 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 11.5 to 17.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.5% | 5.24 to 7.49 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00548 to 0.0062 | EVEN, the same |
| cache hit rate | 0.789 | 0.794 | +0.5% | 0.00374 to 0.00473 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | 0.00467 to 0.0122 | LOSS |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.3% | 0.0132 to 0.0185 | LOSS |
| latency, mean (ms) | 1.35 | 1.33 | -1.3% | -0.0284 to -0.00541 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | 0.277 to 0.695 | power given |
| memory used, mean (MB) | 61.2 | 61.4 | +0.4% | -0.0288 to 0.498 | EVEN, no difference beyond the noise |
| keys evicted | 138,155 | 136,935 | -0.9% | -1,555 to -885 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.128 | +7.0% | -0.03 to 0.0467 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 215 | +7.7% | -57.9 to 88.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.401 | +7.2% | -0.111 to 0.164 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 18.5 to 24.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
