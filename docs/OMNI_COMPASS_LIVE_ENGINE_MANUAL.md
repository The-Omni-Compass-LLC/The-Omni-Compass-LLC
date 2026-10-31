# THE OMNI-COMPASS LIVE BENCHMARK ENGINE MANUAL

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## How to Read the Live Benchmark Engine: Its Monitors, Gauges and Knobs, Native beside Omni-Compass

**October 2026**
**The Omni-Compass LLC**

All patents, copyrights and trademarks covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.

---

# FRONT MATTER

## The Problem and the Answer

**What the whole industry faces.** Every computing system in service, from one server to a cloud region, from a GPU to a
building's chillers, a grid feeder or a robot cell, is run by a stack of native controllers: the Kubernetes autoscalers and
scheduler, the cloud's node pools, the GPU's power and clock firmware, the database's cache and connection pools, the
building's cooling loops, the battery's management system, the servo's loop. Each was designed and tuned alone, against its own
setpoint, with margins sized for the worst case it might meet. Three costs follow, on every stack:

1. **Capacity held idle.** Worst-case margins stay in place through the common case. Machines, power caps, caches and cooling
   run far inside their limits, and the room between the operating point and the limit is paid for and seldom used.
2. **Late reaction.** Reactive loops act on averaged, lagging signals and wait out deliberate cooldowns, so queues and
   response-time tails form before capacity arrives.
3. **Loops at cross purposes.** The loops share power, cooling, connections and memory. One loop's correction is another
   loop's disturbance, and no loop sees the whole.

Demand for computing, above all for AI and the cloud, is growing faster than the power, cooling and hardware that can be built
for it. The usual answer is to add: more machines, more power, more people watching thresholds. Replacing the native
controllers is not an answer most operators will take: they are proven, often certified, and the people on call know them.

**What Omni-Compass does about it.** Omni-Compass is a supervisory governor. It sits on top of those native controllers and
never replaces them. It plugs into each setting a native controller already exposes, through a two-way plug (one wire in, the
reading; one wire out, the setting), takes a snapshot of every setting before its first write, and governs the whole stack as
one body, the organism: every muscle driven as far as its own limit and never past it, and, on the engine that stands, never
below native; where it cannot bring a muscle a GAIN, that muscle stays native. It acts before a line is crossed instead of
after, reads back every write, puts every give-back to its own trial, records every decision with its reason, walks every
setting home if it stops (the lease) and stops at once on the kill switch. Its first rule is do no harm, judged at the
organism: never less work or health than native (`DISCLOSURES.md`, section 3). The aim is the one headline: more work,
faster, on fewer machines, with less energy, from the hardware and the controllers already in place; in a cloud, the same
work for a smaller bill.

**Where the page shows it.** The live benchmark engine page plays every benchmark back from its own SHA-256-checked files, native
beside Omni-Compass on top of native, lane by lane, and runs the engine's own runs in the page: the Python's seeded runs, and
the same runs through the engine's C++ twin, side by side (the page's section 5b). This book reads that page; the mechanism and every
result are in the Owner's Manual.

**What is not claimed.** No new physics, no new model of computation, and no promise for any system Omni-Compass was not
run on. It does not make a system immune to failure, delay or drift: it keeps each muscle inside its own limits and shows, row
by row, what it did against native. A result on another system is that system's own, from its own paired runs; where it
differs, the first presumption is the wiring (`DISCLOSURES.md`, section 4).

## What This Is: a Benchmark Engine

The Omni-Compass Live Benchmark Engine is a benchmark, analysis and audit engine. It runs Omni-Compass on top of native across the
organisms, clusters, software, chips, clouds and muscles of the technical world, and shows every benchmark: native against
Omni-Compass on top of native, on the same work. **Native** is the stack as it runs today, by itself: its fragmented organisms of
muscles (processors, memory, machines, pods, caches, queues, power) run by Kubernetes and the open-source orchestrators,
schedulers, autoscalers, governors and managers the industry runs them with. **Omni-Compass** is the supervisory governor placed on
top of that native stack; it never replaces it. Every number on the page traces to its run's own files and the code that scored
it, so anyone can rerun and audit it: real, open-source software on real machines (class L), a physical meter (class P), or our
own models, marked as such (class S).

Only what could be run and proven was benchmarked. Where a system could not be seen, run or measured, it is not shown, and nothing
is claimed for it. The rest of the story is written when others benchmark Omni-Compass, critique it and analyse it on their own
systems; that work needs to be done and will be, and its results are theirs to publish. No outside party has reviewed or approved
the results in this manual or on the page.

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

**How to read a number beside a word.** The word comes first and settles the direction; the number is the size, and it wears
the word's sign so the two never pull apart: GAIN 29.6% on pods waiting means 29.6% fewer pods waited than under native (a fall
in waiting is the gain, so it is written with the plus of the word, never with the minus of the gauge); LOSS 2.3% on alert
minutes means 2.3% more minutes over the line; STEADY 0.3% means a change under the 0.5% floor; power given 3.1% means 3.1% more
of a resource put in to buy the work beside it. The gauge's own direction is never hidden: on the page, hover any word or any
coloured number and it says what the word means and why the number wears its sign, and where the page knows the gauge, what rose
or fell against native (the page's appendix D, "Size, Sign and Raw Change").

## What You Are Looking At: Omni-Compass, Hooked Up, and How to Read Its Report

**A live tuning engine, and one tuned engine.** The page is the **live tuning bench**: the interface that operates the engine's
controls and displays their effects through the connected backend. Every knob, button and monitor on it turns in real time,
native alone, Omni-Compass on top, or both, and **any knob can move every metric, up or down**. Every benchmark is one engine at
one profile, the **factory profile**; any other setting shows the engine's range, never a benchmark result (the box that opens the page's appendix G,
`#tuningBench`; chapter 41). The words used here for the engine, its profiles and its bench are written once, in
`docs/FACTORY_PROFILE.md`, and this book uses them exactly.

**What the live benchmark engine is.** The live benchmark engine is one web page, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, built by the
repository's own code (`docs/engine/build_live_engine.py`) from the engine that stands and from the repository's own
results. It is a monitor of the engine and of the benchmark runs GitHub ran: every number on it is read from a record the
repository holds (a three-run table, a run's raw files, the engine's own audit, the realms table, the models' own readings),
and every word on it (GAIN, STEADY, LOSS, power given) is that record's own reading under `tools/readings.py`. The page decides
nothing about any result and types nothing in. Where it plays the repository's own models (evidence class S) it says so, and
a model is never proof.

**What "native" and "Omni-Compass" mean on the page.** *Native* is the **native baseline**: the whole system running by itself,
every autoscaler, scheduler, firmware, thermostat, orchestrator and controller it ships with, every muscle wired and moving by
its own machinery. It is drawn in orange. *Omni-Compass* (on the page also *Omni-Compass and native*, or *Omni-Compass on
native*) always means Omni-Compass on top of native: the same whole system with all of that still running underneath, and the
governor on top of all of it, wired in through the two-way plug. It is drawn in blue. There are two sides everywhere on the page,
and only two. Omni-Compass is never by itself: it always sits on top of a native controller,
on muscles that have their own, so no monitor, table, record or button shows a third. Red is never a side: it is only LOSS and the
alarm.

**What a monitor is.** The page is laid out as an operations monitor is: a wall of tiles first (the
monitor wall), each tile a small copy of a monitor further down the page, with the control panel under it; then the results;
then the monitors themselves, section by section, each with its own knobs in a line at its head ("Controls") and a strip under
it; and last the appendixes, where the page keeps its explanations. A knob marked *Live* acts on the live benchmark engine, the engine's own mathematics running in
the page; a knob marked *Recorded data* only chooses which record is shown and never modifies it. Every monitor shows native
beside Omni-Compass on the same demand, the same seconds, so the one difference left between the two sides is Omni-Compass.

**What a gauge is.** A gauge is one measured quantity of the system (the work waiting, the work done, a response time, the
machines in service, the energy drawn, a bill). On the page each gauge is drawn for both sides with its paired reading: the
change from native, its 95% interval, and its word. The word is decided by what the gauge is for (the key, above), never by the
sign of its number.

**How to read the page, in order.** The page opens on the monitors: the monitor wall (the page's section 0), every monitor
live in five blocks, and directly under it the control panel (the page's section 1), with the kill switch, the fuse box, the
mechanism's knobs, the runs, the reports and the manuals. Then come the contents; then Part 2, the results (the scorecard, the
benefit against native, the benefit board, the LOSS register and the status board); then Part 3, the live operation of the
engine (the live organism, the golden signals and the event log, the console, the heartbeat dial, the control cycle, the phase
plane and scoreboard, the brain's state, the verdict and the dashboards); then Part 4, the real runs and the platforms (the
Kubernetes run playback and its telemetry, the controller's decision trace, the clouds, the orchestrators, the GPU and the CPU,
the pipeline); then Part 5, the proof and the models (the Python's runs and the Monte Carlo, the C++ twin, the scenarios and the
injection grid, the whole organism, the measured effect, the telemetry analytics, the master switch's wiring, the specification,
the failure modes and the page's own rendering); and last the appendixes A to G (the title page and build, the reading guide
with every section's explanation, the problem and the answer, the executive summary and the reading key, the monitor list, the
glossary and index, and the disclosures). This manual reads the page in the same order, one chapter for each section.

**What this manual is, and is not.** It is the interpretation of the page: how to follow the dashboard, read each gauge, turn
each knob, and see the mechanism of action of Omni-Compass against native as the monitors show it. It defines every control,
its backend, its effects, its limits, and the distinction between factory and active settings, in the words of
`docs/FACTORY_PROFILE.md` (chapter 6). Nothing in it decides a result: the records of authority are the repository's result
files, the raw files GitHub archived with their SHA-256 lists, the two other manuals and `DISCLOSURES.md`.

## Notice and Disclaimer

This manual describes the live benchmark engine page as `docs/engine/build_live_engine.py` builds it on the engine that stands
(omni-v22, `OMNI_V22.json`). The page names its engine on its own `<html>` element (`data-engine`), and the engine its words
were written for (`data-prose`); where the records stand on a newer engine than the words, a banner under the wall says so
(`#engBanner`). The build stamps the engine that stands on the page and rebuilds every record, and `--check` fails a page whose
engine differs; where the page you are reading names a newer engine, the page is right and this manual is realigned with it in
the same push. The page's own contents (`#contents`, under the control panel) are the authority on the order and the
numbering of its sections; this manual names every section by its number, its title and its anchor (`#s-wall`, `#s-ops`, and
so on), and the anchors do not move when sections are renumbered.

The published benchmarks the page plays are the record of what Omni-Compass did on the systems, loads and engine they name,
each with its evidence class. Where a result on any other system differs from them, or anything on the page looks wrong, the
first presumption is the wiring, the settings, or how Omni-Compass was implemented or read, not the law (`DISCLOSURES.md`, section 4). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Foreword

A governor that cannot be watched cannot be trusted. Every controller a stack already runs has a dashboard somewhere: the
autoscaler's replica count, the card's clock and power, the building's setpoints. What none of them had was one wall where the
whole body is seen at once, native beside the same body governed, decision by decision, with the record each number came
from one click away. The live benchmark engine is that wall, and this book is how to read it.

I asked for it to be a monitor and not a drawing: every record on it made again by the repository's own code, every raw file
checked against its own SHA-256 list before a byte of it is drawn, every word on it the run's own reading and never one drawn
from the stream. So the page can be trusted the way a meter is trusted: it shows what the record holds, and when the record
has nothing yet (a cloud set still running, a chip run not yet started) it says so and shows nothing in its place.

Read the key first. Then stand at the wall: the page opens on it, the control panel under it, and every reading that went
against native is raised on the status board before anything that went for it. If a tile reads LOSS, this book
tells you where its record is and what to do: the row stays, its cause is found (our wiring first, native's setup second, the
scoring third), and the test runs again. Nothing on the page is pushed toward GAIN; the only thing forced is the mechanism.

## The Three Manuals: the Operator's, the Owner's and the Live Benchmark Engine's

Three books stand in the repository, each for a different reader, and each says what it leaves out.

| Book | For whom | What it carries | What it leaves to the others |
|---|---|---|---|
| The Operator's Manual (`docs/OMNI_COMPASS_MANUAL.pdf`) | the engineering team that embeds, wires, tunes, runs and checks Omni-Compass on a stack | the plug, the wire check, the eight levels, every stack, the switches and the lease, the implementer's guide for the cloud, every muscle's wiring and card | nothing on how the engine is built; no benchmark results |
| The Owner's Manual, the master (`docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`) | whoever owns or licenses Omni-Compass and must know the whole mechanism | the philosophy, the mathematics, the mechanism, the engine's source, every result, the wiring | nothing: it is the master |
| The Live Benchmark Engine Manual (this book, `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`) | the operator at the dashboard | how to follow the live benchmark engine page: its monitors, gauges and knobs; every control, its backend, its effects, its limits, and the factory against the active settings; and the mechanism of action native beside Omni-Compass as the monitors show it | how the engine is built (the Owner's); how to wire it (the Operator's) |

A reading on the page and a reading in a receipt are the same reading: the page draws the receipt. Where this book and a
receipt seem to differ, the receipt governs, and the page is rebuilt.

## Preface: How to Use This Manual

| You are | Read |
|---|---|
| The operator on shift, at the wall | the Quick Reference card; chapters 1 and 2 (the wall, the control panel and its kill switch); chapters 8 and 10 (the status board, the golden signals); chapter 44 (when a tile reads LOSS); Appendix E |
| CTO, architect, head of platform | the front matter; chapter 4 (the scorecard); chapter 6 (the benefit board); chapter 28 (the whole organism); chapter 42 (the mechanism of action, side by side); chapter 45 (what the page does not tell you) |
| CEO, CFO, CIO, board member | the front matter's "The Problem and the Answer"; the Foreword; the front matter's "Disclosures, Declarations and Disclaimers"; chapters 4 and 5 (the scorecard, the bill by route); section 2.10 (each deployment route's bill); chapter 28 (the bills and receipts, every way a stack is bought); section 6.4 (one figure for the whole board); chapter 21 (the bill in a cloud) |
| Site reliability engineer, on call | the Quick Reference card; chapters 8 and 10 (the status board, the golden signals, the event log, the OpenMetrics exposition); chapter 18 (the heart and the two tickers); Appendix C |
| Control or plant engineer | chapters 13 to 16 (one control cycle, the phase plane, the brain's state, the verdict); chapter 32 (the component specification); chapters 2 and 11 (the control panel's mechanism knobs, the console) |
| Auditor, diligence team | chapter 35 (the title page and build, and the records); section 2.7 (the profile and its fingerprint); chapter 43 (from a tile to its record); chapter 47 (verifying the page); the page's own appraisal, `docs/engine/APPRAISAL.md` |
| Procurement, counsel and attorneys | `LICENSE`, `NOTICE`, `PATENTS.md`, `TRADEMARKS.md`, `DISCLOSURES.md`, `LICENSING_FAQ.md`, `ENTERPRISE_LICENSE.md`, `SECURITY.md`, bound into this book in full (the front matter's Disclosures; Appendices F to K); chapter 46 |

**Conventions.** `code` is a command, file, anchor or switch exactly as typed. "Native" means the system as it runs today,
without Omni-Compass, drawn in orange. "Omni-Compass" means that same native system with Omni-Compass on top of it, drawn in
blue. Those are the two sides, and the only two: Omni-Compass is never by itself.
"Muscle" means a specific controllable mechanism, with its own actuator, observations, limits and read-back. "Knob" or
"lever" means one setting on a muscle; on the page, a knob is also a control in a monitor's "Controls" bar or in the control panel, and the text says which is meant. "The band" is a reading's safe range, from calm (p = 0) through its center
(p = 0.5) to its line (p = 1). "A decision" is one turn of the governor's loop. "A tile" is one small monitor on the wall. "A
section" is one numbered part of the page, named by its anchor. "The factory profile", "the active profile", "a candidate
profile" and "a custom profile" carry the meanings of `docs/FACTORY_PROFILE.md` (section 6.6). Every step that acts on the
live benchmark engine is marked **LIVE**; a step that only chooses a record is marked **RECORDED**. Every number carries its evidence
class: **P** a physical meter, **L** live software, **S** our own models (modelled). A number from a model is never written as
if it came from hardware.

**The standards every page of this manual keeps.** The page, and so this book, keeps the following discipline throughout:

1. **Native beside Omni-Compass, always.** Every monitor shows native beside Omni-Compass, the same whole system on the same
   demand, the same draw of noise, the same injected fault, at the same second. Omni-Compass is never shown as a competitor to
   the controllers it sits on, and never shown by itself: it always sits on top of native.
2. **Nothing typed in.** Every number is read from a record the repository holds when the page is built or opened; every raw
   file is matched against its run's own SHA-256 list before it is drawn; the brain, the compass law and the verdict running
   in the page are the engine's own code, ported and proven equal to the Python and the C++ on every build
   (`docs/engine/check_live_engine.py`).
3. **The record's own word.** Every word on the page is the reading its record carries under the one key; the page never
   draws a word from the stream it plays, and never prints "up", "down", "better" or "worse".
4. **Every row, LOSS included.** A reading that went against native is raised first, as an alarm, with its source record and
   the repository's root-cause document where one exists. Nothing is cut from the page because it went against Omni-Compass.
5. **Nothing read across engine versions.** The page names the engine it stands on, every record is rebuilt on the engine that stands, and `--check` fails a page whose engine differs; each
   three-run table on it names its own engine, and a table stands on an older engine only until its runs on the engine that
   stands land.
6. **Models are not proof.** Every view says its evidence class. The official Kubernetes and database runs are class L, played
   from their own checked files. The harness, the shipped controller on the modelled cluster, the GPU card's model, the Linux host's
   model, the realms table and the grid are class S, our own models, shown beside the real runs and never presented as proof.
7. **Do no harm, in its one meaning.** Every knob on the console acts on both sides alike; what Omni-Compass does with it is
   held by its guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another
   on the engine that stands, a give-back tried against native first and refused on a LOSS (`DISCLOSURES.md`, section 3).

**How this manual is organised.** It follows the page's own order, one chapter for each section of the page, each chapter
naming its section by number, title and anchor. Part I is the page's opening: the monitor wall (section 0), the control panel
directly under it (section 1, with its fuse box, its mechanism knobs and its kill switch panel) and the page's contents. Part II
is the page's Part 2, Results: the scorecard, the benefit against native, the benefit board, the LOSS register and the status
board. Part III is the page's Part 3, Live Operation: the live organism, the golden signals and the event log, the console, the
heartbeat dial, the control cycle, the phase plane and scoreboard, the brain's state, the verdict and the dashboards. Part IV is
the page's Part 4, Real Runs and Platforms: the Kubernetes run playback, the repetition telemetry, the controller's decision
trace, the cloud providers, the orchestrators and governors, the GPU and CPU hardware and the CI pipeline. Part V is the page's
Part 5, Proof and Models: the Python's runs and the Monte Carlo, the C++ twin, the scenarios and the injection grid, the whole
organism, the measured effect, the telemetry analytics, the master switch's wiring, the specification and mathematics, the
failure modes and the page's own rendering. Part VI is the page's appendixes A to G: the title page and build, the reading guide
(with the sides, the colours and the signal words), the problem and the answer, the executive summary and the reading key, the
monitor list, the glossary and index, and the disclosures. Part VII reads a result off the page: the mechanism of action side by
side, the trace from a tile to its record, what to do when a tile reads LOSS, and what the page does not tell you. Part VIII is
the license and how to verify your copy of the page. The back matter holds this book's glossary, every section of the page,
every control, every gauge on the wall, the colours and marks, troubleshooting, and the papers counsel asks for.

## Where to Get Help

| You need | Where it is |
|---|---|
| What a tile means | chapter 1 (the wall, tile by tile) and Appendix C (every gauge, its side, its aim, its word) |
| What a knob does | chapters 2 and 11 (the control panel with its mechanism knobs, the console) and Appendix B (every control, what it acts on, what it leaves alone) |
| Which profile is governing | section 2.7 (the active profile, FACTORY, CANDIDATE or CUSTOM, and its fingerprint) |
| Why a reading is red | chapter 44 (when a tile reads LOSS), then the record it names (chapter 43) and the Operator's Manual's "wired right or wired wrong" |
| Why a monitor is empty, grey or AWAITING | chapter 45 (what the page does not tell you) and Appendix E (troubleshooting the page) |
| Why the page is slow | the page's section 5j and chapter 34 (the page governs its own drawing; a chart farthest from where you are looking waits a frame) |
| What the engine is | the title block of the page (its name, digest and commit); `python3 tools/omni_version.py`; the Owner's Manual for everything inside it |
| How to wire it | the Operator's Manual, in order; nothing in this book wires anything |
| Licensing, pilots, the Enterprise License | the Contact page at the back; www.omni-compass.com |

## Prelude: A Night at the Wall

It is a quarter past two. The on-call engineer has the wall open on one screen and the cluster's own console on the other.
In the control panel under the wall the kill switch reads Omni-Compass ON, and the active profile reads FACTORY. On the
wall every tile carries its signal: green, GAINING, on nearly all of them. Native in orange on the left of each pair,
Omni-Compass in blue on the right, both moving on the same demand. The orange line of the work waiting climbs as the night's
batch starts; the blue line climbs too, then bends sooner, because the governor's ticker (the page's section 4a) shows the pedal
pushed at the first decision the compass left its center, and two machines recommended before native's autoscaler had seen its
first late sample.

A row of the status board's alarms turns red. It reads LOSS: the pod start wait, mean, +13% in one run. The engineer clicks it
and lands on the three-run table it came from: run A of the Azure steady set, 33 paired repetitions, the interval −44 to +60
seconds, *no* in the significant column. The red is that run's own word; the three-run reading needs runs B and C as well, and
this run's interval includes zero, so it is not yet beyond the noise. The row stays on the page, as every row does. The
engineer opens the root-cause document the row links to, `docs/POD_START_WAIT.md`, and reads that a pod's start on a shared
host is the test machine's own unpacking of an image, the same on both sides at the same host load. Nothing to do tonight; the
record is complete.

At three the batch is done. The blue line of the capacity held eases back a step at a time toward the orange one: the pedal
lifted, the lease walking every setting toward native. The engineer scrolls to the page's section 3f, the phase plane, and
watches sixty dots drift from the right edge back toward the middle line, native's a few decisions behind. Then back to the
wall. The kill switch green, the signals calm, the alarms empty but for the one red row that will stay until its runs B and C
land and the three of them are read together. The status board's last tile, Build Freshness, reads twelve minutes.

## Introduction: The Page, Its Monitors and What This Manual Covers

**The problem the page answers.** Omni-Compass's answer to the problem the whole industry faces (the first section of this
front matter) is a supervisory governor on top of controllers that each have their own dashboard, and the owner of the
stack has to answer one question about it every day: is it doing what the receipts say, right now, on this
body, and would I see it if it were not? The receipts are tables; a table is read after the fact. The page is the same
record played back in motion, native beside Omni-Compass, with the governor's own decisions and the native controllers' own
moves on two tickers side by side, so the mechanism is seen, not inferred.

**What the page is made of.** Four exporters build its records on the engine that stands: the realms harness (one organism and
each muscle alone; `docs/engine/export_harness_trace.py`), the shipped controller on the modelled cluster (on top of the
autoscaler at the max, and in the cloud's setting; `docs/engine/export_controller_trace.py`), the official runs read back from
their raw files and scored again by the repository's own scorer (`docs/engine/export_runs.py`, `tools/live_reps.py`), and the
chip and host models with every judged row of the newest receipts (`docs/engine/export_scenarios.py`). A fifth record is the
build itself: the engine, the commit, the time, and GitHub's own list of the runs in progress and of every run started for
the chips and the clouds (`docs/engine/github_ledger.json`).

**What runs live in the page.** The brain (`omnicompass/core.py`, integrated by the fourth-order Runge–Kutta method), the
compass law (`omnicompass/compass_law.py`) and the verdict (`omnicompass/verdict.py`) run in the page itself, ported to the
browser and proven equal to the Python and the C++ on every build. They govern a stress-test model of sixty muscles, each on
top of its own native controller, and they govern the page's own drawing (the page's section 5j). Everything else is a record
played back.

**What this manual covers.** Every section of the page in the page's own order; every gauge, with its side, its aim and its
word; every control, with its backend, its effects and its limits; the factory profile against the active one; the two tickers
that show the mechanism of action; the trace from any tile to the record it came from; and what to do when a tile reads LOSS.
It covers the page as built on omni-v22; a later engine renames itself on the page's title block and this book is realigned in
the same push.

**What this manual does not cover.** How the engine is built, its equations beyond the ones the page itself prints, the
wiring of Omni-Compass onto any stack, and the benchmark results themselves as a body of evidence: those are the Owner's and
the Operator's Manuals and `docs/STATE_OF_PLAY.md`.

## Quick Reference: The Card for the Glove Box

Keep this card beside the screen that shows the wall. Every line is explained in the chapter named beside it.

**The sides** (chapter 36). Orange is native, the system by itself. Blue is Omni-Compass on top of native. Two sides, and only
two: Omni-Compass is never by itself. Violet is a knob or a profile turned from the factory tune, never a side. Red is never a
side.

**The three words** (the key). Green GAIN, yellow STEADY, red LOSS (the word itself shaped as a stop sign, white on red). A
resource that rose is *power given*, blue. White with a dashed edge is *the runs disagree* or *the runs differ*; grey is
*shown, not judged*; neither is a reading. A change of 0.5% or more is a change and carries its word; under 0.5% it reads STEADY.

**The signal words** (chapter 36). On every monitor, section, part, breaker and in the dock: green GAINING (round), yellow
STEADY (a yield diamond), red REDLINING (an octagon, a stop sign, blinking), and a dark AWAITING where a monitor's run has not
landed, never green.

**The scorecard** (chapter 4). One light and one number for each way to run it against native, and the whole workload's
index on each route.

**The kill switch** (section 2.28). The first row of the fuse box, the head of the control panel's third panel (the page's section 1),
every monitor's strip, every section's controls and the dock. Green ON: the governor's outputs reach the muscles. Red: engaged, every setting
handed back to native at once, the decisions shaded red. White OFF: every Omni-Compass side follows native in a tint of
native's colour. "Return to native" in the control panel is the reset, a separate button with the same effect on the page
(chapter 2).

**The profile** (chapter 2). The active profile reads FACTORY, CANDIDATE or CUSTOM, with its fingerprint. The factory profile is
the released one, omni-v22's, the heartbeat 60 s; nothing is held when the page opens. *Restore factory profile* puts the
mechanism and the heartbeat back; *Hold the active profile* holds every knob as set; *Try the candidate* applies the sweep's best
beat as a candidate, never a release. The heartbeat has seven buttons, 10, 15, 20, 30, 60, 90 and 120 s; the fuse box's tabs add
the live model as Prometheus metrics and every press as the request a running governor takes.

**The status board** (chapter 8). Every reading that went against native, worst first, each with its source record and its
root-cause document where one exists; filters: All, LOSS, the runs disagree, live now, guards and open items, GitHub.

**Where a number comes from** (chapter 43). Click the tile: its monitor names the table, the run and the file, whose SHA-256
was matched before it was drawn (the tables in `results/live/`, the raw files on the `raw` branch).

**When a tile reads LOSS** (chapter 44). The row stays. Read the three-run reading, not the one run. Open the root-cause
document. The cause is found in this order: our wiring, native's setup, the scoring. The test runs again. Nothing is tuned
toward GAIN; where Omni-Compass cannot bring a knob a gain, that knob stays native.

**The console** (chapter 11). Every knob acts on both sides alike: demand, noise σ, sense delay +0 to +6, four faults of 40
decisions, the dial, the load profile, the frame load, the time, the day, every knob to its start.

**The age of the page** (chapter 8). The status board's Build Freshness tile. The page is rebuilt by GitHub on every change to
the engine, a model or a result, and every three hours (chapter 24).

**What the page is not** (chapter 45). It decides nothing. Class S views are models, not proof. The records of authority are
the result files, the raw files and their SHA-256 lists, the manuals and `DISCLOSURES.md`.

## Table of Contents

Part I. Monitor Wall, Control Panel and Contents: 1. Monitor Wall; 2. Control Panel; 3. Contents: the Page's Order and Its Numbering.
Part II. Results: 4. Scorecard; 5. Benefit Against Native; 6. Benefit Board; 7. LOSS Register; 8. Status Board.
Part III. Live Operation: 9. Live Organism; 10. Golden Signals and Event Log; 11. Control Console; 12. Heartbeat Dial; 13. Control Cycle; 14. Phase Plane and Scoreboard; 15. Brain State; 16. Verdict; 17. Dashboards.
Part IV. Real Runs and Platforms: 18. Kubernetes Run Playback; 19. Repetition Telemetry; 20. Controller Decision Trace; 21. Cloud Providers; 22. Orchestrators and Governors; 23. GPU and CPU Hardware; 24. CI Pipeline.
Part V. Proof and Models: 25. Python Runs and Monte Carlo; 26. C++ Twin; 27. Scenarios and Injection Grid; 28. Whole Organism; 29. Measured Effect; 30. Telemetry Analytics; 31. Master Switch Wiring; 32. Specification and Mathematics; 33. Failure Modes and Controls; 34. Self-Governed Rendering.
Part VI. The Page's Appendixes: 35. Title Page and Build; 36. Reading Guide; 37. Problem and Answer; 38. Executive Summary and Reading Key; 39. Monitor List; 40. The Glossary and Index; 41. Disclosures, Law and Contact.
Part VII. Reading A Result off the Page: 42. The Mechanism of Action, Side by Side; 43. From a Tile to Its Record; 44. When a Tile Reads LOSS; 45. What the Page Does Not Tell You.
Part VIII. License and Your Copy: 46. License and Commercial Terms; 47. Verifying Your Copy of the Page. Back matter: Glossary; Appendices A to L; Index; Contact.

---

# PART I. MONITOR WALL, CONTROL PANEL AND CONTENTS

## 1. Monitor Wall

This chapter reads the page's section 0, **Monitor Wall** (`#s-wall`).

### 1.1 What the wall is

The wall (the page's section 0, `#s-wall`) is every monitor of the page in one view: the same canvases the sections draw, copied
small four times a second, so nothing is drawn twice from different data. Every tile carries at its top its number and its title
in capital letters, what the monitor shows, and under them its section and its state (live, replay, from the records, a model, or
awaiting its run), so a tile says where its monitor is and what it represents before it is opened. Click a tile and the page
scrolls to the monitor it copies. The page's own governor (the page's section 5j, chapter 34) leaves a monitor resting while it is
off screen; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to, and while the wall
is in view the resting monitors are drawn in turn, one a frame, each by its own drawing code; a tile with the accent border is a
monitor on screen now.

Under the wall a line, **Monitor Lights** (`#wallLamps`), counts the lights (section 1.3). The section's controls line reads:
click a tile to open its monitor; every tile is read four times a second. Directly under the wall stands the control panel (the page's
section 1, chapter 2), whose first panel holds the button that puts back the factory tune.

### 1.2 The numbered monitors and the five blocks

Every monitor of the page (every chart canvas) carries its number in a badge above it. The number is the monitor's place on
the wall (the page's section 0), which shows every monitor at once in five blocks, each under its own heading and read left to
right, then the next row: 1, **Benefit and Organism** (twelve monitors, three rows of four on a laptop); 2, **Real Runs on
GitHub**; 3, **Brain and Mechanism**; 4, **Clouds, Chips, Orchestrators and Scale**; 5, **Proof and Telemetry**. The first four
monitors are the recap: the benefit board (monitor 1, *Benefit by Domain*), the whole organism (2, *Stack Composition*), the
market map of every three-run table (3, *Market Map*) and the benefit gauge by gauge (4, *Benefit by Gauge Family*). A click on
a tile scrolls to the monitor it copies. Two monitors that sit side by side in their section, native beside Omni-Compass, sit
side by side on the wall too: a pair never splits across two rows, on the wall or on the page at any width. Each badge names its
section, so a monitor and its section read each other both ways. The monitor list (the page's appendix E, chapter 39) gives
every monitor by its number; the whole wall is also a Grafana dashboard (`deploy/grafana/omni-compass-wall.json`), its panels
numbered as the page numbers its monitors, one row for each block. Appendix L lists every monitor under its number.

### 1.3 The light on every monitor

Each tile and each monitor carries its light as a signal under its number, on the left, standing like a traffic signal: red on
top, an octagon like a stop sign, yellow in the middle, a yield diamond, green at the bottom, round; one lamp is lit, and on the
page the word beside the number (GAINING, STEADY, REDLINING, OVER THE LINE or AWAITING, section 36.5) says which. **Green,
GAINING**: low in its band with room to climb, or a GAIN. **Yellow, STEADY**: inside its band, or level with native (a change
under 0.5%). **Red, REDLINING**, blinking red and black: at the top of its band and holding there, or a LOSS row in its record
(every row stays); REDLINING comes before the line: a gauge within 3% of the top of its band, or whose slope over its last
readings reaches it within 3 readings. **Red, OVER THE LINE**, blinking red and white: past the top of its band. **Dark,
AWAITING**: the run that fills it has not landed. **Grey, NO LINE**: a monitor with no line to cross (a bill, a count of runs,
a digest check) or no reading yet; neither dark nor grey is ever counted green. A monitor that draws the organism's two sides carries three lights in one button: native's and Omni-Compass's, each
read from its own side on the same load, and between them the reading now, Omni-Compass against native by the key (GAIN green,
STEADY yellow, LOSS red), each by whether the gauge helps or hurts the muscle and the organism, never by its sign: fewer muscles
over their line, fewer pods waiting, or a 95th percentile faster by 0.5% or more is GAIN, and a 95th percentile within 0.5% of
native's reads STEADY. So the moment one side turns a colour the other does not is seen as it happens; a live light compares that
moment, and the judged readings stay in the record's tables. Click the button for each side's reason; a red or yellow one offers
the way back to the factory tune, because a light the knobs turned is a light the factory tune puts back. A line is a health
requirement in the words of `docs/FACTORY_PROFILE.md`: a service limit, a resource bound or a hardware limit.

The light reads the series the monitor draws and adds no number: on the live benchmark engine, the muscles against their lines; on a
cluster replay, the pods waiting for a place and the 95th percentile against native's at the same moment; on the heart, the
decision's own time against half its beat; on the CPU host, the busy share against the 75% line; on the card, the draw against
its power limit; on the page's own governor, the time between frames; on the proof, the page's runs against the Python's (green
when the digests match, red when they differ); on the governors and orchestrators, their own three-run tables; on a record, the
judged rows of the newest tables (a LOSS row lights red and stays). A light fed by our own models says so (class S). Under the
wall the line **Monitor Lights** counts the green, yellow, red, dark and grey lights, names every red one, names the two-sided
monitors whose native side is red, and gives each live comparison against native once (**Live Comparison Against Native**),
beside the engine's own last entry on its side and the **Redline Reflex**'s hand-backs on the live model. The three-reading projection is the light's own: the brain's law acts on the position inside its band and damps on the
position's rate of change, with a fail-up at the band's 95% wall; it projects nothing ahead.

What the page's organism is. The sixty muscles replay the repository's own model (`realms/harness.py`, class S) under the climb,
whose load steps past what the fixed muscles can carry; at the top of the climb both sides cross their lines, because no
controller makes capacity that is not there and this model adds no machine. Native in every benchmark is the system's own
automatic controllers as shipped, with nobody turning a knob, the same as Omni-Compass; where a person would step in, the record
says so and shows the crossing.

### 1.4 Every monitor's strip and wiring

Under every monitor a strip carries its knobs: the kill switch; *Inspect* (its light's reason, its feed and the query an
operator's Prometheus would ask, its wiring, and downloads of its data as CSV, the page's live metrics in the OpenMetrics format
and its registry entry as JSON, as Grafana's panel inspector gives them) and *Full screen* (the key `v` over a monitor; Esc to
leave); the console's knobs where the monitor is live, its own buttons where it replays, and the factory button.

**Every monitor's wiring.** Under every monitor one line names its wiring (`docs/engine/monitors.json`): the page's own code, the
Python it ports or reads, the C++ twin or why there is none, the checks that hold them equal, each file linked at the build's
commit, and how it moves; the monitor list carries the same. A live monitor runs the page's port of the engine, held equal to the
Python by `docs/engine/check_live_engine.py` and the Python to its C++ twins by the parity tests; a replay plays a record the Python
wrote, held equal to its source by `docs/engine/check_records.py`; a record reads a measured table as written, so no C++ applies.

### 1.5 The motion meter

The page watches itself as the viewer sees it. Every monitor in view is photographed small once a second;
one whose picture changed in the last three seconds reads **● moving** on its badge and in its row of the list, one in view for
three seconds without a change reads **● still** (and says so when the engine is paused). A monitor off screen rests, as the page's
own governor rests it (chapter 34), and its row keeps what it did when it was last in view; the note under the list counts the
monitors seen so far and how many of them moved. Scroll the page once from top to bottom and every row reads what its monitor does.

### 1.6 The keys and the kiosk

The key `?` shows the card **Keyboard Shortcuts**. `v` puts the monitor under the mouse full screen and Esc leaves it; `k` is the kiosk, the wall
and its control panel alone (`k` again to leave); `p` pauses or runs; `s` steps one decision; `f` puts back the factory tune; `w`
goes to the wall; the number keys 1 to 4 go to the four parts of the main matter, Parts 2 to 5. The kill switch is never on one key: it is its own button, on every monitor, in
the dock and in the control panel.

## 2. Control Panel

This chapter reads the page's section 1, **Control Panel** (`#s-health`).

### 2.1 What the section holds

The control panel (the page's section 1, `#s-health`) stands directly under the wall and switches every monitor of the page.
It holds three panels, in this order. **Wall Status and Factory Tune** gives the wall's state in one line and the one button
that puts back the engine's tune as it ships (section 2.2). **Fuse Box** (`#fuseBox`) switches every monitor from one box: its
master rows, the governor request, its seven tabs, the heartbeat, the profile box, the sweep over every beat, the mechanism knobs,
the twenty scenarios and the injection grid, one breaker for each monitor, the Prometheus metrics and the governor's commands
(sections 2.3 to 2.26). **Operator Controls** (`#ctlPanel`) holds the kill switch, the
buttons that run the Python's runs in the page, the jump generator, the variation switchboard, the four reports, the three manuals
and the wall as a Grafana dashboard (sections 2.27 to 2.32). The section draws no monitor of its own: the master switch's wiring
is the page's section 5g (chapter 31) and the monitor list its appendix E (chapter 39). No value here is typed in: each is
computed at runtime from the live benchmark engine or from the repository's records embedded at build time.

### 2.2 Wall Status and Factory Tune

The first panel's head line (`#wallNote`) says how the wall is drawn: how many monitors it holds, in how many blocks, how
many are on screen now, and that the rest are drawn in turn while the wall is in view. Beside it a button reads **Back to the
factory tune**: one button, wherever the knobs were turned, puts back the engine's tune as it ships (`DISCLOSURES.md`, section 3:
the max, Omni-Compass ON, demand ×1, no noise, no added delay, no fault held, every muscle driven, speed 1×) and the page's plant
at rest (section 11.2). Native alone is not a tune: it is the kill switch, beside it on the console and at the head of the third
panel (section 2.28).

### 2.3 Fuse Box: its rows and its tabs

The fuse box (`#fuseBox`, the second panel of the control panel, the page's section 1) switches every monitor from one box,
laid out as a console. Its first row is the master switches, always in view: each acts on the whole page at once, through the same code as
the console and the dock, both sides alike. Under it stand seven tabs, one shown at a time:

| Tab | What it holds |
|---|---|
| **Drive** | the plant's conditions and faults, the breakers' two buttons, the factory button, your own system, the keys; the heartbeat; the sweep over every beat and the candidate; the profile's three buttons and the profile box (the active profile, the backend, the actuation, the contract and each deployment route's bill) |
| **Mechanism Knobs** | the engine's own constants (sections 2.11 to 2.23), one group at a time: a row of group buttons above the knobs names each group, from the four pieces to every muscle (sections 2.14 to 2.22), with *All Groups* for all of them at once |
| **Scenarios and Injection Grid** | the ten organisms, each native and with Omni-Compass on native, and the injection grid: every governor, 1 to 500 runs × 1 to 500 organisms on the Python's batch (section 2.24) |
| **Monitor Breakers** | one for every monitor, by section (section 2.24) |
| **Prometheus Metrics** | the live model printed as a Prometheus endpoint, every decision, with the series a running system serves beside each and the PromQL the Grafana wall draws it with (section 2.25) |
| **Commands** | every control beside the request a running governor takes for it, with its role (section 2.25) |
| **All Tabs** | the whole panel at once, as one long box |

The tab chosen, and the group chosen among the mechanism knobs, are kept in the viewer's own browser only, as a convenience;
the page opens on *Drive* without them. The fuse box's guide and the mechanism knobs' guide stand in the page's reading guide
(appendix B, under *1 Control Panel*), so the controls come first.

Between the master row and the tabs stands one line, **governor request**. After every press it shows the
request a running governor would take for it through its control panel (`tools/omni_control.py`), with the role the request
needs: a heartbeat button, `POST /v1/beat {"seconds": N}`; Return to native, `POST /v1/reset`; the kill switch, `POST /v1/kill`
(and back on, `POST /v1/arm`, two holders of the security role within ten minutes); the dial, `POST /v1/dial`; Restore factory
profile, the dial at the max, the factory beat, every muscle driven and autopilot. A control that acts only on this page's own
model (the plant's conditions, the faults, the time, the body, the view) says so: it has no request. The page sends nothing
anywhere; the line is the request written out, `$OMNI_PANEL` the panel's address and `$OMNI_TOKEN` the operator's token. Every switch is written to the control event log with its decision (the page's section 3c), and
the line at the panel's head counts the breakers by their signal word and the monitors rested, and names the Omni-Compass side:
on top of native, or native's own under the kill switch.
The panel is the bench of `docs/FACTORY_PROFILE.md`: its controls operate the stated backend and show its response.

### 2.4 The master rows

The first row: **kill switch** (it reads "Omni-Compass ON · press to hand back to native", and engaged, "ENGAGED · Omni-Compass
OFF · native alone"; section 2.28); **tune dial**, *the max* or *tune-down*; **body**, *harness, each muscle alone*, *harness, one
organism* or *the live model*; **time**, 1×, 4×, 16×, 60×, *Pause* and *One decision*.

The second row: **demand**, ×0.25 to ×2 the day's own; **noise**, σ 0 to 0.6; **sense delay**, +0 to +6 decisions; **faults, 40
decisions**: *Surge ×2*, *Lose half*, *A sense blind*, *Security hold*; **breakers**: *every breaker ON*, *rest every monitor off
screen*; **factory**: *Back to the factory tune*; **your own system** (section 2.25); **keys**: *Keyboard keys* and *Kiosk*.

The dial, the demand, the noise, the sense delay and the faults act on the live stress-test model; turning any of them while the
harness plays moves the live benchmark engine to the model, and the control event log says so.

### 2.5 The heartbeat period: six buttons

The third row, **heartbeat period**, is the heartbeat, the governor's full decision: seven buttons, **10, 15, 20, 30, 60, 90 and 120 s**, and nothing else
(`BEATS`). The factory profile's beat is 60 s; 15 s is the standard of native's own pod autoscaler, which checks every 15 s; the
10 s button shows a beat below that standard. Pressed, a button sets the beat of Omni-Compass on the live stress-test model
(moving the live benchmark engine to the model if the harness plays), moves the heartbeat sweep monitor (the page's section 4a) to the same
beat, and is logged with its decision.

The live model steps every 15 s of the plant (`STEP_S`), native's own autoscaler check. At a beat of 15 s one full decision lands
in every step; from 30 to 120 s one lands every two to eight steps; at 10 s two full decisions land in every other step, both on
that step's reading, their pushes compounded (`BEAT_N`). Between full decisions the fast checks act: at the max a muscle past its line
has capacity added at once by the reflex (on the tune-down it goes back to native's setting), and otherwise its setting holds
while native may still raise its own. The note beside the
buttons says what the beat in force does on the live model, for example "60 s now, the factory's: on the live model the full
decision every 4 steps of 15 s; the fast checks and native's own 15 s check between".

Its backend is the page's live model (class S); its effect is how often Omni-Compass decides; its limits are the six
buttons on the page (the shipped controller itself takes any period from 5 to 120 s, `--interval`), and while the active profile
is held the buttons are disabled. A beat other than 60 s makes the active profile a custom profile, unless it is the candidate
(section 2.7).

### 2.6 Every beat, three model days each, and the candidate

Beside the heartbeat stands the sweep, the group the page labels **beat sweep · class S** (our own model). **Run every
beat (10 to 120 s), three days each** runs the live stress-test model for a whole model day at each of the seven beats on three
days, the page's own opening seed and the two after it, the same three at every sweep, with the same demand on both arms; when it
ends, the model starts the day in hand again from its seed. Nothing runs until the button is pressed: until then the note reads
"not run yet in this view".

Under the profile box a table gives each beat, Omni-Compass on native against native, the one pair: a light, the change in work
with its word and its sign, the muscle-decisions past the line, the failed work and the capacity held, each with its word. Each
day is paired with native's on the same seed and read by `three_run_reading` (section 36.4): the change is the mean of the three
days' changes; under 0.5% STEADY; from 0.5% up the word by the gauge's aim; days that moved 0.5% or more in opposite directions
disagree. Capacity held that rose is power given. The light is red where work, the muscle-decisions past the line or the failed
work reads LOSS, green where work reads GAIN, yellow otherwise. The best beat is the one with the most work for Omni-Compass on
native and no LOSS; it is outlined and marked "the best", and 60 s is marked "the factory's". Under the table, **Kubernetes Governor Model at Six Beats** reads the
Kubernetes governor's own model at the same beats (the page's section 3d, its ladder record, class S) and names, setting by
setting, every gauge that reads LOSS against native there; where a beat reads LOSS, the cause is the engine's, on the next
version's list, and the real runs at each beat decide (`docs/PACE_PREREGISTRATION.md`).

**Try the candidate** applies the sweep's best beat as a **candidate profile**, a proposed combination of settings under
evaluation: the factory's knobs with the heartbeat at that beat. The log says "a candidate is evaluated, never released". It
does nothing before a sweep has run ("no candidate yet: run every beat first") and nothing while the active profile is held. A
model's best beat is a candidate for the real runs, never a result; the factory's beat stays until the real runs read it.

### 2.7 The profile: factory, candidate, active and custom

The **profile** group holds three buttons, and the profile box (`#fuseProfile`) under it says which profile governs.

- **Restore factory profile** reapplies the released configuration: every knob of the mechanism and the heartbeat back to the
  factory's (60 s), the candidate cleared and any hold released. It leaves the master switch as it stands (its log line reads
  "Omni-Compass still on").
- **Hold the active profile** holds every knob as set: the mechanism's knobs, the heartbeat buttons, the sweep, the heartbeat
  sweep monitor's beat row and the variation switchboard's beat row are disabled, and the note reads "HELD at decision n: the heartbeat
  … s and every knob held as set; restore the factory profile to turn them again". Unheld, the note reads "every knob turns; the
  factory profile is the released one (omni-v22: the heartbeat 60 s, every muscle on its card); no other profile is released".
- **Return to native** hands governance back: the reset, the operator's control (`tools/omni_control.py`, `POST /v1/reset`).
  On the page every setting goes to native's own controller and every Omni-Compass side follows native, as with the kill switch,
  but the switch then reads "OFF by the reset · native alone · press to turn ON" and the event log names the reset. A second
  press of Return to native changes nothing (native already runs alone); the switch turns Omni-Compass on again. The kill switch
  (section 2.28) is separate: for security and instant. On a real machine, `docs/FACTORY_PROFILE.md` gives the reset's meaning: hand
  governance back and restore the recorded native settings, as the adapter supports.

The box's first line is the **active profile**: its kind, FACTORY, CANDIDATE or CUSTOM, the engine, the heartbeat and the
profile's fingerprint, "profile" and eight hexadecimal digits. The fingerprint (`profHash`) is the 32-bit FNV-1a hash of every
setting of the mechanism, the heartbeat and every muscle's body included: one identity for one set of settings, so two views
showing the same fingerprint run the same settings of the mechanism. The kind is FACTORY when no knob of the mechanism is turned
and the heartbeat is the factory's; CANDIDATE when no knob is turned and the heartbeat is the candidate's; CUSTOM otherwise. The
line is printed green for FACTORY, yellow for CANDIDATE and violet for CUSTOM, violet being the page's colour of a tune turned
from the factory, never a side. Its note says what that means: the factory profile is "the released configuration, every muscle on
the setting found for it; every published result is this profile's"; a candidate is "a proposed combination under evaluation … it
becomes a factory profile only after validation and a new release"; a custom profile is the count of knobs turned, "identified by
its fingerprint; its results are its own".

The second line names the **backend**: "this page's live stress-test model (class S, our own model): no meter, so no physical
energy reading; the sections marked replay play recorded runs from their own files", or, while the harness plays, the realms
harness, recorded and replayed from its record, with the reminder that the live model's knobs act on the live model.

### 2.8 Factory and active settings

The distinction between factory and active settings is the one `docs/FACTORY_PROFILE.md` writes. The **factory profile** is the
complete, versioned set of Omni-Compass default settings shipped together: the governing rules, gains, margins, decision interval
and every other default. Freezing it fixes the released rules and default tuning; the engine's internal state, its commands and
the resources it allocates go on responding to changing conditions, so one fixed factory profile governs a changing workload.
The **active profile** is the settings actually governing the current run, named on the profile box with its fingerprint. A
**candidate profile** is a proposed combination under evaluation; a **custom profile** is any identifiable configuration that
differs from the released factory profile. On the page, every benchmark result played back ran the factory profile of the engine
its table names; a candidate or custom profile on the bench is a variation of the mechanism (class S), never a benchmark result,
and its results are its own. The page opens on the factory profile and holds nothing: no profile is locked when the page opens.

Three buttons put things back, and they differ. *The mechanism back to the factory* (in the mechanism panel) puts back the
mechanism's knobs alone. *Restore factory profile* puts back the mechanism's knobs and the heartbeat, clears the candidate and
releases a hold. *Back to the factory tune* (in the control panel's first panel, on the console, in the dock and on every strip) puts back all of
that and the page's plant at rest as well (section 11.2).

### 2.9 Actuation and the contract, this decision

The box's third line reads Omni-Compass on native's actuation in the decision on screen: how many settings it **requested** (a
move of more than 2% of the setting), how many **landed as asked** (inside the muscle's floor and ceiling), how many were **held
at the muscle's limit** (clipped to that floor or ceiling), and how many muscles are **still moving toward their setting**
(capacity in service more than 2% from its setting, following its lever with the muscle's own response time τ). The line adds that
the model's plant refuses nothing, while a real adapter reads every write back and holds a refused one (omni-v12). The line
follows the distinction `docs/FACTORY_PROFILE.md` draws (section 3) between the requested, the commanded and the acknowledged
settings. While the harness plays, nothing is requested, commanded or read back in that view (the harness replays recorded
settings, and the page's section 3e traces one of its decisions), and the line carries a button, *Run the live model*, that moves
the page to the live model, where the counts are computed.

The fourth line, **contract, this decision**, writes the same decision in the symbols of `docs/FACTORY_PROFILE.md`, section 3,
for Omni-Compass on native:

  k = the decision on screen · t[k+1] = t[k] + Δ, Δ = the heartbeat set · θ = the active profile's fingerprint and its kind
  u[req](k): the settings changed · u[cmd](k) = Π[C](u[req](k)): how many were cut to the muscle's own limit
  u[ack](k) = R(u[cmd](k)): how many of the sixty settings stand at their command, and how many are still moving

Under it the whole contract is printed once, y(k) = h(x(t[k])) + ε(k); (u[req](k), z(k+1)) = G[θ](z(k), y(k), A(k));
u[cmd](k) = Π[C](u[req](k)); u[ack](k) = R(u[cmd](k)); x(t[k+1]) = Φ(x(t[k]), u[ack](k), w(k)); θ(k+1) = θ(k) once released, with
what each symbol is on this page: x the sixty muscles' settings and loads, y their readings with the sense delay and the noise σ
set on the panel, w the demand, C each muscle's own range, A Omni-Compass's hand (the max or the tune-down). On the harness the
line names k, Δ and θ and says the three settings are computed only on the live model; with Omni-Compass off it says nothing is
requested and every setting is native's own. The counts are the page's own model (class S): the model's plant refuses nothing, so
every cut is the muscle's own range, never a refused write.

### 2.10 The deployment route and its bill

Two buttons choose the deployment route, **On site: software on your own hardware** or **Through the cloud**, and a table gives
that route's bill as the sum of its costs. Each row is one cost component, with the native total, the Omni-Compass total and what
is measured:

| Route | Cost components |
|---|---|
| On site | energy: kWh × your price per kWh; machines: their cost over their life; operation: people, space and cooling |
| Through the cloud | compute: machines billed × the list price; energy at the back end (the cloud bills no energy to a tenant: inside its price); storage, network and the control plane |

Every native total and every Omni-Compass total reads **unresolved** where no price is recorded, and today none is resolved:
the only component metered in money is the cloud's compute, on Azure, at machine-hours times the list price, and the other
components carry no price in the repository. Beside a component the page prints its measured change from the whole organism's
composition with its word (energy and machines on site, the bill through the cloud), a supporting measurement, never the bill.
The formula under the table is the bill's:

C(r, a) = Σₖ c(r, a, k),  S(r, a) = (C(r, native) − C(r, a)) / C(r, native)

where r is the route, a the arm, and c(r, a, k) each cost component inside the declared boundary, counted once; the saving S is
defined for a positive native cost and the same workload in both arms. A component without a recorded price leaves its total
unresolved, and the saving with it. The whole-workload index on the scorecard is the composition's one number, not a price
(chapter 4). The measured changes follow the whole organism's reading and chip knobs (the page's section 5d).

### 2.11 Mechanism Knobs: where they are and what they turn

Inside the fuse box, under the profile box and on its own tab, stands a second set of knobs, **Mechanism Knobs** (`#mechPanel`,
folded or unfolded at its head, its groups under **Mechanism Knob Groups**). The plant's knobs change the plant's conditions (demand, noise, sense delay, faults, the load profile); these change the
engine's own equations while it runs. Each knob is a constant of the brain (`omnicompass/core.py`), the governor's law
(`omnicompass/adapter.py`, `omnicompass/nervous_system.py`), the compass law (`omnicompass/compass_law.py`), Omni-Compass's hand on
each muscle, the redline reflex (`omnicompass/immune.py`), the model's native controller, or one muscle's body. Turned, the next decision of the live stress-test model is
computed with it, on Omni-Compass's side; native's controller knobs move every native controller, the one under Omni-Compass on
native included. Only the live brain reads the panel; every other brain on the page reads the factory's numbers.

### 2.12 How to turn a knob, and how to read it

Each knob is a slider with its value, its equation and its factory value under it, and ↺ beside it puts that one knob back. A knob
turned from the factory turns violet, the page's colour of a changed tune, never a side; each group has a button that puts the
group back; **The mechanism back to the factory** puts every knob of the panel back, and *Restore factory profile* and *Back to
the factory tune* put back these and more (section 2.8). The count beside it reads either "every knob at the factory: the engine
as it ships" or how many knobs are turned, "a variation of the mechanism (class S); its readings are its own"; the active profile
then reads CUSTOM with a new fingerprint. Every turn is written to the control event log with its decision. Each group prints a
live reading of the quantities its knobs act on, every decision, and the line at the top of the panel prints the live model's
decision with the muscles past the line, the work served, the work failed and the work waiting this day, native beside
Omni-Compass on native. The harness replays recorded positions, so turning any knob moves the live benchmark engine to the stress-test model
(the log says so); the knobs act on that model only. While the active profile is held, the panel's knobs are disabled.

### 2.13 Where each group acts

The compass law, Omni-Compass's hand, the redline reflex, native's controller and every muscle's body move the muscles at once. The brain's four
pieces move the brain's own state (E, U, I[U], S, B on the brain's monitors) and its grants: at the max every organ may add
capacity unless a security hold stands, so the brain's calm acts through the give-backs; set the dial to the tune-down to watch
the four pieces move the muscles too.

### 2.14 Piece 1, State and Basin

Source: `omnicompass/core.py`, `cpp/src/core.cpp`. Live reading: E, U, I[U], the push,
and whether U is in its basin.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the pull toward the basin, K[P] | 0 to 30 | 12 | u = −U̇ + K[P]·(1 − U), bounded by U[auth]; push = u/U[auth]; a push above κ's knee holds every give-back |
| the command's authority, U[auth] | 5 to 50 | 25 | the largest command; the larger it is, the smaller the same command reads as push |
| assimilation, a | 0 to 1 | 0.339 | x ← (1 − a)·x + a·x[obs]: 0 hears nothing, 1 forgets everything |
| the double well's depth, μ | 0 to 8 | 3.782 | U̇ = μ·U·(1 − U²) − Ė/E[max] − λ[U]·U + u: two basins at U = ±1, a ridge at 0 |
| energy's relaxation, α[E] | 0.5 to 8 | 3.487 | Ė = −α[E]·E + β[int] + β[ext] + v |
| energy's scale, E[max] | 0.5 to 4 | 2.0 | unity loses Ė/E[max]: the smaller, the harder energy shakes it |
| energy's drag on the integral, σ₁ | 0 to 1.5 | 0.38 | İ[U] = (1 − U) − σ₁·E − δ·S − λ[I]·I[U] |
| the integral's leak, λ[I] | 0 to 2 | 0.719 | how fast the remembered shortfall fades |
| unity's own leak, λ[U] | 0 to 1 | 0 | a drag on U itself |

What an operator sees: a lower K[P] or a lower a leaves U slower to return to its basin after a surge, and the push on the brain's
monitors smaller; a shallower μ flattens the double well, so the ball on U's landscape wanders nearer the ridge; a smaller E[max]
lets the same stress tilt the well harder.

### 2.15 Piece 2, Basin Potential and Flow

Source: `omnicompass/core.py`. Live reading: S, S[eq] beside its factory value,
and σ = S/S[eq], with a note when σ passes 1.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the inflow, δ | 0.05 to 2 | 0.705 | Ṡ = δ − α[s]·S − ¾·β[s]·S², so Φ(S) = −δ·S + ½α[s]·S² + ¼β[s]·S³ and Ṡ = −Φ′(S) |
| the linear drain, α[s] | 0 to 0.6 | 0.12 | the flow rests at S[eq], the root of Ṡ = 0: S[eq] = (−α[s] + √(α[s]² + 3β[s]·δ))/(1.5·β[s]), about 2.37 at the factory |
| the quadratic drain, β[s] | 0.01 to 0.6 | 0.10 | σ = S/S[eq] above 1 holds every give-back |

What an operator sees: a larger δ or smaller drains raise S[eq] and the stance's resting place on its landscape; while σ stands
above 1 the panel says every give-back is held, and on the tune-down the give-backs stop.

### 2.16 Piece 3, Bath

Source: `omnicompass/core.py`. Live reading: B, Ḃ, the bath's natural period 2π/ω[B] (about 6.28 at the
factory) and its damping ω[B]/Q[B] (0.4 at the factory).

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the bath's frequency, ω[B] | 0.2 to 3 | 1.0 | B̈ = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B; the drive on energy beats at ½ω[B] |
| the bath's quality, Q[B] | 0.5 to 10 | 2.5 | the higher, the less the bath is damped and the longer it rings |
| the flow's coupling into the bath, γ[c] | 0 to 3 | 1.0 | how much of the flow S drives the bath |
| the bath's drive on energy, c | 0 to 3 | 1.0 | v = cos(½ω[B]·t)·c·tanh(z) enters Ė |
| the drive's offset, λ₀ | −2 to 2 | −0.40 | z = λ₀ + λ₁·(U − ½) + λ₂·S |
| unity's weight in the drive, λ₁ | 0 to 3 | 1.55 | as above |
| the flow's weight in the drive, λ₂ | 0 to 3 | 1.15 | as above |

What an operator sees: a higher Q[B] lets B ring longer after a disturbance on the bath's landscape; a larger c feeds that swing
back into E, so the stress on Piece 1's reading oscillates.

### 2.17 Piece 4, Governor Law

Source: `omnicompass/adapter.py`, `omnicompass/nervous_system.py`,
`cpp/src/governor.cpp`. Live reading: ρ*, κ, h, calm, and the organs that may give back now.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the utilisation target, ρ₀ | 0.5 to 1 | 0.914 | ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρ[min], ρ₀): how full a muscle may run after a give-back |
| the target's floor, ρ[min] | 0.3 to 0.95 | 0.627 | as above |
| the shortfall's pull on the target, k[I] | 0 to 1 | 0.252 | as above |
| energy's pull on the target, k[E] | 0 to 1 | 0.297 | as above |
| the push that still lets go, κ's knee | 0 to 0.05 | 0.005 | κ = 1 while push ≤ the knee, else knee/push |
| the unity gate, U[gate] | 0 to 0.95 | 0.481 | h = (U − U[gate])/(1 − U[gate]); calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)) |
| the grants θ[nodes], θ[pods], θ[cpufreq], θ[power], θ[routing], θ[gpu] | 0 to 1 each | 0.7, 0.5, 0.3, 0.3, 0.5, 0.3 | an organ may give back only while calm ≥ its θ, the line clean, the senses seeing |

What an operator sees: raising an organ's θ above the live calm removes that organ from the list that may give back now; on the
tune-down its muscles stop handing capacity back. At the max this piece acts only through the give-backs.

### 2.18 Compass Law

Source: `omnicompass/compass_law.py`, `cpp/src/compass_law.cpp`. Live
reading, for the muscle chosen in the last group: native's p, Omni-Compass's p, v and force F, k[d] for its τ, and the muscles
past the line now on each side.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the band's low edge (load ratio), lo | 0 to 0.6 | 0.2 | p = (r − lo)/(hi − lo): where each muscle stands in its band |
| the line (load ratio; 1 = full), hi | 0.6 to 1.5 | 1.0 | past it a muscle is over the line |
| the centre, where the two forces balance | 0.2 to 0.8 | 0.5 | below it the force pulls capacity back, above it pushes capacity in |
| the cushion before the line | 0 to 0.25 | 0.05 | from 1 − cushion the force is the whole authority A: a muscle is never let past the line |
| the spring, k[p] | 0.1 to 4 | 1 | F = A·tanh((k[p]·(p − centre) + k[d]·v)/A) |
| the authority, A | 0.1 to 2 | 1 | the force's ceiling: smooth (tanh), never hammering |
| the velocity's smoothing, s | 0 to 0.95 | 0.5 | v ← s·v + (1 − s)·Δp/dt |
| the damping, × each muscle's critical k[d] | 0 to 3 | ×1 | k[d] = max(0, 2√(k[p]·τ/dt) − 1)·dt for each muscle's own τ |

What an operator sees: the phase plane's shading (the force field) moves with the centre, the spring and the authority; a smaller
cushion lets the right-hand dots run closer to the right edge before the force fails up; less damping lets the Omni-Compass side
overshoot and the strip's muscles past the line rise.

### 2.19 Push, Lift-Off and Tune-Down

Source: the page's capacity law on `omnicompass/adapter.py`. Live
reading: the settings Omni-Compass wrote this decision, the muscles it holds away from native's setting, and the dial.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the push: capacity added per unit of force | 0 to 1 | 0.30 | the max: L ← L·(1 + gain·F) while F > 0 and the organ may expand; never below native |
| the lift-off's base | 0 to 1 | 0.15 | F < 0: L moves toward native's setting by min(1, base + slope·|F|) |
| the lift-off's slope | 0 to 2 | 0.5 | as above |
| the tune-down's floor, × native | 0.5 to 1 | 0.85 | the dial at the tune-down: never under this share of native's setting |
| the tune-down's step per unit of force | 0 to 0.5 | 0.10 | one step back: L = max(floor·L[nat], min(L, L[nat])·(1 + step·F)) |
| the dwell before a give-back, decisions | 0 to 10 | 3 | calm decisions in a row before one step back |
| the give-back's ceiling in the band | 0 to 1 | 0.40 | a step back only while p is under it |

What an operator sees: a larger push gain makes the Omni-Compass side add capacity faster under a surge (capacity held rises:
power given), a smaller lift-off holds it longer after the surge; the four tune-down knobs act only with the dial on the
tune-down.

### 2.20 Redline Reflex

Source: `omnicompass/immune.py`, its C++ twin `cpp/src/immune.cpp`, and the nervous system's `native_hold`
(`omnicompass/nervous_system.py`). Live reading: the reflex on or off, the muscles held native now, the hand-backs and the stays
this day, and the chosen muscle's own state (under its line, over it so many decisions in a row, or held native with so many
decisions of its hold left).

| Knob | Range | Factory | What it sets |
|---|---|---|---|
| the reflex on (1) or off (0) | 0 or 1 | 1 | off: no muscle is handed to native by the immune rule; the law's push at the wall still acts |
| the law's push at the band's wall | 0.80 to 1 | 0.95 | at or past this place in the band the law pushes at once, before the line |
| redlining: decisions over the line in a row | 1 to 12 | 3 | a muscle redlines when its reading stays over its own line this many decisions in a row |
| stuck: the relief it must show | 0 to 0.30 | 0.05 | stuck while the reading has not fallen by this share of where the redline began, or the knob is at its own limit |
| native stronger: by more than | 0 to 0.30 | 0.05 | native's twin reading lower by more than this share hands the muscle to native; the muscle comes back only when Omni-Compass's side reads lower than native's by the same share and is under its line |
| the hold after a hand-back, decisions | 1 to 60 | 10 | the first hold; it doubles for each hand-back in a row and halves after a quiet hold |
| the longest hold, decisions | 10 to 640 | 160 | the doubling stops here |

The factory numbers are the engine's own (the defaults of `Immune` in `omnicompass/immune.py`); none is written into the
rule: every one is a knob on this panel, and each light (GAINING, STEADY, REDLINING, OVER THE LINE) reads the live reading
against its own band whatever the knobs are set to. What an operator sees: a shorter streak or a smaller margin hands muscles to
native sooner and more often (more hand-backs in the live reading); a longer hold keeps them native longer after a surge. A
changed reflex is a variation of the mechanism (class S), its readings its own (section 2.23).

### 2.21 Native Controller

Source: the model's native rule, Kubernetes' published autoscaling rule, written by us.
Live reading: the settings native's controllers moved this decision, and the chosen muscle's setting and last wish.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| native's target load | 0.3 to 0.95 | 0.70 | desired = current·observed/target |
| native's tolerance | 0 to 0.5 | 0.10 | inside ±tolerance of the target native does nothing |
| native's largest step up, × current | 1 to 5 | ×2 | the most one step may add |
| native's stabilisation window, decisions | 1 to 20 | 5 | a step down only to the highest wish in the window |

What an operator sees: both sides change, because native's controller runs under Omni-Compass on native too. The phase plane marks
native's target on native's side while the stress-test model runs.

### 2.22 Muscle Scale, Response and Switch

The model's sixty muscles, twelve to a body part.
Pick the muscle, then the scope: **this muscle**, **its body part** or **every muscle**. Live reading: the muscle's units on
native and on the Omni-Compass side, its ceiling, floor, size, τ and sensing delay, and whether it is governed.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| scale out: the most units it may hold, × its factory ceiling | ×0.25 to ×4 | ×1 | the ceiling c[max]; Omni-Compass's max rides up to it, never past |
| scale in: the fewest units, × its factory floor | ×0.25 to ×4 | ×1 | the floor c[min]; no controller takes it below |
| scale up: each unit's size | ×0.25 to ×4 | ×1 | capacity in service = units × size, on every arm alike |
| its response time τ | ×0.25 to ×4 | ×1 | c ← c + (L − c)·(1 − e^(−1/τ)); the law's damping follows τ |
| its sensing delay | +0 to +6 decisions | +0 | decisions between what the muscle does and what its controllers read |

The group's switch reads **Omni-Compass governs it** and, pressed, hands the muscles in scope back to native's own controller
while every other muscle stays governed; pressed again, Omni-Compass governs them again. The kill switch hands every muscle back
at once.

### 2.23 A changed tune is not a result

Every knob of this panel shows a variation of the mechanism (class S, our own model). The benchmarks prove the factory profile
only; a custom profile is its tuner's, and so are its readings. This is the one place on the page where a person may turn the
engine away from its factory profile, change its mechanism of action by hand and watch every
monitor move with it; the factory buttons put it back.

### 2.24 Scenarios and Injection Grid, and the Monitor Breakers

On its **Scenarios and Injection Grid** tab the fuse box carries the twenty scenarios in a compact grid (ten organisms, each native alone and with
Omni-Compass on native, each cell one signal word and one number against native); a click on a cell prints its gauges and three
runs under the grid, and the full grid stands in the page's section 5c (chapter 27). Under it the injection grid stands compact:
the organism, the way, what it is read against, the runs, the organisms stacked and the gauge, the cell's readout and its matrix
(sections 27.4 to 27.8). A click on the live benchmark engine's own organism in
the Omni-Compass on native column also moves the live benchmark engine to the harness's one organism.

The **Monitor Breakers** tab holds one breaker for every monitor, grouped by section in the page's order, each section with its
own signal.
Each breaker carries its signal and its word, its number and name, its switch (**ON** draws it live; **REST** stops its drawing,
as the page's own governor rests a monitor off screen, and frees the frame for the rest), a way to it, and, on a monitor that
draws two sides, which side it shows now (native alone under the kill switch, Omni-Compass on native, or as recorded). *Every
breaker ON* and *rest every monitor off screen* act on all of them; the panel's own factory button also turns every breaker ON.

### 2.25 Your own system, Prometheus Metrics and Governor API Commands

The group **your own system** points the page at the operator's own Prometheus: an address, *Connect* and *Disconnect*. Once
connected, each monitor's own query (its feed in `docs/engine/monitors.json`, the series `tools/omni_exporter.py` and the
governor's `/metrics` expose) is asked every 15 s, and each breaker shows what that system answers. It is read only: nothing is
written to the operator's system from the page. The Prometheus must allow the page's address (its `--web.cors.origin` flag, or
the page served behind the same address); a page opened inside another site's sandbox may be refused by the browser, and says so.

**The wall beside Omni-Compass, in one command.** `deploy/wall` (its README) stands up Prometheus, Grafana with the Omni-Compass
wall loaded as its home dashboard (`deploy/grafana/omni-compass-wall.json`), Alertmanager with the governor's alert rules,
node_exporter and the governor's exporter: `cp .env.example .env`, set the Grafana password, `docker compose up -d`, then Grafana at
`http://127.0.0.1:3000` and Prometheus at `http://127.0.0.1:9090`, the address to type here. Every port is bound to the machine
itself, every image pinned; the stack reads and writes nothing. `--profile alloy` adds Grafana Alloy (`config.alloy`) in the
collector's place: it gathers the same targets and writes them into the same Prometheus. Alloy collects and forwards telemetry and
decides nothing; it sits beside Omni-Compass, one of the ways the governor's readings travel to the wall.

**The Prometheus Metrics tab** (its panel **Prometheus Metrics Endpoint**) prints the live model in Prometheus's text exposition format, as `GET /metrics` answers on a running system:
the decisions, the heartbeat, the master switch, the dial, the active profile (`omni_profile_info{kind, fingerprint, engine}`),
the plant's conditions, and for each of the two arms (`arm="native"`, `"on_native"`) the work served, failed and waited, the
muscle-decisions past their line, the writes, the cuts to a muscle's range, the setting moves and this decision's actuation
(`omni_actuation{arm, stage}`). Under it a table sets each beside the series a running system serves (the governor's exporter,
the service's own `http_requests_total` and `http_request_duration_seconds`, node_exporter's `node_cpu_seconds_total`, Kepler's
joules, OpenCost's hourly cost) and the PromQL the wall draws it with. Its names are the page's own model (class S); the output
passes `promtool check metrics`.

**The Commands tab** (its panel **Governor API Commands**) lists every control with the request a running system takes for it, its role and its note: the kill switch
and the arm, Return to native, the dial, the heartbeat, each muscle on or left native (`POST /v1/muscle`, the governor's muscles),
the mode (autopilot, watch, off), Restore factory profile, the reads (`GET /v1/status`, `/v1/presses`, `/metrics`); the
mechanism's knobs have none (an engine constant changed is another engine, never a press), nor have the plant's conditions and the
view.

### 2.26 Every control: its backend, its effects, its limits

| Control | Its backend | Its effects | Its limits |
|---|---|---|---|
| Kill switch | every governor on the page (the live model, the harness's replay, the live controller's replay, the page's render governor) | every setting handed to native's own controller at once; every Omni-Compass side follows native | security only, instant; a recorded result changes colour, never a value; a second press releases it |
| Return to native (the reset) | the same governors | the same hand-back; the switch reads "OFF by the reset" | the operator's control, not a security engagement; a second press changes nothing; the switch turns Omni-Compass on again |
| The dial | the live model | the max (every muscle to its own limit, never below native) or the tune-down (never more than native) | the records keep their own dial |
| The body | the live model or the harness record | which body the live monitors draw | the knobs act on the live model only |
| Time | the live model's clock | 1× to 60×, pause, one decision | none on the records |
| Demand, noise, sense delay, faults | the live model's plant | both sides alike, the same draw | demand ×0.25 to ×2; σ 0 to 0.6; +0 to +6 decisions; a fault lasts 40 decisions |
| Heartbeat | Omni-Compass on the live model | how often the full decision lands (section 2.5) | seven beats; disabled while held |
| Run every beat, Try the candidate | the live model, three model days a beat | the sweep's table, the best beat; a candidate profile | class S; a candidate is never released |
| Restore factory profile, Hold the active profile | the mechanism's knobs and the heartbeat | the released configuration back; every knob held | the plant's conditions are the factory tune's button |
| Deployment route | the whole organism's composition and the recorded prices | the route's bill as a sum of costs | a component with no price stays unresolved |
| Mechanism Knobs | the live model's equations (sections 2.11 to 2.23) | the next decision computed with the knob | the ranges of the panel; the live model only |
| The breakers | the page's drawing | a monitor drawn live or rested | nothing recorded changes |
| Your own system | the operator's Prometheus, read only | each breaker shows its series | the browser's cross-origin rules |
| Back to the factory tune | every knob of the page | the factory profile and the plant at rest | the kill switch released; native alone is the kill switch |

### 2.27 Operator Controls

The third panel of the control panel, **Operator Controls** (`#ctlPanel`), carries at its head the big kill switch ("Kill switch · Omni-Compass ON"). Under it stand the buttons that run the Python's runs in the
page (*Run the Python's 500 runs here*; *Run the Monte Carlo 500: the Python, the C++ and this page, linked*; *Run your own system
through it (here or on GitHub)*; *The proof monitor*), the **Jump Generator**, the **Variation Switchboard**, the four reports
(*Engineering Report*, *CTO Report*, *Board Report*, *CFO Report*), the three manuals and *The wall as a Grafana dashboard
(JSON)*. Its controls line says what acts: the kill switch acts at once on every governor of the page; the buttons run the
Python's runs here and fetch the three manuals. The panel closes with the kill switch's own note (section 2.28).

### 2.28 The kill switch and its three states

While Omni-Compass governs on top of native the switch reads ON in green. Pressed, it turns red: at the next decision every
governor puts every setting it wrote back, reads each one back and stops (`omnicompass/master.py`, `tools/omni_switch.py`); the
word OFF stands white, and every Omni-Compass side of every monitor follows native. Native's own controllers under every muscle
never stop and never see the switch. A recorded result never changes with it: its colour does, never a value, a word or a row.
The same switch stands at the head of every section, in every monitor's strip, in the fuse box's first row, on the console (*Turn Omni-Compass OFF*) and in the dock; one press anywhere is one press everywhere. It is
for security and is instant; the walk back after a crash is the lease, separate.

| State | Colour | What it means on the page | What it means on a real machine |
|---|---|---|---|
| ON | green | the brain's outputs reach every muscle; every monitor shows Omni-Compass acting on top of native | the governors run; every write read back; the lease renewed each beat |
| Kill switch engaged | red | every lever handed to native at once; the decisions shaded red on every time axis; the event log records the engagement and its clearing | `python3 tools/omni_switch.py off`: every governor hands back and exits, and none starts again until `on` |
| OFF | white | the brain keeps reading the native body in shadow, so its monitors keep moving, and nothing it computes leaves it; every Omni-Compass side follows native, drawn in a tint of native's colour, dashed | the governor in watch mode writes nothing (the Operator's Manual, level 1); off, it is not running |

No monitor is switched off by the switch. That is deliberate: the operator sees what the brain would do while it does nothing,
which is the watch level of every installation.

### 2.29 What a kill-switch window looks like

Press the kill switch on the console (chapter 11) and every time axis on the
page shades the window red from the press to its clearing. Inside it, Omni-Compass's lines fall onto native's; the governor's
ticker (the page's section 4a) is empty, for nothing decides on top of native; the phase plane's right-hand dots take the left-hand
positions. When the window clears, the lines part again where the governor's first decision lands.

### 2.30 The Python's runs at a button, and the Jump Generator

The first button runs the Python's own seeded runs in the page (they also run once on their own as the page opens), the second
runs the core's Monte Carlo through the Python, the C++ and the page, linked, and the third opens the panel that runs the
operator's own system through it; chapter 25 reads all three.

**Jump Generator.** In the control panel, under the buttons that run the Python's 500, a switch reads **Jump generator · OFF** until it is pressed. **ON**, the page draws set after set from the Python's jump generator
(500 runs a set unless 100 or 1,000 is chosen; run k of a set takes the seed base + k·0x9E3779B9 mod 2³², its stream mulberry32, the
same generator `tools/engine_runs.py` and `tools/core_runs.py` write bit for bit), one base after another from the first base shown,
which opens on the newest base the Python has run, so the first set reproduces the Python's own. Each set runs twice in the browser:
through the engine's runs (the proof monitor) and through the core's Monte Carlo (the Monte Carlo monitor), both in the page's
section 5a. Each set's output
is its runs, their counts and one SHA-256 digest; where the Python has run the same base its digest stands beside the page's, and
they must be equal. The line under the switch counts the sets drawn, the runs of the set in hand and the next base; the switch rests
while the page is hidden and runs until pressed again. **OFF** is the page's standing mode, the one it opens in: nothing new is
drawn from the generator; the Monte Carlo monitor plays the Python's own 500 (numpy's generator from seed 223387268), the proof
monitor recomputes once, as the page opens, the newest set GitHub ran in the Python and checks it digest for digest, then re-checks
it one run at a time; the 500 scenarios a seed replay from their record; GitHub's runs play back from their own raw files; and the
organism's model day runs on its own seeded stream, the same at every opening. Class S throughout: the engine's own mathematics on
draws, never a measurement.

### 2.31 Variation Switchboard

The **Variation Switchboard** is one group of knobs in the control panel that reaches every monitor carrying the variation it names, through that monitor's own setter; the line
under it names the monitors that moved, or says that no monitor carries the variation live.

- **Arm**, two buttons, one for each side: *native* is Return to native, the reset (not the kill switch), so every Omni-Compass
  side follows native; *Omni-Compass and native* releases it, and every monitor shows Omni-Compass on top of native again.
- **Organism**: the spine, the four realms, the four stacked or the tower: the grid's row is marked, and for the spine and the
  realms the console's fault body part follows.
- **Organisms** and **runs** (1, 10, 100, 500, in line with the Python's batch of 500): the injection grid of the page's section 5c moves
  to that many runs × organisms stacked (chapter 27), and the scale grid's square is marked where GitHub's grid carries that
  tier (it runs 1, 10, 100 and 1,000). The organism row sets the injection grid's organism too.
- **Run**: A, B or C on every replay that holds three runs and on the live organism's record.
- **Beat**: 10, 15, 20, 30, 60, 90 or 120 s: the heartbeat sweep monitor moves to that beat, or to the
  sweep record's nearest one and says which, and, unless the active profile is held, the live model's heartbeat is set to it.

A monitor that does not carry a variation is left as it is.

### 2.32 Reports, manuals and the wall as a Grafana dashboard

**The reports.** Four buttons in the control panel, *Engineering Report*, *CTO Report*, *Board Report* and *CFO Report*,
write a report from the page's own records at the moment they are pressed: the
engineer's (every benchmark on the board with its reading, size, rows and record, the Python's runs and their digests, the clouds'
finished sets, the lights at that moment), the CTO's (the summary; what stands and what runs, which says that two sides are shown,
native and Omni-Compass on top of native, and never Omni-Compass by itself; the board), the board's (the summary, what is proven
and what is modelled, the clouds) and the CFO's (the summary, every cloud set's machine-hours and bill at list price by the one
key, the rows of power given and the cuts). Each opens the browser's print, to print or save as a PDF, and downloads the same
report as a page; the notice stands first and last, every reading is the key's word with the word's sign, and every number names
its engine and its run.

Beside them stand the three manuals, each a PDF to download (this one, the Operator's and the Owner's), and *The wall as a
Grafana dashboard (JSON)*, which saves the wall as `omni-compass-wall.json` (the repository's `deploy/grafana/omni-compass-wall.json`), its panels on the open-source exporters'
series (chapter 39).

### 2.33 The page runs itself

The engine runs itself: its own mathematics decides every beat, and the knobs show the mechanism; they never have to drive it
(the page's own words in its reading guide, appendix B). The page opens on the factory profile, with Omni-Compass on, the heartbeat at 60 s, every
muscle driven and nothing held, and the live benchmark engine governs from the first decision. Every knob turned is a variation of the
mechanism on the live tuning bench (class S); the benchmarks prove the factory profile only, and a changed profile's results are
its own.

## 3. Contents: the Page's Order and Its Numbering

This chapter reads the page's **Contents** (`#contents`), directly under the control panel.

### 3.1 The page's own contents

The page opens on the monitors. Under the banner (the logo, the name, the engine chip and the legal notice) stand the
monitor wall (the page's section 0, `#s-wall`) and, directly under it, the control panel (the page's section 1, `#s-health`).
Only then come the page's contents (`#contents`), in three groups: **Wall and Controls** (0 Monitor Wall, 1 Control Panel),
**Main Matter** (Parts 2 to 5, each with its lettered sections) and **Appendixes** (A to G). Each row carries its number and its
title and links to its anchor. A lettered section (2a, 4d) is a section inside the numbered part that holds it; an appendix
carries a capital letter. The page keeps its explanations in appendix B, the reading guide (`#s-guide`): each section's
introduction stands there under the section's number and title, so the sections themselves open on their monitors and controls.
Native is orange everywhere and Omni-Compass blue, and every monitor, section and part carries its signal and its word: red
REDLINING, yellow STEADY, green GAINING.

### 3.2 The sections, as built on omni-v22

Appendix A lists every section with its anchor and the chapter of this book that reads it. In the page's order:

- **Banner** (`#topBanner`): the logo, the name, the engine chip and the legal notice (`#notice`).
- **Wall and Controls:** 0 Monitor Wall (`#s-wall`), every monitor in five blocks: Benefit and Organism; Real Runs on GitHub;
  Brain and Mechanism; Clouds, Chips, Orchestrators and Scale; Proof and Telemetry; the first four monitors the recap (the benefit
  board, the whole organism, the market map of every three-run table, the benefit gauge by gauge). 1 Control Panel
  (`#s-health`), directly under the wall: wall status and factory tune, the fuse box with its tabs and the mechanism's knobs, the
  kill switch, the runs, the variation switchboard, the reports and the manuals.
- **Contents** (`#contents`).
- **Part 2, Results** (`#p-results`): 2a Scorecard; 2b Benefit Against Native; 2c Benefit Board; 2d LOSS Register; 2e Status
  Board.
- **Part 3, Live Operation** (`#p-live`): 3a Live Organism; 3b Golden Signals and Event Log; 3c Control Console; 3d Heartbeat
  Dial; 3e Control Cycle; 3f Phase Plane and Scoreboard; 3g Brain State; 3h Verdict; 3i Dashboards.
- **Part 4, Real Runs and Platforms** (`#p-runs`): 4a Kubernetes Run Playback; 4b Repetition Telemetry; 4c Controller Decision
  Trace; 4d Cloud Providers; 4e Orchestrators and Governors; 4f GPU and CPU Hardware; 4g CI Pipeline.
- **Part 5, Proof and Models** (`#p-proof`): 5a Python Runs and Monte Carlo; 5b C++ Twin; 5c Scenarios and Injection Grid;
  5d Whole Organism; 5e Measured Effect; 5f Telemetry Analytics; 5g Master Switch Wiring; 5h Specification and Mathematics;
  5i Failure Modes and Controls; 5j Self-Governed Rendering.
- **Appendixes** (`#p-appendix`): A Title Page and Build; B Reading Guide; C Problem and Answer; D Executive Summary and Reading
  Key; E Monitor List; F Glossary and Index; G Disclosures, Law and Contact; then the closing legal notice (`#notice-end`).

### 3.3 Anchors

Every section has an anchor that does not move when the page is reordered: `#notice`, `#s-wall`, `#s-health` (with the
fuse box, `#fuseBox`), `#contents`, `#p-results`, `#s-bottom`, `#s-answer`, `#s-board`, `#s-loss`, `#s-status`, `#p-live`,
`#s-engines`, `#s-feed`, `#s-desk`, `#s-dial`, `#s-decision`, `#s-plane`, `#s-brain`, `#s-verdict`, `#s-dash`, `#p-runs`,
`#s-ops`, `#s-runs`, `#s-live`, `#s-cloud`, `#s-orch`, `#s-stacks`, `#s-github`, `#p-proof`, `#s-proof`, `#s-cpp`, `#s-scn`,
`#s-whole`, `#s-fleet`, `#s-lab`, `#s-master`, `#s-math`, `#s-fail`, `#s-self`, `#p-appendix`, `#title-page`, `#s-guide`,
`#s-problem`, `#s-read`, `#s-monlist`, `#s-glossary`, `#s-disclose`, `#notice-end`. A tile on the wall links to the anchor of
the monitor it copies; a row of the contents links the same way. When this book names a section it gives its number, its title
and its anchor, so the reader finds it on a page whose numbering has moved.

### 3.4 The order

The page is read top down in the order its watchers need it: the wall first, every monitor live, with the control panel
under it; then the results (the scorecard, the benefit against native, the benefit board, every LOSS row and the status board);
then the live operation of the engine; then the real runs and the platforms they ran on; then the proof and the models; and last
the appendixes, which carry the title page and build, the reading guide with every section's explanation, the problem and the
answer, the executive summary and the reading key, the monitor list, the glossary and index, and the disclosures. This book
follows the same order, chapter for chapter, and carries the problem and the answer and the reading key in its own front matter
as well. On a keyboard, `w` goes to the wall and the number keys 1 to 4 go to the four parts of the main matter, Parts 2 to 5.

---

# PART II. RESULTS

## 4. Scorecard

This chapter reads the page's section 2a, **Scorecard** (`#s-bottom`).

### 4.1 What it answers

The scorecard (`#s-bottom`), the first section of the page's Part 2, asks one question: is Omni-Compass a benefit? It answers
with one light and one number for each way to run a workload, against native alone on the same work, read from the
repository's own records. The line at its head (`#blHead`) puts the answer in one sentence: Omni-Compass on native, with its
signal word and its change in work against native in the real three-run test. The same number stands in the dock at the foot of
the screen ("vs native, more work (3 real runs): on native").

### 4.2 How to read it

Each row is one way to run a workload, against native alone on the same work. The light is the whole verdict: green GAINING,
Omni-Compass ahead of native; yellow STEADY, within 0.5% of native (STEADY by the key's floor); red REDLINING, behind native;
dark AWAITING, no test of that way in this build. The big number is how much, its size with no sign, the raw change
(Omni-Compass − native over native) standing apart with its true sign, labelled raw: on the first row more work done for the
same demand, on the bills and the index one number over their gauges, read by the key. A slower service, less work or a failed
request turns the light red whatever the number, on every row: on the bills and the index, any table under the row that reads
one of them LOSS, in either form, turns it red. Each row names what it stands on: its test, its engine and its evidence
class.

### 4.3 Whole-Loop Test by Arm

The first table (`#blArms`) reads a real test, three runs on GitHub's own machines (A, B and C from one commit), class L: the
full form, 18 steps of 25 s with the clients stepping 1 2 3 2 3 4 …, native against Omni-Compass on top of native. Its columns
are the way to run it, the light, the change against native and what else moved. It has two rows, one for each side.

- **Native Alone** is the yardstick: Kubernetes' published autoscaling rule as The Omni-Compass LLC wrote it, a description
  of the rule and not Kubernetes' code, on Omni-Compass's own orchestrator and test machines, with no Kubernetes. It is shown,
  not judged: every other row is read against it, and it carries no reading of its own.
- **Omni-Compass on Native**, Omni-Compass on top of that rule, carries as the big number the mean change in work done (requests
  answered) over runs A, B and C, each run's own change printed under it with the record's reading. Beside it stand the 95th
  percentile (how much faster or slower, with its reading), the machines (how many fewer or more), the serving units (how many
  more or fewer; a rise is power given, the capacity spent to buy the work, never a loss) and the failed or wrong answers over
  the runs, Omni-Compass against native.
- **The light** is red, REDLINING, when the work's reading or the 95th percentile's is LOSS or the runs disagree, or when
  Omni-Compass's arm gave more failed or wrong answers than native in any run; green, GAINING, when the work reads GAIN; yellow,
  STEADY, otherwise. A way with no three-run test in the build reads AWAITING, "not yet run".

The note under the table names the record (on this build `results/orchestrator/V21_THREE_ARMS_ABC.json`, of which the page
carries only the pair Omni-Compass on native against native, and only those two sides' totals), what it ran, the engine, the
commit, the three runs and the file, with the line "Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results."

### 4.4 Whole-Workload Index by Route

The second table (`#blBills`) reads the whole workload, bought two ways: **on site**, your software straight on your own
hardware (the software end × the bare metal; no cloud), and **through the cloud**, your software through the cloud onto its
hardware (the software end × the cloud's wire × the bare metal at the back end). The big number is the whole workload's index,
one number over its gauges, with its word; beside it every gauge with its word and its number. The light follows the index's
word, and is red where any table under the route reads a slower service or less work LOSS, in either form; a route with no
composition reads AWAITING, "not yet composed". The bills read the repository's own headline, by the index's rule, with the
other reading beside it.

The note under it names its source: `tools/whole_system.py` composes every measured layer's own three-run reading into the
whole workload (a model of measurements, class S of class L and P; chapter 28). It says what enters today: the bare metal enters
as no change, because the machine's own layer is not yet run and the card's one run, made on a controller since replaced,
stands outside the headline scope; so both bills are the software end's and, through the cloud, the wire's, and the cloud's own
bill is not counted (its tests are one run each, and by the index's rule a table of one run enters as exactly 1), as the
cloud-is-a-wire box explains (the page's section 4d, chapter 21). The two bills follow the whole
organism's two knobs in the page's section 5d, the reading and the chip's one run in or out. The index here is a composition's
one number, not a price; each route's bill as a sum of costs is the control panel's (section 2.10).

### 4.5 All Real Tests Combined

The third table (`#blAll`) gives Omni-Compass on native over every real test together: the Omni index (chapter 6), its light,
its number with its word, and its count of GAIN, LOSS and power given rows. The note points to every row of the benefit board
(the page's section 2c) and every three-run table (the page's section 5e).

## 5. Benefit Against Native

This chapter reads the page's section 2b, **Benefit Against Native** (`#s-answer`).

### 5.1 What it holds

The section opens on the Omni index, every real test weighed together, read from its record as the page opens
(`results/OMNI_INDEX.md`). Where the engine that stands has not yet landed the tables the index is read from, its head says so
("Not Yet Read on omni-v22") and gives the figure of record on the engine its tables stand on, never read as a result of the
engine that stands, with the count of its GAIN, LOSS and power given rows and the benefit sheet's word for the same tables. The same line
names the LOSS ledger (`docs/LOSS_LEDGER.md`): every LOSS row of the newest tables, the rows Omni-Compass against its own native
counted apart, because do no harm is judged by them, each with its cause where one is written (chapter 7).

### 5.2 One real test of the whole loop

Under the index stands one real test of the whole loop, three runs on GitHub's own machines (A, B and C from one
commit), class L, on Omni-Compass's own orchestrator (`omni_orchestrator`), the organism run without Kubernetes: native is
Kubernetes' published autoscaling rule on the muscles, as written by The Omni-Compass LLC, and the other side is Omni-Compass on
top of the same rule. It is one test, not the figure of record. Its table gives each side's signal, then work, the 95th-percentile
response time, the machines and the units (the service's own copies), each with its reading, its size with no sign, the raw change
apart with its true sign, and every run's own change. Native's row is the baseline in every column. Units that rose are power
given: Omni-Compass adds them to buy the work and the speed. The note names the record (on this build
`results/orchestrator/V21_THREE_ARMS_ABC.json`), its runs and its commit; the record's other arm, Omni-Compass alone on the
muscles, stays in the record and is not carried, because Omni-Compass is never by itself.

### 5.3 Bill by Route

**Bill by Route** reads each route's bill as its native total, then Omni-Compass's, then the saving, 1 − (the
Omni-Compass total ÷ the native total), each total the sum of its non-overlapping cost components inside the declared boundary,
on a matched workload (`docs/THE_TUNE.md`, section 8). A component's own percent is a supporting measurement, never the bill;
where a price or a component is missing the bill reads unresolved, and no price is assumed. Its rows are *On-site: the software
on your own bare metal* and *Through the cloud: the cloud's build, its bare metal at the back end, the software*. Beside it stand
the totals composed from the tables that stand (`results/WHOLE_SYSTEM.md`, `tools/whole_system.py`), each on its own engine, by
the rule that counts only what held in all three runs: a composition across engines (class S over class L tables), never read as
one engine's result (chapter 28). The same route's bill as a sum of costs is the fuse box's profile box (section 2.10).

## 6. Benefit Board

This chapter reads the page's section 2c, **Benefit Board** (`#s-board`).

### 6.1 Benefit by Domain

**Benefit by Domain**: every domain, native against Omni-Compass, as the repository's benefit sheet
holds it (`results/BENEFIT_SHEET.json`, `docs/BENEFIT_SHEET.md`): the domain, the benchmark, its evidence class, its engine,
its benefit (one number and one word), its GAIN rows, power given, STEADY and LOSS counts, and where it stands (landed, running,
queued, not yet run). Its bar chart is monitor 1 on the wall: every benchmark's measured effect in one board, by domain and by
gauge family, with the Omni index that weighs them together at its head. Each bar carries its table's own word (GAIN green, STEADY
yellow, LOSS red, power given blue), and the size beside the word carries the word's sign (GAIN +, LOSS −, STEADY =, power given +).
The axis reads 10, 25, 50 and 100% each way on a square-root scale, so a small bar is seen; a bar past 100% runs to the edge and is
marked. Every LOSS row stands on the board, is raised on the status board and is listed, with its cause where the LOSS ledger records one, in
the page's section 2d.

### 6.2 Benefit by Gauge Family

Every judged row of every newest three-run table (the page's section 5e), sorted into the family
of gauge it measures. A CTO reads speed, the service level, failures and work. A CFO reads machines, energy and the bill. A plant
engineer reads peaks and swings, wear and accuracy, and misses. Each bar counts the rows that read GAIN, in all three runs or by the mean of the three; the
size beside it is the median of those rows' own sizes, each row's size the mean of its runs' raw changes in percent of native (a
row whose native stood at zero is counted and not sized); the largest is printed beside the median; power given and LOSS rows are
counted beside them, and the runs that disagree or differ are listed, not counted.

### 6.3 Trading Floor

Every three-run table of the page's section 5e, read the way a trading floor reads its market. The
market map is a squarified treemap: one tile a table, grouped by stack, its area the number of gauges the table judged and its
colour its reading: green GAIN, deeper the larger the share of its rows that read GAIN; red wherever any row reads LOSS; yellow
STEADY; blue where it gave power; grey with a dashed edge a four-ways comparison that is not Omni-Compass against its
native (the orchestrator's own, with no Omni-Compass in either arm; Omni-Compass in place of a controller; two changes at
once). A reading cursor walks the map one table every one and a half seconds and names it under the map. The quote board
gives every table a quote: its ticker (the table's file) and engine, the gauge that moved most with its mean change across
the three runs, and that gauge in runs A, B and C as a candle: the vertical bar is the run's 95% interval, the tick its value,
the line the zero of no change. The strip under each quote counts the table's rows by word, and a tape runs every headline
across the top. Pointing at a tile or a quote shows its record: the table's title, engine, counts, the headline gauge in each
run and the file. Every figure is the table's own; nothing is typed in.

### 6.4 Whole-Board Aggregate

The Omni index (`results/OMNI_INDEX.md`): the geometric mean of the
ratios of every measure that enters, where a measure enters only as its three-run reading allows (GAIN, LOSS or power given
in all three runs counts; STEADY counts as exactly 1, so nothing inside the noise is claimed either way). Each test is read
from its own newest three-run table, no table is pooled across engines, and every row names its table. The index is one
number for the board; its row of factors under it is the board's own audit.

## 7. LOSS Register

This chapter reads the page's section 2d, **LOSS Register** (`#s-loss`).

### 7.1 What it lists

The LOSS register lists every LOSS row of every standing three-run table, read from the verdict audit's record
(`tools/verdict_audit.py`), the one selection the LOSS ledger (`docs/LOSS_LEDGER.md`) is written from: Omni-Compass against its
native first, then the GPU card's own meter (outside the audit's selection), then the orchestrators' four-ways comparisons by
what their two arms are. It is recorded data: every row is read from the verdict audit's record of the three-run tables and the
GPU card's own record. No row is cut and no number is tuned. Its panels, in order: **Verdict Audit** (every row recomputed from
its stored values, one count, by view: the tables, GAIN, power given, STEADY, LOSS, the runs disagree, the runs differ); **LOSS
Rows Against Native** (each table with its engine and class, the gauge, every run's native and Omni-Compass values with the raw
change, and the evidence); **Armada Two-Cluster BARE Table by Run**; the **Discrepancy Report** (what changed against the tables
as they were); and the **LOSS Ledger**.

### 7.2 How to read a row of the LOSS Ledger

The LOSS Ledger's columns are the comparison (a red LOSS for Omni-Compass against its own native; an orchestrator's own
comparison named by what its two arms are), the table, the gauge with its runs A, B and C and its reading, the cause as the LOSS
ledger records it, and where it was fixed and what decides it, exactly as the ledger records them (`tools/loss_ledger.py`).
Where the ledger records no cause, the row says so and asserts no knob. The rule on every row: find where the mechanism
or its wiring is wrong and correct that in the model gate; a knob with no setting that brings the row STEADY stays native on that
stack, so Omni-Compass hurts nothing (do no harm, `DISCLOSURES.md`, section 3); no number is tuned to make a row read well.
Chapter 44 is the procedure.

## 8. Status Board

This chapter reads the page's section 2e, **Status Board** (`#s-status`).

### 8.1 The order of the board

The status board (the page's section 2e, `#s-status`) says whether Omni-Compass is engaged, which signals are out of tolerance
and where, and raises every LOSS row as an alarm with its source record; each tile and each alarm is computed at runtime from the
live benchmark engine or from the repository's records. The board is laid out the way an operations monitor is. The switch and the engine
come first. Next come the live organism's signals, native beside Omni-Compass, in the terms of site-reliability practice
(latency, traffic, errors and saturation). Then every reading of the real and modelled runs that went against native, worst
first. Last come GitHub and the age of the page. A tile's word is its reading against native by the key; a tile with no reading
says what it shows.

### 8.2 The tiles

Each tile carries its title, its state, a line of detail and its buttons; every tile is read again four times a second.

| Tile | What it shows | Its buttons |
|---|---|---|
| Omni-Compass Engagement | ON on top of native, or OFF, native alone; the dial | the kill switch; the max or the tune-down |
| Engine That Stands | the engine and its digest; its brain, compass law and verdict run in the page, checked against the Python and the C++ before the page is committed | the mathematics |
| Errors, Muscle-Decisions Past the Line · Class S | the muscle-decisions over their line this day, Omni-Compass against native, read beyond the counts' noise (two standard deviations of their difference): GAIN, STEADY or LOSS; "too early to read" in the day's first 20 decisions | Surge ×2; Lose machines |
| Throughput, Requests Served · Class S (on the harness, Throughput, Work Done · Class S) | the work done (on the live model, the requests served), the same demand on both sides, with the paired reading over the day's decisions | Demand ×1.6; Every knob to its start |
| Latency Stand-In, Queue Depth · Class S (on the harness, Power Drawn (kW), Harness · Class S) | on the live model the queue depth now, on the harness the organism's electrical power now (a rise to do more is power given) | Pause |
| Injected Faults | the faults active and the decisions each has left | Blind a sense; Security hold |
| Three-Run Tables | their LOSS rows (and how many were answered: the rig corrected, run again STEADY) and the rows where the runs disagree | Show the LOSS rows; Show where they disagree |
| Verdict Guard · Class S | how often the engine that stands keeps a step that truly costs 3% more, at the noise the real runs measured (class S): open, the next engine version's work | the verdict; where it can fail |
| CI Pipeline | the runs running and queued when the page was built | every run |
| Cloud Runs | the Azure sets running and their repetitions | the clouds |
| Build Freshness | how long ago the page was built, and from which commit | — |

### 8.3 Alarms and Watch Items by Severity

The table under the tiles, **Alarms and Watch Items by Severity**, lists every alarm and watch item, worst first by kind, each with its item, its reading, its source,
the repository's record and a way to it:

1. the live organism, when it has more muscle-decisions past their line than native this day, beyond the noise of the counts
   (LOSS);
2. every LOSS row of Omni-Compass's own three-run tables, with the root-cause document where the repository has one, and "run
   again: STEADY" where the row was answered by its own rerun on the corrected rig;
3. every square of the scale-out grid that reads LOSS with the real cluster inside;
4. every LOSS row of an orchestrator's own cost, where Omni-Compass is in neither arm: not a reading of Omni-Compass, standing as
   its table writes it;
5. every row where the runs disagree or differ;
6. the guards and open items: the verdict can keep a step that costs a little more; two levers act with no trial (a pod's
   processor limit conveyed from its machine, and a machine added), bounded by rules instead; the resources the tables show and
   do not judge that rose in all three runs;
7. GitHub: runs on the engine that stands that ended without a result, clouds whose $0 check has not passed, and the benchmarks
   still awaiting their three-run table on the engine that stands.

The buttons at its head filter it: *All*, *LOSS*, *The runs disagree*, *Live Now*, *Guards and Open Items*, *GitHub*. The line
above it counts the LOSS rows, the rows where the runs disagree, the guards and open items, and the items from GitHub.

### 8.4 Reading an alarm row

An alarm row names its gauge and its table, its size with the word's sign over runs A, B and C, the table's file, engine and
evidence class, and the repository's root-cause document where one exists (`docs/POD_START_WAIT.md`, `docs/TAIL_LATENCY.md`, and
the others). Chapter 44 is what to do with one.

### 8.5 The age of the page

The last tile, Build Freshness, counts from the build's time to now on the viewer's clock and names the commit. A page older than
three hours and a few minutes means the rebuild did not run or did not land (chapter 24); the records on it are still true for
the build they name.

---

# PART III. LIVE OPERATION

## 9. Live Organism

This chapter reads the page's section 3a, **Live Organism** (`#s-engines`).

### 9.1 The two organism rings

The system rendered as an organism: each node is a muscle (one
controlled actuator) and each ring its operating range. The left instance runs under its native controllers alone; the right
runs the same controllers with Omni-Compass's brain, nerves, heart and immune system supervising them. The body is chosen in
the page's section 3e or in the fuse box's first row: *Each Muscle Alone* (native, then on top, one at a time), *One Organism*
(the sixty muscles in one body) or the *Stress-Test Model* (the console's sixty muscles). The two monitors are *Native Organism
Ring · Class S* and *Omni-Compass Organism Ring · Class S*. Evidence class S: our own models, shown beside the real runs and never
presented as proof.

### 9.2 Reading a ring

A ring is a muscle's band drawn as a circle: calm at the inner edge, the line at the outer. The
muscle's live value is the ball on the ring; the reference, the knob at native, is marked. Under the max a muscle is moved only
where it has room above native; a muscle already at its limit on native is left native by design and its ball sits where
native's does. A dashed white ring marks every muscle that differs between the two sides at that moment, a red tail shows where
a muscle went in its last 12 decisions, and a click on a muscle follows it. The counters under each ring (past the line now,
misses so far, settings off native, the two sides differing now) and the scoreboard (chapter 14) give both sides and the
difference. Where the two sides look the same, they are the same.

![The seven organisms. The spine (267 muscles, every muscle that sits in all four realms), the four realms (Compute/AI/Cloud, Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized), the four stacked, and the whole tower of 1,107 muscles in 70 families. The organism monitor plays one organism of sixty muscles and each muscle alone; the measured effect in full (chapter 29) carries all seven.](book/figures/organisms.svg)

### 9.3 Body Scan by Organ

As a scan reads a living body organ by organ, this reads the system playing in the page's section 4a (the
benchmark, run and repetition chosen there), organ by organ, half minute by half minute, from its own SHA-256-checked files:
native beside Omni-Compass. Each organ names what it reads; where native has no such organ (the governor's heart, the nerves)
the cell says so.

### 9.4 Immune System

The immune system is Omni-Compass's; native runs on its own controllers. Every room and
every machine pool has a native twin: the same muscle under its own controller, on native's heat and load, the body's memory
of healthy. A room that stands warmer than its twin is inflamed. Where its own knob can cool it, it is cured on the spot.
Where it cannot, it sends the whole body a signal, its heat debt, like a cytokine calling for help, and the other muscles
answer: the machine pools give back what Omni-Compass added until the room stands no warmer than native's. The skeleton (the
bone: the power and cooling lines the whole body shares) grants nothing it cannot carry. A cooling setting is walked back,
never snapped. On the monitor an inflamed room is marked, its heat debt is a bar, and the pools' give-back is seen on their
rings. In the words of `docs/FACTORY_PROFILE.md` this belongs to the defensive system: constraint enforcement, fault detection,
containment, recovery and restoration (the bone and the twins, the lease's walk back, the kill switch).

### 9.5 Anatomy by Part

Part by part, in the order of control, the brain first and the whole organism last: the brain, the nervous system, the heart,
the spine, the immune system, the muscles, the blood, the power (the nutrients), the intake, the digestion, the exhaust and the
organism, each with what native has, what Omni-Compass and native has, and where it lives in the code.

## 10. Golden Signals and Event Log

This chapter reads the page's section 3b, **Golden Signals and Event Log** (`#s-feed`).

### 10.1 Golden-Signal Feed, Last 240 Decisions · Class S

The golden-signal feed of the page's section 3b, `#s-feed`, streams the live organism's four golden signals, native beside Omni-Compass: errors (muscles
over the line), throughput (work done) and, because neither body has a response time or a machine's busy share, latency's and
saturation's stand-ins: on the live model the work waiting in line and the capacity in service, on the realms harness the spread
of p across the muscles and the electrical power drawn (kW). One point per decision streamed from the live benchmark engine, gapless,
the last 240 decisions, each signal on its own axis, with each side's last, mean and maximum as a time-series dashboard reports
them; a kill-switch window shaded red; native in orange, Omni-Compass in blue, the same demand on both. The feed is the status
board's signals at full size and full history.

### 10.2 Engine Event Log

The live benchmark engine's own events as it emits them, newest first, with the wall-clock time and the
decision: a threshold breach and its clearing on either side, every injected fault and its end, the kill switch, the dial, a
new day, and each organ's hand-back grant withheld or opened again, at that organ's own threshold θ (pods 0.5, nodes 0.7, the
clock, the card and power 0.3, routing 0.5 at the factory: `omnicompass/nervous_system.py`). The log is what an operator reads to answer "what happened at
02:14": the decision number ties it to every other monitor.

Its buttons filter it by grade: *All*, *ALERT*, *WARN*, *INFO*, as an operations log grades its events.

### 10.3 OpenMetrics Exposition

The live benchmark engine's metrics in the OpenMetrics text format, the exposition format
Prometheus scrapes and Grafana charts, refreshed every two seconds. They are the same families, under the same names, as the fuse box's Prometheus Metrics tab prints (section 2.25): the master
switch, the decisions, the plant's knobs, work served, failed and waiting, the muscle-decisions past their line, writes,
capacity, actuation, band time, actuator moves and reversals per side, and frame time; then the verdict's keep ratio at each
true cost (chapter 16), the three-run tables' rows by class, by the engine each table ran on, by the way it compares and by
reading, and the build's engine, digest and commit. *Copy the
exposition* puts the text on the clipboard, so the page's own metrics can be pasted into a scrape target and charted beside
the stack's.

## 11. Control Console

This chapter reads the page's section 3c, **Control Console** (`#s-desk`).

### 11.1 What the console is

Runtime parameter control and fault injection on the live benchmark engine: load
scaling, noise injection, sensor latency, capacity loss, a demand surge, a sensor blackout, a security hold, the dial, and
the kill switch. Every control is applied to both sides identically; the response is plotted per decision, native beside
Omni-Compass. The engine these knobs turn is the engine's own mathematics running in the page: the brain, the compass law and
the verdict, proven equal to the Python and the C++ on every build. It governs the stress-test model's sixty muscles, each on
top of its own native controller. The knobs move the live benchmark engine in the page's sections 3a, 3b, 3e to 3g, 3i and 5h, and the kill switch and the
frame load also move the page's own render governor (the page's section 5j).

### 11.2 Factory Tune

One button, on the console under the kill switch (its knob title **Factory Tune**), on the dock, in the control panel's
first panel and in its fuse box, and in every monitor's own knobs, puts back two things at once: the engine's tune as it ships (`DISCLOSURES.md`, section 3: the dial at the max, every
muscle driven, Omni-Compass ON, the 60 s beat, the factory profile restored and any hold released, the mechanism's knobs at the
factory) and the page's plant at rest (the day as written, demand ×1, noise σ 0, sense delay
+0, no fault held, the load profile as written, speed 1×, running, no frame load, and the heartbeat sweep monitor on 60 s,
on-site, pods waiting, against native). It says what it put back. Turn anything and watch the mechanism change, never break; this button brings
all of it back. Native alone is not a tune: it is the kill switch. The control panel's
own factory button also turns every breaker ON.

### 11.3 Do no harm, at the console

Every control acts on both sides alike; what Omni-Compass does with them is held by its
guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another on the engine
that stands, a give-back tried against native first and refused on a LOSS. Its one meaning is written once, in
`DISCLOSURES.md`, section 3, and the page's appendix G carries it.

### 11.4 Every control

Appendix B lists each control in a table. In reading order:

| Control | Marked | What it does, on both sides |
|---|---|---|
| Kill switch (*Turn Omni-Compass OFF* / *ON*) | LIVE | every lever to native at once; the window shaded red; every Omni-Compass side follows native |
| Factory Tune: every knob back to the factory tune | LIVE | section 11.2 |
| Tune Dial: the max / tune-down | LIVE | the max: every muscle to its own limit, never below native; tune-down: never more than native, capacity handed back only with the organ's grant and the release gate |
| Demand (×0.25 to ×2) | LIVE | scales every muscle's demand from this decision on; ×1 is the day as written |
| Noise Injection (σ 0 to 0.6) | LIVE | multiplies each muscle's demand every decision by 1 + σ·z, z a fresh normal draw, one draw per muscle shared by both sides |
| Sense Delay (+0 to +6 decisions) | LIVE | adds decisions between what a muscle does and what its controller reads, on both sides: native's controllers and Omni-Compass's law read the same late number |
| Faults: the body part; Surge ×2 | LIVE, 40 decisions | doubles that body part's demand |
| Lose half its machines | LIVE, 40 decisions | halves a pool's capacity in service |
| A sense goes blind | LIVE, 40 decisions | forbids any hand-back (blind means hold) |
| Security hold | LIVE, 40 decisions | forbids any addition |
| Pause, One decision, 1×, 4×, 16×, 60× | LIVE | the console's clock: a decision every 0.9 s at 1×; one decision steps once |
| The same day again, A new day | LIVE | replays the seed with the knobs as set; a new day draws a new seed |
| Every knob to its start | LIVE | returns demand, noise and delay to the day as written |
| Frame Load (as it is, +8 ms, +16 ms) | LIVE | burns the stated time inside every frame of the page, both sides alike, for the page's own render governor to hold (chapter 34) |
| Load Profile (the day as written; a step ×1.6; a ramp ×1 to ×2 over 120 decisions; a sine ±40%, period 60 decisions; the Azure bursts `1 4 1 6 1 9`; the real day on 1 to 9; a sequence of the operator's own), *Inject* | LIVE | the same multiplier on every muscle and both sides; a sequence holds each value for 20 decisions and is scaled to its own mean, so the day's mean load is kept |

### 11.5 What a fault shows

Press *Surge ×2* and watch the page's section 3f: both sides' dots for that body part move up and right;
native's controllers each see their own reading one to three decisions late and add in the middle of their range; the
compass law pushes at the first decision the position leaves the center, so the blue dots turn back before the right edge
while orange ones cross it. Press *A sense goes blind* and the governor's hand-backs stop while its additions go on (blind means
hold, never a guess). Press *Security hold* and every addition stops while hand-backs go on. In every case the native side is
put through the same fault, so the difference is Omni-Compass alone.

### 11.6 The console's own monitors and the dock

Under the knobs the console draws **System Response per Decision · Class S** (native in the left lane, Omni-Compass in the right
on the same scale, every knob turned marked at its decision and a kill-switch window shaded), the **Inter-Frame Interval** of the
page against the 60 Hz budget, the **Control Event Log** (newest first: every knob, switch and button pressed, with its
decision), and the **Control-Loop Performance Assessment** of the day, native beside Omni-Compass: the threshold breaches this day, the recovery time
after the last injected fault, the throughput, the time inside the operating band, the mean absolute deviation from the band's
centre, the peak band position, the actuator moves and the direction reversals of p. Each judged row reads by the key's floor
(section 36.4); the band statistics are shown, not judged; the moves and reversals are resources, power given where they rose.

The dock at the foot of the screen keeps the console in reach from anywhere on the page: the kill switch, the factory tune, the
state of the switch, the scorecard's number against native (Omni-Compass on native's change in work in the real three-run
test), the wall's worst signal with its counts, the decision, the
muscles past the line on each side, the frame time, demand and noise, a surge, a lost pool, pause, a way to the control panel
(`#s-health`) and the console, and a button that folds it.

## 12. Heartbeat Dial

This chapter reads the page's section 3d, **Heartbeat Dial** (`#s-dial`).

### 12.1 The dial

The governor's heartbeat, its full decision, is a dial from omni-v17 on (the page's section 3d, `#s-dial`): the main engine, the
factory profile, decides every 60 s, and on the page any of seven beats can be set, 10, 15, 20, 30, 60, 90 or 120 s, with the fast
checks (the scheduling floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat. Every clock of the governor
counts seconds (omni-v16), so turning the dial changes only how often it looks. Each beat stands beside native with what it buys
(the reads of the cluster a day) and what it costs (the governor's own processor, and every service row read against native and
against the main engine's 60 s), because an operator may want a fast beat for its reads and accept what it costs, or a slow one.
At each beat the other knobs may want their own combination; that tuning is the next study, in our own models first.

### 12.2 Beat Ladder: the two tables

Its panel, **Beat Ladder · Class S**, gives every beat in two tables for each setting the models read (**Cloud Setting at the
Tune-Down, Machines Alone**: the compass law at the tune-down, the machines alone; **kind Benchmark at the Max, Autoscalers
Sensed**: the compass law at the max, every autoscaler sensed). The first, **Against Native**, gives each beat's value and its
word against native: the reads of the cluster a day, the governor's own processor, the pods waiting for a place, the 95th
percentile, the minutes over the line, the autoscaler short of its target, the machine-hours and the energy per core-hour; native
has no governor, so its reads and processor are blank, and the main engine's row is set in bold. The second, **Against the Main Engine's 60 s**,
gives each other beat's change against it, with its word. The reads are what a beat spends to look more often, shown as the
key reads a resource spent: power given.

### 12.3 Reading a row

Read a row across: a beat whose service words read GAIN or STEADY against native and whose cost columns the operator accepts is a
beat that can be set. A word of LOSS against native is the engine's at that beat and is listed with every other LOSS row
(the page's section 2d, chapter 7). The values are our own models (class S, `results/model_gate/V17_LADDER.json`, `tools/beat_ladder.py`),
each beat's mean over seeded days on a plant that moves every 5 s, paired by seed; the real runs at every beat
(`docs/PACE_PREREGISTRATION.md`, amendment 3) take their place in the note above the tables when their three runs land. The dial
is the tuning bench's own example: the factory profile runs the main engine at 60 s; any other beat is the engine's range on the
page, never a benchmark result, until its own three runs land on that beat and are read as that beat's. A beat set on a live
system is the operator's own custom profile, and its results are its own.

### 12.4 Where the beat is set

The beat is set on the governor's command line (`--interval`) or with the control panel's heartbeat button (`POST /v1/beat`,
`tools/omni_control.py`: one button for each stop of the dial), which hands every setting back and starts the governor again at
the new beat. The governor's own screen in Grafana counts the time since its last decision in beats of the setting it runs at and
alerts after three (`omni_heartbeat_seconds`, `deploy/grafana/omni-compass.json`, `deploy/prometheus/omni-compass-rules.yaml`). On
the page the heartbeat buttons of the control panel set the live model's beat (section 2.5); the dial's tables are records
and do not move with them.

## 13. Control Cycle

This chapter reads the page's section 3e, **Control Cycle** (`#s-decision`).

### 13.1 Decision Sequence

**Decision Sequence**: one control cycle traced end to end at reduced speed: the sensed inputs,
the brain's decision, and the actuator (the muscle) it wrote. The max: every muscle to its own limit, never below native; the
capacity it holds is power given. The tune-down: never more than native, and a step back only with the organ's grant and the
release gate. In this model native already sits near its band, so the tune-down finds little to hand back; the scoreboard
(chapter 14) reads its runs A, B and C live when the dial is on the tune-down. Class S.

### 13.2 How to read it

Follow the particles: in along the wires from the muscles' meters to the inner arc of nine senses;
through the brain's six spokes; out through the nerves (the grant), the compass (the force) and the plug (the write). Each
stress on the console lasts 40 decisions from the moment it is pressed, and both sides meet the same demand, so a cycle
watched during a surge shows the push on the blue side and the native controllers' late, middle-of-the-range moves on the
orange one.

### 13.3 Cycle Controls and the muscle's card

The section's panel **Cycle Controls** shares the console's state: **Body**, *Each Muscle Alone*, *One Organism* or
*Stress-Test Model*, each native, then on top; **Run**, A · 3000, B · 3001 or C · 3002 (the harness record's seeds); **Play**, pause, 1× to 60×, a new
day, and *Run A, B and C*; and, on the stress-test model, **Tune Dial** and **Stress** (a surge on the compute realm, a sense gone
blind, a security hold, the kill switch). The card beside the cycle follows one muscle: its band, Omni-Compass's force F (solid
blue to add, pale blue to hand back), native's lever and the lever on top, and its own switch: *this muscle*, pressed, hands that
one muscle back to native's own controller while the rest stay governed, and *Every muscle back under Omni-Compass* restores them
all; the kill switch hands every muscle back at once.

## 14. Phase Plane and Scoreboard

This chapter reads the page's section 3f, **Phase Plane and Scoreboard** (`#s-plane`).

### 14.1 The two phase planes

A phase portrait, the picture control engineers use for a system's state. Across
is where each muscle sits in its band: p is 0 when calm, 0.5 at the center and 1 at its line. Up and down is how fast it
moves there (v, per decision). A muscle at rest sits on the middle line. One climbing toward its line moves up and right, and
past the right edge it is past its line. Native is on the left and Omni-Compass on the right: the same muscles at the same
instant, one dot each, with an arrow from where native holds a muscle to where Omni-Compass holds it, and a red ring, drawn as an
octagon, round a muscle past its line. In the stress-test model the shading on the right is the force the compass law would apply there: the
add force toward the line, the hand-back force toward calm. In the realms harness each muscle answers to its own rule, so no
single field is drawn.

![The compass band and the two forces. A reading is placed in its band, p = (r − lo)/(hi − lo), calm at 0, the center at ½, the line at 1, with 5% cushions at each end. Two antagonist forces act on the knob: the add force as the reading climbs toward the line, the hand-back force as it falls toward calm, combined as F = A·tanh((kₚ(p − ½) + k[d]·v)/A), smooth, never hammering. It fails up past 0.95 and never hands back while it climbs above the center. The phase plane's shading is this force at every point.](book/figures/band.svg)

### 14.2 Stat Panels, Last 120 Decisions

Each of the **Stat Panels, Last 120 Decisions · Class S** is one gauge of the live organism, read every decision on both sides, as an operations
dashboard shows it: native's value now and Omni-Compass's, the last 120 decisions of both (native solid orange, Omni-Compass
blue), and the running paired reading in the tables' words. With the master switch OFF the decisions are shaded red and
Omni-Compass's side follows native.

### 14.3 Running Scoreboard: how each row is read

Each row of the **Running Scoreboard · Class S** is the paired change, native against Omni-Compass at the same decision, averaged over blocks of ten
decisions so neighbouring decisions do not count twice, with its 95% interval (Student's t over the blocks). *This run*: a change
under 0.5% of native either way reads STEADY, and from 0.5% up the word follows the gauge's aim, whatever the interval says (work: a
rise is GAIN; misses, failed work, waiting: a fall is GAIN; energy or capacity held: a rise is power given, a fall a cut). *Three
runs*: the change is the mean of runs A, B and C; a mean under 0.5% reads STEADY; from 0.5% up the word by the gauge's aim; runs
that moved 0.5% or more in opposite directions disagree (section 36.4). The spread of positions and the settings are shown, never
judged: no rule of the engine aims at them. The spread can widen a little under the tune-down, because the calm muscles it hands
back move toward their line while the busy ones stay.

## 15. Brain State

This chapter reads the page's section 3g, **Brain State** (`#s-brain`).

### 15.1 What is drawn

The brain's six state variables rendered on their potential-energy
landscapes: a state resting at a minimum is stable; a state driven toward a maximum is under load. Each ball is a live value of
the engine's brain, integrated by the Runge–Kutta method every decision. In the stress-test model its push and target feed the
body's levers. In the harness views the harness arm acts muscle by muscle with no brain, so the brain drawn here is the page's
own, fed the harness's readings. Class S.

![The engine's six states. E the stress, U the utility, I[U] the memory of need, S the stance, B the slow tide of physical load and Ḃ its rate, each drawn on its own scale (E, U and I[U] on [0, 1], S on [−1, 1], B on [−0.5, 1], Ḃ on [−0.5, 0.5]). The brain monitor draws each as a ball on its own landscape, live, every decision.](book/figures/engine.svg)

### 15.2 The three potentials the page prints

**Double-Well Potential of U, Eq. (2)**, the utility's well, V(U) = −μ(U²/2 − U⁴/4) + (Ė/Eₘₐₓ)·U: a rising stress E
tilts the well toward the basin of collapse, and the ball rolls toward it unless the body is relieved. **Cubic Potential of
Stress S, Eqs. (5)–(6)**, the stance's well, Φ(S) = αₛS²/2 + βₛS³/4 − δS: S rolls to its minimum S* and the senses pull it back each decision. **Bath Oscillator B, Eq. (7)**, the
tide, B̈ = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B: the slow tide of physical load, a damped oscillator driven by the stance.

![The double well. The utility U rests in one of two basins: the working basin, where the body does its work inside its lines, and the basin of collapse. The stress E tilts the landscape; the brain's push and the body's relief tilt it back. A ball near the ridge between them is a body under load; the compass law and the nerves exist to keep it on the working side.](book/figures/potential.svg)

### 15.3 Nerves and Calm

calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)), where κ is the convergence (1 while the push is at or under its knee, else the knee
over the push), h the basin health ((U − U[gate])/(1 − U[gate]), held to [0, 1]), σ the stress ratio S/S* and ν the unmet need
(I[U], never below 0); the monitor draws the four as meters beside calm. An organ may hand capacity back only when calm ≥ its threshold θ, the line is
clean and every sense is live; expanding stays allowed except under a security hold. Under the max, lifting off toward native
never needs this grant; going below native does. The monitor draws calm against θ for each organ, so the operator sees why a
hand-back was refused. The four scalars and the grants are the nervous system of `docs/FACTORY_PROFILE.md`: observation, signal
propagation, coordination and authority pathways.

### 15.4 Native Controller Trace

Native has no brain to draw: each of its controllers reads one reading, its own muscle's, and moves.
The orange panel, **Native Controller Trace · Class S**, draws, live from the same decisions, the mean position native's muscles' readings put them at, the share of its
muscles past their line, and how many of its own controllers moved their setting this decision. Native has no nerves: nothing
grants or refuses a controller, and a blind sense or a security hold changes nothing it does.

## 16. Verdict

This chapter reads the page's section 3h, **Verdict** (`#s-verdict`).

### 16.1 The change-acceptance test

Before a knob moves one step past native, the step runs as a
trial: costs at native first, then at the step. The engine reads the change exactly as a report reads a row, on the log of
each cost, with its 95% interval. Each step is kept unless the measurement reads LOSS or its estimated cost exceeds the 2%
allowance; a STEADY result (no difference resolvable from the noise) is accepted, so on a high-variance workload a step with a
small true cost can pass, and the lab under the monitors measures that false-acceptance rate. Its two monitors are *Trial Costs
and 95% Interval* (the panel **Current Trial**) and *Share of Trials Allowed*.

![Block diagram: the verdict's paired trial around a slow knob, read GAIN, STEADY or LOSS. The reference is the cost of n pieces of work at the deepest step already allowed; the trial is the cost of n pieces at the step. Both on the log of the cost, with the 95% interval of their difference: an interval wholly above zero refuses the step; one inside the allowance keeps it; one wider than the allowance measures on, up to three times n each side. The verdict monitor runs this rule live at any true cost the viewer sets.](book/figures/c_verdict.svg)

### 16.2 The lab

Three knobs: *what the step truly does to the cost*, the *allowance* (tolerance) and the *noise σ of the log
cost*, with the *pieces of work measured each side*. Set what the step truly costs and watch the rule decide: the keep ratio at
each true cost is drawn, beside a rule of medians alone for comparison (the medians alone allow a step when the trial's median
is within the allowance of the reference's; the engine's rule also refuses any step whose interval sits wholly above zero, and
measures on while the interval is wider than the allowance, up to three times the pieces each side, keeping a step only if
both estimates are inside the allowance).

The lab opens wired as the shipped Kubernetes controller is wired, on the noise the real runs measured; the **Wiring** buttons
choose *Kubernetes, Google 2011 Day*, *Kubernetes, Load Swing 1 to 8*, *GPU Card* or *Model Gate*. *Run one trial*
and *Run 300 trials* run the rule at the cost set; a new trial starts on its own every few seconds.

### 16.3 How each muscle wires it

The Kubernetes controller measures 200 requests each side against a 2% allowance
(`--verdict-samples 200 --allow 0.02`), the cost being each request's response time; the noise is measured at every build on
each request of the newest tables' own runs. The GPU card measures 30 requests; in its model the card's own time per request
carries no noise. The model gate measures 60 (σ 0.25). Native has no trial: its knob never moves past its own setting, so there
is nothing to judge; every step Omni-Compass takes past native has to pass this test first.

![Flowchart: the give-back trial. A trial starts only with the organ's grant and a clean line; it runs to its full measurement and is never ended by the calm it causes; its reading against native decides, GAIN or STEADY keeps the step, LOSS refuses it and the setting stays; the release gate then passes or holds the write. The ticker's state column reads left native until a trial starts and acting while one runs.](book/figures/f_trial.svg)

## 17. Dashboards

This chapter reads the page's section 3i, **Dashboards** (`#s-dash`). It draws the
same live benchmark engine in nine forms an operations team already reads, each fed by the page's own model as it runs (class
S), native in orange beside Omni-Compass in blue, each change with its word by the key. The forms are the industry's; the
numbers are this engine's; no vendor's product is drawn or implied. On a phone each drawn form also writes what it shows as plain
lines under the drawing.

### 17.1 The nine forms

The section's **Form** buttons choose one of nine forms:

| Form | What it shows |
|---|---|
| Board of Panels | stat panels (muscles past their line, mean load, writes this decision, work so far), two time series (muscles past their line; capacity held) and a bar gauge per body part |
| Host Map | every muscle a cell, one row per body part, shaded by its load against its line; a cell past its line is the stop sign; native's map beside Omni-Compass's |
| Graph of One Series | one series over the decisions with the PromQL a running system's wall uses for it, and the change by its word |
| Event Stream | every decision as a line, newest first: each side's requests, cuts to a muscle's range and muscles past their line |
| Cluster Console | each body part a node, each muscle a workload, load and state on both sides; each row's button leaves the muscle native or drives it again and shows the request a running governor takes (`POST /v1/muscle`) |
| One-Line Diagram | the demand feeding five buses through twelve breakers each: closed, a muscle Omni-Compass drives; open, left native; tripped, past its line |
| Wall of Numbers | the decision, the heartbeat, the switch, muscles past their line, work waiting and failed, writes, native beside Omni-Compass |
| Cost by Body Part | the capacity held, body part by body part, the quantity a bill multiplies by its price; no price is recorded for the model, so no money is printed |
| Two-Way Pipeline, Omni-Compass's own form | demand, muscles, senses, readings, the brain, the constraints, the plug and the read-back, each edge with this decision's count; native's controllers and the kill switch beside it; the exporter carrying it all to Prometheus, Alloy and the wall |

### 17.2 Level, range and series, and the two tables

The **level** gathers each form by muscle, by body part or for the whole organism (*Each Muscle*, *Each Body Part*,
*Whole Organism*); the **range** sets 20, 60 or 240 decisions;
the **series** chooses what the graph draws. Under the forms the section's table, **Roles in the
Control Stack**, gives the words for every
tool a reader may know (an observer, a collector, a console, a native controller, an automatic optimizer, a supervisory governor),
who decides in each, well-known examples and where Omni-Compass sits beside each; `docs/FACTORY_PROFILE.md` carries the same
table, and `docs/THE_FIELD.md` maps the products by name. A second table, **First Five Products to
Benchmark**, names the first five
benchmarks against products that decide and act on their own (ScaleOps, StormForge Optimize Live, IBM Turbonomic, CAST AI and
Zeus), each with its rig and its cost as read on 24 October, and each marked not yet run.

---

# PART IV. REAL RUNS AND PLATFORMS

## 18. Kubernetes Run Playback

This chapter reads the page's section 4a, **Kubernetes Run Playback** (`#s-ops`).

### 18.1 What plays

A real-time operations dashboard over the benchmark runs themselves (class L),
not a model. Every series streams half minute by half minute out of the raw files GitHub archived, each file's SHA-256 matched
before a byte is drawn: native (the whole cluster with everything it ships with) against Omni-Compass, the same load, the
same second. Pick a benchmark, a run (A, B or C) and a repetition at the head of the section or in the page's section 4b; the tiles,
the candles, the heatmap, the bars and the tickers all move together with it. The **Data Pipeline** is its own monitor:
every stage from the GitHub Actions run to the page (the run, the raw files archived, the SHA-256 check, the official scorer,
the three-run tables, the build, the page) drawn whole, the stage being read lit and the data moving between them. 

### 18.2 Governor Heartbeat and Lease

A supervisory governor is only alive while its loop turns: once every decision it reads the whole body,
decides, writes, and proves it is still there. That turn is the heart. Each beat pumps every reading in through the plug and
the decision out (`omni_controller/controller.py`, its main loop) and renews the governor's lease (`master.heartbeat()`,
`omnicompass/master.py`). If the heart stops, its process gone or its lease older than its limit (the larger of 120 s and five
beats), the watchdog (`tools/omni_switch.py watchdog`) walks every setting back to native: a stopped heart leaves the body
exactly as native runs it. Native has no heart of its own: each of its controllers keeps its own clock, the pod autoscaler
one sync every 15 s, and nothing proves any of them is still there.

![Timing diagram: the lease. The governor renews its lease on every beat; the watchdog reads the lease on its own clock. When the governor dies without handing back, the lease ages past its limit (the larger of 120 s and five beats) and the watchdog walks every setting back to native, a step at a time, reading each back. On the page, the heart monitor shows the beat and how close the lease came to its limit; a stopped heart leaves the body exactly as native runs it.](book/figures/t_lease.svg)

### 18.3 A healthy heart, never pushed

The beat runs at a fixed, calm rate (the factory profile's full decision every 60 s since omni-v17, omni-v16's every 15 s, the
fast checks every 5 s between beats; the runs replayed here ran on the engine each table names, omni-v12 and omni-v21, each at the beat its run's own files
record) and is never
driven faster by the load it governs.
Every clock of the engine counts seconds, so the beat's pace sets how often the body is read, never what a rule means: a
give-back still waits its trial's minutes, the cushion still keeps its twenty minutes of memory, and a machine still goes
back at most one a minute. What it costs is counted inside the body's
own load (the row *Omni's own CPU*), so the organism never pays for its brain without knowing it. A decision that fails is
recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal
time. Two gauges read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page
calls a heart under strain when a decision takes more than half its beat, or a gap between beats reaches 80% of the lease. Both
lines are the page's reading, not rules of the engine; the engine's own guard is the lease and the watchdog.

### 18.4 Heartbeat Sweep

Under the heart stands the heartbeat sweep (the panel `#beatPanel`, monitor *Heartbeat Sweep · Class
S*). The beat is a setting of the run, not a constant: the factory profile sets 60 s since omni-v17 (omni-v16 set 15 s, the pod
autoscaler's own pace), and an operator may choose another for a system's own reasons (a slower beat reads the cluster less often; a faster one answers sooner). The monitor shows what each
choice does. Its five rows of buttons pick the record to read:

- **Beat:** 5, 10, 15, 20, 30, 60, 75, 90 or 120 s.
- **Setting:** on-site, where the governor sizes the pool on top of the pod autoscaler, or in the cloud, the machines alone.
- **Engine:** omni-v16, every clock in seconds, or omni-v15, its rules counted in beats.
- **Against:** what each reading is set against: native, the same engine at 15 s (omni-v16's factory beat), or the same
  engine at 60 s (omni-v17's). The sweep's record is omni-v16's and omni-v15's; the dial's ladder (the page's section 3d, chapter 12) reads omni-v17.
  The monitor opens on 60 s, the factory's beat on the engine that stands.
- **Gauge:** *Pods Waiting* (pods waiting for a place), *Machines* (machine-hours), *Energy per Core-Hour*, *95th
  Percentile* and *99th Percentile* response, *Alert Minutes* (the minutes over the line), and the engine's own cost: *Engine
  CPU per Day*, *Cluster Reads per Day*, *Writes per Day* and *Fast-Check Rescues per Day*, the machines its 5-second check
  added only after a pod already waited.

The tiles give the chosen beat whole. They show what it is read against and every gauge's mean change with its 95% interval
and its word (GAIN, STEADY, LOSS or power given, by the one key); the number carries the word's sign (GAIN +, LOSS −, STEADY =),
never the gauge's raw direction. The last tiles give the engine's own cost a day; native,
which runs no governor, costs nothing there. The rescues tile says why a slow beat waits more: the full decision sizes the
pool ahead of the load, and read less often, the load outruns it between decisions, so the 5-second check adds the machine
only once a pod already waits.

The chart gives the chosen gauge at every beat. Each bar is the mean change over the seeds, coloured by its word, with its
whisker the 95% interval. A fall cannot pass −100%, so an interval reaching past it is cut there and marked ▼; the tiles
print it whole. The beat chosen is framed, and a cursor reads the beats in turn and names the row it holds.

Every number is our own model (evidence class S), never a benchmark result. The shipped controller of each engine runs on the
modelled cluster's 5-second plant, eight seeds of a day each, paired by seed and read by the model gate's own rule
(`tools/heartbeat_sweep.py`; the record, `results/model_gate/HEARTBEAT_SWEEP.md`). Every beat on this monitor is read in
the model only: a real run reads the one beat it was started with, the governor's `--interval`, and the gauges
`omni_decisions_total` and `omni_own_cpu_cores` of `tools/omni_exporter.py` show the beat it runs at and what it costs.

### 18.5 Response Time Candlesticks, Latency Heatmap and Throughput per 30 s Bin

**Response Time Candlesticks**, one candlestick per 30-second bin (open, high, low, close of the responses in the
bin), native beside Omni-Compass; **Latency Heatmap**, every response binned by time and by duration, the darker the fuller;
**Throughput per 30 s Bin**, requests served per 30-second bin. Read the three together: a GAIN in the 99th percentile shows as the candles'
upper wicks shortening on the blue side while the heatmap's upper band thins and the throughput bars stand level or higher.

### 18.6 Governor Decision Ticker

From the repetition's own `audit.jsonl`: the minute and second of the decision, the compass
position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward
native). Then the machines it recommends, and the give-back verdict's state: *left native* means every setting stays
native's; *acting* means a trial on its own measurement. Every line of the ticker is a line of the governor's audit, and the
audit is the record of authority for what it did.

### 18.7 Native Controller Ticker

Native has no governor; its own controllers' moves are the second ticker, read
from the native arm's `capture.csv`: the replicas its pod autoscaler holds, the pods waiting for a place and the machines
ready, every change in the same repetition, newest first. With Omni-Compass OFF the first ticker is empty, for nothing
decides on top of native. The two tickers side by side are the mechanism of action in its plainest form (chapter 42).

![One pedal, no brake. Pushing the pedal adds capacity at once; lifting it eases capacity back toward native a step at a time, never below idle, the floor of two machines. Cruise holds every machine in service while a known queue waits. Watching reads and writes nothing. On the governor's ticker, push and lift are the force column, and the machines recommended are what the pedal bought or handed back.](book/figures/pedal.svg)

### 18.8 Paired Repetitions and Benchmark Status by Block

**Paired Repetitions**: each repetition of the run as one small pair of lines, the one streaming now outlined; click a pair to
stream it. **Benchmark Status by Block**: landed, running, queued, or not yet run, for every Kubernetes benchmark of the
campaign. The run's receipt and each repetition's score stand in the page's section 4b (section 19.3).

## 19. Repetition Telemetry

This chapter reads the page's section 4b, **Repetition Telemetry** (`#s-runs`).

### 19.1 What it is

The benchmark runs themselves at one-second resolution: each three-run table's
runs A, B and C read back from the raw files GitHub archived (`results/live/raw`, on the `raw` branch), native and
Omni-Compass, repetition by repetition, played second by second. Every file the page reads has its SHA-256 computed and
matched against the run's own `SHA256SUMS_ALL.txt`, and every Kubernetes repetition is scored by `tools/live_reps.py`;
where a run holds its own scored summary, the scorer's mean over its repetitions equals it. Class L: real Kubernetes on kind,
real databases and a real broker.

### 19.2 How to use it

Choose the benchmark, the run and the repetition; the page's section 4a dashboard follows. Read a gauge's
two lines against each other for the whole repetition, then read the receipt of the run under it: the receipt's word is the
reading; the lines are why. A repetition whose job failed and ran again is marked; one that failed three times is listed and
left out.

### 19.3 Run Receipt, Repetition Score and Benchmark Landing Status

Under the lanes, **Run Receipt** is the receipt of this run as the repository wrote it, and **Repetition Score** is
this repetition scored by the repository's own scorer, gauge by gauge, native beside Omni-Compass with the run's reading over
all its repetitions, which must equal the run's own summary over its repetitions (the count of matches is printed). The page
holds its own scoring of every repetition against the run's own scored summary (`LIVE_REPS.json`) and prints the largest
relative difference: at machine precision (about 1e-16) for every run, the governors that run a group of two clusters included,
whose every file the scorer reads at its own place in the repetition's folder. **Benchmark Landing Status** gives each
benchmark's group, its newest three-run table and where it stands now.

## 20. Controller Decision Trace

This chapter reads the page's section 4c, **Controller Decision Trace** (`#s-live`).

### 20.1 The one place the brain drives the muscles decision by decision

The shipped controller,
`omni_controller/controller.py`, on the modelled cluster of `pilot/selfpilot.py`, wired as the repository wires it. Each decision
runs the chain left to right: the senses, the six-state brain, the nerves and the machine organ's grant, the compass law on
the service (the cloud setting), the verdict's trial, the release gate, the plug. Every value below the chain is the
controller's own audit record of that decision, recorded by `docs/engine/export_controller_trace.py` on runs A, B and C (six
hours each, a decision every 60 s, the fast checks at every 15-second tick between; class S). Two buttons choose the setting,
*On Top of the HPA at the Max* and *Cloud at the Tune-Down, Machines Only*, and three choose the run; the Linux host and the card
are the page's section 4f.

![One decision of the governor. Read the body (the senses), place every reading in its band, let the brain's state evolve, grant or refuse through the nerves, apply the compass law to each muscle (push or lift), run the verdict's trial on a step past native, pass the release gate, write through the plug and read it back, renew the lease. On the decision-trace monitor each box is one column of the audit, and *open the same controller, decision by decision* steps through them.](book/figures/loop.svg)

### 20.2 Audited Decision Chain

The panel **Audited Decision Chain** steps through the chain; the columns, in the audit's order: the stress E, the utility U, the calm, κ, h, σ, ν (the four
scalars of the nerves), the gate and whether it passed, whether machines were in service (a blind reading holds the
decision), the recommendation, the machines seen, the density ρ, the compass position and velocity, the force, the verdict's
word, the writes, the queue, and the law that decided. A row whose gate did not pass wrote nothing; a row whose verdict reads
LOSS kept the setting at native; a row with a write names the lever and the value read back.

### 20.3 Three-Run Score

**Three-Run Score · Class S**: the paired change per 15-second tick, averaged over ten-minute blocks, with its 95% interval (Student's t) in each run; the three runs read by the
key (section 36.4). Machines and power: a fall is a cut, a GAIN; a rise is power given. Our own models (class S): a model's small
numbers are the model's.

### 20.4 Kubernetes Three-Run Tables and Governor Steering

Beside the model's three runs, **Kubernetes Three-Run Tables · Class L** sets what the real thing reads (class L: real Kubernetes, three runs each): every
Kubernetes three-run table on the page, each on its newest engine, with its rows that read GAIN in all three of our runs, power
given, LOSS in all three and STEADY. Under them, **Governor Steering on Kubernetes · Class L** reads how steadily the governor steered on real Kubernetes: its own moves on
every table `results/STEERING.json` holds, each on its own engine, beside native's own controllers.

## 21. Cloud Providers

This chapter reads the page's section 4d, **Cloud Providers** (`#s-cloud`).

### 21.1 The cloud is a wire

The cloud providers' section (the page's section 4d) opens with a box: "THE CLOUD IS A WIRE. A CLOUD RUN ALONE CAN SHOW ONLY A LITTLE." A
cloud is the wire between the software end (the owner's programs, Kubernetes and the open-source orchestrators, managers and
autoscalers that carry the work) and the hardware end (the bare metal: the GPU chips, the Linux racks, the data center, on-site
or off-site). Omni-Compass can live in all three places: on the software end, on the cloud's wire, and on the bare metal. On the
wire alone (every cloud run on the page: Omni-Compass at the tune-down on the machines only, the pods exactly native's), all it
can do is park machines the cloud's own autoscaler already made, after its own trial; so the most a cloud run can show is a small
cut in the bill of the wire. It cannot show the work and speed gained at the software end, nor the energy and throughput gained
at the bare metal, because neither end is under it. The larger benefit lives at the two ends. No tenant can meter a provider's
back end, so the page claims that benefit only as the same mechanism measured on hardware the repository can meter (the page's
section 4f), never as a measurement of the provider's machines.

The box then gives the company's own expectation, not a measured result (24 October): about 3 to 4%
from the front end, 2 to 3% from the back end, about 5% from the two ends together, and 1 to 2% from the wire alone, as a smaller
bill or more work for the same bill. Under it a table reads the measured readings of each place, gauge by gauge (work, speed,
machines, energy, the bill): the software end, the bare metal, the cloud's wire alone, on site with the two ends together, and
through the cloud with all three, each cell its word and its number with its interval, composed by our own code (class S) from the layers measured in it
(class L and P), and the cloud's wire, one run each, reading "not read";
where a measurement differs from the expectation, the measurement stands. The same box and table stand at the head of the whole
organism (the page's section 5d), and both follow that section's reading and chip knobs.

### 21.2 One metric: the bill

In a cloud Omni-Compass shows one thing: the same work as native for a smaller bill, never a
bigger one. Every cloud set runs Omni-Compass at the tune-down on the machines alone (`OMNI_MACHINES_ONLY=1`,
`--give-back-only`): no pod autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's. It parks
only a machine the cloud already made, after its own trial, and wakes it on a breach. The bill and the machines aim lower;
work, speed and failures must read STEADY or GAIN. Azure runs first and is the measure of the other two (Google Cloud, Amazon
Web Services): the same tuning, mechanism and harness. Google's and Amazon's sets are not yet run: their queues are switched off
(24 October), kept ready as Azure's sets run, and the page reads each of their rows "not yet run" until each queue is switched on.

### 21.3 Cloud Run Ledger, Cloud Bill and Gate Monitors, and the Cloud-Setting Controller

**Cloud Run Ledger** gives each provider's four sets (the steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real
day of Google 2011 on 1 to 9) and their status: measured to the end, stopped before a result, or running or queued. **Cloud Bill
and Gate Monitors** draws one monitor a provider, the same harness, mechanism and tuning in all three: each bar pair is a
finished set, native's machine-hours (orange) beside Omni-Compass's (blue), the run's own word by the one key with its size, and
the bill at list price under it; one run is never a set's reading. A provider with no finished set shows its empty frame and
the reason its hourly gate holds, in its own job's words; nothing is drawn for a run that has not run. **Azure Bill by Run**
gives the bill on Azure run by run (machine-hours billed native · Omni-Compass; the bill; the 95th percentile; the failed
requests), each with the engine it ran on. **Cloud-Setting Controller · Class S** plays the shipped controller in the cloud
setting, live: native's machines against Omni-Compass's on the repository's modelled cluster, the cloud's own autoscaler
running in both arms, its run and speed following the console's clock; the bill counts every machine that exists, in service,
booting or parked.

### 21.4 The stopping rule

From 19 October every Azure set runs up to 100 paired repetitions a run, the paid cap, under the
preregistered stopping rule (`tools/stop_rule.py`). After 10, 20, 40 and 70 repetitions the bill's change is read with its
99% interval. The run stops once the bill is read (GAIN, power given, or STEADY within ±2% of native's bill), and never while the
speed or the failed requests read a LOSS. Those runs carry "to the cap, stopping rule" in their title and count as their own
A, B and C. So a cloud set that has run for a day and a half and shows no result on the board is not a fault: its bill has not
yet been read at a look, and `peek` (`.github/workflows/peek.yml`) prints its finished repetitions, paired, while it runs.

### 21.5 Reading a cloud receipt

The rows an operator reads first: machines billed (machine-hours) and the compute bill at
list price, both aiming lower; then the response time's mean, 95th and 99th percentiles, the time over the line, the failed
requests and the alert minutes, all aiming lower and all required STEADY or GAIN; then the rows shown and not judged: the
settings commands the governor wrote on its own (native is 0), the share of its additions decided inside the line, Omni-Compass's
own processor time. A bill not yet read at a look (GAIN, power given, or STEADY within ±2% of native's bill, by the stopping rule)
runs on to its next look.

### 21.6 When a cloud is not ready

The conductor starts a cloud's set only after that cloud's newest check passed
(`.github/workflows/cloud-check.yml`, `tools/cloud_key_check.py`: the key whole, the login, the plan, the machine type,
every quota), at no cost. The monitor shows a failed check as the cloud's status, in the check's own words: a Google key stored
cut short (the stored secret shorter than a whole key file) is stored again whole (`docs/GOOGLE_SETUP.md`, section 4); an Amazon
account on the Free plan, whose organization policy denies every machine read, is moved to the Paid plan
(`docs/AMAZON_SETUP.md`, section 1a); an Azure key stored in another form than the whole block from `{` to `}` (a client
secret's value alone, or a storage account's access key, for two) is stored again: one value to each of four boxes, or the
whole block under a new name, which leaves a running set's login untouched (`docs/AZURE_SETUP.md`, section 7; Azure joined the
check on 22 October). Nothing is built and nothing is billed until the check passes.

## 22. Orchestrators and Governors

This chapter reads the page's section 4e, **Orchestrators and Governors** (`#s-orch`).

### 22.1 What they are

The governors and orchestrators that sit between the work and the cluster: batch schedulers and job
queues (Kueue, Volcano, the KAI scheduler, Armada), multi-cluster governors (Karmada, Open Cluster Management), the default
Kubernetes scheduler and its bin-packing profile, the co-location and rightsizing controllers (Koordinator, Crane, CruiseKube,
Goldilocks), the GPU and edge orchestrators (KubeRay, KubeEdge, Nephio) and Gödel. Each runs live on real Kubernetes as its
project ships it, native and with Omni-Compass on top of it; Omni-Compass never replaces the orchestrator.

### 22.2 Road to a Result, Orchestration Stack and the Catalog

**Road to a Result**, every governor at once: its register row, its
preregistration, its rig on GitHub, runs A, B and C, and its three-run table as it lands. **Orchestration Stack**, live:
Omni-Compass on top, the governor native as shipped, Kubernetes and its nodes beneath, the work dots moving at the live
engine's demand (a picture of the flow, not a measurement, replaced by the governor's readings the moment its three runs
land). **Governor and Orchestrator Catalog**: what each governs, native as shipped, Omni-Compass on top, and what the repository holds
today. Click a governor (a tile, a row of the road or of the catalog) to hold it in every view.

### 22.3 Four-Way Comparison

Each governor runs with the organism alone (nativebare), the
orchestrator as shipped (native), Omni-Compass on top of the organism alone (compassbare) and Omni-Compass on top of the
orchestrator (compass), all four in every repetition, each comparison paired within it and read by the one key
(`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6). On the organism alone Omni-Compass sits on top of Kubernetes' own
scheduler. The monitor shows the four as four columns of one table per governor; the comparisons an operator reads first are
native against compass (what Omni-Compass adds on top of the orchestrator) and nativebare against compassbare (what it adds
with no orchestrator at all). In the official-run playback (the page's section 4a) each of a governor's five tables plays its own
two arms of the run's repetitions, named on the lanes, the candles, the heat map and the repetition's table by the table's own
words, the left lane its reference and the right lane its candidate; Omni-Compass's colour is drawn only on an arm that carries
Omni-Compass, so the orchestrator's own cost (the orchestrator as shipped against the organism alone) plays in native's colours on
both lanes.

### 22.4 Orchestra Organism

The eighth organism: every governor's catalog muscles, each governor's a body of its own and all of
them together one body, native and with Omni-Compass on top (modelled, class S; `tools/run_orchestra.py`,
`results/orchestra/ORCHESTRA.md`). It is a grouping of catalog rows like the seven, never an engine file.

## 23. GPU and CPU Hardware

This chapter reads the page's section 4f, **GPU and CPU Hardware** (`#s-stacks`).

### 23.1 Metered Hardware Run Slots

The silicon itself, the chip at the far end of every stack: there
the max would ride each card's own limit, and every watt it takes is power given, shown beside the work it buys. **Metered Hardware Run Slots** holds
the slots for the metered GPU and CPU runs (class P: the card's own meter on Lambda; the package's own energy counter,
`tools/run_cpu_power.py`), every chip run GitHub has started, newest first (**Chip Run Ledger**), and then the models of one GPU card and one
Linux host (class S), native beside Omni-Compass, each run twice on the same load and seed, native first.

### 23.2 Metered A100 Run and CPU Host Model

The engine that stands on a real card, its own meter recording native beside Omni-Compass, plays second by second (class P):
an NVIDIA A100 (SXM4, 40 GB) on Lambda on 24 October (workflow run 40079645681, omni-v18's card governor at commit e3b05dc), ten paired repetitions
of 600 s an arm, native (the card as shipped), Omni-Compass watching only (the switch OFF: it reads and writes nothing) and
Omni-Compass governing the power limit and the clock ceiling, every `nvidia-smi` sample and every decision of the governor's own
audit (`results/gpu/run-20261024T091235Z`, `docs/engine/export_gpu_run.py`). On this card native already runs both knobs at their
top (the power limit 400 W of 400 W, the clock unlocked to 1,410 MHz), so the factory tune's governor asked for exactly that in its
3,050 decisions and wrote nothing: at its limit on
native, every service gauge STEADY. The runs on the engine that stands and their three-run tables are counted in the hardware run slots and listed run by run
in the Chip Run Ledger; the 8-card run has not been run (its one launch was a priced dry run). The A10 run of 2 October (the card controller
of commit c908054, replaced since) stays as its own record. Its table is re-read by the one key. The CPU host is built and waits for its machine: the CPU
power harness (`tools/run_cpu_power.py`) puts Omni-Compass on top of the Linux kernel's own frequency governor and meters the
processor's package energy (RAPL); no GitHub runner exposes that counter or a writable ceiling, so until a Linux machine that
does is attached the monitor plays the harness on its own modelled machine (class S), marked AWAITING ITS MACHINE, a model, not a
measurement.

### 23.3 Chip Model Settings

Buttons choose the stack (*GPU Card*; *Linux Host*; and two that lead to the page's sections 4c and 4d, Kubernetes and the
cloud), the work on the card
(*AI Token Generation*; *Compute-Bound*) and the card's native power setting (*Shipped Limit, 150 W*; *Operator Cap, 105 W*).
The table, **Chip Model Settings · Class S**, lists every setting with three
runs each: the seconds held off native, the writes, the power (W) or the host's busy share native · Omni-Compass, and the
response (ms) native · Omni-Compass. Click a setting to play it; under it stand **Omni-Compass Audit Trail · Class S** and **Three-Run
Score · Class S**.

### 23.4 8-Card GPU Node, Awaiting Its Run

In the same section a node of eight NVIDIA cards stands built before its run (`scripts/gpu_8card.sh`,
`docs/GPU_RUN_GUIDE.md`, section D): eight card slots, each native lane drawn from the repository's one-card model (class S, the
same model on every card until the run, never eight measurements), each Omni-Compass lane empty and marked awaiting its run.
Nothing on it is invented: on a running node the same panel reads the NVIDIA DCGM exporter's series card by card, and the
8-card run fills it when it lands.

### 23.5 Reading a row with nothing held off native

A row with no second held off native is Omni-Compass deciding to stay
native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native. That row is the
engine's own rule at work and is not a fault. The slots marked not yet run are written as the repository holds them and fill
in, played back from their raw files like every Kubernetes run, the moment their three runs land.

## 24. CI Pipeline

This chapter reads the page's section 4g, **CI Pipeline** (`#s-github`).

### 24.1 When the page is rebuilt

GitHub rebuilds the page (`.github/workflows/live-engine.yml`,
`docs/engine/build_live_engine.py`) whenever the engine, a model or a result changes, and every three hours. Every record is
made again by the repository's own code on the engine that stands, checked against the Python and the C++, and committed.
The page's own file is outside its own push filter, so a rebuild never starts another rebuild; a front-page run that did not
succeed starts no rebuild (`tests/test_workflow_triggers.py` holds both).

### 24.2 GitHub Actions in Flight and Running and Queued Workflows

**Running and Queued Workflows**: every workflow run in
progress or queued at the build, as GitHub's own list at that moment, and the first three of them in each state. Above the table, **GitHub Actions in Flight** draws GitHub Actions as a monitor:
the runs in flight by workflow (running solid blue, waiting pale), the Azure set to the paid cap with its repetitions measured so
far, and each cloud's hourly gate with the reason its own job wrote. The hardware and cloud runs, with their terminal status, are in
the page's sections 4d and 4f; every run on the engine that stands that terminated without a measurement is raised on the status board.

### 24.3 Reading the pipeline against the conductor

The conductor (`scripts/dispatch_grid.py`, every 15 minutes) starts
every run of the campaign on the engine that stands, A of every benchmark, then B, then C, a few a tick, and never starts one
twice; it starts nothing while an Azure run, a grid report or a verify waits for a runner. So a pipeline monitor showing one
Azure run queued and nothing else starting is the conductor holding, by its rule, not a fault. A long run on a free runner
(the organisms at 1,000 copies) lists as in progress for its whole shard.

---

# PART V. PROOF AND MODELS

## 25. Python Runs and Monte Carlo

This chapter reads the page's section 5a, **Python Runs and Monte Carlo** (`#s-proof`).

### 25.1 Three-Way Run Check

The proof monitor, **Three-Way Run Check** (the page's section 5a, `#s-proof`, in the panel **Seeded Engine Runs and
Replayed Scenarios**), reads every run three ways: the Python's set as GitHub ran it
(`tools/engine_runs.py`, its run linked), the same draws through the C++ harness on the engine's C++ twins
(`cpp/tools/engine_runs.cpp`), and this page's own port, one SHA-256 digest each beside the digest of the draws themselves; the
three must be one. Once that first check ends, the page checks the set again without end: one run at a time, about twice a
second, each run recomputed from its own seed by the page's engine and held against the Python's receipt; the run being checked
is boxed on all three lanes and its result printed under the digests.

### 25.2 Running the Python's runs again

In the proof (the page's section 5a, `#s-proof`), beside "Run a new set here", the button
"Run another 500" runs the next set from the base after the last one, and "Run three more sets" runs three in a row; the table
under the monitor lists every set run on the page with its digest and, where the Python has run the same base, the Python's record
and whether the two digests match; where it has not, the line names the engine-runs workflow on GitHub with the runs and the base
that make the Python run the same set.

### 25.3 Held-Out Scenario Replay

Under the proof monitor, in **Held-Out Scenario Replay**, the Python's 500 scenarios a seed replay from their own record, native beside Omni-Compass, scenario by
scenario, with every trace hash; its words stand in its own table.

### 25.4 Engine Core Monte Carlo

The Monte Carlo monitor, **Engine Core Monte Carlo** (the page's section 5a, `#mcPanel`), draws the Python's Monte Carlo of
the engine's core. Every line is one run of the
engine's core (`omnicompass/core.py`: six states, the fourth-order Runge–Kutta step 10 times a macro step of 0.1 s, 20 macro steps),
its U from step 0 to step 20, drawn up to a cursor that sweeps the 20 steps in 10 seconds and holds 3. The left lane is native: the
same plant with no command (u = 0), left to its own double well. The right lane is Omni-Compass on top: the bounded command toward the
nearest basin (|u| ≤ 25, held across the four stages), or, by the knob, toward the far basin, or with the double well switched off
(μ = 0). The green bands are the basins, |U ∓ 1| ≤ 0.10. A run is conveyed when it has stayed in one basin 5 macro steps in a row and
certified at 10; each lane's counters read at the cursor (in a basin, conveyed, certified, of 500), a run's head turns green once
certified, and the bars under each lane count the macro step each run was conveyed and certified. The set the page opens on is the
Python's own 500 (`benchmarks/core_evidence.py`, numpy's generator from seed 223387268), whose counts must be its record's
(`results/core_evidence.json`: Omni-Compass on top conveyed 500 and certified 500, at macro steps 4 to 6; native alone conveyed 476 and
certified 427). A set the page draws from the jump generator is computed by the page's own port of the core, line for line, and its
digest must be the one `tools/core_runs.py` writes for the same base (`tools/core_runs.py --verify` runs the page's port in node and
compares; the engine-runs workflow writes the Python's record of every base it runs). The table under the monitor lists every set,
its counts on both sides and whether its digest matches the Python's. The monitor's light reads the set shown: green when Omni-Compass
on top certified more runs than native alone, yellow when the same, red when fewer or when the page's digest differs from the Python's
or the C++'s record of the same base.

### 25.5 The linked run and the Custom System Run

Two buttons link the runs. **Run the Monte Carlo 500: the Python, the C++ and this page, linked** (in the control panel and on
the monitor) stands three boxes side by side: 1, the Python, the newest set `tools/core_runs.py` ran from the jump generator, with its
digest and its record; 2, the C++, the C++ twin of the core (`cpp/tools/core_runs.cpp` on the sealed `cpp/src/core.cpp`) on the very
draws the Python wrote (the injection, its own SHA-256), with its digest, how many of the 2,000 run-ways agree to 1e-9 and the largest
difference; 3, this page, its own port of the core run on the same base when the button is pressed. The line under them reads
**ALL THREE THE SAME** when the three digests are one (every U at every macro step, four ways, to six decimals), and says so if they
differ; the three are sealed together (`tools/seal.py`, the thirteenth twin) and `verify.py` runs the C++ against the Python on every
push. **Run your own system through it** opens the panel **Custom System Run**: a system is your own stack written as ranges of the core, a name and, for any
of the six starting states and the 22 parameters, a range or one number, the rest the engine's own (`systems/README.md`). It opens on
the engine's own ranges, every one editable; **Load the example** puts in `systems/example_heavy_swing.json` (heavy outside demand,
a strong swing, little headroom; not any real stack). **Check it** reads the block as the Python does and names anything refused;
**Run it here** draws 500 runs in the browser through the page's port (on the base the Python ran that system on, so its digest
compares, else on the linked run's base) and draws them in the monitor beside native; **Download it as a file** saves it for
`systems/`; **Run it on GitHub** checks it, copies it and opens the **monte-carlo** workflow (`.github/workflows/monte-carlo.yml`):
press **Run workflow**, paste the block into **system**, set the runs and the base, and run. On GitHub's own machine, at no cost,
the Python draws the runs over your ranges, the C++ twin runs the same draws, the page's port is run on them in node, and the three
digests must be one; the record, with the run's link, goes to `results/core_runs/` and joins the monitor's table at the page's next
build. A system file committed under `systems/` runs on every push that changes it. GitHub offers **Run workflow** for a workflow on
the repository's main branch, so the button's GitHub half works once omni-v18 reaches main; the page half works now. The block is
read as numbers only, never run as code. Class S: the engine's own mathematics on your ranges, never a measurement of your stack;
wiring Omni-Compass onto the stack itself is the plug of the Operator's Manual.

## 26. C++ Twin

This chapter reads the page's section 5b, **C++ Twin** (`#s-cpp`).

### 26.1 The Python's runs through the C++ engine: five tables

The engine is written twice, in Python and in C++, line for line where a twin exists. Every time the page is built, the
Python's own runs are fed into the C++ as its input and the C++ answer is set beside the Python's, number by number. Where
they are the same to the last digit, the two are one engine. The section holds five tables.

| Table | What it shows | How to read it |
|---|---|---|
| Twin Parity Checks | each Python file and its C++ twin, the inputs the check fed both, the largest difference, and the reading | "the same" on every row is a whole engine in two languages; "DIFFERS" names the row to look at |
| C++ Engine Run Receipts | the record of the Python's seeded runs the page shows (the jump generator's 500), its draws (the Python's injection) fed to the C++ harness at the page's build (`cpp/tools/engine_runs.cpp`): the record, its runs and base seed, the Python's digest, the C++ engine's digest, how many receipts are identical to the last bit, the largest difference, the reading, and the GitHub run that made the record | the Python's runs are the input and the C++ engine's receipts the output; the two digests one string and every receipt identical is the same engine run twice, in two languages |
| Compass Law Parity on Page Runs | every compass law the page's own runs wired while the page was built, grouped by the file that wired it, each law's readings in the order they came, through the C++ law and through the Python again | the C++ against the Python, and the Python again against the run's own forces: 0 (identical) on both is the run's law reproduced exactly |
| Organism Law Parity at the Tune-Down | each organism, its muscles, the muscles that run the compass law at the tune-down, the readings fed through the C++, and any muscle that differs | at the max, the default brain, the edge and the bone decide each muscle, and they have no C++ twin yet; the tune-down is where every muscle's law is the compass law, so that is where it is fed through |
| Python-Only Components | every part of the engine with no C++ twin yet, by file | the list is the work still to twin; nothing on it is hidden from the other tables |

A box under the organisms' table finds any muscle by its catalog id: it names each organism the muscle's law ran in, its
readings, and whether the C++ and the Python gave the same answer. A muscle with no lever at the tune-down stays native
there, and the box says so.

## 27. Scenarios and Injection Grid

This chapter reads the page's section 5c, **Scenarios and Injection Grid** (`#s-scn`).

### 27.1 Twenty Scenarios

The grid of the page's section 5c, `#s-scn`, reads ten organisms two ways each: the spine; the four realms (Compute/AI/Cloud,
Physics/Robotics/Autonomous, Energy/Facility/Industrial, Distribution/Specialized); the four stacked; the whole tower; the
orchestra; the live benchmark engine's own organism of sixty muscles; and the whole organism in its three places. Each runs **native
alone** and **Omni-Compass on native** (the factory profile, on top of every native controller), on the same seeds, so the same
demand meets both. Omni-Compass is never by itself, so there is no third way. That makes
twenty cells, each read by the key against native, from the record `results/scenarios/SCENARIOS_20.json` (written out as
`results/scenarios/SCENARIOS_20.md`, by `tools/scenarios_20.py`; class S, our own models, three runs A, B and C). A cell with no
run reads "not yet run", never a number. The same grid stands, compact, in the control panel (section 2.24). The earlier
record of thirty scenarios is kept as history in `docs/history/SCENARIOS_30_2026-10-24.md`; the page does not read it.

### 27.2 One cell

Each cell carries one signal word and one number against native. The native column reads STEADY and 0%, the yardstick. In the
Omni-Compass on native column the organism's gauges are work, the time over the line and the power drawn: a cell is red,
REDLINING, when any of them reads LOSS, green, GAINING, when any reads GAIN and none LOSS, and yellow, STEADY, otherwise; its
number is the gauge that decided the light (work, where work decides it), with the word's sign (+ a GAIN, − a LOSS, = STEADY). The
whole organism's cell reads its composition's index over the gauges (chapter 28). Hover a cell for each gauge's reading and each
run's change.

### 27.3 Its detail and its three runs

Click a cell for its detail under the grid: the organism, what it is, its muscles and its class, then a table of its one pair,
Omni-Compass on native against native, on work, the time over the line and the power drawn, each with its word, its reading and
the change of each run A, B and C. Every run under 0.5% reads STEADY; from 0.5% up the word by what the gauge is for; runs pointing
different ways, the runs disagree. The note names the record's file, its engine and its commit. A click on the live benchmark engine's
organism in the Omni-Compass on native column also puts the live benchmark engine on that body, the harness's one organism.

### 27.4 Injection Grid

Under the twenty scenarios the section carries the injection grid (`#s-inj`; the record
`results/injection_grid/INJECTION_GRID_<base>.json` and its `.md`, written by `tools/injection_grid.py`; class S). Its line
under the heading, **The batch**, names the batch it stands on: its base, its 500 injections and the jump generator's rule (seed_k =
base + k·0x9E3779B9 mod 2³²), the digest of the Python's runs of that batch and its file, and the C++ engine's digest of the same
seeds ("identical", with the count of runs that agree). The same batch drives the Python's runs in the page's section 5a. An injection is one
seed: every plant of every organism draws its demand, its weather and its disturbances from it, under the climb, for 240 decisions
of 15 s, and the same injection reaches every organism and every way.

The same line prints two checks the page makes as it opens. First it re-hashes the record's cells the way the Python hashed them
and prints "identical digest to the Python's" or "not identical to the Python's". Then it recomputes every cell's mean from the runs' means, joined and
stacked as the Python joins and stacks them, and prints the number of cell gauges checked. It reports "every one agrees" with the
largest difference, or the count that differ by more than 0.001 points and where the largest one is. The engine, the commit, when
it ran and on how many processes close the line.

### 27.5 The knobs

- **Organism**: the nine organisms with a plant, by their scenario number (the spine 1 to the live benchmark engine's own organism 9), each
  with its muscles. The whole organism (10) is a composition of measured tables and takes no injection; its reading stands in
  the twenty scenarios above.
- **Way**: *Omni-Compass on native*; *a governor on the organism* (each of the fourteen: the Kubernetes scheduler with its
  bin-packing profile, Kueue, Volcano, KAI, Koordinator, CruiseKube, Crane, KubeRay, Gödel, Armada, Karmada, Open Cluster
  Management, KubeEdge and Nephio); *Omni-Compass on top of a governor*. The orchestra already holds every governor's muscles,
  so on it only Omni-Compass on native is offered.
- **Against**: native, and, for Omni-Compass on top of a governor, the governor on the organism too, so Omni-Compass's own
  effect on that governed stack is read alone.
- **Runs**: 1, 10, 100 or 500. **Organisms stacked**: 1, 10, 100 or 500. Every cell is the one batch cut down: 100 runs are
  the first 100 of the batch's 500, 10 the first 10, 1 the first; and each run carries a stack of 500 organisms, of which 100
  organisms are the first 100 copies, 10 the first 10, 1 the first (copy c of run k on injection k + c, mod 500). A click on
  100 shows those 100 and no others. A cell whose runs × organisms pass 500 uses an injection more than once, and its readout
  says so.
- **Gauge**: work, the share of muscles over the line, or the power per muscle. Every gauge is read per muscle. Two ways on the
  same muscles read the same either way, and a governor's way, which carries its own body's muscles beside the organism's, is
  read like for like.

The switchboard's *Organisms* and *Runs* (section 2.31) and its organism row set the same knobs.

### 27.6 What a cell shows

The readout on the left prints the cell's word and its number with the word's sign, the gauge, the way and what it is read
against. Under it come the reading in the key's words for its run count ("in all 500 of our runs", "by the mean of our 10
runs", "in our one run") and how many runs are beyond the noise. It then gives the range the runs moved over in plain directions
("from up 2.6% to up 3.4%") and the mean as this page recomputes it. The scenario number, the organism, the cell's tier, the
injections it draws on and its reference follow. The cell's three gauges stand at the end, each with its word.

Under the readout, the strip draws each run's change against its reference as a dot. The band is the 0.5% floor. A dot is green
toward the gauge's aim, red away from it and amber for power given, by the floor alone; the dashed line is the mean. The cell's
word adds the noise: each run's 95% interval over its 24 blocks of ten decisions (Student's t), read by the key. Hover a dot for
its run, its injections and its seed.

On the right, the matrix shows every runs × organisms cell of the chosen way and gauge, each with its signal, its number and its
word. A click on a cell selects it.

### 27.7 Ways ranked, organisms on the same injections, one injection

- **Ways Ranked Against Native**: every way on this organism in this cell, ranked against native by work, then by the share over the line, with power
  beside. Its line names the first way, the rank of Omni-Compass on native, and the ranks held by the ways with Omni-Compass on
  top; the rows with Omni-Compass are drawn in its colour. A click on a way selects it. In our models a governor's knobs run
  under their own native controllers, so a governor's way reads native's work index by construction. What it moves is the share
  over the line and the power of its knobs, and its rank says so. The governors as their projects ship them, governing real
  workloads, are read on real Kubernetes in the page's section 4e (class L): fourteen named, twelve with a rig built, eleven run the four
  ways.
- **Organisms on the Same Injections**: the chosen way and cell on every organism, so each organism's reaction to the same
  injections is read side by side. A click on an organism selects it.
- **Single Injection Across Organisms**: pick k (0 to 499) with the arrows or the box. The line prints its seed and the rule
  that made it. The table gives each organism's mean over that run's 240 decisions per muscle, the reference to the way, with
  the change in plain directions.

### 27.8 Exports, import and the reference

- **This cell, every run (CSV)**: each run k, its first and last injection, its first seed and its change on the three gauges.
- **This organism, every way and cell (CSV)**: every pair, tier and gauge with its mean, word, reading, runs beyond the noise,
  smallest and largest run.
- **The batch's 500 injections (CSV)**: k and its seed.
- **The whole record (JSON)**: the record as the page holds it.

Each file opens with the notice and the batch's line (its base, the Python's and the C++ engine's digests, the engine, the
commit). **Import** reads another record of `tools/injection_grid.py` (another batch). Every view and both checks follow it,
the batch line says it is imported and not this build's record, and *Back to this build's record* returns. Every cell has a
**reference**, `IG/base/organism/way|against/NxM/gauge` (for example `IG/1488855732/tower/on_native|native/500x1/work`).
*Copy this cell's reference* copies it, and typing it in the box and pressing *Go* reaches that cell on any copy of the page that
holds the batch. Another batch is run with `python3 tools/engine_runs.py --runs 500 --base B` (the Python, then the C++ engine
on the same seeds) and `python3 tools/injection_grid.py --base B`. On GitHub, every set the engine-runs workflow commits on main
starts the injection-grid workflow (eight shards, then the record and the page's rebuild), and a dispatch runs any base.

One batch is one run in the key's sense; three batches make a three-run reading. Class S, our own models.

## 28. Whole Organism

This chapter reads the page's section 5d, **Whole Organism** (`#s-whole`).

### 28.1 Every way a stack is bought

The whole organism (the page's section 5d, `#s-whole`) opens with the same box as the clouds' section, the cloud is a wire,
and its table of the three places Omni-Compass lives (section 21.1); the three places compose into one organism and one bill
below it, read two ways, native and Omni-Compass on top of native.

Omni-Compass is wired into every piece of a stack through its own two-way plug: the
software (the cluster, its add-ons, its governors and orchestrators, and the services on it: the pools, the consumers, the
caches), the bare metal under it (the chip's power limit and clock; the machine's kernel and its own meter) and, where the stack
is rented, the cloud that bills the machines. The whole-organism monitor (the page's section 5d, `#s-whole`) has a button for each
way a stack is bought (**Scenario**): *On-Site Bare Metal*, the software on the owner's own bare metal (software × bare metal, no cloud);
*Through the Cloud*, the cloud's build, its bare metal at the back end and the software (cloud × bare metal × software), with
the cloud as two pieces beside it; *In the Device*, the bare metal alone, for one who buys the chip or the machine and no
software stack on it; and *As a Service*, the software alone, for one who runs it on machines someone else meters. The cloud is a
piece of the stack, bought and billed, and what Omni-Compass does there composes with what it does on every piece beneath it.

A tenant cannot meter the provider's bare metal at the back of a cloud: the cloud's piece is the bill and the machines the
provider meters, and the bare-metal piece is gauged on hardware the repository meters and carried to the provider's only as a
modelled factor, said so on the monitor in the box **CLOUD BACK-END METERING DISCLOSURE** (`DISCLOSURES.md`, section 9). A piece with no measured run yet is named and left out
of the whole, never filled with a guess.

### 28.2 Stack Composition

The stack, native beside Omni-Compass, with the work flowing down through the pieces: the service,
the cluster, the governors, the machines, the chip, and, through the cloud, the provider's bill. The dots move at the live
engine's demand; the picture is of the flow, not a measurement; each piece's measured factor replaces the picture's weight
the moment its three runs land.

### 28.3 Composed Benefit by Gauge

The benefits, gauge by gauge, added together over every measured piece: work (more), speed (a
shorter 95th percentile), machines (fewer), energy (less), the bill (smaller), and the one number, the index over the gauges.
Two readings are offered by the buttons (**Reading**): *Every Piece, Intervals Carried* (every factor with its own 95%
interval, the whole their product) and *Strict Reading, Index Rule* (only a factor that reads GAIN or power given in
all three of its runs counts; STEADY counts as exactly 1). A third pair of buttons, **Chip Run**, puts the chip's newest
finished run *Beside the Count* or *In the Count*.

### 28.4 Composition by Piece and Layer

Piece by piece and layer by layer: each factor with its 95% interval, the whole their product. Read
the table left to right: the piece and its layer, the five gauges, the index, and the receipt (the table's own row) each factor
is read from. A factor's interval that includes 1 is STEADY and multiplies the whole by exactly 1 in the strict reading.

### 28.5 Bills and Receipts

What native spent (the cost; runs A, B and C), what Omni-Compass spent (the expense; A, B and
C), and the benefit (pooled, with its 95% interval), in the units each receipt bills in: machine-hours, dollars at list price,
watt-hours of the declared model, the meter's watt-hours where a meter exists. The cost is native's, the expense is
Omni-Compass's, and the benefit is their difference read by the key: a smaller bill is GAIN, a larger one is power given,
shown beside the work it bought.

### 28.6 Tables Outside the Count

The governors' tables on this page, the models beside them, the separability test (whether the
pieces' factors may be multiplied: the factors are independent where each piece's run holds every other piece at native), and
where the missing pieces are: every slot not yet measured is named, and the whole is read without it rather than with a guess
in its place.

## 29. Measured Effect

This chapter reads the page's section 5e, **Measured Effect** (`#s-fleet`).

### 29.1 What it holds

The measured effect in full (the page's section 5e, `#s-fleet`) is everything the benefit board stands on, from the organisms down to the single muscle: the
seven organisms under their three loads, all 1,107 muscles of the catalog one cell each, every registered benchmark still to run,
the scale-out grid of copies and runs, and every three-run table in the repository with every row as it is written. Its first
monitor, *Seven Organisms Under Three Loads · Class S*, draws the seven organisms of the catalog under three loads (the spine first; the four realms; the four stacked; the whole
tower), each native and with Omni-Compass on top, misses against native; the whole stack's two arms are the whole organism's
composition (chapter 28) until the stacked run measures them in one run. Its second, *Catalog Muscle Matrix · Class S*, draws every muscle of the catalog as one
matrix, each cell its word against native; click a cell to read the muscle (its name, family, realm, template, knob and its word
under each load).

### 29.2 Open Register Slots

The register's slots, in order (`docs/REGISTER.md`): every muscle in
them already runs, modelled, in the 1,107-muscle catalog and the seven organisms, native and with Omni-Compass on top; a slot is
the same test on the outside world's own software, each queued until its three runs land. A slot shows its status in the
register's own words, what is measured (the lines of its preregistration) and the known limits said before the result.

### 29.3 Scale-Out Grid

Seven organisms × 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs: modelled (**Misses · Class S**)
and with the real cluster inside (**95th Percentile · Class L Inside the Model**), both values shown in every square. The 1,000 tier runs on GitHub's free
runners only; paid machines stay at 100. Two buttons choose *the engine that stands: its runs as they land* or *the road: the
newest grid with its squares landed*. A square not yet landed says so; a square beyond a free runner's memory or time is listed
as pending runner capacity, never rented. The grid's monitor draws the engine that stands' own campaign as GitHub runs it: each
square filled by its runs started (pale) and measured (solid), as GitHub was read at the build, with the age of that reading in
its heading; the reading cursor walks every started square and names it under the grid. Once the grid's receipt is written, each
square takes its word. The road draws the newest grid with its squares landed, under its own engine's name, never read across.

### 29.4 Standing Three-Run Tables

Every three-run table in the repository, native against Omni-Compass, every row as written,
each benchmark's newest engine's table; open a row to read every judged row that is not STEADY. The table's own rule is printed
with it; rows shown and not judged are left out of the counts; a tuning case is shown and never counted.

### 29.5 Realms Table

From `results/realms_v5/REALMS_V5.json`, the realms runner at the max, its
engine and commit named above it (`tools/run_realms_v5.py`, catalog `realms/catalog_v5.csv`), ten paired seeds per muscle and
per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A
muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none
moving the other way; STEADY at its limit on native when its knob already sits at the top of its range; STEADY, the same as
native, when it wrote and nothing moved beyond the noise. Energy is power given where it rose. The seven organisms are listed
spine first, then the four realms, the four stacked and the whole tower, each under its own load, the climb and the work
waiting in line (the three buttons). Evidence class S: a model's energy is not a meter's.

### 29.6 Families by Stack

Each muscle alone, native and then with Omni-Compass on top, grouped by the family of its
knob and the stack it lives on; *Find a muscle* searches the 1,107 by name. A family reads GAIN when more of its rows read
GAIN than LOSS; the row of a muscle at its limit on native is counted as STEADY.

## 30. Telemetry Analytics

This chapter reads the page's section 5f, **Telemetry Analytics** (`#s-lab`).

### 30.1 Telemetry Tensor Cube

The engine's own record is a tensor: two sides × every decision × sixty muscles,
each entry a muscle's compass position (0 calm, 0.5 the center of its band, 1 its line), recorded from `realms/harness.py`
(class S). It fills in decision by decision as the page's section 3a plays: the tensor, the difference matrix and the principal
motions replay that record on the live benchmark engine's clock, and no knob of the console changes them. Read it as a sheet of heat: a column (one decision) that is
light on the blue side and dark on the orange side is a body Omni-Compass held nearer calm at that moment.

### 30.2 Tensor Difference Matrix and Principal Modes

The difference between the sides, muscle by decision, with the
sign of the word; and the body's principal motions, the tensor's eigen-decomposition: the few patterns of movement that
account for most of the body's motion, each with the share of the variance it carries. The line across each bar is the
decision on screen: the share of that decision's own departure from the run's mean that lies in the mode. A first motion that is the whole body
rising and falling together is a body breathing with its demand; a motion that is one room against the rest is that room's
inflammation.

### 30.3 Service Level and Error Budget

The official runs (class L) read as a site-reliability engineer reads a
service: the service level this repetition, the error budget burned, and every gauge of this repetition against native, each
replaying the official run chosen in the page's section 4a (**Service Level and Error Budget**, then
**Repetition Gauges Against Native**).

### 30.4 Omni-Compass Narration

Omni-Compass speaks for itself: every line is read from its own records at the moment
on screen (the official run playing in the page's section 4a, its governor's own audit, and the engine's harness on the console's clock)
and says what it is doing, beside what native does. *Speak aloud* reads it out on the viewer's own browser voice as the run
plays.

### 30.5 Ask Omni-Compass

Ask in your own words, or pick a question (what are you doing right now; where do you read LOSS,
and why; explain yourself to a buyer; show me your largest GAIN). Omni-Compass answers in the first person, for its own
mechanism and its own runs, reading only this page's records through six tools. The words are composed for it by Claude on
claude.ai, on the viewer's own account and with the viewer's permission; opened anywhere else, the rest of the page runs
whole without it. The answers are drawn from the page's records and are not reviewed by any outside party.

## 31. Master Switch Wiring

This chapter reads the page's section 5g, **Master Switch Wiring** (`#s-master`).

### 31.1 One switch for the whole organism

The master switch (the page's section 5g, `#s-master`; its kill switch heads the page's section 1) is wired at the top of the
organism (the monitor *Master Switch and Kill Switch*): switch, brain, organism, every muscle, as the repository builds it (`omnicompass/master.py`,
`tools/omni_switch.py`). It holds the brain's outputs. Every governor on the page is registered with it and obeys it at once;
on a real machine every governor exits at the switch.

### 31.2 The table under the switch

The table's columns: the governor; where it lives (the module, the section); its state;
what it does at the switch. Every governor the page runs (the stress-test model's, the harness's, the live controller's replay, the page's
own render governor) is a row, so there is no governor on the page that the switch does not reach.

![State machine: the governor's modes. OFF is native alone; WATCHING reads and logs and writes nothing; AUTOPILOT pushes, lifts off and idles; CRUISE holds every machine in service while a known queue waits; RESET hands every setting back and reads it back. The kill switch leaves every mode for OFF at once; the lease walks a crashed governor's settings back to native. On the page the switch's three states are ON (green), the kill switch engaged (red) and OFF (white, the brain reading in shadow).](book/figures/g_modes.svg)

## 32. Specification and Mathematics

This chapter reads the page's section 5h, **Specification and Mathematics** (`#s-math`).

### 32.1 Every part and its equation

The component specification: every part of the engine, its
equation in Unicode as the repository writes it, and the source module that implements it. Items 1 to 5 and 8 are the engine's
code and run in every view; items 6 and 7 as written (the compass law on each muscle, the plug's lever) drive the stress-test
model; in the harness views the max and the plants' own overrides take their place; the live controller runs the compass law
on the service, as the page's section 4c shows.

| Item | Part | What the page prints | Module |
|---|---|---|---|
| 1 | Senses | the muscles' meters read and normalised to nine observations: q, load, power, thermal, network, drift, stale, security, conflict | `adapter.observe_vector` |
| 2 | Assimilate | x ← (1 − a)·x + a·x[obs], a = 0.339: the engine is pulled toward what the senses read | `adapter.assimilate` |
| 3 | Evolve | equations (1) to (7), the Runge–Kutta method, ten micro steps of 0.01, the controller evaluated and not applied | `core.macro_step` |
| 4 | Allocate | push = clip(−f[U] + 12·(1 − U), ±25)/25 and ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρₘᵢₙ, ρ₀) | `adapter.Governor.step` |
| 5 | Nerves | κ, h, σ, ν into calm; calm against each organ's θ grants contraction (the spine to nodes, θ 0.7; compute to pods, 0.5; physics to the processor's clock, 0.3; energy to power, 0.3; distribution to routing, 0.5) | `nervous_system` |
| 6 | Compass | p = (r − lo)/(hi − lo); F = A·tanh((kₚ(p − ½) + k[d]·v)/A); fails up past 0.95; never hands back while climbing above the center; k[d] at three times critical damping from the muscle's own τ, the push | `compass_law.CompassLaw` |
| 7 | Plug | one wire in, one wire out: each write clipped to the cover; the snapshot taken once at the start is what reset restores; each write read back; the kill switch hands every lever to native at once | `compass_law.Plug`, `master.py` |
| 8 | Verdict | the paired trial of chapter 16 | `verdict.py` (its C++ twin `cpp/src/verdict.cpp`, chapter 26) |
| 9 | The whole organism | each layer measured against its own native, the layers composed by the product law with every interval carried in logarithms, two readings of the same numbers, the separability assumption tested on the governors' four ways | `tools/whole_system.py`, `docs/engine/export_whole.py` |

### 32.2 What the specification is for

It lets the reader of the page check that what moves on the monitors is what the
code says: the six spokes at the center of the cycle (E, U, I[U], S, B, Ḃ) are item 3's state, the inner arc of nine segments
is item 1's senses, the force field of the phase plane is item 6's law. The Owner's Manual carries the derivations; this page
carries the statements.

### 32.3 Stress-Test Model and Reads and Sets by Part

Under the specification, **Stress-Test Model · Class S** writes out the model drawn for the page: one decision of muscle i in the order
it runs (capacity following its lever with its response τ; the work served, the waiting work and the failed work; the reading,
read one to three decisions late; native's rule; the compass position and force; the max and the tune-down; the plug; the kill
switch), with both arms on the same demand. A table, **Reads and Sets by Part**, names every part, what it reads, what it sets and its
source: native's controller under each muscle, the max of the harness, the brain, the nerves, the immune system, the compass law,
the release gate, the plug and the verdict. Two notes close the section: **Engine Code Provenance** (what is the engine's code,
ported, and checked against the Python and the C++ on every build) and **Realms Harness and Stress-Test Model**, the two bodies.

## 33. Failure Modes and Controls

This chapter reads the page's section 5i, **Failure Modes and Controls** (`#s-fail`).

### 33.1 Failure-Mode Register

Every known way Omni-Compass can fall short, the control that mitigates it,
that control's coverage and the residual risk where it does not reach, and its implementation in the code; every failure mode
the live benchmark engine can be put through has a fault-injection control on the console, named in the row. The register is
`docs/SAFETY_CASE.md` and `docs/THREAT_MODEL.md` read as a table.

### 33.2 Unjudged Resource Costs

Under the register, the rows the three-run tables report but do not judge:
the governor's own commands, its processor time, the pending pods in a snapshot, the energy per core-hour. They are printed so
the cost of the governor is never hidden; they carry no word because their preregistrations declared them shown only.

## 34. Self-Governed Rendering

This chapter reads the page's section 5j, **Self-Governed Rendering** (`#s-self`).

### 34.1 Omni-Compass inside the page

The engine that runs the page has Omni-Compass in it. Native
is the browser's own loop: every chart on screen drawn on every frame, and when the frame overruns, whole frames dropped.
Omni-Compass is the same loop with the engine's own compass law governing it. Each chart is a muscle whose knob is how many
frames it waits between draws, and the reading is the time between frames. Below the band's center the pedal lifts and every
chart is handed back to native, drawn every frame. Toward the line it pushes: the charts farthest from where you are looking
wait a frame or more, so the frame itself stays inside its line. Evidence class L: live software, on the viewer's own machine.

### 34.2 Reading it

The monitor, *Inter-Frame Interval by Window*, shows the frame time on both sides, the frames dropped by
native's loop, and the frames waited by each chart under Omni-Compass; the table **Paired Window Measurement** pairs the two sides
window by window. On a laptop with the wall in view, the charts on screen draw every frame and the
rest wait; scroll, and the waiting moves with the eye. The kill switch on the console reaches this governor too: engage it and
the page draws as the browser alone would.

---

# PART VI. THE PAGE'S APPENDIXES

## 35. Title Page and Build

This chapter reads the page's appendix A, **Title Page and Build** (`#title-page`).

### 35.1 The title page

The title page (the page's appendix A, `#title-page`) carries the build: the engine that stands and its digest, the commit and the
time the repository built the page, the evidence classes (P a meter, L live software, S our models, each marked), the arms
("native · Omni-Compass and native, never Omni-Compass by itself"), and a line that names the engine every table's runs ran on and
how many benchmarks are being run again on the engine that stands (`#bEngRuns`). Its opening paragraph says the same in full: two
sides everywhere, and only two, native and Omni-Compass and native; Omni-Compass is never by itself, it always sits on top of a
native controller; what omni-v18 and omni-v19 added to run it otherwise is still in the engine
and is not shown on the page. Under the build lines stand **Product Scope**, the **Colour Key** and,
folded, **Coverage, Signals and Result Words** (**Benchmark Coverage**, **Live Signals on the Band**, **Result Words**); its last
line points to the two disclosures that head the page's appendix G (chapter 41): this page is a live tuning engine, and the
benchmarks are one tuned engine; and real runs, a real engine, nothing hardwired. Where the records stand on a newer engine
than the page's words were written for, a banner under the wall says so and says to read the newer engine wherever a sentence names the older one as the engine that
stands.

Beside the title, on a desktop, stand the owner's two illustrations, one above the other (on a phone they sit under the
title): the stacks Omni-Compass sits on top of as he pictures them, and under it the Omni-Compass as the unified control
authority. Each says under it that it is an illustration, not a result, and the first says that the product names and marks in
it belong to their owners, with no partnership, sponsorship or endorsement stated or implied. The engine draws over them: a
ring at every decision of the live benchmark engine; on the rose two hands, native's (orange, the longer) and Omni-Compass's (blue), each
at the mean place of that side's muscles in their bands, calm at north and the line at south; on the control core a glow that
grows with the settings Omni-Compass wrote in that decision; and under each, that decision's counts. The marks are the engine's
state (the page's section 3a), never a number of the picture's own.

### 35.2 What the page is

The live benchmark engine is a monitor of the Omni-Compass engine and of the benchmark runs GitHub ran. A
monitor shows what its instrument reads; a drawing shows what its author believes. The page is the former by construction:
every record it replays is made again by the repository's own code on the checkout it is built from, and `--check` fails a
page whose engine is not the one `python3 tools/omni_version.py` reads. So the page never runs ahead of the repository: when
a new engine stands, the build stamps it on the page and rebuilds every record on it, and the page says in a banner that its
prose was written for the older engine until a person realigns the words.

It is also a live tuning engine, a tuning bench. Its buttons turn the engine's knobs in real time: the heartbeat (six buttons in the control panel, from 10
to 120 s), the dial between the max and the tune-down, the pedal, each muscle driven or left native, up or down, in or out, minus or
plus. Turning them shows the mechanism of action and its variations with native alone, with Omni-Compass on top of native, or
both side by side. As on any engine, where the mixture, the intake, the exhaust, the firing or the pistons change what a car's
engine delivers, **turning any knob of Omni-Compass can change every metric, up or down, in any direction a tuner chooses**: one
engine for many vessels, tuned many ways, for many outputs. The records the page replays are something else: the main engine's
one tune, the factory tune (its factory profile), as the benchmarks ran it. That tune is chosen by a declared rule: of the tunes that harm no gauge
against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on
development seeds and read again on untouched ones (`docs/THE_TUNE.md`). What the page shows at any other setting demonstrates
the engine's range and is never a benchmark result; a tune other than the factory tune belongs to its tuner, and so do its
results. The box that opens the page's appendix G says which is which (`#tuningBench`). The beat on the dial (the page's section 3d)
is one such knob: the factory profile runs it at 60 s, and every other beat is shown beside native with what it buys and what it
costs, as range, never as a result. Each muscle's own setting is part of the same factory profile: its card where one was found
under the same rule, the engine's setting for the rest (`realms/muscle_cards_v5.csv`).

In the words of `docs/FACTORY_PROFILE.md`, the page is the **live tuning bench**: the interface that operates the engine's
controls and displays their effects through the connected backend. The **factory profile** is the complete, versioned set of
Omni-Compass default settings shipped together; on the engine that stands it is omni-v22's (`OMNI_V22.json`): the governor's
full decision every 60 s, the fast checks every 5 s, every muscle on the card found for it and on the engine's own setting
otherwise. The **active profile** is the settings actually governing the current run. An adjustment on the bench produces an
identifiable active configuration, a **custom profile**; it becomes a new factory profile only after validation and a new
release declaration. The control panel shows which profile is active and its fingerprint (section 2.7).

### 35.3 The five records

The page carries five kinds of record, and every monitor says which it plays.

| Record | Made by | What it holds | Class |
|---|---|---|---|
| The harness | `docs/engine/export_harness_trace.py` | the realms harness (`realms/harness.py`, the max of `realms/compass_arm_v5.py` with the bone, the twins and the immune system): one organism of sixty muscles, and each muscle alone, native and with Omni-Compass on top, decision by decision | S |
| The controller | `docs/engine/export_controller_trace.py` | the shipped Kubernetes governor (`omni_controller/controller.py`) on the modelled cluster, on top of the autoscaler at the max and in the cloud's setting, every tick and every audited decision, runs A, B and C of six hours | S |
| The runs | `docs/engine/export_runs.py` | the official runs as recorded: every three-run table's runs A, B and C read back from their raw files, every file's SHA-256 matched against the run's own list, every Kubernetes repetition scored by `tools/live_reps.py` and checked against the run's result | L |
| The scenarios | `docs/engine/export_scenarios.py` | the GPU card (`realms/gpu_card.py`), the Linux host (the conveyance of `tools/model_gate.py`), every muscle and organism of the realms table (`results/realms_v5`), and every judged row of the newest receipts (`results/live/`) | S, with the receipts' own classes |
| The build | `docs/engine/build_live_engine.py` | the engine, its digest and the commit; the time; GitHub's runs in progress and queued; every run started for the chips and the clouds (`docs/engine/github_ledger.json`) | the record of the build |

Beside them the page embeds the records its newer sections read, each named where it is used: the real three-run test of
Omni-Compass on native against native (the scorecard and the benefit against native, chapters 4 and 5), the twenty scenarios (`results/scenarios/SCENARIOS_20.json`,
chapter 27),
the whole organism's composition (written by `tools/whole_system.py`, chapter 28) and the glossary (`docs/engine/glossary.json`,
chapter 40).

### 35.4 What runs live

Three parts of the governing engine run in the page itself: the brain (`omnicompass/core.py`), the compass law
(`omnicompass/compass_law.py`) and the verdict (`omnicompass/verdict.py`), each ported to the browser and proven equal to the
Python and the C++ on every build by `docs/engine/check_live_engine.py`. They drive the stress-test model of sixty muscles
(the page's sections 3a, 3c, 3e to 3g) and the page's own render loop (the page's section 5j); the page's own runs of the
Python's seeded runs and of the core's Monte Carlo (chapter 25) run the same ported code. Every other monitor plays a record.

### 35.5 What the page decides

Nothing. Every word on it is the reading its record carries under the one key
(`tools/readings.py`), applied once, in the repository, when the table was written. The page never reads a word off the stream
it draws. When a monitor has no record yet (a cloud set still running, a chip run not yet started), it says what the
repository holds and shows nothing in its place: the empty slot is itself a true reading of the record.

### 35.6 The appraisal

Every view of the page is reproduced from the repository's own code by an independent path and
compared value by value (`docs/engine/APPRAISAL.md`; rerun with `docs/engine/check_live_engine.py` and
`docs/engine/check_records.py`). The brain's mathematics agree to machine precision; the harness views and the live controller
are identical to the repository's own runs on every tick and every plant. Chapter 47 says how to rerun the appraisal on your
copy.

## 36. Reading Guide

This chapter reads the page's appendix B, **Reading Guide** (`#s-guide`).

### 36.1 What the guide holds

The page keeps the explanations of its sections in one place, its appendix B, the reading guide (`#s-guide`), so that every
section opens on its monitors and controls. Each section's introduction stands there under the section's number and title, in
the page's order: 0 Monitor Wall, 1 Control Panel, then 2a to 5j. It opens with the **Monitor Wall Legend** (each monitor's
signal and word, what the control panel holds, the five blocks, how a tile is drawn) and the **Organism Ring Guide** (two arms,
one demand; what a dot's position means; the engine's code behind the default body). Under *0 Monitor Wall* it sets out the
light count, the redline reflex and every light's meaning; under *1 Control Panel*, the fuse box and its seven tabs, the
mechanism knobs and the manuals; under each lettered section, what that section shows and where it stands in the record. The
legend's rules are read in the sections that follow: the sides, the words, the 0.5% rule, the signal words and their shapes, and
the marks.

### 36.2 The sides

There are two sides, and only two: native and Omni-Compass on top of native. Omni-Compass is never by itself: it always sits on top
of a native controller. Native is orange (`--steel`, #ff8a1f) and Omni-Compass blue,
everywhere: every line, bar, tile and number that belongs to one side wears that side's colour, in every chart and table, and
the word "native" itself is orange. Red is never a side; it is only LOSS and the alarm. Violet (`--tuned`) is never a side
either: it marks only a knob or a profile turned from the factory tune (sections 2.7 and 2.12). Where a monitor draws the two
sides on one axis, native is the left lane or the upper row; where it draws them as two instances (the organism, the phase
plane), native is on the left. With the master switch OFF, every Omni-Compass side is drawn in a lighter tint of native's
colour, dashed, so both stay in view.

### 36.3 The words

GAIN is green, STEADY is yellow, LOSS is red. Every reading, in every table, chart, bar and tile, wears one of those three
colours, or blue for power given, and no other. Power given wears blue, Omni-Compass's own colour, because it is what
Omni-Compass put in. A LOSS word is printed white on red in the shape of a stop sign. *The runs disagree* and *the runs differ*
are white with a dashed edge, and *shown, not judged* is grey, because none of them is a reading. The size printed beside a word
is how far the gauge moved from native and carries the word's own sign (GAIN +, LOSS −, STEADY =), never the gauge's raw
direction.

### 36.4 The 0.5% rule

The page reads every change by the key's one floor, half of one percent (`tools/readings.py`). A three-run reading follows
`three_run_reading`: the change is the mean of the three runs' changes, each in percent of native; a mean of 0.5% or more reads
GAIN, LOSS or power given by the gauge's aim, "in all three of our runs" when every run moved the same way clear of zero, and
otherwise "by the mean of our three runs" with the count of runs beyond the noise; a mean under 0.5% reads STEADY, under the floor;
runs that moved 0.5% or more in opposite directions disagree. The same rule reads the sweep's three model days (section 2.6) and
the three-run column of the page's scoreboards. One run's reading, on the scoreboard and on the control-loop table, is under
0.5% either way STEADY and from 0.5% up the word, whatever the interval says. The lights that compare the two sides at one moment
read STEADY only inside ±0.5% of native's value; where a light counts (the muscles over their line, the pods waiting), a
difference of one is a change. Two values that print the same are never told apart: they read STEADY.

### 36.5 The signal words and their shapes

Every monitor, every section heading and part title whose section holds a monitor, every breaker of the fuse box, the
wall's tiles, the scorecard's rows, the twenty scenarios' cells and the dock carry a signal and its word, read on the band:

| Signal | Shape | Word | What it means on the page |
|---|---|---|---|
| green | round | GAINING | low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN) |
| yellow | a yield diamond | STEADY | inside its band, or level with native (a change under 0.5%) |
| red | an octagon, a stop sign, blinking red and black | REDLINING | at the top of its band and holding there, or Omni-Compass behind native now (a LOSS) |
| red | an octagon, blinking red and white | OVER THE LINE | past the top of its band: the alarm |
| dark | no lamp lit | AWAITING | the run that fills this monitor has not landed yet; its light stays dark until it does, never green |
| grey | no lamp lit | NO LINE | a monitor with no line to cross (a bill, a count of runs, a digest check) or no reading yet; never counted green |

These four live words belong to the moving monitors. A result fixed after the fact, in a table, reads GAIN, STEADY or LOSS (with
power given for a resource spent that rose): GAINING and GAIN go together, STEADY and STEADY, REDLINING and LOSS.

Every signal shows all four live words at once, the lit one bright and the rest dim, on native's side and on Omni-Compass's side
alike; a monitor that draws both sides carries a full signal for each, with the result now against native (GAIN, STEADY, LOSS)
beside them. Omni-Compass's redline reflex is built never to let a muscle redline: at the top of a muscle's band it pushes at once,
before the line. Where a muscle stays over its line three decisions in a row and is stuck (at its own limit, or not relieved by 5%
of where the redline began) and native's own twin reads lower by more than 5%, it hands the muscle back to native for 10 decisions,
the hold doubling for each hand-back in a row up to 160; it takes the muscle back only when its side is under the line and lower
than native's by 5%. Where native is not stronger it stays, because redlining less than native is still a benefit against native.
The red is still wired on its side, so that if a muscle does redline there (a fault, a bug), it is seen at once. That is the kill
switch's purpose: when something redlines that Omni-Compass itself cannot stop, one press hands every muscle back to native in the
same instant. The engine that stands, omni-v22, carries this rule in its immune system, knob by knob (`omnicompass/immune.py`, its
C++ twin `cpp/src/immune.cpp`, proven alike on 200 seeded scripts, and the nervous system's `native_hold`; on Kubernetes each
service's autoscaler target, native's twin the operator's own target), beside the SLO reflex and the pod reflex of the Kubernetes
governor (`omni_controller/controller.py`); the page's live model (class S) applies the same rule, with the engine's own numbers, to
every muscle it draws.

Each light reads what its gauge is for, never the direction of its needle: a wait that falls is GAINING, work that falls is not.

The number of every monitor carries the colour key: Omni-Compass blue behind the number of a monitor that shows Omni-Compass on top
of native, native orange behind one that shows native alone, both (orange first) behind one that shows the two side by side, with
black type. The key is fixed: no switch recolours it.

The signal stands as a traffic signal does, red on top, yellow in the middle, green at the bottom, one lamp lit. Red appears only
in a stop sign's shape: a red light is an octagon, a red word (REDLINING, LOSS) is a stop sign's shape printed white on red, and
on the canvases any whole circle drawn in red is drawn as an octagon. A section's or a part's signal shows the worst of its
monitors' lights (red over yellow over green; AWAITING only where every monitor awaits); hovering it gives the count of each.

### 36.6 The sides are never a reading

Blue does not mean good and orange does not mean bad: they name who is being read.
Where the two sides look the same, they are the same, and that is STEADY. Where Omni-Compass's blue line sits closer to a
muscle's line than native's orange one, that is the max at work: every muscle to its own limit, never past it, and the
capacity it holds there is power given, shown beside the work and the speed it bought.

### 36.7 The marks

A kill-switch window is shaded red across every time axis. A monitor on screen now carries an accent
border on its tile. A tile with no reading says what it shows (a count, a state, an age) and carries no colour of a word. A
row shown and not judged (the knob's own setting, the governor's own commands, Omni-Compass's own processor time) is grey and
counted in no total. A ring that opens and fades at the head of a line is the decision that has just landed on it, and the small
box beside the head prints that line's newest value, as a quote board prints the last price. A box drawn round a row, a cell or a
bar of a record monitor is its reading cursor: it walks the record one row for each decision of the live benchmark engine, and the row it
holds is named under the monitor; the record itself changes only when GitHub's next run rebuilds the page. An age printed
beside a reading of GitHub ("read 06:16 UTC, 41 min 07 s ago") counts up every second.

## 37. Problem and Answer

This chapter reads the page's appendix C, **Problem and Answer** (`#s-problem`).

### 37.1 What it holds

The problem and the answer (the page's appendix C, `#s-problem`) prints in one paragraph what every stack faces, what Omni-Compass does about it, where the
proof is, what is not claimed and what is protected, and unfolds (**Problem, Answer, Proof, Limits and Protection**) into the
whole section: **Industry Problem**, with its outside sources named and quoted only for scale; **Omni-Compass Answer**; **Costs
and Responses**, how it addresses each cost and how each is judged; where the page shows each answer; what it does not do; and how it is held to account. This
book carries the same matter in its front matter, "The Problem and the Answer".

## 38. Executive Summary and Reading Key

This chapter reads the page's appendix D, **Executive Summary and Reading Key** (`#s-read`).

### 38.1 What it holds

The executive summary and reading key (the page's appendix D, `#s-read`) opens with the Omni index, every real test weighed together, and one paragraph on the two
sides, the three words and the three classes of evidence, and unfolds (**Summary, Key, Terms and Examples**) into the **Executive
Summary** (every number read from the records on the page when it opens), the **Reading Key** (GAIN, STEADY, LOSS and power given,
the colours, **Size, Sign and Raw Change**, and **Sign and the Gauge's Aim**: why a minus can be a GAIN and a plus a LOSS) and the terms the page uses, each defined once and shown when pointed at. This book
carries the key in its front matter, word for word as `tools/readings.py` writes it.

## 39. Monitor List

This chapter reads the page's appendix E, **Monitor List** (`#s-monlist`).

### 39.1 Every monitor by its number

The monitor list (the page's appendix E, `#s-monlist`) is the list that goes with the wall, **Monitors by Number**: every monitor by its number, in the same order, with
what it shows, its section, its layer, its evidence class and state (live, replay, record, model or awaiting its run), the
open-source exporter and series that would carry it on a running system, its knobs, its wiring (the page's code, the Python, the
C++ and the checks that hold them equal) and the motion meter's reading, and, where it waits, the run that fills it. Click a
number to go to its monitor, a section to go to its section. The feeds name the open-source exporters an operator's Prometheus
and Grafana already run (node_exporter, kube-state-metrics, the NVIDIA DCGM exporter, Kepler, OpenCost, the governor's own
`tools/omni_exporter.py`); the button in the control panel downloads the whole wall as a Grafana dashboard on those series
(`deploy/grafana/omni-compass-wall.json`, written from `docs/engine/monitors.json`), beside the governor's own screen
(`deploy/grafana/omni-compass.json`). A monitor the page draws from the repository's tables, or from its own clock, says so: no
series carries it.

## 40. The Glossary and Index

This chapter reads the page's appendix F, **Glossary and Index** (`#s-glossary`).

### 40.1 The four tabs

The glossary and index (the page's appendix F, `#s-glossary`) says what every word on the page means, written from the repository's own pages (each
definition names its source file and quotes it), the organisms by their realms and families, and every muscle of the catalog
(`realms/catalog_v5.csv`) with the organisms it sits in; the index sends each term to the sections where it is used. It is built
by `tools/live_glossary.py` into `docs/engine/glossary.json`, and a term whose source no longer says what it is cited for stops
the build. Four tabs open its four parts:

- **Terms**: every term with its group, its definition, its other spellings, the sections that use it, and its source with the
  quoted words; letters A to Z jump through them.
- **Organisms and Scenarios**: the ten organisms and the twenty scenarios, each organism with its muscles, its class, its meaning, its families, its
  governors where it has them, and its two scenarios, each with its signal word and number from the twenty scenarios' record
  (click one for its gauges and its three runs, chapter 27). The two arms are named in their colours: native orange,
  Omni-Compass on native blue.
- **Muscles by Realm and Family**: every one of the catalog's 1,107 muscles once, the spine first and then each realm's own
  muscles, by family; open a family for its wiring (who runs it natively, what Omni-Compass reads and writes, how it is
  restored) and its muscles, each with its id, its name, what it is, what the max does with it, its card and the organisms it
  sits in.
- **Index**: every term, organism and arm, and the sections of the page that print it, in the page's own numbering.

### 40.2 How to find a thing

Type in the search box: the glossary answers with every term, organism and muscle whose words match, the muscles capped at the
first 200 with the rest named by count. Click a letter to jump among the terms, a realm among the muscles, and an index entry to
its definition. This book's own glossary stands in its back matter; where the two differ in wording, each names its source.

## 41. Disclosures, Law and Contact

This chapter reads the page's appendix G, **Disclosures, Law and Contact** (`#s-disclose`).

### 41.1 What the section holds

The page closes on its appendix G, **Disclosures, Law and Contact** (`#s-disclose`), before the closing legal
notice (`#notice-end`). It opens with the live tuning engine box (`#tuningBench`): **THIS PAGE IS A LIVE TUNING ENGINE. THE
BENCHMARKS ARE ONE TUNED ENGINE.** Every knob, button and monitor on the page can be turned in real time (the heartbeat at 10, 15,
30, 60, 90 or 120 s, the dial between the max and the tune-down, the pedal, each muscle driven or left native), and turning any
knob can change every metric, either way; what the page shows at any setting other than the factory tune demonstrates that range
and is never a benchmark result. Every benchmark result is one engine at its one factory tune, chosen by the declared rule of
`docs/THE_TUNE.md`; a tune other than the factory tune is the tuner's own, and its results are its own. No profile on the page is
locked as the baseline (`docs/FACTORY_PROFILE.md`).

### 41.2 The disclosures under it

Under the box stand the disclosure of real runs (**REAL RUNS, A REAL ENGINE, NOTHING HARDWIRED**: every run played
back is read from the raw files of runs executed on GitHub's own machines, each file checked against its run's SHA-256 list before
a number is drawn; every model view runs the engine's own code, checked against the Python and the C++ on every build), the cloud's
back end (a tenant cannot meter a provider's machines), the road to the engine that stands (**Engine Lineage**), what the page is
(**Page Scope**), do no harm in its one meaning as `DISCLOSURES.md`, section 3, writes it, the governing law, and the company's
contact lines. The legal notice opens the page in its banner and closes it under this section; chapter 46 gives the license's
terms.

---

# PART VII. READING A RESULT OFF THE PAGE

## 42. The Mechanism of Action, Side by Side

### 42.1 What native does

Each native controller reads one reading, its own muscle's, one to three decisions late (the pod
autoscaler one sync every 15 s), and moves its one setting toward the middle of its range, because protecting its one thing is
its whole job. It has no heart (nothing proves it is still there), no brain (no state, no memory of need, no stress, no tide),
and no nerves (nothing grants or refuses it, and a blind sense or a security hold changes nothing it does). Its moves are the
second ticker of the page's section 4a and the orange panel of the page's section 3g.

### 42.2 What Omni-Compass does, on top

Once every decision it reads the whole body through the plug (the senses), places
every reading in its band, lets the brain's state evolve, grants or refuses through the nerves, applies the compass law to each
muscle (push toward more as the reading climbs, lift toward native as it falls, smooth, never hammering), runs the verdict's
trial on any step past native, passes the release gate, writes through the plug and reads it back, and renews its lease. Every
one of those is a column of the audit, a line of the first ticker and a box of the cycle monitor. The native controllers keep
running underneath, untouched; Omni-Compass moves only the settings they already expose.

![Block diagram: the compass control loop. The muscle's reading comes in on the sense terminal, is placed in its band, and the compass law computes a force; the force is a setting written out on the motor terminal, inside the knob's cover, through the plug, and read back; the native controller sits inside the loop, still reading its own gauge and still moving its own setting; the kill switch opens the motor terminal and the lease restores the snapshot. On the page the two tickers show the two loops, native's own and the governor's on top of it, at the same seconds.](book/figures/c_compass_loop.svg)

### 42.3 Where to see the difference

On the official run playback (chapter 18): the first ticker shows the pedal pushed at
the compass position's first move off the center and the machines recommended before native's first late sample; the second
ticker shows native's autoscaler adding replicas a sync or two later. On the phase plane (chapter 14): the blue dots turn back
before the right edge where the orange ones cross it. On the scoreboard: the work waiting lower, the decisions past their line
fewer, the capacity held higher during the climb (power given) and eased back after it (the lift). On the brain (chapter 15):
calm falling under a surge and the grant refused until the line is clean again, which native has no equivalent of.

### 42.4 What the difference is not

It is not a competitor's dashboard. Omni-Compass never replaces the controller it sits
on; every move native makes is still made. A monitor where the two sides are identical is a muscle Omni-Compass left native,
at its limit or with nothing to add, and that reading is STEADY and correct.

## 43. From a Tile to Its Record

### 43.1 The chain

Every number on the wall can be walked back to the file it came from.

1. **The tile** names its gauge and its word, and links to the monitor it copies.
2. **The monitor** names the benchmark, the run (A, B or C) and the repetition, or the table and the row, and the evidence
   class.
3. **The three-run table** is in `results/live/` (each named `V<n>_*.md` for the engine it ran on; each table names its engine), with
   its runs' ids and its rule printed at its head.
4. **The run's raw files** are on the `raw` branch at `results/live/raw/run-<id>/`, with `SHA256SUMS_ALL.txt`; the page
   matched every file it drew against that list. `scripts/raw_archive.sh open /run-<id>/` places them where the table names
   them.
5. **The governor's audit** is the run's `audit.jsonl`; native's own controllers' moves are its `capture.csv`.
6. **The scorer** is `tools/live_reps.py`; the page's per-repetition score equals the run's own summary over its repetitions.

### 43.2 The engine's name and the profile

Every table and every monitor names the engine it ran on; the page's title block names the engine
the page stands on (omni-v22). A table on an older engine stands only until its runs on the engine that stands land, and the
board says which it is. Nothing is read across engines. Every result the page plays ran the factory profile of the engine its
table names; the control panel names the profile governing the live model now, with its fingerprint (section 2.7), and a
candidate or custom profile there is never a result of record.

## 44. When a Tile Reads LOSS

### 44.1 The rule

Theoretically the word LOSS should never appear: the engine that stands moves a knob only where a paired
trial on the muscle itself shows the muscle never behind for it, and where it cannot bring a knob a gain, that knob stays
native. When LOSS does appear, the row stays, and the rule governs: if Omni-Compass hurts something, no mechanism of
Omni-Compass is pushed through that muscle. The cause is found in this order, our own wiring first, native's setup second, the
scoring third; the mechanism or its wiring is corrected; the test runs again on the next engine version, and the earlier
table stands as its engine's record.

### 44.2 Read the three-run reading, not the one run

A red row from one run of a table still running (the Azure steady set at 33 of up to 100 repetitions) is that run's own word for
that run and not yet a three-run reading: a three-run word needs all three runs, and it reads "in all three of our runs" only when
every run moved the same way clear of zero. Wait for the look.

### 44.3 Open the root-cause document

Where the repository has found the cause it is linked from the tile:
`docs/POD_START_WAIT.md` (a pod's start on one shared host is the test machine's own unpacking of an image, the same on
both sides at the same host load), `docs/TAIL_LATENCY.md` (where a 95th or 99th percentile reads higher, and why),
`docs/BATCH_QUEUE_PREREGISTRATION.md` amendment 11 (the conveyance on a shared host beside another workload's room, fixed in
omni-v13). A tile with a root-cause document is a known cause with its fix landed or on the next version's list.

### 44.4 Which knob, and what to turn

The LOSS row names its gauge; the governor's audit names the knob that moved in that
window and why. Three outcomes follow, and only these:

| What the audit shows | What it means | What is done |
|---|---|---|
| a knob moved and the gauge went against its aim while the muscle stayed inside its limit | the wire or the rule is wrong for this muscle | the mechanism is corrected in the model gate first, lands as the next engine version with no LOSS, and the benchmark runs again |
| a knob moved and the muscle went past its own limit, or another muscle's room was taken | a guard did not hold | the guard is corrected (as omni-v13 did for the conveyance on a shared host) and lands the same way |
| no knob moved, and the gauge still differs | the test machine, native's setup or the scoring | the rig or the scorer is fixed; a test machine's limit is never reported as Omni-Compass's result |

Nothing is ever tuned to make a row read well; no row is steered. What is held to the letter is the mechanism: the code does
what its rule says, the wire is fastened right, the harness measures as a deployment runs. On the page, each muscle of the stress-test model and of the replay carries its own switch on its card (the page's
section 3e), and the mechanism panel's last group carries the same switch for a muscle, its body part or every muscle (section
2.22): the muscles in scope handed back to native while the rest stay governed, to see their part in the result. On a real
machine the same choice is the muscle's wiring (the Operator's Manual's wiring of each muscle).

### 44.5 On your own system

The Operator's Manual's "wired right or wired wrong" (the Operator's Manual's section 4.5) and its drill book (the
Operator's Manual's chapter 28) are the procedure; `DISCLOSURES.md`, section 4, is the rule: where a result elsewhere differs from the published
record, the first presumption is the wiring, the settings or the reading, not the law.

## 45. What the Page Does Not Tell You

### 45.1 It decides nothing

The page is a monitor. Every word on it was decided in the repository when its table was
written. A reading you disagree with is taken up with the table and its runs, never with the page.

### 45.2 Class S is not proof

The harness, the shipped controller on the modelled cluster, the GPU card, the Linux host, the
realms table, the grid's modelled half and the orchestra are our own models. They show the mechanism; they do not measure a
machine. A model's energy is not a meter's. The page says the class on every view, and the manuals say it again.

### 45.3 Slots not yet run are empty on purpose

The metered chip runs, the CPU host's meter, the clouds' sets still running
and the register's third-party slots are written as the repository holds them and marked not yet run, and a monitor whose run
has not landed reads AWAITING, never green. An empty slot is a true reading of the record. Nothing is drawn in its place.

### 45.4 The page's age

A page is true for the build it names. The status board's Build Freshness tile is its age; the title block is its
commit. A reading landed after the build is on the next page.

### 45.5 The page's own rendering is measured on your machine

The self-governed rendering is class L on the viewer's own device; its
numbers are the viewer's browser's and prove nothing about any server.

### 45.6 Ask Omni-Compass is composed

Its answers are drawn from the page's records by a language model on the viewer's own
account, are not reviewed by any outside party, and are not a record. The records are the tables and the raw files.

### 45.7 A changed profile is not a result

The live tuning bench shows the governing mechanism so that the profile can be moved, demonstrated and studied. A candidate or
custom profile on the bench is a variation of the mechanism (class S); the page's live model has no meter, so it gives no
physical energy reading; and each route's bill stays unresolved where no price is recorded. The page tells you what the factory
profile did on the systems its records name, and what the mechanism does when a knob is turned; it does not tell you what a
changed profile would do on a real system until that profile is validated and released (`docs/FACTORY_PROFILE.md`).

---

# PART VIII. LICENSE AND YOUR COPY

## 46. License and Commercial Terms

The live benchmark engine page, this manual and every part of the repository are the property of The Omni-Compass LLC; all rights
reserved; all patents, copyrights and trademarks filed in the USA. Use is evaluation and simulation only under `LICENSE`
(`LicenseRef-OmniCompass-Evaluation-1.0`); any commercial use, commercialization, monetization, production use,
redistribution or hosted service requires a signed, paid Omni-Compass Enterprise License (`ENTERPRISE_LICENSE.md`). The
license is governed by the laws of the State of Delaware and the federal laws of the United States, and the state courts of
Delaware and the United States District Court for the District of Delaware have exclusive jurisdiction. Serving the page to
others is a hosted service and needs the Enterprise License. The license, the licensing questions and answers, the third-party
notices, the Enterprise License's standard terms, the patents and trademarks and the security policy are bound into this book
in full (Appendices F to K). Licensing, pilots and evaluations: the Contact page.

## 47. Verifying Your Copy of the Page

### 47.1 The engine

`python3 tools/omni_version.py` prints the engine the checkout stands on and its digest; the page's
`<html data-engine>` must name the same. `python3 docs/engine/build_live_engine.py --check` rebuilds the page in memory and
exits 1 if any record differs from the page; nothing is written.

### 47.2 The mathematics

`python3 docs/engine/check_live_engine.py` runs the page's brain, compass law and verdict against the
Python and the C++ (`docs/engine/cpp_core_probe.cpp`) and prints the largest difference, which is at machine precision.

### 47.3 The records

`python3 docs/engine/check_records.py` reproduces every record the page carries by an independent path
and compares value by value; `docs/engine/APPRAISAL.md` is the standing result.

### 47.4 The wiring

`python3 -m unittest tests.test_live_monitors` holds every monitor to its wiring: every page function a monitor names is in the
page's script; every Python, C++ and check file it names is in the repository; every monitor sits in a numbered section; every
section of the page closes what it opens; and every panel of the Grafana wall sits under the row of its block of the wall, its section named in its
description, numbered as the page numbers it.

### 47.5 The whole

`python3 verify.py` runs every check of the repository, this page's included, and ends
`VERIFICATION: PASS`; `python3 tools/release_manifest.py` writes `RELEASE_MANIFEST.json` at the commit and must read 0 FAIL.
A copy whose page, engine or records differ from what these print is not a copy of the record.

---
# BACK MATTER

## Glossary

- **Active profile.** The settings actually governing the current run (`docs/FACTORY_PROFILE.md`); on the page, the first line of
  the control panel's profile box, FACTORY, CANDIDATE or CUSTOM, with its fingerprint.
- **Actuation.** Each decision's requested settings, those that landed as asked, those held at a muscle's limit, and those still
  moving toward their setting; the profile box's third line.
- **Alarm.** A judged row of a real or modelled run that read LOSS, a run that ended without a measurement, or a watch item,
  raised on the status board worst first with its source and its root-cause document.
- **Anchor.** The part of a page address after `#` (`#s-wall`) that names a section and does not move when sections are
  renumbered.
- **AWAITING.** The signal word of a monitor whose run has not landed: dark, never green.
- **Band.** A reading's safe range, from calm (p = 0) through its center (p = 0.5) to its line (p = 1), with 5% cushions.
- **Beat.** One turn of the governor's loop: read, decide, write, renew the lease. The heart.
- **Breaker.** One monitor's switch in the fuse box: ON draws it live; REST stops its drawing.
- **Calm.** κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)): the nerves' one number, against which each organ's threshold θ grants a hand-back.
- **Candidate profile.** A proposed combination of settings under evaluation; on the page, the sweep's best beat applied by *Try
  the candidate*, never a release.
- **Class (P, L, S).** The evidence class of a number: a physical meter, live software, our own models.
- **Compass position (p).** Where a reading sits in its band; 0 calm, 1 at the line.
- **Console.** The controls of the page's section 3c: every runtime control of the live benchmark engine, acting on both sides alike.
- **Control panel.** The control panel, the page's section 1 (`#s-health`), directly under the wall: wall status and factory tune, the fuse box,
  and the kill switch with the runs, the variation switchboard, the reports and the manuals.
- **Custom profile.** An identifiable configuration that differs from the released factory profile; its fingerprint names it,
  and its results are its own.
- **Decision.** One turn of the governor; the unit of time on every live monitor.
- **Defensive system.** Constraint enforcement, fault detection, containment, recovery and restoration: the bone and the twins,
  the lease's walk back, the kill switch.
- **Dial.** The max (every muscle to its own limit, never below native; the default) or the tune-down (never more than native).
- **Engine that stands.** The engine version on main, named on the page's title block and in `python3 tools/omni_version.py`;
  omni-v22 for this edition.
- **Factory profile.** The complete, versioned set of Omni-Compass default settings shipped together; on the engine that
  stands, omni-v22's, the heartbeat 60 s, every muscle on its card. Every published result is this profile's.
- **Fingerprint (of a profile).** The page's FNV-1a hash of every setting of the mechanism, the heartbeat and every muscle's body
  included: one identity for one set of settings.
- **Fuse box.** The second panel of the control panel (`#fuseBox`) that switches every monitor from one place: the master
  rows, the heartbeat, the sweep, the profile, each route's bill, the mechanism knobs, the twenty scenarios, the injection grid
  and the breakers.
- **Golden signals.** Latency, traffic, errors and saturation: on the page, the golden-signal feed of the page's section 3b.
- **Governing engine.** The executable mathematical rules that turn observations and internal state into governing decisions.
- **Harness.** The machinery that supplies workloads, executes comparisons, checks requirements and records results; on the page,
  the realms harness's record (`realms/harness.py`).
- **Health.** The explicit operating requirements: correctness, service limits, resource bounds and every applicable hardware
  limit.
- **Heart.** The governor's beat and its lease, drawn on the official run playback.
- **Immune system.** Omni-Compass's: native twins, the heat debt, the cure on the spot, the pools' give-back, the bone's grant.
- **Kill switch.** The instant hand-back of every lever to native, for security; red on the switch and on every time axis.
- **Lease.** The governor's proof of life; when it ages past its limit the watchdog walks every setting back to native.
- **Live / Recorded.** A knob marked Live acts on the live benchmark engine; one marked Recorded data chooses a record and modifies nothing.
- **Live tuning bench.** The interface that operates the engine's controls and displays their effects through the connected
  backend: the live benchmark engine page and its control panel.
- **Master switch.** The one switch at the top of the organism: ON (green), the kill switch engaged (red), OFF (white).
- **Monitor.** One canvas of the page that draws a record or the live benchmark engine; its small copy on the wall is a tile.
- **Muscle.** A specific controllable mechanism, with its own actuator, observations, limits and read-back.
- **Native.** The whole system by itself with everything it ships with: the native baseline; orange.
- **Native baseline.** The system's documented configuration and behaviour with no Omni-Compass governing it: every muscle under
  its own native controller, as its vendor ships it.
- **Nervous system.** Observation, signal propagation, coordination and authority pathways.
- **Omni-Compass.** Omni-Compass on top of native; blue. Never by itself: it always sits on top of a native controller, so the
  page has two sides and only two.
- **Organism.** The complete declared system whose useful output, health and resource costs are assessed together.
- **Pedal.** Push for more, lift for less; the force column of the governor's ticker.
- **Power given.** A resource spent or held that rose: what Omni-Compass put in to buy the work and speed beside it; blue.
- **Reading guide.** The page's appendix B (`#s-guide`): every section's introduction under its number and title.
- **REDLINING.** The red signal word, an octagon, blinking: at the top of its band and holding there, or Omni-Compass behind
  native now (a LOSS); OVER THE LINE is past the top of its band.
- **Scorecard.** The scorecard, the page's section 2a: one light and one number for each way to run a workload against native, and the
  whole workload's index on each route.
- **Shown, not judged.** A gauge declared in advance as shown only; grey; counted in no total.
- **STEADY.** The yellow signal word, a yield diamond: inside its band, or level with native (a change under 0.5%).
- **Stopping rule.** The cloud sets' preregistered looks at 10, 20, 40 and 70 repetitions with 99% intervals (`tools/stop_rule.py`).
- **GAINING.** The green signal word, round: low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN).
- **Ticker.** The governor's decisions (first ticker) and native's own controllers' moves (second ticker), newest first.
- **Tile.** One small monitor on the wall; click it to go to the monitor it copies.
- **Twenty scenarios.** Ten organisms, each native and with Omni-Compass on native, each read against native.
- **Verdict.** The paired trial every step past native must pass: kept unless it reads LOSS or exceeds the 2% allowance.
- **Violet.** A knob or a profile turned from the factory tune (`--tuned`); never a side and never a reading.
- **Wall.** Every monitor of the page in one view (the page's section 0), numbered 1 upward by its place in the wall's five
  blocks, each block read left to right, then the next row.

## Appendix A - The Page, Section by Section

| Page section | Anchor | Title | Chapter of this book |
|---|---|---|---|
| — | `#topBanner`, `#notice` | Banner: logo, name, engine chip and legal notice | Notice and Disclaimer |
| 0 | `#s-wall` | Monitor Wall | 1 |
| 1 | `#s-health` | Control Panel (with the fuse box, `#fuseBox`) | 2; 36.1 |
| — | `#contents` | Contents | 3 |
| 2 | `#p-results` | Results | 4 to 8 |
| 2a | `#s-bottom` | Scorecard | 4 |
| 2b | `#s-answer` | Benefit Against Native | 5 |
| 2c | `#s-board` | Benefit Board | 6 |
| 2d | `#s-loss` | LOSS Register | 7, 44 |
| 2e | `#s-status` | Status Board | 8 |
| 3 | `#p-live` | Live Operation | 9 to 17 |
| 3a | `#s-engines` | Live Organism | 9 |
| 3b | `#s-feed` | Golden Signals and Event Log | 10 |
| 3c | `#s-desk` | Control Console | 11 |
| 3d | `#s-dial` | Heartbeat Dial | 12 |
| 3e | `#s-decision` | Control Cycle | 13 |
| 3f | `#s-plane` | Phase Plane and Scoreboard | 14 |
| 3g | `#s-brain` | Brain State | 15 |
| 3h | `#s-verdict` | Verdict | 16 |
| 3i | `#s-dash` | Dashboards | 17 |
| 4 | `#p-runs` | Real Runs and Platforms | 18 to 24 |
| 4a | `#s-ops` | Kubernetes Run Playback | 18 |
| 4b | `#s-runs` | Repetition Telemetry | 19 |
| 4c | `#s-live` | Controller Decision Trace | 20 |
| 4d | `#s-cloud` | Cloud Providers | 21 |
| 4e | `#s-orch` | Orchestrators and Governors | 22 |
| 4f | `#s-stacks` | GPU and CPU Hardware | 23 |
| 4g | `#s-github` | CI Pipeline | 24 |
| 5 | `#p-proof` | Proof and Models | 25 to 34 |
| 5a | `#s-proof` | Python Runs and Monte Carlo | 25 |
| 5b | `#s-cpp` | C++ Twin | 26 |
| 5c | `#s-scn` | Scenarios and Injection Grid | 27 |
| 5d | `#s-whole` | Whole Organism | 28 |
| 5e | `#s-fleet` | Measured Effect | 29 |
| 5f | `#s-lab` | Telemetry Analytics | 30 |
| 5g | `#s-master` | Master Switch Wiring | 31 |
| 5h | `#s-math` | Specification and Mathematics | 32 |
| 5i | `#s-fail` | Failure Modes and Controls | 33 |
| 5j | `#s-self` | Self-Governed Rendering | 34 |
| — | `#p-appendix` | Appendixes | 35 to 41 |
| A | `#title-page` | Title Page and Build | 35, 43 |
| B | `#s-guide` | Reading Guide | 36 |
| C | `#s-problem` | Problem and Answer | 37; The Problem and the Answer |
| D | `#s-read` | Executive Summary and Reading Key | 38; the key |
| E | `#s-monlist` | Monitor List | 39 |
| F | `#s-glossary` | Glossary and Index | 40 |
| G | `#s-disclose` | Disclosures, Law and Contact | 41, 46 |
| — | `#notice-end` | Closing legal notice | Notice and Disclaimer |

## Appendix B - Every Control

| Control | Where | Acts on | Leaves alone |
|---|---|---|---|
| Kill switch | the control panel; the head of the page's section 1; every section's controls; every monitor's strip; the console; the dock | every lever of every governor on the page, to native at once; shades every time axis red; a second press releases it | the records: nothing recorded is modified |
| Return to native (the reset) | the fuse box's profile row; the variation switchboard's native arm | the same hand-back, named the reset; the switch reads "OFF by the reset" | the records: nothing recorded is modified |
| Turn Omni-Compass OFF / ON | the console | the brain's outputs: OFF, read in shadow, nothing leaves; ON, outputs reach the muscles | the native side, which never stops |
| The max / Tune-down | the control panel; the console; the page's section 3e | the dial of the live benchmark engine's governor | the records; the official runs' own dial, named in each |
| The body | the control panel; the page's section 3e | which body the live monitors draw | the records |
| Heartbeat: 10, 15, 20, 30, 60, 90, 120 s | the control panel | the live model's full decision period | the dial's tables (the page's section 3d), which are records |
| Run every beat (10 to 120 s), three days each | the control panel | three model days at each beat on the live model; the sweep's table | the live day in hand, restored after |
| Try the candidate | the control panel | the heartbeat set to the sweep's best beat, a candidate profile | every other knob |
| Restore factory profile | the control panel | the mechanism's knobs and the heartbeat back to the factory's; a hold released; the candidate cleared | the master switch; the plant's conditions |
| Hold the active profile | the control panel | every knob of the mechanism, the heartbeat buttons, the sweep and the beat rows held | the plant's conditions |
| On site / Through the cloud | the control panel | which route's bill the profile box shows | the composition |
| Mechanism Knobs; The mechanism back to the factory | the fuse box (`#mechPanel`) | the live model's equations, on Omni-Compass's side (sections 2.11 to 2.23) | the harness record; the records |
| Every breaker ON; rest every monitor off screen; ON / REST | the control panel | whether each monitor is drawn live | the records |
| Your own system: Connect / Disconnect | the control panel | each monitor's query asked of the operator's Prometheus, read only | the operator's system: nothing is written |
| Demand × | the control panel; the console; the dock | every muscle's demand, both sides, from this decision on | the seed |
| Noise σ | the control panel; the console; the dock | each muscle's demand each decision, 1 + σ·z, one draw shared by both sides | the seed's day |
| Sense delay (+0 to +6 decisions) | the control panel; the console | the decisions between a muscle's act and its controller's reading, both sides | the demand |
| Frame load (as it is, +8 ms, +16 ms) | the console; the page's section 5j | the time burned inside every frame of the page | the engine |
| Load profile, Inject | the console | the same multiplier on every muscle and both sides | the day's mean load, kept |
| Surge ×2 / Lose half its machines / A sense goes blind / Security hold | the control panel; the console; the page's section 3e; the status board's tiles | one body part for 40 decisions, both sides | every other part |
| Pause / One decision / 1× 4× 16× 60× | the control panel; the console; the page's section 3e | the console's clock | nothing else |
| The same day again / A new day | the console; the page's section 3e | the seed replayed or redrawn, with the knobs as set | the knobs |
| Every knob to its start | the console | demand, noise and delay, back to the day as written | the dial and the switch |
| Back to the factory tune | the control panel's first panel and its fuse box; the console; the dock; every monitor's strip; the key `f` | the factory profile and the plant at rest (section 11.2) | the records |
| Arm, Organism, Organisms, Runs, Run, Beat (the variation switchboard) | the page's section 1 | every monitor that carries the variation (section 2.31) | every monitor that does not |
| A / B / C | the page's sections 4a, 4b, 4c, 4f | which run is played | the other runs |
| Benchmark, run, repetition | the page's sections 4a, 4b | which record is played | the record itself |
| This muscle; Every muscle back under Omni-Compass | the page's section 3e, on the muscle's card; the mechanism panel's last group | one muscle of the stress-test model run by native's own controller alone, or in a replay shown by native's own record, while every other muscle stays governed | the body's recorded totals in a replay; the kill switch, which hands every muscle back at once |
| Its own load / The climb / Work waiting in line | the page's section 5e | which load the realms table is read under | the table |
| On-Site Bare Metal / Through the Cloud / In the Device / As a Service | the page's section 5d | which way the stack is bought in the composition | the receipts |
| Every Piece, Intervals Carried / Strict Reading, Index Rule; Chip Run: Beside the Count / In the Count | the page's section 5d | which rule Composed Benefit by Gauge counts by, and whether the chip's run enters; the scorecard's bills and the route's bill follow | the factors |
| All / LOSS / The runs disagree / Live Now / Guards and Open Items / GitHub; All / ALERT / WARN / INFO | the page's sections 2e, 3b | which rows are shown | the rows |
| Copy the exposition | the page's section 3b | the clipboard | the page |
| Inspect; Full screen | every monitor's strip | the monitor's reason, feed, wiring and downloads; the monitor full screen | the monitor's data |
| Run the Python's 500 runs here; a new set (base seed, count); print and download the receipts | the page's sections 1 and 5a | the page's own run of the Python's seeded runs, its digest against the Python's | the Python's record, `results/engine_runs/` |
| Jump generator · OFF / ON | the page's section 1 | set after set from the Python's jump generator, through the proof monitor and the Monte Carlo monitor | the records the page plays when it is OFF |
| Speak aloud / Ask Omni-Compass / Stop | the page's section 5f | the viewer's browser voice; a question composed on the viewer's own account | the records |
| The glossary's search, letters and four parts | the page's appendix F | which terms, organisms or muscles are shown | the glossary's record |

## Appendix C - The Gauges on the Wall

| Gauge | Side | Aim | GAIN reads | Power given reads | Where it comes from |
|---|---|---|---|---|---|
| The work waiting | both | time waited: lower | the blue line under the orange | — | the live benchmark engine; on the official runs, pending pods and the queue |
| The work done | both | work done: higher | the blue line over the orange | — | requests served, jobs finished, work inside the line |
| The decisions past their line | both | missed: lower | fewer blue past the line | — | the compass positions over 1 |
| The capacity held | both | a resource held | a fall (a cut) | a rise | machines, replicas, clock in service |
| Response time, mean, 95th, 99th | both | time waited: lower | a fall | — | the runs' own samples, binned |
| Time over the response line | both | missed: lower | a fall | — | the share of samples over the line |
| Failed requests | both | failed: lower | a fall | — | the load generator's record |
| Alert minutes | both | time over the line: lower | a fall | — | whole minutes whose 95th percentile, failed requests counted over, was over the line |
| Machines billed, the compute bill | both | a resource spent | a fall | a rise | the cloud's own count of machines, priced at list |
| Energy (declared model, the meter, Kepler) | both | a resource spent | a fall | a rise | the declared model; the RAPL counters where a meter exists (P); Kepler shown, not judged |
| HPA replicas, pods started | both | a resource held | a fall | a rise | native's autoscaler's own record in both arms |
| Pod start wait, total and mean | both | time waited: lower | a fall | — | the pods' own start times; the test machine's limit never read as the governor's |
| The governor's commands, its additions inside the line, its own processor time | Omni-Compass | shown, not judged | — | — | the audit; native is 0 |
| Frame time, frames dropped, frames waited | both | time waited: lower | a fall | — | the viewer's browser (L, the viewer's machine) |

## Appendix D - The Colours and the Marks

| Mark | Meaning |
|---|---|
| Orange | native |
| Blue | Omni-Compass; on a reading, power given |
| Violet | a knob or a profile turned from the factory tune (the mechanism panel's knobs, a CUSTOM profile); never a side |
| Green | GAIN |
| Yellow | STEADY |
| Red | LOSS; the kill switch and its window; the master switch engaged; only ever in a stop sign's shape |
| White, dashed edge | the runs disagree; the runs differ; not a reading |
| Grey | shown, not judged; NO LINE, a monitor with no line to cross or no reading yet |
| Green, round | GAINING |
| Yellow, a yield diamond | STEADY |
| Red octagon, blinking red and black | REDLINING |
| Red octagon, blinking red and white | OVER THE LINE |
| Dark, dashed word | AWAITING |
| A tint of orange, dashed | Omni-Compass's side following native with the switch OFF |
| Accent border on a tile | the monitor it copies is on screen now |
| Red shading across a time axis | a kill-switch window |
| A bar on a ring | a room's heat debt (the immune system) |

## Appendix E - Troubleshooting the Page

| Symptom | Cause | What to do |
|---|---|---|
| The page is slow or stutters | the browser's own loop would draw every chart on every frame | the page's section 5j governs it: charts off screen wait; rest monitors at the breakers; close other tabs; the kill switch shows native's loop for comparison |
| A tile is grey or AWAITING and says "not yet run" | the record does not exist yet | nothing: an empty slot is a true reading; the board says where it stands |
| A monitor says "stopped before a result" | a cloud or chip run ended without a measurement | the status board carries it; the run's own log says why (a key cut short, a plan, a quota); fix at the cloud, never on the page |
| The age of the page is over three hours | the rebuild did not run or did not land | `.github/workflows/live-engine.yml` on GitHub; `python3 docs/engine/build_live_engine.py` locally |
| A number on the page differs from a table | the page was built before the table changed | the Build Freshness tile; the table governs; the next build carries it |
| The two sides are identical on a monitor | the muscle is at its limit on native, or Omni-Compass left it native | STEADY, correct; section 42.4 |
| The first ticker is empty | the switch is OFF or the kill switch engaged | nothing decides on top of native while it is; turn it ON |
| The heartbeat, the sweep or the mechanism's knobs do nothing | the active profile is held | *Restore factory profile* in the control panel |
| The active profile reads CUSTOM | a knob of the mechanism or the heartbeat was turned | *Restore factory profile*, or *Back to the factory tune* for the whole page |
| *Try the candidate* does nothing | no sweep has run in this view, or the profile is held | *Run every beat*, then try again |
| A route's bill reads "unresolved" | no price for that component is recorded in the repository | nothing on the page: the measured changes beside it are supporting measurements |
| Ask Omni-Compass does not answer | the page is open outside claude.ai or without permission | the rest of the page runs whole without it |
| The page refuses to build | the checkout's engine is not the one the page names | a new engine is written into the page's words by a person first; `python3 tools/omni_version.py` |

## Appendix F - The License

The license is bound here in full from the file `LICENSE` at the root of the repository, as the book is built.

## Appendix G - Licensing: Questions and Answers

Bound from `LICENSING_FAQ.md` as the book is built.

## Appendix H - Third-Party Notices

Bound from `THIRD_PARTY_NOTICES.md` as the book is built.

## Appendix I - The Enterprise License: Standard Terms

Bound from `ENTERPRISE_LICENSE.md` as the book is built.

## Appendix J - Patents and Trademarks

Bound from `PATENTS.md` and `TRADEMARKS.md` as the book is built.

## Appendix K - Security Policy

Bound from `SECURITY.md` as the book is built.

## Appendix L - The Page Word for Word: Every Section, Monitor and Knob

Bound from `docs/engine/PAGE_WORD_FOR_WORD.md` as the book is built: the page itself, written from
`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build by `docs/book/build_live_manual.py`, every section in the page's
order, every monitor under its number with its evidence class, state, feed and knobs, every knob and every LOSS row with its
cause and the knob that answers it.

## Contact

Licensing, pilots, evaluations and the Omni-Compass Enterprise License: **The Omni-Compass LLC**. Owner and developer: AJ Dubra.
Main office infrastructure: toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1. Landline, registered in
Florida: 321-746-4411. www.omni-compass.com. Repository: github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC. Any use beyond
evaluation and simulation requires a signed, paid Omni-Compass Enterprise License. Write to The Omni-Compass LLC before any
production use.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
