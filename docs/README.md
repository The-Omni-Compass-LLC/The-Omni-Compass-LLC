# The documents

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Start here: the documents by reader

A navigation layer, top down, the way an IP asset is read at a board meeting. It is not a substitute for the evidence and not an
outside endorsement: every performance claim is read with its engine version, its workload, its native baseline, its evidence
class (P a physical meter, L live software, S our own models) and its original receipt.

| Reader | Read first | Then the evidence and the decision |
|---|---|---|
| CEO, board, strategic acquirer | [Due diligence](DUE_DILIGENCE.md) | [State of play](STATE_OF_PLAY.md), [claims register](CLAIMS_REGISTER.md), [every LOSS kept](LOSS_LEDGER.md), [limitations](LIMITATIONS.md) |
| CFO, investment committee | [Benefit sheet](BENEFIT_SHEET.md) | [The Omni index](../results/OMNI_INDEX.md), [evidence ledger](EVIDENCE_LEDGER.md), [the cloud bill's setup](AZURE_SETUP.md) |
| CTO, chief architect | [Mechanism of action](MECHANISM_OF_ACTION.md) | [Canonical engine](CANONICAL_ENGINE.md), [the engine that stands, omni-v23](OMNI_V23.md), [formal status](FORMAL_STATUS.md), [wiring verdicts](WIRING_VERDICTS.md) |
| Engineering, SRE, operations | [The Operator's Manual](OMNI_COMPASS_MANUAL.md) | [Integration manual](INTEGRATION_MANUAL.md), [pilot protocol](PILOT_PROTOCOL.md), [the benchmark harness](HARNESS.md) |
| Security, legal, IP | [Repository standards](REPOSITORY_STANDARDS.md) | [Security policy](../SECURITY.md), [threat model](THREAT_MODEL.md), [safety case](SAFETY_CASE.md), [license](../LICENSE), [disclosures](../DISCLOSURES.md) |
| Independent benchmark referee | [How to read the results](HOW_TO_READ_THE_RESULTS.md) | [The referee's audit pack](audit/README.md), [the verdict audit](../results/verdict_audit/VERDICT_AUDIT.md), [every reading recomputed](audit/STATISTICAL_VALIDATION.md), [preregistrations](K8S_COMPASS_PREREGISTRATION.md) |
| Live benchmark engine evaluator | [The live benchmark engine](engine/OMNI_COMPASS_LIVE_ENGINE.html) | [The Live Benchmark Engine Manual](OMNI_COMPASS_LIVE_ENGINE_MANUAL.md), [its appraisal](engine/APPRAISAL.md), [native's register](engine/NATIVE_REGISTER.md) |

### The hierarchy of evidence and claims

1. **Canonical source and version.** The engine's fingerprint and the commit before any result is compared
   (`python3 tools/omni_version.py`).
2. **Mathematics and contracts.** What is proved, under which assumptions, what is modelled and what is not yet proved
   ([formal status](FORMAL_STATUS.md)).
3. **The mechanism at run time.** Observe, decide, admit, actuate, verify, restore; a model is never presented as a live actuator.
4. **Measurements.** Physical meters (P), live software (L) and our own models (S), kept apart.
5. **Benchmark readings.** Native and Omni-Compass with their raw values, the raw change with its true sign, the gauge's aim, the
   uncertainty, the resource it took and every adverse row; STEADY of three kinds, exactly the same to nine decimals, under the
   0.5% floor, or (an older key) no difference beyond the noise, never mixed.
6. **Financial implications.** Only costs measured or priced inside a stated boundary; an unpriced bill stays unresolved.
7. **Board and IP claims.** Each linked to its source, its caveats, its ownership terms and its review status: run and scored by
   The Omni-Compass LLC's own code; no outside party has reviewed or approved these results.

A generated page or dashboard is changed through its generator, never by hand; historical receipts are never rewritten.

Read in this order. Every page here is current; dated records are in [`history/`](history/README.md).

## 1. Results

| Page | What it holds |
|---|---|
| [`STATE_OF_PLAY.md`](STATE_OF_PLAY.md) | Where everything stands: every result, every platform, real and modelled kept apart |
| [`RERUN_2026-10-10.md`](RERUN_2026-10-10.md) | Every benchmark dispatched again on 10 October 2026 on one commit: the record, run by run, with what each lands as |
| [`BENEFIT_SHEET.md`](BENEFIT_SHEET.md) | The benefit sheet: one number per benchmark, plus always toward the system's own aims, minus away from them, whatever the gauge measures |
| [`../results/OMNI_INDEX.md`](../results/OMNI_INDEX.md) | The Omni index: every test as more for the same, or the same for less, in one number |
| [`WIRING_VERDICTS.md`](WIRING_VERDICTS.md) | Wire in, or watch: every knob's verdict (write, watch, operator's choice) from every table, with every loss and its cause |
| [`COVERAGE_MAP.md`](COVERAGE_MAP.md) | Every domain with a controller against the register: done, queued, model only, or excluded by rule; the abbreviations with their places |
| [`HOW_TO_READ_THE_RESULTS.md`](HOW_TO_READ_THE_RESULTS.md) | Every column of every table, in plain words |
| [`DOSSIER.md`](DOSSIER.md) | Every result with its charts |
| [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md), [`CLAIMS_REGISTER.md`](CLAIMS_REGISTER.md) | Every claim with its evidence class, the losses kept |

## 2. Method (each written before its run)

| Page | What it holds |
|---|---|
| [`K8S_COMPASS_PREREGISTRATION.md`](K8S_COMPASS_PREREGISTRATION.md) | Kubernetes and Azure: every test, every amendment, every result |
| [`GPU_PREREGISTRATION.md`](GPU_PREREGISTRATION.md) | The card and the eight cards |
| [`REALMS_PREREGISTRATION.md`](REALMS_PREREGISTRATION.md) | The muscles and the organisms: the question, the rules and the seeds, frozen before the runs, with every amendment (the spine, the seventh organism, 16 October) |
| [`OMNI_V4_PLAN.md`](OMNI_V4_PLAN.md) | The next engine, ordered 10 October: the collective mechanism (one body, one brain, the reflex rule, the body's cost, nothing pushed to a LOSS anywhere), the final coverage sweep with the closed systems of the mega-caps mapped to open analogs, the catalog's new families, and the order and cost of the rerun |
| [`CITYLEARN_PREREGISTRATION.md`](CITYLEARN_PREREGISTRATION.md) | Omni-Compass on top of CityLearn, an independent building and battery simulator |
| [`CPU_POWER_PREREGISTRATION.md`](CPU_POWER_PREREGISTRATION.md) | The machine itself: Omni-Compass on top of the Linux kernel's own frequency governor, energy from the processor's meter; built, waiting for a machine on the metal |
| [`REFEREE_CHECKLIST.md`](REFEREE_CHECKLIST.md) | A referee's checklist, item by item |

## 3. The mechanism

| Page | What it holds |
|---|---|
| [`MECHANISM_OF_ACTION.md`](MECHANISM_OF_ACTION.md) | How Omni-Compass acts, wire by wire |
| [`engine/OMNI_COMPASS_LIVE_ENGINE.html`](engine/OMNI_COMPASS_LIVE_ENGINE.html) | The engine running, drawn live (open in a browser): native alone beside Omni-Compass on top of native, sixty muscles of the catalog. It opens on the operations center: the official runs streaming half minute by half minute from their SHA-256-checked raw files (the data pipeline from the GitHub run to the page, live tiles with sparklines, a response-time candlestick chart, a latency heatmap, a throughput tick chart, every repetition as paired bars, the governor's decision ticker, and every benchmark's place block by block), every word the run's own reading. Then the tensor lab and the AI analyst: the engine's record as a live three-dimensional tensor (two arms × every decision × sixty muscles), the difference matrix between the arms, the body's principal motions (the covariance of the sixty positions decomposed in the page), the flow of every request as a Sankey, a radar of every gauge against native, a live narrator, and Claude answering questions about the screen through six tools that read the page's data and turn the dashboard (on the viewer's own Claude account, in claude.ai). The heart: the governor's decision loop, beat by beat from each official run's audit, with its lease and the watchdog that hands every setting back if it stops. The benefit board (every benchmark's row of `results/BENEFIT_SHEET.json` and the Omni index) and the scale-out grid (seven organisms × 1, 10, 100 copies × 1, 10, 100 runs, modelled and with the cluster inside, from the newest grid's `GRID.json`), all rebuilt by [`engine/build_live_engine.py`](engine/build_live_engine.py). Every chart draws only while it is on screen. By default the body is the realms harness itself (its plants and the max), recorded on runs A, B and C by [`engine/export_harness_trace.py`](engine/export_harness_trace.py) (each muscle alone and as one organism) and read by the three-run rule; the shipped live controller on the model cluster, brain to plug, recorded by [`engine/export_controller_trace.py`](engine/export_controller_trace.py); every stack native and then with Omni-Compass on top (a GPU card, `realms/gpu_card.py`; Linux on one host, the shipped CFS-quota conveyance in `tools/model_gate.py`'s model) every muscle of the catalog and the seven organisms on omni-v8 (the realms table, each native and then on top), and every judged row of the 22 receipts of the real runs (the omni-v7 tables until omni-v9's land), LOSS rows kept, recorded by [`engine/export_scenarios.py`](engine/export_scenarios.py); the brain, nerves, compass law and v7 verdict are ported and checked against the Python by [`engine/check_live_engine.py`](engine/check_live_engine.py). A labelled stress-test model (native and Omni-Compass on top, side by side) can be switched on to stress the body by hand (class S throughout; a picture of the mechanism, not a benchmark result) |
| [`engine/NATIVE_REGISTER.md`](engine/NATIVE_REGISTER.md) | Native's real settings, knob by knob, each with its source (a receipt, the system's own default, or the machine's reading when it runs), beside the realms harness's native: what is measured, what matches, what does not (the HPA target) and what is not yet measured |
| [`engine/build_live_engine.py`](engine/build_live_engine.py) | The live benchmark engine rebuilt by GitHub from the engine that stands (`.github/workflows/live-engine.yml`: on every change to the engine, a model or a result, after every front-page refresh, every three hours): every record made again by the repository's own code, checked against the Python, the C++ core and the repository's own runs; the official runs played back from their raw files ([`engine/export_runs.py`](engine/export_runs.py)), every file's SHA-256 matched against the run's own list and every repetition scored by the repository's own scorer; every benchmark's place (landed, running, queued, not yet run); the commit, the time and the runs GitHub is running |
| [`engine/APPRAISAL.md`](engine/APPRAISAL.md) | The live benchmark engine appraised: every view reproduced from the repository's own code by an independent path and compared value by value (rerun: [`engine/check_records.py`](engine/check_records.py), [`engine/check_live_engine.py`](engine/check_live_engine.py)), the grades, what the mechanism reads, and the material findings for the owner |
| [`CONVEYANCE_LAW.md`](CONVEYANCE_LAW.md), [`TRACKING_THEOREM.md`](TRACKING_THEOREM.md), [`FORMAL_STATUS.md`](FORMAL_STATUS.md) | The law, what is proved, and how |
| [`CANONICAL_ENGINE.md`](CANONICAL_ENGINE.md), [`ENGINES.md`](ENGINES.md) | The one engine the software runs |
| [`TWO_WAY_NERVOUS_SYSTEM.md`](TWO_WAY_NERVOUS_SYSTEM.md), [`NERVOUS.md`](NERVOUS.md) | Senses in, settings out |
| [`THE_SPINE.md`](THE_SPINE.md), [`REALMS.md`](REALMS.md), [`REALM_MUSCLES.md`](REALM_MUSCLES.md), [`MUSCLE_CATALOG.md`](MUSCLE_CATALOG.md), [`DOMAIN_MAP.md`](DOMAIN_MAP.md) | The muscles: what each is, where it sits, how it is wired; every family's wiring recipe on your own stack (native controller, wire out, wire in, restore, live or modelled; `docs/wiring_recipes.csv`) |
| [`METRICS_CATALOG.md`](METRICS_CATALOG.md) | Every gauge, measured or modelled |

## 4. Running it

| Page | What it holds |
|---|---|
| [`OMNI_COMPASS_MANUAL.pdf`](OMNI_COMPASS_MANUAL.pdf), [`OMNI_COMPASS_MANUAL.md`](OMNI_COMPASS_MANUAL.md) | The manual |
| [`INTEGRATION_MANUAL.md`](INTEGRATION_MANUAL.md), [`WIRING_GUIDE.md`](WIRING_GUIDE.md), [`OPERATOR_MANUAL.md`](OPERATOR_MANUAL.md) | Wiring it onto your stack and operating it |
| [`PILOT_KIT.md`](PILOT_KIT.md), [`PILOT_PROTOCOL.md`](PILOT_PROTOCOL.md) | A read-only shadow pilot on your own cluster |
| [`HARNESS.md`](HARNESS.md), [`HANDOFF.md`](HANDOFF.md) | Every benchmark and every command |
| [`GPU_BENCH.md`](GPU_BENCH.md), [`GPU_RUN_GUIDE.md`](GPU_RUN_GUIDE.md), [`AZURE_SETUP.md`](AZURE_SETUP.md) | The card runs and the Azure runs |

## 5. Due diligence

| Page | What it holds |
|---|---|
| [`DUE_DILIGENCE.md`](DUE_DILIGENCE.md) | The diligence pack |
| [`COMPARISON.md`](COMPARISON.md) | What runs data centres today, and where Omni-Compass sits |
| [`REPOSITORY_STANDARDS.md`](REPOSITORY_STANDARDS.md) | Licensing, scanning and the standards this repository meets |
| [`HISTORY.md`](HISTORY.md) | Earlier states, failures and chronology, kept whole |

Folders: [`specs/`](specs) (contracts and specifications), [`realm_study/`](realm_study) (the primary sources of the
656), [`book/`](book) (the printable book's sources), [`source/`](source) (the source code as PDF),
[`figures/`](figures), [`dossier/`](dossier), [`plate/`](plate), [`handoff/`](handoff) (the engine's mathematics).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
