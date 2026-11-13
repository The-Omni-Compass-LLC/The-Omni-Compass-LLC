# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
