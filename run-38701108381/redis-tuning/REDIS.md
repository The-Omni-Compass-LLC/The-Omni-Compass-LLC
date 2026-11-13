# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,250 | +5.6% | 59.5 to 73.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00185 to 0.00692 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.834 | +5.6% | 0.0396 to 0.049 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0163 to 0.00346 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.012 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.1 | -18.1% | -0.263 to -0.226 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.4 | +35.0% | 19.7 to 25.1 | power given |
| memory used, mean (MB) | 61.2 | 79 | +29.1% | 17.4 to 18.2 | power given |
| keys evicted | 138,104 | 109,313 | -20.8% | -31,335 to -26,247 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.116 | -9.0% | -0.0425 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 194 | -9.4% | -77.4 to 37.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.401 | 0.344 | -14.2% | -0.157 to 0.0425 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 48.3 |  | 37.1 to 59.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
