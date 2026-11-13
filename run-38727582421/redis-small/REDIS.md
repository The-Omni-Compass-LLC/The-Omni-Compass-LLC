# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
