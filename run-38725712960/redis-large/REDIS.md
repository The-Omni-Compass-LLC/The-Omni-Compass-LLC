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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
