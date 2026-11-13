# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
