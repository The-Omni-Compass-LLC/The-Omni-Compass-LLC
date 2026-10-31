# The 95th and 99th percentiles: where a tail reads higher with Omni-Compass, and why

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder asked on 19 October why the 95th and 99th percentiles show a loss on the live page. This page answers from the
receipts themselves. Every number is read from omni-v11's three-run tables (the engine that stood when this page was written) and from the raw
files of their runs. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these
results.

## 1. No tail reads LOSS

By the preregistered rule (a gauge reads LOSS only when it moves away from its aim in all three of our runs, every 95%
interval clear of zero), **no 95th- or 99th-percentile row reads LOSS in any omni-v11 table** (23 tables), and none read
LOSS in the omni-v10 tables before them. The one omni-v10 LOSS, the pod start wait under KEDA's HTTP add-on, was the test
machine (an empty node unpacking the image inside the window); since the kind rig pulls the served image onto every worker
before each arm, it reads STEADY on omni-v11 (`docs/POD_START_WAIT.md`, `results/live/V11_KEDA_REQUESTS.md`).

## 2. Real Kubernetes: Omni-Compass's tail was below native's in every repetition

The 90 paired repetitions of the three omni-v11 Kubernetes tests (Goldilocks, KEDA's HTTP add-on, KEDA on CPU and requests;
ten pairs in each of runs A, B and C), each scored from its own raw files by `tools/live_reps.py arm_gauges`:

| Test | Repetitions | Omni-Compass's 95th percentile above native's | 99th percentile above native's | The 95th percentile, three-run reading |
|---|---:|---:|---:|---|
| Goldilocks and the VPA | 30 | 0 | 0 | cut 61% to 64%, GAIN |
| KEDA's HTTP add-on | 30 | 0 | 0 | cut 72% to 74%, GAIN |
| KEDA on CPU and requests | 30 | 0 | 0 | cut 52% to 53%, GAIN |

## 3. Where a single run's tail rose: the data stores and the kill test

Six tail rows on omni-v11 have one or two runs whose interval lies wholly above zero. None holds in all three runs, so each
reads STEADY; a page that colours each run's cell on its own shows them red.

| Table, workload | Gauge | A | B | C | What it is |
|---|---|---|---|---|---|
| Kafka at the max, light | end-to-end latency, 99th percentile | +4.2% (+2.0 to +6.5) | −1.6% (−11.8 to +8.6) | −2.8% (−12.6 to +7.0) | one run up, two down: run-to-run variation |
| MySQL at the tune-down, read and write | latency, 95th percentile | +11.4% (+6.9 to +15.9) | −3.6% (−57.6 to +50.4) | +0.2% (−76.5 to +76.9) | one run up, the other two within wide noise |
| Redis at the tune-down, small values | latency, 99th percentile | +0.1% (+0.1 to +0.2) | +0.1% (−0.2 to +0.4) | +0.2% (−0.1 to +0.5) | about 6 µs on 5,600 µs, consistent in sign |
| Redis at the max, small values | latency, 99th percentile | +0.1% (−0.5 to +0.6) | +0.2% (+0.1 to +0.4) | +0.2% (+0.1 to +0.3) | the same |
| The governor killed outright mid-run (robustness) | response time, 99th percentile | +25.2% (+7.7 to +42.7) | −27.3% (−60.1 to +5.5) | −24.5% (−55.7 to +6.8) | one repetition of run A (below) |
| Redis at the max, the tuning workload | latency, 99th percentile | +0.3% (−0.0 to +0.5) | +0.2% (+0.1 to +0.2) | +0.0% (−0.2 to +0.3) | the same (the tuning workload, not counted) |

**The Kafka and MySQL rows are single-run excursions.** In each, one run rose and the others fell or sat inside a wide
interval; the three-run rule exists to keep such a run from being read as a result. On MySQL's read-and-write workload the
three runs' intervals are ±4.5, ±54 and ±77 points wide: with three pairs a run, the test cannot resolve a tail change of
under about 10% of native (`docs/POWER.md`).

**The kill test's row is one repetition.** In nine of run A's ten repetitions both arms' 99th percentile is the probe's
10-second timeout. In the fifth, the omni arm's slowest answers reached 9.2 s 140 to 190 s after the kill, at the load's peak,
with every setting already handed back to native's and both arms at the same ten replicas; the runner's processor was 100% busy
for 70 s, and the second governor had started 50 s before on the same four cores. That is the likely cause, not proven
(`docs/ROBUSTNESS_PREREGISTRATION.md`, "On omni-v11").

**The Redis rows are a real, tiny, consistent rise: about 6 µs at the 99th percentile.** Pooled over the 27 counted pairs
of each set, Omni-Compass's 99th percentile is +5.8 µs (standard deviation 8.9 µs) at the tune-down and +7.1 µs (8.9 µs) at
the max, while its mean latency falls about 32 µs (the larger ceiling turns misses into hits). The order of the arms does
not explain it: with Omni-Compass running second the rise is +4.9 µs, running first +8.5 µs. The cause is examined in
section 4.

## 4. The Redis tail: the harness's own layout, not Omni-Compass's effect on Redis

In the Redis harness (`tools/run_redis.py`) the brain runs as a thread inside the load generator's own Python process. Once a
second it reads the last second's requests (twice rebuilding a list of about 1,500 of them under the application's lock),
decides and writes its audit line. While it computes it holds Python's interpreter lock, so a request thread that wakes from
its store-trip sleep at that moment waits before its clock is read. Omni-Compass in a deployment is its own process and never
a thread inside the application it governs; only this harness puts the two together. The harnesses of the other data stores
do not: Kafka's producer and consumers, pgbench, sysbench and YCSB all run as processes of their own.

**The test** (`tools/redis_brain_probe.py`, the record in `results/REDIS_BRAIN_PROBE.json`, class S). It runs the harness's
own application at the GitHub rate (1,500 requests a second, 32 request threads), with and without the harness's own brain
loop in the same process, paired, the order alternating. Two outside parts are stand-ins, the same in both arms. The store
answers every request in a fixed 0.1 ms (a sleep, as a socket wait is), a hit with probability 0.6 and otherwise the declared
5 ms store trip. The plug writes nowhere, so the brain reads, decides and runs its trials while the cache never changes. The
only difference between the arms is the brain thread computing in the same process (1.4 ms of processor a second).

| With the brain in the process, against without (12 pairs of 20 s) | Change | 95% interval | Pairs with a rise |
|---|---:|---:|---:|
| response time, 99th percentile | +101 µs | +50 to +151 µs | 10 of 12 |
| response time, 95th percentile | +6.8 µs | +1.2 to +12.4 µs | 9 of 12 |
| response time, median | +2.1 µs | +0.2 to +4.0 µs | 9 of 12 |
| response time, mean | +5.4 µs | +2.9 to +7.9 µs | 11 of 12 |

**What it shows.** The brain's presence in the load generator's process, with nothing else changed, lengthens the timed
requests, most in the tail. In this stand-in the effect is larger than on GitHub's machines (+101 µs at the 99th percentile
against about +6 µs), because the stand-in's store answers in a fixed time and its tail is narrow. Three findings agree with it:
- in the Redis set run with native as shipped, the brain is idle (the knob is at its limit on native, and it computes
  nothing), and the 99th percentile shows no rise of consistent sign (`V11_REDIS_SHIPPED.md`);
- the rise appears in both of the operator's sets, where the brain computes every second;
- the mean still falls in those sets, because the larger ceiling turns misses into hits.

The tail rise is the harness's layout, and it weighs against Omni-Compass, because only the omni arm carries the brain inside
its process. A direct test on a real Redis on this machine (three pairs) could not resolve it: the arms differed by hundreds of
microseconds from pair to pair, and it was replaced by the test above.

**The fix.** The harness runs the brain in a process of its own, as a deployment does. It changes how the omni arm is
measured, so it lands with the next engine version and its reruns, never inside the omni-v11 tables
(`docs/CHANGE_CONTROL.md`).

## 5. Why the live page showed red

The live page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, rebuilt by its own workflow) reads each benchmark's newest
table. Until the omni-v11 tables reached main it read omni-v10's, where the KEDA pod start wait read LOSS. It also shows
each run's own interval beside the three-run reading, so a single run's rise, like those in section 3, can show as that
run's own excursion even where the three-run reading is STEADY. With the omni-v11 tables on main (19 October), the page's
only LOSS is gone, and its next rebuild reads them.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
