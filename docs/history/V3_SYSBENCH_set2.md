# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Superseded on 2026-10-09.** This is the table of the second counted set (runs 37770617236, 37770620582, 37770624805, on amendment 1 of `docs/MYSQL_PREREGISTRATION.md`). Amendment 2 (the pool grows only while it is missing; no give-back in a second without a read request) followed its read_write row, and the third counted set replaced it in `results/live/V3_SYSBENCH.md`. Kept whole, every row; nothing below is current.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37770617236 | `a033fd09b6d5` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 37770620582 | `a033fd09b6d5` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 37770624805 | `a033fd09b6d5` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,906 | 2,910 | +0.1% (-0.4 to +0.6) | -0.2% (-0.7 to +0.3) | -0.2% (-0.7 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,909 | 2,912 | +0.1% (-0.4 to +0.6) | -0.1% (-0.3 to +0.1) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,909 | 2,912 | +0.1% (-0.4 to +0.6) | -0.1% (-0.3 to +0.1) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.301 | 0.303 | +0.7% (-6.1 to +7.4) | +1.9% (-2.8 to +6.6) | +6.2% (-5.2 to +17.6) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.395 | 0.381 | -3.5% (-7.9 to +0.9) | +2.5% (-4.5 to +9.5) | +3.7% (-5.5 to +12.8) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.123 | 0.125 | +1.3% (-6.8 to +9.3) | +3.0% (-3.3 to +9.3) | +10.4% (-21.1 to +41.9) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 328.5 | -35.8% (-104.8 to +33.1) | +7.1% (-107.4 to +121.6) | +22.6% (-128.0 to +173.1) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.8 | 302.9 | -34.4% (-106.2 to +37.4) | +1.7% (-86.8 to +90.2) | +10.8% (-93.0 to +114.5) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 263,217 | 456,511 | +73.4% (-45.7 to +192.5) | +12.1% (-103.5 to +127.7) | +6.2% (-80.0 to +92.5) | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.105 | -1.0% (-6.8 to +4.9) | +1.5% (-3.7 to +6.7) | +2.4% (-17.7 to +22.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 129.1 | 127.8 | -1.0% (-7.0 to +4.9) | +1.6% (-3.9 to +7.1) | +2.4% (-17.7 to +22.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.142 | -1.1% (-7.3 to +5.2) | +1.8% (-3.3 to +6.9) | +2.6% (-17.9 to +23.2) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 | +4.33 (-1.4 to +10.1) | +9.33 (+0.609 to +18.1) | +12 (+1.17 to +22.8) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.5 | 290.8 | -0.6% (-2.5 to +1.3) | -0.3% (-2.6 to +2.0) | +0.8% (-2.8 to +4.3) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 292.7 | 291.0 | -0.6% (-2.4 to +1.3) | -0.4% (-2.5 to +1.8) | +0.2% (-1.7 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,683 | 4,655 | -0.6% (-2.4 to +1.3) | -0.4% (-2.5 to +1.8) | +0.2% (-1.7 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 4.79 | 4.91 | +2.4% (-2.8 to +7.6) | +0.6% (-13.2 to +14.3) | -3.0% (-16.6 to +10.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 6.1 | 6.17 | +1.2% (-9.2 to +11.6) | +0.6% (-6.3 to +7.5) | -13.1% (-55.4 to +29.3) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.85 | 2.93 | +2.9% (+2.2 to +3.7) | -1.2% (-14.4 to +12.0) | -2.4% (-12.1 to +7.2) | no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 170.5 | -66.7% (-66.9 to -66.5) | -66.9% (-67.6 to -66.2) | -66.7% (-66.9 to -66.5) | **confirmed better** |
| pages holding data, mean (MB) | 439.8 | 148.6 | -66.2% (-72.1 to -60.4) | -67.0% (-71.8 to -62.3) | -66.7% (-72.0 to -61.3) | **confirmed better** |
| pages read from disk into the pool (misses) | 169,349 | 334,300 | +97.4% (+95.1 to +99.7) | +101.1% (+97.2 to +105.0) | +102.0% (+97.7 to +106.4) | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.226 | +1.6% (+0.0 to +3.2) | -0.2% (-3.0 to +2.7) | -1.5% (-10.1 to +7.1) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 89.4 | 90.8 | +1.6% (+0.0 to +3.2) | -0.2% (-3.1 to +2.8) | -1.1% (-10.3 to +8.0) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.97 | 3.04 | +2.2% (+0.5 to +4.0) | +0.1% (-4.2 to +4.4) | -1.9% (-14.5 to +10.8) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 3 | +3 (+3 to +3) | +3 (+3 to +3) | +3 (+3 to +3) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292.6 | 293.2 | +0.2% (-0.4 to +0.9) | -0.1% (-0.9 to +0.7) | +0.2% (-0.2 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 292.8 | 293.6 | +0.3% (-0.3 to +0.9) | -0.1% (-1.1 to +0.9) | +0.2% (-0.2 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,685 | 4,698 | +0.3% (-0.3 to +0.9) | -0.1% (-1.1 to +0.9) | +0.2% (-0.2 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.68 | 3.75 | +1.8% (+1.8 to +1.8) | -0.5% (-14.5 to +13.4) | +3.0% (-6.4 to +12.5) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 5.09 | 5.06 | -0.6% (-7.4 to +6.2) | +3.5% (-20.8 to +27.7) | +0.6% (-6.2 to +7.4) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.75 | 2.81 | +2.3% (+0.5 to +4.1) | -3.6% (-16.8 to +9.5) | +1.5% (-4.5 to +7.5) | no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 258.5 | -49.5% (-92.9 to -6.1) | -56.1% (-95.9 to -16.2) | -51.7% (-91.7 to -11.6) | **confirmed better** |
| pages holding data, mean (MB) | 461.5 | 219.5 | -52.4% (-77.1 to -27.8) | -54.2% (-93.1 to -15.2) | -49.7% (-94.3 to -5.2) | **confirmed better** |
| pages read from disk into the pool (misses) | 456,881 | 1,035,506 | +126.6% (+82.7 to +170.6) | +142.0% (+20.8 to +263.3) | +122.6% (+50.5 to +194.7) | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.226 | +2.0% (-1.8 to +5.7) | -4.4% (-19.9 to +11.1) | +1.3% (-4.4 to +7.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 265.9 | 271.1 | +2.0% (-2.0 to +5.9) | -4.4% (-20.0 to +11.1) | +1.3% (-4.4 to +7.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.96 | 3.01 | +1.7% (-2.0 to +5.4) | -4.3% (-20.4 to +11.8) | +1.1% (-4.8 to +7.1) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 10.0 | +10 (+3.43 to +16.6) | +6 (-1.45 to +13.5) | +6.67 (+3.8 to +9.54) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181.1 | 184.7 | +2.0% (-2.6 to +6.5) | +0.9% (-0.4 to +2.2) | +0.5% (-0.5 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 192.5 | 192.5 | +0.0% (-2.1 to +2.1) | -0.4% (-2.1 to +1.4) | -0.6% (-1.9 to +0.7) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,850 | 3,850 | +0.0% (-2.1 to +2.1) | -0.4% (-2.1 to +1.4) | -0.6% (-1.9 to +0.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 11.6 | 9.5 | -18.0% (-56.2 to +20.2) | -10.8% (-13.3 to -8.3) | -11.3% (-26.6 to +3.9) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 157.8 | 192.7 | +22.1% (-58.2 to +102.4) | -9.1% (-17.6 to -0.6) | +0.3% (-37.6 to +38.1) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 8.77 | 9.17 | +4.5% (-24.5 to +33.5) | -3.4% (-4.7 to -2.2) | -1.5% (-12.3 to +9.3) | no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 894.8 | +74.8% (-1.4 to +150.9) | +59.3% (+14.6 to +104.1) | +79.2% (+23.1 to +135.2) | no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 459.2 | 773.0 | +68.3% (+8.0 to +128.7) | +53.0% (+24.3 to +81.8) | +70.4% (+40.5 to +100.2) | **confirmed WORSE** |
| pages read from disk into the pool (misses) | 434,039 | 230,443 | -46.9% (-113.8 to +19.9) | -40.2% (-84.1 to +3.7) | -45.1% (-61.6 to -28.5) | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.225 | -4.1% (-15.3 to +7.1) | -5.2% (-10.3 to -0.0) | -5.3% (-11.9 to +1.2) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 285.2 | 273.6 | -4.1% (-15.0 to +6.8) | -5.1% (-10.2 to -0.1) | -5.2% (-11.9 to +1.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 5.07 | 4.77 | -5.9% (-17.8 to +5.9) | -6.0% (-10.8 to -1.2) | -5.7% (-13.3 to +1.8) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 | +23.3 (+13.9 to +32.7) | +22 (+17 to +27) | +24.7 (+18.9 to +30.4) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.29 | 6.75 | +7.2% (-72.6 to +87.1) | +0.7% (-46.2 to +47.6) | -1.8% (-35.7 to +32.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 979.2 | 976.1 | -0.3% (-1.2 to +0.5) | -0.3% (-0.7 to +0.1) | +0.2% (-0.0 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 979.2 | 976.1 | -0.3% (-1.2 to +0.5) | -0.3% (-0.7 to +0.1) | +0.2% (-0.0 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 1.73 | 2.06 | +19.2% (+5.4 to +33.0) | +2.7% (-43.6 to +49.1) | -6.5% (-20.7 to +7.7) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 3 | 4.82 | +60.6% (+47.9 to +73.3) | -17.0% (-491.7 to +457.7) | -68.3% (-332.5 to +195.9) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.09 | 1.45 | +33.1% (+5.6 to +60.5) | -5.4% (-119.7 to +109.0) | -27.9% (-92.1 to +36.3) | no difference beyond the noise (2 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 700.9 | +36.9% (-59.5 to +133.3) | +5.8% (-59.4 to +71.1) | +9.8% (-25.5 to +45.1) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 449.8 | 546.2 | +21.4% (-38.0 to +80.9) | -1.1% (-54.7 to +52.6) | +4.3% (-33.1 to +41.7) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 139,508 | 124,289 | -10.9% (-71.8 to +50.0) | +4.7% (-44.8 to +54.2) | +2.8% (-30.4 to +36.1) | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.229 | +76.6% (-56.5 to +209.8) | -1.1% (-16.7 to +14.5) | -1.1% (-21.6 to +19.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 134.4 | 239.3 | +78.0% (-58.7 to +214.7) | -1.0% (-16.3 to +14.2) | -1.2% (-21.5 to +19.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 70.0 | 135.1 | +92.9% (-209.5 to +395.3) | -3.3% (-66.1 to +59.5) | -3.6% (-42.7 to +35.6) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 | +25.7 (+9.13 to +42.2) | +21.7 (+6.49 to +36.8) | +24.3 (+10.7 to +38) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 4 gauge-rows confirmed better, 1 confirmed worse, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
