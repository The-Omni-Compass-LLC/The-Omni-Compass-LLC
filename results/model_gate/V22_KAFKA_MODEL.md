# The Kafka consumer group in our own model, closed loop

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S (our own model, never a benchmark result). The standing wire is `tools/run_kafka.py` at `29370eec0b`; the objective resource; seeds 101 to 108, every arm on the same seeds; notches of 30 s. Built by `tools/kafka_model.py` from the omni-v21 runs' own files (see its header).

## burst

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 340.3 | 340.3 | 410.1 | STEADY, under the floor (0.00%), +0.0% | GAIN, +20.5% | GAIN, +20.5% |
| end-to-end latency, 95th percentile (ms) | 2,633.3 | 2,633.3 | 208.3 | STEADY, under the floor (0.00%), +0.0% | GAIN, -92.1% | GAIN, -92.1% |
| end-to-end latency, 99th percentile (ms) | 3,239.5 | 3,239.5 | 1,408.3 | STEADY, under the floor (0.00%), +0.0% | GAIN, -56.5% | GAIN, -56.5% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), -0.0% | STEADY, under the floor (0.00%), -0.0% |
| end-to-end latency, mean (ms) | 420.8 | 420.8 | 96.2 | STEADY, under the floor (0.00%), +0.0% | GAIN, -77.1% | GAIN, -77.1% |
| consumer lag, most messages waiting at once | 1,650.1 | 1,650.1 | 1,344.1 | STEADY, under the floor (0.00%), +0.0% | GAIN (inside the seeds spread), -18.6% | GAIN (inside the seeds spread), -18.6% |
| consumer lag, mean messages waiting | 148.9 | 148.9 | 17.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -88.2% | GAIN, -88.2% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.4 | STEADY, under the floor (0.00%), +0.0% | power given, +71.0% | power given, +71.0% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 1.9 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 26.2 | 26.2 | 1.5

## light

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 724.2 | 724.2 | 842.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.4% | GAIN, +16.4% |
| end-to-end latency, 95th percentile (ms) | 2,501.0 | 2,501.0 | 51.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -98.0% | GAIN, -98.0% |
| end-to-end latency, 99th percentile (ms) | 3,207.3 | 3,207.3 | 619.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.7% | GAIN, -80.7% |
| end-to-end latency, median (ms) | 51.0 | 51.0 | 51.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 353.2 | 353.2 | 66.7 | STEADY, under the floor (0.00%), +0.0% | GAIN, -81.1% | GAIN, -81.1% |
| consumer lag, most messages waiting at once | 3,261.8 | 3,261.8 | 1,869.4 | STEADY, under the floor (0.00%), +0.0% | GAIN, -42.6% | GAIN, -42.6% |
| consumer lag, mean messages waiting | 253.0 | 253.0 | 13.1 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.8% | GAIN, -94.8% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 54.4 | 54.4 | 3.5

## heavy

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 146.7 | 146.7 | 170.3 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.1% | GAIN, +16.1% |
| end-to-end latency, 95th percentile (ms) | 2,367.5 | 2,367.5 | 55.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -97.7% | GAIN, -97.7% |
| end-to-end latency, 99th percentile (ms) | 3,073.8 | 3,073.8 | 623.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -79.6% | GAIN, -79.6% |
| end-to-end latency, median (ms) | 55.0 | 55.0 | 55.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 337.0 | 337.0 | 70.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -79.0% | GAIN, -79.0% |
| consumer lag, most messages waiting at once | 636.0 | 636.0 | 377.1 | STEADY, under the floor (0.00%), +0.0% | GAIN, -40.6% | GAIN, -40.6% |
| consumer lag, mean messages waiting | 47.7 | 47.7 | 2.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.5% | GAIN, -94.5% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 53.4 | 53.4 | 3.5

## tuning

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 365.3 | 365.3 | 424.9 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.3% | GAIN, +16.3% |
| end-to-end latency, 95th percentile (ms) | 2,483.3 | 2,483.3 | 52.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -97.9% | GAIN, -97.9% |
| end-to-end latency, 99th percentile (ms) | 3,177.0 | 3,177.0 | 620.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.4% | GAIN, -80.4% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 351.3 | 351.3 | 67.7 | STEADY, under the floor (0.00%), +0.0% | GAIN, -80.7% | GAIN, -80.7% |
| consumer lag, most messages waiting at once | 1,636.6 | 1,636.6 | 942.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -42.3% | GAIN, -42.3% |
| consumer lag, mean messages waiting | 126.3 | 126.3 | 6.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -94.8% | GAIN, -94.8% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 2.8 | STEADY, under the floor (0.00%), +0.0% | power given, +42.2% | power given, +42.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 54.2 | 54.2 | 3.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
