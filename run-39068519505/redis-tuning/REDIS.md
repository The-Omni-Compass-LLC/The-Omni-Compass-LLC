# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
