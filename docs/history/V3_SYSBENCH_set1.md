# sysbench on MySQL, the first counted set (superseded by the second set on the amended plug): the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Why this table is in the history.** This is the first counted set of the MySQL benchmark (runs 37757840760, 37757850988,
> 37757861572, commit `23f6ca4c`, Omni v3, 2026-10-08), kept whole, every row as it was published. Its hand-back row read NO on
> four of five workloads because the plug's restore was issued while the server was still carrying out a shrink the law had asked
> for, which MySQL ignores (`docs/MYSQL_PREREGISTRATION.md`, the first set's result and the amendment). The plug was fixed and the
> second counted set (A2, B2, C2) run on it; that table is the one in `results/live/V3_SYSBENCH.md` and the one the index reads.
> The engine was the same in both sets. Nothing here was changed after publication.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37757840760 | `23f6ca4cf9c8` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 37757850988 | `23f6ca4cf9c8` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 37757861572 | `23f6ca4cf9c8` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,916 | 2,917 | +0.0% (-0.4 to +0.4) | -0.0% (-0.4 to +0.3) | +0.0% (-0.3 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,928 | 2,929 | +0.0% (-0.4 to +0.4) | -0.0% (-0.4 to +0.3) | +0.1% (-0.3 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,928 | 2,929 | +0.0% (-0.4 to +0.4) | -0.0% (-0.4 to +0.3) | +0.1% (-0.3 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.386 | 0.388 | +0.6% (-2.0 to +3.2) | +0.0% (-9.3 to +9.3) | +0.6% (-4.4 to +5.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.505 | 0.496 | -1.8% (-6.2 to +2.6) | -0.6% (-11.8 to +10.5) | +1.1% (-1.3 to +3.6) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.225 | 0.227 | +1.2% (-5.3 to +7.8) | +0.8% (-7.0 to +8.5) | +4.1% (-0.5 to +8.7) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 361.8 | -29.3% (-107.9 to +49.3) | -14.6% (-77.7 to +48.6) | +25.2% (-19.3 to +69.6) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 462.3 | 337.1 | -27.1% (-107.7 to +53.5) | -13.8% (-77.3 to +49.7) | +22.1% (-6.4 to +50.7) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 262,404 | 396,278 | +51.0% (-91.5 to +193.5) | +28.3% (-83.0 to +139.6) | -21.4% (-104.6 to +61.8) | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.127 | +0.9% (-1.3 to +3.0) | +1.9% (-12.8 to +16.7) | +0.3% (-6.7 to +7.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 140.4 | 141.7 | +1.0% (-0.8 to +2.8) | +2.2% (-12.9 to +17.2) | +0.4% (-6.3 to +7.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.158 | +0.9% (-0.5 to +2.3) | +2.2% (-12.8 to +17.2) | +0.4% (-6.5 to +7.2) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 | +7.67 (-2.37 to +17.7) | +7.33 (+1.08 to +13.6) | +15.7 (+11.9 to +19.5) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: **NO** (2 of 9 omni arms not handed back).

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.4 | 293.8 | +0.5% (-1.3 to +2.3) | +0.7% (-2.7 to +4.1) | +0.1% (-0.9 to +1.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 292.7 | 294.3 | +0.5% (-1.2 to +2.2) | +0.6% (-2.9 to +4.2) | +0.2% (-0.8 to +1.1) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,684 | 4,708 | +0.5% (-1.2 to +2.2) | +0.6% (-2.9 to +4.2) | +0.2% (-0.8 to +1.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.7 | 3.66 | -1.2% (-14.0 to +11.6) | -0.6% (-7.4 to +6.2) | +1.2% (-5.6 to +8.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.09 | 5.09 | +0.0% (-7.8 to +7.8) | -0.6% (-3.1 to +1.9) | +0.6% (-4.5 to +5.8) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.63 | 1.61 | -1.5% (-8.8 to +5.8) | +1.0% (-0.8 to +2.8) | +0.7% (-2.1 to +3.5) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 282.5 | -44.8% (-156.9 to +67.3) | -53.9% (-126.9 to +19.1) | -70.8% (-71.0 to -70.7) | no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 438.7 | 253.3 | -42.3% (-157.7 to +73.2) | -54.4% (-118.1 to +9.3) | -69.5% (-74.8 to -64.3) | no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 168,778 | 278,789 | +65.2% (-91.9 to +222.2) | +74.0% (-60.1 to +208.2) | +103.5% (+95.5 to +111.6) | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.117 | -2.4% (-8.8 to +4.1) | +3.8% (-1.8 to +9.4) | +2.0% (-0.1 to +4.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 48.5 | 47.4 | -2.4% (-8.8 to +4.0) | +4.3% (-1.4 to +10.0) | +2.4% (-0.2 to +5.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.62 | 1.58 | -2.8% (-9.2 to +3.6) | +3.5% (+1.4 to +5.7) | +2.3% (-1.1 to +5.8) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 | +4.67 (-2.5 to +11.8) | +5 (-3.61 to +13.6) | +3 (+3 to +3) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: **NO** (7 of 9 omni arms not handed back).

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.0 | 291.9 | -0.4% (-1.4 to +0.7) | +0.4% (-1.7 to +2.5) | -0.2% (-1.8 to +1.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 293.0 | 292.3 | -0.2% (-1.3 to +0.8) | +0.4% (-1.7 to +2.5) | -0.2% (-1.7 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,688 | 4,677 | -0.2% (-1.3 to +0.8) | +0.4% (-1.7 to +2.5) | -0.2% (-1.7 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.66 | 3.7 | +1.2% (-1.4 to +3.8) | +1.2% (-1.4 to +3.8) | +3.0% (-2.1 to +8.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 4.94 | 5.09 | +3.1% (+0.4 to +5.8) | +0.6% (-4.6 to +5.8) | +4.3% (-0.9 to +9.4) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 2.72 | 2.77 | +1.5% (-0.8 to +3.9) | +1.1% (-1.9 to +4.1) | +1.7% (+1.2 to +2.2) | no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 493.0 | -3.7% (-105.7 to +98.3) | -27.3% (-99.2 to +44.7) | -36.3% (-105.7 to +33.2) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.8 | 405.2 | -12.2% (-100.8 to +76.3) | -26.6% (-97.0 to +43.8) | -37.4% (-98.7 to +23.9) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 458,003 | 782,316 | +70.8% (+31.7 to +110.0) | +82.6% (-30.7 to +195.8) | +92.8% (+21.3 to +164.3) | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.222 | +1.0% (-0.9 to +2.9) | +2.9% (-7.0 to +12.7) | +3.0% (+1.6 to +4.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 264.7 | 267.2 | +0.9% (-1.0 to +2.9) | +3.2% (-7.1 to +13.5) | +3.5% (+1.9 to +5.1) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.98 | +1.3% (-1.6 to +4.2) | +2.8% (-5.3 to +11.0) | +3.7% (+0.8 to +6.6) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 | +15.3 (+7.35 to +23.3) | +15.7 (-0.497 to +31.8) | +13.7 (+3.32 to +24) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: **NO** (4 of 9 omni arms not handed back).

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191.2 | 193.5 | +1.2% (-1.7 to +4.1) | +1.3% (-1.1 to +3.8) | +1.4% (-0.3 to +3.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 194.3 | 195.9 | +0.8% (-0.2 to +1.9) | -0.1% (-2.0 to +1.8) | -0.6% (-1.7 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,886 | 3,918 | +0.8% (-0.2 to +1.9) | -0.1% (-2.0 to +1.8) | -0.6% (-1.7 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 7.94 | 7.56 | -4.8% (-28.7 to +19.1) | -11.5% (-33.9 to +10.8) | -14.4% (-19.1 to -9.8) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 11.7 | 10.7 | -9.0% (-41.1 to +23.1) | -12.9% (-38.3 to +12.5) | -15.5% (-38.3 to +7.3) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 5.08 | 4.99 | -1.9% (-10.0 to +6.3) | -4.6% (-10.7 to +1.5) | -6.5% (-19.6 to +6.5) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 708.1 | +38.3% (-84.0 to +160.6) | +56.8% (-19.5 to +133.1) | +84.1% (+15.8 to +152.3) | no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 460.8 | 610.5 | +32.5% (-68.2 to +133.1) | +53.8% (-22.3 to +130.0) | +73.0% (+26.2 to +119.7) | no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 431,242 | 318,781 | -26.1% (-137.7 to +85.5) | -42.2% (-110.0 to +25.7) | -55.5% (-83.7 to -27.3) | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.204 | -2.5% (-16.5 to +11.5) | -6.3% (-17.4 to +4.8) | -6.9% (-13.8 to -0.1) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 226.3 | 220.6 | -2.5% (-16.6 to +11.5) | -6.4% (-17.6 to +4.9) | -7.0% (-13.5 to -0.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 3.85 | 3.71 | -3.6% (-20.0 to +12.7) | -7.5% (-20.8 to +5.8) | -8.3% (-13.4 to -3.1) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 | +19.7 (+7.41 to +31.9) | +24.7 (+18.9 to +30.4) | +26.3 (+24.9 to +27.8) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.38 | 2.28 | +65.2% (-103.7 to +234.1) | -22.7% (-131.3 to +85.9) | -0.1% (-74.8 to +74.6) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 974.8 | 975.7 | +0.1% (-0.6 to +0.8) | +0.0% (-0.3 to +0.3) | +0.2% (-1.7 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 974.8 | 975.7 | +0.1% (-0.6 to +0.8) | +0.0% (-0.3 to +0.3) | +0.2% (-1.7 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 1.8 | 1.84 | +2.3% (-28.8 to +33.4) | +7.8% (-17.5 to +33.2) | -22.7% (-278.5 to +233.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 2.96 | 3.19 | +8.1% (-29.4 to +45.5) | +8.1% (-2.3 to +18.4) | -15.0% (-298.0 to +268.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.11 | 1.12 | +1.0% (-14.7 to +16.6) | +2.5% (-10.3 to +15.3) | -15.6% (-234.2 to +203.1) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 614.7 | +20.0% (-31.6 to +71.7) | +6.9% (-15.6 to +29.4) | +28.8% (+4.2 to +53.4) | no difference beyond the noise (2 of 3 runs) |
| pages holding data, mean (MB) | 449.5 | 500.3 | +11.3% (-23.3 to +46.0) | -1.9% (-16.6 to +12.7) | +11.8% (-2.5 to +26.1) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 138,795 | 123,169 | -11.3% (-29.0 to +6.5) | +6.2% (-24.8 to +37.1) | -3.5% (-16.9 to +9.8) | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.181 | +19.7% (-88.1 to +127.5) | +25.5% (-37.6 to +88.5) | +1.7% (-7.7 to +11.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 156.2 | 187.6 | +20.1% (-88.8 to +129.0) | +25.7% (-37.8 to +89.2) | +1.7% (-8.4 to +11.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 441.1 | 275.8 | -37.5% (-221.4 to +146.4) | +20.8% (-111.7 to +153.2) | -7.5% (-108.5 to +93.6) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 | +25.7 (+16.9 to +34.4) | +24.3 (+14.9 to +33.7) | +22.3 (+18.5 to +26.1) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: **NO** (2 of 9 omni arms not handed back).

**Across 4 untouched workloads: 0 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
