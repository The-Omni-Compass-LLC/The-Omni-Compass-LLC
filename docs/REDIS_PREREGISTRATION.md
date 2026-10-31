# Redis: Omni-Compass on top of a cache's operator-set memory ceiling, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-07, before any counted run. The rules below were set on the tuning workload (run on one machine, never
counted) and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings
are the three-run readings of `docs/OMNI_V1.md`. The runner is `tools/run_redis.py`, the workflow
`.github/workflows/redis.yml`, the three-run table `tools/redis_abc.py`. This is register row 27 (caches).

## Why this benchmark

A cache in front of a store is sized once: an operator sets Redis's memory ceiling (`maxmemory`) and its eviction rule and
leaves them. The working set the application needs moves through the day; when it outgrows the ceiling the cache evicts,
the application misses and goes to the store behind it, and the service slows; when it shrinks, the memory sits reserved
and unused. That fixed ceiling is the native controller here, and Omni sits on top of it.

## What is someone else's

- **Redis** as Ubuntu ships it (Redis Ltd and the Redis project; 7.0.15 on the development machine, the runner's own
  version recorded in every result), one server on the machine, its configuration as shipped but for the two settings an
  operator sets for a cache: the memory ceiling **64 MB** and the eviction rule **allkeys-lru**. Nothing else is touched.
- **redis-py** (the client, MIT License).
- **The machine:** a GitHub Actions runner (4 cores): Redis and the application share it. There is no watt-meter on it.
- **The application** is ours and declared: 1,500 requests a second from 32 worker threads, each request a GET of a key
  drawn from the working set of the moment (Zipf, exponent 0.5: a hot core and a long tail); a hit is Redis's answer; a
  miss costs a declared **5 ms trip to the store behind the cache** (a sleep, no CPU) and a write-back of the value. The
  working set steps one notch at a time, **1 2 3 2 3 4 5 6 5 4 3 2 1 2 1**, 20 s a notch, 300 s an arm (the burst
  workload steps 1 6 1 8 1 6); notch n is n times the base working set, so notch 1 fits the operator's ceiling and
  notch 6 is about twice it. Before the counted window the notch-1 set is loaded once into a flushed cache, the same in
  both arms, so the first notch is warm and later notches bring their own cold misses, as a real day does.

Nothing here models a cache. Omni writes one setting through Redis's own console (`CONFIG SET maxmemory`) and reads what
Redis itself reports (`INFO memory`, `INFO stats`) and what the application itself records.

## Arms

- **native:** Redis at the operator's ceiling, 64 MB, allkeys-lru, for the whole run.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the memory ceiling**, inside the
  cover **[16 MB, 512 MB]**. The eviction rule, the application and the requests stay the same.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the application's own request latency: the mean over the requests of the last second (a
  hit about 0.3 ms, a miss about 5.5 ms); a second with no request reads as calm (0).
- **Band.** From 0 to the response line, **2 ms** (a hit is inside the line, a miss and its store trip outside). The
  compass pulls the reading to 40% of the line (0.8 ms), the service profile of the Kubernetes adapter, with its usual
  gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second).
- **Direction, and the do-no-harm gate.** A positive force (misses) grows the ceiling by ceil(force / 0.10) notches of
  8 MB, **only while the cache is full** (memory used at 90% of the ceiling or more): a miss in a cache with room to
  spare is a cold miss, which no ceiling can mend, and the knob is left alone. A negative force (calm) with **nothing
  evicted in the last second** gives back one notch of 8 MB a second, after a five-second dwell since the last growth.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line with the cache full, a quarter of the cover (128 MB) is added at once, and again the
  next second if the service is still past the wall; never past the cover.
- **One writer.** The ceiling is read once before the first write (the operator's 64 MB) and read back after every write;
  a ceiling found at a value Omni did not write stops Omni writing (the plug contract).
- **Reset.** At the end of every omni arm the ceiling is handed back to the operator's 64 MB (Redis evicts down to it,
  as the operator's rule says) and read back; the report says whether every arm was handed back.

Disclosed: a ceiling given back below the memory in use makes Redis evict, so a give-back under load costs misses; the
compass sees that cost in its next reading and the gauges include it.

## Gauges (from the application's records, Redis's own INFO, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: requests a second answered within 2 ms | **the aim is higher** (the product number) |
| throughput (requests a second), cache hit rate | the aim is higher |
| latency p95, p99, mean | the aim is lower |
| failed requests | **any increase is marked** |
| memory ceiling held, mean (the knob, the resource); memory used, mean | the aim is lower (Omni will hold more under a wide working set, and that reads higher) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 requests inside the line (the compass's own cost included) | the aim is lower |
| keys evicted, ceiling changes written | shown, not judged |

Memory held is the resource this benchmark trades; no energy is claimed beyond the host's CPU seconds (evidence class L:
real software, no meter).

## Workloads

- **Tuning workload:** 8 KB values, a base working set of 2,500 keys (about 20 MB at notch 1, 120 MB at notch 6), the
  standard steps. The band, the direction rule and its gate, the dwell, the notch and the fail-up above were set on it;
  nothing else is tuned. It is run and shown, and not counted.
- **Untouched workloads:** **small** (2 KB values, base 10,000 keys), **large** (32 KB values, base 625 keys), **burst**
  (8 KB, base 2,500, steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, order alternating, the per-request records, the
audit and the server log archived with the code. Three separate runs on the frozen engine (A, B, C); the table
(`tools/redis_abc.py`) reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when all three runs move the same way with every 95% interval
clear of zero, no difference beyond the noise when a run's interval includes zero, and the runs disagree when clear runs
point different ways. `tests/test_run_redis.py` and `tests/test_redis_abc.py`, run by `verify.py`, prove the rules
without a Redis.

## What the tuning workload showed on one machine, said before the counted runs

Three short repetitions (10 s a notch) on the development machine shaped the rule, and are said here so nothing is hidden:

1. With a hot-core working set that fit the ceiling, Omni raised the ceiling to 500 MB while Redis used 21 MB: the
   misses it reacted to were cold misses, which no ceiling can mend. That is why the direction rule is gated on a full
   cache, and why the working set was made to outgrow the ceiling at the higher notches (the benchmark is of a cache
   whose working set moves, not of one that always fits).
2. With the whole cover added at the wall and a notch given back only every five seconds, the ceiling sat near 400 MB for
   most of the run while 270 MB were used. That is why the fail-up adds a quarter of the cover and the give-back runs a
   notch a second (the dwell holds only after a growth).
3. With the rule as frozen: hit rate 66% → 81%, work inside the line 982 → 1,197 requests a second (+22%), p95 7.8 →
   7.1 ms, the ceiling held 64 → 304 MB on average against 256 MB used (the cost, which will read higher), host CPU 137 →
   113 s, every arm handed back. The counted runs will show whatever they show.

## Amendment 2 (2026-10-09, declared before any run on it): the brain's own verdict on the ceiling

**Why, and when.** Written after the first counted set was read (`results/live/V3_REDIS.md`: work inside the line +14% to +27%,
the hit rate up, the ceiling held 64 → 200 to 300 MB power given in all three of our runs, the index's resource reading −24.9%), at the founder's order
of 9 October: Omni need not be wired into every muscle; a knob that cannot prove it pays stays native and Omni only reads it.
The brain must decide that on the muscle itself, in real time, by a measurement, not by a table after the fact.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 2 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the ceiling held (MB) × the host's CPU busy share × the mean latency of the last second's requests (the compass's own reading) / the requests answered inside the 2 ms line in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean latency of the last second's requests (the compass's own reading) / the requests answered inside the 2 ms line in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and the cache is full (memory used at 90% of the ceiling or more); a give-back step only while the service is calm and nothing was evicted in the last second. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. The fail-up rule (+128 MB at the wall) is clamped to the allowance like every other move: the first counted set shows it fired 3 to 10 times an arm, and most of the 64 → 200 to 300 MB came from it; under this amendment no unproven step is taken. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** Under the resource objective the first notch is refused: 12.5% more memory buys about one percent
of latency on these workloads, the cost rises and the step fails. The ceiling then stays at 64 MB in both arms, every gauge reads
inside the noise and the Redis category of the index reads exactly nothing: no gain, no loss. Under the service objective the
ceiling grows one notch a trial while the cache is full and missing, to perhaps 120 to 200 MB by the end of an arm; work inside
the line and the hit rate rise by less than the first set's +14% to +27%, the memory held by less than before. Both readings
are run: three runs each. The first counted set stays in `docs/history` as the result of the rule before this amendment.

**Dispatched (2026-10-10 01:28 and 01:29 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=all`, `reps=3`, `step_s=30`: under the resource objective runs 38013287665 (A), 38013291972 (B) and 38013296599 (C), 01:28:10 to 01:28:19 UTC; under the service objective runs 38013357351 (A), 38013361862 (B) and 38013366329 (C), 01:29:17 to 01:29:26 UTC. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/redis_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.

## Amendment 3 (2026-10-10 13:05 UTC, after the first counted set on amendment 2, before the next): a spend trial runs to its samples

The first counted set on the brain's verdict (runs 38013287665, 38013291972, 38013296599 under the resource objective and 38013357351, 38013361862, 38013366329 under the service objective; the table `results/live/V3_REDIS.md` and `results/live/V3_REDIS_SERVICE.md`) landed at midday on 10 October. What it showed about the trials: most trials in both directions were abandoned before they could be judged: of 14 to 20 trials an omni arm, 10 to 17 were abandoned, 1 to 5 allowed, 0 to 3 refused; the allowance stayed at one notch each way (56 to 72 MB) and every gauge read inside the noise in both objectives: no gain, no loss.

**The cause is ours.** Amendment 2 ended a trial when the service swung to the other direction's condition: a give-back trial when the service left calm (the engine's own rule, kept), and a spend trial when the service turned calm. A spend that works calms the service within seconds, so a spend trial could never reach its samples: every successful spend ended its own trial unjudged. Nothing in the stack and nothing in the engine did this; the engine's verdict ends a trial when the condition it is given ends, and we gave it the wrong condition for spending. Found on the first set, corrected before the second, declared here.

**From this amendment** (`tools/knob_verdict.py`, the harness outside the engine; Omni v3 unchanged): a spend trial, once started, runs to its samples whatever the compass's force; only the wall (a fail-up) or the engine's own time limit on a trial ends it early. A give-back trial still ends when the service leaves calm. The conditions to start a trial, the cost, the judge, the allowance and the recheck are unchanged.

**Expected before the runs:** under the resource objective the first spend notch is judged and most likely refused (12.5% more memory buys about one percent of latency on these workloads: the cost rises), so the ceiling stays near the operator's and the category reads nothing; under the service objective the spend notches are judged on latency and work alone and allowed while the hit rate rises, the ceiling growing to perhaps 100 to 200 MB with work inside the line and the hit rate up by less than the first set's +14% to +27%. The first set's table stands as the result of amendment 2 until the set on this amendment lands and supersedes it; it then goes whole to `docs/history`.

**Dispatched (2026-10-10 13:10 to 13:12 UTC, commit `ca745467`).** Under the resource objective runs 38054731163, 38054735302, 38054739168 (A, B, C); under the service objective runs 38054791688, 38054795871, 38054800068 (A, B, C); the same inputs as the morning's; recorded run by run in `docs/RERUN_2026-10-10.md`.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Amendment 4 (2026-10-17, declared before any run on it): native as shipped, beside the operator's ceiling

The founder's order of 17 October: every native muscle also runs exactly as it is shipped. A second set runs beside the
preregistered one with every rule unchanged but native's two settings: Redis exactly as shipped, with no memory ceiling
(`maxmemory 0`) and `noeviction` (`tools/run_redis.py --native shipped`, workflow input `native: shipped`). A cache with no
ceiling holds every key it is given: the knob is at its limit on native, and any ceiling Omni-Compass wrote would sit below
native, which the max never does. So in the shipped set omni reads the cache, writes nothing and says so in its audit ("native
has no ceiling: at its limit on native"), and every row reads STEADY; that is the result, said before the run. The value of the
compass on this knob is where an operator has set a ceiling, which the preregistered set measures; its tables keep their name,
and the shipped set's are named for it (`…_REDIS_SHIPPED.md`).


## Amendment 5 (2026-10-30, declared before any run on it): the max on the cache's ceiling, with the working set's floor (the next engine's candidate)

**The cause, from the omni-v21 runs' own files** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`, `tools/store_causes.py`). In 4,426 of the
4,581 seconds the application stood over its 2 ms line in the omni-v21 resource set (runs 40254205224, 40276907808, 40400989005),
the brain asked for memory and amendment 2's allowance kept it from it: the wall abandoned the spend trials (62 of 68 in run A)
and the fail-up itself was clamped to the allowance they never earned, so the cache stayed at 64 to 80 MB. In our own model of the
cache (`tools/redis_model.py`, class S, its hit and miss latencies the omni-v21 native arms' own records), a ceiling the working set
fits under raises the hit share from 63% to 72% at 256 MB in the small workload; the misses that remain are each notch's first
touch of a new keyspace, which no ceiling mends.

**From this amendment** (`tools/run_redis.py` `Brain`, the code the real run and the model drive): the store wires were written on
9 and 10 October, before the founder's order of 12 October that the max is the default brain, and never brought to it; this brings
the cache's wire to the max.

- the spend: misses with the cache full go through by the compass's own law (ceil(force / 0.1) notches of 8 MB a second; at the
  wall a quarter of the cover at once), never clamped by the allowance, up to the cover's top; the memory is power given, shown
  beside the hits it bought;
- the hold: the twin is the working set itself, the most memory the cache held in the last 60 s with the fullness margin; calm
  with nothing evicted hands one notch back a second, never below that floor and never below the operator's ceiling (a ceiling
  handed back below the working set evicts the keys the application still asks for, and the next rise buys them back at the
  store's price: the sawtooth the model showed on the first candidate, which read LOSS against omni-v21 in two workloads);
- the floor: the operator's ceiling, the max's native, handed back at the end as before; the verdict's allowance and its trials
  stand for the tune-down below it (`dial save`), where giving memory back is the aim.
- the account of a miss (`tools/store_brain.py`, what the three cache wires share): memory is spent only where the misses are at
  least the one key's floor (a half of one percent, `tools/readings.py` `SIZE_FLOOR`) of the service's own time over the last 10 s,
  from the application's own split of each request into hits and misses (the misses' count times what a miss cost beyond a hit,
  over the requests times their mean); under the floor the misses are nothing the record could read, memory could buy nothing it
  could read, and the ceiling holds and says why; where the split is not read this second (the wire's older records), nothing is
  known and nothing is taken;
- the host's room: a notch is taken only while the host keeps 5% of its memory available after it (`/proc/meminfo`, the compass's
  cushion); unread, nothing is taken;
- the record: every second's split and the misses' share of the service's time, the floor and the host's room in the audit; the
  arm's record carries the max's counts where it carried the verdict's allowance; every workload record carries its `dial`;
  `OMNI_DIAL=save` keeps omni-v21's loop (the tune-down); `tools/store_brain.py` and `tools/knob_verdict.py` join the fingerprint
  with this version (`tools/omni_version.py`, `STORE_WIRES`).

**The model gate** (`tools/redis_model.py --compare`, seeds 101 to 103, 30 s a notch, against omni-v21's own loop read from git; the
model's host has room for every notch; `results/model_gate/V22_REDIS_MODEL.md`): work inside the line GAIN in every workload (small
up 22.9%, burst up 17.6%, tuning up 10.3%, large up 7.7%), the mean latency GAIN (down 36% to 59%), the 95th and 99th percentiles
GAIN or EVEN (the large workload's 95th down 95.1%), the memory held power given (201 to 304 MB against 62 to 66 MB); no LOSS row.
In the open-loop replay of the omni-v21 arms' recorded seconds (`tools/store_gate.py`, class S), whose audits carry neither the
split nor the host's memory, the candidate holds at the operator's ceiling: seconds below native 36.6 → 0 an arm (shown), seconds
below native while missing 1.5 → 0 (GAIN +100.0%), the knob's moves 12.3 → 0 (GAIN +100.0%), the ceiling held 64.2 → 64.0 MB
(EVEN); no LOSS.

**Expected before the runs**, at the counted 30 s a notch, three paired repetitions a run: work inside the line and the mean latency
GAIN in every untouched workload; the 95th percentile EVEN or GAIN (the misses that remain are cold); the memory ceiling and the
memory used power given; the knob's moves shown. The counted runs on this amendment run on the next engine version, which lands only
when the model gate reads no LOSS for every store wire it changes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
