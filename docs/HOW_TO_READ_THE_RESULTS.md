# How to Read the Results

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- the key: GAIN, STEADY and LOSS (tools/readings.py) -->
## The key: GAIN, STEADY and LOSS

Every judged reading in Omni-Compass is one of three words: **GAIN**, **STEADY** or **LOSS**. Better, same and worse are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before the runs.

| Word | What each letter stands for | Its sense in underwriting | What it means in a table |
|---|---|---|---|
| **GAIN** | **G** Growth (asset appreciation); **A** Advantage (risk reduction); **I** Improvement (margin expansion); **N** Net-positive (profitable outcome) | surplus and positive variance | the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a resource cut |
| **STEADY** | **S** Stable (zero variance); **T** True to baseline (expected norm); **E** Equilibrium (balanced risk); **A** At par (no net change); **D** Drift-free (within the 0.5% floor); **Y** Yield held (nothing lost) | the par baseline: equilibrium | native and Omni-Compass within 0.5% of each other: the mean of the three runs' changes under the 0.5% floor, or no change at all; a knob native already runs at the top of its range is STEADY, at its limit on native |
| **LOSS** | **L** Leakage (capital drain); **O** Off-track (adverse selection); **S** Setback (claim liability); **S** Subpar (negative variance) | actuarial deficit and exposure | the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures |

How the sign of a number becomes a word:

- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.
- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.
- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak that rose is power given, in a data centre and in a building alike (17 October).
- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; a fall is power given, because it falls when more power is given for the same work.
- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).
- **The floor, and every change above it** (the founder's orders of 20 and 24 October 2026): a change of half of one percent (0.5%) or more either way is a change, and reads **GAIN** or **LOSS** (or **power given**) by what the gauge is for; STEADY is kept for a change under 0.5%. The change is the mean of the three runs' changes, each in percent of native. Where every run moved the same way with its 95% interval clear of zero, the word reads **in all three of our runs**; otherwise it reads **by the mean of our three runs** and says in how many of the three runs it stood beyond the noise, so a reader sees how firmly it stands. Where runs moved 0.5% or more in opposite directions, the reading is **the runs disagree**. A mean under 0.5% reads **STEADY, under the floor**, with its size.
- **Two numbers, never mixed** (the referee's work order of 25 October): every row shows native's value and Omni-Compass's, the **raw change** (Omni-Compass − native) / native with its true sign, + for a rise and − for a fall whatever the gauge is for, labelled raw, and apart from it the word with its size and no sign. A bill cut 3% reads raw −3.0%, GAIN 3.0%; failed requests up 2% read raw +2.0%, LOSS 2.0%; a pod start wait from 0.22 s to 0.83 s reads raw +275.0%, LOSS 275.0%; a change under the 0.5% floor reads STEADY 0.3%. No raw sign is ever turned to match a word.

Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: TOWARD ITS AIMS reads GAIN; BOTH WAYS reads GAIN AND LOSS; AWAY FROM ITS AIMS reads LOSS; SAME AS NATIVE reads STEADY (the same as native); AT ITS LIMIT ON NATIVE reads STEADY (at its limit on native); SUPERIOR WITHIN GUARDRAILS reads GAIN (within the guardrails); ENERGY IMPROVEMENT WITH SERVICE TRADEOFF reads GAIN AND LOSS (energy cut, service traded for it); SERVICE IMPROVEMENT WITH ENERGY TRADEOFF reads GAIN, power given (service GAIN, energy given for it); NONINFERIOR / INCONCLUSIVE reads STEADY (inside the noise, within the guardrails); NOT ESTABLISHED reads STEADY (not established: inside the noise, a guardrail crossed on the mean). A run that breaks its own validity checks reads INVALID and carries no word.

Every reading is one of these. **GAIN, LOSS or power given in all three of our runs**: A, B and C moved the same way, every 95% interval clear of zero. **GAIN, LOSS or power given by the mean of our three runs**: the runs' mean moved 0.5% or more, with the count of runs that stood beyond the noise beside it. **STEADY, under the floor**: the mean moved less than 0.5%. **STEADY, the same**: no change at all. **The runs disagree**: runs moved 0.5% or more in opposite directions, so the test is unstable there and is looked into. **Shown, not judged**: a gauge declared in advance as shown only, such as the knob's own setting.

Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as surplus, par or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (STEADY). Its first rule is do no harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit (`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.

Disclosure and disclaimer: GAIN, STEADY and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs measured against native under the declared aims, not a promise about any other system; every number stands beside its word, so a reader can judge it by any other convention. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end of the key -->

This chapter teaches you to read every table Omni-Compass produces. You do not need to know Kubernetes or GPUs to
follow it. Read the five ideas first, then go to the table you have in front of you.

## The five ideas behind every table

1. **Native, Omni-Compass on native, and Omni-Compass direct.** Every result compares a system running alone
   ("native": Kubernetes alone, the card's own firmware alone, a building's own controller alone) with the same system
   with Omni-Compass sitting on top of it (Omni-Compass on native, "omni" in the tables), and, since the founder's order
   of 23 October, wherever native's own controller can be switched off, with the same system run by Omni-Compass alone
   (Omni-Compass direct, "solo" or "Omni direct" in the records). Same machine, same work, same moment: the only
   difference is Omni-Compass, and which controller moves the knob. The three arms are always shown together, and each
   pair is read on its own.
2. **Paired runs.** Each comparison is run many times ("repetitions" or "runs"), each time with both arms on the same
   seed (the same pattern of work). Each repetition gives one difference; the table reports the average difference.
3. **The 95% interval.** Next to each average is a range, for example `+0.092% (+0.090 to +0.093)`: the paired mean
   difference ± t₀.₉₇₅,ₙ₋₁ · s/√n, where s is the standard deviation of the n paired differences and t₀.₉₇₅,ₙ₋₁ the
   two-sided 95% point of Student's t on n − 1 degrees of freedom (`omnicompass/student_t.py`, computed for any n:
   4.303 at 3 pairs, 2.262 at 10, 2.093 at 20). The method that draws it covers the true difference in 95 of 100
   repetitions of the whole experiment; it is not a 95% chance about this one range.
   - If the whole range is on one side of zero, the difference is **clear of the noise** (a table's "significant"
     column says "yes"); its word is GAIN, LOSS or power given, by the gauge's aim.
   - If the range includes zero, that run is **not beyond the noise**: it could not tell the arms apart by itself. It
     does not show that they are equal; how small a difference the run could have seen is the interval's half-width,
     printed beside it. Since the founder's order of 24 October the word is decided by the size first: a change of 0.5%
     or more reads its word even where a run's range includes zero ("by the mean of our three runs", with the count of
     runs beyond the noise), and only a mean under 0.5% reads STEADY (the key above; section "The verdict rules" below).
4. **The word, not the sign.** Every judged reading is GAIN, STEADY or LOSS (the key above). For response time,
   failures and time over the line a fall is GAIN; for work and work per energy a rise is GAIN; for energy, machines
   and every other resource spent or held a fall is a cut, a GAIN, and a rise is **power given**, never a loss.
   Every table gives the word beside the number.
5. **Evidence class.** Every result is marked with how it was measured:
   - **T**: a theorem;
   - **V**: verified in code;
   - **S**: our own model (modelled);
   - **L**: live software (real Kubernetes);
   - **P**: a physical meter (a real card's own power meter).

   Only **P** speaks for hardware energy.

## What every result names: the workload, the boundary, the profile, the costs, the requirements and the verdict

The common language of these six is written once in `docs/FACTORY_PROFILE.md`; this section is how to read a result by it.
Every result identifies the engine version, the configuration, the hardware or model, the workload and the measurement
boundary that produced it, and says nothing beyond them.

**The workload contract.** Both arms are offered the same work: the same demand at the same moments (an open-loop schedule,
the same seeds in every arm), on the same machines, in the same window, against the same service line, all written down
before the first counted run in the benchmark's preregistration (`docs/*_PREREGISTRATION.md`). A comparison is valid only for
a matched workload; a run whose work was not matched, or a workload left incomplete, is shown as unresolved or invalid and
carries no word. The load is a declared input, and a result belongs to the load it names (`DISCLOSURES.md`, section 4).

**The measurement boundary.** What a result counts, and what it does not: the cluster's machines in service, the host's
processor seconds, a card's own meter, the machines a cloud bills, the plant models' energy. Each receipt names its boundary,
and nothing outside it is claimed. The energy on GitHub's Kubernetes is a declared formula over machines, not a meter; a
model's energy is not a meter's; only class P speaks for hardware energy. The whole organism's composition
(`results/WHOLE_SYSTEM.md`) names its three places, the software end, the cloud's wire and the bare metal, and enters a place
with no measurement as exactly 1, named.

**The profile's identity.** Every result names its engine and fingerprint (`python3 tools/omni_version.py`) and the profile
that governed it: the **factory profile** (the complete, versioned set of Omni-Compass default settings shipped together; the
released one is omni-v19's, the governor's full decision every 60 s with its fast checks every 5 s and every muscle on its card
or the engine's setting), a **candidate profile** (a proposed combination under evaluation) or a **custom profile** (an
identifiable configuration that differs from the released factory profile, whose results are its own). The **active profile**
is the one governing the run in front of you; the live benchmark engine names it with its fingerprint. A matching fingerprint establishes
identity; the validation receipts establish what that identified implementation demonstrated. A result is never read across
engines, and never across profiles. The best validated factory profile for the declared operating conditions has not yet been
established (`docs/FACTORY_PROFILE.md`, section 5): until it is, every published result is the released factory profile's.

**The costs.** A resource spent or held that fell is a cut, a GAIN; one that rose is **power given**, never a loss. The bill
of a deployment route r (on site; through the cloud) is the sum of its costs inside the declared boundary, each counted once,
for each arm a (native, Omni-Compass on native, Omni-Compass direct): C(r, a) = Σₖ c(r, a, k), and its saving is
S(r, a) = (C(r, native) − C(r, a)) ⁄ C(r, native), for a positive native cost and a matched workload. A component's percentage
(fewer machine-hours, less energy) is a supporting measurement, never the bill. A missing price stays visibly unresolved: today
only the cloud's compute is metered in money (Azure, machine-hours at the list price, `results/live/AKS_BILL.md`), so neither
route's bill is resolved yet. A whole-workload index (the composition's one number over its gauges) is not a price.

**The requirements.** Health is the explicit operating requirements: correctness, service limits (the response-time line),
resource bounds and every applicable hardware limit; each reading Hⱼ has its limit Lⱼ. A result names which of the two
objectives its tune served: the most healthy production, maximise E[P(θ)] subject to Hⱼ(θ) ≤ Lⱼ for every j (the max, the
default brain), or the least cost per unit of completed production, minimise E[C(θ) ⁄ P(θ)] subject to the same requirements
(the tune-down, `dial save`, a tune anyone may set; the clouds ran it until 31 October, when the founder struck that rule and
every cloud runs the max with the bill judged beside the work). P is the useful output, the work done inside the line. A requirement crossed is
read on its own gauge (time over the line, failed requests, alert minutes) and never traded away.

**The verdict rules.** Every judged gauge is read by the one key (`tools/readings.py`, the key at the top of this page): the
word by what the gauge is for, never by its sign; over runs A, B and C the change is the mean of the three runs' changes in
percent of native; a mean under 0.5% reads STEADY, under the floor (STEADY, the same where nothing moved); from 0.5% up GAIN, LOSS
or power given **in all three of our runs** where every run moved the same way with its 95% interval clear of zero, otherwise
**by the mean of our three runs** with the count of runs beyond the noise; runs that moved 0.5% or more in opposite directions
read **the runs disagree**; a count that must never rise (failed requests, lost messages) reads LOSS on any rise in any run.
Each run's own number wears that run's own word by the same floor. A label written before the run is shown with its word
first. A model (class S) is never read as proof of hardware, and a reading on the live tuning bench at any setting other than
the factory profile is a variation of the mechanism, never a benchmark result.

## The words in the tables

| Word | What it means | Its aim |
|---|---|---|
| Work per energy | work done for each unit of energy (requests per kilojoule on a card) | higher |
| Energy (J, Wh) | the energy used | lower |
| Work, requests served | how much was done; both arms must serve the same work | equal |
| Response time, median (p50) | half of the answers were faster than this | lower |
| Response time, p95 | 95 of 100 answers were faster than this: the slow answers, what service promises are written on | lower |
| Response time, p99 | 99 of 100 answers were faster than this: the slowest answers | lower |
| Time over the line, violations (pp) | the share of time the service was past its promise, in percentage points | lower |
| Failed requests, not served | answers that never came | zero |
| Machines in service, node-hours | how many machines were kept on, and for how long | lower |
| Band first | the founder's rule: no win unless time over the line is no higher than native's | "held" |
| Knobs handed back, restored | at the end every setting Omni-Compass touched was put back exactly | True / yes |
| Label | the verdict, chosen by a rule written before the run, never by hand | see each table |

## The GPU card (`results/gpu/run-<stamp>/GPU_REPS.md`)

One card, three arms, many repetitions:
- **native**: the card's firmware alone;
- **watch**: Omni-Compass running and deciding but writing nothing. It must equal native: this proves Omni-Compass
  watching costs nothing;
- **omni**: Omni-Compass on top, moving the card's clock ceiling and power limit.

Read it in this order:
1. **The verdict line** at the top, one of the labels chosen by rule (`docs/GPU_PREREGISTRATION.md`, amendment 1):
   SUPERIOR WITHIN GUARDRAILS, ENERGY IMPROVEMENT WITH SERVICE TRADEOFF, NONINFERIOR / INCONCLUSIVE, NOT ESTABLISHED,
   AWAY FROM ITS AIM, NOT ATTRIBUTABLE or INVALID; each gauge reads GAIN, LOSS or power given **clear of the noise**, or
   **STEADY, no difference beyond the noise** (amendment 14; the first counted run of 2 October printed "proven" and "not
   proven" for the same rule).
2. **Work per energy** (requests per kilojoule): the headline. A plus sign with a range wholly above zero is a GAIN
   clear of the noise.
3. **Requests served** must be equal in every arm. More energy saved by serving less work would be cheating; the bench
   checks it.
4. **p95 and p99**: the slow answers. With the verdict rule (`omnicompass/verdict.py`), Omni-Compass never takes a step
   that makes a request more than 2% slower.
5. **Writes and restore**: how many settings were changed, and that every arm ended at the card's own limit.

The file `omni-gpu-<stamp>-confirmations.tar.gz` holds two such tables: compute-bound work (matrix products) and AI
token generation (memory-bound work).

## The card inside the seven organisms (`results/hil/run-<stamp>/HIL.md`)

The real card is wired into each of the seven organisms (the spine, the four realms, the four stacked, the whole tower) at four
sizes (1, 10, 100 and 1,000 copies). Each row is one size, one organism and one part:
- **stacks (model)**: the modelled machines (evidence S);
- **card (meter)**: the real card, its own meter (evidence P);
- **both**: the two added together.

The second table lists the card's own receipts for every arm: its energy, requests served, p95, and its power limit at
the start and at the end, which must be equal.

## Real Kubernetes (`results/live/LIVE_REPS_<n>.md`)

Each set is 10 paired repetitions on a real Kubernetes cluster (kind): native Kubernetes (its HPA and scheduler)
against the same Kubernetes with Omni-Compass on top. Read:
1. **worker nodes in service** and **node-hours**: how many machines were kept busy. A fall is GAIN.
2. **response time p95 and p99**: a fall is GAIN (faster).
3. **failed requests**: must be zero on both sides.
4. **CPU used with Omni's own**: Omni-Compass's own cost included; "no" in the significant column means its cost is
   inside the noise of the test (the interval beside it gives the size the test could have seen).
5. **The label** at the bottom, by the rule written before the run.

Energy on kind is a declared model, not a meter: kind keeps every machine powered.

## The three-run tables (`results/live/V<engine>_<TEST>.md`, for example `V7_GOLDILOCKS.md`, `V8_CITYLEARN.md`)

Every benchmark since the engine was frozen runs three separate times, A, B and C, on the same bytes, and the table
shows all three beside each gauge, each with its own 95% interval. Read the last column first, by the verdict rules above:
**GAIN**, **LOSS** or **power given in all three of our runs** (the mean moved 0.5% or more, every run the same way with its
interval clear of zero), **by the mean of our three runs** (the mean moved 0.5% or more; the count of runs beyond the noise
beside it), **STEADY, under the floor** or **STEADY, the same**, or **the runs disagree** (runs of 0.5% or more pointing opposite
ways: the test is unstable there and is looked into). Every table was read again from its own data by that rule on 24
October (`tools/reread.py`). Nothing reads "confirmed" or "not
confirmed": nobody outside The Omni-Compass LLC has reviewed or approved these results. The `V<n>_` in a table's name (`V10_`, `V11_`, `V12_` and so on) is the engine the runs carried (`python3 tools/omni_version.py --commit <sha>`);
a table never mixes engines, and a reading is never carried from one engine to another. Every LOSS and every power given is in the table beside
the GAINs. On the omni-v11 tables there is no LOSS. Power given appears in the grid's dissipated energy in four grids, the tap
operations in one, PgBouncer's connections, MySQL's pool from its factory size, Redis's memory and CityLearn's distance from net
zero in one district. An earlier engine's LOSS stays in its own table, for example CityLearn's energy not served on omni-v7.

**How often the rule reads a difference that is not there.** Under no true difference, one run's 95% interval falls
wholly above zero with probability 0.025 and wholly below with 0.025. A row reads GAIN or LOSS **in all three of our runs**
only when all three independent runs fall on the same side, so its chance of a false reading is 2 × 0.025³ ≈ 3.1 × 10⁻⁵. A
word read **by the mean of our three runs** carries no such bound: it says the runs' mean moved 0.5% or more, and the count of
runs beyond the noise beside it says how firmly; read it with that count. Over a table of 30
judged rows the chance that any one is false is at most 30 × 3.1 × 10⁻⁵ ≈ 0.09% (a union bound, as Bonferroni's), and over
the 798 judged rows of the omni-v11 tables that carry noise (1,039 judged rows in 23 tables, less the 241 of the deterministic
simulators) the expected number of false readings is 798 × 3.1 × 10⁻⁵ ≈ 0.02. The
bound assumes the three runs independent; runs on the same kind of machine can share a bias, which three runs cannot
remove and the bound does not cover. The price of "in all three of our runs" is power: a small true difference must clear
the noise three times, so many rows read by the mean of our three runs are differences too small for a run's pairs to resolve
(with 3 pairs a run, t = 4.303 and the interval is wide). Every reading is printed with the three intervals behind it. The deterministic simulators (CityLearn,
pandapower, MuJoCo) reproduce to the digit, so there the three runs check the harness, not the noise; their STEADY means
the same to one part in a million.

## The workload tables (`V<engine>_PGBENCH.md`, `_KAFKA.md`, `_REDIS.md`, `_YCSB.md`, `_SYSBENCH.md`) and the swarm table (`V<engine>_SWARM.md`)

The database, the broker and the cache share one shape. The head names the three runs, their commits and the engine each
carried. Then one section per **workload**: the tuning workload first, marked "shown and not counted" because the rules were
fitted on it, then the untouched workloads, which are the judged ones. Each section says what the workload is (value sizes,
rates, steps) and what native's own capacity measured on that run, so the reader knows how hard native was pushed. The
rows are the gauges with their direction in the name: the first row is always **work inside the response line**, the
product number; then throughput, the latency percentiles, failures (any increase in any run is marked), **the resource
held** (connections, consumers, the memory ceiling: the aim is lower, and Omni-Compass holds more of it wherever it bought
a gain, so expect it higher there), the host's CPU (the compass's own cost included), and the knob's moves (shown, not
judged). The last line of each section says whether every arm handed the knob back; the last line of the table counts the
rows toward their aims, away from them and disagreeing across the untouched workloads. The swarm table reads the same way with cells instead
of workloads, with collisions voiding a cell, and with a declared reproduction tolerance (one part in a thousand) because
PyBullet does not reproduce to the bit across machines; its amendment says so.

## The governor's own cost (`V3_OWN_COST.md`) and the robustness tables (`V<engine>_ROBUST_KILL.md`, `V<engine>_ROBUST_LONG.md`)

`V3_OWN_COST.md` is Omni-Compass's own CPU, from the `overhead` record every omni arm's audit carries, by organism and
copies, under the engine each run carried; it is shown and not judged, and it is a few thousandths of one core at every
size. The robustness tables (`results/live/V11_ROBUST_KILL.md` and `V11_ROBUST_LONG.md` on the engine that stands; each earlier engine's are its own record) add rows that belong to the omni
arm alone, since native has no governor to kill: the seconds from the kill until every setting was back at the operator's
(the allowance is 60 s, declared before the run), whether a second governor started and governed to the end, and the
governor's memory in the last ten minutes over the first ten (a quarter's growth is a leak, declared before the run); the
300 s after the kill (120 s on the tables up to omni-v14's) are compared between the arms like any paired gauge.

## The organisms with a real cluster inside (`SIX_KUBE.md`, `V3_SIX_KUBE.md`, `V3_BIG_ORGANISM.md`)

Two kinds of rows, kept apart: **the cluster** (real Kubernetes, measured) and **the organism** (the modelled stacks
around it, evidence S). "Organism behind its window (s)" is shown and not judged; a repetition reads **OFF THE CLOCK**
when either arm ended more than 5% of its window late (its last steps saw a cluster whose load had already ended). The
pairing stands, the mark stays, and the remedy is a longer window for that size on that machine.

## The one number (`results/OMNI_INDEX.md`)

Every measure is a ratio oriented so that above 1 is a GAIN for Omni-Compass on top of native: work, speed, machines,
energy. A test's index is the geometric mean of its ratios, a category's of its tests, the headline of the real
categories, each weighted the same. A measure enters only as its three-run reading allows: GAIN, LOSS or power given in
all three of our runs enters as the geometric mean of the runs' ratios; anything else (STEADY, the runs disagree, a word read by
the mean of our three runs) enters as exactly 1. Modelled muscles are shown beside the index, never inside it.

## The real test, the twenty scenarios and the whole organism

- **The real test** (`results/orchestrator/V18_THREE_ARMS_ABC.md`): one row per pair and gauge, each run's own word beside its
  number, the three-run reading in bold; below, each arm's totals in each run (requests answered, failed, wrong). The bottom line
  on the README and the live benchmark engine page reads its pair Omni-Compass on native against native, takes the work row's mean of the
  three runs as its number and turns its light red on any slower service or failed request. The record's third arm, Omni-Compass
  alone on the muscles, is not carried there: Omni-Compass is never by itself (the founder's order of 25 October).
- **The twenty scenarios** (`results/scenarios/SCENARIOS_20.md`, class S): ten organisms, each native and with Omni-Compass on
  native. The first table gives native's own gauges and Omni-Compass on native's word and mean change against native; the
  sections after it give every run's change with its interval and the reading, each arm's own gauges, the realms runner's
  contrasts, and every LOSS row by name.
- **The whole organism** (`results/WHOLE_SYSTEM.md`): each layer's ratio oriented so that above 1 is a GAIN, composed by the
  product law R(g) = ∏ℓ Rℓ(g); read the scope (with or without the card's old run) and the reading (by the index's rule, or
  every interval carried) before the number. It is a model of measurements, class S of class L and P, and its index is not a
  price.

## The seven organisms grid (`results/grid_v5/GRID.md`; each engine's runs in `results/grid_v<engine>/`)

Columns are **copies × runs**: 1, 10 and 100 clustered copies, each at 1, 10 and 100 paired runs, and on GitHub's own
machines 1,000 of each as well (paid cloud and card runs stop at 100). Rows are the seven organisms: the spine, the four
realms, the four stacked and the whole tower. Each square shows the modelled value and the value with the real cluster
inside. Read a square as "with Omni-Compass on top, against native, at this many copies, over this many runs". A square
still running says so, and one beyond a free runner's memory or time is listed as pending runner capacity, never rented.

## Kubernetes at scale (`KWOK.md`, from the `kwok-scale` workflow)

Real Kubernetes at 50, 500 and 1,000 nodes (KWOK nodes: real Kubernetes objects with no machines behind them):
- **decision time** is how long Omni-Compass takes to decide, at that size;
- **memory** is what it uses;
- **master switch** must read "yes": everything handed back.

## One number, one word (`docs/BENEFIT_SHEET.md`)

In the tables a change keeps its raw sign: a response time that fell reads "-65%", a cache that grew reads "+300%", and
the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for (the key above). The benefit sheet turns
every gauge the same way round against **its declared aim**: plus is a GAIN, minus a LOSS or power given, whatever the
gauge measures, and 0% is STEADY. Beside it every change the same in all three of our runs is
written out in words, never as a bare sign: "p95 cut 65% (GAIN)", "memory ceiling held up 215% (power given)", so
neither can be misread against a table that shows the same changes as "-65%" and "+215%". One number per benchmark, by
the index's own rule, with its word beside it. Read that sheet first; read the tables for
the rows behind a number, and read their Reading column, never the sign alone. The wiring page uses the same words.

## Wire in, or watch (`docs/WIRING_VERDICTS.md`)

One of three words per knob, by one rule from the tables above. **Write**: a gauge GAIN in all three of our runs
and none LOSS or power given in all three of our runs; Omni holds the knob. **Watch**: nothing GAIN in all three of our runs; the knob stays native and Omni only
reads it (one wire out, no wire in), and a loss in all three of our runs is named with its cause. **Operator's choice**: gains and losses both the same in all three of our runs, a trade, shown with both readings of the index. Rows marked "shown, not judged" never count. A modelled
muscle takes its word from its label: superior is write, a tradeoff label is the operator's choice, the rest is watch. The
CSV beside the page (`results/WIRING_VERDICTS.csv`) has one row per knob and per muscle.

## Where to start

1. `docs/STATE_OF_PLAY.md`: one page, every result and how strong it is.
2. `docs/DOSSIER.md`: every result with its chart.
3. This chapter, next to the table in front of you.
4. `DISCLOSURES.md`: what a result is and is not.

## Reading the benefit: more work, or the same work for less

With the work held equal in both arms, the gain from Omni-Compass on top is *G = C[native] / C[omni] − 1*, where *C* is a
resource (machine-hours, CPU core-hours, joules). The same work then needs *1 / (1 + G)* of the resources, a saving of
*G / (1 + G)*: a third more work is a quarter off the bill. The full explanation, the three rules for reading a receipt
and where every number stands today are in the Owner's Manual, chapter 3, *Where the Value Comes From*
(`docs/OMNI_COMPASS_OWNERS_MANUAL.md`).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
