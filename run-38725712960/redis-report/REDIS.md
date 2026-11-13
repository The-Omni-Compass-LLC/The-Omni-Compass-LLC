# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,321 | +4.3% | -21.4 to 129 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00119 to 0.00296 | EVEN, the same |
| cache hit rate | 0.845 | 0.881 | +4.3% | -0.0141 to 0.0862 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.2% | -0.0519 to 0.0249 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.1% | -0.0339 to 0.0249 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.851 | -19.0% | -0.486 to 0.0874 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 69.5 | +8.5% | -6.02 to 16.9 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 65 | +6.0% | -4.89 to 12.3 | EVEN, no difference beyond the noise |
| keys evicted | 103,448 | 79,612 | -23.0% | -57,655 to 9,985 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.11 | -4.9% | -0.0669 to 0.0557 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 184 | -5.0% | -125 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.31 | -8.7% | -0.232 to 0.173 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 32.7 |  | 9.58 to 55.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.1% | -3 to 0.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0195 to 0.0116 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.1% | -0.00184 to 0.000207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | -0.00309 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.00827 to 0.0396 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.4% | -0.00341 to 0.0221 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.8% | 0.435 to 1.85 | power given |
| memory used, mean (MB) | 60.7 | 60.7 | -0.1% | -0.782 to 0.688 | EVEN, no difference beyond the noise |
| keys evicted | 243,174 | 245,909 | +1.1% | -1,271 to 6,742 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.141 | +1.6% | -0.00758 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 236 | +1.7% | -15.3 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.557 | 0.568 | +1.8% | -0.0362 to 0.0566 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25 |  | 22.5 to 27.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,185 | 1,253 | +5.8% | 44.4 to 92.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00286 to 0.00405 | EVEN, the same |
| cache hit rate | 0.79 | 0.836 | +5.8% | 0.0296 to 0.0618 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.56 | -0.5% | -0.0368 to -0.0196 | GAIN |
| latency, 99th percentile (ms) | 5.67 | 5.66 | -0.2% | -0.0159 to -0.00544 | GAIN |
| latency, mean (ms) | 1.25 | 1 | -19.8% | -0.327 to -0.17 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 85.1 | +33.0% | 10 to 32.2 | power given |
| memory used, mean (MB) | 61.2 | 77.1 | +26.0% | 7.13 to 24.7 | power given |
| keys evicted | 137,847 | 108,674 | -21.2% | -38,921 to -19,426 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.0969 | -10.0% | -0.0456 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 172 | -10.5% | -88.2 to 47.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.305 | -15.4% | -0.173 to 0.0616 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 44.7 |  | 28.1 to 61.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
