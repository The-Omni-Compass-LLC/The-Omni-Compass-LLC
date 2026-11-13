# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,685 | 5,676 | -0.2% | -31 to 13.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,702 | 5,693 | -0.2% | -31.1 to 13.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.446 | 0.445 | -0.2% | -0.00757 to 0.00557 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.659 | -0.5% | -0.0138 to 0.00783 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.258 | -0.3% | -0.00618 to 0.00476 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -80.6 to -55.9 | GAIN |
| bytes in the cache, mean (MB) | 417 | 365 | -12.6% | -61.5 to -43.5 | GAIN |
| pages read into the cache (misses) | 676,627 | 787,410 | +16.4% | 70,543 to 151,023 | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.3% | -0.00666 to 0.00856 | EVEN, no difference beyond the noise |
| host CPU-seconds | 478 | 481 | +0.7% | -11.7 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.182 | +0.7% | -0.00352 to 0.00615 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
