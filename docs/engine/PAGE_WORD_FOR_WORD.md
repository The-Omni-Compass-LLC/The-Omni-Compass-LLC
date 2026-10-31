# The Live Benchmark Engine Page, Word for Word

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This appendix is the live benchmark engine page itself, written from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build of this book (`docs/book/build_live_manual.py`): every section in the page's own order with its number, title, summary and controls line; every monitor under the number its badge carries, with its evidence class, its state, the open-source feed that would carry it on a running system and its knobs; every knob; and every LOSS row with whose it is, its cause and the knob that answers it. Nothing here is typed twice: what the page says, this appendix says, so the book and the page read each other both ways. This edition was written from the page built 2026-10-31 16:17 UTC on omni-v22 (digest 0e23a0bc561b900a) from commit 0371e899990a.


Each part below is one section of the page, in the page's order and under its number: what the page says it is, its controls, its panels, and every monitor in it under its own number, with what it shows, its evidence and state, the feed that would carry it live, its knobs, how to read it and what to do with it.

## 0 Monitor Wall

**Controls.** Click a tile to open its monitor. Every tile is read four times a second.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 1 Control Panel

**Controls.** Live: the kill switch acts at once on every governor of this page; the buttons run the Python's runs here and fetch the three manuals.

**The page, in its own words.**

**Wall Status and Factory Tune**

**Fuse Box**

**Mechanism Knobs**

A tune other than the factory's is a variation of the mechanism (class S, our own model): the benchmarks prove the factory tune only, and a changed tune's results are its own.

**Operator Controls**

ON: the page draws set after set from the Python's jump generator, 500 runs a set unless another size is chosen, one base after another (run k of a set takes the seed base + k·0x9E3779B9 mod 2³², its stream mulberry32, the generator tools/engine_runs.py and tools/core_runs.py write bit for bit). Each set runs twice in this browser: through the engine's runs (288 decisions of the brain, 80 steps of the compass law and one give-back trial a run; the proof monitor, section 5a) and through the core's Monte Carlo (the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps a run, native beside Omni-Compass; the Monte Carlo monitor, section 5a). Each set's output is its 500 runs, their counts and one SHA-256 digest; where the Python has run the same base its record's digest stands beside this page's, and they must be equal. It runs until the switch is pressed again, and rests while the page is hidden. Class S: the engine's own mathematics on draws, never a measurement.

OFF (the page's standing mode, as it opens): nothing new is drawn from the generator. The page plays its records: the Monte Carlo monitor plays the Python's own 500 (benchmarks/core_evidence.py, numpy's generator from seed 223387268, the record results/core_evidence.json); the proof monitor recomputes, once as the page opens, the newest set GitHub ran in the Python and checks it digest for digest, then re-checks it one run at a time; the 500 scenarios a seed replay from their record with every trace hash; GitHub's runs play back from their own raw files; the organism's model day (sections 3a, 3c and 3e to 3h) runs on its own seeded stream, the same at every opening. A button above or in section 5a still runs one set at a time.

Each knob sets every monitor that carries its variation and names them here; a monitor that does not carry it is left as it is.

Kill Switch. While Omni-Compass governs on top of native the switch reads ON in green. Pressed, it turns red: at the next decision every governor puts every setting it wrote back, reads each one back and stops (omnicompass/master.py, tools/omni_switch.py); the word OFF stands white, and every Omni-Compass side of every monitor follows native, drawn in native's colour. Native's own controllers under every muscle never stop and never see the switch. A recorded result never changes with it: its colour does, never a value, a word or a row. The same switch stands at the head of every section and in every monitor's own knobs; one press anywhere is one press everywhere. It is for security and is instant; the walk back after a crash is the lease, separate.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## Part 2 of the page: Results

## 2a Scorecard

**The page, in its own words.**

The light is the whole verdict: green GAINING, Omni-Compass ahead of native; yellow STEADY, within 0.5% of native (STEADY by the key's floor); red REDLINING, behind native. The big number is how much, its size with no sign (the raw change, Omni-Compass − native over native, stands apart with its true sign, labelled raw): on the first row more work done for the same demand, on the bills and the index one number over their gauges, read by the key (GAIN, STEADY, LOSS by what the gauge is for, never by its sign; STEADY only under 0.5%, the mean of the three runs' changes). A slower service, less work or a failed request turns the light red whatever the number, on every row: on the bills and the index, any table under the row that reads one of them LOSS, in either form, turns it red. The bills read the repository's own headline, by the index's rule, with the other reading beside it. Each row names what it stands on: its test, its engine and its evidence class.

**Whole-Loop Test by Arm**

**Whole-Workload Index by Route · Class S**

**All Real Tests Combined**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 2b Benefit Against Native

**The page, in its own words.**

**Bill by Route**

**Its monitors.** This section draws no canvas: it is words and their sources, written in the page itself.

## 2c Benefit Board

**Controls.** Recorded data: every receipt as the repository holds it. The kill switch recolours a recorded result and never rewrites it; console controls never modify it.

**The page, in its own words.**

Every bar is its table's own word (GAIN green, STEADY yellow, LOSS red, power given blue) beside its size; every LOSS row of the benchmarks on this board stands on it, and every LOSS row of every three-run table, the governors' four-ways tables and the service variants included, is raised on the status board (section 2e) and listed, with its cause where the LOSS ledger records one, in section 2d.

**Benefit by Domain**

**Benefit by Gauge Family**

Every judged row of every newest three-run table (section 5e), sorted into the family of gauge it measures. Each bar counts the rows that read GAIN, in all three runs or by the mean of the three; the size beside it is the median of those rows' own sizes, each row's size the mean of its runs' raw changes in percent of native (a row whose native stood at zero has no percent: it is counted and not sized). Power given and LOSS rows are counted beside them.

**Trading Floor**

Every three-run table of section 5e, as GitHub's runs wrote them. The market map: one tile a table, grouped by stack, its area the gauges it judged and its colour its reading: green GAIN, the deeper the more of its rows; red where any row reads LOSS; yellow STEADY; blue where it gave power; grey with a dashed edge a four-ways comparison that is not Omni-Compass against its native (the orchestrator's own, with no Omni-Compass in either arm; Omni-Compass in place of a controller; two changes at once). The board: one quote a table, its ticker and engine, the gauge that moved most with its mean change, and that gauge in each of the three runs (A, B and C) as a candle, the bar its 95% interval and the tick its value against the zero line; the strip under it counts the table's rows by word, and the tape runs every headline across the top. Point at a tile or a quote for its record. Every figure is the table's own.

**Whole-Board Aggregate**

**Its monitors.**

### Monitor 1: Benefit by Domain

Every domain's three-run table as one bar: GAIN, STEADY, LOSS and power given, native against Omni-Compass.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawBenefit, fxCursor` → the Python `tools/benefit_sheet.py`, `tools/omni_index.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the bars, one benchmark at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 4: Benefit by Gauge Family

The same tables by gauge family: work, speed, misses, resources.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawFam` → the Python `tools/benefit_sheet.py`, `tools/readings.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_benefit_sheet.py`, `tests/test_readings.py`.
- **Moves.** The reading cursor walks the families, one at a time.
- **Knobs.** Filter: which rows, words, families or organisms are shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 3: Market Map

Every three-run table on the page as a tile of a squarified treemap, grouped by stack: its area the gauges it judged, its colour its reading (GAIN green, LOSS red, STEADY yellow, power given the accent, an orchestrator's own cost grey and dashed).

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawTradeMap` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The scan cursor walks every tile, one every 1.5 s.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

### Monitor 20: Quote Board

Every three-run table as a quote: its ticker and engine, the gauge that moved most with its mean change, that gauge in runs A, B and C as a candle (the 95% interval and the value), its rows counted by word, and a tape of every headline.

- **Evidence and state.** Class L/S; record.
- **Feed.** the build (the repository's three-run tables, no live feed: a recording rule would carry each table's counts).
- **Wired.** This page's `drawQuotes` → the Python `tools/confirm_abc.py`, `tools/readings.py`, `docs/engine/build_live_engine.py` → the C++ none: the repository's measured tables, read as written; no engine runs in the page for them; held equal by `tests/test_confirm_abc.py`, `tests/test_readings.py`, `docs/engine/build_live_engine.py`.
- **Moves.** The tape of the headlines runs across the top at 55 px a second.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

## 2d LOSS Register

**Controls.** Recorded data: every row is read from the verdict audit's record of the three-run tables and the GPU card's own record.

**The page, in its own words.**

Every LOSS row of every standing three-run table, read from the verdict audit's record, the one selection the LOSS ledger (`docs/LOSS_LEDGER.md`) is written from: Omni-Compass against its native first, then the GPU card's own meter (outside the audit's selection), then the orchestrators' four-ways comparisons by what their two arms are. Each row carries the cause, the fix and what decides it exactly as the ledger records them (tools/loss_ledger.py); where the ledger records none, the row says so and asserts no knob.

**Verdict Audit**

**LOSS Rows Against Native**

**Armada Two-Cluster BARE Table by Run**

**Discrepancy Report**

**LOSS Ledger**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 2e Status Board

**Controls.** Live: the filters act at once, and every tile is read again four times a second.

**The page, in its own words.**

The board shows whether Omni-Compass is engaged, which signals are out of tolerance and where, and every LOSS row raised as an alarm with its source record. Each tile and each alarm is computed at runtime from the live benchmark engine or from the repository's records.

**Alarms and Watch Items by Severity**

A tile's word is its reading against native by the key (appendix D); a tile with no reading says what it shows.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## Part 3 of the page: Live Operation

## 3a Live Organism

**Controls.** Live: the rings, the immune system and the anatomy respond to the console.

**The page, in its own words.**

Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Native**

**Omni-Compass**

**Body Scan by Organ**

The table reads the system playing in section 4a (the benchmark, run and repetition chosen there) organ by organ, half minute by half minute, from its own SHA-256-checked files: native beside Omni-Compass. Where native has no such organ the cell says so.

**Immune System · Class S**

On the ring a pulsing red circle marks the inflamed muscle, and red signals run from it to every machine pool that answers it.

**Anatomy by Part**

**Its monitors.**

### Monitor 5: Native Organism Ring · Class S

Sixty muscles of the stress model, each on its own native controller, at their positions in the band.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); kube-state-metrics; series `omni_recommended`, `kube_horizontalpodautoscaler_status_current_replicas`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position in the band.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; Muscle Switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 6: Omni-Compass Organism Ring · Class S

The same sixty muscles with Omni-Compass on top of their native controllers, the brain's grants and pushes.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_recommended_moves_total`, `omni_writes_total`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawRing` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle moves to its position, the brain's grants and pushes pulse.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused; Body: which body the organism runs: the harness, the organism, every muscle alone; Muscle Switch: pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 11: Immune System · Class S

Where the two sides differ, and the body's heat debt: a room warmer than its native twin, inflamed, given back.

- **Evidence and state.** Class S; live.
- **Feed.** Prometheus Alertmanager; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `ALERTS`, `omni_compass_decisions_total{zone="wall"}`; on a running system: `sum(ALERTS{alertstate="firing"})`; `increase(omni_compass_decisions_total{zone="wall"}[1h])`.
- **Wired.** This page's `drawImm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py`, `realms/compass_arm_v5.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each side's pools, warmest room and muscles past the line take a point.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

### Monitor 35: Body Parts on the Band · Class S

Each body part's muscles (the spine and the four realms) at their positions in the band, native above and Omni-Compass below, every decision.

- **Evidence and state.** Class S; live.
- **Feed.** the realms harness's own record (realms/harness.py, each body part's muscles at their positions in the band, recorded by docs/engine/export_harness_trace.py); no Prometheus feed.
- **Wired.** This page's `drawSwarm` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's dot moves to its position in the band.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.
- **What to do with it.** Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did.

## 3b Golden Signals and Event Log

**Controls.** Live: one point a decision from the live benchmark engine; the event log's filters act at once; the metrics refresh every two seconds.

**The page, in its own words.**

The live organism's four golden signals, native beside Omni-Compass, one point a decision, our own model (class S): errors (muscles over their line), throughput (work done), and, because neither body has a response time or a machine's busy share, latency's and saturation's stand-ins: on the live model the work waiting in line and the capacity in service, on the realms harness the spread of p across the muscles and the electrical power drawn (kW). The query under a panel is the analogous series on a running system, never this panel's data.

**Golden-Signal Feed, Last 240 Decisions · Class S**

One point per decision streamed from the live benchmark engine, gapless, each signal on its own axis, with each arm's last, mean and maximum as a time-series dashboard reports them; a kill-switch window is shaded red. Native in orange, Omni-Compass in blue, the same demand on both.

**Engine Event Log**

The live benchmark engine's own events as it emits them, with the wall-clock time and the decision. They are a threshold breach and its clearing on either arm, every injected fault and its end, the kill switch, the dial, a new day, and each organ's hand-back grant withheld or opened again, at that organ's own threshold θ (pods 0.5, nodes 0.7, the clock, the card and power 0.3, routing 0.5 at the factory: omnicompass/nervous_system.py), as the brain gives it. ALERT, WARN and INFO as an operations log grades them.

**OpenMetrics Exposition**

The live benchmark engine's metrics in the OpenMetrics text format, the CNCF exposition format Prometheus scrapes and Grafana charts, refreshed every two seconds: the same families, under the same names, as the control panel's Metrics tab prints in Prometheus's text format (section 1), from one exposition. They are the master switch, the decisions, the plant's knobs, work served, failed and waiting, the muscle-decisions past their line, writes, capacity, actuation, band time, actuator moves and reversals per arm, and frame time; then the verdict's keep ratio at each true cost, the three-run tables' rows by class, by the engine each table ran on (each that engine's own, never read as the engine that stands's), by the way it compares and by reading, as each table writes it, and the build's engine, digest and commit. Every counter keeps its own arm's value and only rises within a day; the OFF window is marked by omni_master_switch 0 (Omni-Compass's arm then runs at native's own settings), never by putting native's totals in its place.

**Its monitors.**

### Monitor 7: Errors per Decision · Class S

Errors each decision on the live organism, counted as the muscles over their line, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client), kube-state-metrics for pod restarts; series `http_requests_total{code=~"5.."}`, `kube_pod_container_status_restarts_total`; on a running system: `sum(rate(http_requests_total{code=~"5.."}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 8: Throughput per Decision · Class S

Work done a decision (traffic), native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own request counter (Prometheus client); series `http_requests_total`; on a running system: `sum(rate(http_requests_total[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 9: Latency Stand-In per Decision · Class S

Latency's stand-in a decision, native beside Omni-Compass: the work waiting in line on the live model, the spread of p across the muscles on the harness; neither body has a response time.

- **Evidence and state.** Class S; live.
- **Feed.** the service's own duration histogram; series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

### Monitor 10: Saturation Stand-In per Decision · Class S

Saturation's stand-in a decision, native beside Omni-Compass: capacity in service on the live model, electrical power drawn (kW) on the harness.

- **Evidence and state.** Class S; live.
- **Feed.** node_exporter; series `node_cpu_seconds_total`; on a running system: `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`.
- **Wired.** This page's `drawFeed` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine: each side's line takes a point.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.
- **What to do with it.** Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises.

## 3c Control Console

**The page, in its own words.**

Do no harm. What Omni-Compass does with these controls is held by its guards: no muscle driven below native or past its own limit, nothing taken from one muscle to give to another, a give-back tried against native first and refused on a LOSS. Its one meaning is written once, in appendix G, as `DISCLOSURES.md` section 3 writes it.

**System Response per Decision · Class S**

**Inter-Frame Interval**

**Control Event Log**

**Control-Loop Performance Assessment**

**Its monitors.**

### Monitor 60: System Response per Decision · Class S

The last 120 decisions of the live benchmark engine: the muscles past their line and the work, native beside Omni-Compass, every knob of the console turned marked.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawDeskCv` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: both lanes slide one decision, a ring opens at each head with its newest value; every knob turned is marked.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused; Pause: hold the engine's clock; Frame Load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live benchmark engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

### Monitor 61: Inter-Frame Interval

The time between frames of this page against its line under the frame load knob.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawFrameCv` → the Python none: the page's own frame clock, measured in the browser; there is nothing to port → the C++ none: the page's own frame clock, measured in the browser; there is nothing to port.
- **Moves.** Every frame of this page.
- **Knobs.** Frame Load: +0, +8 or +16 ms burned inside every frame of this page.
- **How to read it.** The live benchmark engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.
- **What to do with it.** Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone.

## 3d Heartbeat Dial

**Controls.** Recorded data: every beat of the Kubernetes governor read in our own models (class S, results/model_gate/V17_LADDER.json, tools/beat_ladder.py); the real runs at every beat (`docs/PACE_PREREGISTRATION.md`, amendment 3) join their place when their three runs land. The beat itself is set on the governor's command line (--interval) or with the control panel's heartbeat button (POST /v1/beat, tools/omni_control.py: one button for each stop of the dial), which hands every setting back and starts the governor again at the new beat.

**The page, in its own words.**

The governor's heartbeat, its full decision, is a dial from omni-v17 on: the main engine decides every 60 s, and any of six beats can be set on this page, 10, 15, 30, 60, 90 or 120 s, with the fast checks (the scheduling floor, the pod reflex, the conveyance every 15 s) every 5 s at every beat. Every clock of the governor counts seconds (omni-v16), so turning the dial changes only how often it looks. The governor's own screen counts the time since its last decision in beats of the setting it runs at and alerts after three (omni_heartbeat_seconds, deploy/grafana/omni-compass.json, deploy/prometheus/omni-compass-rules.yaml).

**Beat Ladder · Class S**

Each value is the beat's mean over seeded days on a plant that moves every 5 s, the same seeds and plant at every beat, on the engine its row names; the word beside it is the record's own reading against native (GAIN, STEADY, LOSS, power given: the key, appendix D), decided by the seeds' mean change and the 0.5% floor, with whether the seeds' paired interval stands clear of zero written beside it: a word inside the seeds' noise gives the direction of the mean, not a change the seeds stand behind. Native has no governor, so its reads and processor are blank. The reads are what a beat spends to look more often, shown as the key reads a resource spent: power given. A LOSS here is the engine's at that beat, a model's reading (class S): it stands in this table and on the next version's list; section 2d lists the LOSS rows of the three-run tables of real software, never these.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 3e Control Cycle

**Controls.** Live: the cycle and the controls below share the console's state.

**The page, in its own words.**

Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Decision Sequence**

**Cycle Controls**

The max: every muscle to its own limit, never below native; the capacity it holds is power given. Tune-down: never more than native, and a step back only with the organ’s grant and the release gate. In this model native already sits near its band, so the tune-down finds little to hand back; the scoreboard (section 3f) reads its runs A, B and C live when the dial is on the tune-down. The spread of positions can widen a little, because the calm muscles it hands back move toward their line while the busy ones stay.

Each stress lasts 40 decisions from the moment you press it. Both arms meet the same demand.

**Its monitors.**

### Monitor 25: Compass Band of the Followed Muscle

The compass band with its cushions, the two forces and one decision, step by step.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawBand` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** One control cycle traced step by step on the followed muscle, every decision.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3f Phase Plane and Scoreboard

**Controls.** Live: the phase planes, the strip charts, the stat panels and the scoreboard respond to the console.

**The page, in its own words.**

Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Native**

**Omni-Compass**

**Stat Panels, Last 120 Decisions · Class S**

Each panel is one gauge of the live organism, read every decision on both sides. It gives native's value now and Omni-Compass's, the last 120 decisions of both (native solid orange, Omni-Compass blue), and the running paired reading in the tables' words. With the master switch OFF the decisions are shaded red and Omni-Compass's side follows native: its value equals native's and its line is drawn in native's colour, dashed on top of native's, so both stay in view.

**Running Scoreboard · Class S**

Each row is read on the paired change, native against Omni-Compass at the same decision, averaged over blocks of ten decisions so neighbouring decisions do not count twice, with its 95% interval (Student’s t over the blocks). This run (tools/readings.py, run_word): a change under 0.5% of native reads STEADY; 0.5% or more, the word follows the gauge’s aim (work: a rise is GAIN; misses, failed work, waiting: a fall is GAIN; energy or capacity held: a rise is power given, a fall a cut), its 95% interval printed beside it. Runs A, B and C (tools/readings.py, three_run_reading): the change is the mean of the three runs' changes; under 0.5% it reads STEADY, under the floor; 0.5% or more reads GAIN, LOSS or power given by the gauge's aim, “in all three of our runs” when every run went the same way clear of zero, otherwise “by the mean of our three runs” with the count of runs beyond the noise; runs that moved 0.5% or more in opposite directions disagree. The spread of positions and the settings are shown, never judged: no rule of the engine aims at them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

### Monitor 27: Native Phase Plane

Native's muscles in position and velocity.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 28: Omni-Compass Phase Plane

Omni-Compass's muscles in position and velocity, the band's walls drawn.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`.
- **Wired.** This page's `drawPhase` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision: each muscle's point moves in position and velocity.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 26: Scoreboard Strip · Class S

The body's capacity in service and its demand (in the harness, its electrical power), the muscles past their line and the spread of positions over the day, native beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_decisions_total`, `omni_writes_total`; on a running system: `increase(omni_compass_decisions_total{zone="wall"}[1h])`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawStrip` → the Python `omnicompass/adapter.py`, `omnicompass/core.py`, `omnicompass/nervous_system.py`, `omnicompass/compass_law.py`, `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_twins_parity.py`, `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine (900 ms at 1×): the line takes a point, a ring opens at its head and its newest value is printed beside it.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3g Brain State

In the harness views the harness arm (realms/compass_arm_v5.py) acts muscle by muscle with no brain, so the brain drawn here is the page's own, fed the harness's readings. With each muscle alone there is no body, and its power and thermal readings are held at 0.3.

**Controls.** Live: the wells, the native trace and the nerve meters respond to the console.

**The page, in its own words.**

Evidence class S: our own models, shown beside the real runs and never presented as proof.

**Double-Well Potential of U, Eq. (2)**

V(U) = −μ(U²/2 − U⁴/4) + (Ė/E_max)·U, eq. (2). A rising E tilts the well toward the basin of collapse.

**Cubic Potential of Stress S, Eqs. (5)–(6)**

Φ(S) = αₛ S²/2 + βₛ S³/4 − δS, eqs. (5)–(6). S rolls to S*; the senses pull it back each decision.

**Bath Oscillator B, Eq. (7)**

B̈ = γ[c] δ S − (ω[B]/Q[B]) Ḃ − ω[B]² B, eq. (7). B is the slow tide of physical load.

**Native Controller Trace · Class S**

Native has no brain to draw: each of its controllers reads one reading, its own muscle's, and moves. Drawn live from the same decisions as the wells above: the mean position its muscles' readings put them at (0 calm, 1 at the line), the share of its muscles past their line, and how many of its own controllers moved their setting this decision. Class S, our own models.

**Nerves and Calm**

Native has no nerves: nothing grants or refuses a controller, and a blind sense or a security hold changes nothing it does.

calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)). An organ may hand capacity back only when calm ≥ its θ, the line is clean and every sense is live; expanding stays allowed except under a security hold. Under the max, lifting off toward native never needs this grant; going below native does.

**Its monitors.**

### Monitor 29: Double-Well Potential of U

The brain's double-well potential and where its state sits.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 30: Cubic Potential of Stress S

Stress S on its cubic potential Φ(S) = αₛS²/2 + βₛS³/4 − δS, rolling toward S*; the senses pull it back each decision (eqs. (5)–(6)).

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`.
- **Wired.** This page's `drawBrain, drawWell` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the ball rolls to the brain's state and a ring opens where it lands.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 31: Bath Oscillator B

The bath oscillator B, the slow tide of physical load, over the last 120 decisions (eq. (7)), its spring at the latest B.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`.
- **Wired.** This page's `drawBrain` → the Python `omnicompass/core.py`, `omnicompass/adapter.py` → the C++ `cpp/src/core.cpp`, `cpp/src/governor.cpp`; held equal by `docs/engine/check_live_engine.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** Every decision the bath's line takes a point and a ring opens at its head.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

### Monitor 32: Native Controller Trace · Class S

What native's controller would do at the same decision, beside the brain's grant.

- **Evidence and state.** Class S; live.
- **Feed.** kube-state-metrics; series `kube_horizontalpodautoscaler_status_desired_replicas`.
- **Wired.** This page's `drawNat6c` → the Python `realms/harness.py`, `docs/engine/export_harness_trace.py` → the C++ none: native's own controllers, as the harness's record or the page's own model holds them; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision of the live benchmark engine.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.
- **What to do with it.** The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it.

## 3h Verdict

**The page, in its own words.**

The verdict is the change-acceptance test. Each step is trialled against native and kept unless the measurement reads LOSS or its estimated cost exceeds the 2% allowance. A STEADY result (no difference resolvable from the noise) is also accepted, so on high-variance workloads a step with a small true cost can pass; the lab below measures that false-acceptance rate.

**Current Trial**

**Share of Trials Allowed**

Native: its knob never moves past its own setting, so there is no trial and nothing to judge; every step Omni-Compass takes past native has to pass this test first. The medians alone allow a step when the trial's median is within the allowance of the reference's. The engine's rule (omni-v12's, unchanged) also refuses any step whose interval sits wholly above zero. It measures on while the interval is wider than the allowance, up to three times the pieces measured each side. It keeps a step only if both estimates are inside the allowance. Ported from omnicompass/verdict.py; the costs are modelled (class S).

Wiring per Muscle. The Kubernetes controller measures 200 requests each side against a 2% allowance (omni_controller/controller.py --verdict-samples 200 --allow 0.02), the cost being each request's response time. The noise is measured at every build on each request of the newest tables' own runs. The σ 0.05 and 0.25 used before 19 October did not come from these files and are withdrawn. The GPU card measures 30 requests (gpu_compass.py --verdict-samples 30); in its model the card's own time per request carries no noise. The model gate measures 60 (tools/model_gate.py, σ 0.25). Keep Rate by Cost. Computed live in this page: trials at each cost with this lab's own rule, 200 requests a side to start (the trial side measured on to 600 while its interval is wider than the allowance), a 2% allowance and the measured σ (modelled, class S). With noise this wide, 200 requests a side do not refuse a small LOSS on their own; with no noise any LOSS it can read is refused, 0.1% included. A larger sample would refuse more. Above the verdict the max never goes below native at all, so in the default it never runs (section 4c: no trial on top of the HPA).

**Its monitors.**

### Monitor 33: Trial Costs and 95% Interval

A give-back trial judged against native: its reference, its step, its interval and the word.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`; on a running system: `omni_verdict_state`.
- **Wired.** This page's `drawVerdict, vTick, judge` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** A cost measured every 28 ms until the verdict reads; a new trial starts 2.6 s after.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

### Monitor 34: Share of Trials Allowed

The keep ratio of the verdict at each true cost, from trials run in this page's idle time.

- **Evidence and state.** Class S; live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_verdict_state`.
- **Wired.** This page's `drawVerdict2, runTrialSync` → the Python `omnicompass/verdict.py`, `omnicompass/student_t.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`, `verify.py`.
- **Moves.** Trials run in the browser's idle time; the shares fill as they run.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native).
- **How to read it.** A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.
- **What to do with it.** A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it.

## 3i Dashboards

**The page, in its own words.**

Each form is fed by this page's own model as it runs (class S), native in orange beside Omni-Compass in blue, each change with its word by the key; the forms are the industry's, the numbers are this engine's, and no vendor's product is drawn or implied. The level sets what the host map and the cluster console gather (each muscle, each body part, or the whole organism) and whether the cost form reads body part by body part or the whole organism; the board, the graph, the event stream, the one-line diagram, the wall of numbers and the pipeline always read the whole organism.

**Roles in the Control Stack**

**First Five Products to Benchmark**

Each takes its own preregistration (the knobs it owns, the muscles left native, its learning window), a trial run that is never counted, and its three runs; a vendor's licence is read for evaluation and publication first. Every other product, the observers, the consoles and the native controllers, with its sources: `docs/THE_FIELD.md`. A vendor's savings figure is that vendor's own claim.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## Part 4 of the page: Real Runs and Platforms

## 4a Kubernetes Run Playback

Class L: the benchmark runs themselves, streamed half minute by half minute from the raw files GitHub archived, every file SHA-256-checked.

**The page, in its own words.**

**Data Pipeline**

**Governor Heartbeat and Lease**

A supervisory governor is only alive while its loop turns: once every decision it reads the whole body, decides, writes, and proves it is still there. That turn is the heart. Each beat pumps every reading in through the plug and the decision out (omni_controller/controller.py, its main loop), and renews the governor's lease (master.heartbeat(), omnicompass/master.py). If the heart stops, its process gone or its lease older than its limit (the larger of 120 s and five beats), the watchdog (tools/omni_switch.py watchdog) walks every setting back to native: a stopped heart leaves the body exactly as native runs it. Native has no heart of its own: each of its controllers keeps its own clock (the pod autoscaler every 15 s, the firmware, the thermostats) and no beat joins them. On the engine that stands the governor's heart beats every 60 s at the factory, a full read of the state once a minute (from omni-v17); 15 s, the pod autoscaler's own pace, is a beat a person may pick on the dial (3d), as are 10, 30, 90 and 120 s. omni-v16 beat every 15 s (`docs/OMNI_V16.md`).

The beat runs at a fixed rate, never driven faster by the load it governs: on the engine that stands one decision every 60 s at the factory, or the beat a person picks on the dial, the fast checks every 5 s between beats. The runs replayed here ran on the engine each table names, omni-v12 and omni-v21, each at the beat its run's own files record. Every clock of the engine counts seconds, so the beat's pace sets how often the body is read, never what a rule means: a give-back still waits its trial's minutes, the cushion still keeps its twenty minutes of memory, and a machine still goes back at most one a minute. What it costs is counted inside the body's own load. A decision that fails is recorded and skipped: it writes nothing, the body keeps the last settings that landed, and the next beat comes at its normal time (safe_step). Two gauges below read its health: the share of each beat spent deciding, and how close the lease came to its limit. The page calls a heart under strain when a decision takes more than half its beat, or a gap between beats reaches 80% of the lease. Past half its beat, the governor would have less than half its period left to act before the next reading. Both lines are this page's reading, not rules of the engine; the engine's own guard is the lease and the watchdog.

**Heartbeat Sweep · Class S**

The governor's full read of the state, its heartbeat, is a setting of the run: every clock of the engine counts seconds, so the beat sets only how often the body is read, never what a rule means (omni-v16, `docs/OMNI_V16.md`). The factory sets 60 s since omni-v17, the main engine (omni-v16 set 15 s, the pod autoscaler's own pace; this sweep reads omni-v16 and omni-v15, and the dial's own ladder reads omni-v17 at every beat in section 3d). A slower beat reads the cluster less, a faster one answers sooner; this monitor shows what each beat does. Each bar is our own model (evidence class S, never a benchmark result): the shipped controller on the modelled cluster's 5-second plant, eight seeds of a day each, paired by seed with native and read by the one key (tools/heartbeat_sweep.py, `results/model_gate/HEARTBEAT_SWEEP.md`). Every beat here is read in the model only: a real run reads the one beat it was started with, the governor's --interval.

**Response Time Candlesticks**

**Latency Heatmap**

**Throughput per 30 s Bin**

**Paired Repetitions**

**Governor Decision Ticker**

**Native Controller Ticker**

From the repetition's own audit.jsonl: the minute and second of the decision, the compass position (0 calm, 1 at the line), and the force on the pedal (push: toward more; lift: handing the setting back toward native). Then the machines it recommends, and the give-back verdict's state: "left native" means every setting stays native's; "acting" means a trial on its own measurement. Native has no governor; its own controllers' moves are the second ticker, read from the native arm's capture.csv: the replicas its pod autoscaler holds, the pods waiting for a place and the machines ready. With Omni-Compass OFF the first ticker is empty, for nothing decides on top of native.

**Benchmark Status by Block**

**Its monitors.**

### Monitor 13: Data Pipeline

Every stage from the GitHub Actions run to this page: the run, the raw files archived, the SHA-256 check, the official scorer, the three-run tables, the build and the page, the stage being read lit.

- **Evidence and state.** Class L; replay.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawPipe` → the Python `scripts/raw_archive.sh`, `tools/live_reps.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the stages are GitHub's runs and the repository's own tools; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The stage being read lights in turn and the data moves between the stages.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown.
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 14: Governor Heartbeat and Lease

Native's own 15 s clock above, every beat of the governor's decision loop in the repetition below, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; the load generator's own histogram (the rig's loadgen); series `kube_horizontalpodautoscaler_status_current_replicas`, `kube_node_status_allocatable`; on a running system: `sum(kube_horizontalpodautoscaler_status_current_replicas)`.
- **Wired.** This page's `drawHeart` → the Python `docs/engine/export_runs.py`, `omni_controller/controller.py` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen repetition replayed decision by decision; native's own 15 s clock beats above.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 36: Heartbeat Sweep · Class S

The governor's beat as a knob: what a decision every 5 to 120 s does against native, or against the same engine at 15 s or 60 s, on-site and in the cloud, gauge by gauge with its 95% interval, and what each beat costs the engine; our own model.

- **Evidence and state.** Class S; model.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_decisions_total`, `omni_decision_seconds`, `omni_last_decision_timestamp_seconds`, `omni_own_cpu_cores`; on a running system: `60 * rate(omni_decisions_total[5m])`; `omni_own_cpu_cores`; `time() - omni_last_decision_timestamp_seconds`.
- **Wired.** This page's `drawBeat, beatSetup` → the Python `tools/heartbeat_sweep.py`, `tools/model_gate.py`, `omni_controller/controller.py` → the C++ none here: the sweep runs the shipped Python controller on the model cluster; the C++ governor twin is held to the Python's at 60 s and at 15, 10 and 5 s (tests/test_cpp_governor_parity.py); held equal by `results/model_gate/HEARTBEAT_SWEEP.md`, `docs/engine/build_live_engine.py`.
- **Moves.** A cursor reads the beats in turn and names the row it holds; every button redraws the chart from the record.
- **Knobs.** Beat: the governor's full read of the state and its decision: every 5, 10, 15, 20, 30, 60, 75, 90 or 120 s in the heartbeat sweep's record; on a real governor its --interval (60 s at the factory since omni-v17, 15 s on omni-v16); Scenario: on-site bare metal, through the cloud, in the device, as a service; Engine: which engine's record the monitor reads: the engine that stands or the one before it; Baseline: what each reading is set against: native, or the same engine at another setting; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 15: Response Time Candlesticks

The response time of the chosen run as candles, one a half minute, native above and Omni-Compass below, on one logarithmic scale.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen); series `http_request_duration_seconds_bucket`; on a running system: `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[1m])))`.
- **Wired.** This page's `drawCandle` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 16: Latency Heatmap

The responses of each half minute counted in eight response-time buckets, native above and Omni-Compass below.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawHeat` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 17: Throughput per 30 s Bin

The requests answered each half minute, native and Omni-Compass side by side, the failed requests marked.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawBars` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The chosen run replayed half minute by half minute.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 18: Paired Repetitions

Each repetition's reading in the chosen gauge with its interval.

- **Evidence and state.** Class L; replay.
- **Feed.** the load generator's own histogram (the rig's loadgen).
- **Wired.** This page's `drawReps` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each repetition's reading filled in as the run replays.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Gauge: which gauge of the run is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

## 4b Repetition Telemetry

Class L: real Kubernetes on kind, real databases and a real broker; each three-run table's runs A, B and C, read back from the raw files GitHub archived (results/live/raw), every file's SHA-256 matched against the run's own SHA256SUMS_ALL.txt.

**The page, in its own words.**

**Native**

**Omni-Compass**

**Run Receipt**

**Repetition Score**

**Benchmark Landing Status**

**Its monitors.**

### Monitor 19: Repetition Telemetry per 30 s Bin

One repetition half minute by half minute from its archived capture: the 95th percentile of the response time, the replicas, the host's processor and the governor's heartbeat, native beside Omni-Compass.

- **Evidence and state.** Class L; replay.
- **Feed.** kube-state-metrics; metrics-server; Kepler; series `kube_node_status_condition`, `kube_pod_status_phase`, `kepler_node_package_joules_total`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`; `rate(kepler_node_package_joules_total[1m])`.
- **Wired.** This page's `drawRuStrip` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The archived capture replayed half minute by half minute; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

## 4c Controller Decision Trace

The shipped controller, omni_controller/controller.py, runs decision by decision on the modelled cluster of pilot/selfpilot.py, wired as the repository wires it. Each decision runs the chain left to right: the senses, the six-state brain, the nerves and the machine organ’s grant, the compass law on the service (cloud setting), the verdict’s trial, the release gate, the plug. Every value below is the controller’s own audit record of that decision, recorded by docs/engine/export_controller_trace.py on runs A, B and C (six hours each, a decision every 60 s, class S).

**Controls.** Recorded data: the shipped controller replayed decision by decision from its own audit (class S).

**The page, in its own words.**

**Native**

**Omni-Compass**

**Audited Decision Chain**

**Three-Run Score · Class S**

The paired change per 15 s tick, averaged over ten-minute blocks, with its 95% interval (Student’s t) in each run. Runs A, B and C (tools/readings.py, three_run_reading): the change is the mean of the three runs' changes; under 0.5% it reads STEADY, under the floor; 0.5% or more reads GAIN, LOSS or power given by the gauge's aim, “in all three of our runs” when every run went the same way clear of zero, otherwise “by the mean of our three runs” with the count of runs beyond the noise; runs that moved 0.5% or more in opposite directions disagree. Machines and power: a fall is a cut, a GAIN; a rise is power given. Our own models (class S): a model’s small numbers are the model’s.

**Kubernetes Three-Run Tables · Class L**

**Governor Steering on Kubernetes · Class L**

**Its monitors.**

### Monitor 21: Native Cluster Trace · Class S

The controller every Kubernetes and cloud set runs, replayed decision by decision from its own audit: native's cluster.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_nodes_observed`; on a running system: `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live benchmark engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 22: Omni-Compass Cluster Trace · Class S

The same, Omni-Compass's cluster: every write, every trial, every hold.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_recommended`, `omni_writes_total`, `omni_verdict_state`; on a running system: `omni_recommended`; `increase(omni_writes_total[1h])`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live benchmark engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

### Monitor 23: Machines and Response Time · Class S

The shipped controller's machines (in service, booting and parked) and the response time over the run, native beside Omni-Compass, replayed from its own audit.

- **Evidence and state.** Class S; replay.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_compass_position`, `omni_compass_force`; on a running system: `omni_compass_position`; `omni_compass_force`.
- **Wired.** This page's `drawCStrip` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live benchmark engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.
- **What to do with it.** Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries omni-v23; an older engine's run is its own record.

## 4d Cloud Providers

**Controls.** Recorded data: GitHub's own cloud runs as read at the build. The controller below plays live; its run and speed follow the console's clock.

**The page, in its own words.**

**Cloud Run Ledger**

**Cloud Bill and Gate Monitors**

One monitor a provider, the same harness, mechanism and tuning in all three. Each bar pair is a finished set: native's machine-hours (orange) beside Omni-Compass's (blue), the word the run's own by the one key, the same rule as the bill table below (tools/readings.py run_word: the bill aims lower, a fall of 0.5% or more a GAIN, a rise of 0.5% or more power given, STEADY only under 0.5%), its size with no sign and, above it, whether the change stands beyond the run's own noise; the bill at list price under it. One run is never a set's reading: a set reads GAIN, STEADY or LOSS only from three runs on one engine. A provider with no finished set shows its empty frame and the reason its hourly gate holds, in its own job's words; nothing is drawn for a run that has not run.

**Azure Bill by Run**

From 19 October: every Azure set runs up to 100 paired repetitions a run, the paid cap, under the preregistered stopping rule (tools/stop_rule.py). After 10, 20, 40 and 70 repetitions the bill's change is read with its 99% interval. The run stops once the bill is read (GAIN, power given, or STEADY within ±2% of native's bill), and never while the speed or the failed requests read a LOSS. Those runs carry "to the cap, stopping rule" in their title and count as their own A, B and C; the 5-repetition runs below stay as their own engines' record.

**Cloud-Setting Controller · Class S**

The controller every cloud set runs from 31 October (omni_controller/controller.py at the max, the whole engine), decision by decision on the repository's modelled cluster (class S; until the live-engine workflow rebuilds this record from the push of 31 October, the record shown is the one read at the tune-down on the machines alone). The cloud's own autoscaler runs in both arms. Omni-Compass moves the target inside the autoscaler's cover and parks a machine the cloud already made, after its trial, waking it on a breach. The bill counts every machine that exists, in service, booting or parked, from the record.

**Native**

**Omni-Compass**

**Its monitors.**

### Monitor 37: Azure Bill

Machine-hours billed and the bill at list price, native against Omni-Compass, every finished Azure set with its 95% interval, and the running set's repetitions done.

- **Evidence and state.** Class L (metered by Azure); record.
- **Feed.** OpenCost; Azure's own billing export; series `node_total_hourly_cost`, `kube_node_info`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/live_reps.py`, `tools/stop_rule.py`, `docs/engine/build_live_engine.py` → the C++ none: the bill as Azure meters it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the finished sets; the age of GitHub's reading counts up every second.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 38: Google Cloud Gate and Bill

Google Cloud's hourly gate reading (the key, the login, the quota) and, once a set runs, its bill native against Omni-Compass; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: the first set starts within the hour after the gate passes: the key stored whole (`docs/GOOGLE_SETUP.md`, section 4).
- **Feed.** OpenCost; Google Cloud Billing export; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live benchmark engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 39: Amazon Web Services Gate and Bill

Amazon Web Services' hourly gate reading and, once a set runs, its bill native against Omni-Compass; until its first set lands, the mechanism every cloud set runs, live on the cloud setting's model (class S, marked, never this cloud's bill)

- **Evidence and state.** Class L; awaiting its run: the first set starts within the hour after the gate passes: the account on the Paid plan (`docs/AMAZON_SETUP.md`, section 1).
- **Feed.** OpenCost; AWS Cost and Usage Report; series `node_total_hourly_cost`; on a running system: `sum(node_total_hourly_cost)`.
- **Wired.** This page's `drawCloudBill` → the Python `tools/cloud_key_check.py`, `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `tests/test_cloud_check.py`, `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** Until the first set lands: the modelled machines decision by decision on the live benchmark engine's clock, a ring at each head.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 40: Native Cloud Machines · Class S

The shipped controller's cloud mode on the model cluster: the cloud's own autoscaler alone.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`; on a running system: `count(kube_node_info)`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live benchmark engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

### Monitor 41: Omni-Compass Cloud Machines · Class S

The same autoscaler with Omni-Compass parking a machine only after its trial, waking it on a breach.

- **Evidence and state.** Class S; replay.
- **Feed.** kube-state-metrics; tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `kube_node_info`, `omni_nodes_observed`, `omni_writes_total`; on a running system: `count(kube_node_info)`; `omni_nodes_observed`.
- **Wired.** This page's `drawCluster` → the Python `omni_controller/controller.py`, `pilot/selfpilot.py`, `fleet/harness.py`, `tools/model_gate.py`, `docs/engine/export_controller_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`, `cpp/src/compass.cpp`, `cpp/src/hpa.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`, `tests/test_cpp_hpa_parity.py`.
- **Moves.** The shipped controller's record played decision by decision on the live benchmark engine's clock; a ring opens at each head with its newest value.
- **Knobs.** Run: A, B or C (or the archived run) the monitor plays; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.
- **What to do with it.** The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands.

## 4e Orchestrators and Governors

**Controls.** Recorded data: each governor's place as the repository holds it, its runs read from GitHub at the build and played here the moment they land; click a governor (a tile, a row of the road or of the catalog) to hold it.

**The page, in its own words.**

Each governor and orchestrator runs four ways in every repetition: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, and Omni-Compass on top of the orchestrator; only the last two, each against its own native, are readings of Omni-Compass, and the other comparisons are the orchestrator's own cost. Each place fills itself from the repository as its runs land; until then it shows what the repository holds, and nothing more.

**Road to a Result**

**Orchestration Stack**

Where each governor sits in the stack. Omni-Compass reads and writes on top of it once its wire is in the repository. The governor runs native as shipped beneath it, and Kubernetes places the work on the nodes. The work dots move at the live benchmark engine's demand (section 3c): a picture of the flow, not a measurement. Each governor's readings replace this picture the moment its three runs land.

**Governor and Orchestrator Catalog**

**Four-Way Comparison**

**Orchestra Organism · Class S**

**Its monitors.**

### Monitor 42: Road to a Result

Every scheduler, queue and multi-cluster governor on its way through trial, A, B and C, on the engine that stands.

- **Evidence and state.** Class L; record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter.
- **Wired.** This page's `drawOrchRoad` → the Python `tools/governors_page.py`, `tools/confirm_abc.py`, `docs/engine/build_live_engine.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`.
- **Moves.** A dot travels each governor's road, a running run pulses, and the reading cursor walks the governors, one a decision.
- **Knobs.** Governor: which orchestrator or governor is shown.
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

### Monitor 24: Orchestration Stack

Where the chosen governor sits in the stack: Omni-Compass on top, the governor running native as shipped, Kubernetes and its nodes beneath, the work moving down at the live benchmark engine's demand; a picture of the flow, not a measurement.

- **Evidence and state.** Class L; record.
- **Feed.** kube-state-metrics; each orchestrator's own metrics endpoint (Kueue, Volcano, KAI, Koordinator, Crane, KubeRay); series `kube_pod_status_phase{phase="Pending"}`, `kueue_pending_workloads`; on a running system: `sum(kube_pod_status_phase{phase="Pending"})`.
- **Wired.** This page's `drawOrch` → the Python `tools/governors_page.py`, `tools/run_orchestra.py` → the C++ none: the governors are live software on Kubernetes, run as their projects ship them; held equal by `tests/test_governors_page.py`, `tests/test_orchestra.py`.
- **Moves.** Work flows down the stack at the live benchmark engine's demand.
- **Knobs.** Governor: which orchestrator or governor is shown; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.
- **What to do with it.** Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's.

## 4f GPU and CPU Hardware

Each stack is its own model in the repository, run exactly as the repository runs it and recorded second by second by docs/engine/export_scenarios.py (class S, our own models).

**Controls.** Recorded data: GitHub's chip runs, then the chip models replayed from the repository's own run (class S); pick a setting in the table below.

**The page, in its own words.**

**Metered Hardware Run Slots**

The GPU runs on Lambda (class P: the card's own meter) and the CPU on its own machine (class P: the package's own energy counter, tools/run_cpu_power.py) are the chip's own receipts, read only from their three-run tables: The GPU runs on the engine that stands are counted from GitHub's run records. No CPU package has been measured on real hardware. A place is played back from its raw files like every Kubernetes run once its run is exported for the replay; beside them, the views below other than the metered card run (class P) are the repository's own models of one GPU card and one Linux host (class S), run native and then with Omni-Compass on the same load and seed.

**Metered A100 Run**

The one card run replayed here sample by sample from the card's own meter (class P), native beside Omni-Compass: an NVIDIA A100 (SXM4, 40 GB) on Lambda on 24 October (workflow run 40079645681, omni-v18's card governor at commit e3b05dc), ten paired repetitions of 600 s an arm, native (the card as shipped), Omni-Compass watching only (the switch OFF: it reads and writes nothing) and Omni-Compass governing the power limit and the clock ceiling, every sample of nvidia-smi (200 ms) and every decision of the governor's own audit (results/gpu/run-20261024T091235Z, docs/engine/export_gpu_run.py). On this card native already runs both knobs at their top (the power limit 400 W of 400 W, the clock unlocked to 1,410 MHz), so the factory tune's governor asked for exactly that in its 3,050 decisions and wrote nothing: at its limit on native. The runs on the engine that stands and their three-run tables are counted in the hardware run slots above and listed run by run below, and the 8-card run has not been run (its one launch was a priced dry run). The A10 run of 2 October (the card controller of commit c908054, replaced since) stays as its own record in results/gpu/run-20261002T082232Z. Its own table, re-read by the one key:

**CPU Host Model · Class S**

The CPU power harness (tools/run_cpu_power.py) puts Omni-Compass on top of the Linux kernel's own frequency governor and meters the processor's package energy (RAPL). No GitHub runner exposes that counter or a writable ceiling, so its real run waits for a Linux machine that does (the register's row 18, cpu-power.yml). Until then this monitor plays the harness on its own modelled machine (--plant sim, written for its tests; results/sim/cpu_power_model, three repetitions): the mechanism moving, every decision and write of its own audit, never a measurement. The machine layer enters the whole organism as exactly 1 until the real run lands.

**8-Card GPU Node · Class S**

The 8-card result is one command on a rented machine with eight NVIDIA cards (scripts/gpu_8card.sh, `docs/GPU_RUN_GUIDE.md` section D): every card runs the whole card test at once, its firmware alone against its firmware with Omni-Compass on top, 24 paired repetitions a test pooled across the cards. It has not run. The monitor is built for it: eight card slots, each native lane drawn from the repository's one-card model (class S: AI token generation at the card's shipped 150 W, the same model on every card until the run, never eight measurements), each Omni-Compass lane empty until the run lands. On a running node the same panel reads the NVIDIA DCGM exporter's series card by card.

**Chip Run Ledger**

**Chip Model Settings · Class S**

Read from the replayed record itself, second by second, in each of the three runs (seeds as below). A row with no second held off native is Omni-Compass deciding to stay native: its trial of one step read LOSS and was refused, or the knob is already at its limit on native.

**Native**

**Omni-Compass**

**Omni-Compass Audit Trail · Class S**

**Three-Run Score · Class S**

**Its monitors.**

### Monitor 43: Metered A100 Run

The NVIDIA A100 (SXM4, 40 GB) run of 24 October on Lambda (omni-v18's card governor, workflow run 40079645681, ten paired repetitions) replayed from the card's own meter: draw, limit, clock and temperature, requests served and the 95th percentile, native beside Omni-Compass, every write of the governor marked. Every service gauge read STEADY: native already ran both knobs at their top, so the governor wrote nothing (at its limit on native).

- **Evidence and state.** Class P; awaiting its run: the stacks with the card inside on omni-v21, A, B and C on Lambda's A10, finished on 28 October (`docs/RUN_LEDGER.md`): their files are on the raw branch and their three-run table is not yet written; the A10 run of 2 October is obsolete and stays as history.
- **Feed.** NVIDIA DCGM exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`, `DCGM_FI_DEV_GPU_TEMP`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_POWER_MGMT_LIMIT`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawGpuRun` → the Python `docs/engine/export_gpu_run.py` → the C++ none: omni-v18's card governor, replayed from the card's own meter; today's GPU rules have their twin, cpp/src/gpu_rules.cpp, for the omni-v21 runs on Lambda; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The card's own meter replayed at ten times the run's seconds.
- **Knobs.** Repetition: which repetition of the run is replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v23 run lands.

### Monitor 44: CPU Host Model · Class S

The CPU power harness on the host: the frequency ceiling, the clock run at, the package power and the response line, native beside Omni-Compass; today its own modelled machine (class S), the real run the day a machine with its meter runs it.

- **Evidence and state.** Class S (model) until the run; awaiting its run: a Linux machine whose processor exposes its energy counter (RAPL) and a writable frequency ceiling (register row 79, cpu-power.yml).
- **Feed.** node_exporter (rapl, cpufreq collectors); Kepler; series `node_rapl_package_joules_total`, `node_cpu_scaling_frequency_hertz`, `node_cpu_scaling_frequency_max_hertz`, `kepler_node_package_joules_total`; on a running system: `rate(node_rapl_package_joules_total[1m])`; `avg(node_cpu_scaling_frequency_hertz)`.
- **Wired.** This page's `drawCpuHost` → the Python `docs/engine/export_cpu_model.py`, `tools/run_cpu_power.py` → the C++ none: the host's model until its run lands on a machine with its meter; held equal by `tests/test_run_cpu_power.py`.
- **Moves.** The host's model replayed second by second until its run lands.
- **Knobs.** Repetition: which repetition of the run is replayed; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The processor's frequency ceiling (the knob), the clock the kernel's own governor ran at under it, the package power and the busy share, native beside Omni-Compass.
- **What to do with it.** Until a machine with its energy counter runs it, the monitor plays the harness's own modelled machine: read the mechanism, never the numbers.

### Monitor 45: 8-Card GPU Node · Class S

Eight card slots for scripts/gpu_8card.sh: each native lane the repository's one-card model (class S), each Omni-Compass lane empty until the 8-card run lands, 24 paired repetitions a test pooled across the cards.

- **Evidence and state.** Class S (native model) until the run; awaiting its run: scripts/gpu_8card.sh on a rented machine with eight NVIDIA cards (`docs/GPU_RUN_GUIDE.md`, section D).
- **Feed.** NVIDIA DCGM exporter, card by card; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_POWER_MGMT_LIMIT`, `DCGM_FI_DEV_SM_CLOCK`; on a running system: `sum by (gpu) (DCGM_FI_DEV_POWER_USAGE)`.
- **Wired.** This page's `drawGpu8` → the Python `realms/gpu_card.py`, `omni_controller/gpu_governor.py`, `scripts/gpu_8card.sh` → the C++ `cpp/src/gpu_rules.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** The one-card model's native lanes replayed second by second; the Omni-Compass lanes wait for the 8-card run.
- **Knobs.** Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v23 run lands.

### Monitor 46: Stack Models · Class S

The repository's own models of one GPU card and one Linux host, native beside Omni-Compass, second by second (class S).

- **Evidence and state.** Class S; model.
- **Feed.** NVIDIA DCGM exporter; node_exporter; series `DCGM_FI_DEV_POWER_USAGE`, `DCGM_FI_DEV_SM_CLOCK`, `node_cpu_scaling_frequency_hertz`; on a running system: `DCGM_FI_DEV_POWER_USAGE`; `DCGM_FI_DEV_SM_CLOCK`.
- **Wired.** This page's `drawSStrip` → the Python `realms/gpu_card.py`, `omnicompass/compass_law.py`, `tools/model_gate.py`, `omni_controller/muscles.py`, `omnicompass/conveyance.py`, `docs/engine/export_scenarios.py` → the C++ `cpp/src/conveyance.cpp`, `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_records.py`, `tests/test_cpp_conveyance_parity.py`, `verify.py`.
- **Moves.** The chip's and the host's models replayed second by second; a ring opens at each head with its newest value.
- **Knobs.** Stack: the GPU card, the Linux host, Kubernetes or the cloud; Run: A, B or C (or the archived run) the monitor plays; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.
- **What to do with it.** Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its omni-v23 run lands.

## 4g CI Pipeline

**Controls.** Recorded data: GitHub's runs as read when the page was built.

**The page, in its own words.**

**GitHub Actions in Flight**

Read at the build from GitHub's own API: a workflow's running runs in solid blue, its waiting ones pale; the Azure set to the paid cap with its repetitions measured so far (the table is written when the set ends); each cloud's hourly gate with the reason its own job wrote. Live, the same lives in the open-source github-actions-exporter for Prometheus.

**Running and Queued Workflows**

The page is rebuilt by GitHub itself (.github/workflows/live-engine.yml, docs/engine/build_live_engine.py) whenever the engine, a model or a result changes, and every three hours. Every record is made again by the repository's own code on the engine that stands, checked against the Python and the C++, and committed. This table is GitHub's own list at that moment.

**Its monitors.**

### Monitor 59: GitHub Actions in Flight

Every workflow run in progress or queued when the page was built, the Azure set's repetitions done of its cap, and the clouds' gates.

- **Evidence and state.** Class L (GitHub's own API, read at the build); record.
- **Feed.** GitHub Actions API (read at the build); live: github-actions-exporter; series `github_workflow_run_status`, `github_job_duration_seconds`; on a running system: `sum by (workflow) (github_workflow_run_status == 1)`.
- **Wired.** This page's `drawCi` → the Python `docs/engine/build_live_engine.py` → the C++ none: GitHub's own record of its runs, read from its API at the build; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** The reading cursor walks the workflows, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** GitHub's runs in flight at the build by workflow, the Azure set's repetitions measured, each cloud's gate with its reason, the chips' runs.
- **What to do with it.** A gate that holds names its fix in its own words; nothing is billed while it holds.

## Part 5 of the page: Proof and Models

## 5a Python Runs and Monte Carlo

**Controls.** Live: the runs start on their own when the page opens; the buttons run them again, run a new set from any base, print them and save the receipts.

**The page, in its own words.**

**Seeded Engine Runs and Replayed Scenarios**

Three-Way Run Check. tools/engine_runs.py runs N runs from a base seed: run k's seed is base + k·0x9E3779B9 mod 2³² (the jump generator), its stream mulberry32 (this page's own generator, written in the Python bit for bit), through the engine that stands: 288 decisions of the brain's state equations integrated by the fourth-order Runge–Kutta step, 80 steps of the compass law and one give-back trial judged by the verdict. Each run's receipt is its final state, its pushes and grants, the law's mean and last force and the trial's answer; the digest is the SHA-256 of every receipt at six decimals. The Python writes every draw of every run, the injection, and the C++ harness (cpp/tools/engine_runs.cpp) reads it as its input, puts the mechanism on through the engine's C++ twins and writes every receipt: its digest must be the Python's. This page runs the same N with its own port of the engine (proven equal to the Python and the C++ to 1e-12 on every build by docs/engine/check_live_engine.py) as it opens and compares every receipt and the digest. GitHub does all three on every set it runs (.github/workflows/engine-runs.yml) and on every push (verify.py); run the Python again with another base and it writes another set, and the three digests must be one.

**Engine Core Monte Carlo**

**Custom System Run**

A system is your own stack written as ranges of the engine's core: a name, and for any of the six starting states (E, energy debt; U, the order parameter, its basins at −1 and +1; I[U], the integral of need; S, stress; B, the bath; Ḃ, its rate; the block below names each by its key) and any of the 22 parameters of omnicompass/core.py a range [low, high] or one number; the rest keep the engine's own. Among the parameters: beta_int and beta_ext, the demand into E from inside and outside; E[max], the headroom; c, ω[B], Q[B] and λ₀ to λ₂, the bath's swing; mu, the depth of the double well. The draws keep their one order, so the jump generator's streams are the same; only the ranges they spread over change. The block is read as numbers only, never run as code (`systems/README.md`).

On GitHub (the modelled runs done within GitHub, on its own machines, at no cost): the button checks the block, copies it and opens the monte-carlo workflow. There, press Run workflow, paste the block into system, set runs (500) and base (empty for a new one) and press Run workflow again. The Python (tools/core_runs.py) draws the runs, the C++ twin of the core (cpp/tools/core_runs.cpp on cpp/src/core.cpp) runs the same draws, this page's own port is run on them in node, and the three digests must be one; the record, with the run's link, is committed to results/core_runs/ and joins this monitor's table at the page's next build. A system file committed under systems/ runs there on every push that changes it. GitHub offers Run workflow for a workflow on the repository's main branch, where this one is (.github/workflows/monte-carlo.yml).

Class S: the engine's own mathematics on your ranges, never a measurement of your stack. Wiring Omni-Compass onto the stack itself is the plug of the Operator's Manual.

Every line is one run of omnicompass/core.py: six states (E, U, I[U], S, B, Ḃ), the fourth-order Runge–Kutta step 10 times a macro step (Δt 0.01 s), 20 macro steps, from the starting state and parameters the run drew; the line is its U at step 0 and at the end of every macro step. The left lane is native: the same plant with no command (u = 0), left to its own double well, μU(1 − U²). The right lane is Omni-Compass on top: the bounded feedforward-plus-proportional command (u = −f[U] + 12(σ − U), clipped to ±25 and held across the four stages) toward the nearest basin, or, by the knob, toward the far one, or with the double well switched off (μ = 0). The green bands are the basins, |U ∓ 1| ≤ 0.10. A run is conveyed when it has stayed in one basin for 5 macro steps in a row, certified at 10; the bars under each lane count the macro step each run was conveyed (its colour) and certified (green), and the counters read at the sweeping cursor. The set the page opens on is the Python's own 500 (benchmarks/core_evidence.py, numpy's generator from seed 223387268), whose counts must be its record's (results/core_evidence.json); a set run here from the jump generator is computed by this page's own port of the core, line for line, and its digest must be the one tools/core_runs.py writes for the same base. Class S: the engine's own mathematics, never a measurement.

**Its monitors.**

### Monitor 50: Three-Way Run Check

The engine's seeded runs: the Python's receipts (results/engine_runs) beside the same runs computed by this page's own engine, run by run, with one digest each.

- **Evidence and state.** Class S (the engine itself); live.
- **Feed.** tools/engine_runs.py (the Python) and this page.
- **Wired.** This page's `drawProof, engineRuns, proofRecheck` → the Python `tools/engine_runs.py` → the C++ `cpp/tools/engine_runs.cpp`, `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `verify.py`, `tests/test_engine_runs.py`, `.github/workflows/engine-runs.yml`.
- **Moves.** The page recomputes one run of the Python's set from its own seed about twice a second, round after round, and holds its receipt against the Python's.
- **Knobs.** Runs: how many of the Python's runs this page computes again; Print: the receipts of the runs, printable, with the digests and the notice.
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

### Monitor 51: Held-Out Scenario Replay

benchmarks/stack_benchmark.py's 500 scenarios a seed base (the two held-out seeds), each through every arm, replayed from its record scenario by scenario with every trace hash and the file's SHA-256; verify.py replays them on every push.

- **Evidence and state.** Class S; replay.
- **Feed.** benchmarks/stack_benchmark.py (results/heldout_seed_*/RUNS.csv).
- **Wired.** This page's `drawHeld` → the Python `benchmarks/stack_benchmark.py`, `omnicompass/adapter.py`, `omnicompass/shield.py`, `omnicompass/stack_sim.py`, `docs/engine/export_heldout.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/shield.cpp`; held equal by `verify.py`, `tests/test_cpp_governor_parity.py`, `tests/test_cpp_shield_parity.py`.
- **Moves.** The 500 scenarios replayed one after another from the record, every scenario's trace hash with it.
- **Knobs.** Seed Base: which held-out seed base's 500 scenarios are replayed; Arm: which arm stands on the right: Omni-Compass governing, or watching only; Gauge: which gauge of the run is shown; Speed: 1×, 4×, 16× or 60× of the engine's clock; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

### Monitor 52: Engine Core Monte Carlo

The engine's core (omnicompass/core.py) over 500 runs, each from step 0: the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps, native (the plant alone, u = 0) beside Omni-Compass on top (the bounded command toward the nearest basin, the far basin, or with the double well off), every run's U, the basins at ±1, and the macro step each run was conveyed (5 in a row) and certified (10 in a row); the Python's own 500 (benchmarks/core_evidence.py, seed 223387268) and every set the jump generator draws here, each held to tools/core_runs.py's digest; the linked run holds the Python's digest, the C++ twin's on the same draws and this page's beside each other, and a system of your own runs here or on GitHub.

- **Evidence and state.** Class S (the engine itself); live.
- **Feed.** benchmarks/core_evidence.py and tools/core_runs.py (the Python) and this page's port of the core.
- **Wired.** This page's `drawMC, mcRun, mcLinkedRun, mcSysParse, coreSim, coreRk4, jgTick` → the Python `omnicompass/core.py`, `benchmarks/core_evidence.py`, `tools/core_runs.py`, `systems/README.md`, `docs/engine/build_live_engine.py` → the C++ `cpp/tools/core_runs.cpp`, `cpp/src/core.cpp`; held equal by `tests/test_core_runs.py`, `tests/test_cpp_core_runs_parity.py`, `verify.py`, `.github/workflows/monte-carlo.yml`, `.github/workflows/engine-runs.yml`.
- **Moves.** The cursor sweeps macro step 0 to 20 in 10 s, every run's line drawn up to it, the counters and the bars read at it; with the jump generator ON a new set of 500 arrives set after set.
- **Knobs.** Set: the Python's own 500 (numpy, seed 223387268) or a set the jump generator drew on this page; Omni-Compass Way: the bounded command toward the nearest basin, toward the far basin, or with the double well off (μ = 0); native is the plant alone (u = 0); Custom System: your stack written as ranges of the core's six states and 22 parameters, run in the page or on GitHub through the Python and the C++ (`systems/README.md`); Play / Pause: the cursor's sweep of the 20 macro steps, held or running; Runs: how many of the Python's runs this page computes again; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.
- **What to do with it.** Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file.

## 5b C++ Twin

**The page, in its own words.**

**Twin Parity Checks**

**C++ Engine Run Receipts**

The Python's seeded runs (tools/engine_runs.py: the jump generator's seeds, 288 decisions of the brain, 80 steps of the compass law and one give-back trial a run) are the input: the Python writes every run's draws as the injection, the C++ harness (cpp/tools/engine_runs.cpp) reads it, puts the mechanism on through the C++ twins (the governor, the nervous system, the compass law, the verdict) and writes its own receipts and digest, the output. The proof monitor (section 5a, Seeded Engine Runs and Replayed Scenarios) shows the same column run by run.

**Compass Law Parity on Page Runs**

**Organism Law Parity at the Tune-Down**

**Python-Only Components**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 5c Scenarios and Injection Grid

**Controls.** Recorded data: click an organism and an arm, or hover a cell, for its gauges and its readings. In the injection grid: the organism, the way (Omni-Compass on native, a governor on the organism, Omni-Compass on top of a governor), what it is read against, the runs (1, 10, 100, 500), the organisms stacked (1, 10, 100, 500), the gauge and the injection; exports, an import and a reference to any cell. Both grids also stand in the control panel (section 1), and the Variation Switchboard's runs, copies and organism drive the injection grid.

**The page, in its own words.**

Twenty cells, each read by the key against native, from the record results/scenarios/SCENARIOS_20.json: cells 1 to 9 our own models (class S), three runs A, B and C on the engine named above the grid, each that engine's own, never read as the engine that stands's until its rerun lands; cell 10 a composition by our own code of measured tables across engines (class S of class L and P measurements), its engines named in the cell, never three runs. Each cell shows every judged gauge, power given beside the work and the time over the line it bought. A cell with no run reads "not yet run", never a number.

**Twenty Scenarios**

**Injection Grid**

Class S, our own models (tools/injection_grid.py, results/injection_grid/).

The governors themselves, as their projects ship them, run on real Kubernetes in section 4e (class L): fourteen named, twelve with a rig built, eleven run the four ways (KubeEdge and Nephio are modelled only). A LOSS counts against Omni-Compass only on a way with Omni-Compass on top (on native, or on top of a governor); a governor on the organism read against native is the governor's own reading, shown as the governor's. One batch is one run in the key's sense; three batches make a three-run reading.

The injection grid draws as the page opens.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 5d Whole Organism

The composition is read four ways (the Scenario knob): the two ways a stack is bought, and two more that take its pieces alone, in the device (the bare metal by itself) and as a service (the software by itself). The composition is a model (evidence class S) of class P and class L measurements under the separability assumption; no run has yet stacked every layer at once, and that stacked run is the measurement that would replace it. The chip's newest finished run (the A100 of 24 October on Lambda, omni-v18's card governor, ten paired repetitions: every service gauge STEADY, the governor writing nothing because native already ran both knobs at their top) stands beside the count by default, every row of it shown; one click puts it in, until a three-run table from the stacks with the card inside on omni-v21 replaces it (their runs on Lambda finished; their files are on the raw branch, and no table has been written from them yet). The A10 run of 2 October is obsolete. The machine (the kernel, bare metal, Kepler) is not yet run and enters as exactly 1, named. GAIN is green, LOSS red, STEADY yellow, power given blue, on every word, cell and tile.

**The page, in its own words.**

Composed Reading. —

CLOUD BACK-END METERING DISCLOSURE. Through the cloud, the bare metal at the back end belongs to the provider: no tenant can read its power meter or write its chips' limits, so no run here reaches it. What a tenant can measure is what the cloud meters and bills: the machines it counts every fifteen seconds and the bill at list price (section 4d); that difference, native against Omni-Compass on top of the cloud's own autoscaler, is the cloud piece's benefit, and it is the provider's own health on its own hardware too, fewer machines held for the same work. The bare-metal piece is gauged on hardware we can meter (the card's own meter, the CPU host's energy counter, section 4f) and claimed for the provider's bare metal only as the same mechanism on the same kind of part: the composition multiplies it in as a modelled factor (class S of class P), never as a measurement of the provider's machines. Four ways are composed: on-site bare metal (the owner's own racks and chips: software × bare metal); through the cloud (the cloud's build, its bare metal at the back end and the software; and the cloud as two pieces, the back end left to the provider); in the device (Omni-Compass built into the bare metal alone, the card and the machine, nothing else wired: for an owner who ships hardware); as a service (the software alone, run for an owner with neither bare metal of their own nor a cloud account: the transport of the software only). This whole stack is a composition with two arms, native and with Omni-Compass on top of every piece; it is not counted among the organisms (the seven, and the orchestra the eighth). Each piece is its own newest measurement, on the engine its record names (the cloud piece Azure's three one-run tests, two on omni-v1 and one on the engine of commit 5b2832f of 4 October, the chip piece the A100 run of 24 October under omni-v18's card governor, the software pieces their newest three-run tables): the composition is across those engines, names each, and is remade as each piece's run on the engine that stands lands.

**Stack Composition**

**Composed Benefit by Gauge**

**Composition by Piece and Layer**

**Bills and Receipts**

**Tables Outside the Count**

**Its monitors.**

### Monitor 2: Stack Composition

The pieces of a stack, native beside Omni-Compass, each piece's composed factors and the whole, their product, in every way a stack is bought.

- **Evidence and state.** Class S (of P and L); composed.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawWhole` → the Python `tools/whole_system.py`, `docs/engine/export_whole.py` → the C++ none: a composition of measured tables by the product law, read as tools/whole_system.py writes it; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Work flows down both columns; the reading cursor walks the pieces, one a decision.
- **Knobs.** Scenario: on-site bare metal, through the cloud, in the device, as a service; Reading: every measured piece carried, or the index's strict rule; Chip Run: the chip's one run beside the count or in it; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.
- **What to do with it.** Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob.

## 5e Measured Effect

**Controls.** Recorded data: every receipt as the repository holds it. Console controls never modify it.

**The page, in its own words.**

**Seven Organisms Under Three Loads · Class S**

**Catalog Muscle Matrix · Class S**

Click a cell to read the muscle: its name, family, realm, template, knob and its word under each load.

**Open Register Slots**

**Scale-Out Grid**

**Misses · Class S**

**Cluster 95th Percentile · Class L**

Each square runs the real cluster inside the model.

**Standing Three-Run Tables**

From each benchmark's newest engine's table (results/live/V<engine>_*.md, the engine named in each row), read row by row by docs/engine/export_scenarios.py; open a row to read every judged row that is not STEADY. Class L: the real software (Kubernetes on kind, the real databases and broker). Class S: the outside simulators run by our own runner (CityLearn, pandapower on SimBench, MuJoCo Menagerie, gym-pybullet-drones). Rows shown and not judged are left out of the counts; the counts take every table of a receipt, its tuning case included where it has one (a receipt's own summary line counts its untouched cases). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Realms Table · Class S**

The eighth organism, the orchestra (every governor's catalog muscles, each governor's a body of its own and all of them one body), has its own runner and its own table: section 4e, under the governors.

**Families by Stack**

From results/realms_v5/REALMS_V5.json, the realms runner at the max, its engine and commit named above (tools/run_realms_v5.py, catalog realms/catalog_v5.csv), ten paired seeds per muscle and per organism, the lease after 80% of every run. Misses: the plant decisions over their line, summed over the ten seeds. A muscle reads GAIN when one of its aims (more work, faster, fewer misses) moved beyond the noise under some load with none moving the other way; STEADY at its limit on native when its knob already sits at the top of its range. Energy is power given where it rose. Evidence class S, our own models: a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.**

### Monitor 47: Seven Organisms Under Three Loads · Class S

Each organism's misses against native under its own load, the climb and the line (the realms table).

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawOrgCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks every organism under every load, one a decision.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow STEADY, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

### Monitor 48: Catalog Muscle Matrix · Class S

The 1,107 muscles as one matrix, each cell its word against native, by family and realm; a click names the muscle.

- **Evidence and state.** Class S; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawMuscleCv` → the Python `tools/run_realms_v5.py`, `realms/harness.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `tests/test_realms.py`, `tests/test_cpp_governor_parity.py`.
- **Moves.** The reading cursor walks the 1,107 muscles, one a decision; a click holds one.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Every muscle of the catalog one cell, its word against native on its own load: green GAIN, yellow STEADY (pale: at its limit on native), red LOSS.
- **What to do with it.** Click a cell to read the muscle: its family, realm, template, knob and its word under each load.

### Monitor 49: Scale-Out Grid

Seven organisms × copies × runs: every square's word, modelled and with the real cluster inside.

- **Evidence and state.** Class S/L; record.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawGridCv` → the Python `tools/grid_v5.py`, `scripts/dispatch_grid.py`, `docs/engine/build_live_engine.py` → the C++ none: the grid's squares as its runs on GitHub write them; held equal by `tests/test_grid_v5.py`.
- **Moves.** The reading cursor walks every square with runs started, one a decision; the age of GitHub's reading counts up every second.
- **Knobs.** Filter: which rows, words, families or organisms are shown.
- **How to read it.** Each organism or grid square read by the one key: green GAIN, yellow STEADY, red LOSS, grey a single run, dashed not yet run.
- **What to do with it.** A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs.

## 5f Telemetry Analytics

The engine's own record is a tensor: two arms × every decision × sixty muscles, each entry a muscle's compass position (0 calm, 0.5 the center of its band, 1 its line), recorded from realms/harness.py by docs/engine/export_harness_trace.py (class S, our own models). The service level, error budget and gauge panels read the official runs (class L); every GAIN, STEADY, LOSS and power given in this section is a run's own reading.

**Controls.** Recorded data: the engine's harness record (class S), played on the live benchmark engine's clock, and the official run chosen in section 4a (class L). Console controls never modify either.

**The page, in its own words.**

**Omni-Compass Narration**

Every line is read from Omni-Compass's own records at the moment on screen (the official run playing in section 4a, its governor's own audit, and the engine's harness on the console's clock) and says what Omni-Compass is doing, beside what native does. Speak aloud reads the lines out on the viewer's own browser voice as the run plays, and reads Omni-Compass's answers below too.

**Telemetry Tensor Cube · Class S**

**Tensor Difference Matrix · Class S**

**Tensor Principal Modes · Class S**

**Service Level and Error Budget**

**Repetition Gauges Against Native**

**Ask Omni-Compass**

Omni-Compass answers in the first person, for its own mechanism and its own runs, reading only this page's records through six tools. The words are composed for it by Claude on claude.ai, on the viewer's own account and with the viewer's permission; opened anywhere else, the rest of the page runs whole without it.

Connecting…

Omni-Compass's answers are drawn from this page's records and are not reviewed by any outside party. © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with LICENSE, NOTICE and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**Its monitors.**

### Monitor 53: Telemetry Tensor Cube · Class S

The engine's harness record as a tensor (decisions × sixty muscles × two arms), native and Omni-Compass as two slabs, filling in on the live benchmark engine's clock.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** kube-state-metrics; the service's own metrics.
- **Wired.** This page's `drawCube` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Fills in decision by decision on the live benchmark engine's clock, and turns.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 54: Tensor Difference Matrix · Class S

The difference of the two sides' tensors, cell by cell.

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawDelta` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** One column a decision on the live benchmark engine's clock.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 55: Tensor Principal Modes · Class S

The principal modes of the telemetry (its matrix decomposed).

- **Evidence and state.** Class S (the harness's record, realms/harness.py); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawModes, tEig` → the Python `realms/harness.py`, `realms/compass_arm_v5.py`, `docs/engine/export_harness_trace.py` → the C++ `cpp/src/governor.cpp`, `cpp/src/core.cpp`, `cpp/src/nervous_system.cpp`; held equal by `docs/engine/check_records.py`.
- **Moves.** Every decision: the line across each bar is that decision's own motion in the mode; the first mode's line takes a point, a ring at its head.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 56: Service Level

The share of each half minute's requests answered inside the 500 ms line, native beside Omni-Compass, through the official run chosen in section 4a.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra) over the service's histogram; series `slo:sli_error:ratio_rate5m`; on a running system: `1 - slo:sli_error:ratio_rate5m`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 57: Error Budget Burn

The requests over the 500 ms line counted up since the repetition began, native beside Omni-Compass: each side's error budget burned.

- **Evidence and state.** Class L (the official run's request log, SHA-256-checked); replay.
- **Feed.** SLO recording rules (sloth, pyrra); series `slo:error_budget:remaining`; on a running system: `slo:error_budget:remaining`.
- **Wired.** This page's `drawSankey` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Half minute by half minute through the official run; its newest value printed at the head.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

### Monitor 58: Repetition Gauges Against Native

Every gauge of the repetition replaying in section 4a against native's 0 line: GAIN to the right in green, LOSS to the left in red, its side the run's own reading.

- **Evidence and state.** Class L (the official run's own gauges); replay.
- **Feed.** the build (the repository's tables, no live feed: a recording rule would compose the layers' ratios).
- **Wired.** This page's `drawRadar` → the Python `docs/engine/export_runs.py`, `tools/live_reps.py`, `scripts/raw_archive.sh` → the C++ none: the live software's own measurements, played back from their SHA-256-checked files; held equal by `docs/engine/build_live_engine.py`.
- **Moves.** Each gauge of the repetition replaying in section 4a.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white); Tune Dial: the max (every muscle to its own limit) or the tune-down (never more than native); Demand: ×0.25 to ×2 of the day's own demand, both arms alike; Noise: σ of the demand's noise, one draw a muscle a decision, both arms alike; Sense Delay: decisions added between what a muscle does and what its controller reads, both arms alike; Faults: a surge, half the machines lost, a sense blind, a security hold, on the chosen body part; Speed: 1×, 4×, 16× or 60× of the engine's clock; One Decision: step the engine one decision while paused.
- **How to read it.** The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.
- **What to do with it.** The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs.

## 5g Master Switch Wiring

**Controls.** Live: the switch on this monitor is the kill switch of section 1.

**The page, in its own words.**

**Master Switch and Kill Switch**

One switch for the whole organism, as the repository builds it (omnicompass/master.py, tools/omni_switch.py). It sits at the top and holds the brain's outputs. With it OFF, nothing the brain computes is pushed or pulled into any muscle, and every muscle runs on native's own controllers, which never stop. On a real machine every governor exits at the switch; on this page the brain keeps reading the native body in shadow, so its monitors keep moving, and nothing it computes leaves it. No monitor is switched off: every Omni-Compass side follows native, drawn in native's colour. Every governor on this page is registered with it and obeys it at once. The live organism hands every setting it held back to native's own controller and reads each one back. Every record's Omni-Compass side, and every playback, trace, table, board and grid, reads native's own. Native's own controllers are never switched, so native's side never moves with the switch. Every section carries the same switch in its controls bar; pressing any one of them throws this one.

**Its monitors.**

### Monitor 12: Master Switch and Kill Switch

The switch above the brain: ON, Omni-Compass governs every wired muscle; engaged, every setting is handed back to native's own controller at once and every Omni-Compass side on the page follows native.

- **Evidence and state.** Class S (the page's port of the master switch; the real one is omnicompass/master.py); live.
- **Feed.** tools/omni_exporter.py (the governor's own audit, Prometheus text format); series `omni_master_switch`; on a running system: `omni_master_switch`.
- **Wired.** This page's `drawMaster, masterSet` → the Python `omnicompass/master.py`, `tools/omni_switch.py`, `omnicompass/nervous_system.py` → the C++ `cpp/src/nervous_system.cpp`; held equal by `tests/test_master_switch.py`, `tests/test_cpp_twins_parity.py`.
- **Moves.** Every decision: the brain's pulse and the work flowing down to every muscle; the switch acts at once.
- **Knobs.** Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** The wiring from the top down: the master switch above the brain, the brain above the organism, the organism above every muscle, and native's own controllers under every muscle, never switched. The switch's state is the word on it: ON in green while Omni-Compass governs; engaged, the switch red and OFF in white.
- **What to do with it.** Press the kill switch only for security: it is instant, every setting goes back to native and is read back. Watch the governors' table beside it: every governor on the page says OFF and what it handed back.

## 5h Specification and Mathematics

Items 1 to 5 and 8 are the engine’s code and run in every live view (the official-run playback of 4a and 4b replays records and runs none of it). Items 6 and 7 as written (the compass law on each muscle, the plug’s lever) drive the stress-test model. In the harness views the max and the plants’ own overrides take their place. The live controller runs the compass law on the service, as section 4c shows.

**Controls.** Live: five of the brain's six state variables (E, U, I[U], S, B) and the nerves' calm below are read from the live benchmark engine every decision, beside the equations that give them.

**The page, in its own words.**

**Stress-Test Model Equations · Class S**

**Reads and Sets by Part**

**Engine Code Provenance**

The six-state engine, its constants and RK4 integrator, the assimilation, push and ρ*, the four nerve scalars and the organ thresholds, the compass law and the verdict in words are ported from omnicompass/core.py, adapter.py, nervous_system.py, compass_law.py and verdict.py at commit c8ba7775d. All are inside the fingerprint of the engine that stands, omni-v23: omni-v18 to omni-v23 left core.py, adapter.py, compass_law.py and verdict.py as omni-v17's bytes, and omni-v21 changed nervous_system.py and added immune.py for the immune rule, which the page's reflex block ports from those two files; adapter.py carries omni-v16's clocks in seconds, which the page's brain ports (a = 1 − (1 − 0.339)^k and macro_dt = 0.1·k for k = period/60 s; at a 60 s period every value is omni-v15's; checked against the Python at 10, 15, 60 and 120 s with no grant differing) and omni-v15's clear-time gate on the power-cap request, which the port does not compute (it ports the states, the push and the headroom), and the others are omni-v12's bytes. omni-v9 added omnicompass/student_t.py, and the page carries its Student t too, computed by bisection on its own distribution and rounded to three decimals as the printed tables are. omni-v10 changed only the CityLearn wire's glide, omni-v11 only the Kubernetes governor's blind-reading guard, omni-v12 only that governor's hold on a refused raise, and omni-v13 only the governor's conveyance on a shared host at its top, omni-v14 only the governor and its muscles: a muscle left native, the operator's commands without a shell, and omni-v15 the brain's power-cap request through the line's own clear time, with the card governor handing the brain its clear flag. Checked against the Python on seeded inputs (docs/engine/check_live_engine.py): 8,000 decisions of the governor (state, push, ρ*, κ, h, σ, ν, calm), 48,000 organ grants, 4,800 compass forces, 300 verdict intervals and 400 full verdict trials. A build passes only when the largest difference is under 10⁻¹², no grant and no verdict differs, and the Student t is equal on all 500 degrees of freedom checked. And against the C++ twin of the core (cpp/src/core.cpp, compiled by the check with docs/engine/cpp_core_probe.cpp): 2,000 seeded states, the derivative and the RK4 step within 10⁻¹² of each other. The check prints its own measured differences in each build's report on GitHub. The harness views are not ported: they are the harness’s own record, made by its code.

**Realms Harness and Stress-Test Model**

Realms Harness. The default body: the sixty muscles are one organism of realms/harness.py. Each is a plant of realms/plants.py: machine pools under their autoscalers, cooled zones, batteries on their lines, motion axes and process loops. They are coupled through their heat and their power, under the climb (1 2 3 2 3 4 …), for 240 decisions of 15 s. Omni-Compass is the max of realms/compass_arm_v5.py with the body’s bone, its twins and the muscles’ cards; at 80% the brain goes silent and the lease walks every setting back to native over 24 decisions. Recorded on seeds 3000, 3001 and 3002 (runs A, B and C) by docs/engine/export_harness_trace.py; the page replays the record. Each muscle alone is the same harness one muscle at a time, as run_muscle_arm runs the preregistered muscle table: under the line (work waiting at the start), the max with the muscle's own twin, and the lease after 80%. Each muscle's decisions are laid on 240 frames. A frame shows the last decision it covers, and reads over the line if any of them was. In that harness the brain’s state is computed from the body’s aggregate, as a governor reads it, and shown; the max itself acts muscle by muscle. Stress-Test Model. A model drawn for this page so the body can be stressed by hand (a surge, a blind sense, a security hold, the kill switch), evidence class S; like every view it runs native and Omni-Compass, side by side, on the same demand. Sixty muscles named from the 1,107-muscle catalog (twelve each from the spine and the four realms), each a capacity lever with its own response time τ and sensing delay, under an HPA-style native controller (target 0.70, 10% tolerance, five-decision scale-down window). Demand climbs 1 2 3 2 3 4, surges, eases and idles over 360 steps of 15 s, 90 minutes of the plant, the same for both arms. The lever rules that turn F into a write are this page's, written out above. Under the max: never below native, and lifting off hands back toward native. On the tune-down: never above native, and below it only with the organ's grant and the release gate.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 5i Failure Modes and Controls

**Controls.** Live: every way below that the live benchmark engine can be put through has its own button, and the response plays on the console (section 3c), native beside Omni-Compass.

**The page, in its own words.**

**Failure-Mode Register**

**Unjudged Resource Costs**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## 5j Self-Governed Rendering

Native is the browser's own loop: every chart on screen drawn on every frame, and when the frame overruns, whole frames dropped. Omni-Compass is the same loop with the engine's own compass law governing it (omnicompass/compass_law.py, ported here and checked against the Python). The reading is the time between frames, the band two frames wide with its center one frame at 60 Hz. The two arms take turns in paired windows of three seconds on this same page, on your own machine, and are read by the three-run rule's interval (class L: this browser, live; a reading of this page, never a benchmark of record).

**The page, in its own words.**

**Native**

**Omni-Compass**

**Inter-Frame Interval by Window**

**Paired Window Measurement**

**Its monitors.**

### Monitor 62: Inter-Frame Interval by Window

This page's own render loop governed by the compass law: the frame time against its line, native (no governor) beside Omni-Compass.

- **Evidence and state.** Class S; live.
- **Feed.** this page's own clock (no exporter: the page measures itself).
- **Wired.** This page's `drawSelf` → the Python `omnicompass/compass_law.py` → the C++ `cpp/tools/engine_runs.cpp`; held equal by `docs/engine/check_live_engine.py`.
- **Moves.** Every frame: this page's own frame time under the compass law.
- **Knobs.** Frame Load: +0, +8 or +16 ms burned inside every frame of this page; Kill Switch: Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white).
- **How to read it.** This page's own render loop governed by the compass law: the time between frames against its line, native (no governor) beside Omni-Compass.
- **What to do with it.** Load the page with the frame-load knob and watch the governor shed chart frames to keep every frame inside its line.

## The page's Appendixes

## A Title Page and Build

**The page, in its own words.**

A live monitor of the Omni-Compass engine and of every benchmark GitHub has run on it: each run played back from its own SHA-256-checked files, each model run by the repository's own code, so the engine can be watched moving instead of only read. Two sides everywhere, and only two: Native, the whole system running by itself, and Omni-Compass and native, the same system with Omni-Compass on top of all of it. On this page Omni-Compass is never run by itself: it always sits on top of a native controller. Beside this title stand the owner's two pictures, each with the engine's live marks over it. The engine that stands is omni-v23 (`docs/OMNI_V23.md`); its road back to omni-v18 is in the disclosures (appendix G), and each earlier engine has its own page (docs/OMNI_V<n>.md). The engine that stands still carries the code omni-v18 and omni-v19 added to run Omni-Compass by itself (its own orchestrator and a pod muscle of its own); it is an opt-in start flag outside the factory tune, and this page shows none of it. Its only modelled record read LOSS: the record of 24 October carried that third arm, Omni-Compass by itself, and it read LOSS in all three of our runs on work and on muscles over the line in eight organisms, 32 rows (on omni-v19, digest 36ee67284c035235, the record's own engine, never read as the engine that stands; class S); the arm is off this page, and its record is kept whole in `docs/history/SCENARIOS_30_2026-10-24.md`.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## B Reading Guide

**The page, in its own words.**

**Monitor Wall Legend**

Each monitor carries its signal and its word (green GAINING, low in its band with room to climb; yellow STEADY, inside its band; red REDLINING, at the top of its band, blinking red and black; red OVER THE LINE, past its band, blinking red and white). The control panel (section 1) holds every switch and knob: the kill switch, the heartbeat (10, 15, 30, 60, 90 or 120 s), the sweep over every beat, the active profile with Restore factory profile and Return to native, the actuation and each route's bill, the mechanism's own knobs, the plant's conditions and faults, the twenty scenarios, and one breaker per monitor. The engine runs itself: its own mathematics decides every beat; the knobs show the mechanism, they never have to drive it.

Five blocks: 1, benefit and organism (twelve monitors, three rows of four on a laptop); 2, real runs on GitHub; 3, brain and mechanism; 4, clouds, chips, orchestrators and scale; 5, proof and telemetry. Each block reads left to right, then the next row. A click on a tile goes to its monitor. The monitor list (appendix E) gives each monitor's source and feed.

The same canvases the sections draw, copied small four times a second; nothing is drawn twice from different data. The page's own governor (section 5j) leaves a monitor resting while it is off screen, so while this wall is in view the resting monitors are drawn in turn, one a frame, each through its own drawing code; every monitor is drawn once as the page opens, so no tile waits for its section to be scrolled to. Two monitors that sit side by side in their section, native beside Omni-Compass, sit side by side on the wall too: a pair never splits across two rows. Each tile's head is its number and its title in capital letters, then its section and its state (live, replay, from the records, a model, or awaiting its run). A tile with the accent border is a monitor on screen now.

**Organism Ring Guide**

**0 Monitor Wall**

The wall's light count is the one count the breakers, the section signals and the dock print.

Redline Reflex. At the top of its band Omni-Compass pushes at once; where a muscle stays over its line three decisions, stuck, and native's twin reads lower by more than 5%, it hands the muscle to native for 10 decisions (doubling for each hand-back in a row, up to 160), and takes it back only when its side is under the line and lower than native's by 5%; where native is not stronger it stays, because redlining less than native is still a benefit against native. Every light still carries its red: if a muscle redlines on Omni-Compass's side and the reflex cannot stop it (a fault, a bug), it is seen at once, and the kill switch hands everything back to native in the same instant. The rule entered the engine with omni-v21 and stands in the engine that stands, omni-v23, in its immune system, knob by knob (omnicompass/immune.py, the same file in both fingerprints, its C++ twin cpp/src/immune.cpp, proven alike on 200 seeded scripts, and the nervous system's native_hold; on Kubernetes each service's autoscaler target, native's twin the operator's own target), beside the SLO reflex and the pod reflex of the Kubernetes governor (omni_controller/controller.py); this page's live model (class S) applies the same rule, with the engine's own numbers, to every muscle it draws.

Green, GAINING: low in its band with room to climb, or a GAIN. Dark, AWAITING: the run that fills it has not landed. Grey, NO LINE: a monitor with no line to cross (a bill, a count of runs, a digest check) or no reading yet; neither is ever counted green. Yellow, STEADY: inside its band, or level with native (a change under 0.5%). Red, REDLINING, blinking red and black: at the top of its band and holding there, or a LOSS row. Red, OVER THE LINE, blinking red and white: past the top of its band. Native is orange everywhere, Omni-Compass blue; red is never a side, only the alarm. A monitor that draws two sides carries three lights in its button: native's, Omni-Compass's, each read from its own side on the same load, and the reading between them now by the key (GAIN green, STEADY yellow, LOSS red), so the moment one side turns a colour the other does not is seen as it happens. REDLINING comes before the line: a gauge within 3% of the top of its band, or whose slope over its last readings reaches it within 3 readings. A needle that falls is not a LOSS and one that rises is not a GAIN: each light reads what its gauge is for (a wait that falls is GAINING; work that falls is not). Click a light for its reason; a light turned red by the knobs goes back with the factory tune. The three-reading projection is the light's own. The brain's law acts on the position inside its band and damps on the position's rate of change (K[D] × v, omnicompass/compass_law.py), with a fail-up at the band's 95% wall; it projects nothing ahead (section 3). Each light reads the series its monitor draws, and a light fed by our own models says so (class S); hover it for the reading.

**1 Control Panel**

Fuse Box. The first row is the master switches: each acts on the whole page at once, through the same code as the console and the dock, both sides alike (the kill switch hands everything back to native; the dial, the body and the time). Under it, seven tabs: Drive (the plant's conditions and faults, the heartbeat, the profile with its actuation, its contract and each route's bill), Mechanism Knobs (the engine's own constants, one group at a time), Scenarios and Injection Grid, Monitor Breakers (one per monitor: its light and word, green GAINING, yellow STEADY, red REDLINING, red OVER THE LINE; ON runs it live, REST stops its drawing; a way to it), Prometheus Metrics (the live model as a Prometheus endpoint, the same series section 3b exposes), Commands (the request a running governor would take for each press) and All Tabs (the whole panel at once). Every switch is logged with its decision; Back to the factory tune puts all of it back.

Mechanism Knobs. Not the plant's conditions of the Drive tab: these turn the engine's own equations while it runs. Each knob is a constant of the brain (omnicompass/core.py), the compass law (omnicompass/compass_law.py), the governor's law (omnicompass/adapter.py, nervous_system.py), Omni-Compass's push, lift-off and tune-down on each muscle, the model's native controller, or one muscle's body. Turned, the next decision of the live stress-test model is computed with it, on Omni-Compass's side; native's controller knobs move every native controller, the one under Omni-Compass on native too. The harness replays recorded positions, so turning a knob moves the live benchmark engine to the model. A knob turned from the factory turns violet; ↺ puts that one back; Back to the factory tune puts every one back. The monitors (the strip, the rings, the phase plane, the brain's state, the status board) show the mechanism of action as it changes.

The compass law, the push, lift-off and tune-down, native's controller and every muscle's body move the muscles at once. The brain's four pieces move its own state (E, U, I[U], S, B on the brain's monitors) and its grants: at the max every organ may add capacity unless a security hold stands, so the brain's calm acts through the give-backs; at the tune-down the four pieces move the muscles too.

Manuals. The Live Benchmark Engine Manual reads this page top to bottom: how to read, operate, tune and watch it, native beside Omni-Compass, chapter by chapter in the page's own order, and, in its last appendix, the page word for word, every section, every monitor under its number and every knob, written from this page at every build. The Operator's Manual wires and runs Omni-Compass on a stack; the Owner's Manual holds the whole mechanism, its mathematics, its source and every result. Each carries the notice, the LICENSE, the NOTICE and `DISCLOSURES.md`.

**2a Scorecard**

Each row is one way to run a workload, against native alone on the same work.

**2c Benefit Board**

Every benchmark's measured effect in one board, native against Omni-Compass on top of native, by domain and by gauge family, and the Omni index that weighs them together. The whole organism composed from these same tables is in section 5d; every table, every muscle and the grid in full in section 5e.

**2e Status Board**

The tiles, in order: the switch and the engine; the live organism's signals, native beside Omni-Compass, on the four signals of site reliability practice (errors, traffic, latency and saturation), here the muscle-decisions past their line, the work done, and the stand-in each body has (the work waiting in line on the live model, the electrical power drawn on the harness), each named on its tile, with the injected faults beside them; the three-run tables and the verdict guard; GitHub's runs, the clouds and the age of this page. Under the tiles, every alarm and watch item, worst first.

**3a Live Organism**

The system rendered as an organism: each node is a muscle (one controlled actuator) and each ring its operating range. The left instance runs under its native controllers alone; the right runs the same controllers with Omni-Compass's brain, nerves, heart and immune system supervising them.

Every view is run twice on the same body, the same load and the same seed: native (left), then Omni-Compass (right). "One organism" is the sixty muscles in one body: the whole native organism on the left, the same organism with Omni-Compass on the right; "each muscle alone" runs each muscle native and then with Omni-Compass, one at a time. The counters under each ring and the scoreboard (section 3f) give both arms and the difference. Inside one organism the bone, the power and cooling the whole body shares, holds most moves back. A dashed white ring marks every muscle that differs between the two sides at that moment; the counter under each ring counts them.

Every room and every machine pool has a native twin: the same muscle under its own controller, on native's heat and load, the body's memory of healthy. A room that stands warmer than its twin is inflamed. Where its own knob can cool it, it is cured on the spot. Where it cannot, it sends the whole body a signal, its heat debt, like a cytokine calling for help. The other muscles answer: the machine pools give back what Omni-Compass added until the room stands no warmer than native's. The skeleton (the bone: the power and cooling lines the whole body shares) grants nothing it cannot carry. A cooling setting is walked back, never snapped. A pool never loses a machine its queue needs, a battery is timed for its line, and no sense is locked.

Under the max a muscle is moved only where it has room above native. A muscle already at its limit on native (— of these sixty) is left native by design. In these harness views the max acts muscle by muscle and the brain at the center reads the body without steering it, as in the realms harness itself; section 4c shows the live controller, where the brain's rules run every decision.

**3c Control Console**

Runtime parameter control and fault injection on the live benchmark engine: load scaling, noise injection, sensor latency, capacity loss, a demand surge, a sensor blackout, a security hold, the dial, and the kill switch. Every control is applied to both arms identically; the response is plotted per decision, native beside Omni-Compass.

The engine these knobs turn is the engine's own mathematics running in this page: the brain (omnicompass/core.py, integrated by RK4), the compass law (omnicompass/compass_law.py) and the verdict (omnicompass/verdict.py). docs/engine/check_live_engine.py proves the port equal to the Python and the C++ on every build. It governs the stress-test model's sixty muscles (class S), each on top of its own native controller. Every knob acts on both sides at once, the same demand, the same draw of noise, the same lost pool, so the one difference left between them is Omni-Compass. The knobs move the live benchmark engine here and in sections 3a, 3b, 3e to 3g, 3i and 5h, and the kill switch and the frame load also move this page's own renderer (section 5j). A recorded run (the benefit board, the chips' and Kubernetes' replays, the official runs) is a record: no knob rewrites it.

**3d Heartbeat Dial**

Each beat stands beside native with what it buys (the reads of the cluster a day) and what it costs (the governor's own processor, and every service row read against native and against the main engine's 60 s).

**3e Control Cycle**

One control cycle traced end to end at reduced speed: the sensed inputs, the brain's decision, and the actuator (muscle) it wrote.

**3f Phase Plane and Scoreboard**

The phase-plane state of every muscle (its position and velocity in its band) for both arms at the same instant, with the running scoreboard.

The plane is a phase portrait, the picture control engineers use for a system's state. Across is where each muscle sits in its band: p is 0 when calm, 0.5 at the center and 1 at its line. Up and down is how fast it moves there (v, per decision). A muscle at rest sits on the middle line. One climbing toward its line moves up and right, and past the right edge it is past its line. Native is on the left and Omni-Compass on the right: the same muscles at the same instant, one dot each. In the realms harness each muscle answers to its own rule, so no single field is drawn. In the stress-test model the shading on the right is the force the compass law would apply there: the add force gives capacity and the hand-back force returns it. Past the 0.95 wall the law fails up at once. Under each plane the same instant is written in words.

**3g Brain State**

The brain's six state variables rendered on their potential-energy landscapes: a state resting at a minimum is stable; a state driven toward a maximum is under load.

The wells draw the same state the cycle panel (section 3e) prints. Each ball is a live value of the engine's brain, integrated by RK4 every decision. In the stress-test model the brain's push and target feed the body's levers. Native has none of this: no state, no memory of need, no stress, no tide; each controller sees only its own reading, one to three decisions late.

**3h Verdict**

Before a knob moves one step past native, the step runs as a trial: costs at native first, then at the step. The engine that stands reads the change exactly as a report reads a row, on the log of each cost, with its 95% interval. The lab opens wired as the shipped Kubernetes controller is wired, on the noise the real runs measured.

**3i Dashboards**

The dashboards draw the same live benchmark engine the ways the industry draws a system: a board of panels, a host map, a graph of one series, an event stream, a cluster console with a button on every workload, a one-line diagram with its breakers, a wall of numbers, the cost of each body part, and Omni-Compass's own form, the two-way pipeline that reads, decides, writes and reads back. On a phone each drawn form also writes what it shows as plain lines under the drawing.

A muscle is any machine, service or controller Omni-Compass can read and set; native is the system as it runs without Omni-Compass; a write is one setting Omni-Compass changed; read back means it checks the setting landed; the lease walks every setting back to native after a crash; the kill switch stops Omni-Compass at once, for security. Every benchmark puts Omni-Compass on top of a native setup and reads both sides by the same key.

**4a Kubernetes Run Playback**

Playback of the official benchmark runs from their archived raw files: the native cluster and the Omni-Compass cluster under identical load, in 30-second bins, every file verified against its run's SHA-256 manifest.

Native (the whole cluster with everything it ships with, everything but Omni-Compass) against Omni-Compass, the same load, the same second, each file's SHA-256 matched before a byte is drawn. The tiles, the candles, the heatmap, the bars and the governor's ticker all move together with section 4b (pick a benchmark, a run or a repetition in either place). Every word is the run's own reading, never one drawn from the stream.

**4b Repetition Telemetry**

Per-repetition telemetry in 30-second bins, with the run's receipt and each repetition's score from the repository's own scorer.

Native and Omni-Compass, repetition by repetition, played in 30-second bins. Every Kubernetes repetition is scored by the repository's own scorer (tools/live_reps.py); where a run holds its own scored summary, the scorer's mean over its repetitions equals it (the count is in section 4b).

**4c Controller Decision Trace**

The shipped controller's decision trace, replayed from its own audit log one decision at a time: its inputs, its choice and its writes.

**4d Cloud Providers**

In a cloud the bill is read beside the work: whether the same bill buys more work with Omni-Compass on top. Each provider's card lists its four test sets and their status.

In a cloud, Omni-Compass shows two things: that the engine holds on the cloud's machines as it does on site, and the work per dollar: more work for the same bill, never a smaller bill as the aim (the founder's words of 31 October). From 31 October every cloud set runs the whole engine at the max on top of the cloud's own autoscaler (the founder's order of that day: no hard rule): the governor senses the service, moves its pod target inside the autoscaler's cover, conveys the processor, and parks a machine the cloud already made, after its own trial, waking it on a breach; it asks the cloud for no machine itself, and the cloud's autoscaler alone adds machines. Every gauge is read against native by the one key, the bill beside the work it bought. A bill that rises is the cloud's tune falling out wrong: it is fixed in our models before a set at the max starts, and Azure's queue holds its sets until then. Until 31 October every cloud set ran at the tune-down on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped), and those sets stand as their own record. Azure, Google Cloud and Amazon run the same tuning, mechanism and harness.

A cloud is the wire between the software end (the owner's programs, Kubernetes and the open-source orchestrators, managers and autoscalers that carry the work) and the hardware end (the bare metal: the GPU chips, the Linux racks, the data center, on-site or off-site). Omni-Compass can live in all three places: on the software end, on the cloud's wire, and on the bare metal. The wire makes no benefit of its own. On the wire alone (every cloud run on this page so far: Omni-Compass at the tune-down on the machines only, the pods exactly native's, the cloud's rule until 31 October), all it could do was park machines the cloud's own autoscaler already made, after its own trial, so the most those runs can show is a small cut in the bill of the wire. From 31 October every cloud set runs the whole engine at the max on the cloud's cluster, so its receipt shows that the engine holds there as on site and how much of the software end's gain comes through the wire, read as work per dollar beside the bill. It cannot show the energy and throughput gained at the bare metal, because the provider's machines are not a tenant's to meter. Omni-Compass on the software end (the front end) and on the bare metal (the back end) reaches gauges a cloud run cannot. A cloud provider that runs Omni-Compass on its own back end would see those gauges on its own GPU chips and Linux racks; no tenant can meter a provider's back end, so this page claims it only as the same mechanism measured on hardware we can meter (section 4f), never as a measurement of the provider's machines. The three places compose into one organism and one bill in section 5d.

The company's own expectation, not a measured result (24 October): about 3 to 4% from the front end, 2 to 3% from the back end, about 5% from the two ends together, and 1 to 2% from the wire alone, as a smaller bill or more work for the same bill; the readings of each place stand in the place table of sections 4d and 5d; where a measurement differs from the expectation, the measurement stands.

**4e Orchestrators and Governors**

These are the governors and orchestrators that sit between the work and the cluster: batch schedulers and job queues, multi-cluster governors, the default Kubernetes scheduler, GPU and edge orchestrators, and the rightsizing controllers. Each has three runs, and every row is shown.

**4f GPU and CPU Hardware**

The chip is the far end of every stack: there the max would ride each card's own limit, and every watt it takes is power given, shown beside the work it buys.

Each stack is run twice on the same load and the same seed: native first, then Omni-Compass. Left is native, right is Omni-Compass, and every table gives both columns and the difference. The clouds are section 4d and Kubernetes sections 4a to 4c; every muscle of the catalog, the seven organisms and the three-run tables are in section 5e.

**4g CI Pipeline**

The canvas and the table list every GitHub Actions workflow run in progress or queued at build time. The hardware and cloud runs, with their terminal status, are in sections 4d and 4f; every run on the engine that stands that terminated without a measurement is raised on the status board (section 2e).

**5a Python Runs and Monte Carlo**

The Python's runs, the C++ harness's and this page's, run by run: the jump generator's set GitHub ran in the Python (its run linked), the same draws run through the C++ harness on the engine's C++ twins, and the same set recomputed here by this page's own port of the engine as the page opens; every receipt compared three ways, one SHA-256 digest each, and the digest of the draws themselves; and the Python's 500 scenarios a seed replayed from its own record with every trace hash; and the Python's Monte Carlo of the engine's core, 500 runs each from step 0 through the fourth-order Runge–Kutta step, 20 macro steps of 10 micro steps, native beside Omni-Compass, into the basin, held and certified, with every set the jump generator draws here held to the Python's digest.

**5b C++ Twin**

The engine is written twice, in Python and in C++, line for line. Every time this page is built, the Python's own runs are fed into the C++ as its input, and the C++ answer is set beside the Python's, number by number. Where they are the same to the last digit, the two are one engine. Where a part runs in Python only, the list Python-Only Components names it.

**5c Scenarios and Injection Grid**

The ten organisms (the spine; the four realms; the four stacked; the whole tower; the orchestra; this page's own sixty-muscle organism; and the whole organism in its three places), each run two ways: native alone, and Omni-Compass on top of native (the factory tune).

Injection Grid. One batch of the Python's Monte Carlo injections (tools/engine_runs.py: base B, injection k drawing seed B + k·0x9E3779B9 mod 2³²; the C++ engine runs the same seeds to an identical digest, section 5a) runs through every organism the harness runs (the nine organisms of cells 1 to 9, each with a plant; the whole organism is a composition of measured tables and takes no injection), each native and with Omni-Compass on native, and through each of the fourteen governors and orchestrators sitting on the same organism (the third arm): the governor on the organism, and Omni-Compass on top of the governor. Every cell is the one batch cut down: its 500 runs, of which 100 runs are the first 100, 10 the first 10 and 1 the first; and in each run a stack of 500 organisms, of which 100 are the first 100 copies, 10 the first 10 and 1 the first (copy c of run k on injection k + c, mod 500). A click on 100 shows those 100 and no others; a cell whose runs × organisms pass 500 uses an injection more than once: the organism axis is a resampling of the same 500 injections and adds no independent evidence, so the cells at 500 organisms read as the cells at 1 do. A cell's word is one batch's (one run in the key's sense), its injections within that batch, never "our runs". Each run's change against its reference is read over its 24 blocks of ten decisions, and the cell's word by the key over its N runs (tools/readings.py three_run_reading, the 0.5% floor). The page re-hashes the record's cells and recomputes every cell's mean from the runs' means; both checks are printed under the batch.

Governors in the Injection Grid. In our models each governor is the body of the catalog muscles that stand for its knobs (tools/run_orchestra.py, the mapping of tools/governors_page.py), run on the organism's clock on the same injections, each under its own native controllers; Omni-Compass on top of the governor governs both bodies. The governor's body does not reach the organism's own muscles, so its way reads its own muscles beside the organism's.

**5d Whole Organism**

Omni-Compass is wired into every piece of a stack through its own two-way plug: the software (the cluster: Kubernetes, its add-ons, its governors and orchestrators; and the services on it: the pools, the consumers, the caches), the bare metal under it (the chip's power limit and clock; the machine's kernel and its own meter) and, where the stack is rented, the cloud that bills the machines. A stack is bought one of two ways: on-site bare metal, the software on the owner's own bare metal (software × bare metal, no cloud); through the cloud, the cloud's build, its bare metal at the back end and the software (cloud × bare metal × software), with the cloud as two pieces beside it (cloud × software, the back-end bare metal left to the provider).

Every piece's benefit is added into one collective reading, gauge by gauge (work, the 95th percentile response, machines, energy, the bill), with the receipts under it: what native spent, what Omni-Compass spent, and the benefit, in the units each table measured. The repository composes the layers in one place, tools/whole_system.py, which writes `results/WHOLE_SYSTEM.md` from the tables that stand: each layer measured against its own native with the layer under it as native runs it; a gauge's ratio oriented so that above 1 is a GAIN at every layer alike; the layers composed by the product law, R(g) = ∏ℓ Rℓ(g), log R = Σℓ log Rℓ (for small benefits the product is their sum), every interval carried (the exact Student t per run; A, B and C pooled by inverse variance; the layers' variances added); two readings of the same numbers (every measured piece: everything measured enters with its interval; the strict reading, the index's rule: only what held the same way in all three of our runs, everything else exactly 1); and the separability assumption tested on the governors' four ways. Section 5d recomputes nothing from the tables: it regroups that file's layers into the two ways (docs/engine/export_whole.py), summing the logarithms of the layers a scenario stacks and adding their variances, as the file's rule composes any set of layers; the one number is the mean of the gauge logarithms, its 95% interval under the file's two bounds.

**5e Measured Effect**

Everything the board in section 2c stands on, from the organisms down to the single muscle: the seven organisms under their three loads, all 1,107 muscles of the catalog one cell each, every registered benchmark still to run, the scale-out grid of copies and runs, and every three-run table in the repository with every row as it is written.

That board holds every benchmark's benefit in one place, as the repository's benefit sheet holds it (results/BENEFIT_SHEET.json), with the Omni index that weighs them together (`results/OMNI_INDEX.md`). The scale-out grid holds every organism at 1, 10, 100 and 1,000 copies, each at 1, 10, 100 and 1,000 runs, modelled and with the real cluster inside.

Seven Organisms Under Three Loads. The seven organisms of the catalog (the spine first, the base every stack runs on; the four realms; the four stacked; the whole tower), each run native and with Omni-Compass on top of native, under its own load, the climb (1 2 3 2 3 4 …) and work waiting in line; and the whole organism, the software, the cloud and the hardware stacked into one body (section 5d), composed from the pieces' own readings, native and with Omni-Compass on top of every piece: a composition with two arms, not an organism of the catalog. The orchestra, every governor's muscles as one body, is the eighth organism (section 4e). The monitor draws the seven from the realms table; the whole stack's two arms are section 5d's composition until the stacked run, preregistered in `docs/WHOLE_SYSTEM_PREREGISTRATION.md`, measures them in one run.

Open Register Slots. Every muscle in them (a legged robot's gait, locomotion_speed; a wind turbine's blade pitch, pitch_angle_limit; a mobile robot's travel speed, agv_speed and trajectory_speed) already runs, modelled, in the 1,107-muscle catalog and the seven organisms of section 5e, native and with Omni-Compass on top. A slot here is the next step for that kind of muscle: the same test on the outside world's own software (MuJoCo's Unitree Go2, NREL's OpenFAST, ROS 2 Nav2), each queued until its three runs land.

The 1,000 tier runs on GitHub's free runners only; paid machines stay at 100. Each bar and square carries its own word with its size and no sign; the raw change keeps its own sign, labelled raw.

**5f Telemetry Analytics**

The same telemetry analysed four ways: a three-dimensional tensor view, a difference matrix, a principal-component decomposition and Omni-Compass's own account of its run; the service level and error budget in SRE terms; and Omni-Compass answering the viewer's questions about itself from the page's own records.

The tensor fills in decision by decision as section 3a plays, and the same numbers are read three more ways: the difference between the arms, the body's principal motions, and Omni-Compass's own account of what it is doing. The official runs (class L) are read as an SRE reads a service: the service level, the error budget burned and every gauge against native; and Omni-Compass answers questions about itself, reading the page's own records through tools and turning the dashboard to a run.

**5g Master Switch Wiring**

One switch for the whole organism, drawn as the repository wires it: the master switch holds the brain's outputs; the brain sits above the organism; every muscle hangs under it with native's own controller under every muscle, never switched. Every governor of this page is listed with its state at the switch.

**5h Specification and Mathematics**

The component specification: every part, its equations and the source module that implements it, as the repository writes them.

**5i Failure Modes and Controls**

The failure-mode register: every known way Omni-Compass can fall short, the control that mitigates it, that control's coverage, and the residual risk where it does not reach. The second table: the resource costs the three-run tables report but do not judge.

**5j Self-Governed Rendering**

The page's own render loop is governed by the same compass law, measured on the client device, native beside Omni-Compass.

Each chart is a muscle whose knob is how many frames it waits between draws, and the reading is the time between frames. Below the band's center the pedal lifts and every chart is handed back to native, drawn every frame. Toward the line it pushes: the charts farthest from where you are looking wait a frame or more, so the frame itself stays inside its line. Every step is a trial run to its full measurement and kept only when the frame shortens; a step that buys nothing is refused and every chart handed back to native (the reflex rule: where a knob cannot bring a GAIN, it stays native).

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## C Problem and Answer

**The page, in its own words.**

**Problem, Answer, Proof, Limits and Protection**

**Industry Problem**

Demand Outrunning Capacity. Demand for computing is growing faster than the power, the machines and the budgets built to carry it. The International Energy Agency puts the world's data centres at about 415 TWh of electricity in 2024, around 1.5% of all the electricity the world used, and expects that to more than double, to about 945 TWh, by 2030, with artificial intelligence the largest driver. In the United States, Lawrence Berkeley National Laboratory counts 176 TWh in 2023, 4.4% of the country's electricity, and between 6.7% and 12% by 2028. The usual answer is to build more: more machines, more megawatts, more cooling and a larger bill.

Idle Capacity. Across the Kubernetes clusters Cast AI measured in 2025, the average processor was 8% busy and the average memory 20% used, read before its own automation was switched on. The organizations Flexera surveyed estimate that 29% of what they spend on cloud infrastructure and platforms is wasted.

Coordination Gap. In every realm (compute, AI and the cloud; physics, robotics and autonomy; energy, facilities and industry; distribution and specialized systems) each machine already runs under local feedback loops: horizontal autoscalers, firmware power and clock governors, building-management loops, battery-management systems, connection pools, servo controllers. Each loop is tuned on its own, against its own setpoint, with margins sized for a worst case. Four costs follow, and every operator pays them:

Reaction Latency. Reactive loops act on lagging, averaged signals. A Kubernetes Horizontal Pod Autoscaler recomputes its replicas every 15 seconds by default and damps its scale-downs over a 5-minute stabilization window; new pods then need time to schedule and start. Queues form before capacity arrives.

Static Over-Provisioning. Worst-case margins persist through the far more common nominal regime. The operating point sits well inside the safe region, and the headroom between it and the constraint boundary is paid for and rarely used.

Uncoordinated Coupling. Loops share resources: power, cooling, connections, memory, network. One loop's correction is another loop's disturbance: more web replicas saturate the database's connections; more cooling pushes a power feed toward its limit.

Gaps Closed by Hand. Operators close them with fixed settings, runbooks, alerts and on-call rotations, and the settings go stale as the load moves. That is safe, and it leaves the region between the operating point and the safe boundary unused nearly all of the time.

**Omni-Compass Answer**

Omni-Compass is a supervisory governor. It sits on top of every native controller and never in place of one; native keeps running underneath, always. It treats each setting a native controller already exposes (a replica floor, a power cap, a clock ceiling, a temperature setpoint, a pool size) as a muscle, and the whole stack as one body, the organism. Through a two-way plug, one wire in (the readings native already reports) and one wire out (the settings native already exposes), it reads every muscle, places each reading in the muscle's own band, from calm to its line (the limit it must not cross: a response time, a temperature, a feed's rating), and moves each setting one bounded, smooth step at a time. By default every muscle is driven up to its own limit, never past it and never below native; every write is read back; every give-back is tried in its own paired trial (the muscle with and without it, under the same load) and undone if the muscle loses by it, by the verdict's own rule: refused and undone where the 95% interval of its change in cost lies wholly above zero, or where the median or the mean of its logarithmic cost rises past the 2% allowance (omnicompass/verdict.py); a raise is held inside the muscle's own bounds and judged afterwards by the three-run tables; and wherever no gain can be brought, the muscle stays native. One brain governs the whole body: one shared calm, read from the brain's state over the whole organism, gates every give-back in every organ (an organ gives capacity back only while that calm stands at or above its own threshold, its service line is clean and its sense is fresh; omnicompass/nervous_system.py), while every raise stays inside the muscle's own band. Every muscle is judged on itself; a trade between muscles, one used less so another carries more, is not in the engine that stands. The aim: more work, faster, on fewer machines, with less energy. Where Omni-Compass takes more energy to buy more work or speed, that energy is shown beside what it bought, as power given, and never called a loss.

**Costs and Responses**

| Industry cost | Omni-Compass response | Judged by |
|---|---|---|
| Reaction Latency: waiting, queues and time over the line before capacity arrives | it reads every muscle on its own clock (on Kubernetes its full read of the state every 60 seconds at the factory, 15 seconds or faster where a person picks it on the dial, and its fast checks every 5 seconds) and moves as a reading nears its line, not after the line is crossed: proactive as well as reactive, like an immune system | time waited, missed or failed: a fall is GAIN, a rise is LOSS |
| Static Over-Provisioning: machines, energy and a bill paid for headroom rarely used | every muscle driven up to its own limit and never past it, so the machines already paid for carry more work; in a public cloud it parks only a machine the cloud already made, after its own trial, and wakes it on a breach: by construction it adds no machine and no pod of its own; the bills measured so far are single runs (read from the cloud ledger as the page opens), and no three-run bill exists yet | work done: a rise is GAIN; machines, energy and the bill: a fall is a cut, a GAIN, and a rise is power given |
| Uncoordinated Coupling: one loop's correction is another loop's disturbance | one brain for one body: one shared calm over the whole organism gates every give-back in every organ, and every raise stays inside the muscle's own band; a trade between muscles is not in the engine that stands | every muscle judged on itself, and the organism judged whole |
| Gaps Closed by Hand: settings retuned by hand, alert minutes, on-call | an autopilot: every write read back, every give-back on its own trial, every reason written to its audit; an alert minute on Omni-Compass's side is found and fixed, never accepted | the alert minutes, judged; the settings commands it wrote on its own, shown |

Section Map. Reaction latency: the organism live, every muscle's place in its band and the decisions past the line, native beside Omni-Compass (3a), and the shipped controller's decision trace (4c). Static over-provisioning: the benefit board (2c) and the clouds' bills (4d). Uncoordinated coupling: the whole organism (5d) and the organism's immune system (3a). The gaps closed by hand: the status board's alarms (2e) and the golden signals, the event log and the live metrics (3b).

Limits. It replaces no controller, and it creates no capacity a machine does not have: it uses the capacity already there, each muscle to its own limit. It promises no number on a system it has not run on: the only number that applies to a system is the one that system's own paired runs produce. The outside figures above are their authors' own, quoted for scale; none was measured, checked or endorsed by The Omni-Compass LLC, and none is a result of Omni-Compass.

Accountability. Every comparison judged pairs two arms, native and Omni-Compass on top of native, on the same machines with the same work (the governors' tests run four arms and pair them two at a time, section 4e). Every three-run table is run three separate times (A, B and C); the Azure runs read so far and the card's run inside the whole organism's composition are single runs, named as such where they appear. Every reading is one word, GAIN, STEADY or LOSS, decided by what the gauge is for (the key, appendix D); every result carries its evidence class (P a physical meter, L live software, S our own models, never shown as proof of hardware); and every row is shown, LOSS included. The governing rule is do no harm, in its one meaning (`DISCLOSURES.md`, section 3): the aim is an organism never left turning out less than native, nor less healthy; where a row of a three-run table reads LOSS against native (section 2d lists each, every one; a model's own LOSS rows, class S, stand in their own sections, the heartbeat dial's in 3d), the row stays, its cause is to be found and fixed (the LOSS ledger writes a cause beside those it has; the others read "not yet written"), and the test runs again on the engine that stands. The executive summary (appendix D) reads where the record stands, from the records on this page.

Outside Sources. International Energy Agency, Energy and AI (April 2025), its executive summary. Lawrence Berkeley National Laboratory, 2024 United States Data Center Energy Usage Report (December 2024), prepared for the U.S. Department of Energy. Cast AI, 2026 State of Kubernetes Optimization Report: a seller of Kubernetes optimization, reporting its own customers' clusters as they ran before its automation. Flexera, 2026 State of the Cloud Report (March 2026): a survey of 753 cloud decision-makers and users, the figure their own estimate. The Kubernetes documentation, Horizontal Pod Autoscaling: the controller's defaults.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## D Executive Summary and Reading Key

The Omni index, every real test weighed together, is read from its record as the page opens.

**Controls.** Live: the buttons act on the live benchmark engine; every number below is read from the records on this page.

**The page, in its own words.**

**Summary, Key, Terms and Examples**

**Executive Summary**

Every count and reading in this list is read from the records on this page when it opens (the three-run tables, the Omni index, the cloud ledger, the card run, the models' own readings, the realms table and the harness). The settings it quotes are their sources' own: the native defaults in its last line from `docs/engine/NATIVE_REGISTER.md`, the Azure sets' repetition cap from scripts/azure_queue.txt. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Reading Key**

**Defined Terms**

Each term is defined once; where it first appears on the page it carries the same definition, shown when pointed at.

The size is how far the gauge moved from native; the word says whether that move helped the work. Examples, read from the three-run tables on this page, appear here when they load. A miss is a decision where the work went over its line. The key is written once in tools/readings.py and stands at the top of the README, `docs/HOW_TO_READ_THE_RESULTS.md` and the manuals. GAIN, STEADY and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results; the underwriting senses explain the words and are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## E Monitor List

The list that goes with the wall: every monitor by its number, in the same order, with what it shows, the section it lives in, its evidence class and state, the open-source feed that would carry it live and its knobs.

**Controls.** Recorded data: the list is the page's own registry of its monitors, read when the page opens; click a number to go to its monitor, a section to go to its section.

**The page, in its own words.**

**Monitors by Number**

Motion Meter. Every monitor in view is photographed small once a second, as you see it, and its badge says whether it moved.

Every monitor is one canvas on this page; its number is its place in the wall's five blocks (docs/engine/monitors.json), and the wall (section 0) shows them in that order, left to right, then the next row. The feeds name the open-source exporters an operator's Prometheus and Grafana already run (node_exporter, kube-state-metrics, the NVIDIA DCGM exporter, Kepler, OpenCost, the governor's own tools/omni_exporter.py); the button in the control panel downloads the whole wall as a Grafana dashboard on those series (deploy/grafana/omni-compass-wall.json, written from docs/engine/monitors.json), beside the governor's own screen (deploy/grafana/omni-compass.json). A monitor the page draws from the repository's tables, or from its own clock, says so: no series carries it.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## F Glossary and Index

What every word on this page means, written from the repository's own pages (each definition names its source file), the organisms by their realms and families, and every muscle of the catalog (realms/catalog_v5.csv) with the organisms it sits in; the index sends each term to the sections where it is used. Built by tools/live_glossary.py into docs/engine/glossary.json.

**Controls.** Type to find a term, an organism or a muscle; click a letter to jump; each muscle opens to its family, its realms, its template, its knob and its wiring.

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.

## G Disclosures, Law and Contact

**The page, in its own words.**

THIS PAGE IS A LIVE TUNING ENGINE. THE BENCHMARKS ARE ONE TUNED ENGINE. Every knob, button and monitor on this page can be turned in real time: the heartbeat at 10, 15, 30, 60, 90 or 120 s, the dial between the max and the tune-down, the pedal, each muscle driven or left native, up or down, in or out, minus or plus, to see and produce the variations of the mechanism of action with native alone, with Omni-Compass on top of native, or both side by side. Like any engine, where turning the mixture, the intake, the exhaust, the firing or the pistons changes what it delivers, turning any knob can change every metric, either way, in any direction a tuner chooses: that range is the engine's versatility, one engine for many vessels, tuned many ways, for many outputs. What the page shows at any setting other than the factory tune demonstrates that range and is never a benchmark result. Every benchmark result is one engine at its one factory tune: the engine its table names, every benchmark run again on the engine that stands (section 4g). From omni-v17 the factory tune is chosen by a declared rule: of the tunes that harm no gauge against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on development seeds and read again on untouched ones (`docs/THE_TUNE.md`; `DISCLOSURES.md`, section 3). A tune other than the factory tune is the tuner's own, and its results are its own. No profile on this page is locked as the baseline: the factory profile is the one released with the engine, and reading every knob against it, one at a time, is the standing work of the sweeps (`docs/FACTORY_PROFILE.md`).

DISCLOSURE: REAL RUNS, A REAL ENGINE, NOTHING HARDWIRED. Every run played back on this page (sections 4a and 4b) is read from the raw files of benchmark runs executed on GitHub's own machines, each file checked against its run's SHA-256 list before a single number is drawn; every three-run table is read as the repository holds it, each naming its runs, and the raw branch holds their folders as they are archived (the status board, section 2e, marks each run whose raw files are archived). Every model view runs the engine's own code (the compass law, the brain, the verdict) live in this page, linked through software to the repository's Python and C++ and checked against them on every build. GitHub rebuilds the page from the repository whenever the engine, a model or a result changes, and every three hours: no number on it is typed in by hand, and when the repository changes, the page changes with it.

**Engine Lineage**

**Page Scope**

**Disclosures**

**Contact**

**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.


## Every monitor

| No. | Monitor | Section | Class | State |
|---|---|---|---|---|
| 1 | Benefit by Domain | 2c Benefit Board | L/S | record |
| 2 | Stack Composition | 5d Whole Organism | S (of P and L) | composed |
| 3 | Market Map | 2c Benefit Board | L/S | record |
| 4 | Benefit by Gauge Family | 2c Benefit Board | L/S | record |
| 5 | Native Organism Ring · Class S | 3a Live Organism | S | live |
| 6 | Omni-Compass Organism Ring · Class S | 3a Live Organism | S | live |
| 7 | Errors per Decision · Class S | 3b Golden Signals and Event Log | S | live |
| 8 | Throughput per Decision · Class S | 3b Golden Signals and Event Log | S | live |
| 9 | Latency Stand-In per Decision · Class S | 3b Golden Signals and Event Log | S | live |
| 10 | Saturation Stand-In per Decision · Class S | 3b Golden Signals and Event Log | S | live |
| 11 | Immune System · Class S | 3a Live Organism | S | live |
| 12 | Master Switch and Kill Switch | 5g Master Switch Wiring | S (the page's port of the master switch; the real one is omnicompass/master.py) | live |
| 13 | Data Pipeline | 4a Kubernetes Run Playback | L | replay |
| 14 | Governor Heartbeat and Lease | 4a Kubernetes Run Playback | L | replay |
| 15 | Response Time Candlesticks | 4a Kubernetes Run Playback | L | replay |
| 16 | Latency Heatmap | 4a Kubernetes Run Playback | L | replay |
| 17 | Throughput per 30 s Bin | 4a Kubernetes Run Playback | L | replay |
| 18 | Paired Repetitions | 4a Kubernetes Run Playback | L | replay |
| 19 | Repetition Telemetry per 30 s Bin | 4b Repetition Telemetry | L | replay |
| 20 | Quote Board | 2c Benefit Board | L/S | record |
| 21 | Native Cluster Trace · Class S | 4c Controller Decision Trace | S | replay |
| 22 | Omni-Compass Cluster Trace · Class S | 4c Controller Decision Trace | S | replay |
| 23 | Machines and Response Time · Class S | 4c Controller Decision Trace | S | replay |
| 24 | Orchestration Stack | 4e Orchestrators and Governors | L | record |
| 25 | Compass Band of the Followed Muscle | 3e Control Cycle | S | live |
| 26 | Scoreboard Strip · Class S | 3f Phase Plane and Scoreboard | S | live |
| 27 | Native Phase Plane | 3f Phase Plane and Scoreboard | S | live |
| 28 | Omni-Compass Phase Plane | 3f Phase Plane and Scoreboard | S | live |
| 29 | Double-Well Potential of U | 3g Brain State | S | live |
| 30 | Cubic Potential of Stress S | 3g Brain State | S | live |
| 31 | Bath Oscillator B | 3g Brain State | S | live |
| 32 | Native Controller Trace · Class S | 3g Brain State | S | live |
| 33 | Trial Costs and 95% Interval | 3h Verdict | S | live |
| 34 | Share of Trials Allowed | 3h Verdict | S | live |
| 35 | Body Parts on the Band · Class S | 3a Live Organism | S | live |
| 36 | Heartbeat Sweep · Class S | 4a Kubernetes Run Playback | S | model |
| 37 | Azure Bill | 4d Cloud Providers | L (metered by Azure) | record |
| 38 | Google Cloud Gate and Bill | 4d Cloud Providers | L | awaiting its run |
| 39 | Amazon Web Services Gate and Bill | 4d Cloud Providers | L | awaiting its run |
| 40 | Native Cloud Machines · Class S | 4d Cloud Providers | S | replay |
| 41 | Omni-Compass Cloud Machines · Class S | 4d Cloud Providers | S | replay |
| 42 | Road to a Result | 4e Orchestrators and Governors | L | record |
| 43 | Metered A100 Run | 4f GPU and CPU Hardware | P | awaiting its run |
| 44 | CPU Host Model · Class S | 4f GPU and CPU Hardware | S (model) until the run | awaiting its run |
| 45 | 8-Card GPU Node · Class S | 4f GPU and CPU Hardware | S (native model) until the run | awaiting its run |
| 46 | Stack Models · Class S | 4f GPU and CPU Hardware | S | model |
| 47 | Seven Organisms Under Three Loads · Class S | 5e Measured Effect | S | record |
| 48 | Catalog Muscle Matrix · Class S | 5e Measured Effect | S | record |
| 49 | Scale-Out Grid | 5e Measured Effect | S/L | record |
| 50 | Three-Way Run Check | 5a Python Runs and Monte Carlo | S (the engine itself) | live |
| 51 | Held-Out Scenario Replay | 5a Python Runs and Monte Carlo | S | replay |
| 52 | Engine Core Monte Carlo | 5a Python Runs and Monte Carlo | S (the engine itself) | live |
| 53 | Telemetry Tensor Cube · Class S | 5f Telemetry Analytics | S (the harness's record, realms/harness.py) | replay |
| 54 | Tensor Difference Matrix · Class S | 5f Telemetry Analytics | S (the harness's record, realms/harness.py) | replay |
| 55 | Tensor Principal Modes · Class S | 5f Telemetry Analytics | S (the harness's record, realms/harness.py) | replay |
| 56 | Service Level | 5f Telemetry Analytics | L (the official run's request log, SHA-256-checked) | replay |
| 57 | Error Budget Burn | 5f Telemetry Analytics | L (the official run's request log, SHA-256-checked) | replay |
| 58 | Repetition Gauges Against Native | 5f Telemetry Analytics | L (the official run's own gauges) | replay |
| 59 | GitHub Actions in Flight | 4g CI Pipeline | L (GitHub's own API, read at the build) | record |
| 60 | System Response per Decision · Class S | 3c Control Console | S | live |
| 61 | Inter-Frame Interval | 3c Control Console | S | live |
| 62 | Inter-Frame Interval by Window | 5j Self-Governed Rendering | S | live |

## Every knob

| Knob | What it does | Where it is |
|---|---|---|
| Kill Switch | Omni-Compass ON (green) or engaged (red): every setting handed back to native at once; every Omni-Compass side follows native (white) | the kill switch (section 1; its wiring, section 5g) |
| Tune Dial | the max (every muscle to its own limit) or the tune-down (never more than native) | the console's dial |
| Demand | ×0.25 to ×2 of the day's own demand, both arms alike | the console's demand slider |
| Noise | σ of the demand's noise, one draw a muscle a decision, both arms alike | the console's noise slider |
| Sense Delay | decisions added between what a muscle does and what its controller reads, both arms alike | the console's delay slider |
| Faults | a surge, half the machines lost, a sense blind, a security hold, on the chosen body part | the console's fault buttons |
| Speed | 1×, 4×, 16× or 60× of the engine's clock | the console's time knob |
| One Decision | step the engine one decision while paused | the console's time knob |
| Pause | hold the engine's clock | the console's time knob |
| Frame Load | +0, +8 or +16 ms burned inside every frame of this page | the console's frame-load knob |
| Run | A, B or C (or the archived run) the monitor plays | the monitor's own buttons |
| Repetition | which repetition of the run is replayed | the monitor's own buttons |
| Arm | which arm stands on the right: Omni-Compass governing, or watching only | the monitor's own buttons |
| Stack | the GPU card, the Linux host, Kubernetes or the cloud | the monitor's own buttons |
| Governor | which orchestrator or governor is shown | the monitor's own table |
| Scenario | on-site bare metal, through the cloud, in the device, as a service | the monitor's own buttons |
| Reading | every measured piece carried, or the index's strict rule | the monitor's own buttons |
| Chip Run | the chip's one run beside the count or in it | the monitor's own buttons |
| Beat | the governor's full read of the state and its decision: every 5, 10, 15, 20, 30, 60, 75, 90 or 120 s in the heartbeat sweep's record; on a real governor its --interval (60 s at the factory since omni-v17, 15 s on omni-v16) | the monitor's own buttons |
| Engine | which engine's record the monitor reads: the engine that stands or the one before it | the monitor's own buttons |
| Baseline | what each reading is set against: native, or the same engine at another setting | the monitor's own buttons |
| Gauge | which gauge of the run is shown | the monitor's own buttons |
| Filter | which rows, words, families or organisms are shown | the monitor's own buttons |
| Body | which body the organism runs: the harness, the organism, every muscle alone | the organism's own buttons |
| Muscle Switch | pick one muscle on either ring: its card, and its own switch, which hands that one muscle back to native (Omni-Compass OFF on it) or puts Omni-Compass on it again; the kill switch hands every muscle back at once | the organism's monitors and the muscle's card (section 3a) |
| Runs | how many of the Python's runs this page computes again | the monitor's own buttons |
| Print | the receipts of the runs, printable, with the digests and the notice | the monitor's own button |
| Seed Base | which held-out seed base's 500 scenarios are replayed | the monitor's own buttons |
| Set | the Python's own 500 (numpy, seed 223387268) or a set the jump generator drew on this page | the Monte Carlo monitor's set knob (section 5a) |
| Omni-Compass Way | the bounded command toward the nearest basin, toward the far basin, or with the double well off (μ = 0); native is the plant alone (u = 0) | the Monte Carlo monitor's way knob (section 5a) |
| Play / Pause | the cursor's sweep of the 20 macro steps, held or running | the Monte Carlo monitor (section 5a) |
| Custom System | your stack written as ranges of the core's six states and 22 parameters, run in the page or on GitHub through the Python and the C++ (`systems/README.md`) | the Monte Carlo monitor's own-system panel (section 5a) |

## Every LOSS row, whose it is, its cause and the knob that answers it

163 LOSS rows are Omni-Compass against its native; 171 are an orchestrator's own cost against the organism alone, with no Omni-Compass in either arm. Every one is shown as its table writes it.

- **Omni-Compass against native.** All four in one run (omni-v21, `results/live/V21_ALL_FOUR.md`): pod start wait, total (s), A B C 8.9 → 10.3; raw +15.7% (95%: −19.6% to +51.1%); LOSS · 9 → 12.8; raw +42.2% (95%: −16.2% to +100.6%); LOSS · 7.8 → 9.3; raw +19.2% (95%: −23.0% to +61.4%); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): response time (ms), 95th percentile, A B C 2452 → 2510; raw +2.4% (95%: −2.1% to +6.9%); LOSS · 2697 → 2871; raw +6.5% (95%: −3.8% to +16.7%); LOSS · 1422 → 1533; raw +7.7% (95%: +1.4% to +14.1%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): response time (ms), 99th percentile, A B C 3425 → 3535; raw +3.2% (95%: −1.9% to +8.3%); LOSS · 3778 → 4014; raw +6.3% (95%: −5.8% to +18.3%); LOSS · 1972 → 2162; raw +9.7% (95%: +3.3% to +16.0%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): failed requests (%), A B C 0.006817 → 0.007637; raw +12.0% (95%: −355.1% to +379.2%), +0.0008 in the gauge's unit; LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 12 → 12.33; raw +2.8% (95%: −0.4% to +6.0%); LOSS · 13 → 14; raw +7.7% (95%: −2.4% to +17.7%); LOSS · 6.8 → 8.2; raw +20.6% (95%: ±0.0% to +41.2%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): pod start wait, total (s), A B C 0.4444 → 1; raw +125.0% (95%: −50.3% to +300.3%), +0.5556 in the gauge's unit; LOSS · 0.3 → 2.3; raw +666.7% (95%: +151.6% to +1181.7%), +2.0000 in the gauge's unit; LOSS · 0.3 → 1; raw +233.3% (95%: −257.2% to +723.9%), +0.7000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): pod start wait, mean (s), A B C 0.2222 → 0.8333; raw +275.0% (95%: −46.0% to +596.0%), +0.6111 in the gauge's unit; LOSS · 0.3 → 1.083; raw +261.1% (95%: +52.5% to +469.8%), +0.7833 in the gauge's unit; LOSS · 0.15 → 0.65; raw +333.3% (95%: −217.3% to +884.0%), +0.5000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): batch: queue finished (s), A B C 872.8 → 885.1; raw +1.4% (95%: +0.4% to +2.4%); LOSS · 892.4 → 912.5; raw +2.3% (95%: +1.0% to +3.5%); LOSS · 806 → 818.8; raw +1.6% (95%: −0.1% to +3.2%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 184.4 → 193.8; raw +5.1% (95%: +1.9% to +8.3%); LOSS · 203.2 → 221.3; raw +8.9% (95%: +4.9% to +12.9%); LOSS · 115.3 → 125.8; raw +9.1% (95%: +0.9% to +17.3%); LOSS. Cause: Job turnaround under Armada, Omni-Compass on the organism alone (`V12_ARMADA_4W_BARE.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_TOP.md`): pod start wait, total (s), A B C 0.4444 → 2.222; raw +400.0% (95%: −79.7% to +879.7%), +1.7778 in the gauge's unit; LOSS · 0 → 2.3; raw +2.3000 in the gauge's unit (95%: +1.0361 to +3.5639); LOSS · 1.5 → 1.6; raw +6.7% (95%: −168.1% to +181.4%); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Batch queue (omni-v21, `results/live/V21_BATCH.md`): failed requests (%), A B C 0 → 0.01036; raw +0.0104 in the gauge's unit (95%: −0.0131 to +0.0338); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Batch queue (omni-v21, `results/live/V21_BATCH.md`): pod start wait, total (s), A B C 0 → 0.9; raw +0.9000 in the gauge's unit (95%: +0.1887 to +1.6113); LOSS · 0 → 4; raw +4.0000 in the gauge's unit (95%: −0.2519 to +8.2519); LOSS · 0 → 1.5; raw +1.5000 in the gauge's unit (95%: −0.7176 to +3.7176); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Batch queue (omni-v21, `results/live/V21_BATCH.md`): pod start wait, mean (s), A B C 0 → 0.9; raw +0.9000 in the gauge's unit (95%: +0.1887 to +1.6113); LOSS · 0 → 2.2; raw +2.2000 in the gauge's unit (95%: +0.1475 to +4.2525); LOSS · 0 → 0.8333; raw +0.8333 in the gauge's unit (95%: −0.0319 to +1.6985); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): response time (ms), 99th percentile, A B C 427.2 → 439.5; raw +2.9% (95%: −1.2% to +7.0%); LOSS · 415.6 → 425.7; raw +2.4% (95%: −3.4% to +8.3%); LOSS · 419.3 → 430.5; raw +2.7% (95%: −0.4% to +5.7%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): time over the response line (% of samples), A B C 0.7443 → 1.042; raw +40.0% (95%: −9.4% to +89.3%), +0.2976 in the gauge's unit; LOSS · 0.5461 → 0.6976; raw +27.7% (95%: −62.9% to +118.3%), +0.1515 in the gauge's unit; LOSS · 0.7367 → 0.8459; raw +14.8% (95%: −23.2% to +52.8%), +0.1093 in the gauge's unit; LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 1.2 → 2.1; raw +75.0% (95%: −11.4% to +161.4%); LOSS · 0.9 → 1.3; raw +44.4% (95%: −123.9% to +212.8%), +0.4000 in the gauge's unit; LOSS · 1.7 → 1.7; raw ±0.0% (95%: −44.4% to +44.4%); STEADY. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): pod start wait, total (s), A B C 0.1 → 0.6; raw +500.0% (95%: −272.6% to +1272.6%), +0.5000 in the gauge's unit; LOSS · 0.2 → 1; raw +400.0% (95%: −179.2% to +979.2%), +0.8000 in the gauge's unit; LOSS · 0.1 → 0.1; raw ±0.0% (95%: −337.2% to +337.2%), ±0.0000 in the gauge's unit; STEADY. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): pod start wait, mean (s), A B C 0.1 → 0.5; raw +400.0% (95%: −291.1% to +1091.1%), +0.4000 in the gauge's unit; LOSS · 0.2 → 0.75; raw +275.0% (95%: −158.6% to +708.5%), +0.5500 in the gauge's unit; LOSS · 0.1 → 0.1; raw ±0.0% (95%: −337.2% to +337.2%), ±0.0000 in the gauge's unit; STEADY. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.1 → 0.1; raw ±0.0% (95%: −337.2% to +337.2%), ±0.0000 in the gauge's unit; STEADY · 0.2 → 0.2; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY · 0 → 0.1; raw +0.1000 in the gauge's unit (95%: −0.1262 to +0.3262); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream (omni-v12, `results/live/V12_BINPACK.md`): queue: job turnaround, submitted to done, mean (s), A B C 26.6 → 26.97; raw +1.4% (95%: +0.8% to +1.9%); LOSS · 26.39 → 26.66; raw +1.0% (95%: +0.4% to +1.7%); LOSS · 26.58 → 26.89; raw +1.2% (95%: +0.7% to +1.6%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): response time (ms), 95th percentile, A B C 1397 → 1463; raw +4.7% (95%: −1.7% to +11.2%); LOSS · 866.2 → 923.9; raw +6.7% (95%: −1.7% to +15.0%); LOSS · 827.2 → 872.2; raw +5.4% (95%: −1.5% to +12.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): response time (ms), 99th percentile, A B C 2014 → 2059; raw +2.3% (95%: −6.1% to +10.6%); LOSS · 1230 → 1274; raw +3.5% (95%: −2.6% to +9.6%); LOSS · 1250 → 1246; raw −0.3% (95%: −11.9% to +11.3%); STEADY. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 10.8 → 10.9; raw +0.9% (95%: −2.8% to +4.7%); LOSS · 6.9 → 7.7; raw +11.6% (95%: −2.1% to +25.2%); LOSS · 8.3 → 8.6; raw +3.6% (95%: −4.6% to +11.8%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 102.4 → 106.9; raw +4.4% (95%: −1.7% to +10.5%); LOSS · 63.56 → 65.83; raw +3.6% (95%: −3.2% to +10.3%); LOSS · 58.77 → 61.3; raw +4.3% (95%: −2.3% to +10.9%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): pod start wait, total (s), A B C 0.5 → 0.9; raw +80.0% (95%: −124.6% to +284.6%), +0.4000 in the gauge's unit; LOSS · 0.5 → 1; raw +100.0% (95%: −294.7% to +494.7%), +0.5000 in the gauge's unit; LOSS · 0 → 0.6; raw +0.6000 in the gauge's unit (95%: −0.0032 to +1.2032); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): pod start wait, mean (s), A B C 0.25 → 0.9; raw +260.0% (95%: +7.2% to +512.8%), +0.6500 in the gauge's unit; LOSS · 0.4 → 0.65; raw +62.5% (95%: −267.4% to +392.4%), +0.2500 in the gauge's unit; LOSS · 0 → 0.6; raw +0.6000 in the gauge's unit (95%: −0.0032 to +1.2032); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 106.1 → 108.4; raw +2.2% (95%: −2.3% to +6.7%); LOSS · 63.75 → 65.27; raw +2.4% (95%: −1.2% to +6.0%); LOSS · 58.35 → 61.38; raw +5.2% (95%: +0.9% to +9.5%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The capacity test, native and Omni-Compass on top at the same resource cap (omni-v21, `results/live/V21_CAPACITY.md`): cap 3 cores: completed work (requests answered within the line over the window), A B C −0.6% (−1.4 to +0.2) · −1.1% (−3.6 to +1.4) · −0.2% (−0.7 to +0.4). Cause: 5. The fixed-capacity test at its top cap: 3 cores, the completed work (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BARE.md`): pod start wait, total (s), A B C 6.8 → 10.9; raw +60.3% (95%: +15.0% to +105.6%); LOSS · 8 → 10.3; raw +28.7% (95%: −22.5% to +80.0%); LOSS · 7.1 → 12; raw +69.0% (95%: +30.9% to +107.1%); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_TOP.md`): pod start wait, total (s), A B C 6.8 → 12.3; raw +80.9% (95%: +37.3% to +124.5%); LOSS · 6.6 → 13.5; raw +104.5% (95%: +46.9% to +162.2%); LOSS · 7.9 → 12.2; raw +54.4% (95%: +20.0% to +88.9%); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_TOP.md`): pod start wait, mean (s), A B C 1.492 → 1.62; raw +8.6% (95%: −9.5% to +26.8%); LOSS · 1.325 → 1.607; raw +21.3% (95%: +1.4% to +41.2%); LOSS · 1.58 → 1.594; raw +0.9% (95%: −15.0% to +16.8%); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** CruiseKube (omni-v21, `results/live/V21_CRUISEKUBE.md`): response time (ms), mean, A B C 83.61 → 84.39; raw +0.9% (95%: −0.8% to +2.7%); LOSS · 89.5 → 90.76; raw +1.4% (95%: +0.1% to +2.7%); LOSS · 85.69 → 87.79; raw +2.4% (95%: +0.9% to +4.0%); LOSS. Cause: 2. CruiseKube: three rows, two arms that are one system (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** CruiseKube (omni-v21, `results/live/V21_CRUISEKUBE.md`): response time (ms), 95th percentile, A B C 127.6 → 127.6; raw ±0.0% (95%: −1.6% to +1.5%); STEADY · 137.9 → 140.4; raw +1.8% (95%: +0.5% to +3.1%); LOSS · 136.4 → 137.8; raw +1.0% (95%: −0.8% to +2.9%); LOSS. Cause: 2. CruiseKube: three rows, two arms that are one system (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** CruiseKube (omni-v21, `results/live/V21_CRUISEKUBE.md`): time over the response line (% of samples), A B C 0.01176 → 0.01227; raw +4.3% (95%: −340.2% to +348.8%), +0.0005 in the gauge's unit; LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. Cause: 2. CruiseKube: three rows, two arms that are one system (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Fairness (omni-v21, `results/live/V21_FAIRNESS.md`): pod start wait, mean (s), A B C 1.6 → 1.678; raw +4.9% (95%: −28.0% to +37.8%); LOSS · 1.606 → 1.769; raw +10.1% (95%: −14.4% to +34.7%); LOSS · 1.203 → 1.817; raw +51.0% (95%: −7.9% to +109.9%); LOSS. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Fairness (omni-v21, `results/live/V21_FAIRNESS.md`): second app: failed requests (%), A B C 13.65 → 13.8; raw +1.1% (95%: −4.9% to +7.0%); LOSS · 11.61 → 11.73; raw +1.1% (95%: −3.5% to +5.6%); LOSS · 13.67 → 14.18; raw +3.7% (95%: −1.6% to +9.0%); LOSS. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Goldilocks (omni-v21, `results/live/V21_GOLDILOCKS.md`): pod start wait, total (s), A B C 4.8 → 8.4; raw +75.0% (95%: +27.8% to +122.2%); LOSS · 4.3 → 8.7; raw +102.3% (95%: +38.5% to +166.1%); LOSS · 4.6 → 10.9; raw +137.0% (95%: +32.0% to +241.9%); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Goldilocks (omni-v21, `results/live/V21_GOLDILOCKS.md`): pod start wait, mean (s), A B C 1.408 → 1.681; raw +19.4% (95%: −6.1% to +44.9%); LOSS · 1.267 → 1.673; raw +32.1% (95%: +7.0% to +57.2%); LOSS · 1.425 → 1.584; raw +11.2% (95%: −27.5% to +49.8%); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): response time (ms), 99th percentile, A B C 484.3 → 487.6; raw +0.7% (95%: −3.4% to +4.7%); LOSS · 519.6 → 569.8; raw +9.7% (95%: −2.4% to +21.7%); LOSS · 565.6 → 598.1; raw +5.7% (95%: −11.8% to +23.3%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): time over the response line (% of samples), A B C 1.003 → 1.091; raw +8.8% (95%: −24.7% to +42.4%); LOSS · 1.527 → 2.172; raw +42.3% (95%: −9.2% to +93.8%); LOSS · 2.335 → 2.487; raw +6.5% (95%: −47.1% to +60.1%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 1.4 → 1.8; raw +28.6% (95%: −74.2% to +131.3%); LOSS · 1.8 → 2.9; raw +61.1% (95%: −21.5% to +143.7%); LOSS · 3.5 → 3.5; raw ±0.0% (95%: −46.2% to +46.2%); STEADY. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 1 → 1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY · 1 → 1; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY · 1 → 1.2; raw +20.0% (95%: −10.2% to +50.2%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream (omni-v12, `results/live/V12_KAI.md`): queue: job turnaround, submitted to done, mean (s), A B C 29.85 → 30.29; raw +1.5% (95%: +0.4% to +2.5%); LOSS · 30.8 → 32.45; raw +5.3% (95%: −2.4% to +13.1%); LOSS · 32.25 → 32.97; raw +2.2% (95%: −5.4% to +9.9%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): response time (ms), 95th percentile, A B C 1070 → 1095; raw +2.3% (95%: −4.4% to +9.1%); LOSS · 1366 → 1450; raw +6.2% (95%: −4.2% to +16.5%); LOSS · 1135 → 1150; raw +1.3% (95%: −8.6% to +11.2%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): batch: queue finished (s), A B C 771.5 → 775.5; raw +0.5% (95%: +0.1% to +0.9%); LOSS · 790 → 797.8; raw +1.0% (95%: +0.2% to +1.8%); LOSS · 772.7 → 773.3; raw +0.1% (95%: −0.9% to +1.0%); STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 78.3 → 81.36; raw +3.9% (95%: +0.6% to +7.2%); LOSS · 98.16 → 106.2; raw +8.2% (95%: +2.6% to +13.8%); LOSS · 82.27 → 82.29; raw ±0.0% (95%: −11.1% to +11.2%); STEADY. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): response time (ms), 95th percentile, A B C 1478 → 1519; raw +2.8% (95%: −8.6% to +14.1%); LOSS · 1927 → 1992; raw +3.4% (95%: −2.4% to +9.1%); LOSS · 1712 → 1788; raw +4.4% (95%: −7.1% to +16.0%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): response time (ms), 99th percentile, A B C 2206 → 2288; raw +3.7% (95%: −4.5% to +12.0%); LOSS · 2841 → 2937; raw +3.4% (95%: −3.5% to +10.3%); LOSS · 2761 → 2775; raw +0.5% (95%: −9.2% to +10.2%); STEADY. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): pod start wait, mean (s), A B C 0.15 → 0.8; raw +433.3% (95%: −117.9% to +984.6%), +0.6500 in the gauge's unit; LOSS · 0.15 → 0.4; raw +166.7% (95%: −36.0% to +369.3%), +0.2500 in the gauge's unit; LOSS · 0.4 → 0.5; raw +25.0% (95%: −171.8% to +221.8%), +0.1000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): batch: queue finished (s), A B C 804.2 → 810.9; raw +0.8% (95%: +0.1% to +1.6%); LOSS · 835 → 844.2; raw +1.1% (95%: +0.3% to +1.9%); LOSS · 807.9 → 812.4; raw +0.6% (95%: −0.3% to +1.4%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 1.6 → 2.6; raw +62.5% (95%: −21.8% to +146.8%); LOSS · 2.6 → 3; raw +15.4% (95%: −60.5% to +91.2%); LOSS · 1.4 → 1.6; raw +14.3% (95%: −18.0% to +46.6%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 109.7 → 115.9; raw +5.6% (95%: −0.4% to +11.7%); LOSS · 139.5 → 148.6; raw +6.5% (95%: +0.8% to +12.2%); LOSS · 119.4 → 125.4; raw +5.0% (95%: +0.2% to +9.9%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): response time (ms), 95th percentile, A B C 2164 → 2439; raw +12.7% (95%: +5.9% to +19.5%); LOSS · 2260 → 2366; raw +4.6% (95%: −3.6% to +12.9%); LOSS · 2707 → 2815; raw +4.0% (95%: −2.0% to +10.0%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): response time (ms), 99th percentile, A B C 3077 → 3538; raw +15.0% (95%: +3.5% to +26.5%); LOSS · 3117 → 3349; raw +7.4% (95%: −0.4% to +15.3%); LOSS · 3712 → 3925; raw +5.7% (95%: −5.3% to +16.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 11.33 → 13; raw +14.7% (95%: −2.6% to +32.0%); LOSS · 11.3 → 12.3; raw +8.8% (95%: −2.7% to +20.4%); LOSS · 10.4 → 10.9; raw +4.8% (95%: +1.2% to +8.4%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): pod start wait, total (s), A B C 0.5556 → 2.222; raw +300.0% (95%: −72.5% to +672.5%), +1.6667 in the gauge's unit; LOSS · 0 → 1.2; raw +1.2000 in the gauge's unit (95%: +0.3879 to +2.0121); LOSS · 0 → 1.9; raw +1.9000 in the gauge's unit (95%: −0.1077 to +3.9077); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): pod start wait, mean (s), A B C 0.5556 → 1.389; raw +150.0% (95%: −99.4% to +399.4%), +0.8333 in the gauge's unit; LOSS · 0 → 0.95; raw +0.9500 in the gauge's unit (95%: +0.3091 to +1.5909); LOSS · 0 → 1.25; raw +1.2500 in the gauge's unit (95%: +0.2210 to +2.2790); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): batch: queue finished (s), A B C 852.7 → 875.9; raw +2.7% (95%: +1.0% to +4.5%); LOSS · 856.4 → 866.9; raw +1.2% (95%: −0.1% to +2.6%); LOSS · 909.9 → 928.2; raw +2.0% (95%: +0.7% to +3.3%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.07407 → 0.1019; raw +37.5% (95%: −30.9% to +105.9%), +0.0278 in the gauge's unit; LOSS · 0.1042 → 0.1083; raw +4.0% (95%: −58.5% to +66.5%), +0.0042 in the gauge's unit; LOSS · 0.0875 → 0.1; raw +14.3% (95%: −43.7% to +72.3%), +0.0125 in the gauge's unit; LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.5556 → 0.6667; raw +20.0% (95%: −63.1% to +103.1%), +0.1111 in the gauge's unit; LOSS · 0.6 → 0.8; raw +33.3% (95%: −16.9% to +83.6%), +0.2000 in the gauge's unit; LOSS · 0.5 → 0.5; raw ±0.0% (95%: ±0.0% to ±0.0%), ±0.0000 in the gauge's unit; STEADY. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 163.2 → 182; raw +11.6% (95%: +4.9% to +18.2%); LOSS · 167.6 → 171.2; raw +2.2% (95%: −1.7% to +6.0%); LOSS · 216.2 → 228.7; raw +5.8% (95%: +1.3% to +10.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), mean, A B C 709.8 → 808.5; raw +13.9% (95%: −0.4% to +28.2%); LOSS · 691.8 → 764.6; raw +10.5% (95%: −0.5% to +21.6%); LOSS · 844.3 → 867.4; raw +2.7% (95%: −8.4% to +13.9%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), 95th percentile, A B C 3269 → 3923; raw +20.0% (95%: +4.1% to +35.9%); LOSS · 3140 → 3665; raw +16.7% (95%: +1.6% to +31.8%); LOSS · 3666 → 3759; raw +2.5% (95%: −6.2% to +11.3%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): response time (ms), 99th percentile, A B C 4767 → 5337; raw +12.0% (95%: +1.8% to +22.1%); LOSS · 4602 → 5114; raw +11.1% (95%: +1.2% to +21.0%); LOSS · 4876 → 5069; raw +4.0% (95%: −4.2% to +12.2%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): time over the response line (% of samples), A B C 24.64 → 25.85; raw +4.9% (95%: −0.1% to +10.0%); LOSS · 23.99 → 25.28; raw +5.4% (95%: +1.7% to +9.1%); LOSS · 25.85 → 28; raw +8.3% (95%: −7.7% to +24.3%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): failed requests (%), A B C 0.08233 → 0.159; raw +93.2% (95%: −3.5% to +189.8%), +0.0767 in the gauge's unit; LOSS · 0.0524 → 0.1452; raw +177.2% (95%: −58.9% to +413.2%), +0.0928 in the gauge's unit; LOSS · 0.06374 → 0.1831; raw +187.3% (95%: −70.3% to +444.8%), +0.1194 in the gauge's unit; LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): pod start wait, total (s), A B C 1.111 → 3.889; raw +250.0% (95%: −212.5% to +712.5%); LOSS · 1.1 → 1.9; raw +72.7% (95%: −145.8% to +291.2%); LOSS · 1.1 → 2.2; raw +100.0% (95%: −164.5% to +364.5%); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): pod start wait, mean (s), A B C 0.8333 → 1.101; raw +32.1% (95%: −147.0% to +211.2%), +0.2672 in the gauge's unit; LOSS · 0.65 → 1.033; raw +59.0% (95%: −121.0% to +238.9%), +0.3833 in the gauge's unit; LOSS · 0.85 → 1.225; raw +44.1% (95%: −131.4% to +219.6%), +0.3750 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): batch: queue finished (s), A B C 952.2 → 993.1; raw +4.3% (95%: +1.8% to +6.8%); LOSS · 952.2 → 991; raw +4.1% (95%: +1.8% to +6.3%); LOSS · 1010 → 1040; raw +3.0% (95%: −0.3% to +6.4%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 258.1 → 298.7; raw +15.7% (95%: +5.9% to +25.6%); LOSS · 261.5 → 298.5; raw +14.2% (95%: +6.1% to +22.2%); LOSS · 311.6 → 341.4; raw +9.6% (95%: −1.7% to +20.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kubernetes with KEDA on the CPU target and the live requests in flight (omni-v21, `results/live/V21_KEDA_CPU_REQUESTS.md`): pod start wait, total (s), A B C 6.3 → 11.6; raw +84.1% (95%: +40.6% to +127.6%); LOSS · 8.1 → 10.6; raw +30.9% (95%: −7.6% to +69.3%); LOSS · 8 → 10.2; raw +27.5% (95%: −14.0% to +69.0%); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Koordinator under the batch stream (omni-v12, `results/live/V12_KOORDINATOR.md`): pod start wait, total (s), A B C 0.2 → 0.8; raw +300.0% (95%: −264.2% to +864.2%), +0.6000 in the gauge's unit; LOSS · 0.2 → 0.8; raw +300.0% (95%: −45.5% to +645.5%), +0.6000 in the gauge's unit; LOSS · 0.2 → 0.9; raw +350.0% (95%: −304.1% to +1004.1%), +0.7000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Koordinator under the batch stream (omni-v12, `results/live/V12_KOORDINATOR.md`): pod start wait, mean (s), A B C 0.2 → 0.6; raw +200.0% (95%: −219.8% to +619.8%), +0.4000 in the gauge's unit; LOSS · 0.2 → 0.8; raw +300.0% (95%: −45.5% to +645.5%), +0.6000 in the gauge's unit; LOSS · 0.2 → 0.65; raw +225.0% (95%: −224.6% to +674.6%), +0.4500 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): response time (ms), 95th percentile, A B C 536.2 → 567.1; raw +5.8% (95%: +1.6% to +9.9%); LOSS · 1283 → 1372; raw +6.9% (95%: −1.2% to +15.1%); LOSS · 863.2 → 913.5; raw +5.8% (95%: −1.2% to +12.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): response time (ms), 99th percentile, A B C 767.9 → 818.7; raw +6.6% (95%: −4.7% to +17.9%); LOSS · 1874 → 2010; raw +7.3% (95%: −1.6% to +16.1%); LOSS · 1252 → 1296; raw +3.6% (95%: −1.3% to +8.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 38.07 → 40.1; raw +5.3% (95%: −4.7% to +15.3%); LOSS · 85.79 → 89.12; raw +3.9% (95%: −0.1% to +7.9%); LOSS · 55.45 → 59.44; raw +7.2% (95%: +0.2% to +14.2%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0.1 → 0.2; raw +100.0% (95%: −306.0% to +506.0%), +0.1000 in the gauge's unit; LOSS · 0.1 → 0.1; raw ±0.0% (95%: −337.2% to +337.2%), ±0.0000 in the gauge's unit; STEADY. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): batch: queue finished (s), A B C 1290 → 1313; raw +1.8% (95%: −3.7% to +7.2%); LOSS · 1421 → 1421; raw ±0.0% (95%: −0.8% to +0.8%); STEADY · 1396 → 1421; raw +1.8% (95%: −1.3% to +4.8%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 614 → 650.2; raw +5.9% (95%: −2.3% to +14.1%); LOSS · 799.3 → 814.5; raw +1.9% (95%: −4.7% to +8.5%); LOSS · 763.3 → 789; raw +3.4% (95%: −1.1% to +7.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): response time (ms), 95th percentile, A B C 1132 → 1204; raw +6.3% (95%: −0.8% to +13.4%); LOSS · 1090 → 1166; raw +7.0% (95%: +2.5% to +11.4%); LOSS · 1496 → 1547; raw +3.4% (95%: −0.7% to +7.4%); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): response time (ms), 99th percentile, A B C 1583 → 1738; raw +9.8% (95%: +1.5% to +18.0%); LOSS · 1617 → 1688; raw +4.4% (95%: +0.1% to +8.7%); LOSS · 2030 → 2294; raw +13.0% (95%: +4.7% to +21.2%); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): pod start wait, total (s), A B C 0 → 0.5556; raw +0.5556 in the gauge's unit (95%: −0.3133 to +1.4244); LOSS · 0 → 0.5; raw +0.5000 in the gauge's unit (95%: −0.1952 to +1.1952); LOSS · 0 → 0.6; raw +0.6000 in the gauge's unit (95%: −0.1689 to +1.3689); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): pod start wait, mean (s), A B C 0 → 0.5556; raw +0.5556 in the gauge's unit (95%: −0.3133 to +1.4244); LOSS · 0 → 0.35; raw +0.3500 in the gauge's unit (95%: −0.0647 to +0.7647); LOSS · 0 → 0.6; raw +0.6000 in the gauge's unit (95%: −0.1689 to +1.3689); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): batch: queue finished (s), A B C 774.1 → 780.1; raw +0.8% (95%: +0.1% to +1.5%); LOSS · 775.3 → 780.5; raw +0.7% (95%: +0.2% to +1.2%); LOSS · 802.6 → 807.7; raw +0.6% (95%: +0.2% to +1.1%); LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.03241 → 0.05093; raw +57.1% (95%: −54.6% to +168.9%), +0.0185 in the gauge's unit; LOSS · 0.04167 → 0.09167; raw +120.0% (95%: −61.0% to +301.0%), +0.0500 in the gauge's unit; LOSS · 0.05417 → 0.09583; raw +76.9% (95%: −65.1% to +219.0%), +0.0417 in the gauge's unit; LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.1111 → 0.3333; raw +200.0% (95%: −105.1% to +505.1%), +0.2222 in the gauge's unit; LOSS · 0.4 → 0.4; raw ±0.0% (95%: −119.2% to +119.2%), ±0.0000 in the gauge's unit; STEADY · 0.4 → 0.6; raw +50.0% (95%: −25.4% to +125.4%), +0.2000 in the gauge's unit; LOSS. Cause: Amendment 10: what the counted runs of 20 October found (written after those runs, before the Gödel runs start again) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 81.79 → 87.35; raw +6.8% (95%: −0.6% to +14.2%); LOSS · 83.3 → 87.46; raw +5.0% (95%: −0.2% to +10.2%); LOSS · 107.6 → 114.2; raw +6.1% (95%: +1.9% to +10.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_TOP.md`): response time (ms), 95th percentile, A B C 1305 → 1356; raw +3.9% (95%: −6.9% to +14.7%); LOSS · 1271 → 1343; raw +5.6% (95%: −4.2% to +15.5%); LOSS · 1432 → 1440; raw +0.5% (95%: −5.9% to +7.0%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 635 → 637.5; raw +0.4% (95%: −8.5% to +9.2%); STEADY · 533.6 → 536.6; raw +0.6% (95%: −7.9% to +9.1%); LOSS · 670.7 → 677.6; raw +1.0% (95%: −3.7% to +5.7%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): response time (ms), 95th percentile, A B C 1006 → 1044; raw +3.8% (95%: −2.2% to +9.8%); LOSS · 1151 → 1169; raw +1.6% (95%: −5.0% to +8.2%); LOSS · 1278 → 1334; raw +4.4% (95%: −5.1% to +13.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): pod start wait, total (s), A B C 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.3786 to +0.9786); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): pod start wait, mean (s), A B C 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.3786 to +0.9786); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 73.89 → 79.93; raw +8.2% (95%: +0.2% to +16.1%); LOSS · 81.23 → 83.89; raw +3.3% (95%: −1.2% to +7.8%); LOSS · 87.61 → 92.22; raw +5.3% (95%: −2.3% to +12.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): failed requests (%), A B C 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0.009302; raw +0.0093 in the gauge's unit (95%: −0.0117 to +0.0303); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 7.8 → 8; raw +2.6% (95%: −8.7% to +13.8%); LOSS · 10.3 → 10.6; raw +2.9% (95%: −1.8% to +7.6%); LOSS · 11.11 → 11.33; raw +2.0% (95%: −1.1% to +5.1%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.1625 → 0.1667; raw +2.6% (95%: −75.0% to +80.1%), +0.0042 in the gauge's unit; LOSS · 0.2 → 0.2; raw ±0.0% (95%: −63.2% to +63.2%), ±0.0000 in the gauge's unit; STEADY · 0.2361 → 0.2361; raw ±0.0% (95%: −17.9% to +17.9%), ±0.0000 in the gauge's unit; STEADY. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 82.38 → 83.16; raw +0.9% (95%: −5.4% to +7.3%); LOSS · 88.75 → 92.45; raw +4.2% (95%: −2.2% to +10.6%); LOSS · 98.69 → 102.1; raw +3.5% (95%: −2.7% to +9.6%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): response time (ms), 95th percentile, A B C 2969 → 3098; raw +4.3% (95%: −0.7% to +9.4%); LOSS · 2682 → 2784; raw +3.8% (95%: −4.2% to +11.8%); LOSS · 2493 → 2538; raw +1.8% (95%: −8.0% to +11.6%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): response time (ms), 99th percentile, A B C 4041 → 4247; raw +5.1% (95%: −6.1% to +16.3%); LOSS · 3704 → 3891; raw +5.1% (95%: −3.0% to +13.1%); LOSS · 3409 → 3512; raw +3.0% (95%: −4.7% to +10.7%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 14.9 → 15.3; raw +2.7% (95%: +0.2% to +5.2%); LOSS · 12.4 → 12.7; raw +2.4% (95%: −0.4% to +5.2%); LOSS · 10.1 → 11.2; raw +10.9% (95%: −0.9% to +22.7%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): pod start wait, total (s), A B C 0.8 → 1.7; raw +112.5% (95%: −108.3% to +333.3%), +0.9000 in the gauge's unit; LOSS · 0.2 → 2.4; raw +1100.0% (95%: +243.6% to +1956.4%), +2.2000 in the gauge's unit; LOSS · 0.6 → 1.3; raw +116.7% (95%: −70.2% to +303.5%), +0.7000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): pod start wait, mean (s), A B C 0.55 → 1.1; raw +100.0% (95%: −102.1% to +302.1%), +0.5500 in the gauge's unit; LOSS · 0.2 → 1.25; raw +525.0% (95%: +52.2% to +997.8%), +1.0500 in the gauge's unit; LOSS · 0.4 → 0.8; raw +100.0% (95%: −44.8% to +244.8%), +0.4000 in the gauge's unit; LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): batch: queue finished (s), A B C 911.9 → 932.9; raw +2.3% (95%: +0.9% to +3.7%); LOSS · 885.4 → 898.2; raw +1.4% (95%: +0.3% to +2.6%); LOSS · 881.5 → 890.5; raw +1.0% (95%: −0.3% to +2.4%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 222.3 → 236.9; raw +6.5% (95%: +3.2% to +9.9%); LOSS · 194.8 → 204.3; raw +4.9% (95%: −0.2% to +9.9%); LOSS · 190.6 → 195; raw +2.3% (95%: −2.9% to +7.5%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): response time (ms), 95th percentile, A B C 4119 → 4499; raw +9.2% (95%: −1.6% to +20.0%); LOSS · 4095 → 4162; raw +1.6% (95%: −12.0% to +15.2%); LOSS · 2738 → 3866; raw +41.2% (95%: +1.6% to +80.7%); LOSS. Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): response time (ms), 99th percentile, A B C 5429 → 6036; raw +11.2% (95%: −2.0% to +24.3%); LOSS · 5491 → 5867; raw +6.9% (95%: −7.7% to +21.4%); LOSS · 3776 → 5213; raw +38.0% (95%: +0.1% to +76.0%); LOSS. Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): failed requests (%), A B C 0.3539 → 0.4937; raw +39.5% (95%: −46.7% to +125.8%), +0.1399 in the gauge's unit; LOSS · 0.05059 → 0.1132; raw +123.7% (95%: −203.3% to +450.7%), +0.0626 in the gauge's unit; LOSS · 0.01653 → 0.05082; raw +207.5% (95%: −260.7% to +675.6%), +0.0343 in the gauge's unit; LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 17.6 → 18.6; raw +5.7% (95%: +1.4% to +10.0%); LOSS · 14.8 → 15.7; raw +6.1% (95%: +0.8% to +11.4%); LOSS · 12.1 → 17.6; raw +45.5% (95%: +5.7% to +85.2%); LOSS. Cause: Alert minutes under Open Cluster Management, Omni-Compass on top (`V12_OCM_4W_TOP.md`): under investigation since 21 October 2026 (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`). The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): pod start wait, total (s), A B C 0.3 → 2.9; raw +866.7% (95%: +127.9% to +1605.4%), +2.6000 in the gauge's unit; LOSS · 0 → 2.9; raw +2.9000 in the gauge's unit (95%: +1.1014 to +4.6986); LOSS · 0 → 5; raw +5.0000 in the gauge's unit (95%: −0.4892 to +10.4892); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): pod start wait, mean (s), A B C 0.3 → 1.55; raw +416.7% (95%: +69.1% to +764.2%), +1.2500 in the gauge's unit; LOSS · 0 → 1.617; raw +1.6167 in the gauge's unit (95%: +0.8358 to +2.3975); LOSS · 0 → 2.467; raw +2.4667 in the gauge's unit (95%: −0.2772 to +5.2106); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): batch: queue finished (s), A B C 1049 → 1107; raw +5.5% (95%: +2.2% to +8.9%); LOSS · 1026 → 1058; raw +3.0% (95%: +1.0% to +5.0%); LOSS · 1023 → 1050; raw +2.6% (95%: −4.4% to +9.5%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 7.229 → 22.47; raw +210.8% (95%: −13.9% to +435.5%); LOSS · 6.929 → 18.62; raw +168.7% (95%: −49.3% to +386.7%); LOSS · 3.13 → 14.34; raw +358.1% (95%: −20.3% to +736.6%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 39.4 → 159.5; raw +304.8% (95%: −8.1% to +617.8%); LOSS · 55.9 → 105.6; raw +88.9% (95%: −32.2% to +210.0%); LOSS · 6.333 → 94.33; raw +1389.5% (95%: −119.4% to +2898.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 328.8 → 380; raw +15.6% (95%: +2.8% to +28.4%); LOSS · 305.8 → 326.8; raw +6.9% (95%: −5.0% to +18.7%); LOSS · 258.9 → 309.6; raw +19.6% (95%: +8.1% to +31.0%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Robustness (omni-v21, `results/live/V21_ROBUST_KILL.md`): pod start wait, total (s), A B C 6.9 → 7.6; raw +10.1% (95%: −37.0% to +57.3%); LOSS · 8.2 → 10.2; raw +24.4% (95%: −63.1% to +111.9%); LOSS · 8.4 → 15; raw +78.6% (95%: +16.2% to +140.9%); LOSS. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Robustness (omni-v21, `results/live/V21_ROBUST_LONG.md`): pod start wait, total (s), A B C 10 → 19; raw +90.0% (95%: −18.3% to +198.3%); LOSS · 7.667 → 24.67; raw +221.7% (95%: −317.6% to +761.1%); LOSS · 8.333 → 35.33; raw +324.0% (95%: −244.8% to +892.8%); LOSS. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Robustness (omni-v21, `results/live/V21_ROBUST_LONG.md`): pod start wait, mean (s), A B C 1.279 → 1.591; raw +24.5% (95%: −69.7% to +118.6%); LOSS · 1.444 → 1.834; raw +27.0% (95%: −100.1% to +154.0%); LOSS · 1.38 → 1.732; raw +25.6% (95%: −32.6% to +83.7%); LOSS. Cause: 1. The pod start wait: thirteen rows in eight tables (`docs/LOSS_CAUSES_2026-10-31.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** A public day of demand (omni-v21, `results/live/V21_TRACE_GOOGLE2011.md`): pod start wait, total (s), A B C 10 → 20.9; raw +109.0% (95%: +31.2% to +186.8%); LOSS · 10.7 → 20.1; raw +87.9% (95%: +13.7% to +162.0%); LOSS · 7.7 → 29.2; raw +279.2% (95%: +180.7% to +377.8%); LOSS. Cause: The pod start wait on one shared host: where it goes, why it rose, and the rig amendment of 18 October (`docs/POD_START_WAIT.md`). The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): response time (ms), 95th percentile, A B C 523.3 → 522.3; raw −0.2% (95%: −5.3% to +4.9%); STEADY · 417.2 → 455; raw +9.1% (95%: +3.9% to +14.2%); LOSS · 469.7 → 494.8; raw +5.3% (95%: −1.2% to +11.9%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): response time (ms), 99th percentile, A B C 672.1 → 678.9; raw +1.0% (95%: −2.6% to +4.6%); LOSS · 553.2 → 584.8; raw +5.7% (95%: +1.0% to +10.4%); LOSS · 621.8 → 650.1; raw +4.5% (95%: +1.1% to +8.0%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 9.7 → 9.7; raw ±0.0% (95%: −4.9% to +4.9%); STEADY · 4.5 → 5.8; raw +28.9% (95%: −3.8% to +61.6%); LOSS · 6.8 → 8.3; raw +22.1% (95%: −5.7% to +49.8%); LOSS. The knob: the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS.
- **Omni-Compass against native.** The Kubernetes scheduler as shipped under the batch stream (omni-v12, `results/live/V12_VANILLA.md`): queue: job turnaround, submitted to done, mean (s), A B C 28.22 → 28.48; raw +0.9% (95%: +0.2% to +1.7%); LOSS · 25.72 → 25.95; raw +0.9% (95%: +0.1% to +1.6%); LOSS · 27.32 → 27.65; raw +1.2% (95%: +0.6% to +1.8%); LOSS. Cause: Amendment 5: the governor's own core (written before any run on it, 20 October 2026) (`docs/BATCH_QUEUE_PREREGISTRATION.md`). The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): response time (ms), 95th percentile, A B C 926.1 → 996.5; raw +7.6% (95%: +0.8% to +14.5%); LOSS · 1133 → 1167; raw +2.9% (95%: −2.9% to +8.8%); LOSS · 1065 → 1145; raw +7.5% (95%: −0.1% to +15.1%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): response time (ms), 99th percentile, A B C 1337 → 1467; raw +9.7% (95%: +1.9% to +17.5%); LOSS · 1627 → 1620; raw −0.4% (95%: −10.6% to +9.7%); STEADY · 1483 → 1638; raw +10.4% (95%: −0.9% to +21.7%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 0.3; raw ±0.0% (95%: −159.0% to +159.0%), ±0.0000 in the gauge's unit; STEADY · 0.4 → 0.5; raw +25.0% (95%: −76.5% to +126.5%), +0.1000 in the gauge's unit; LOSS · 0.2 → 0.5; raw +150.0% (95%: −91.4% to +391.4%), +0.3000 in the gauge's unit; LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BARE.md`): queue: job turnaround, submitted to done, mean (s), A B C 65.63 → 70.4; raw +7.3% (95%: +1.1% to +13.4%); LOSS · 85.9 → 87.21; raw +1.5% (95%: −1.8% to +4.8%); LOSS · 75.65 → 82.43; raw +9.0% (95%: +1.5% to +16.5%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): response time (ms), 95th percentile, A B C 517.4 → 518.9; raw +0.3% (95%: −21.7% to +22.3%); STEADY · 884.6 → 1003; raw +13.4% (95%: −8.4% to +35.1%); LOSS · 758.9 → 839.4; raw +10.6% (95%: −7.0% to +28.2%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): pod start wait, total (s), A B C 0.2 → 0.4; raw +100.0% (95%: −306.0% to +506.0%), +0.2000 in the gauge's unit; LOSS · 0.1 → 1.4; raw +1300.0% (95%: −1085.5% to +3685.5%), +1.3000 in the gauge's unit; LOSS · 0 → 1.2; raw +1.2000 in the gauge's unit (95%: −0.3004 to +2.7004); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): pod start wait, mean (s), A B C 0.2 → 0.4; raw +100.0% (95%: −306.0% to +506.0%), +0.2000 in the gauge's unit; LOSS · 0.1 → 0.7; raw +600.0% (95%: −625.1% to +1825.1%), +0.6000 in the gauge's unit; LOSS · 0 → 1.2; raw +1.2000 in the gauge's unit (95%: −0.3004 to +2.7004); LOSS. The knob: the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms.
- **Omni-Compass against native.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_TOP.md`): queue: job turnaround, submitted to done, mean (s), A B C 81.51 → 86.72; raw +6.4% (95%: +0.7% to +12.1%); LOSS · 101 → 102.8; raw +1.8% (95%: −4.5% to +8.1%); LOSS · 93.17 → 95.34; raw +2.3% (95%: −2.1% to +6.8%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, resource objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, mean (ms), A B C 341 → 339.6; raw −0.4% (95%: −8.4% to +7.6%); STEADY · 284.4 → 293.1; raw +3.0% (95%: −6.0% to +12.0%); LOSS · 214.2 → 220.5; raw +2.9% (95%: −20.8% to +26.7%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, resource objective (omni-v21, `results/live/V21_KAFKA.md`): consumer lag, mean messages waiting, A B C 62.6 → 62.55; raw −0.1% (95%: −6.1% to +5.9%); STEADY · 52.12 → 53.75; raw +3.1% (95%: −5.2% to +11.5%); LOSS · 39.89 → 41.44; raw +3.9% (95%: −23.7% to +31.5%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, resource objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, 99th percentile (ms), A B C 3736 → 3759; raw +0.6% (95%: −4.3% to +5.5%); LOSS · 3649 → 3679; raw +0.8% (95%: −3.8% to +5.4%); LOSS · 2394 → 2611; raw +9.1% (95%: −14.1% to +32.2%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, resource objective (omni-v21, `results/live/V21_KAFKA.md`): end-to-end latency, mean (ms), A B C 318.8 → 323.5; raw +1.5% (95%: −3.7% to +6.6%); LOSS · 326.7 → 326.9; raw +0.1% (95%: −10.7% to +10.8%); STEADY · 210.7 → 235.5; raw +11.8% (95%: −13.9% to +37.4%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, resource objective (omni-v21, `results/live/V21_KAFKA.md`): consumer lag, mean messages waiting, A B C 277.4 → 281.1; raw +1.3% (95%: −4.4% to +7.1%); LOSS · 287.4 → 287.7; raw +0.1% (95%: −10.3% to +10.5%); STEADY · 184.6 → 205.4; raw +11.2% (95%: −13.1% to +35.6%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C 362.2 → 371.4; raw +2.5% (95%: −4.5% to +9.6%); LOSS · 385.8 → 384.7; raw −0.3% (95%: −3.4% to +2.8%); STEADY · 405.4 → 418.6; raw +3.3% (95%: −3.3% to +9.8%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, most messages waiting at once, A B C 1565 → 1574; raw +0.5% (95%: −6.5% to +7.5%); LOSS · 1656 → 1678; raw +1.3% (95%: −4.8% to +7.4%); LOSS · 1737 → 1788; raw +2.9% (95%: +1.9% to +3.9%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C 158 → 162.6; raw +2.9% (95%: −4.1% to +9.9%); LOSS · 167.4 → 167; raw −0.2% (95%: −5.9% to +5.4%); STEADY · 180.1 → 184.5; raw +2.4% (95%: −4.4% to +9.3%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C 289.1 → 287.8; raw −0.4% (95%: −2.4% to +1.5%); STEADY · 347.2 → 354; raw +1.9% (95%: −9.9% to +13.8%); LOSS · 328.8 → 337.7; raw +2.7% (95%: −4.3% to +9.8%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, most messages waiting at once, A B C 646.3 → 654; raw +1.2% (95%: −14.0% to +16.4%); LOSS · 731.7 → 741.3; raw +1.3% (95%: −4.3% to +6.9%); LOSS · 695.7 → 706; raw +1.5% (95%: −7.4% to +10.4%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C 52.71 → 52.45; raw −0.5% (95%: −8.2% to +7.2%); STEADY · 63.84 → 65.04; raw +1.9% (95%: −10.3% to +14.0%); LOSS · 60.45 → 61.5; raw +1.7% (95%: −2.4% to +5.9%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): work inside the response line (messages a second handled within the line), A B C 724.8 → 715.5; raw −1.3% (95%: −3.1% to +0.5%); LOSS · 725.4 → 720.8; raw −0.6% (95%: −2.8% to +1.5%); LOSS · 723.4 → 720.3; raw −0.4% (95%: −2.2% to +1.3%); STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, 95th percentile (ms), A B C 2272 → 2293; raw +0.9% (95%: −6.0% to +7.9%); LOSS · 2181 → 2238; raw +2.6% (95%: −0.7% to +5.9%); LOSS · 2100 → 2098; raw −0.1% (95%: −2.6% to +2.4%); STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): end-to-end latency, mean (ms), A B C 304.5 → 320.9; raw +5.4% (95%: −9.7% to +20.5%); LOSS · 298.5 → 310.1; raw +3.9% (95%: −3.9% to +11.7%); LOSS · 274.6 → 279.5; raw +1.8% (95%: −7.6% to +11.2%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Kafka, a consumer group's operator-set size, service objective (omni-v21, `results/live/V21_KAFKA_SERVICE.md`): consumer lag, mean messages waiting, A B C 266.5 → 277.3; raw +4.0% (95%: −11.0% to +19.1%); LOSS · 259.2 → 268.7; raw +3.7% (95%: −4.4% to +11.7%); LOSS · 235.9 → 239.9; raw +1.7% (95%: −7.3% to +10.7%); LOSS. The knob: the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack.
- **Omni-Compass against native.** Redis, a cache's operator-set memory ceiling, resource objective (omni-v21, `results/live/V21_REDIS.md`): latency, 99th percentile (ms), A B C 5.74 → 5.75; raw +0.2% (95%: −0.3% to +0.6%); STEADY · 5.739 → 5.749; raw +0.2% (95%: +0.1% to +0.3%); STEADY · 5.366 → 5.458; raw +1.7% (95%: +0.4% to +3.1%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** Redis, a cache's operator-set memory ceiling, service objective (omni-v21, `results/live/V21_REDIS_SERVICE.md`): latency, 99th percentile (ms), A B C 5.691 → 5.713; raw +0.4% (95%: −0.7% to +1.5%); STEADY · 5.339 → 5.393; raw +1.0% (95%: −2.2% to +4.2%); LOSS · 5.754 → 5.768; raw +0.2% (95%: ±0.0% to +0.5%); STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped, resource objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, 95th percentile (ms), A B C 5.57 → 5.57; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY · 15.38 → 54.62; raw +255.1% (95%: −554.4% to +1064.6%); LOSS · 5.438 → 5.471; raw +0.6% (95%: −2.0% to +3.3%); LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped, resource objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, mean (ms), A B C 3.052 → 3.041; raw −0.4% (95%: −4.6% to +3.9%); STEADY · 2.3 → 2.499; raw +8.7% (95%: −40.0% to +57.4%); LOSS · 3.347 → 3.344; raw −0.1% (95%: −1.7% to +1.5%); STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** sysbench on MySQL, a database's buffer pool as shipped, resource objective (omni-v21, `results/live/V21_SYSBENCH_SHIPPED.md`): latency, mean (ms), A B C 1.046 → 1.064; raw +1.6% (95%: −17.8% to +21.1%); LOSS · 1.143 → 1.175; raw +2.8% (95%: −22.6% to +28.2%); LOSS · 0.886 → 0.9053; raw +2.2% (95%: −4.1% to +8.4%), +0.0192 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, resource objective (omni-v21, `results/live/V21_YCSB.md`): latency, 95th percentile (ms), A B C 0.4083 → 0.409; raw +0.2% (95%: −2.9% to +3.2%), +0.0007 in the gauge's unit; STEADY · 0.3047 → 0.321; raw +5.4% (95%: −7.8% to +18.6%), +0.0163 in the gauge's unit; LOSS · 0.2703 → 0.2723; raw +0.7% (95%: −1.1% to +2.6%), +0.0020 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, resource objective (omni-v21, `results/live/V21_YCSB.md`): latency, 99th percentile (ms), A B C 0.577 → 0.5793; raw +0.4% (95%: −4.4% to +5.2%), +0.0023 in the gauge's unit; STEADY · 0.462 → 0.4737; raw +2.5% (95%: −0.4% to +5.5%), +0.0117 in the gauge's unit; LOSS · 0.4513 → 0.459; raw +1.7% (95%: −2.5% to +5.9%), +0.0077 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, service objective (omni-v21, `results/live/V21_YCSB_SERVICE.md`): latency, 95th percentile (ms), A B C 0.38 → 0.3807; raw +0.2% (95%: −7.1% to +7.5%), +0.0007 in the gauge's unit; STEADY · 0.3177 → 0.321; raw +1.0% (95%: −1.2% to +3.3%), +0.0033 in the gauge's unit; LOSS · 0.1807 → 0.1817; raw +0.6% (95%: −11.7% to +12.8%), +0.0010 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, service objective (omni-v21, `results/live/V21_YCSB_SERVICE.md`): latency, mean (ms), A B C 0.2119 → 0.2128; raw +0.4% (95%: −6.9% to +7.8%), +0.0009 in the gauge's unit; STEADY · 0.1874 → 0.1905; raw +1.7% (95%: −1.8% to +5.1%), +0.0031 in the gauge's unit; LOSS · 0.09107 → 0.09106; raw ±0.0% (95%: −9.7% to +9.7%), ±0.0000 in the gauge's unit; STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C 0.3097 → 0.3277; raw +5.8% (95%: −8.1% to +19.7%), +0.0180 in the gauge's unit; LOSS · 0.1267 → 0.1553; raw +22.6% (95%: −26.5% to +71.7%), +0.0287 in the gauge's unit; LOSS · 0.2133 → 0.2173; raw +1.9% (95%: −9.9% to +13.7%), +0.0040 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 99th percentile (ms), A B C 0.5047 → 0.515; raw +2.0% (95%: −5.1% to +9.2%), +0.0103 in the gauge's unit; LOSS · 0.3333 → 0.3507; raw +5.2% (95%: −2.2% to +12.6%), +0.0173 in the gauge's unit; LOSS · 0.4087 → 0.4177; raw +2.2% (95%: −10.4% to +14.9%), +0.0090 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C 0.1866 → 0.1895; raw +1.6% (95%: −2.4% to +5.5%), +0.0029 in the gauge's unit; LOSS · 0.06213 → 0.06473; raw +4.2% (95%: −17.6% to +26.0%), +0.0026 in the gauge's unit; LOSS · 0.1527 → 0.1626; raw +6.5% (95%: −8.3% to +21.3%), +0.0099 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C 0.378 → 0.385; raw +1.9% (95%: −2.7% to +6.5%), +0.0070 in the gauge's unit; LOSS · 0.4893 → 0.49; raw +0.1% (95%: −17.5% to +17.7%), +0.0007 in the gauge's unit; STEADY · 0.2417 → 0.252; raw +4.3% (95%: −6.4% to +15.0%), +0.0103 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 99th percentile (ms), A B C 0.5347 → 0.559; raw +4.6% (95%: −6.6% to +15.7%), +0.0243 in the gauge's unit; LOSS · 0.7627 → 0.767; raw +0.6% (95%: −49.8% to +50.9%), +0.0043 in the gauge's unit; LOSS · 0.3813 → 0.3997; raw +4.8% (95%: −2.5% to +12.1%), +0.0183 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C 0.1386 → 0.142; raw +2.5% (95%: −1.5% to +6.5%), +0.0034 in the gauge's unit; LOSS · 0.2326 → 0.234; raw +0.6% (95%: −16.5% to +17.7%), +0.0014 in the gauge's unit; LOSS · 0.07182 → 0.0752; raw +4.7% (95%: −3.9% to +13.3%), +0.0034 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C 0.178 → 0.1793; raw +0.7% (95%: −2.2% to +3.7%), +0.0013 in the gauge's unit; LOSS · 0.294 → 0.2947; raw +0.2% (95%: −2.2% to +2.7%), +0.0007 in the gauge's unit; STEADY · 0.075 → 0.077; raw +2.7% (95%: −8.8% to +14.1%), +0.0020 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, mean (ms), A B C 0.1313 → 0.1317; raw +0.3% (95%: −2.5% to +3.1%), +0.0004 in the gauge's unit; STEADY · 0.1818 → 0.1839; raw +1.2% (95%: −3.7% to +6.0%), +0.0021 in the gauge's unit; LOSS · 0.04938 → 0.04998; raw +1.2% (95%: −2.3% to +4.8%), +0.0006 in the gauge's unit; LOSS. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **Omni-Compass against native.** YCSB on MongoDB, a database's operator-set cache size, native as shipped (omni-v21, `results/live/V21_YCSB_SHIPPED.md`): latency, 95th percentile (ms), A B C 0.4157 → 0.418; raw +0.6% (95%: −2.2% to +3.3%), +0.0023 in the gauge's unit; LOSS · 0.162 → 0.1657; raw +2.3% (95%: −1.6% to +6.1%), +0.0037 in the gauge's unit; LOSS · 0.3997 → 0.4007; raw +0.3% (95%: −1.0% to +1.5%), +0.0010 in the gauge's unit; STEADY. The knob: the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): pod start wait, total (s), A B C 0.4444 → 2.222; raw +400.0% (95%: +25.3% to +774.7%), +1.7778 in the gauge's unit; LOSS · 0.3 → 2.3; raw +666.7% (95%: +176.7% to +1156.6%), +2.0000 in the gauge's unit; LOSS · 0.3 → 1.6; raw +433.3% (95%: −140.3% to +1007.0%), +1.3000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): pod start wait, mean (s), A B C 0.2222 → 1.167; raw +425.0% (95%: +53.6% to +796.4%), +0.9444 in the gauge's unit; LOSS · 0.3 → 1.4; raw +366.7% (95%: +136.3% to +597.0%), +1.1000 in the gauge's unit; LOSS · 0.15 → 0.8917; raw +494.4% (95%: −34.9% to +1023.8%), +0.7417 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): batch: queue finished (s), A B C 872.8 → 1504; raw +72.4% (95%: +61.8% to +82.9%); LOSS · 892.4 → 1505; raw +68.6% (95%: +58.6% to +78.6%); LOSS · 806 → 1505; raw +86.7% (95%: +75.6% to +97.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.09722 → 1158; raw +1190995.2% (95%: +1185985.7% to +1196004.8%), +1157.9120 in the gauge's unit; LOSS · 0.07083 → 1158; raw +1634917.6% (95%: +1630334.8% to +1639500.5%), +1158.0667 in the gauge's unit; LOSS · 0.0875 → 1159; raw +1324419.0% (95%: +1319896.0% to +1328942.1%), +1158.8667 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.6667 → 1474; raw +221050.0% (95%: +220287.4% to +221812.6%), +1473.6667 in the gauge's unit; LOSS · 0.6 → 1474; raw +245633.3% (95%: +245069.1% to +246197.6%), +1473.8000 in the gauge's unit; LOSS · 0.6 → 1475; raw +245750.0% (95%: +245056.6% to +246443.4%), +1474.5000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 184.4 → 1158; raw +528.0% (95%: +478.0% to +578.0%); LOSS · 203.2 → 1158; raw +469.9% (95%: +426.8% to +513.0%); LOSS · 115.3 → 1159; raw +904.9% (95%: +825.1% to +984.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS · 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS · 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): batch: queue finished (s), A B C 872.8 → 1507; raw +72.6% (95%: +62.2% to +83.1%); LOSS · 892.4 → 1503; raw +68.4% (95%: +58.3% to +78.6%); LOSS · 806 → 1505; raw +86.7% (95%: +75.4% to +98.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.09722 → 1160; raw +1193142.9% (95%: +1189052.7% to +1197233.0%), +1160.0000 in the gauge's unit; LOSS · 0.07083 → 1157; raw +1632935.3% (95%: +1629797.0% to +1636073.6%), +1156.6625 in the gauge's unit; LOSS · 0.0875 → 1158; raw +1323895.2% (95%: +1320577.4% to +1327213.0%), +1158.4083 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.6667 → 1476; raw +221366.7% (95%: +220793.7% to +221939.6%), +1475.7778 in the gauge's unit; LOSS · 0.6 → 1473; raw +245383.3% (95%: +244977.9% to +245788.8%), +1472.3000 in the gauge's unit; LOSS · 0.6 → 1475; raw +245666.7% (95%: +245189.8% to +246143.5%), +1474.0000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 184.4 → 1160; raw +529.1% (95%: +479.5% to +578.7%); LOSS · 203.2 → 1157; raw +469.3% (95%: +425.4% to +513.1%); LOSS · 115.3 → 1158; raw +904.5% (95%: +823.7% to +985.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS · 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS · 0 → 24; raw +24.0000 in the gauge's unit (95%: +24.0000 to +24.0000); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), mean, A B C 125.9 → 586.4; raw +365.9% (95%: +157.4% to +574.3%); LOSS · 137.3 → 669.1; raw +387.2% (95%: +211.6% to +562.8%); LOSS · 102.2 → 379.7; raw +271.6% (95%: +1.7% to +541.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 95th percentile, A B C 171.6 → 2510; raw +1362.7% (95%: +633.9% to +2091.4%); LOSS · 186.5 → 2871; raw +1439.3% (95%: +847.3% to +2031.3%); LOSS · 141 → 1533; raw +986.8% (95%: +75.2% to +1898.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): response time (ms), 99th percentile, A B C 197.3 → 3535; raw +1691.7% (95%: +817.5% to +2565.8%); LOSS · 207.1 → 4014; raw +1837.8% (95%: +1123.2% to +2552.5%); LOSS · 162.2 → 2162; raw +1233.4% (95%: +145.9% to +2320.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): time over the response line (% of samples), A B C 0.004241 → 24.76; raw +583748.7% (95%: +317248.1% to +850249.4%), +24.7561 in the gauge's unit; LOSS · 0 → 27.76; raw +27.7590 in the gauge's unit (95%: +17.8729 to +37.6451); LOSS · 0 → 13.96; raw +13.9600 in the gauge's unit (95%: +2.2913 to +25.6287); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): failed requests (%), A B C 0 → 0.007637; raw +0.0076 in the gauge's unit (95%: −0.0100 to +0.0252); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Armada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_ARMADA_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 0 → 12.33; raw +12.3333 in the gauge's unit (95%: +7.0357 to +17.6310); LOSS · 0 → 14; raw +14.0000 in the gauge's unit (95%: +10.0676 to +17.9324); LOSS · 0 → 8.2; raw +8.2000 in the gauge's unit (95%: +2.5094 to +13.8906); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): response time (ms), 95th percentile, A B C 1397 → 1543; raw +10.5% (95%: −0.8% to +21.8%); LOSS · 866.2 → 874.5; raw +1.0% (95%: −10.2% to +12.1%); LOSS · 827.2 → 887.2; raw +7.2% (95%: −3.3% to +17.7%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): response time (ms), 99th percentile, A B C 2014 → 2300; raw +14.2% (95%: −2.7% to +31.2%); LOSS · 1230 → 1327; raw +7.9% (95%: −3.3% to +19.0%); LOSS · 1250 → 1410; raw +12.7% (95%: −3.6% to +29.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 102.4 → 108.4; raw +5.9% (95%: −0.1% to +12.0%); LOSS · 63.56 → 65.27; raw +2.7% (95%: −0.5% to +5.8%); LOSS · 58.77 → 61.38; raw +4.4% (95%: −1.1% to +10.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_ORCH.md`): response time (ms), 99th percentile, A B C 2014 → 2292; raw +13.8% (95%: −0.5% to +28.2%); LOSS · 1230 → 1412; raw +14.7% (95%: −3.2% to +32.7%); LOSS · 1250 → 1375; raw +9.9% (95%: −7.4% to +27.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): time over the response line (% of samples), A B C 16.92 → 20.49; raw +21.1% (95%: +5.3% to +36.8%); LOSS · 8.854 → 12.15; raw +37.2% (95%: +12.4% to +61.9%); LOSS · 10.38 → 13.47; raw +29.8% (95%: +1.0% to +58.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 10.7 → 10.9; raw +1.9% (95%: −2.4% to +6.1%); LOSS · 6 → 7.7; raw +28.3% (95%: −3.0% to +59.6%); LOSS · 7.9 → 8.6; raw +8.9% (95%: −4.7% to +22.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): batch: queue finished (s), A B C 796.8 → 799.8; raw +0.4% (95%: −0.7% to +1.4%); STEADY · 756.2 → 761.1; raw +0.6% (95%: −0.2% to +1.4%); LOSS · 748.4 → 754.2; raw +0.8% (95%: −0.2% to +1.7%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The Kubernetes scheduler with the operator's bin-packing profile under the batch stream, the four ways (omni-v12, `results/live/V12_BINPACK_4W_VS.md`): queue: job turnaround, submitted to done, mean (s), A B C 106.1 → 106.9; raw +0.7% (95%: −6.2% to +7.7%); LOSS · 63.75 → 65.83; raw +3.3% (95%: −2.8% to +9.3%); LOSS · 58.35 → 61.3; raw +5.0% (95%: −4.9% to +15.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BOTH.md`): response time (ms), mean, A B C 146.9 → 150; raw +2.2% (95%: −0.1% to +4.4%); LOSS · 132.1 → 135.3; raw +2.4% (95%: −0.2% to +5.1%); LOSS · 150.4 → 153; raw +1.7% (95%: −1.0% to +4.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_BOTH.md`): pod start wait, total (s), A B C 6.8 → 12.3; raw +80.9% (95%: +32.7% to +129.0%); LOSS · 8 → 13.5; raw +68.8% (95%: +12.8% to +124.7%); LOSS · 7.1 → 12.2; raw +71.8% (95%: +31.7% to +112.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_ORCH.md`): response time (ms), mean, A B C 146.9 → 150.6; raw +2.6% (95%: +0.7% to +4.4%); LOSS · 132.1 → 136.3; raw +3.2% (95%: +0.5% to +5.9%); LOSS · 150.4 → 154.8; raw +2.9% (95%: +0.9% to +5.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_VS.md`): pod start wait, total (s), A B C 6.8 → 10.9; raw +60.3% (95%: +28.4% to +92.2%); LOSS · 6.6 → 10.3; raw +56.1% (95%: +0.6% to +111.6%); LOSS · 7.9 → 12; raw +51.9% (95%: +20.4% to +83.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Crane (Effective HPA, on Kubernetes 1.25) under the batch stream, the four ways (omni-v12, `results/live/V12_CRANE_4W_VS.md`): pod start wait, mean (s), A B C 1.492 → 1.515; raw +1.6% (95%: −21.9% to +25.0%); LOSS · 1.325 → 1.547; raw +16.8% (95%: −11.2% to +44.7%); LOSS · 1.58 → 1.704; raw +7.8% (95%: −8.6% to +24.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), mean, A B C 316.4 → 318.3; raw +0.6% (95%: −8.8% to +10.0%); LOSS · 396.8 → 425; raw +7.1% (95%: −2.9% to +17.1%); LOSS · 347.3 → 371.1; raw +6.9% (95%: −2.3% to +16.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 95th percentile, A B C 1070 → 1519; raw +41.9% (95%: +11.7% to +72.1%); LOSS · 1366 → 1992; raw +45.9% (95%: +20.6% to +71.1%); LOSS · 1135 → 1788; raw +57.5% (95%: +32.2% to +82.7%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): response time (ms), 99th percentile, A B C 1577 → 2288; raw +45.2% (95%: +12.1% to +78.2%); LOSS · 1972 → 2937; raw +48.9% (95%: +22.4% to +75.5%); LOSS · 1712 → 2775; raw +62.1% (95%: +33.1% to +91.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 8.6 → 8.8; raw +2.3% (95%: −13.7% to +18.4%); LOSS · 11.6 → 12.1; raw +4.3% (95%: −3.0% to +11.6%); LOSS · 10.9 → 11.5; raw +5.5% (95%: +0.9% to +10.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): pod start wait, total (s), A B C 0.4 → 0.8; raw +100.0% (95%: −169.2% to +369.2%), +0.4000 in the gauge's unit; LOSS · 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.1001 to +0.9001); LOSS · 0 → 0.5; raw +0.5000 in the gauge's unit (95%: −0.0058 to +1.0058); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): pod start wait, mean (s), A B C 0.2 → 0.8; raw +300.0% (95%: −84.5% to +684.5%), +0.6000 in the gauge's unit; LOSS · 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.1001 to +0.9001); LOSS · 0 → 0.5; raw +0.5000 in the gauge's unit (95%: −0.0058 to +1.0058); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): batch: queue finished (s), A B C 771.5 → 810.9; raw +5.1% (95%: +1.7% to +8.5%); LOSS · 790 → 844.2; raw +6.9% (95%: +3.4% to +10.3%); LOSS · 772.7 → 812.4; raw +5.1% (95%: +3.0% to +7.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.05417 → 1.004; raw +1753.8% (95%: +1040.8% to +2466.9%), +0.9500 in the gauge's unit; LOSS · 0.0625 → 1.079; raw +1626.7% (95%: +910.1% to +2343.3%), +1.0167 in the gauge's unit; LOSS · 0.07917 → 0.8042; raw +915.8% (95%: +807.5% to +1024.0%), +0.7250 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.4 → 2.6; raw +550.0% (95%: +38.6% to +1061.4%), +2.2000 in the gauge's unit; LOSS · 0.4 → 3; raw +650.0% (95%: +129.0% to +1171.0%), +2.6000 in the gauge's unit; LOSS · 0.7 → 1.6; raw +128.6% (95%: +70.6% to +186.6%), +0.9000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 78.3 → 115.9; raw +48.0% (95%: +17.8% to +78.1%); LOSS · 98.16 → 148.6; raw +51.3% (95%: +28.0% to +74.7%); LOSS · 82.27 → 125.4; raw +52.5% (95%: +31.0% to +73.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), mean, A B C 316.4 → 358.1; raw +13.2% (95%: +1.6% to +24.8%); LOSS · 396.8 → 459.4; raw +15.8% (95%: +8.1% to +23.5%); LOSS · 347.3 → 410.9; raw +18.3% (95%: +7.5% to +29.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 95th percentile, A B C 1070 → 1478; raw +38.1% (95%: +7.2% to +69.0%); LOSS · 1366 → 1927; raw +41.1% (95%: +19.5% to +62.6%); LOSS · 1135 → 1712; raw +50.8% (95%: +22.6% to +79.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): response time (ms), 99th percentile, A B C 1577 → 2206; raw +39.9% (95%: +7.8% to +72.1%); LOSS · 1972 → 2841; raw +44.0% (95%: +23.2% to +64.9%); LOSS · 1712 → 2761; raw +61.3% (95%: +30.8% to +91.7%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 8.6 → 8.7; raw +1.2% (95%: −11.5% to +13.8%); LOSS · 11.6 → 12.4; raw +6.9% (95%: +4.3% to +9.5%); LOSS · 10.9 → 11.6; raw +6.4% (95%: +2.0% to +10.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): batch: queue finished (s), A B C 771.5 → 804.2; raw +4.2% (95%: +1.6% to +6.9%); LOSS · 790 → 835; raw +5.7% (95%: +2.8% to +8.6%); LOSS · 772.7 → 807.9; raw +4.6% (95%: +2.7% to +6.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.05417 → 0.8458; raw +1461.5% (95%: +1162.4% to +1760.7%), +0.7917 in the gauge's unit; LOSS · 0.0625 → 1.071; raw +1613.3% (95%: +1157.7% to +2069.0%), +1.0083 in the gauge's unit; LOSS · 0.07917 → 0.8458; raw +968.4% (95%: +828.5% to +1108.4%), +0.7667 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.4 → 1.6; raw +300.0% (95%: +115.3% to +484.7%), +1.2000 in the gauge's unit; LOSS · 0.4 → 2.6; raw +550.0% (95%: +225.7% to +874.3%), +2.2000 in the gauge's unit; LOSS · 0.7 → 1.4; raw +100.0% (95%: +31.0% to +169.0%), +0.7000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 78.3 → 109.7; raw +40.1% (95%: +16.1% to +64.0%); LOSS · 98.16 → 139.5; raw +42.1% (95%: +24.1% to +60.0%); LOSS · 82.27 → 119.4; raw +45.2% (95%: +26.8% to +63.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** The KAI scheduler under the batch stream, the four ways (omni-v12, `results/live/V12_KAI_4W_VS.md`): time over the response line (% of samples), A B C 13.22 → 15.37; raw +16.2% (95%: +5.8% to +26.6%); LOSS · 18.89 → 19.84; raw +5.0% (95%: −12.2% to +22.3%); LOSS · 17.63 → 19.09; raw +8.2% (95%: −2.0% to +18.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), mean, A B C 555 → 808.5; raw +45.7% (95%: +15.8% to +75.5%); LOSS · 574.4 → 764.6; raw +33.1% (95%: +14.0% to +52.3%); LOSS · 694 → 867.4; raw +25.0% (95%: +7.6% to +42.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 95th percentile, A B C 2164 → 3923; raw +81.3% (95%: +33.4% to +129.1%); LOSS · 2260 → 3665; raw +62.1% (95%: +27.0% to +97.3%); LOSS · 2707 → 3759; raw +38.8% (95%: +13.8% to +63.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): response time (ms), 99th percentile, A B C 3077 → 5337; raw +73.4% (95%: +34.4% to +112.5%); LOSS · 3117 → 5114; raw +64.1% (95%: +30.5% to +97.7%); LOSS · 3712 → 5069; raw +36.5% (95%: +13.7% to +59.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): time over the response line (% of samples), A B C 21.93 → 25.85; raw +17.9% (95%: +8.8% to +27.1%); LOSS · 22.45 → 25.28; raw +12.6% (95%: +0.3% to +25.0%); LOSS · 22.87 → 28; raw +22.4% (95%: +7.1% to +37.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): failed requests (%), A B C 0.0157 → 0.159; raw +912.6% (95%: +76.0% to +1749.3%), +0.1433 in the gauge's unit; LOSS · 0 → 0.1452; raw +0.1452 in the gauge's unit (95%: −0.0085 to +0.2990); LOSS · 0.01501 → 0.1831; raw +1119.8% (95%: −207.1% to +2446.7%), +0.1681 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 11.33 → 16.44; raw +45.1% (95%: +21.3% to +68.9%); LOSS · 11.3 → 15.2; raw +34.5% (95%: +21.0% to +48.0%); LOSS · 10.4 → 13.6; raw +30.8% (95%: +18.3% to +43.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): pod start wait, total (s), A B C 0.5556 → 3.889; raw +600.0% (95%: −258.5% to +1458.5%), +3.3333 in the gauge's unit; LOSS · 0 → 1.9; raw +1.9000 in the gauge's unit (95%: +0.4914 to +3.3086); LOSS · 0 → 2.2; raw +2.2000 in the gauge's unit (95%: −0.0820 to +4.4820); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): pod start wait, mean (s), A B C 0.5556 → 1.101; raw +98.1% (95%: −145.9% to +342.1%), +0.5450 in the gauge's unit; LOSS · 0 → 1.033; raw +1.0333 in the gauge's unit (95%: +0.3341 to +1.7326); LOSS · 0 → 1.225; raw +1.2250 in the gauge's unit (95%: +0.2048 to +2.2452); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): batch: queue finished (s), A B C 852.7 → 993.1; raw +16.5% (95%: +7.4% to +25.6%); LOSS · 856.4 → 991; raw +15.7% (95%: +8.5% to +23.0%); LOSS · 909.9 → 1040; raw +14.3% (95%: +5.7% to +22.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.07407 → 1.963; raw +2550.0% (95%: −2197.6% to +7297.6%), +1.8889 in the gauge's unit; LOSS · 0.1042 → 3.271; raw +3040.0% (95%: −1048.9% to +7128.9%), +3.1667 in the gauge's unit; LOSS · 0.0875 → 16.2; raw +18419.0% (95%: +3305.6% to +33532.5%), +16.1167 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.5556 → 1.556; raw +180.0% (95%: +82.2% to +277.8%), +1.0000 in the gauge's unit; LOSS · 0.6 → 1.7; raw +183.3% (95%: +52.1% to +314.5%), +1.1000 in the gauge's unit; LOSS · 0.5 → 122.3; raw +24360.0% (95%: +1893.1% to +46826.9%), +121.8000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 163.2 → 298.7; raw +83.0% (95%: +40.0% to +126.1%); LOSS · 167.6 → 298.5; raw +78.2% (95%: +42.6% to +113.8%); LOSS · 216.2 → 341.4; raw +57.9% (95%: +24.1% to +91.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), mean, A B C 555 → 709.8; raw +27.9% (95%: +13.5% to +42.3%); LOSS · 574.4 → 691.8; raw +20.4% (95%: +10.8% to +30.0%); LOSS · 694 → 844.3; raw +21.6% (95%: +7.9% to +35.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 95th percentile, A B C 2164 → 3269; raw +51.1% (95%: +21.9% to +80.2%); LOSS · 2260 → 3140; raw +38.9% (95%: +18.4% to +59.5%); LOSS · 2707 → 3666; raw +35.4% (95%: +13.9% to +56.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): response time (ms), 99th percentile, A B C 3077 → 4767; raw +54.9% (95%: +23.6% to +86.2%); LOSS · 3117 → 4602; raw +47.7% (95%: +25.1% to +70.2%); LOSS · 3712 → 4876; raw +31.3% (95%: +13.1% to +49.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): time over the response line (% of samples), A B C 21.93 → 24.64; raw +12.4% (95%: +0.5% to +24.3%); LOSS · 22.45 → 23.99; raw +6.9% (95%: −6.2% to +19.9%); LOSS · 22.87 → 25.85; raw +13.0% (95%: +4.3% to +21.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): failed requests (%), A B C 0.0157 → 0.08233; raw +424.2% (95%: −104.6% to +953.0%), +0.0666 in the gauge's unit; LOSS · 0 → 0.0524; raw +0.0524 in the gauge's unit (95%: −0.0355 to +0.1403); LOSS · 0.01501 → 0.06374; raw +324.7% (95%: −281.1% to +930.4%), +0.0487 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 11.33 → 15.22; raw +34.3% (95%: +13.3% to +55.3%); LOSS · 11.3 → 13.8; raw +22.1% (95%: +12.1% to +32.1%); LOSS · 10.4 → 13.7; raw +31.7% (95%: +8.1% to +55.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): pod start wait, total (s), A B C 0.5556 → 1.111; raw +100.0% (95%: −239.7% to +439.7%), +0.5556 in the gauge's unit; LOSS · 0 → 1.1; raw +1.1000 in the gauge's unit (95%: −0.2676 to +2.4676); LOSS · 0 → 1.1; raw +1.1000 in the gauge's unit (95%: −0.2254 to +2.4254); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): pod start wait, mean (s), A B C 0.5556 → 0.8333; raw +50.0% (95%: −224.8% to +324.8%), +0.2778 in the gauge's unit; LOSS · 0 → 0.65; raw +0.6500 in the gauge's unit (95%: −0.1049 to +1.4049); LOSS · 0 → 0.85; raw +0.8500 in the gauge's unit (95%: −0.1338 to +1.8338); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): batch: queue finished (s), A B C 852.7 → 952.2; raw +11.7% (95%: +5.1% to +18.3%); LOSS · 856.4 → 952.2; raw +11.2% (95%: +6.1% to +16.2%); LOSS · 909.9 → 1010; raw +11.0% (95%: +5.0% to +16.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.07407 → 3.431; raw +4531.3% (95%: −4930.2% to +13992.7%), +3.3565 in the gauge's unit; LOSS · 0.1042 → 1.867; raw +1692.0% (95%: −1263.7% to +4647.7%), +1.7625 in the gauge's unit; LOSS · 0.0875 → 9.812; raw +11114.3% (95%: −373.7% to +22602.3%), +9.7250 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.5556 → 36.89; raw +6540.0% (95%: −8333.9% to +21413.9%), +36.3333 in the gauge's unit; LOSS · 0.6 → 1.5; raw +150.0% (95%: +31.4% to +268.6%), +0.9000 in the gauge's unit; LOSS · 0.5 → 64.4; raw +12780.0% (95%: −6059.7% to +31619.7%), +63.9000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 163.2 → 258.1; raw +58.2% (95%: +28.9% to +87.5%); LOSS · 167.6 → 261.5; raw +56.1% (95%: +30.6% to +81.6%); LOSS · 216.2 → 311.6; raw +44.2% (95%: +20.7% to +67.7%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_VS.md`): pod start wait, total (s), A B C 1.111 → 2.222; raw +100.0% (95%: −48.6% to +248.6%); LOSS · 1.1 → 1.2; raw +9.1% (95%: −162.8% to +181.0%); LOSS · 1.1 → 1.9; raw +72.7% (95%: −105.5% to +250.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Karmada on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_KARMADA_4W_VS.md`): pod start wait, mean (s), A B C 0.8333 → 1.389; raw +66.7% (95%: −35.0% to +168.4%), +0.5556 in the gauge's unit; LOSS · 0.65 → 0.95; raw +46.2% (95%: −124.3% to +216.6%), +0.3000 in the gauge's unit; LOSS · 0.85 → 1.25; raw +47.1% (95%: −53.7% to +147.8%), +0.4000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): pod start wait, total (s), A B C 0.2 → 0.3; raw +50.0% (95%: −63.1% to +163.1%), +0.1000 in the gauge's unit; LOSS · 0 → 0.7; raw +0.7000 in the gauge's unit (95%: −0.1294 to +1.5294); LOSS · 0.2 → 0.2; raw ±0.0% (95%: −337.2% to +337.2%), ±0.0000 in the gauge's unit; STEADY. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): batch: queue finished (s), A B C 731 → 1313; raw +79.6% (95%: +57.4% to +101.8%); LOSS · 778.8 → 1421; raw +82.5% (95%: +72.2% to +92.7%); LOSS · 747.2 → 1421; raw +90.2% (95%: +71.9% to +108.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.03333 → 110.9; raw +332575.0% (95%: +204178.2% to +460971.8%), +110.8583 in the gauge's unit; LOSS · 0.025 → 175.4; raw +701433.3% (95%: +502619.2% to +900247.5%), +175.3583 in the gauge's unit; LOSS · 0.0625 → 142.5; raw +227980.0% (95%: +149811.1% to +306148.9%), +142.4875 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 518.5; raw +172733.3% (95%: +104746.8% to +240719.9%), +518.2000 in the gauge's unit; LOSS · 0.1 → 763.9; raw +763800.0% (95%: +530043.0% to +997557.0%), +763.8000 in the gauge's unit; LOSS · 0.5 → 684.4; raw +136780.0% (95%: +86044.3% to +187515.7%), +683.9000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 38.07 → 650.2; raw +1607.8% (95%: +1081.3% to +2134.4%); LOSS · 85.79 → 814.5; raw +849.4% (95%: +675.6% to +1023.2%); LOSS · 55.45 → 789; raw +1322.9% (95%: +1027.8% to +1618.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C 0 → 5.3; raw +5.3000 in the gauge's unit (95%: −0.8906 to +11.4906); LOSS · 0 → 10.7; raw +10.7000 in the gauge's unit (95%: +4.0490 to +17.3510); LOSS · 0 → 8.8; raw +8.8000 in the gauge's unit (95%: +3.2613 to +14.3387); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): batch: queue finished (s), A B C 731 → 1290; raw +76.5% (95%: +54.1% to +98.9%); LOSS · 778.8 → 1421; raw +82.5% (95%: +72.8% to +92.1%); LOSS · 747.2 → 1396; raw +86.9% (95%: +68.4% to +105.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.03333 → 103.6; raw +310637.5% (95%: +166814.0% to +454461.0%), +103.5458 in the gauge's unit; LOSS · 0.025 → 171.5; raw +686083.3% (95%: +439006.5% to +933160.2%), +171.5208 in the gauge's unit; LOSS · 0.0625 → 146.3; raw +233933.3% (95%: +162122.7% to +305743.9%), +146.2083 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 513.9; raw +171200.0% (95%: +91149.9% to +251250.1%), +513.6000 in the gauge's unit; LOSS · 0.1 → 798; raw +797900.0% (95%: +545467.5% to +1050332.5%), +797.9000 in the gauge's unit; LOSS · 0.5 → 698.5; raw +139600.0% (95%: +101748.5% to +177451.5%), +698.0000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 38.07 → 614; raw +1512.7% (95%: +1011.0% to +2014.4%); LOSS · 85.79 → 799.3; raw +831.8% (95%: +691.5% to +972.0%); LOSS · 55.45 → 763.3; raw +1276.6% (95%: +979.1% to +1574.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C 0 → 4.9; raw +4.9000 in the gauge's unit (95%: −0.7971 to +10.5971); LOSS · 0 → 9.4; raw +9.4000 in the gauge's unit (95%: +3.5091 to +15.2909); LOSS · 0 → 9.6; raw +9.6000 in the gauge's unit (95%: +3.5005 to +15.6995); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), mean, A B C 113 → 158.7; raw +40.4% (95%: −3.0% to +83.9%); LOSS · 131.2 → 325.7; raw +148.2% (95%: +55.6% to +240.8%); LOSS · 141.2 → 242; raw +71.4% (95%: +13.0% to +129.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 95th percentile, A B C 194.7 → 567.1; raw +191.2% (95%: +63.6% to +318.8%); LOSS · 234.3 → 1372; raw +485.5% (95%: +212.9% to +758.0%); LOSS · 236.9 → 913.5; raw +285.6% (95%: +106.4% to +464.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): response time (ms), 99th percentile, A B C 291 → 818.7; raw +181.3% (95%: +56.9% to +305.8%); LOSS · 345.6 → 2010; raw +481.6% (95%: +212.0% to +751.1%); LOSS · 336.7 → 1296; raw +285.0% (95%: +116.9% to +453.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): time over the response line (% of samples), A B C 0.1615 → 7.237; raw +4381.5% (95%: −131.3% to +8894.3%), +7.0757 in the gauge's unit; LOSS · 0.2311 → 17.38; raw +7419.5% (95%: +3065.0% to +11774.0%), +17.1481 in the gauge's unit; LOSS · 0.1697 → 13.87; raw +8073.6% (95%: +3500.6% to +12646.7%), +13.6994 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Koordinator under the batch stream, the four ways (omni-v12, `results/live/V12_KOORDINATOR_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 0 → 4.9; raw +4.9000 in the gauge's unit (95%: +0.7503 to +9.0497); LOSS · 0.1 → 9; raw +8900.0% (95%: +4446.3% to +13353.7%), +8.9000 in the gauge's unit; LOSS · 0.1 → 9.6; raw +9500.0% (95%: +6140.7% to +12859.3%), +9.5000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): response time (ms), mean, A B C 330.3 → 613.4; raw +85.7% (95%: +68.2% to +103.3%); LOSS · 317.1 → 587; raw +85.1% (95%: +68.5% to +101.7%); LOSS · 405.7 → 677.4; raw +67.0% (95%: +49.1% to +84.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): time over the response line (% of samples), A B C 16.77 → 52.45; raw +212.8% (95%: +175.6% to +250.1%); LOSS · 15.06 → 48.66; raw +223.2% (95%: +172.9% to +273.6%); LOSS · 19.25 → 59.29; raw +207.9% (95%: +172.9% to +243.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 8 → 24.22; raw +202.8% (95%: +146.0% to +259.6%); LOSS · 7.3 → 23.1; raw +216.4% (95%: +168.3% to +264.6%); LOSS · 9.3 → 23.9; raw +157.0% (95%: +115.5% to +198.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): pod start wait, total (s), A B C 0 → 1.111; raw +1.1111 in the gauge's unit (95%: −0.2981 to +2.5203); LOSS · 0 → 0.2; raw +0.2000 in the gauge's unit (95%: −0.2524 to +0.6524); LOSS · 0 → 0.8; raw +0.8000 in the gauge's unit (95%: −0.0121 to +1.6121); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): pod start wait, mean (s), A B C 0 → 0.7407; raw +0.7407 in the gauge's unit (95%: −0.1540 to +1.6355); LOSS · 0 → 0.2; raw +0.2000 in the gauge's unit (95%: −0.2524 to +0.6524); LOSS · 0 → 0.8; raw +0.8000 in the gauge's unit (95%: −0.0121 to +1.6121); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): batch: queue finished (s), A B C 774.1 → 1466; raw +89.3% (95%: +79.7% to +98.9%); LOSS · 775.3 → 1396; raw +80.1% (95%: +69.7% to +90.5%); LOSS · 802.6 → 1451; raw +80.8% (95%: +71.6% to +90.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.03241 → 637.5; raw +1967119.6% (95%: +1111934.3% to +2822304.9%), +637.4925 in the gauge's unit; LOSS · 0.04167 → 536.6; raw +1287745.8% (95%: +521467.2% to +2054024.4%), +536.5607 in the gauge's unit; LOSS · 0.05417 → 677.6; raw +1250833.4% (95%: +747221.5% to +1754445.3%), +677.5348 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.1111 → 1113; raw +1001696.3% (95%: +623421.0% to +1379971.7%), +1112.9959 in the gauge's unit; LOSS · 0.4 → 924.3; raw +230987.0% (95%: +116467.0% to +345506.9%), +923.9479 in the gauge's unit; LOSS · 0.4 → 1141; raw +285052.5% (95%: +193399.9% to +376705.2%), +1140.2102 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 81.79 → 955; raw +1067.6% (95%: +891.6% to +1243.7%); LOSS · 83.3 → 841.3; raw +910.0% (95%: +690.2% to +1129.8%); LOSS · 107.6 → 941.7; raw +774.9% (95%: +649.7% to +900.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_BOTH.md`): queue: jobs unfinished at the window's end, A B C 0 → 13.44; raw +13.4444 in the gauge's unit (95%: +7.1631 to +19.7258); LOSS · 0 → 11.3; raw +11.3000 in the gauge's unit (95%: +3.8583 to +18.7417); LOSS · 0 → 14.5; raw +14.5000 in the gauge's unit (95%: +8.3259 to +20.6741); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): response time (ms), mean, A B C 330.3 → 620.7; raw +87.9% (95%: +61.0% to +114.8%); LOSS · 317.1 → 591.8; raw +86.6% (95%: +61.9% to +111.4%); LOSS · 405.7 → 692.2; raw +70.6% (95%: +49.8% to +91.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): time over the response line (% of samples), A B C 16.77 → 53.85; raw +221.2% (95%: +183.5% to +258.9%); LOSS · 15.06 → 50.32; raw +234.2% (95%: +179.7% to +288.8%); LOSS · 19.25 → 61.12; raw +217.5% (95%: +182.6% to +252.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 8 → 24.33; raw +204.2% (95%: +145.9% to +262.4%); LOSS · 7.3 → 23.3; raw +219.2% (95%: +169.2% to +269.1%); LOSS · 9.3 → 24.1; raw +159.1% (95%: +116.0% to +202.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): pod start wait, total (s), A B C 0 → 0.2222; raw +0.2222 in the gauge's unit (95%: −0.2902 to +0.7347); LOSS · 0 → 0.8; raw +0.8000 in the gauge's unit (95%: −0.4526 to +2.0526); LOSS · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.1828 to +0.7828); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): pod start wait, mean (s), A B C 0 → 0.2222; raw +0.2222 in the gauge's unit (95%: −0.2902 to +0.7347); LOSS · 0 → 0.55; raw +0.5500 in the gauge's unit (95%: −0.2837 to +1.3837); LOSS · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.1828 to +0.7828); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): batch: queue finished (s), A B C 774.1 → 1474; raw +90.4% (95%: +80.4% to +100.4%); LOSS · 775.3 → 1400; raw +80.6% (95%: +70.9% to +90.3%); LOSS · 802.6 → 1456; raw +81.4% (95%: +72.4% to +90.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.03241 → 635; raw +1959438.6% (95%: +1137492.1% to +2781385.0%), +635.0032 in the gauge's unit; LOSS · 0.04167 → 533.6; raw +1280430.0% (95%: +511805.8% to +2049054.2%), +533.5125 in the gauge's unit; LOSS · 0.05417 → 670.7; raw +1238207.0% (95%: +751232.1% to +1725181.9%), +670.6955 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.1111 → 1129; raw +1015791.5% (95%: +684899.6% to +1346683.4%), +1128.6572 in the gauge's unit; LOSS · 0.4 → 914.7; raw +228574.2% (95%: +114225.9% to +342922.5%), +914.2970 in the gauge's unit; LOSS · 0.4 → 1145; raw +286211.2% (95%: +190609.6% to +381812.7%), +1144.8447 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 81.79 → 954.8; raw +1067.4% (95%: +882.4% to +1252.3%); LOSS · 83.3 → 855.5; raw +927.0% (95%: +727.3% to +1126.7%); LOSS · 107.6 → 946.3; raw +779.3% (95%: +655.6% to +902.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** KubeRay (the Ray autoscaler) under the batch stream, the four ways (omni-v12, `results/live/V12_KUBERAY_4W_ORCH.md`): queue: jobs unfinished at the window's end, A B C 0 → 14.33; raw +14.3333 in the gauge's unit (95%: +8.2201 to +20.4465); LOSS · 0 → 11.1; raw +11.1000 in the gauge's unit (95%: +3.7552 to +18.4448); LOSS · 0 → 14.6; raw +14.6000 in the gauge's unit (95%: +8.6134 to +20.5866); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): response time (ms), 95th percentile, A B C 1006 → 1101; raw +9.5% (95%: +1.9% to +17.1%); LOSS · 1151 → 1305; raw +13.4% (95%: +3.4% to +23.4%); LOSS · 1278 → 1474; raw +15.4% (95%: +7.8% to +22.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): response time (ms), 99th percentile, A B C 1451 → 1605; raw +10.6% (95%: −0.7% to +22.0%); LOSS · 1720 → 1946; raw +13.1% (95%: +4.1% to +22.1%); LOSS · 1825 → 2040; raw +11.8% (95%: +3.7% to +19.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): failed requests (%), A B C 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY · 0 → 0.009302; raw +0.0093 in the gauge's unit (95%: −0.0117 to +0.0303); LOSS · 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000); STEADY. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 7.8 → 8; raw +2.6% (95%: −5.9% to +11.0%); LOSS · 10.2 → 10.6; raw +3.9% (95%: −1.0% to +8.8%); LOSS · 11 → 11.33; raw +3.0% (95%: −0.5% to +6.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): pod start wait, total (s), A B C 0 → 0.1; raw +0.1000 in the gauge's unit (95%: −0.1262 to +0.3262); LOSS · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.1828 to +0.7828); LOSS · 0 → 1.222; raw +1.2222 in the gauge's unit (95%: −0.3983 to +2.8427); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): pod start wait, mean (s), A B C 0 → 0.1; raw +0.1000 in the gauge's unit (95%: −0.1262 to +0.3262); LOSS · 0 → 0.3; raw +0.3000 in the gauge's unit (95%: −0.1828 to +0.7828); LOSS · 0 → 0.7222; raw +0.7222 in the gauge's unit (95%: −0.1607 to +1.6052); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): batch: queue finished (s), A B C 768.1 → 775.8; raw +1.0% (95%: +0.3% to +1.7%); LOSS · 772.9 → 785.5; raw +1.6% (95%: +0.8% to +2.5%); LOSS · 779.2 → 794.2; raw +1.9% (95%: +1.1% to +2.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.05833 → 0.1667; raw +185.7% (95%: −48.1% to +419.5%), +0.1083 in the gauge's unit; LOSS · 0.09167 → 0.2; raw +118.2% (95%: +27.2% to +209.1%), +0.1083 in the gauge's unit; LOSS · 0.03704 → 0.2361; raw +537.5% (95%: +360.4% to +714.6%), +0.1991 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 0.6; raw +100.0% (95%: −15.2% to +215.2%), +0.3000 in the gauge's unit; LOSS · 0.8 → 0.8; raw ±0.0% (95%: −42.1% to +42.1%), ±0.0000 in the gauge's unit; STEADY · 0.1111 → 1; raw +800.0% (95%: +569.4% to +1030.6%), +0.8889 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 73.89 → 83.16; raw +12.5% (95%: +3.2% to +21.8%); LOSS · 81.23 → 92.45; raw +13.8% (95%: +6.4% to +21.3%); LOSS · 87.61 → 102.1; raw +16.6% (95%: +8.6% to +24.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), mean, A B C 307 → 329.3; raw +7.3% (95%: ±0.0% to +14.5%); LOSS · 346.2 → 368.3; raw +6.4% (95%: +1.8% to +11.0%); LOSS · 371.1 → 404; raw +8.9% (95%: +3.7% to +14.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), 95th percentile, A B C 1006 → 1134; raw +12.8% (95%: +0.3% to +25.2%); LOSS · 1151 → 1266; raw +10.0% (95%: +1.4% to +18.7%); LOSS · 1278 → 1409; raw +10.2% (95%: +2.9% to +17.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): response time (ms), 99th percentile, A B C 1451 → 1643; raw +13.2% (95%: −1.3% to +27.7%); LOSS · 1720 → 1841; raw +7.0% (95%: +0.4% to +13.6%); LOSS · 1825 → 2029; raw +11.1% (95%: +5.0% to +17.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): time over the response line (% of samples), A B C 14.95 → 15.73; raw +5.2% (95%: −0.2% to +10.5%); LOSS · 20.05 → 20.83; raw +3.9% (95%: −0.7% to +8.5%); LOSS · 21.68 → 23.23; raw +7.2% (95%: +2.9% to +11.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 7.8 → 7.8; raw ±0.0% (95%: −6.1% to +6.1%); STEADY · 10.2 → 10.3; raw +1.0% (95%: −6.0% to +8.0%); LOSS · 11 → 11.11; raw +1.0% (95%: −1.3% to +3.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): pod start wait, total (s), A B C 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.5048 to +1.3048); LOSS · 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.5048 to +1.3048); LOSS · 0 → 0.3333; raw +0.3333 in the gauge's unit (95%: −0.4353 to +1.1020); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): pod start wait, mean (s), A B C 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.5048 to +1.3048); LOSS · 0 → 0.4; raw +0.4000 in the gauge's unit (95%: −0.5048 to +1.3048); LOSS · 0 → 0.3333; raw +0.3333 in the gauge's unit (95%: −0.4353 to +1.1020); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): batch: queue finished (s), A B C 768.1 → 775.1; raw +0.9% (95%: −0.1% to +1.9%); LOSS · 772.9 → 781.3; raw +1.1% (95%: +0.3% to +1.8%); LOSS · 779.2 → 790.4; raw +1.4% (95%: +0.6% to +2.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.05833 → 0.1625; raw +178.6% (95%: +75.7% to +281.5%), +0.1042 in the gauge's unit; LOSS · 0.09167 → 0.2; raw +118.2% (95%: +22.2% to +214.1%), +0.1083 in the gauge's unit; LOSS · 0.03704 → 0.2361; raw +537.5% (95%: +313.8% to +761.2%), +0.1991 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 1; raw +233.3% (95%: +118.2% to +348.5%), +0.7000 in the gauge's unit; LOSS · 0.8 → 1; raw +25.0% (95%: −12.7% to +62.7%), +0.2000 in the gauge's unit; LOSS · 0.1111 → 0.8889; raw +700.0% (95%: +394.9% to +1005.1%), +0.7778 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Kueue under the batch stream, the four ways (omni-v12, `results/live/V12_KUEUE_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 73.89 → 82.38; raw +11.5% (95%: +0.3% to +22.7%); LOSS · 81.23 → 88.75; raw +9.3% (95%: +2.0% to +16.5%); LOSS · 87.61 → 98.69; raw +12.7% (95%: +5.4% to +19.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), mean, A B C 752.2 → 1203; raw +59.9% (95%: +38.6% to +81.3%); LOSS · 665.7 → 1010; raw +51.7% (95%: +23.3% to +80.0%); LOSS · 630.1 → 1000; raw +58.7% (95%: +37.1% to +80.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 95th percentile, A B C 2969 → 4499; raw +51.5% (95%: +36.6% to +66.4%); LOSS · 2682 → 4162; raw +55.2% (95%: +22.4% to +88.0%); LOSS · 2493 → 3866; raw +55.0% (95%: +29.0% to +81.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): response time (ms), 99th percentile, A B C 4041 → 6036; raw +49.4% (95%: +31.0% to +67.8%); LOSS · 3704 → 5867; raw +58.4% (95%: +25.9% to +90.9%); LOSS · 3409 → 5213; raw +52.9% (95%: +30.2% to +75.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): time over the response line (% of samples), A B C 28.08 → 43.77; raw +55.9% (95%: +30.2% to +81.5%); LOSS · 26.74 → 33.12; raw +23.9% (95%: +11.2% to +36.5%); LOSS · 21.13 → 37.09; raw +75.5% (95%: +53.5% to +97.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): failed requests (%), A B C 0.04202 → 0.4937; raw +1075.1% (95%: −954.5% to +3104.7%), +0.4517 in the gauge's unit; LOSS · 0.007491 → 0.1132; raw +1410.9% (95%: −485.9% to +3307.7%), +0.1057 in the gauge's unit; LOSS · 0.03597 → 0.05082; raw +41.3% (95%: −219.2% to +301.7%), +0.0148 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 14.9 → 18.6; raw +24.8% (95%: +18.0% to +31.6%); LOSS · 12.4 → 15.7; raw +26.6% (95%: +20.5% to +32.7%); LOSS · 10.1 → 17.6; raw +74.3% (95%: +40.2% to +108.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): pod start wait, total (s), A B C 0.8 → 2.9; raw +262.5% (95%: −113.2% to +638.2%), +2.1000 in the gauge's unit; LOSS · 0.2 → 2.9; raw +1350.0% (95%: +337.7% to +2362.3%), +2.7000 in the gauge's unit; LOSS · 0.6 → 5; raw +733.3% (95%: −39.7% to +1506.4%), +4.4000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): pod start wait, mean (s), A B C 0.55 → 1.55; raw +181.8% (95%: −92.4% to +456.0%), +1.0000 in the gauge's unit; LOSS · 0.2 → 1.617; raw +708.3% (95%: +164.7% to +1251.9%), +1.4167 in the gauge's unit; LOSS · 0.4 → 2.467; raw +516.7% (95%: −69.1% to +1102.4%), +2.0667 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): batch: queue finished (s), A B C 911.9 → 1107; raw +21.4% (95%: +16.0% to +26.8%); LOSS · 885.4 → 1058; raw +19.4% (95%: +11.5% to +27.4%); LOSS · 881.5 → 1050; raw +19.1% (95%: +13.1% to +25.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.1542 → 22.47; raw +14475.7% (95%: +1985.4% to +26966.0%), +22.3167 in the gauge's unit; LOSS · 0.1167 → 18.62; raw +15860.7% (95%: +1447.0% to +30274.5%), +18.5042 in the gauge's unit; LOSS · 0.075 → 13.05; raw +17305.6% (95%: +349.2% to +34262.0%), +12.9792 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.7 → 159.5; raw +22685.7% (95%: +4894.5% to +40476.9%), +158.8000 in the gauge's unit; LOSS · 0.8 → 105.6; raw +13100.0% (95%: +1240.5% to +24959.5%), +104.8000 in the gauge's unit; LOSS · 0.5 → 85.4; raw +16980.0% (95%: +170.1% to +33789.9%), +84.9000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 222.3 → 380; raw +70.9% (95%: +54.6% to +87.2%); LOSS · 194.8 → 326.8; raw +67.7% (95%: +38.0% to +97.5%); LOSS · 190.6 → 337.1; raw +76.8% (95%: +55.5% to +98.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), mean, A B C 752.2 → 1080; raw +43.6% (95%: +24.2% to +62.9%); LOSS · 665.7 → 1041; raw +56.4% (95%: +31.6% to +81.2%); LOSS · 630.1 → 729.1; raw +15.7% (95%: −32.1% to +63.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), 95th percentile, A B C 2969 → 4119; raw +38.7% (95%: +19.4% to +58.1%); LOSS · 2682 → 4095; raw +52.7% (95%: +28.2% to +77.2%); LOSS · 2493 → 2738; raw +9.8% (95%: −42.8% to +62.5%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): response time (ms), 99th percentile, A B C 4041 → 5429; raw +34.4% (95%: +13.7% to +55.0%); LOSS · 3704 → 5491; raw +48.2% (95%: +27.5% to +69.0%); LOSS · 3409 → 3776; raw +10.8% (95%: −40.6% to +62.1%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): time over the response line (% of samples), A B C 28.08 → 38.86; raw +38.4% (95%: +26.1% to +50.6%); LOSS · 26.74 → 33.85; raw +26.6% (95%: +12.2% to +41.0%); LOSS · 21.13 → 24.85; raw +17.6% (95%: −34.5% to +69.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 14.9 → 17.6; raw +18.1% (95%: +12.6% to +23.7%); LOSS · 12.4 → 14.8; raw +19.4% (95%: +10.7% to +28.0%); LOSS · 10.1 → 12.1; raw +19.8% (95%: −34.2% to +73.8%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): batch: queue finished (s), A B C 911.9 → 1049; raw +15.0% (95%: +9.3% to +20.7%); LOSS · 885.4 → 1026; raw +15.9% (95%: +9.3% to +22.6%); LOSS · 881.5 → 1023; raw +16.1% (95%: +4.7% to +27.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.1542 → 7.229; raw +4589.2% (95%: −3377.6% to +12556.0%), +7.0750 in the gauge's unit; LOSS · 0.1167 → 6.929; raw +5839.3% (95%: +343.3% to +11335.2%), +6.8125 in the gauge's unit; LOSS · 0.075 → 3.135; raw +4080.2% (95%: −2342.8% to +10503.3%), +3.0602 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.7 → 39.4; raw +5528.6% (95%: −3642.5% to +14699.6%), +38.7000 in the gauge's unit; LOSS · 0.8 → 55.9; raw +6887.5% (95%: −217.2% to +13992.2%), +55.1000 in the gauge's unit; LOSS · 0.5 → 6.389; raw +1177.8% (95%: −860.9% to +3216.5%), +5.8889 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 222.3 → 328.8; raw +47.9% (95%: +27.4% to +68.3%); LOSS · 194.8 → 305.8; raw +57.0% (95%: +30.7% to +83.2%); LOSS · 190.6 → 278.3; raw +46.0% (95%: +18.7% to +73.3%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, total (s), A B C 0.3 → 1.7; raw +466.7% (95%: +186.8% to +746.5%), +1.4000 in the gauge's unit; LOSS · 0 → 2.4; raw +2.4000 in the gauge's unit (95%: +0.9225 to +3.8775); LOSS · 0 → 1.3; raw +1.3000 in the gauge's unit (95%: +0.4047 to +2.1953); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Open Cluster Management on the group of two clusters under the batch stream, the four ways (omni-v12, `results/live/V12_OCM_4W_VS.md`): pod start wait, mean (s), A B C 0.3 → 1.1; raw +266.7% (95%: +26.9% to +506.4%), +0.8000 in the gauge's unit; LOSS · 0 → 1.25; raw +1.2500 in the gauge's unit (95%: +0.6136 to +1.8864); LOSS · 0 → 0.8; raw +0.8000 in the gauge's unit (95%: +0.2615 to +1.3385); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): pod start wait, total (s), A B C 0.4 → 0.4; raw ±0.0% (95%: −168.6% to +168.6%), ±0.0000 in the gauge's unit; STEADY · 0.3 → 1.4; raw +366.7% (95%: −477.8% to +1211.2%), +1.1000 in the gauge's unit; LOSS · 0.2 → 1.2; raw +500.0% (95%: −326.0% to +1326.0%), +1.0000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): pod start wait, mean (s), A B C 0.2 → 0.4; raw +100.0% (95%: −126.2% to +326.2%), +0.2000 in the gauge's unit; LOSS · 0.15 → 0.7; raw +366.7% (95%: −477.8% to +1211.2%), +0.5500 in the gauge's unit; LOSS · 0.2 → 1.2; raw +500.0% (95%: −326.0% to +1326.0%), +1.0000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): batch: queue finished (s), A B C 758.7 → 772.3; raw +1.8% (95%: +0.8% to +2.8%); LOSS · 780.2 → 793.3; raw +1.7% (95%: +0.4% to +2.9%); LOSS · 770.9 → 784.7; raw +1.8% (95%: +0.4% to +3.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.0625 → 0.7667; raw +1126.7% (95%: +1020.2% to +1233.2%), +0.7042 in the gauge's unit; LOSS · 0.075 → 0.8917; raw +1088.9% (95%: +690.1% to +1487.7%), +0.8167 in the gauge's unit; LOSS · 0.05 → 0.7583; raw +1416.7% (95%: +986.8% to +1846.5%), +0.7083 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 1.3; raw +333.3% (95%: +174.4% to +492.3%), +1.0000 in the gauge's unit; LOSS · 0.4 → 2.2; raw +450.0% (95%: +38.7% to +861.3%), +1.8000 in the gauge's unit; LOSS · 0.2 → 1.3; raw +550.0% (95%: +436.9% to +663.1%), +1.1000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_BOTH.md`): queue: job turnaround, submitted to done, mean (s), A B C 65.63 → 86.72; raw +32.1% (95%: +13.4% to +50.8%); LOSS · 85.9 → 102.8; raw +19.7% (95%: +5.5% to +33.9%); LOSS · 75.65 → 95.34; raw +26.0% (95%: +8.1% to +43.9%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): batch: queue finished (s), A B C 758.7 → 767.6; raw +1.2% (95%: +0.6% to +1.8%); LOSS · 780.2 → 791.2; raw +1.4% (95%: +0.4% to +2.5%); LOSS · 770.9 → 781.9; raw +1.4% (95%: +0.3% to +2.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, mean (s), A B C 0.0625 → 0.7208; raw +1053.3% (95%: +883.9% to +1222.8%), +0.6583 in the gauge's unit; LOSS · 0.075 → 0.725; raw +866.7% (95%: +664.7% to +1068.6%), +0.6500 in the gauge's unit; LOSS · 0.05 → 0.7958; raw +1491.7% (95%: +1085.0% to +1898.3%), +0.7458 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job wait, submitted to its first pod running, 95th percentile (s), A B C 0.3 → 1.4; raw +366.7% (95%: +231.3% to +502.0%), +1.1000 in the gauge's unit; LOSS · 0.4 → 1.5; raw +275.0% (95%: +78.2% to +471.8%), +1.1000 in the gauge's unit; LOSS · 0.2 → 1.2; raw +500.0% (95%: +331.4% to +668.6%), +1.0000 in the gauge's unit; LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_ORCH.md`): queue: job turnaround, submitted to done, mean (s), A B C 65.63 → 81.51; raw +24.2% (95%: +10.9% to +37.5%); LOSS · 85.9 → 101; raw +17.6% (95%: +5.6% to +29.5%); LOSS · 75.65 → 93.17; raw +23.2% (95%: +6.9% to +39.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), mean, A B C 222.2 → 266.7; raw +20.0% (95%: +0.7% to +39.3%); LOSS · 260.4 → 290.2; raw +11.4% (95%: −6.3% to +29.2%); LOSS · 253.5 → 286.6; raw +13.1% (95%: −1.5% to +27.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), 95th percentile, A B C 517.4 → 996.5; raw +92.6% (95%: +46.7% to +138.5%); LOSS · 884.6 → 1167; raw +31.9% (95%: +10.8% to +53.0%); LOSS · 758.9 → 1145; raw +50.9% (95%: +23.2% to +78.6%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): response time (ms), 99th percentile, A B C 846.3 → 1467; raw +73.3% (95%: +31.5% to +115.1%); LOSS · 1478 → 1620; raw +9.6% (95%: −8.3% to +27.4%); LOSS · 1326 → 1638; raw +23.6% (95%: +1.1% to +46.0%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): time over the response line (% of samples), A B C 7.226 → 16.19; raw +124.1% (95%: +51.4% to +196.7%); LOSS · 8.862 → 13.31; raw +50.2% (95%: +5.7% to +94.8%); LOSS · 9.369 → 14.5; raw +54.8% (95%: +19.1% to +90.4%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.
- **the orchestrator’s own cost.** Volcano under the batch stream, the four ways (omni-v12, `results/live/V12_VOLCANO_4W_VS.md`): alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line), A B C 7.6 → 9.9; raw +30.3% (95%: +6.8% to +53.8%); LOSS · 7.1 → 7.9; raw +11.3% (95%: −3.6% to +26.1%); LOSS · 6.9 → 8.5; raw +23.2% (95%: −1.8% to +48.2%); LOSS. The knob: nothing of Omni-Compass to turn: the orchestrator's own cost.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
