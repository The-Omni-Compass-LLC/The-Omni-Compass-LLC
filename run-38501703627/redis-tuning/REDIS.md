# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 58.7 to 81.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00699 to 0.00736 | EVEN, the same |
| cache hit rate | 0.789 | 0.836 | +5.9% | 0.0392 to 0.0545 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.62 | -0.2% | -0.0824 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.0491 to 0.0541 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.02 | -19.7% | -0.265 to -0.236 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 88.3 | +37.9% | 16.6 to 31.9 | power given |
| memory used, mean (MB) | 61.2 | 79.6 | +30.0% | 15.7 to 21 | power given |
| keys evicted | 138,110 | 107,076 | -22.5% | -37,321 to -24,749 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.11 | +10.1% | -0.0201 to 0.0403 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 196 | +11.8% | -37.6 to 79 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.328 | 0.346 | +5.5% | -0.0849 to 0.121 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 58.3 |  | 53.2 to 63.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
