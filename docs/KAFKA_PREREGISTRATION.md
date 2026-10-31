# Kafka: Omni-Compass on top of a consumer group's operator-set size, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-07, before any counted run. The rules below were set on the tuning workload (run on one machine, never
counted) and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings
are the three-run readings of `docs/OMNI_V1.md`. The runner is `tools/run_kafka.py`, the workflow
`.github/workflows/kafka.yml`, the three-run table `tools/kafka_abc.py`. This is register row 26 (messaging).

## Why this benchmark

Kafka carries the messages between the services of most large systems. A consumer group reads a topic; how many consumers
it runs is a number an operator sets once, and it stays at that number through every quiet hour and every rush, spending
machines when there is nothing to read and falling behind when there is too much. That fixed number is the native
controller here, and Omni sits on top of it.

## What is someone else's

- **Apache Kafka 3.9.1** (the Apache Software Foundation, Apache License 2.0), one KRaft broker on the machine, its
  `server.properties` as shipped but for the log directory, fetched from Apache's archive and checked against Apache's
  own SHA-512; a topic of **8 partitions**, replication factor 1 (one broker).
- **kafka-python-ng** (the client, Apache License 2.0): the producer and the consumers; the group's own rebalance and
  offset commit, as shipped.
- **The machine:** a GitHub Actions runner (4 cores): broker, producer and consumers share it, as a small deployment
  does. There is no watt-meter on it.

Nothing here models a message system. Omni starts and stops consumers of the group, which is what an operator does, and
reads what the consumers themselves record.

## Arms

- **native:** the consumer group at the operator's count, **2 consumers**, for the whole run.
- **omni:** the same group, with the compass law (`omnicompass/compass_law.py`) on **one knob, the consumer count**,
  inside the cover [1, 8]: never under one consumer, never more consumers than partitions (an idle consumer by Kafka's own
  rule). Everything else is native's.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the group's own end-to-end latency: the mean, over the messages consumed in the last
  second, of the time from a message's production to the end of its handling. A second with nothing consumed while
  messages wait reads as the line (someone is waiting and no one is taking); nothing consumed and nothing waiting reads
  as calm (0).
- **Band.** From 0 to the response line, **500 ms**. The compass pulls the reading to 40% of the line (200 ms), the
  service profile of the Kubernetes adapter, with its usual gains (kp 1.0, response time 3 s because a consumer added or
  removed shows only after the group rebalances, smoothing 0.5, one decision a second).
- **Direction.** A positive force (the service slow) with messages waiting adds ceil(force / 0.10) consumers (full
  force adds ten, capped by the cover). A negative force (calm) with no message waiting gives back **one idle consumer a
  second** (a consumer that read nothing in the last second), and only after a five-second dwell since the last change.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line every consumer the topic can use (8) is started at once; the compass then resumes.
- **One writer.** The consumers are the harness's own processes; nothing else starts or stops them.
- **Reset.** At the end of every omni arm the count is handed back to the operator's (2) and read back; the report says
  whether every arm was handed back.

Disclosed: a consumer added or removed makes the group rebalance, during which no partition is read for a moment; Omni
pays that cost every time it moves the knob, and the gauges below include it.

## The load

A producer offers messages at a rate stepping one notch at a time, **1 2 3 2 3 4 5 6 5 4 3 2 1 2 1**, 20 s a notch,
300 s an arm; the burst workload steps **1 6 1 8 1 6**. The base rate is set **once per workload before the counted
repetitions, in native mode**: 20 s of messages offered faster than the operator's two consumers can take give native's
capacity, and the peak notch offers nine tenths of it, so native is at its knee and not past it. Each message carries its
production time and a sequence number; its handling is a declared **service time of CPU** (the work the message is for:
1, 2 or 5 ms by workload), spent by the consumer before the message counts as handled. Both arms start from the operator's
two consumers after an 8 s settling period and alternate order between repetitions.

## Gauges (from the consumers' records, the group's lag, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: messages a second handled within 500 ms of production | **the aim is higher** (the product number) |
| throughput (messages a second) | the aim is higher |
| end-to-end latency p95, p99, median, mean | the aim is lower |
| consumer lag, most and mean messages waiting | the aim is lower |
| messages produced and never consumed | **any increase is marked** |
| consumers running, mean and most at once (the resources held) | the aim is lower (Omni will often hold more under load, and that reads higher) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 messages inside the line (the compass's own cost included) | the aim is lower |
| consumer changes written (the knob's moves) | shown, not judged |

Energy is not claimed beyond the host's CPU seconds (evidence class L: real software, no meter).

## Workloads

- **Tuning workload:** 2 ms of work a message, 256-byte messages, the standard steps. The band, the direction rule, the
  dwell and the reading above were set on it; nothing else is tuned. It is run and shown, and not counted.
- **Untouched workloads:** **light** (1 ms, 128 B, standard steps), **heavy** (5 ms, 1,024 B, standard steps), **burst**
  (2 ms, 256 B, steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, the per-message records, the audit and the broker log
archived with the code. Three separate runs on the frozen engine (A, B, C); the table (`tools/kafka_abc.py`) reads
GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when all three runs move the same way with every 95% interval clear of zero, no difference
beyond the noise when a run's interval includes zero, and the runs disagree when clear runs point different ways.
`tests/test_run_kafka.py` and `tests/test_kafka_abc.py`, run by `verify.py`, prove the rules without a broker.

## What the tuning workload showed on one machine, said before the counted runs

One short repetition (5 s a notch) on the development machine: native's two consumers at their knee held a p95 of 429 ms
with up to 329 messages waiting; omni held a p95 of 12 ms with at most 45 waiting, handled 3% more messages inside the
line, and did so with a mean of 5.8 consumers against 2, at slightly fewer host CPU-seconds (117 against 123: idle consumers
polling cost CPU too). The expected shape of the counted result is therefore: latency and lag much lower, consumers held higher, CPU about even, and every arm handed back. The counted runs will show whatever they show.

## Amendment 2 (2026-10-09, declared before any run on it): the brain's own verdict on the group's size

**Why, and when.** Written after the counted set was read (`results/live/V3_KAFKA.md`: work inside the line +16% to +21%, p95 1.6 s
→ 9 to 14 ms, consumers 2 → 6 to 8 power given in all three of our runs, host CPU higher on the light workload), at the founder's order of 9 October:
Omni need not be wired into every muscle; a knob that cannot prove it pays stays native and Omni only reads it. The brain must
decide that on the muscle itself, in real time, by a measurement.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 6 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the consumers running × the host's CPU busy share × the mean end-to-end latency of the messages consumed in the last second / the messages consumed inside the 500 ms line in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean end-to-end latency of the messages consumed in the last second / the messages consumed inside the 500 ms line in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and messages are waiting (the lag is above zero); a give-back step only while the service is calm and a consumer is idle and nothing is waiting. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. The fail-up rule (every consumer at once at the wall) is clamped to the allowance like every other move. The settle after a change is 6 s, two of the group's time constants, because a consumer that joins rebalances the group before it consumes. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** Under the resource objective the first consumer added under a queue pays: the queue drains, the
latency of the messages consumed falls by far more than one consumer in two costs, and the step is allowed; the next steps are
allowed while each still shortens the queue by more than it costs. The group is expected to reach 3 to 5 consumers at the peak
notches against 6 to 8 before, one notch a trial; p95 GAIN in all three of our runs but by less than 1.6 s → 10 ms, the lag GAIN in all three of our runs,
the consumers running power given in all three of our runs by less than before, the host's CPU inside the noise. Under the service objective a
step or two more. Both readings are run: three runs each. The counted set stays in `docs/history` as the result of the rule
before this amendment.

**Dispatched (2026-10-10 01:28 and 01:29 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=all`, `reps=3`, `step_s=30`: under the resource objective runs 38013300872 (A), 38013304929 (B) and 38013309420 (C), 01:28:23 to 01:28:31 UTC; under the service objective runs 38013371103 (A), 38013376137 (B) and 38013380640 (C), 01:29:31 to 01:29:40 UTC. Run A under the resource objective lost
its `heavy` job to GitHub (the runner shut down at 03:20:53 UTC, the harness never failed, the other three workloads finished); one
replacement run of all four workloads, the same inputs, was dispatched at 03:43:29 UTC: run 38021564790 on commit `0a74e9a6`, whose Kafka
harness is byte for byte that of `3aac0ab7`; the table reads it as A. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/kafka_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.

## Amendment 3 (2026-10-10 13:05 UTC, after the first counted set on amendment 2, before the next): a spend trial runs to its samples

The first counted set on the brain's verdict (runs 38021564790, 38013304929, 38013309420 under the resource objective and 38013371103, 38013376137, 38013380640 under the service objective; the table `results/live/V3_KAFKA.md` and `results/live/V3_KAFKA_SERVICE.md`) landed at midday on 10 October. What it showed about the trials: every spend trial was abandoned before it could be judged: 2 or 3 trials an omni arm, all abandoned, 0 allowed, 0 refused, in all 36 omni arms of each objective; the group stayed at the operator's two consumers (1.98 to 1.99 on average, the trial's reference seconds included) and the lag and latency gains of the earlier set, bought with 6 to 8 consumers, did not appear: consumers running read GAIN in all three of our runs by a fraction of one percent, everything else inside the noise.

**The cause is ours.** Amendment 2 ended a trial when the service swung to the other direction's condition: a give-back trial when the service left calm (the engine's own rule, kept), and a spend trial when the service turned calm. A spend that works calms the service within seconds, so a spend trial could never reach its samples: every successful spend ended its own trial unjudged. Nothing in the stack and nothing in the engine did this; the engine's verdict ends a trial when the condition it is given ends, and we gave it the wrong condition for spending. Found on the first set, corrected before the second, declared here.

**From this amendment** (`tools/knob_verdict.py`, the harness outside the engine; Omni v3 unchanged): a spend trial, once started, runs to its samples whatever the compass's force; only the wall (a fail-up) or the engine's own time limit on a trial ends it early. A give-back trial still ends when the service leaves calm. The conditions to start a trial, the cost, the judge, the allowance and the recheck are unchanged.

**Expected before the runs:** the consumer trials are judged: a third consumer is allowed where the latency falls and the work inside the line rises by more than the consumer count rises (the index's arithmetic), and the next one only if it pays again; the lag and p95 gains return (lag cut by most of its length, p95 from seconds to tens of milliseconds) with fewer consumers than the earlier set's 6 to 8, each one paid for; under the service objective the same with the consumers shown and not judged. The first set's table stands as the result of amendment 2 until the set on this amendment lands and supersedes it; it then goes whole to `docs/history`.

**Dispatched (2026-10-10 13:11 to 13:12 UTC, commit `ca745467`).** Under the resource objective runs 38054742933, 38054746778, 38054750788 (A, B, C); under the service objective runs 38054804459, 38054808912, 38054812962 (A, B, C); the same inputs as the morning's; recorded run by run in `docs/RERUN_2026-10-10.md`.

## Amendment 4 (2026-10-30, declared before any run on it): the group's twin and the immune reflex (the next engine's candidate)

**The cause, from the omni-v21 runs' own files** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`, `tools/store_causes.py`). In every one
of the 1,428 seconds the service stood over its line in the omni-v21 resource set, and the 1,625 of the service set, the brain
asked for consumers and amendment 2's allowance kept it from them: the wall (the fail-up) abandoned every spend trial before
its samples were in, and the fail-up itself was clamped to the allowance those trials never earned. The hand-back of 25
October gave back a consumer the load still needed: each change rebalances the whole group (a median 1.24 s of every message
waiting for a consumer added, 2.58 s for one removed), and the brain re-added it within seconds. The harness's eight keys land
on six partitions (Kafka's murmur2), so under the range assignor two consumers keep up with at most 792 messages a second at
2 ms of work (offered 880 they serve 825), three with 990, four no more than three, and five to eight with 1,980; every
workload's peak offers about 111% of what two consumers keep up with.

**From this amendment** (`tools/run_kafka.py` `Brain`, the code the real run and the closed-loop model drive):

- the twin reads each partition's arrivals from the topic's log-end offsets once a second (one wire in), places them on the
  members by the range assignor, and learns one member's rate from each second the queue grew with no change settling (the
  group consumed Σ min(load, μ), solved for μ; the median of the last 15) and a change's own stall from the seconds after it
  (the median of the last 9; one heartbeat interval, the consumers' own 3 s, before one is seen);
- the reflex: with the rate known, when the busiest member would run past nine tenths of its rate under the arrivals and the
  backlog (what waits, and what one change's stall would add, drained within 6 s), the count goes at once to the smallest count
  that carries them, up to the partitions; the reflex is never clamped by the allowance, which keeps judging the compass's own
  moves; with no rate yet known the wall adds one consumer;
- the hold: above the operator's count the count stays until a smaller one carries the last 60 s's arrival peak at seven tenths
  of its rate, 30 s after the last change, calm, with nothing waiting beyond one poll round a consumer; then it is handed back in
  one move (one rebalance); a change's own stall is never read as demand;
- the floor: never below the operator's count (the max, the factory tune); no give-back trial below it;
- the immune system (`omnicompass/immune.py`): Omni-Compass's count redlining past the line, stuck, and native's twin (the
  operator's count on the same arrivals) reading lower, the knob goes to native for the immune hold.

**The model gate** (`tools/kafka_model.py`, class S, every input set from the omni-v21 runs' own files; the standing wire is
omni-v21's loop read from git): at the counted 30 s a notch, on the development seeds 101 to 108 and the untouched seeds 201 to
208, no LOSS row in any workload against omni-v21; work inside the line GAIN (up 16% to 21%), the 95th percentile GAIN (down
92% to 98%), the most messages waiting at once GAIN (down 19% to 43%), the consumers power given (up 42% to 71%). At 20 s a
notch (run C's setting, not the counted one) one row reads LOSS: the burst's most messages waiting at once, up 30.6% inside the
seeds' spread, because native's queue grows about 1,100 messages in a 20 s notch and one change's rebalance costs about the
same; it is on the next version's list with that cause.

**The dial and the fingerprint** (30 October, the same candidate): `OMNI_DIAL=save` keeps omni-v21's loop on this wire (the
tune-down, where giving consumers back is the aim; the verdict's allowance and its trials as amendments 2 and 3 wrote them), the
max (the Brain above) is the factory tune, and every workload record carries its `dial`; `tools/knob_verdict.py`, which every
store wire's tune-down runs through, joins the fingerprint with this version (`tools/omni_version.py`, `STORE_WIRES`). In the
open-loop replay of the omni-v21 arms' recorded seconds (`tools/store_gate.py`, class S) the twin reads no arrivals (the audits
carry none) and the reflex adds consumers from the compass's own wanting: consumers held 2.1 → 4.9 (+130.6%, power given), no second
below the operator's count in either wire; no LOSS.

**Expected before the runs**, at the counted 30 s a notch, three paired repetitions a run: the work inside the line and every
latency and lag gauge GAIN in every untouched workload; the consumers running power given; the consumer changes shown. The
counted runs on this amendment run on the next engine version, which lands only when the model gate reads no LOSS for every
store wire it changes.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
