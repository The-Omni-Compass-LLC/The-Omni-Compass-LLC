# The Kafka consumer group in our own model, closed loop

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S (our own model, never a benchmark result). The standing wire is `tools/run_kafka.py` at `29370eec0b`; the objective resource; seeds 201 to 208, every arm on the same seeds; notches of 30 s. Built by `tools/kafka_model.py` from the omni-v21 runs' own files (see its header).

## burst

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 340.4 | 340.4 | 413.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, +21.4% | GAIN, +21.4% |
| end-to-end latency, 95th percentile (ms) | 2,620.8 | 2,620.8 | 133.3 | STEADY, under the floor (0.00%), +0.0% | GAIN, -95.0% | GAIN, -95.0% |
| end-to-end latency, 99th percentile (ms) | 3,233.3 | 3,233.3 | 1,045.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -67.8% | GAIN, -67.8% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), -0.0% | STEADY, under the floor (0.00%), -0.0% |
| end-to-end latency, mean (ms) | 419.5 | 419.5 | 82.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.3% | GAIN, -80.3% |
| consumer lag, most messages waiting at once | 1,643.5 | 1,643.5 | 1,023.2 | STEADY, under the floor (0.00%), +0.0% | GAIN (inside the seeds spread), -37.8% | GAIN (inside the seeds spread), -37.8% |
| consumer lag, mean messages waiting | 148.4 | 148.4 | 12.1 | STEADY, under the floor (0.00%), +0.0% | GAIN, -91.8% | GAIN, -91.8% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.4 | STEADY, under the floor (0.00%), +0.0% | power given, +71.0% | power given, +71.0% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 1.9 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 26.4 | 26.4 | 1.4

## light

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 724.2 | 724.2 | 842.3 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.3% | GAIN, +16.3% |
| end-to-end latency, 95th percentile (ms) | 2,494.8 | 2,494.8 | 51.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -98.0% | GAIN, -98.0% |
| end-to-end latency, 99th percentile (ms) | 3,188.5 | 3,188.5 | 663.5 | STEADY, under the floor (0.00%), +0.0% | GAIN, -79.3% | GAIN, -79.3% |
| end-to-end latency, median (ms) | 51.0 | 51.0 | 51.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 352.7 | 352.7 | 68.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.7% | GAIN, -80.7% |
| consumer lag, most messages waiting at once | 3,250.2 | 3,250.2 | 1,851.4 | STEADY, under the floor (0.00%), +0.0% | GAIN, -43.1% | GAIN, -43.1% |
| consumer lag, mean messages waiting | 252.6 | 252.6 | 13.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.5% | GAIN, -94.5% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 54.1 | 54.1 | 3.5

## heavy

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 146.7 | 146.7 | 170.2 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.0% | GAIN, +16.0% |
| end-to-end latency, 95th percentile (ms) | 2,361.3 | 2,361.3 | 55.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -97.7% | GAIN, -97.7% |
| end-to-end latency, 99th percentile (ms) | 3,067.5 | 3,067.5 | 667.5 | STEADY, under the floor (0.00%), +0.0% | GAIN, -78.3% | GAIN, -78.3% |
| end-to-end latency, median (ms) | 55.0 | 55.0 | 55.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 336.5 | 336.5 | 72.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -78.6% | GAIN, -78.6% |
| consumer lag, most messages waiting at once | 633.5 | 633.5 | 373.5 | STEADY, under the floor (0.00%), +0.0% | GAIN, -41.1% | GAIN, -41.1% |
| consumer lag, mean messages waiting | 47.6 | 47.6 | 2.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.2% | GAIN, -94.2% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 53.4 | 53.4 | 3.5

## tuning

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 365.4 | 365.4 | 424.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.3% | GAIN, +16.3% |
| end-to-end latency, 95th percentile (ms) | 2,483.3 | 2,483.3 | 52.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -97.9% | GAIN, -97.9% |
| end-to-end latency, 99th percentile (ms) | 3,177.0 | 3,177.0 | 664.5 | STEADY, under the floor (0.00%), +0.0% | GAIN, -79.1% | GAIN, -79.1% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 350.8 | 350.8 | 69.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.3% | GAIN, -80.3% |
| consumer lag, most messages waiting at once | 1,630.8 | 1,630.8 | 933.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -42.8% | GAIN, -42.8% |
| consumer lag, mean messages waiting | 126.1 | 126.1 | 7.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.5% | GAIN, -94.5% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 54.1 | 54.1 | 3.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
