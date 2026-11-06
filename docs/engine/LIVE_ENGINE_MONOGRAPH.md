# The Omni-Compass Live Benchmark Engine: Purpose, Mechanism, Evidence and Limits

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Abstract

This monograph describes the Omni-Compass live benchmark engine: one web page that plays back the three-run tables of Omni-Compass against its native controllers and runs three parts of the engine in the browser (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`). Omni-Compass is a supervisory control layer: it sits on top of the native controllers, reads their meters and writes only settings they already accept; no request or byte passes through it. The engine that stands is omni-v25 (`OMNI_V25.json`). Chapter 1 fixes the page's purpose and boundary; chapter 2 the stack under test and the 1,107-muscle catalogue (`realms/catalog_v5.csv`); chapter 3 the mechanism, read from the code; chapter 4 the evidence classes, the four arms, the paired three-run design and the key that turns a change into GAIN, STEADY, LOSS or power given; chapter 5 the receipts; chapter 6 the native products Omni-Compass sits on, the reproduction of every number and the limits. The headline, the Omni index, reads GAIN, up 20.4%: more work and shorter waits on real software on GitHub's machines (class L), not bare metal, not a cloud and not a bill (`results/OMNI_INDEX.md`). The record also holds 273 LOSS rows against native, most with no cause yet written (`docs/LOSS_LEDGER.md`). On the chip the work for the bill reads the runs disagree, and in the cloud it is not yet read (`results/TWO_BILLS.md`). Four theorems bound the engine's own channels over a declared parameter box; none is a global-stability proof (`docs/FORMAL_STATUS.md`). The company's own code ran and scored all of it; no outside party has reviewed it.

## Contents

- [1. Purpose and Scope of the Live Benchmark Engine](#1-purpose-and-scope-of-the-live-benchmark-engine)
  - [1.1 The object: Omni-Compass on top of native](#11-the-object-omni-compass-on-top-of-native)
  - [1.2 The question the engine exists to answer](#12-the-question-the-engine-exists-to-answer)
  - [1.3 What the engine is: one page and its copies](#13-what-the-engine-is-one-page-and-its-copies)
  - [1.4 How the page is fed and rebuilt](#14-how-the-page-is-fed-and-rebuilt)
  - [1.5 The self-update and its stamp](#15-the-self-update-and-its-stamp)
  - [1.6 What runs live, what plays back, and the three evidence classes](#16-what-runs-live-what-plays-back-and-the-three-evidence-classes)
  - [1.7 Who can run what](#17-who-can-run-what)
  - [1.8 What the engine can answer today, place by place](#18-what-the-engine-can-answer-today-place-by-place)
  - [1.9 What the engine is not](#19-what-the-engine-is-not)
  - [1.10 Threats to validity](#110-threats-to-validity)
- [2. The System Under Test: the Stack, its Native Controllers and the Muscle Catalogue](#2-the-system-under-test-the-stack-its-native-controllers-and-the-muscle-catalogue)
  - [2.1 What this chapter fixes](#21-what-this-chapter-fixes)
  - [2.2 Where Omni-Compass sits: the cascade](#22-where-omni-compass-sits-the-cascade)
  - [2.3 The layers, from the chip to the cloud](#23-the-layers-from-the-chip-to-the-cloud)
  - [2.4 The clocks side by side](#24-the-clocks-side-by-side)
  - [2.5 The muscle catalogue](#25-the-muscle-catalogue)
  - [2.6 The seven organisms and the eighth](#26-the-seven-organisms-and-the-eighth)
  - [2.7 From a muscle to a real knob](#27-from-a-muscle-to-a-real-knob)
  - [2.8 Where the receipts are](#28-where-the-receipts-are)
  - [2.9 Threats to validity](#29-threats-to-validity)
- [3. The Mechanism: the Compass Law, the Supervisory Loop, the Immune System and the Kill Switch](#3-the-mechanism-the-compass-law-the-supervisory-loop-the-immune-system-and-the-kill-switch)
  - [3.1 Where the mechanism sits](#31-where-the-mechanism-sits)
  - [3.2 The state, the observation and the control law](#32-the-state-the-observation-and-the-control-law)
  - [3.3 The four pieces and the allocation law](#33-the-four-pieces-and-the-allocation-law)
  - [3.4 One law across every muscle: the compass law](#34-one-law-across-every-muscle-the-compass-law)
  - [3.5 Every muscle to its own limit, never past it](#35-every-muscle-to-its-own-limit-never-past-it)
  - [3.6 The verdict: do no harm as a trigger](#36-the-verdict-do-no-harm-as-a-trigger)
  - [3.7 The beat and the loop: read, decide, write](#37-the-beat-and-the-loop-read-decide-write)
  - [3.8 The immune system and the redline reflex](#38-the-immune-system-and-the-redline-reflex)
  - [3.9 The lease and the heartbeat](#39-the-lease-and-the-heartbeat)
  - [3.10 The factory profile and the two restoring controls](#310-the-factory-profile-and-the-two-restoring-controls)
  - [3.11 The kill switch](#311-the-kill-switch)
  - [3.12 The audit of every write](#312-the-audit-of-every-write)
  - [3.13 The C++ twin and the seal](#313-the-c-twin-and-the-seal)
  - [3.14 The formal status, stated exactly](#314-the-formal-status-stated-exactly)
  - [3.15 Threats to validity](#315-threats-to-validity)
- [4. The Evidence: Classes, Arms, the Three-Run Key and How Every Reading Is Judged](#4-the-evidence-classes-arms-the-three-run-key-and-how-every-reading-is-judged)
  - [4.1 Evidence classes, and why class S is never proof](#41-evidence-classes-and-why-class-s-is-never-proof)
  - [4.2 The four arms, the two bills and the one equation](#42-the-four-arms-the-two-bills-and-the-one-equation)
  - [4.3 Paired repetitions and the three runs](#43-paired-repetitions-and-the-three-runs)
  - [4.4 The one key](#44-the-one-key)
  - [4.5 A worked example: four readings where the sign and the word differ](#45-a-worked-example-four-readings-where-the-sign-and-the-word-differ)
  - [4.6 The verdict audit and its four comparisons](#46-the-verdict-audit-and-its-four-comparisons)
  - [4.7 The Omni index and how it is composed](#47-the-omni-index-and-how-it-is-composed)
  - [4.8 Threats to validity](#48-threats-to-validity)
- [5. What the Receipts Show on omni-v25: What Omni-Compass Does, What It Gives, What It Does Not Do](#5-what-the-receipts-show-on-omni-v25-what-omni-compass-does-what-it-gives-what-it-does-not-do)
  - [5.1 The engines, the places and the key](#51-the-engines-the-places-and-the-key)
  - [5.2 The headline: the Omni index](#52-the-headline-the-omni-index)
  - [5.3 By product: the six categories](#53-by-product-the-six-categories)
  - [5.4 Real Kubernetes: nine tests, one reads LOSS on the index](#54-real-kubernetes-nine-tests-one-reads-loss-on-the-index)
  - [5.5 The LOSS rows inside the index's own tables](#55-the-loss-rows-inside-the-indexs-own-tables)
  - [5.6 The cluster's 34 LOSS rows by gauge, and the stores' 14](#56-the-clusters-34-loss-rows-by-gauge-and-the-stores-14)
  - [5.7 The oversight line: the minutes a person would be paged](#57-the-oversight-line-the-minutes-a-person-would-be-paged)
  - [5.8 The chip: arm A against arm B (class P)](#58-the-chip-arm-a-against-arm-b-class-p)
  - [5.9 The cloud: arm C against arm D (class L, omni-v18)](#59-the-cloud-arm-c-against-arm-d-class-l-omni-v18)
  - [5.10 The whole-system composition: a second reading (class S)](#510-the-whole-system-composition-a-second-reading-class-s)
  - [5.11 The LOSS ledger: 273 rows against native, and their causes as written](#511-the-loss-ledger-273-rows-against-native-and-their-causes-as-written)
  - [5.12 Can, gives, cannot yet show, does not do](#512-can-gives-cannot-yet-show-does-not-do)
  - [5.13 Threats to validity](#513-threats-to-validity)
- [6. The Native Tools and Products: What They Do, What They Leave, Where Omni-Compass Sits; Reproducing the Engine; Limits](#6-the-native-tools-and-products-what-they-do-what-they-leave-where-omni-compass-sits-reproducing-the-engine-limits)
  - [6.1 The three layers: inner loops, the outer loop, the control plane](#61-the-three-layers-inner-loops-the-outer-loop-the-control-plane)
  - [6.2 The chip layer](#62-the-chip-layer)
  - [6.3 The cloud layer](#63-the-cloud-layer)
  - [6.4 The software layer, I: autoscalers and each service's own controllers](#64-the-software-layer-i-autoscalers-and-each-services-own-controllers)
  - [6.5 The software layer, II: open-source schedulers and orchestrators, run live](#65-the-software-layer-ii-open-source-schedulers-and-orchestrators-run-live)
  - [6.6 Commercial products in the same layers, from their own material](#66-commercial-products-in-the-same-layers-from-their-own-material)
  - [6.7 The live benchmark engine beside the operator's surfaces that exist](#67-the-live-benchmark-engine-beside-the-operators-surfaces-that-exist)
  - [6.8 Reproducing the engine: from a workflow to a number](#68-reproducing-the-engine-from-a-workflow-to-a-number)
  - [6.9 Re-running each benchmark](#69-re-running-each-benchmark)
  - [6.10 The Python 500 and its C++ twin](#610-the-python-500-and-its-c-twin)
  - [6.11 verify.py, the verification receipt and the release manifest](#611-verifypy-the-verification-receipt-and-the-release-manifest)
  - [6.12 Checking the page and re-deriving a reading](#612-checking-the-page-and-re-deriving-a-reading)
  - [6.13 What the record establishes](#613-what-the-record-establishes)
  - [6.14 Threats to validity across the programme](#614-threats-to-validity-across-the-programme)
- [References](#references)

## 1. Purpose and Scope of the Live Benchmark Engine

This chapter fixes the object of study and draws its boundary: what the live benchmark engine is, the question it exists to answer, how it is fed and kept current, who can run which part of it, what it can answer today and what it does not claim. The stack is described in chapter 2, the mechanism in chapter 3, the evidence rules in chapter 4, the receipts in chapter 5, and the products, the reproduction and the limits of the programme in chapter 6.

Every statement about a file describes the repository as read on 6 November 2026. Where they differ, the monograph reads `main` as GitHub serves it (commit `81002a41f6c`), because that is the copy every published page updates itself from (section 1.5); the working branch, which carried later edits to the page and its builder, is named where it matters (section 1.10).

### 1.1 The object: Omni-Compass on top of native

Omni-Compass is a supervisory control layer. It sits on top of the native controllers a stack already runs (an autoscaler, a scheduler, a card's power limit, a database's pool), reads their gauges (one wire in) and writes only the settings those controllers already accept (one wire out). It acts in the control plane only: no request, packet, file or byte of the work passes through it (`DISCLOSURES.md`, section 10, "Never in the data path"). It removes no controller: on Kubernetes the scheduler, the kubelet and the autoscalers stay in every arm (`docs/INDUSTRY_LANDSCAPE.md`). The products it sits on, among them Kubernetes' own autoscalers, KEDA, Kueue, Volcano, the KAI scheduler and Karmada (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 2.25), are described in this monograph only from their own public material and only as what Omni-Compass sits on. In this monograph "governor" names only such a product; what Omni-Compass does is called supervisory.

On the page every comparison has two sides and only two. *Native* is the system by itself, every controller it ships with still running. *Omni-Compass on top of native* is the same system with those controllers still running and the supervisory layer above them. The page never shows Omni-Compass by itself (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, "What You Are Looking At").

The engine that stands is omni-v25, digest `cf56fc0a7b707452`, 65 files (`OMNI_V25.json`; `docs/OMNI_V25.md`); `python3 tools/omni_version.py` prints the same on the checkout. Every result names the engine its runs ran on, and no result is read across engines (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, Preface, standard 5).

### 1.2 The question the engine exists to answer

The manual states the question in an operator's words: "is it doing what the receipts say, right now, on this body, and would I see it if it were not?" (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, Introduction). A referee needs it in a form that can be checked.

Each run of a three-run table (runs A, B and C, indexed i = 1, 2, 3) holds paired repetitions of native and of Omni-Compass on top of native on the same seed, load and clock. For a gauge g, let nᵢ(g) be native's mean in run i and dᵢ(g) the mean paired difference, Omni-Compass minus native. The raw change of run i, and the mean the reading is judged on, are

  δᵢ(g) = dᵢ(g) / |nᵢ(g)|,  δ̄(g) = (δ₁(g) + δ₂(g) + δ₃(g)) / 3.  (1.1)

The reading R(g) is a word, never a sign. It is computed once, in the repository, by `three_run_reading` in `tools/readings.py`, from the three δᵢ, their 95% intervals and the gauge's declared aim (work done; time waited, missed or failed; a resource spent or held; a count that must never rise; or shown, not judged). Its rules are set out in section 4.4. In brief: a mean change under the 0.5% floor reads STEADY; runs that moved 0.5% or more in opposite directions read *the runs disagree*, an unresolved reading; otherwise the word is GAIN or LOSS by what the gauge is for, or *power given* where a resource spent or held rose (a resource that fell is a cut, a GAIN), worded "in all three of our runs" when every run moved the same way with its 95% interval clear of zero and "by the mean of our three runs" otherwise.

On that footing the engine answers four questions.

| | Question | Where it is read |
|---|---|---|
| Q1 | **Hold.** In each place, does any judged gauge of Omni-Compass on top of native read LOSS against native? | the LOSS register and status board; `docs/LOSS_LEDGER.md` |
| Q2 | **Benefit.** Which gauges read GAIN, and what resource was given to buy them? | the scorecard and benefit board; `results/OMNI_INDEX.md` |
| Q3 | **Bill.** In each place, does the work done for each dollar rise? (the equation of section 4.2) | the benefit against native; `results/TWO_BILLS.md` |
| Q4 | **Fidelity.** Does every number and word on the page equal what the repository's own code computes from its own raw files? | the appraisal; `docs/engine/APPRAISAL.md` |

Q1 to Q3 are questions about Omni-Compass. Q4 is a question about the engine itself, and it comes first: a page that cannot show its own fidelity answers nothing else.

"Does and does not" is meant literally. The page raises every reading that went against native on its status board before anything that went for it (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, Foreword and Preface, standard 4). The record holds 273 rows that read LOSS for Omni-Compass on top of native against that native alone, the rows by which do no harm is judged (`docs/LOSS_LEDGER.md`); section 5.11 sets out where they sit and what is written of their causes.

### 1.3 What the engine is: one page and its copies

The live benchmark engine is one web page, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, built by the repository's own code, `docs/engine/build_live_engine.py`, from the engine that stands and the repository's own results. Its builder's header states the design rule: "the page is a monitor of the engine, never a drawing of it". The workflow that rebuilds it records the order behind that rule, given on 17 October 2026: "wire it up to the engine itself and let the math move through" (`.github/workflows/live-engine.yml`, header comment).

The page carries its records inside itself as twenty-five JSON blocks (counted in the page). The builder's header names the seven it makes directly: the realms harness, the shipped Kubernetes controller on a modelled cluster, the official runs read back from their raw files, the chip and host models with the newest receipts, the Python's runs fed through the C++, the heartbeat dial, and the build record (`docs/engine/build_live_engine.py`, header). The rest are named where the page uses them (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 35.3). The page reaches readers in three forms.

| Form | Where | Made by | What it is |
|---|---|---|---|
| The source page | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` | `docs/engine/build_live_engine.py` | the page with its records, 60,411,316 bytes as committed on `main` (`docs/engine/LIVE_ENGINE_VERSION.json`); GitHub shows it as text, so it is downloaded and opened in a browser (`README.md`) |
| The one-file copy | `docs/live/index.html`; where GitHub Pages serves `docs/`, the address in `README.md` | `docs/engine/build_standalone.py` | the same page, its records packed inside it (gzip, then base64) and unpacked in the browser, for a phone, a laptop's disk or a web host (`docs/engine/build_standalone.py`, header) |
| The published split copy | the claude.ai artifact address given in `README.md` | published from a build | the saved page with five files published beside it (`docs/SITE_AUDIT.md`, section F) |

The one-file copy is rebuilt from the page at every build (`.github/workflows/live-engine.yml`, the rebuild step). On `main` its packed build record names the same engine, commit and build time as the source page's (omni-v25; commit `af612472`; 2026-11-06 03:33 UTC; compare `docs/engine/LIVE_ENGINE_VERSION.json`), and it carries the same twenty-five records. No workflow the files describe rebuilds the published split copy; section 1.10 returns to it.

### 1.4 How the page is fed and rebuilt

The rebuild is one GitHub Actions workflow, `.github/workflows/live-engine.yml`, on GitHub's own machine with a 60-minute limit. Its concurrency group never cancels a build in progress.

| It starts | When |
|---|---|
| On a push to main | when the engine, a model, a harness, a result, a queue or the page's tools change; the page's own file is excluded from the paths (the workflow's comment gives the reason: on 20 October the page had rebuilt itself every 7 minutes) |
| After every result | when the `front-page` workflow (`.github/workflows/front-page.yml`) completes successfully on main or a GPU branch; it runs within minutes of every finished benchmark run and every hour besides (`README.md`, "Latest, newest first") |
| On a clock | at minute 41 of every third hour (the workflow's schedule) |
| By hand | a manual dispatch |

Each build on `main` runs in this order (`.github/workflows/live-engine.yml`):

1. **The raw files are opened.** The raw folders of the official runs the page plays back are checked out from the branch `raw`.
2. **The records are made again.** `docs/engine/build_live_engine.py` rebuilds every record with the repository's own code on the checkout, reading GitHub's list of runs in progress and queued where a token is present. (A step before it re-records the guided tour's voice for any stop whose words changed; that step may fail without stopping the build.)
3. **The numbers a site may print follow.** The same step rewrites the two bills, the oversight line, the work per bill, the work-today sheet, the FAQ, the README's headline and `results/SITE_NUMBERS.json`, then rebuilds the one-file copy. The page and the numbers a website may show come from one build and the same records.
4. **The stamp is written last**, from the page as it will be committed (section 1.5).
5. **The page is checked.** `docs/engine/check_live_engine.py` holds the page's ported mathematics against the Python and a compiled C++ core; `docs/engine/check_records.py` (seeds 3000, 3001 and 3002) reproduces every record by an independent path; `docs/engine/build_live_engine.py --check` rebuilds in memory and fails on any difference. The job's shell runs with `-e` and `pipefail`, so a failed check fails its step and the page is not committed.
6. **The legal check, the commit and the push.** The push is tried up to six times if the branch moved meanwhile.

Two properties follow. The page cannot run ahead of the repository's engine: `--check` fails a page whose engine differs from the one `tools/omni_version.py` reads (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 35.2). It can run behind the repository's records: a page is true for the build it names, and a reading that lands after that build appears only on a later one (section 45.4 of the same manual). The build the stamp names is of 2026-11-06 03:33 UTC (`docs/engine/LIVE_ENGINE_VERSION.json`); the Python 500-run record written at 10:44:56 UTC that day (`results/engine_runs/ENGINE_RUNS_500_3549104563.md`) is not on it. No file bounds how far behind the page may fall (section 1.10).

### 1.5 The self-update and its stamp

Every copy of the page carries a short script, `omniSelfUpdate`, placed in its head before anything else runs, and a pointer to the repository's main branch as GitHub serves it (`docs/engine/build_live_engine.py`, `SELF_UPDATE` and `self_update`).

The stamp is a file of a few hundred bytes, `docs/engine/LIVE_ENGINE_VERSION.json`. As committed on `main` it reads:

| Field | Value |
|---|---|
| engine | omni-v25 |
| digest | cf56fc0a7b707452 |
| commit | af612472ef9012c92cb41992486426e324d9c3a6 |
| built_at | 2026-11-06 03:33 UTC |
| bytes | 60,411,316 |
| sha256 | d35d4aa290515fe217fb975bbada45b8591097a44124b7c4f5a7cd7c598139a6 |

A copy reads the stamp when it opens and every 24 hours after; after a failed read it asks again in an hour, doubling with each failure in a row up to a day (`docs/engine/build_live_engine.py`, `later` and `failed`). It fetches the page only when the stamp names a later build time than its own, and opens it only when four tests pass: exactly the stamp's byte count; the stamp's SHA-256; the stamp's build time in the page's own build record; and every script compiling in the reader's browser. If the new engine does not start, the tab returns to the copy it came from and does not open that build again (`settle`). The script's header comment states that it only reads and sends nothing. Its behaviour is held by `tests/test_live_self_update.py`.

On `main`, the SHA-256 and byte count of `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` equal the stamp's; anyone can repeat the check with `sha256sum` and `wc -c`. What the stamp establishes is narrow: that a copy is the published page, byte for byte. It does not show that the build's content is right. That is Q4, answered by the checks of section 1.4 and the appraisal.

### 1.6 What runs live, what plays back, and the three evidence classes

Three parts of the engine run in the page itself: the brain (`omnicompass/core.py`, integrated by the fourth-order Runge–Kutta method), the compass law (`omnicompass/compass_law.py`) and the verdict (`omnicompass/verdict.py`), ported to the browser with the files they rest on (`omnicompass/adapter.py`, `omnicompass/nervous_system.py`, `omnicompass/student_t.py`) and held to the Python and the C++ at every build (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 35.4). The appraisal reports the size of the agreement. Against the Python on seeded inputs (8,000 decisions, 48,000 organ grants, 4,800 compass forces, 300 verdict intervals, 400 whole verdict trials and 500 degrees of freedom of the exact t), the largest difference is 2 × 10⁻¹⁵, and no grant, verdict or t value differs. Against the C++ twin of the core on 2,000 seeded states, the largest relative difference is 4.4 × 10⁻¹⁶ in the derivative and 2.2 × 10⁻¹⁶ in the Runge–Kutta step (`docs/engine/APPRAISAL.md`, "Method"). These ported parts drive a stress-test model of sixty muscles, each on top of its own native controller, and the page's own runs of the Python's seeded sets and of the core's Monte Carlo (section 6.10). All of that is class S.

Everything else on the page is a record played back. The official runs are read from their raw files, and every file's SHA-256 is matched against its run's own list before a byte is drawn. At the newest build that covered 94 three-run tables with 282 runs, and 229,338 of 229,338 raw files matched (`docs/engine/APPRAISAL.md`, counts).

Every monitor states its evidence class (`DISCLOSURES.md`, section 9). The monograph uses three classes as the repository defines them (`DISCLOSURES.md`, section 2, item 1; `docs/HOW_TO_READ_THE_RESULTS.md`); section 4.1 adds the two further classes the repository names and the reasons class S is never proof.

| Class | What it is | Examples on file | Where its tables live | What it may speak for |
|---|---|---|---|---|
| **L** | live software on real machines | Kubernetes in kind on GitHub's runners; the five data stores (PostgreSQL behind PgBouncer, MySQL, Redis, MongoDB, Kafka) on the same runners; Kubernetes through Azure's AKS | `results/live/` | the software end, measured on the machine and software named: work done, time waited, failures, machines and memory held, each as the software counts it |
| **P** | a physical chip's own meter | the A10 card on Lambda (omni-v23); the A100 (omni-v21; the eight-card machine on omni-v23) | `results/gpu/` | the card's energy and the work it served inside a rented window, measured by the card's meter |
| **S** | the repository's own models | the 1,107 muscles and the seven organisms; the injection grid; the shipped controller on the modelled cluster; the GPU card and Linux host models; the sixty-muscle stress-test model; the model gate; the Python 500 and its C++ twin | `results/model_gate/`, `results/realms_v5/`, `results/injection_grid/` | how a mechanism behaves under stated assumptions: modelled, never proof |

The models were written by the same people who wrote the law. They show how the mechanism behaves; they are not an independent test (`DISCLOSURES.md`, section 2, item 2).

### 1.7 Who can run what

What each kind of reader can run, and what that run can and cannot establish, is set out below from the files that describe each path.

| Path | How | Where it runs | Class | What it can establish | What it cannot |
|---|---|---|---|---|---|
| **Read the page** | open the published address in `README.md`; or download the source page; or open `docs/live/index.html` | the reader's browser | as each monitor states | every record of the build named in the stamp, native beside Omni-Compass on top of native | anything after the build's time; anything no record holds |
| **Check the page against the repository** | the commands of section 6.12 (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, chapter 47) | the reader's machine | a property of the code | that the page's records are the repository's own and its ported mathematics equals the Python and the C++ | that the repository's runs measured what they claim |
| **Run the Python 500 and its C++ twin** | the page's buttons, "Run the Python's 500 runs here" and the linked Monte Carlo; on a machine, `tools/engine_runs.py` and `tools/core_runs.py`, the C++ built from `cpp/`; on GitHub, `.github/workflows/engine-runs.yml` (daily, on a push and by hand) and `.github/workflows/monte-carlo.yml` (by hand, 1 to 10,000 runs, 500 by default, and on a push that changes the core, the harness or a system file) | browser, the reader's machine, a GitHub runner | S | that the Python, the C++ and the page compute one digest on the same draws (section 6.10) | anything about a real system |
| **Run a benchmark** | the benchmark workflows on GitHub's runners (section 6.9); `bash scripts/run_live_local.sh 3` on the reader's own kind cluster; `sudo bash scripts/gpu_rented_run.sh` on a rented NVIDIA machine (`README.md`, "Check it yourself"); `.github/workflows/reproduce.yml` rebuilds every three-run table of the engine that stands from its raw receipts each Monday and compares it byte for byte | GitHub runners; the reader's cluster or card | L, or P for a card's meter | a paired comparison on that machine and that load | a result for any other machine; a bill unless the place prices it |
| **Bring your own system** | a system file under `systems/` (`systems/README.md`; any of six starting states and 22 parameters of the core, each a range or a number) run through `.github/workflows/monte-carlo.yml` or the page's Custom System Run; or the page's own-system panel and Auxiliary Input, pointed at the reader's own Prometheus | a GitHub runner or the browser; the reader's Prometheus, read only | S for a system file; for Prometheus, readings of the reader's own system | the engine's mathematics on the reader's ranges; the reader's own gauges set beside a record | a paired benchmark; that Omni-Compass would do the same on that stack |

Four boundaries apply to the table.

First, the paid places are not a reader's to start. The cloud and card runs go through the repository's own workflows (the ledger in `docs/engine/build_live_engine.py` names `.github/workflows/aks-metered.yml`, `.github/workflows/gke-metered.yml`, `.github/workflows/eks-metered.yml` and `.github/workflows/lambda-gpu.yml`) behind keys held as repository secrets; the status of Google's and Amazon's sets is given in section 2.3.6. Every card rental is on the founder's word (`README.md`). A reader who rents a card and runs `scripts/gpu_rented_run.sh` makes a run of the reader's own.

Second, the Monte Carlo workflow bills nothing, and its pasted block is read as numbers only, never run as code (`.github/workflows/monte-carlo.yml`, header; `systems/README.md`).

Third, the own-system panel only reads. Once each of its two windows holds four readings, each gauge is read by the key; but that is one run of the reader's system, not a three-run table, and the windows ran at different times, so the load may differ between them (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 2.25). Wiring Omni-Compass onto a real stack is the Operator's Manual's work, not the page's.

Fourth, the manual treats serving the page to others as a hosted service that needs the Enterprise License (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, chapter 46).

### 1.8 What the engine can answer today, place by place

A system runs Omni-Compass in one of two places, each with two arms (section 4.2): on bare metal, arm A the chip native and arm B the chip with Omni-Compass on native; through a cloud, arm C the cloud native (Azure AKS) and arm D the cloud with Omni-Compass on native. The software end goes with it to either place (`DISCLOSURES.md`, section 10). Each row below is its record's own reading, given in full in the section named; engines differ by row, and no row is read as another engine's.

| Place | Class | Engine | Reading, and what it means for the system | Section; receipt |
|---|---|---|---|---|
| The software end: Kubernetes and the data stores on GitHub's runners | L | omni-v25 | **The Omni index: GAIN, up 20.4%.** More work done and shorter waits, the resources it took scored beside them (a rise there is power given). Not bare metal, not a cloud, not a bill. On work and speed alone, a named second reading: GAIN, up 94.0% | 5.2; `results/OMNI_INDEX.md`, `results/SITE_NUMBERS.json` |
| Bare metal: one A10 card, fully loaded, arm B against arm A | P | omni-v23 | The bill STEADY, under the floor (the three runs' mean 0.01%): the rented time held. The work for the bill: the runs disagree (up 1.5%, up 0.7%, down 0.7%), so more work inside the same bill is not yet shown. Energy for each request served: GAIN in all three of our runs, down 1.3%, less of the chip's energy per request | 5.8; `results/TWO_BILLS.md`, `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| Through the cloud: Azure AKS, arm D against arm C, one set of 97 paired repetitions, not a three-run table | L | omni-v18 | The 99th-percentile response GAIN, down 11.0%, beyond the noise: the slowest requests waited less. The bill power given, up 1.2%, inside the noise. Failed requests LOSS, up 3.9%, inside the noise. No work counted, so the work per dollar is not read | 5.9; `results/live/AKS_STEADY_100_OMNI_V18.md`, `results/SITE_NUMBERS.md` |
| The whole organism, composed layer by layer | S, of L tables (the chip and the cloud enter as exactly 1) | across engines | GAIN, up 41.9%, a composition over work, speed and machines, with the machines held read power given (77.7% more machines held). A second reading under its own rule, never a measurement | 5.10; `results/WHOLE_SYSTEM.md`, `README.md` |
| Against its native, every standing table | L | omni-v25 and omni-v12 | 273 LOSS rows, each named, with its cause where one is written | 5.11; `docs/LOSS_LEDGER.md`, `results/verdict_audit/VERDICT_AUDIT.md` |

The hardware, plainly. The Kubernetes clusters run in kind on GitHub's rented runners, never called bare metal (class L; `DISCLOSURES.md`, section 10). The A10 is read by its own meter on omni-v23 and the A100 on omni-v21, omni-v18 and omni-v23 (class P; section 5.8). The CPU host is a model; the CPU's own meter is marked not yet run (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, sections 23.2 and 45.3). No bare-metal or cloud receipt stands on omni-v25 yet (`README.md`, "Benefit Against Native").

### 1.9 What the engine is not

**Not a sales claim.** The README opens with the aim: "More work, faster, on fewer machines, for the same energy and the same bill". The record does not yet bear all of it out: the index reads the work and the speed, and the machines are not yet fewer; the composition reads the machines held power given (`results/WHOLE_SYSTEM.md`; `README.md`, "Bill by Route"; section 5.10). The repository's own evidence-integrity notice says that the Omni index is an internally computed geometric-mean composite of heterogeneous ratios, "not a measured reduction in total compute bills or a universal throughput improvement" (`README.md`, evidence-integrity notice; `docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`).

**Not outside review.** Every result is run and scored by The Omni-Compass LLC's own code, and no outside party has reviewed or approved it (`results/OMNI_INDEX.md`; `docs/engine/APPRAISAL.md`). The appraisal's grades are the repository's own, and the integrity audit's rule for internally assigned grades is that they are never described as external referee certification (`docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`). "Preregistered" means written down in the repository before the runs; nothing was filed with an outside body (`results/OMNI_INDEX.md`).

**Not a bill saving yet.** Neither place's bill is resolved. On bare metal, no machine-hour or energy price is declared for an owner's own machines; through the cloud, no bill has yet been read from a three-run table on omni-v25 (`README.md`, "Bill by Route"). The bills that are printed are list prices or a rental rate applied to measured machine time (`results/TWO_BILLS.md`; `results/live/AKS_STEADY_100_OMNI_V18.md`), and the repository states that no dollar figure in it is a measured result (`DISCLOSURES.md`, section 2, item 6).

**Not a judge.** The page decides nothing: every word on it was decided in the repository by `tools/readings.py` when its table was written, and a monitor with no record shows nothing in its place (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, sections 35.5 and 45.1).

**Not a benchmark when a knob is turned.** The page is also a live tuning bench. Any knob can move any metric in either direction, and what the page shows at a setting other than the factory profile is the engine's range, never a result (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 45.7; `docs/FACTORY_PROFILE.md`).

**Not a proof of stability.** The formal record holds four theorems on bounded channels over the declared parameter box, and is not a global-stability proof (`docs/FORMAL_STATUS.md`; section 3.14). The page's "Ask Omni-Compass" answers, composed by a language model, are not a record either (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 45.6).

### 1.10 Threats to validity

**Authorship.** The law, the models, the scorer, the reading key, the page and its appraisal come from one source. The appraisal reproduces each part of the page "by an independent path" (`docs/engine/APPRAISAL.md`): independent of the page's code, not of its authors, so Q4 is answered internally. The repository's integrity audit of 29 October lists full provenance, exact-head reruns, physical meter calibration and independent replication as not completed (`docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`).

**The page's counts are not the audit's.** The appraisal counts the page's receipts, Omni-Compass against its native over 65 tables, at 291 LOSS rows as the tables wrote them and 220 after the 0.5% floor the page applies at load; the verdict audit, the one selection the LOSS ledger reads, counts 273 over its 61 standing tables. The appraisal prints the difference itself ("differ") for GAIN, power given, STEADY, LOSS, the runs disagree and shown (`docs/engine/APPRAISAL.md`, counts; `results/verdict_audit/VERDICT_AUDIT.md`). This monograph quotes the audit's 273 (`docs/LOSS_LEDGER.md`). A reader of the page may meet another count.

**The page can fall behind its records.** The rebuild is scheduled every third hour and after every result, yet on `main` the last page committed by the rebuild workflow is of 03:57 UTC on 6 November (`54ae35f3182`, in the git history of `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`), while new records landed after it the same day, among them `results/engine_runs/ENGINE_RUNS_500_3549104563.md`. The files do not record why no later build committed a page. A reader who needs the newest record reads the result file, not the page.

**A build time is not a page's identity.** Two later hand commits on `main` changed the page (04:16 and 10:10 UTC); the second, `415a18f73d8`, also gave the stamp the byte count and SHA-256 that earlier stamps did not carry, while the build record and the stamp still name 03:33 UTC. The self-update on `main` fetches only on a later build time (section 1.5), so a copy saved from an earlier commit of the same build never loads the later bytes. The working branch's builder adds a page identity to close that gap; its comment records the same finding of 6 November: four different pages carried one build time, so copies of three of them never loaded the newest (`docs/engine/build_live_engine.py`).

**The working branch and `main` differ.** On the working branch, commits from `6c79bb09da1` (6 November, 17:43 UTC) on changed the page and its builder without writing a new stamp, so there the page's bytes and SHA-256 no longer equal those in `docs/engine/LIVE_ENGINE_VERSION.json`, and its identity tag (`omni-page-id`) still reads zeros. The branch's builder adds that identity tag to the self-update's tests, and its `--check` also fails a page whose bytes or build time differ from the stamp's; its workflow writes the stamp before the one-file copy and the page word for word (`docs/engine/PAGE_WORD_FOR_WORD.md`), and adds the page's own tests to the check step. Were the branch's page pushed to `main` unstamped, a copy reading the stamp would refuse it on its byte count and keep the copy it has. The next build that runs `--stamp` restores the match.

**Descriptions that lag their objects.** Six were found while reading for this chapter. The one-file builder's header says the copy packs "21 records" (`docs/engine/build_standalone.py`), while the packed copy holds twenty-five, as the source page does (`docs/live/index.html`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`). The README calls that copy "about 15 MB" (`README.md`); on `main` it is 21,632,368 bytes (`docs/live/index.html`). The manual describes the eight-card GPU node as "Awaiting Its Run" and says the 8-card run has not been run (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, sections 23.4 and 23.2), while an eight-card record from omni-v23 is on file (`results/gpu/V23_A100_8CARD_STACKS_ABC.md`). The manual says the page names the engine its prose was written for in `data-prose`; the builder adds that attribute only when a new engine is adopted (`docs/engine/build_live_engine.py`, `main`), and the page carries `data-engine="omni-v25"` alone. Section 35.2 of the manual says the factory profile runs the dial's beat at 60 s, while the same section gives omni-v25's factory profile as a decision every 10 s on site and every 60 s through a cloud. `DISCLOSURES.md`, section 9, says Google and Amazon have no keys in the repository's secrets, while their queues' switches read on (`scripts/google_queue.txt`; `scripts/amazon_queue.txt`); the files do not say which holds now, and all of them agree that no set has run. The manual's own rule settles these cases: where a book and a receipt differ, the receipt prevails (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, "The Three Manuals").

**The published split copy.** The graded site audit read the published copy as naming omni-v23, with no self-update, at a time when omni-v24 stood (`docs/SITE_AUDIT.md`, section F). A copy without the self-update keeps the build it was published with until it is published again. Nothing in the files read for this monograph records a later republication from an omni-v25 build.

**The trust root of the self-update.** The stamp and the page come from the same branch. A matching SHA-256 shows that a copy arrived whole and unchanged. It does not show that the branch's content is right.

**Construct validity of the headline.** The Omni index is a geometric mean over heterogeneous ratios. Its "machines" axis can mean connections, consumers or memory held, and its energy on kind is a declared model, not a meter (`README.md`, evidence-integrity notice; `results/OMNI_INDEX.md`). The 0.5% floor and the three-run words are descriptive conventions, not statistical proof or exact equality (`docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`, release gate, item 5). Section 4.8 treats the index's construction in full.

**External validity.** The software-end results are from GitHub's rented runners in kind clusters. The chip and cloud receipts stand on older engines (omni-v23 and omni-v18), none yet on omni-v25, and the cloud's is one set run at the tune-down on the machines alone, not the whole engine. No result is a promise of a saving on any other system (`DISCLOSURES.md`, section 2, item 6); where a result elsewhere differs, the repository's first presumption is the wiring, the settings or how Omni-Compass was implemented or read (`DISCLOSURES.md`, section 4). The composed whole organism is class S over tables from several engines and must not be described as one deployed system's observed performance (`results/WHOLE_SYSTEM.md`; `docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`, release gate, item 4).

**Timeliness.** The page is true for the build its stamp names (section 1.4). Every count in this monograph is the repository's on 6 November 2026 and moves as the tables are run again on the engine that stands.

## 2. The System Under Test: the Stack, its Native Controllers and the Muscle Catalogue

### 2.1 What this chapter fixes

This chapter fixes the object of every measurement: each layer of the stack under test, the native controller that owns it, what that loop acts on and how often, and what Omni-Compass may write there. It then describes the muscle catalogue, the modelled counterpart of the stack, and how a catalogue row maps to a real setting. The receipts each layer has are listed in section 2.8 and read in chapters 5 and 6; this chapter gives only the catalogue's and the organisms' own modelled readings (class S, sections 2.5 and 2.6), which no later chapter repeats.

The engine that stands is omni-v25: omni-v24 with one fault fixed in the Kafka wire, its decisions byte for byte omni-v24's (`docs/OMNI_V25.md`; chapter 3). Receipts on older engines are named with their engine wherever they appear.

### 2.2 Where Omni-Compass sits: the cascade

In the vocabulary of cascade design, the native controllers are the inner loops, each closing on its own signal at its own clock, and Omni-Compass is one outer loop that reads them as one body (`docs/INDUSTRY_LANDSCAPE.md`).

Write the stack's native controllers as C₁, …, Cₙ. Each Cᵢ reads its signal yᵢ (a card's power, a pod autoscaler's utilisation, a pool's waits) and moves its actuator uᵢ under a setting θᵢ that an operator gave it (a power limit, a target, a pool size), by its own published rule:

  uᵢ(t) = Cᵢ(yᵢ(t); θᵢ).  (2.1)

Each Cᵢ reads only its own yᵢ. Omni-Compass leaves every Cᵢ in place and acts only on the θᵢ, at decision instants k, inside the range Θᵢ that the controller already accepts (its cover):

  θᵢ(k+1) = Πᵢ[ θᵢ(k) + Δᵢ(y(k)) ],  Πᵢ the projection onto Θᵢ,  y = (y₁, …, yₙ).  (2.2)

The increment Δᵢ comes from the compass law (`omnicompass/compass_law.py`; section 3.4). At the factory tune, the max, the setting moves toward the machine's own limit, never past it and never below native (`docs/MUSCLE_CATALOG.md`; section 3.5). The write in (2.2) is a setting, never an actuation, and never a bypass of Cᵢ. Equation (2.2) is a schematic of those two stated rules, not the law itself, and it does not cover a lever that hands a resource back: a machine parked for a cloud's autoscaler takes the count below native's, and such a machine is parked only after its own trial and woken on a breach (`results/live/AKS_STEADY_100_OMNI_V18.md`; section 3.6).

Every write passes through a two-way plug. It reads the setting once before the first write, reads back every write, steps aside if another controller moves the setting, and restores the setting at the end (`docs/MUSCLE_CATALOG.md`; section 3.4). Before its first write each process also records the commands that restore every setting, and renews a lease at every decision; a watchdog that finds the process gone or its lease stale runs those commands for it (`omnicompass/master.py`; section 3.9, which also reads that hand-back's cost on real Kubernetes).

One consequence holds for every table in this monograph: each layer was measured with the layer under it running as native runs it (`results/WHOLE_SYSTEM.md`, section 1). No run has stacked Omni-Compass on every layer at once; that run is preregistered and not yet made (`docs/WHOLE_SYSTEM_PREREGISTRATION.md`).

### 2.3 The layers, from the chip to the cloud

#### 2.3.1 The chip: power limit and clock ceiling

**Native.** The card's own firmware limits, reached through NVML and nvidia-smi: the power limit, the application clocks, MIG and the compute mode (`docs/wiring_recipes.csv`, family 9). In the A10 benchmark native is the card under the operator's power cap at 70% of the card's top (`results/gpu/V23_A10_CAP_FULL_ABC.md`).

**What Omni-Compass writes.** In the counted runs, two settings the card already accepts: the clock ceiling (`nvidia-smi -lgc`, reset with `-rgc`), which bounds how high the card's own boost may climb, and the power limit (`nvidia-smi -pl`), never over the limit read at the start (`docs/GPU_PREREGISTRATION.md`, amendment 5; `omni_controller/gpu_compass.py`). The firmware keeps its own control. The wire reads the card's draw, temperature, utilisation, limit and clock and the workload's response times. It never holds the ceiling under the card's own busy clock. A blind reading fails up; under a thermal or hardware slowdown it never tightens; a power limit it did not write stops its writes for the rest of the run. On exit both settings are reset and read back. Its decision period defaults to 2 s (`--interval`, same file). The earlier power-limit-only wire (`omni_controller/gpu_governor.py`) remains selectable and is not the counted arm (`docs/GPU_PREREGISTRATION.md`, amendment 5).

**Receipts.** Class P, on omni-v23 and omni-v21: section 5.8.

#### 2.3.2 The host: the kernel's frequency governor

**Native.** The Linux kernel's own controls: cpufreq (schedutil or the processor driver), RAPL, cpuidle and the memory manager; for the wider kernel family, cgroup v2 files and sysctl keys (`docs/wiring_recipes.csv`, families 8 and 53).

**What Omni-Compass would write.** The preregistered runner moves one knob, the frequency ceiling (`scaling_max_freq`, on every CPU), inside the cover from half the top clock to the top, and reads the processor's energy counter (RAPL) as its meter; the snapshot is restored at the end (`tools/run_cpu_power.py`). The family's wiring row also lists the RAPL package power limit as a wire (`docs/wiring_recipes.csv`, family 8); the runner does not write it. The question is whether, moving only the ceiling the kernel's loop works under, the same work inside the response line costs less energy by the processor's own meter (`docs/CPU_POWER_PREREGISTRATION.md`, section 1).

**Receipts.** None. GitHub's machines are virtual and cannot write the kernel's frequency setting; the live run needs a real Linux machine (`docs/wiring_recipes.csv`, family 8). The whole-system page lists the machine layer (the kernel, bare metal, Kepler) as not yet run and enters it as exactly 1 (`results/WHOLE_SYSTEM.md`, section 2); the Kepler energy meter is a kit built and preregistered (`docs/REGISTER.md`, row 79). The layer is wired on paper and empty on the record.

#### 2.3.3 The cluster: Kubernetes and its autoscalers

**The rig.** A six-worker cluster in kind (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines; each arm on a fresh cluster, the two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading (`results/live/GOVERNORS.md`; section 4.3). The six workers share one runner of four cores (`results/live/V25_FAIRNESS.md`, the host's rows). These are rented virtual machines, never bare metal (`results/SITE_NUMBERS.md`).

**Native controllers.**

- *The scheduler*: kube-scheduler's default profile as shipped places every pod of every Kubernetes set (`docs/REGISTER.md`, row 88).
- *The pod autoscaler (HPA)*: it checks every 15 s and the metrics it reads refresh every 15 s (`docs/PACE_PREREGISTRATION.md`); its scale-down stabilisation window is 300 s by default (`docs/OMNI_COMPASS_MANUAL.md`, section 24.4).
- *KEDA*: it scans every 30 s (`docs/PACE_PREREGISTRATION.md`); run live on the CPU target with the requests in flight, and with its HTTP add-on (`results/OMNI_INDEX.md`).
- *Vertical recommenders*: Goldilocks with the VPA's recommender, and CruiseKube applying its own recommendations, run live (`results/WHOLE_SYSTEM.md`, section 2).
- *The Cluster Autoscaler*: it scans every 10 s (`docs/PACE_PREREGISTRATION.md`). It is absent on kind, where the machines are made at the start (`docs/OMNI_V24.md`); it runs underneath only on AKS (section 2.3.6).
- *Karpenter*: the write path is written (a NodePool limit as the pool's size command, `docs/wiring_recipes.csv`, family 5), and register row 68 lists it as next, on Azure (`docs/REGISTER.md`). No Karpenter receipt exists.

**What Omni-Compass writes** (`docs/wiring_recipes.csv`, families 2, 3 and 5). The HPA's target and floor by kubectl patch, the operator's values recorded in an annotation first; KEDA through its ScaledObject, so the add-on keeps its own loop; the running pod's CPU limit in place through the pod's `resize` subresource, the template untouched, so no rollout; and the node pool, a machine parked by taint and drain, never deleted by Omni-Compass. On top of CruiseKube it never writes the CPU limit, which CruiseKube resizes in place itself (`docs/REGISTER.md`, row 81). Its own beat is read from the place it runs in: a decision every 10 s on site and every 60 s through a cloud, decided at the start from the nodes' providerID (`docs/OMNI_V24.md`; section 3.7); its fast checks run every 5 s (`--floor-interval`, `omni_controller/controller.py`).

**Receipts.** Class L, omni-v25: the nine tests of the index in sections 5.2 to 5.5; the cluster's 34 LOSS rows by gauge in section 5.6 (`docs/LOSS_LEDGER.md`); the two robustness tests in section 3.9.

#### 2.3.4 The services: five data stores

The stores run on GitHub's runners of four cores with no watt-meter (each store's preregistration, e.g. `docs/POSTGRES_PREREGISTRATION.md`). Their energy column is the host's processor seconds, a model's estimate, shown and scored as native's (`results/OMNI_INDEX.md`). Here native is not a loop. Each store's capacity setting has no controller of its own: a number is set once, as shipped or by the operator, and the store holds it through every quiet hour and every rush; that number is the native arm. The supervisory loop is therefore measured against a constant. Omni-Compass takes one reading a second (the store's own account of its latency; for Redis, the application's own request latency) and writes one setting through the store's own interface (each store's preregistration; `docs/wiring_recipes.csv`, families 18 to 20).

| Store and driver | Native (fixed) | Omni-Compass's one setting, its cover |
|---|---|---|
| PostgreSQL 16 behind PgBouncer 1.22, pgbench | the shipped pool, 20 server connections | `default_pool_size` through the admin console, [2, 90], never below the pooler's own setting (`docs/OMNI_V22.md`) |
| Apache Kafka | the operator's 2 consumers | the consumer group's size, [1, 8] |
| Redis | the operator's ceiling, 64 MB, allkeys-lru | `maxmemory` by CONFIG SET, [16 MB, 512 MB] |
| MongoDB under YCSB | the operator's cache, 512 MB | WiredTiger's cache size by setParameter, [256 MB, 2,048 MB] |
| MySQL under sysbench | the operator's pool, 512 MB | `innodb_buffer_pool_size` by SET GLOBAL, [128 MB, 2,048 MB] |

Native settings and covers: `docs/POSTGRES_PREREGISTRATION.md`, `docs/KAFKA_PREREGISTRATION.md`, `docs/REDIS_PREREGISTRATION.md`, `docs/YCSB_PREREGISTRATION.md`, `docs/MYSQL_PREREGISTRATION.md`. Besides the operator's setting, PostgreSQL runs as the distribution ships it behind PgBouncer's shipped pool (`.github/workflows/pgbench.yml`), and MySQL, Redis and MongoDB also run against native exactly as the vendor ships it (`scripts/reruns.txt`). For Redis that means no ceiling, so the knob is at its limit on native and Omni-Compass writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4).

**Receipts.** Class L, omni-v25: the categories in section 5.3; the stores' 14 LOSS rows in section 5.6 (`docs/LOSS_LEDGER.md`).

#### 2.3.5 The batch schedulers and the multi-cluster products

The list, versions and catalogue mapping are written once in `tools/governors_page.py` and printed with their readings in `results/live/GOVERNORS.md`. Each runs as its project ships it, the organism native under it: Kueue v0.20.2 with one ClusterQueue sized to the workers; Volcano v1.16.0 with its default queue; the KAI scheduler v0.18.6 with its chart's default queues; Koordinator 1.8.0 with colocation on; CruiseKube applying its own recommendations; Crane 0.11.0 with its Effective HPA in auto mode, on Kubernetes 1.25.16; KubeRay 1.7.1 with one Ray 2.52.0 cluster; the Gödel scheduler on Kubernetes 1.24.17; Armada v0.22.14 on its own local stack; Karmada v1.19.0 with two member clusters; Open Cluster Management (bundle 1.4.0) with two member clusters. On Crane's and Gödel's Kubernetes releases no pod is resized in place, so no processor limit is moved in any of their arms. KubeEdge and Nephio are listed with no rig built.

Omni-Compass sits on top with its own levers: the node pool, the service's autoscaler and processor limit, cruise and idle. It never writes a product's objects, places a pod or admits a job. The one exception is Crane, which owns the service's autoscaler; there Omni-Compass's moves reach it through Crane's own object by a plug, as on KEDA (`results/live/GOVERNORS.md`). On the scheduler rigs Omni-Compass's own process has a core of its own and the kind nodes the others (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 5). Eleven of the systems also run four ways in every repetition (section 4.6): the organism alone, the product as shipped, Omni-Compass on the organism alone, and Omni-Compass on top of the product (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendments 5 and 6). Cost: $0, on GitHub's free machines.

**Receipts.** Class L, omni-v25 (Koordinator's four ways omni-v12): section 6.5.

#### 2.3.6 The cloud: Azure AKS, with Google and Amazon wired

**Native.** Azure's managed Kubernetes with Azure's own Cluster Autoscaler underneath. The profile defaults the manual prints are a 10-minute unneeded time, a 10-minute delay after a scale-up and a 10 s scan (`docs/OMNI_COMPASS_MANUAL.md`, section 24.4).

**What Omni-Compass wrote.** In the set on file (run 40069633316, eastus, Standard_D2s_v4, the steady load, omni-v18) it ran at the tune-down on the machines alone: no pod autoscaler moved, no processor conveyed, no power capped. It parked only a machine the cloud had already made, after its own trial, and woke it on a breach (`results/live/AKS_STEADY_100_OMNI_V18.md`). That rule was struck on 31 October; the omni-v25 Azure sets are queued at the max (`results/OMNI_INDEX.md`). It asks the cloud for no machine and holds no cloud credential (`docs/INDUSTRY_LANDSCAPE.md`).

**Receipts.** Class L, one run of 97 paired repetitions (`results/live/AKS_STEADY_100_OMNI_V18.md`): section 5.9.

**Google and Amazon.** The same four sets are wired for GKE (us-central1-a, e2-standard-2) and EKS (us-east-1, m5.large) and were switched on again on 1 November; both queues' switches read on. A set starts only after the provider's $0 check passes; the first attempts of 18 October stopped at the login or the pre-flight at no cost, and no set has run to a result (`scripts/google_queue.txt`, `scripts/amazon_queue.txt`; `docs/LIMITATIONS.md`). `DISCLOSURES.md`, section 9, gives the reason as their keys not being in the repository's secrets (section 1.10 records the disagreement). Through any cloud the provider's chips and back end are inside its price and out of Omni-Compass's reach: a tenant cannot meter them (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`).

### 2.4 The clocks side by side

| Loop | Its period | Source |
|---|---|---|
| The HPA's sync; the metrics it reads | 15 s; 15 s | `docs/PACE_PREREGISTRATION.md` |
| The HPA's scale-down stabilisation window | 300 s by default | `docs/OMNI_COMPASS_MANUAL.md` |
| The Cluster Autoscaler's scan | 10 s | `docs/PACE_PREREGISTRATION.md` |
| KEDA's scan | 30 s | `docs/PACE_PREREGISTRATION.md` |
| AKS: a machine unneeded before deletion | 10 min (default) | `docs/OMNI_COMPASS_MANUAL.md` |
| Omni-Compass on the cluster, the full decision: on site; through a cloud | 10 s; 60 s | `docs/OMNI_V24.md` |
| Omni-Compass on the cluster, the fast checks | 5 s | `omni_controller/controller.py` |
| Omni-Compass on a data store | one reading a second | each store's preregistration |
| Omni-Compass on a card | 2 s by default | `omni_controller/gpu_compass.py` |

The usual design of a cascade keeps the outer loop well slower than the inner loops, so that each inner loop settles before its setting moves again. This stack does not keep that separation everywhere. On site the supervisory beat (10 s) is shorter than the HPA's sync (15 s), and the fast checks (5 s) shorter still, so Omni-Compass can move a target the HPA has not yet acted on. The 10 s beat was picked on our own models (class S), by a rule frozen before any reading, as the beat no other dominates on site (`docs/PACE_PREREGISTRATION.md`, amendments 4 to 6; `docs/OMNI_V24.md`; section 3.7). The formal statements on file (section 3.14) do not address the interaction of the beat with the native loops. How the clocks interact is a measured matter, not a derived one.

### 2.5 The muscle catalogue

**Definition.** A muscle is one setting on one machine that already has its own control: a replica target, a node pool's size, a GPU's clock ceiling, a chiller's setpoint, a battery's reserve, a joint's effort (`docs/MUSCLE_CATALOG.md`). The catalogue is `realms/catalog_v5.csv`: 1,107 rows in 70 families. Each row carries its identifier, its family, its name (the setting's own name on its controller), its home realm, the realms it sits in, its plant (the `template` column), its preset (the class of machine that decides the wire) and its kind of knob.

**Four kinds of knob** (definitions `docs/MUSCLE_CATALOG.md`; counts `realms/catalog_v5.csv`, `docs/WIRING_VERDICTS.md`): capacity, how much of the machine is in service (539); admission, what is let in (275); setpoint, the target the machine's own loop holds (174); power, the share or limit it may draw (119).

**Five plants.** Each muscle is modelled on one of five plants, each with its own service reading and lever (`docs/MUSCLE_CATALOG.md`): `compute_pool` (695 muscles), `process_loop` (195), `motion_axis` (116), `energy_storage` (54) and `thermal_zone` (47) (counts from `realms/catalog_v5.csv`).

**Home realms.** Compute / AI / Cloud 444, Physics / Robotics / Autonomous 137, Energy / Facility / Industrial 249, Distribution / Specialized 277 (`docs/MUSCLE_CATALOG.md`).

**Cards.** One brain, each muscle's settings its own: 364 muscles carry a card of their own (`realms/muscle_cards_v5.csv`); the rest run the global setting (`docs/MUSCLE_CATALOG.md`).

**What the catalogue reads (class S).** Each muscle alone on its plant under two loads, at the max on omni-v8, seeds 3000 to 3009 (`results/realms_v5/REALMS_V5.md`): 530 muscles read GAIN and earn a wire in; 577 stay native. Of those, 421 are at their limit on native (all 275 admission knobs among them, since native already lets everything in) and 156 read the same as native (`docs/WIRING_VERDICTS.md`). No muscle alone read LOSS, or GAIN and LOSS, under any load (`results/realms_v5/REALMS_V5.md`, the no-harm check). The ranking heaviest hitter first is read from the same omni-v8 record; the first row of the Compute / AI / Cloud table is architecture selection (muscle 108), GAIN, 3.12% of its decisions brought back under its line (`docs/MUSCLE_CATALOG.md`). These are a model's readings of the engine on plants we wrote, not benchmark results.

### 2.6 The seven organisms and the eighth

The organisms are groupings of catalogue rows made in the runners, never in a fingerprinted engine file (`tools/run_realms_v5.py`). Let Rₖ be the set of muscles whose realm list includes realm k, for k = 1, …, 4 (`docs/MUSCLE_CATALOG.md`):

- the four realms: |R₁| = 540, |R₂| = 404, |R₃| = 480, |R₄| = 484;
- the spine, the muscles in all four: |R₁ ∩ R₂ ∩ R₃ ∩ R₄| = 267;
- the whole tower, every muscle once: |R₁ ∪ R₂ ∪ R₃ ∪ R₄| = 1,107;
- the four stacked, every duplicate kept: |R₁| + |R₂| + |R₃| + |R₄| = 1,908.

The counts are mutually consistent. In `realms/catalog_v5.csv` a muscle sits either in all four realms (267) or in exactly one (840). The stacked count therefore exceeds the tower by three copies of the spine:

  1,908 = 1,107 + 3 × 267,  (2.3)

and the home realms sum to the tower, 444 + 137 + 249 + 277 = 1,107.

With every muscle written at once by one brain, on omni-v8, each of the seven organisms read GAIN (fewer misses) under each of its three loads (its own, the climb, work waiting in line). The power given beside it was at most 0.046% of native's energy, and the work moved by at most 0.003%. The tower under the climb read misses down 0.094 percentage points (`docs/WIRING_VERDICTS.md`; `results/realms_v5/REALMS_V5.md`). Class S.

**The orchestra, the eighth organism.** Every catalogue muscle that stands for a knob of a named scheduler or orchestrator joins a body for that product, and all of them together form one body of 55 muscles. The mapping is in `tools/governors_page.py`: the Kubernetes scheduler to twelve rows of family 4, Kueue to five admission rows of family 1, Karmada to four rows of family 39, and so on. Each body runs native and with Omni-Compass on top at the max, on omni-v12, seeds 3000 to 3009 (`results/orchestra/ORCHESTRA.md`). The orchestra read GAIN (more work and fewer misses) under all three loads, with power given beside it: the body's energy up 25.4% under its own load, 54.5% under the climb and 42.4% with work waiting in line (`results/orchestra/ORCHESTRA.md`). The Kueue, Volcano, KAI, Koordinator, KubeRay and Gödel bodies read STEADY, the same as native (`results/live/GOVERNORS.md`). The same file states the limit: "a plant written by the people who wrote the law is not an independent test." The model and the live record differ in kind: where the model reads Kueue STEADY, the live two-way table carries nine LOSS rows (section 6.5).

### 2.7 From a muscle to a real knob

`docs/wiring_recipes.csv` holds one row per family (70 rows). Each names the native controller that owns the family's muscles, where the reading is tapped (the wire out), where the setting is written (the wire in), how it is restored, and whether that wire has run live. Worked examples:

| Muscle (catalogue id) | Native controller | Wire in | Restore | Status |
|---|---|---|---|---|
| `hpa_cpu_target` (18), `hpa_min_replicas` (1001) | the HPA or KEDA ScaledObject | target and floor by kubectl patch; KEDA through its ScaledObject | from an annotation written first | live |
| `cpu_limit` (34) | the pod's requests and limits; VPA, Goldilocks or CruiseKube | the limit in place through the pod's `resize` subresource | to the operator's limit | live (not written on top of CruiseKube) |
| `node_pool_min` (66), `node_pool_max` (67) | Karpenter, the Cluster Autoscaler, a MachineSet, a cloud node pool | the pool's size by the operator's own command; parking by taint and drain | the starting count | live on kind and AKS |
| `gpu_power_limit` (130), `gpu_sm_clock` (131) | the card's firmware through NVML | `nvidia-smi -pl`; `-lgc` and `-rgc` | the snapshot in the card's audit | live on rented A10 and A100 cards |
| `cpufreq_max` (114) | Linux cpufreq and RAPL | `scaling_max_freq` through sysfs | from the snapshot | written and tested on a modelled machine, not run live |
| `db_pool_resize` (283), `buffer_pool` (1102) | PgBouncer's console, MySQL's SET GLOBAL, MongoDB's setParameter | `default_pool_size`; `innodb_buffer_pool_size`; WiredTiger's cache size | read once first; a failed read-back stops the writer | live |

Rows: `realms/catalog_v5.csv`; wires: `docs/wiring_recipes.csv`, families 2, 3, 5, 8, 9 and 18. By the file's live column, seven families have run live: Kubernetes Workload Scaling, Container Resources, Node Fleet & Karpenter-Class Control, GPU Hardware, Database & Transactions, Messaging & Streaming, and Cache & Memory Services. AI Inference Serving and Reliability, Security & Recovery are live in part. Cloud VM & Capacity is live on AKS through the node pool. Host CPU & Memory and Linux Kernel & OS Control are written, not run. Work Admission & Demand Shaping is read only, at its limit on native. The other 57 families are modelled. A live family does not make every one of its muscles live: the receipts are for single knobs in it. The verdict per knob from every result on file (`docs/WIRING_VERDICTS.md`): on the real stacks, of 26 knob-cases, 1 is write, 21 operator's choice and 4 watch.

### 2.8 Where the receipts are

| Part of the system | Class | Engine | Receipt | Read in |
|---|---|---|---|---|
| The chip: A10 | P | omni-v23 | `results/gpu/V23_A10_CAP_FULL_ABC.md`, `results/TWO_BILLS.md` | section 5.8 |
| The chip: A100 | P | omni-v21 (one card); omni-v23 (eight cards) | `results/gpu/V21_A100_CAP_ABC.md`, `results/gpu/V23_A100_8CARD_STACKS_ABC.md`, `results/WHOLE_SYSTEM.md` (section 3b) | section 5.8 |
| The host | none | — | `docs/CPU_POWER_PREREGISTRATION.md` (written, not run) | section 2.3.2 |
| The cluster and its add-ons | L | omni-v25 | `results/OMNI_INDEX.md`, the `results/live/` tables named V25 (e.g. `results/live/V25_FAIRNESS.json`) | sections 3.9, 5.2 to 5.7 |
| The five data stores | L | omni-v25 | `results/OMNI_INDEX.md` | sections 5.3, 5.6 |
| The batch schedulers and multi-cluster products | L | omni-v25 (Koordinator's four ways omni-v12) | `results/live/GOVERNORS.md` | section 6.5 |
| The cloud: Azure | L | omni-v18, one run | `results/live/AKS_STEADY_100_OMNI_V18.md` | section 5.9 |
| The cloud: Google, Amazon | none | — | `scripts/google_queue.txt`, `scripts/amazon_queue.txt` | section 2.3.6 |
| The catalogue and the seven organisms | S | omni-v8 | `results/realms_v5/REALMS_V5.md`, `docs/WIRING_VERDICTS.md`, `docs/MUSCLE_CATALOG.md` | sections 2.5, 2.6 |
| The orchestra | S | omni-v12 | `results/orchestra/ORCHESTRA.md` | section 2.6 |
| The layers composed | S of L and P | across engines | `results/WHOLE_SYSTEM.md` | section 5.10 |

### 2.9 Threats to validity

1. **Native as a constant.** At the data stores native is a fixed setting. A GAIN there answers whether a moving setting outperforms this fixed one, not whether it outperforms an adaptive controller; other preregistered values would give other readings.
2. **The rig is not bare metal.** GitHub's runners are virtual and rented; the six kind workers share one runner of four cores; energy there is a declared model or processor seconds, never a meter. The host layer has no receipt because the runners cannot write the kernel's frequency setting.
3. **The node layer under a real node autoscaler.** On kind no Cluster Autoscaler runs. The only receipt with one underneath is one Azure run on omni-v18, at the tune-down on the machines alone, a rule since struck. No Karpenter, GKE or EKS result exists.
4. **Engines differ by layer.** The A10 is omni-v23, the A100 omni-v21, Azure omni-v18, Koordinator's four ways and the orchestra omni-v12, the catalogue and the seven organisms omni-v8, the cluster and the stores omni-v25. No table is pooled across engines, but layers set side by side are different engines.
5. **The model does not map one to one onto the live knobs.** Catalogue rows are generic. Kafka's consumer group size has no row named for it; the nearest, `consumer_concurrency` (296), is typed admission, a kind that reads at its limit on native in the model (`realms/catalog_v5.csv`). The orchestra reads STEADY where live tables carry LOSS rows, and the orchestra's GAIN came with 25.4% to 54.5% more modelled energy. The plants were written by the people who wrote the law.
6. **Clock ordering.** On site the supervisory beat and its fast checks are shorter than the HPA's sync, so the usual cascade argument does not apply, and the formal statements on file do not cover this interaction (section 3.14).
7. **Documentation lag.** Several pages cited here for definitions only trail the record. The live column of `docs/wiring_recipes.csv` still names V3 tables for the stores, names the power-limit-only card wire, and says the card runs wait on Lambda. Amendment 1 of `docs/GPU_PREREGISTRATION.md` says the wire never writes clock locks; amendment 5 replaced that arm with the two-wire one. `docs/WIRING_VERDICTS.md` labels the 1,107 modelled muscles "omni-v5 at the max", where the record it reads names omni-v8 (`results/realms_v5/REALMS_V5.md`), and its "Not decided here" predates the A10 receipt. Section 4 of `results/WHOLE_SYSTEM.md` says "on omni-v12" while its rows read omni-v25 tables for every system but Koordinator (section 5.10). `docs/INDUSTRY_LANDSCAPE.md` prints an earlier Omni index, which `results/OMNI_INDEX.md` supersedes (section 6.14).
8. **Scale and use.** Every receipt is from evaluation rigs run and scored by The Omni-Compass LLC's own code. None is from production use, and no outside party has reviewed the results.

## 3. The Mechanism: the Compass Law, the Supervisory Loop, the Immune System and the Kill Switch

This chapter states, from the code, what Omni-Compass computes and writes at each decision and what happens when it is stopped. It concerns the engine that stands, omni-v25 (`OMNI_V25.json`, 65 fingerprinted files). Omni-v25 moves no rule, gain, guard, preset, card or law against omni-v24. It fixes one fault in the Kafka wire (the producer process is now started before Omni-Compass's own thread, and a producer still running 120 s past its schedule stops its workload) and corrects one comment in the Kubernetes controller (`docs/OMNI_V25.md`). The model gate read omni-v25 identical to omni-v24 on all twelve models, 104 readings and none different (`results/model_gate/V25_VS_V24.md`, class S, modelled).

Each statement below rests on one of three supports, kept apart: the code itself, read directly; the tests and C++ twins that hold the code to its own specification; or receipts from live software (class L) and a physical card's own report (class P). Readings against native appear in this chapter only where they test a safety mechanism.

### 3.1 Where the mechanism sits

Every muscle Omni-Compass acts on keeps its own native controller: the HPA and VPA size pods, the Cluster Autoscaler and Karpenter size node pools, Linux schedutil picks processor frequency, and NVIDIA DCGM manages the GPU (`omnicompass/nervous_system.py`, docstring; section 1.1).

On Kubernetes it writes each HorizontalPodAutoscaler's CPU target and, where the replicas bind, its replica range, and it sizes one node pool through the operator's own command template (`omni_controller/controller.py`, docstring and the replica-room code). On a card it writes two levers, the clock range and the power limit, through `nvidia-smi` (`results/SEAL.json`, `python_only`; the two covers in the first line of `results/gpu/drill-20261024T091235Z/audit-switch.jsonl`).

Two consequences follow. When Omni-Compass stops, the native controllers keep running on the settings then in force, so safety at a stop depends on what those settings are and on how fast they are handed back (sections 3.9 to 3.11). And the mechanism is present only in arms B and D (the chip and the cloud with Omni-Compass on native), never in arms A and C (`results/SITE_NUMBERS.json`, `four_arms`).

### 3.2 The state, the observation and the control law

The engine's state is x = (E, U, I[U], S, B, Ḃ) (`omnicompass/core.py`). In the Owner's Manual's words (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`, section 4): E is the deviation; U the alignment, a double well with poles at −1 and +1, and the controlled channel; I[U] the memory of misalignment; S the basin structure; B and Ḃ the bath. The equations, as `omnicompass/core.py` writes them:

  (3.1) dE/dt = −α[E]·E + β[int] + β[ext] + v[eff]
  (3.2) dU/dt = μ·U·(1 − U²) − (dE/dt)/E[max] − λ[U]·U + u,  |u| ≤ 25
  (3.3) dI[U]/dt = (1 − U) − σ₁·E − δ·S − λ[I]·I[U]
  (3.4) v[eff] = cos(ω[B]·t/2)·c·tanh(λ₀ + λ₁·(U − 0.5) + λ₂·S)
  (3.5) Φ(S) = α[s]·S²/2 + β[s]·S³/4 − δ·S
  (3.6) dS/dt = −dΦ/dS = δ − α[s]·S − (3/4)·β[s]·S²
  (3.7) dB/dt = Ḃ,  dḂ/dt = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B

Integration is classical fourth-order Runge–Kutta, ten micro steps of 0.01 in each macro step of 0.1, with the command held through all four stages of each micro step (`omnicompass/core.py`, `macro_step`).

**The observation.** At each decision the telemetry becomes nine clipped channels and one flag (`omnicompass/adapter.py`, `observe_vector`). On Kubernetes the controller fills them as follows (`omni_controller/controller.py`, `step`; `omni_controller/muscles.py`, `sense`):

| Channel | Range | On Kubernetes |
|---|---|---|
| queue q | [0, 2] | pending pods per replica, or the latency pressure (p95 ⁄ SLO − 1, or the failed share) if higher |
| load | [0, 2] | CPU used over the allocatable CPU of the recommended machines |
| power | [0, 1.5] | an operator's power command over the site limit, where both are given; else zero |
| thermal | [0, 1.5] | a heat model or the card's own temperature, where wired; else zero |
| network | [0, 1.5] | zero |
| drift | [0, 1.5] | how far an observed setting stands from a command still landing |
| stale | [0, 1] | the share of declared senses that are blind |
| security | [0, 1] | the hold flag of a named ConfigMap, where one is named; else zero |
| conflict | [0, 1] | count over four; the controller passes a count of zero |
| clean | 0 or 1 | no breach and no blind latency sense over the clear time (180 s by default) |

Fixed weights turn the channels into an observed state, for example

  E[obs] = clamp(0.25·q + 0.18·max(0, load − 0.85) + 0.16·power + 0.13·thermal + 0.10·network + 0.08·drift + 0.06·conflict + 0.04·stale, 0, 1.5),

and set the two pressures β[int] and β[ext] (`omnicompass/adapter.py`, `assimilate`). The state is blended toward the observed state, x ← (1 − a)·x + a·x[obs], with a = 0.339 at the reference minute, and then evolved one macro step with the command at zero (`Governor.step` calls `macro_step` with no target).

**The control law.** On U the core evaluates

  u = sat(−f[U](x, t) + K[P]·(σ − U)),  K[P] = 12,  |u| ≤ U[auth] = 25,  (3.8)

where f[U] is the drift of (3.2) with the command at zero and σ ∈ {−1, +1} is the target pole; the adapter evaluates it with σ = +1 (`omnicompass/core.py`, `control_command`; `omnicompass/adapter.py`). This u never moves a lever. Its push, u ⁄ 25, goes to the nervous system, which uses it to decide whether anything may be given back (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`, section 4.3).

### 3.3 The four pieces and the allocation law

`docs/book/THEORY.md` describes the engine as four pieces and says where each appears in the software: piece 1 in the state equations (deviation, alignment, memory and basin), piece 2 in the basin potential and its flow, piece 3 in the bath, and piece 4 in the one law that couples every muscle with no outside authority. Read against the code:

| Piece | In the software (`docs/book/THEORY.md`) | Code that carries it |
|---|---|---|
| 1 | the state equations | equations (3.1) to (3.3) and the control law (3.8), `omnicompass/core.py` |
| 2 | the basin potential and its flow | equations (3.5) and (3.6), `omnicompass/core.py` |
| 3 | the bath | equation (3.7) and the drive (3.4), `omnicompass/core.py` |
| 4 | one law over every muscle | the allocation law and the nervous system's grants, `omnicompass/adapter.py`, `omnicompass/nervous_system.py`, `cpp/src/governor.cpp` |

The fourth row's mapping to files is this monograph's reading of the code. `docs/book/THEORY.md` adds that the wider physical theory behind the pieces is where the design came from; the software has not measured it, and no result depends on it.

**The target utilisation.** The allocation law sets

  ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρ[min], ρ₀)  (3.9)

(`omnicompass/adapter.py`, `AllocationLaw`). Its defaults are ρ₀ = 0.914, ρ[min] = 0.627, k[I] = 0.252, k[E] = 0.297. The Kubernetes controller runs the fleet mode instead (`mode_law("fleet")`), whose values are ρ₀ = 0.829, ρ[min] = 0.769, k[I] = 0.072, k[E] = 0.487 (`FLEET_MODE`), and it clamps the result to [0.5, 0.95] before use (`omni_controller/controller.py`). Under the controller's default law (`--law governor`) ρ* is the HPA target; under the compass law (section 3.4) it is audited and bounds the idle floor.

**The body's calm.** The nervous system computes

  calm = κ·h·(1 − clamp(σ[S] − 1, 0, 1))·(1 − clamp(ν, 0, 1)),  (3.10)

where κ = 1 while the push is at or below the release threshold (`push_release`) and `push_release` ⁄ push above it; h = clamp((U − U[gate]) ⁄ (1 − U[gate]), 0, 1); σ[S] = S ⁄ S*, with S* the root of equation (3.6); and ν = max(0, I[U]) (`omnicompass/nervous_system.py`, docstring).

Authority is asymmetric. Adding capacity is allowed except under a security hold. Giving back needs calm at or above the organ's threshold θ (pods 0.5; machines 0.7; processor frequency, GPU and power 0.3; routing 0.5) and a clean line (`omnicompass/nervous_system.py`, `THETA`).

### 3.4 One law across every muscle: the compass law

The compass law (`CompassLaw`, `omnicompass/compass_law.py`) is written once for every muscle. On Kubernetes it runs when the controller is started with `--law compass`, as the kind rig (`scripts/kind_bench.sh`) and the cloud install file (`deploy/install/omni-compass-cloud.yaml`) start it; the parser's default is the allocation law of section 3.3. Each muscle has two bands:

- **The cover** [lo, hi] is the lever's hard range. Every write is clipped to it.
- **The compass** places the service reading in its band as a position p = (r − r[lo]) ⁄ (r[hi] − r[lo]), where 0 is calm and 1 is the service line. Its walls stand at 0.05 and 0.95, so the last 5% on each side is cushion.

From the position the law forms a smoothed velocity and a bounded force:

  v ← s·v + (1 − s)·(p − p[prev]) ⁄ dt  (3.11)
  F = A·tanh((K[P]·(p − c) + K[D]·v) ⁄ A)  (3.12)

Here c is the centre, A the authority, K[P] the pull and K[D] the push against whatever is moving the position. The hyperbolic tangent bends the force smoothly into its ceiling A instead of meeting it at a corner. Two rules override the formula:

- **Fail up:** if p ≥ 1 − cushion, then F = A at once, before the line.
- **No take-back while climbing:** if F < 0, v > 0 and p > c, then F = 0.

By default K[D] is critical damping for a first-order muscle with response time τ:

  K[D] = max(0, 2·√(K[P]·τ ⁄ dt) − 1)·dt.  (3.13)

The Kubernetes controller sets K[P] = A = 1, τ = 60 s and a smoothing of 0.3 a minute, evaluates K[D] at the reference minute (dt = 60 s, which gives K[D] = 60 s), and then multiplies it by three, citing "the same push as on every realm muscle" (`omni_controller/controller.py`). The live loop is therefore damped at three times the value the formula calls critical at the reference minute.

**Antagonist pairs.** A positive force adds capacity and a negative force takes it back, each side with its own gain, because adding and taking back do not cost the same. On Kubernetes the HPA target moves by 0.10·F up or 0.02·F down, times the cover's width, per minute (`COMPASS_UP`, `COMPASS_DOWN`, `step_scale`); a machine is asked back only when F falls below −0.2 with the position below the centre and the verdict's depth allows it (`COMPASS_RELEASE`).

**The reading on Kubernetes.** The reading is the mean response time of the latency window, placed between the bare service time (a tenth of the SLO) and the SLO. Each of the following sets p = 1: a pod waiting for a place, a blind latency sense, or a 95th percentile at or past the SLO (`omni_controller/controller.py`).

**The plug** (`Plug`, `omnicompass/compass_law.py`) has one wire in and one wire out. `attach` reads the lever once, before any write: that value is the snapshot, and it never moves. `write` checks that the lever stands where the plug last left it, clips the new value to the cover, sends it and reads back what the device took. `restore` returns the lever to the snapshot. A lever found at a value the plug did not write has another owner: the plug raises `ForeignWriter` and stops writing it, since restoring over it would fight the new owner. This is the one-writer rule. The Kubernetes controller does not use the `Plug` class: it records each original on the object itself as an annotation (the constants `ANNOTATION` and `RANGE_ANN`, the original target and the original replica range) before its first change and restores from those records (`omni_controller/controller.py`, `restore`).

### 3.5 Every muscle to its own limit, never past it

The default dial is the max: each muscle's settings moved toward more work, faster, up to the muscle's own limit and never past it, a step kept only where the muscle is never behind native for it (`DISCLOSURES.md`, section 3; `docs/THE_TUNE.md`, section 1). In the Kubernetes controller the max is four constraints (`omni_controller/controller.py`):

1. **Centre.** The compass's centre is 0.3 at the max and 0.4 at the tune-down.
2. **No give-back.** The verdict's deepest step is forced to zero, so no machine the cluster ran on its own is given back.
3. **Target cover.** The HPA target moves only inside [max(10, 0.6·T[op])·g, T[op]·g], where T[op] is the operator's own target and g ≥ 1 is the gain of a raised CPU limit (g = 1 where none is raised; `_gain`). With g = 1 the autoscaler is never asked for fewer pods than its own rule asks at the operator's target; with g > 1 the target rises by the same factor, so each pod is held as busy as the operator's target holds it.
4. **Floor.** The pool never falls below what the pods' CPU requests with 50% headroom (`--headroom`), or current use, need, nor below two machines (`--min-nodes`).

The cushion is enforced three times:

- the compass law's walls at 0.05 and 0.95;
- the nervous system's living band, which keeps every envelope it grants between 5% and 95% of the organ's range (`omnicompass/nervous_system.py`, `BAND`);
- the safety shield's five invariants, security, bounds, coherence, power and rate, on the actions it is given (`omnicompass/shield.py`); on Kubernetes every machine action passes through it. The shield's docstring limits its guarantee to those invariants under the observed state; it does not certify the plant model.

What the max spends is power given: a resource put in to buy work and speed, shown beside them and never called a loss. These limits bound the levers. They do not keep the service under its line (section 3.15).

### 3.6 The verdict: do no harm as a trigger

A lever that is slow to reverse, such as a machine given back, moves only after a paired trial on the muscle itself (`omnicompass/verdict.py`). While the service is calm the lever stands at the reference (stepwise: the deepest step already allowed) until enough pieces of work are measured; it then moves one step deeper until as many again are measured. The trial is read on log costs:

  d = mean ln c[trial] − mean ln c[ref],  interval d ± 1.96·se (Welch),  τ = ln(1 + tolerance).  (3.14)

An interval wholly above zero is a LOSS: the step is undone and not tried again until the recheck time has passed. While an interval is wider than the allowance, the trial measures on, up to three times the minimum sample. Otherwise the step is allowed only if both the median and the mean of the log costs lie within the allowance, d ≤ τ. Run stepwise, each step is judged also against the costs first measured at native, so steps cannot add up past the allowance. A trial that sees the service leave calm, or that runs past its time, is abandoned.

The Kubernetes controller runs it stepwise with a 2% allowance, 200 requests a phase, a trial every 600 s, a refused step retried after 7,200 s and a phase abandoned after 1,200 s (`--allow`, `--verdict-samples`, `--verdict-every-s`, `--verdict-recheck-s`, `--verdict-trial-s`), and it starts no trial before it has watched for one recheck period (`omni_controller/controller.py`). At the max the verdict runs and is audited but gives nothing back (section 3.5). For an interval that straddles zero the fingerprinted verdict file still writes the word retired on 25 October; the key reads that word as STEADY (`tools/readings.py`; section 4.4).

### 3.7 The beat and the loop: read, decide, write

**The beat.** The full decision runs every 10 s on site and every 60 s through a cloud (`omni_controller/controller.py`, `FACTORY_BEAT`). The place is read once, at the start, from the nodes' `providerID`: a public cloud's machine makes the cluster a cloud's, anything else is on site, a failed or empty reading keeps the longer beat, and `--interval` set by hand always wins. In node-pool mode the fast checks (the scheduling floor, the pod reflex, the conveyance's clock) run every 5 s between decisions. The two beats were picked by a rule written before the ladder was read (`docs/PACE_PREREGISTRATION.md`, amendments 4 to 6; `docs/FACTORY_PROFILE.md`, section 1), on a modelled ladder (`results/model_gate/V23_LADDER_CORRECTED.md`, class S); section 6.3 reads that ladder's cloud rows, and section 6.5 the cost the on-site beat carries on a shared host.

The engine keeps its own minute. At a beat of P seconds, k = P ⁄ 60, and the observation's weight becomes

  a(P) = 1 − (1 − 0.339)ᵏ.  (3.15)

The engine advances k of its macro interval, dwells and waits last the same number of seconds at any beat, and for a beat shorter than a minute the machines added or removed over the last minute stay inside the per-minute limits (`omnicompass/adapter.py`, `Governor.step`). The loop keeps a fixed schedule: missed slots are skipped, never run in a burst, and a step that outruns its slot is audited (`omni_controller/controller.py`, `main`).

**One decision.** The contract is that of `docs/FACTORY_PROFILE.md`, section 3:

  y(k) = h(x(tₖ)) + ε(k);  (u[req](k), z(k+1)) = G[θ](z(k), y(k), A(k));  u[cmd](k) = Π[C](u[req](k));  u[ack](k) = R(u[cmd](k));  x(tₖ₊₁) = Φ(x(tₖ), u[ack](k), w(k))  (3.16)

It keeps three settings apart: the one requested, the one commanded, and the one the device acknowledged. The Kubernetes controller carries it out in this order (`omni_controller/controller.py`, `step`):

1. **Kill check.** The controller's kill file, `OMNI_KILL=1` or the master switch: every setting is restored and nothing else runs.
2. **Read.** Nodes, pods, autoscalers, metrics. With no machine in service the reading is blind: nothing is decided or written.
3. **Proprioception.** Each recent command is watched for 60 s (`LAND_S`); its drift enters the observation.
4. **Engine.** Assimilate and evolve, twice: once on the whole body's view and once on the machine organ's own view; the push, ρ* and the grants.
5. **Compass and verdict.** Position, force, the verdict's tick; fail up at the wall.
6. **Release gate.** A machine goes back only if the gate, the reserve for the largest recent rise and native's own utilisation line all allow it, and at most one a minute.
7. **Audit.** Senses, state, authority, the gate's reason, the compass record and the recommendation.
8. **Targets.** For each sensed autoscaler: the immune rule (section 3.8), then the original recorded as an annotation, then the patch, each write audited.
9. **Pool.** The machine count through the shield and the operator's command.

A decision that raises an error writes nothing more, the error and the count of failures in a row are audited, and the next decision comes on time. There is no automated fallback (`safe_step`).

### 3.8 The immune system and the redline reflex

The redline reflex has two layers (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, section 2.20). The first is the compass law's fail-up, full force at 0.95 of the band, before the line. The second is the immune system's self-knowledge (`Immune`, `omnicompass/immune.py`), which acts when that push is not enough. For one lever it compares p[omni], the gauge over its line under Omni-Compass's setting (1 is on the line), with p[native], a twin's reading of the same moment under native's setting. With the factory constants (a streak of 3 decisions, relief 0.05, margin 0.05, holds of 10 to 160 decisions):

  redlining ⇔ p[omni] > 1 for 3 decisions in a row
  stuck ⇔ redlining ∧ (at its limit ∨ p[omni] > p[red]·(1 − 0.05)),  p[red] the reading when the redline began
  stronger ⇔ p[native] < p[omni]·(1 − 0.05)

Stuck with native stronger, the lever is handed to native for a hold that starts at 10 decisions, doubles with each hand-back up to 160 and halves after a quiet hold. Stuck with native not stronger, Omni-Compass keeps the lever and audits why, because redlining less than native would is still a benefit against native. After a hold it takes the lever back only when p[omni] ≤ 1 and p[omni] < p[native]·(1 − 0.05). An organ all of whose levers are held native has no authority from Omni-Compass until one returns (`omnicompass/nervous_system.py`, `native_hold`).

**On Kubernetes**, p[omni] = p95 ⁄ SLO. Native's twin is modelled, not measured: it takes the replicas native's rule would ask for the measured demand, n[native] = ⌈100·demand ⁄ T[op]⌉, and scales the wait as a single queue would,

  p[native] = p[omni]·(1 − ρ[omni]) ⁄ (1 − ρ[native]),  (3.17)

with ρ[omni] = min(0.98, demand ⁄ replicas) and ρ[native] = min(0.98, demand ⁄ n[native]), each pod's busy share of its request (`omni_controller/controller.py`, `_immune_native`). The lever counts as at its limit when the target is at the bottom of its cover or the replicas are at the autoscaler's maximum.

The omni-v19 immune rules stay in force (`docs/OMNI_V21.md`). Among them: while a pod waits for a place, every autoscaler whose target Omni-Compass holds below the operator's gets the operator's target back from the fast check, held for 600 s, doubling with each hand-back in a row up to 7,200 s (`omni_controller/controller.py`, `_pods_wait_handback`).

### 3.9 The lease and the heartbeat

"Heartbeat" names two things in this repository. The beat is the decision interval (section 3.7). The heartbeat proper renews the lease.

Before its loop starts, the Kubernetes controller registers its process id, a lease time, a staleness limit of max(120 s, 5 × beat) and the exact commands that put every setting back, a `--restore-only` run (`omnicompass/master.py`, `register`; `omni_controller/controller.py`, `main`). It renews the lease before every decision (`heartbeat` in `omnicompass/master.py`).

A watchdog runs as its own service (`tools/omni_switch.py watchdog`). It finds any controller whose process is gone or whose lease is stale, stops a hung process first, then runs the recorded commands. Those commands read each original value from the annotation written before the first change and try each step of the hand-back five times (`RESTORE_TRIES`, `omni_controller/muscles.py`). The watchdog acts only on registry records owned by its own user or root, not symbolic links and writable by no other user (`tools/omni_switch.py`, docstring).

In the models the lease walks every setting back gradually, over 24 decisions (`realms/harness.py`, `WALK`). Live, the recorded commands put each setting back directly.

**Receipt** (class L, kind on GitHub's runners, omni-v25, 10 pairs in each of three runs; `results/live/V25_ROBUST_KILL.md`). The controller is killed outright mid-run; native's arm has no controller, and the kill moment marks the same window in both arms (`docs/ROBUSTNESS_PREREGISTRATION.md`). Over each repetition the Omni-Compass arm wrote, on average, 71.7 to 80.2 settings commands on its own (shown, not judged), so the hand-back reversed settings that had moved. In every repetition of all three runs every setting was back at the operator's inside the 60 s allowance, at a mean of 11 to 12 s and at most 14 to 17 s, and a second controller then ran to the end. Every judged row of the receipt:

| Gauge | Reading | What it means for the system |
|---|---|---|
| failed requests in the 300 s after the kill | LOSS in all three of our runs, up 10.9% to 15.1% | more requests failed in the five minutes after the kill than in native's arm over the same window |
| time over the line in those 300 s | LOSS by the mean of our three runs, beyond the noise in none, up 1.7% to 4.3% | more of that window spent over the response line |
| pod start wait, total | LOSS in all three of our runs, up 125.6% to 164.2% | more time passed with pods started but not yet serving |
| pod start wait, mean | LOSS by the mean of our three runs, beyond the noise in none, up 14.6% to 16.2% | each pod took longer to start serving |
| response time, mean | GAIN in all three of our runs, down 36.9% to 42.2% | requests answered faster over the whole window |
| response time, 95th percentile | GAIN in all three of our runs, down 40.9% to 56.3% | the slow tail answered faster |
| response time, 99th percentile | the runs disagree (run A down 18.7%, run B down 6.6%, run C up 5.1%) | the test is unstable on the extreme tail |
| time over the response line | GAIN in all three of our runs, down 30.9% to 33.4% | less time over the line |
| alert minutes | GAIN in all three of our runs, down 18.3% to 20.0% | fewer minutes that would page a person |
| failed requests, whole window | GAIN by the mean of our three runs, beyond the noise in one, down 3.5% to 6.9% | fewer requests failed over the whole window |
| HPA replicas | power given in all three of our runs, up 20.7% to 22.0% | more pods held, the price of the faster answers |
| pods started | power given in all three of our runs, up 93.1% to 135.2% | more pods started, which the total start wait above counts |
| node-hours; energy (two declared models, class S inside the receipt) | STEADY, under the floor (means 0.13% and 0.41%) | the machines and the modelled energy held level |
| nodes in service; unschedulable pods; their pod-minutes | STEADY, the same | no machine added or removed, no pod left without a machine |

The four LOSS rows stand in the LOSS ledger with no cause yet written (`docs/LOSS_LEDGER.md`). The second robustness test, the long run, carries two LOSS rows of its own, both on the pod start wait (`docs/LOSS_LEDGER.md`; section 5.6).

### 3.10 The factory profile and the two restoring controls

The factory profile is one vector, θ = (the rules, the gains, the margins and cushions, Δ, the dial, every muscle's card, …). After release θ(k + 1) = θ(k) = θ[factory] while x, z and u keep changing (`docs/FACTORY_PROFILE.md`, sections 3 and 4). The released profile is omni-v25's. The best validated profile for the declared conditions is not yet established: the repository stands at steps 1 and 2 of the eight (`docs/FACTORY_PROFILE.md`, sections 1 and 5).

The control panel (`tools/omni_control.py`) offers two ways back:

| Control | Endpoint and role | Effect |
|---|---|---|
| Restore factory profile | POST /v1/factory, operator | autopilot, the max, every muscle driven, the command's own beat |
| Return to native | POST /v1/reset, operator, a reason required | every setting handed back; stopped until the next mode press |

Every change passes through native. The panel creates the controller's own kill file, waits up to 120 s (`--handback`) for the controller to exit, sends SIGTERM if it has not, and kills it after a further 30 s; the controller's SIGTERM handler restores every setting before exiting. The panel then removes the file and starts the controller with the new arguments, or leaves it stopped. A controller that exits on its own is not restarted, because a fresh start would snapshot settings not yet handed back; its lease hands them back instead (`tools/omni_control.py`, `_hand_back` and docstring).

Read from the code, the Kubernetes controller restores on its kill file and then stays running in observe mode (`omni_controller/controller.py`, `step`); it exits on SIGTERM (`main`). The panel's docstring says the controller exits on its kill file. On the code as written, every press reaches the SIGTERM branch after 120 s, and the panel records that hand-back with `handed_back` false, though the controller's handler restores before it exits.

### 3.11 The kill switch

The kill switch is a third way back, separate from both of those and from the lease. Its purpose is security: if anything gets into Omni-Compass's brain and tries to drive a system for its own ends, one switch in a person's hand turns Omni-Compass off at once (`omnicompass/master.py`, docstring).

Return to native belongs to an operator, for one controller. The lease belongs to the watchdog, for a dead or hung controller. The kill switch belongs to the security role on the panel, or to anyone with access to the machine's command line, and acts on every controller on that machine. The switch is a file (by default /tmp/omni-compass/OFF, set by `OMNI_MASTER_OFF`). Every controller sees it at its next decision and restores; `tools/omni_switch.py off` also signals each registered controller, which restores and exits. A switch that cannot be read counts as OFF, and while it is OFF `refuse_if_off` stops every start.

On the panel the kill (POST /v1/kill) needs the security role and a reason. Re-arming (POST /v1/arm) needs two different holders of the security role within ten minutes (`ARM_WINDOW_S` = 600 s); the first press is answered 202, and the same holder pressing twice counts once (`tests/test_omni_control.py`). Tokens are stored only as SHA-256 digests; a request without a valid token gets 401 and one whose holder lacks the role 403; binding beyond the loopback needs HTTPS. The command line and the file stay available, so a panel that is down never prevents an OFF.

**Receipts.** `tests/test_master_switch.py` runs the Kubernetes and card controllers as their own processes against stand-in devices and checks that one OFF hands both back and stops both, that neither starts while OFF, that a start works again after ON, and that the watchdog hands both back after both are killed outright while acting.

On a real card (class P; NVIDIA A100 SXM4 40 GB, Lambda run 40079645681, omni-v18 at commit e3b05dc; `docs/RUN_LEDGER.md`, `results/gpu/drill-20261024T091235Z/DRILL.md`) the drill passed 5 of 5 checks: killed outright, the watchdog handed the card back (limit 400 W, start 400 W); the switch pulled, the controller handed back and exited (`results/gpu/drill-20261024T091235Z/switch.txt`); while OFF, a start was refused; with the response-time feed stopped, the controller failed up; at the end the card stood at its own start limit of 400 W. On that card native already ran both levers at their top, and the controller wrote nothing in 3,050 decisions (`docs/EVIDENCE_LEDGER.md`); the switch audit records zero writes before the hand-back (`results/gpu/drill-20261024T091235Z/audit-switch.jsonl`, last line). The drill therefore shows the switch path working on real hardware, not the reversal of a setting the controller had moved. It predates omni-v25. The two-person arm has been exercised only in unit tests.

### 3.12 The audit of every write

Every write is audited before it runs: the `write` method of the `Kube` class appends a JSON line with the command, the reason and the dry-run flag, then executes the command (`omni_controller/controller.py`). A write the cluster refuses raises an error, which the decision's error line records with the command's standard error (`safe_step`). Each decision appends its authority record (calm, the grants, the gate's reason, blind senses, drift), its compass record, any verdict or immune event and the decision itself; at exit the controller records its own processor time. The panel logs every press, refused ones included, with time, holder, button, reason and outcome (`tools/omni_control.py`).

The card's audit shows the whole shape (`results/gpu/drill-20261024T091235Z/audit-switch.jsonl`, class P). Its first line is the snapshot of every lever, taken before any write; each decision line carries the telemetry, the position, the velocity and who decided; the last line sets the restored values beside the start values and records whether a foreign writer was seen. A reader checks the hand-back by comparing two columns, not by trusting a summary.

### 3.13 The C++ twin and the seal

The allocation law's step in `omnicompass/adapter.py` has a C++ twin, `cpp/src/governor.cpp`. A parity test records the Python's inputs over 60 scenarios of 72 steps from the modelled stack (`omnicompass/stack_sim.py`), with a fixed breach pattern of three decisions in every seven, and replays them through the C++ (`tests/test_cpp_governor_parity.py`). It covers five modes at a step every 60 s, the fleet mode at 15, 10 and 5 s and the power-protect mode at 15 s, and it asserts zero discrete mismatches and a largest absolute difference under 10⁻¹² in the power cap, the demand, the command and five state coordinates (E, U, I[U], S, B). The compass law and plug are held on 300 seeded laws (`tests/test_cpp_compass_law_parity.py`), the verdict on 300 seeded verdicts (`tests/test_cpp_verdict_parity.py`) and the immune rule on 40 seeded scripts of 80 to 200 decisions (`tests/test_cpp_immune_parity.py`).

The seal (`results/SEAL.json`, written 2026-10-25T17:07:20+00:00) records 17 twins, the core engine, the allocation laws, the compass law and plug, the verdict and the immune rule among them, each with the parity check that held it equal before its hashes were written. Of the Python files it records, the 16 that omni-v25's fingerprint also holds carry the same hash there (`OMNI_V25.json`); three (`fleet/harness.py`, `tools/engine_runs.py`, `tools/core_runs.py`) lie outside the fingerprint.

**What the seal establishes.** On each check's recorded and seeded inputs the two implementations compute the same decisions, and the sealed engine files are the fingerprinted ones.

**What it does not establish.** That any rule suits any plant or brings any GAIN, or anything about the live input and output. The seal lists what has no twin (`results/SEAL.json`, `python_only`): the Kubernetes controller (`omni_controller/controller.py`) and its muscles; the card's device input and output (reading `nvidia-smi`, writing power limits); the CPU and GPU power-budget harness (`hardware/node_exchange.py`); the max that is every organism's default brain (`realms/compass_arm_v5.py`); the organisms' harness; and the control plane of Omni-Compass's own orchestrator. The loop behind every class L receipt therefore has no twin, and is checked by tests and by its runs' receipts, not by a second implementation; the parity inputs are modelled traces, class S.

### 3.14 The formal status, stated exactly

`docs/FORMAL_STATUS.md` opens: "Not a global-stability proof of the forced six-state system." It holds:

- the isolated S-flow is the gradient of Φ;
- Theorem 1 (T), unsaturated: dU/dt = K[P]·(σ − U), and V = e²⁄2 has dV/dt = −K[P]·e² on that channel;
- Theorem 2 (T), saturated, with the U drift bounded by F̄ < U[auth]: V decreases wherever e ≠ 0; over the declared parameter box F̄ = 16.86 < 25, so it holds over the box in continuous time;
- Theorem 3 (T, constant computed), sampled-data RK4: eₖ₊₁ = 0.88·eₖ + dₖ; with ε[h] computed over the frozen fixtures (V), the ultimate bound 0.0315 lies inside the 0.10 basin;
- Theorem 4 (T continuous, V discrete): the admissible box is forward invariant.

It lists as open: ε[h] and discrete invariance over the whole box by interval arithmetic; the intertwining residual against a real plant, instrumented but not yet measured on a card; the mapping of Theorem 5.6 of the Closed Structure (`docs/CANONICAL_ENGINE.md`) onto (E, U, I[U], S, B); and a tracking bound for `printed_eight_line`.

The four theorems concern bounded channels of the engine's own state over the declared box. They do not reach the compass law on a plant, the verdict, the immune rule, the plug, the lease or the kill switch; those rest on tests and receipts. Nor does that page state how far they reach the Kubernetes controller that acts in the class L runs, or the interaction of the beat with the native loops (section 2.4); they predict none of the readings of chapter 5. `docs/TRACKING_THEOREM.md` records further computer-assisted claims (`docs/ENGINE_PROOFS.md`) that `docs/FORMAL_STATUS.md` still lists as open. This monograph follows `docs/FORMAL_STATUS.md`.

### 3.15 Threats to validity

**Internal.**

- Native's twin in the immune rule is a single-queue model running inside a live loop; it is not native measured.
- No omni-v25 live receipt reports an immune event as a row.
- The threefold damping is justified in the code only by consistency with the realm muscles; no record read for this monograph isolates its effect.
- The factory beats were picked on a modelled ladder (class S).
- The four LOSS rows of `results/live/V25_ROBUST_KILL.md` have no cause written. Two of them concern the hand-back window itself: after the kill, more requests failed in the Omni-Compass arm than in native's. A deployment that relies on the hand-back inherits that window.
- The panel's docstring and the controller's code differ on what the controller does at its kill file (section 3.10).
- The audit is appended by the process that writes, and no hash chain or signature binds its lines.

**Construct.**

- "Never past its own limit" is enforced on levers, not on the service. In the kill receipt the Omni-Compass arm still spent 16.23% to 19.6% of samples over the response line, against native's 24.35% to 28.35% (`results/live/V25_ROBUST_KILL.md`): GAIN in all three of our runs, down 30.9% to 33.4%, less time over the line, but not zero.
- On Kubernetes the redline is defined by the 95th percentile alone; another gauge could redline differently.
- The energy rows in the kill receipt are declared models, not meters.

**External.**

- The lease receipt is class L, from kind on GitHub's runners: not bare metal, not a cloud, not a bill.
- The card drill is class P but ran omni-v18 on a card whose levers the controller never moved.
- The two-person arm has no live receipt.
- The arms B and D on file ran omni-v23 and omni-v18 (`results/SITE_NUMBERS.json`), not omni-v25.

**Reproducibility.** `tools/seal.py` builds the C++ and runs every twin's parity check; with the switch tests (`tests/test_master_switch.py`, `tests/test_omni_control.py`) it runs from the repository with Python and a C++ compiler. Each live receipt names its GitHub runs and commits.

## 4. The Evidence: Classes, Arms, the Three-Run Key and How Every Reading Is Judged

This chapter sets out what the record counts as evidence, how a measured difference becomes one of the record's words, and how the aggregates are composed. How a reader checks each step from the repository is set out in sections 6.8 to 6.12.

Two conventions hold throughout. The three runs of a benchmark are run A, run B and run C; the four arms of the two bills are arm A, arm B, arm C and arm D. Where both appear together the runs are numbered 1, 2 and 3, as `results/TWO_BILLS.md` numbers them, "so the run letters never meet the arm letters". Every three-run table carries the sentence `tools/readings.py` writes: "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."

### 4.1 Evidence classes, and why class S is never proof

The three classes L, P and S are defined in section 1.6. The same repository page names two further classes, T (a theorem) and V (verified in code), and adds: "Only **P** speaks for hardware energy." (`docs/HOW_TO_READ_THE_RESULTS.md`). Class T reaches only as far as `docs/FORMAL_STATUS.md` takes it (section 3.14).

A class belongs to a gauge, not to a table. In a class L table on kind the energy row is "a declared model, not a meter: kind keeps every machine powered" (`docs/HOW_TO_READ_THE_RESULTS.md`); on the data stores it is the host's processor seconds (`results/OMNI_INDEX.md`). The Omni index therefore scores both as native's (section 4.7). In the A10 table with the seven organisms around the card, the organisms' rows are class S and the card's rows class P (`results/gpu/V23_A10_STACKS_FULL_ABC.md`).

**Why class S is never proof.** The record gives three reasons.

1. *The plant and the controller come from the same hand.* A model shows only what its plant allows. The live engine manual says of the page's own model that "the model's plant refuses nothing, so every cut is the muscle's own range, never a refused write" (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`), and `docs/OMNI_V23.md` says of the model gate: "No model refuses a write of the cluster". The real cluster did refuse. On kind, from omni-v19 to omni-v22, the rig's own identity refused the pod writes of the arm that ran by itself: "Fifteen of fifteen decisions a window ended Forbidden, in every repetition" (`docs/OMNI_V23.md`). The live runs' files exposed a fault the models could not show.
2. *A model's figure can hide its cost.* `results/SITE_NUMBERS.md` keeps a modelled response-time figure for Omni-Compass alone off the site, because "the same column used 40.8% more machine-hours and 25.9% more energy".
3. *A composition is a model.* The whole-system composition is "a modelled composition (**class S**) of class P and class L measurements". It assumes separability, and no run stacked the layers (`results/WHOLE_SYSTEM.md`, section 1; section 5.10).

Class S has its place: every engine change goes through the model gate before any real run (`docs/CHANGE_CONTROL.md`; `results/model_gate/`). Among the standing rows of Omni-Compass against its native, class L reads 384 GAIN, 169 power given, 409 STEADY, 273 LOSS and 185 the runs disagree. Class S, which in that audit means the outside simulators our own runner drives, reads 97 GAIN, 10 power given, 161 STEADY, 30 the runs differ and no LOSS (`results/verdict_audit/VERDICT_AUDIT.md`). Every one of the 273 LOSS rows is class L. The audit holds no class P table (section 4.6).

### 4.2 The four arms, the two bills and the one equation

The four arms are the design of 1 November. Each is read by its bill, by the work done inside it, and by the two together (`results/TWO_BILLS.md`; `results/SITE_NUMBERS.json`, `four_arms`):

| Arm | What it is | Place and bill | Class | Engine | Receipt |
|---|---|---|---|---|---|
| A | the chip native | one A10 card rented directly; its bill the rental | P | omni-v23 | `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| B | the chip with Omni-Compass on native | the same card, the same rented window | P | omni-v23 | the same |
| C | the cloud native | Azure (AKS), its own bill at list price | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| D | the cloud with Omni-Compass on native | the same machines, paired with C | L | omni-v18 | the same |

In arms B and D native's controller stays in place, with the supervisory layer above it (section 1.1).

**The one equation** (`results/TWO_BILLS.md`, `docs/WORK_PER_BILL.md`). For a place p and an arm a, under the same offered load over the same window:

```
W(p, a)                                the work done (requests served; jobs finished)
B(p, a) = Σₖ c(p, a, k)                the bill: every cost line k inside the place's boundary
E(p, a) = W(p, a) / B(p, a)            the work for each dollar
G(p)    = E(p, Omni-Compass) / E(p, native) − 1 = (1 + ΔW) / (1 + ΔB) − 1
ln(1 + G) = ln(1 + ΔW) − ln(1 + ΔB)
G(chip) = E(B) / E(A) − 1              G(cloud) = E(D) / E(C) − 1
```

Here ΔW and ΔB are the changes in the work and the bill. On the chip the hour's price is fixed and both arms rent the same window, so ΔB ≈ 0 and G ≈ ΔW: any benefit is work done in time already paid for. Through the cloud both sides move: Omni-Compass moves the machine-hours kept in service, a bill that rises is power given, and the place gains only where the work rises more than the bill (`results/TWO_BILLS.md`). Places are never added or set against each other. Inside one place both arms pay the same prices, so "the price level cancels in G(p)" (`docs/WORK_PER_BILL.md`). A line item not metered stays "written as not metered, never filled with a guessed price" (`results/TWO_BILLS.md`).

**What the equation reads today** (`results/TWO_BILLS.md`):

| Place | Run | Work, ΔW | Bill, ΔB | G, the work for the bill |
|---|---|---|---|---|
| the chip, arm B against arm A | 1 | GAIN, up 1.51% | STEADY, up 0.04% | GAIN, up 1.46% |
| the chip, arm B against arm A | 2 | GAIN, up 0.73% | STEADY, unchanged (0.00%) | GAIN, up 0.73% |
| the chip, arm B against arm A | 3 | LOSS, down 0.70% | STEADY, down 0.01% | LOSS, down 0.69% |
| the chip, three runs | | **the runs disagree** | STEADY, under the floor (the three runs' mean 0.01%) | **the runs disagree** |
| the cloud, arm D against arm C | one set of 97 paired repetitions | not counted | power given, up 1.21%, inside the noise | not read |

On the chip, the work for the bill has not yet been shown to rise. Runs 1 and 2 served more requests in the same rented window and run 3 fewer, each by 0.5% or more, so the key reads the runs disagree (section 4.4). The cloud set sent a fixed rate of requests and counted no work, so G(cloud) is not read (`results/SITE_NUMBERS.md`). Sections 5.8 and 5.9 read every other gauge of the two places.

### 4.3 Paired repetitions and the three runs

**The repetition is the unit.** Every arm runs back to back on the same runner, each on a fresh kind cluster, "in an order rotated by repetition so no arm always runs first or last". The same script gives the reason: "separate runners differ by about 15% in p95 on their own" (`scripts/kind_paired.sh`). The four ways rotate all four arms the same way (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6).

**The interval of one run.** A run of n paired differences reports

```
d̄ ± t₀.₉₇₅,ₙ₋₁ · s / √n
```

where s is the standard deviation of the n differences and t₀.₉₇₅,ₙ₋₁ the exact Student point on n − 1 degrees of freedom (`omnicompass/student_t.py`): 4.303 at 3 pairs, 2.262 at 10, 2.093 at 20 (`docs/HOW_TO_READ_THE_RESULTS.md`). A run is *beyond the noise* when its whole interval lies on one side of zero.

**Pairs a run, on file.**

- Ten on kind (`results/live/V25_FAIRNESS.json`).
- Three on the data stores (`results/OMNI_INDEX.md`).
- Five on the A10 at full load (`results/gpu/V23_A10_CAP_FULL_ABC.md`).
- 97 in the one Azure run (`results/live/AKS_STEADY_100_OMNI_V18.md`).

**The three runs.** Every benchmark runs three times, A, B and C (`tools/confirm_abc.py`), on one engine but not necessarily at one commit. The fairness runs ran at commits 63fc4dc666d3, db6e040b4584 and 0a92e09fe669, each recorded as "omni-v25 (digest cf56fc0a7b707452, 65 files)" (`results/live/V25_FAIRNESS.json`; `OMNI_V25.json`). The engine is identified by its fingerprint (`tools/omni_version.py`), and "a table never mixes engines" (`docs/HOW_TO_READ_THE_RESULTS.md`). A run's interval measures the noise inside one job; the three runs ask whether a change recurs on other machines at other times. "Each run's own number wears that run's own word by the same floor" (`docs/HOW_TO_READ_THE_RESULTS.md`); the three-run column carries the word of the three runs' mean.

### 4.4 The one key

The one key is `tools/readings.py`, `three_run_reading`, "the only place a word is decided" (`tools/verdict_audit.py`). For a gauge with declared aim a and runs i = 1, 2, 3 (native's mean nᵢ, mean paired change dᵢ, interval Iᵢ), with δᵢ and δ̄ as in (1.1):

```
δᵢ = dᵢ / |nᵢ|        δ̄ = (δ₁ + δ₂ + δ₃) / 3        f = 0.005   (SIZE_FLOOR)
M = { sgn(δᵢ) : |δᵢ| ≥ f }                           the signs of the runs that moved at least the floor
```

The key applies five steps in order:

1. A run with no value gives *no value*; a gauge declared shown reads *shown, not judged*. A count that must never rise reads "LOSS in at least one of our runs" on any rise in any run, and "GAIN or STEADY in all three of our runs" where it rose in none and fell in some.
2. If every run's two values agree to 10⁻⁹ of the value, the reading is **STEADY, the same**.
3. If M holds both signs, the reading is **the runs disagree**.
4. If |δ̄| < f, the reading is **STEADY, under the floor**, with |δ̄| printed.
5. Otherwise the word is w(δ̄ < 0, a), from the table below. If every Iᵢ excludes zero and all runs share one sign, the reading is "w **in all three of our runs**". If not, it is "w **by the mean of our three runs**, beyond the noise in k of 3", where k counts the runs whose interval excludes zero.

A gauge whose native stands at zero in a run is read by the signs alone, with no floor: any change is a change.

| What the gauge is for | It fell | It rose | Examples |
|---|---|---|---|
| work done | LOSS | GAIN | requests inside the response line, requests served |
| time waited, missed or failed | GAIN | LOSS | response time, failed requests, pod start wait |
| a resource spent or held | GAIN (a cut) | power given | machines, energy, memory, replicas, the bill |
| work per resource | power given | GAIN | work per energy |
| a count that must never rise | GAIN or STEADY, if no run rose | LOSS on any rise in any run | lost messages |

Five properties of the key shape how the record reads:

- **The sign never decides.** A fall can read GAIN or LOSS, and a rise GAIN, LOSS or power given, by what the gauge is for.
- **Disagreement is tested before the floor.** A mean under 0.5% built from opposite moves of 0.5% or more reads *the runs disagree*, never STEADY. A run under the floor does not count as a mover, so its sign cannot create a disagreement.
- **"In all three" turns on sign and interval, not on each run's own floor.** On the A10 at full load the card's energy fell 0.31%, 0.63% and 1.48%, every interval clear of zero. Run 1's own word is STEADY, because its change is under the floor. The three-run reading is still GAIN in all three of our runs: all three fell, every interval excluded zero, and the mean clears the floor (`results/TWO_BILLS.json`, `chip`; `results/TWO_BILLS.md`).
- **Strength sits beside the word and never changes it.** Strong: every run on the mean's side and beyond its noise. Moderate: all but one. Weak: one. Inconclusive: none (`results/verdict_audit/VERDICT_AUDIT.md`). A row that reads the runs disagree has the strength "unresolved" (`results/verdict_audit/VERDICT_AUDIT.json`).
- **Only "in all three" carries a bound.** Under no true difference and independent runs, it is false with probability 2 × 0.025³ ≈ 3.1 × 10⁻⁵; "A word read **by the mean of our three runs** carries no such bound" (`docs/HOW_TO_READ_THE_RESULTS.md`).

**Power given**: "a resource spent or held rose: shown beside what it bought, never a LOSS" (`tools/readings.py`). It is never hidden, and it is judged by the work and waiting rows beside it. The word once used for STEADY is retired. It survives only as a code alias of STEADY, kept for fingerprint-locked engine files, and any older record that carries it is read as STEADY (`tools/readings.py`). A further word, *the runs differ*, marks a deterministic simulator whose runs did not reproduce (`tools/readings.py`).

### 4.5 A worked example: four readings where the sign and the word differ

The fairness test puts a noisy neighbour on the same workers (`results/live/V25_FAIRNESS.md`; omni-v25, three runs of ten pairs). The raw change is (Omni-Compass − native) / native, printed apart from the word as `docs/HOW_TO_READ_THE_RESULTS.md` prescribes, and given here in words, up or down; it is a measurement, not a reading. Means, strengths and intervals come from `results/verdict_audit/VERDICT_AUDIT.json`.

| Gauge (what it is for) | Raw change, runs A / B / C | Raw mean of three | Reading | Strength |
|---|---|---|---|---|
| pod autoscaler's replicas, mean (a resource held) | up 4.93% / up 5.14% / up 6.03% | up 5.37% | **power given in all three of our runs** | strong |
| failed requests (failed: a fall is the aim) | down 16.43% / down 25.30% / down 24.54% | down 22.09% | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | inconclusive |
| response time, mean (waited: a fall is the aim) | down 6.73% / down 0.87% / up 0.94% | down 2.22% | **the runs disagree** | unresolved |
| response time, 95th percentile (waited: a fall is the aim) | down 0.45% / up 16.53% / up 6.64% | up 7.57% | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | inconclusive |

1. **The replicas: a rise that is not a LOSS.** Replicas are a resource held, so the key reads power given. The autoscaler's mean count rose from 14.80, 15.02 and 15.08 to 15.53, 15.79 and 15.99, every interval clear of zero on the same side: more pods were kept serving. The machines in service were the same in both arms (STEADY, the same), and node-hours read STEADY, under the floor (the three runs' mean 0.07%), so no machine was added for them (`results/live/V25_FAIRNESS.json`).
2. **Failed requests: a fall that is a GAIN, held loosely.** The aim is fewer failures, so the fall reads GAIN: fewer of the offered requests failed. Native failed about 2.9% to 3.4% of requests, and the mean fell 22.1%, far past the floor. No run's own interval excluded zero, so the strength is inconclusive. The interval of the three runs' mean, from down 34.3% to down 9.9%, does exclude zero (`results/verdict_audit/VERDICT_AUDIT.json`, `mean_ci95_pct`). The word stands, and its strength is printed beside it.
3. **The mean response time: a fall that is not a GAIN.** A reader going by the mean's sign would print GAIN, 2.2%. The key prints the runs disagree, because run A fell 6.7% and run B 0.9%, both past the floor, while run C rose 0.9%, also past the floor. The audit names the cause: "opposite directions inside overlapping noise". The row is looked into, not averaged into a word.
4. **The 95th percentile: the floor at work.** Run A fell 0.45%, under the floor, so it is not a mover and cannot make the runs disagree. The reading is LOSS by the mean of our three runs, up 7.6%: the slowest twentieth of requests waited longer with Omni-Compass on top. This named LOSS is why the Omni index reads the fairness test LOSS 2.3% (section 5.4).

Beside the extra replicas, then, the record shows fewer failures and a slower tail. It does not attribute either to the replicas. Recomputing the four rows with the key from their stored values reproduces each stored word, and the audit finds no stored reading the key reads otherwise (`results/verdict_audit/VERDICT_AUDIT.md`).

### 4.6 The verdict audit and its four comparisons

Each product Omni-Compass sits on (Kueue, Volcano, the KAI scheduler, Koordinator, Armada, Karmada and the rest) runs four ways (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6):

- *nativebare*: the organism alone, with the default scheduler;
- *native*: the product as shipped;
- *compassbare*: Omni-Compass on the organism alone, the default scheduler still placing every pod;
- *compass*: Omni-Compass on top of the product.

The verdict audit files each table under one of four comparisons (`tools/verdict_audit.py`):

| Comparison | Table suffix | First arm against second | Omni-Compass against its native? |
|---|---|---|---|
| against its native | every plain table; TOP; BARE | compass vs native; compassbare vs nativebare | yes: *do no harm* is judged here |
| in place of a controller | VS (and the SOLO tables) | compassbare vs native | no: shown |
| the orchestrator's own | ORCH | native vs nativebare | no: Omni-Compass in neither arm |
| two changes at once | BOTH | compass vs nativebare | no: shown |

Only the first comparison keeps native's controller in place and changes one thing, so only it measures what a supervisory layer adds. VS tests a role Omni-Compass does not play, ORCH measures the product alone, and BOTH changes two things at once. Pooling them would credit or charge Omni-Compass with the product's own effect.

**Standing counts** (`results/verdict_audit/VERDICT_AUDIT.md`):

| Comparison | GAIN | power given | STEADY | LOSS | the runs disagree | shown |
|---|---:|---:|---:|---:|---:|---:|
| against its native | 481 | 179 | 570 | 273 | 185 | 637 |
| in place of a controller | 108 | 29 | 69 | 76 | 17 | 137 |
| the orchestrator's own | 31 | 11 | 85 | 76 | 32 | 99 |
| two changes at once | 61 | 25 | 45 | 95 | 9 | 99 |

The first row also carries 30 *the runs differ* and 201 *tuning* (a tuning workload, shown and never counted, `results/OMNI_INDEX.md`).

**What the audit does.** `tools/verdict_audit.py` recomputes every judged row from its stored values with the one key. It read 338 three-run tables (98 standing, 178 superseded, 60 the road, 2 taken out) and recomputed 10,560 of their 14,574 rows. It found 0 stored readings the key reads otherwise and 0 Markdown readings unlike their JSON twin. With `--check` it exits 1 when the record is stale or a stored reading differs from the key's (tests: `tests/test_verdict_audit.py`, `tests/test_readings.py`). In the standing tables its discrepancy report counts 997 rows whose printed change had carried the word's sign and now carries its true sign, and 807 rows changed only by the rename to STEADY; no raw measurement changed (`results/verdict_audit/DISCREPANCIES.md`).

**What the audit does not read.** It selects the three-run tables in `results/live/` and `results/orchestrator/` (`tools/verdict_audit.py`). The card's tables in `results/gpu/` lie outside that selection, and so outside the 273 LOSS rows and the ledger built from the same count. The A10 fully loaded inside the organisms carries 7 LOSS rows of its own on the card's meter (`docs/THE_RECEIPTS.md`); section 4.8, item 1, reads them. Where the 273 rows sit, by product, gauge, strength and engine, and what is written of their causes, is set out in section 5.11.

### 4.7 The Omni index and how it is composed

`tools/omni_index.py` turns each measure of test t into a ratio r oriented so that a value above 1 is a GAIN, from Omni-Compass's value o and native's n in each run (`results/OMNI_INDEX.md`):

```
work                                   r[W] = o / n
speed (the 95th percentile)            r[S] = n / o
machines (or the resource held)        r[M] = n / o
energy                                 r[E] = n / o
```

**Admission.** A measure enters as the geometric mean of its three runs' ratios when its reading is judged, whether in all three of our runs or by the mean of our three runs (`tools/omni_index.py`, which calls `judged` in `tools/readings.py`); STEADY and the runs disagree enter as exactly 1:

  ρ[t, m] = (r[A] · r[B] · r[C])^(1/3) when the reading is judged, else 1.  (4.1)

Energy is scored only where a meter read it. Elsewhere (a declared model on kind, the host's processor seconds on the stores) it enters as native's and is shown beside, never dropped, "because a geometric mean of fewer measures would weigh the rest more" (`results/OMNI_INDEX.md`).

**Composition.** With k[t] the measures taken in test t and n[c] the tests in category c,

  I[t] = (∏ₘ ρ[t, m])^(1/k[t]),  I[c] = (∏ over t ∈ c of I[t])^(1/n[c]),  I = (∏ over the six real categories of I[c])^(1/6),  (4.2)

and the headline is I − 1, each real category weighted the same. For a data store the "machines" column is the resource it holds: connections open to the database (PostgreSQL), consumers running (Kafka), the cache's memory ceiling (Redis), the storage engine's cache size (MongoDB) and the buffer pool's size (MySQL). A combined number below 1 reads LOSS only when its service reading (work and speed alone) is also below 1; otherwise it reads power given (`tools/omni_index.py`, `index_word`).

As a check, with the six category values of section 5.3 (Kubernetes 1.205, PostgreSQL 0.986, Kafka 3.186, Redis 0.932, MongoDB 0.952, MySQL 0.905), (1.205 × 0.986 × 3.186 × 0.932 × 0.952 × 0.905)^(1/6) ≈ 1.204: the headline, GAIN 20.4% (`results/OMNI_INDEX.md`; `results/OMNI_INDEX.json`, `headline_pct`). Section 5.2 reads it and names the second readings beside it.

The index page names its own lean. Kafka's speed ratio is a hundredfold because "native's queue grew at nine tenths of its capacity by design", "so the service reading leans on it" (`results/OMNI_INDEX.md`).

### 4.8 Threats to validity

1. **The mean's word has no error bound, and the record holds a null case.** On the A10 fully loaded inside the organisms, Omni-Compass's own audit recorded no write on the card in any of the 62 arms of each run, "so on the card the two arms were one system" (`results/gpu/V23_A10_STACKS_FULL_ABC.md`). Its card rows still read 1 GAIN, 6 power given and 7 LOSS beside 84 STEADY (`docs/THE_RECEIPTS.md`). Each of those words is "by the mean of our three runs, beyond the noise in 0 of 3", none "in all three", and the record puts them down to "the order of the arms and the card's own drift, not the engine". A mean's word at 0 of 3 can appear with no effect present.
2. **The audit's reach.** The verdict audit, its 273 LOSS rows and the LOSS ledger's 520 cover `results/live/` and `results/orchestrator/` only (`tools/verdict_audit.py`). The card's LOSS rows in `results/gpu/` are counted on their own pages (`docs/THE_RECEIPTS.md`), not in those totals.
3. **Independence.** The 3.1 × 10⁻⁵ bound assumes independent runs, and "runs on the same kind of machine can share a bias, which three runs cannot remove" (`docs/HOW_TO_READ_THE_RESULTS.md`).
4. **Power.** At 3 pairs a run, t = 4.303 and the interval is wide. Many differences too small for a run's pairs to resolve read by the mean of our three runs, or STEADY (`docs/HOW_TO_READ_THE_RESULTS.md`).
5. **The floor is a convention.** The 0.5% floor (`tools/readings.py`, `SIZE_FLOOR`, set on 20 and 24 October) is one constant for every gauge, not derived from any gauge's noise. A finely measured 0.4% change reads STEADY, and a noisy 0.6% change reads a word.
6. **Scope of class L.** GitHub's runners in kind are not bare metal, not a cloud and not a production system. Energy on kind is a declared model, not a meter.
7. **Engines and places.** Arms A and B ran on omni-v23. Arms C and D ran on omni-v18, under a cloud rule since struck, in one run with no work counted. Neither pair ran on the engine that stands, and five standing tables are not yet run again on omni-v25 (`results/verdict_audit/VERDICT_AUDIT.md`).
8. **One quantity, two aims.** `tools/two_bills.py` reads work per dollar as work done, so a fall reads LOSS (chip run 3). `tools/hil_abc.py` reads it as work per resource, so a fall reads power given (the organisms' card cells in `results/TWO_BILLS.md`). The same fall gets a different word in each table.
9. **The index's construction.** It weights its categories equally, Kafka (GAIN, up 218.6%) carries much of its size, and Kafka's native sat at nine tenths of its capacity by design (`results/OMNI_INDEX.md`); no record prints the index without it. The page's body sentence admits only "GAIN, LOSS or power given in all three of our runs", while the code also admits readings by the mean (`tools/omni_index.py`, `judged` in `tools/readings.py`). The fairness test, LOSS 2.3%, enters on such a reading, with no run beyond its noise (`results/OMNI_INDEX.json`). The number follows the code.
10. **The composition.** The whole-system composition is class S and assumes separability. Its layers are read from tables on several engines: omni-v25 for most of the cluster and its services, omni-v12 for Koordinator inside the cluster layer, and older engines for the card and the cloud, which enter as exactly 1 (`results/WHOLE_SYSTEM.md`, section 2). Its page, like the index's, says the headline counts only what held in all three of our runs, while `tools/whole_system.py` also admits readings by the mean (`judged`).
11. **Self-scoring.** The runs, the rules and the scoring are the company's own. The preregistrations sit in its own repository and were filed with no outside body (`tools/readings.py`). The verification receipt on file comes from quick mode, and Sigstore covers only runs archived from 31 October (section 6.8).

## 5. What the Receipts Show on omni-v25: What Omni-Compass Does, What It Gives, What It Does Not Do

This chapter reads the records and nothing else. It asks three questions of each place where Omni-Compass was measured: what it did against the native controller it sits on, what resources it put in to do so, and what it did not do or cannot yet show. Every number is printed in a cited file of the repository, or is a count of rows that this chapter makes from a cited file and says so. Where a file is silent the chapter says so; those silences close section 5.13. The readings of the products Omni-Compass sits on in the batch and multi-cluster rigs are in section 6.5, and the robustness test's hand-back in section 3.9.

### 5.1 The engines, the places and the key

The software end's receipts ran on omni-v25, the chip's on omni-v23 and the cloud's on omni-v18; the whole-system composition draws on tables from several engines. No table is pooled across engines (`results/OMNI_INDEX.md`, `results/TWO_BILLS.md`). Every benchmark pairs two arms on the same machines under the same load: native, and Omni-Compass on top of native. The places, their arms, classes and receipts are those of the table in section 1.8 and the arms table in section 4.2; every word is the key's (section 4.4), and its evidence strength is printed beside it where the verdict audit gives one. The arithmetic can be re-derived from the raw receipts (sections 6.8 and 6.12); the experiment is not independent.

### 5.2 The headline: the Omni index

The Omni index, composed as section 4.7 sets out, on omni-v25 reads **GAIN, up 20.4%** (`results/OMNI_INDEX.md`, `results/SITE_NUMBERS.md`): more work inside the response line and a shorter 95th percentile, with the resources it took scored beside them and energy held at native's. The place is real software on GitHub's machines, class L: not bare metal, not a cloud, not a bill (`results/SITE_NUMBERS.md`).

Every other aggregate is a named second reading (`results/OMNI_INDEX.md`):

- on work and speed alone, the same runs read GAIN, up 94.0%; Kafka's hundredfold speed ratio weighs on it (section 5.3);
- by the reading declared on 4 October, with the modelled energy scored, GAIN, up 20.9%;
- the whole-system composition, GAIN, up 41.9%, class S, its headline row composed from class L tables (`results/WHOLE_SYSTEM.md`, section 3; section 5.10).

The cloud and card categories are pending and enter nothing: the index page lists the omni-v25 Azure sets as still to run and the card's rerun on its current controller as still to land.

### 5.3 By product: the six categories

Each size below is the index's ratio less one, oriented toward the aim (`results/OMNI_INDEX.md`): work is Omni-Compass's over native's; speed and the resource held are native's over Omni-Compass's.

| Product | Tests | Index | Service reading | Work | Speed (native's p95 against Omni-Compass's) | Resource held (native's against Omni-Compass's) | What it means for the system |
|---|---:|---|---|---|---|---|---|
| Kubernetes | 9 | GAIN, up 20.5% | GAIN, up 61.8% | GAIN, 19.8% more | GAIN, native's 74.6% longer | GAIN, a cut: native's machine-hours 2.0% above | shorter waits at the tail; the machine cut comes from the batch test alone (section 5.4) |
| PostgreSQL behind PgBouncer | 3 | power given, the index down 1.4% | GAIN, up 0.7% | STEADY | GAIN, native's 1.4% longer | power given: native's connections 6.7% below | more pool connections held, for a service gain just above the 0.5% floor; the speed rose in one of three workloads (`tpcb_hot`, faster by 4.3%) |
| Apache Kafka | 3 | GAIN, up 218.6% | GAIN, up 1,515.1% | GAIN, 19.0% more | GAIN, native's 21,811.3% longer | power given: native's consumers 60.5% below | more consumers drain a queue that grows under native, which ran at nine tenths of its measured capacity by the test's design |
| Redis | 3 | power given, the index down 6.8% | GAIN, up 86.2% | GAIN, 21.8% more | GAIN, native's 184.8% longer | power given: native's memory ceiling 78.3% below | memory spent to buy work and speed; in two of three workloads (`burst`, `small`) the memory ratio outweighs them on the index's equal weights |
| MongoDB under YCSB | 4 | power given, the index down 4.8% | STEADY | STEADY | STEADY | power given: native's cache 17.8% below | a larger cache held with no service change counted: work STEADY in every workload; the speed reads the runs disagree in three of four workloads, entered as 1 |
| MySQL under sysbench | 4 | power given, the index down 9.5% | GAIN, up 8.7% | GAIN, 8.5% more | GAIN, native's 8.9% longer | power given: native's buffer pool 43.1% below | the buffer pool grew more than the service it bought, on the index's weights |

Every cell: `results/OMNI_INDEX.md`. The energy column of that page (shown, not scored where no meter read it) is not repeated here.

**Why four categories read power given.** By default the engine drives each muscle up to its own limit and never past it (the max, section 3.5), and a resource spent that rose is power given, shown beside what it bought and never called a loss (`DISCLOSURES.md`, section 3). The index counts that resource below 1. In PgBouncer, Redis, MongoDB and MySQL no work or speed measure the index scores reads LOSS; a pool, a memory ceiling, a cache or a buffer pool grew, and on the index's equal weights its ratio outweighs what it bought. In MongoDB no benefit is shown for the memory.

**Two cautions from the page itself.** Kafka's very large speed ratio comes from a native run at nine tenths of its measured capacity by design, and the service reading leans on it (section 4.7). The energy column is a declared model on kind and the host's processor seconds on the stores, never a meter, and is scored as native's (`results/OMNI_INDEX.md`).

### 5.4 Real Kubernetes: nine tests, one reads LOSS on the index

| Test (omni-v25, ten pairs, three runs) | Index | Speed (native's p95 against Omni-Compass's) | Machines | Energy (declared model, shown, not scored) |
|---|---|---|---|---|
| Steady load, the same fixed-rate work | GAIN, up 30.8% | GAIN, native's 192.3% longer | STEADY, the same | STEADY, the same |
| Demand that wanders one step at a time | GAIN, up 23.4% | GAIN, native's 88.0% longer | STEADY, the same | STEADY, the same |
| All four in one run (work GAIN, 43.5% more) | GAIN, up 29.1% | GAIN, native's 93.7% longer | STEADY, the same | STEADY, the same |
| Fairness: a noisy neighbour | **LOSS, down 2.3%** | LOSS, native's 6.8% shorter | STEADY, the same | STEADY, the same |
| Faults: machine down, spike, runaway pod, blind probe | GAIN, up 25.2% | GAIN, native's 96.2% longer | STEADY, the same | STEADY, the same |
| A queue of jobs (the batch test) | GAIN, up 9.0% | GAIN, native's 8.8% longer | GAIN, a cut: native's machine-hours 19.1% above | GAIN, a cut: native's 12.5% above |
| The Google cluster trace of 2011 | GAIN, up 35.3% | GAIN, native's 147.6% longer | STEADY, the same | STEADY, the same |
| KEDA on the CPU target and requests in flight | GAIN, up 16.0% | GAIN, native's 56.2% longer | STEADY, the same | power given: native's 1.4% below |
| KEDA's HTTP add-on | GAIN, up 22.5% | GAIN, native's 84.0% longer | STEADY, the same | power given: native's 2.0% below |

Source: `results/OMNI_INDEX.md`. Together: **GAIN, up 20.5%** (`results/SITE_NUMBERS.md`). In eight of the nine tests the 95th percentile was shorter: users at the tail waited less. Only the batch test moved the machines: its jobs ran on fewer machine-hours, a cut, though its queue finished later (section 5.5). Work is counted in two tests only. The steady test sends the same fixed-rate work to both arms by design (STEADY); the all-four test reads GAIN, 43.5% more work inside the line. The category's 19.8% is the geometric mean of the two.

**The fairness LOSS** (`results/live/V25_FAIRNESS.md`; the worked example of section 4.5). A noisy neighbour shares the workers. The index reads **LOSS, down 2.3%**, and the service reading LOSS, down 6.8% (`results/OMNI_INDEX.md`), from one measure: the first application's 95th percentile, LOSS by the mean of our three runs with no run beyond its noise (0.5% shorter in run A; 16.5% and 6.6% longer in runs B and C). The second application's 95th percentile reads LOSS by the mean, one run beyond its noise (13.4%, 8.0% and 3.6% longer). Against these, failed requests (down 16.4%, 25.3%, 24.5%) and alert minutes (down 8.0%, 2.4%, 4.4%) read GAIN by the mean, no run beyond its noise: fewer requests failed and fewer minutes went over the line. The second application's 99th percentile reads GAIN by the mean, no run beyond its noise. The first application's mean, its 99th percentile and its time over the line read the runs disagree. The pod autoscaler's replicas rose, power given in all three of our runs (up 4.9%, 5.1%, 6.0%), and Omni-Compass's own processor read 0.05539 to 0.0564 of a core. More replicas went in and the 95th percentile did not shorten: on shared workers users at the tail waited longer by the mean, though fewer requests failed. The ledger writes no cause (`docs/LOSS_LEDGER.md`).

### 5.5 The LOSS rows inside the index's own tables

The index reads fourteen omni-v25 tables (`results/OMNI_INDEX.md`). The LOSS ledger lists 21 rows from them under "Against my own native" (`docs/LOSS_LEDGER.md`); that count is this monograph's, made from the ledger's rows, and every row is in the table below. Strengths and the runs' directions are the verdict audit's (`results/verdict_audit/VERDICT_AUDIT.md`).

| Table | Gauge | Omni-Compass against native, runs A, B, C | Strength |
|---|---|---|---|
| All four | failed requests | more by 5.3%, 1.3%, 1.7% | inconclusive |
| All four | pod start wait, total | longer by 116.7%, 97.3%, 94.4% | strong |
| Batch | time over the line | more by 0.4%, 2.3%; less by 0.4% | inconclusive |
| Batch | failed requests | none in either arm; 0 to 0.01093%; none in either arm | inconclusive |
| Batch | alert minutes | more by 0.9%; the same; more by 3.7% | weak |
| Batch | queue finished | later by 2.6%, 2.7%, 2.9% | strong |
| Fairness | p95 | shorter by 0.5%; longer by 16.5%, 6.6% | inconclusive |
| Fairness | pod start wait, total | longer by 9.1%, 24.4%, 31.3% | inconclusive |
| Fairness | pod start wait, mean | longer by 1.4%, 20.7%, 25.7% | weak |
| Fairness | second app, p95 | longer by 13.4%, 8.0%, 3.6% | weak |
| Fairness | second app, time over the line | more by 3.0%, 0.1%, 0.9% | inconclusive |
| Faults | pod start wait, total | longer by 100.0%, 97.6%, 113.3% | weak |
| KEDA, CPU and requests | pod start wait, total | longer by 63.5%, 84.8%, 47.3% | strong |
| KEDA, HTTP | pod start wait, mean | longer by 20.7%, 7.4%, 20.5% | weak |
| pgbench `simple_update` | median | longer by 1.8%, 0.5%, 0.1% | inconclusive |
| Google 2011 trace | pod start wait, total | longer by 138.7%, 2,381.2%, 211.4% | moderate |
| Google 2011 trace | pod start wait, mean | longer by 11.0%, 576.3%, 24.9% | weak |
| Wandering | failed requests | more by 0.2%, 4.4%, 3.8% | inconclusive |
| Wandering | pod start wait, total | longer by 176.1%, 130.1%, 73.9% | strong |
| YCSB `burst` | 99th percentile | longer by 0.9%, 1.7%; shorter by 0.5% | inconclusive |
| YCSB `burst` | mean | longer by 1.6%, 1.9%; shorter by 0.3% | inconclusive |

Where native's value is near zero the ledger prints a run's values instead of its change: the Google trace's run B, 9.6 s to 238.2 s; the batch test's failed requests, 0 to 0.01093% in run B (`docs/LOSS_LEDGER.md`).

**What they mean for the system.** Nine rows are the pod start wait: new copies of a service took longer, in total or on average, to become ready, so added capacity arrived later. Six are rises in failed requests, in time over the line or in alert minutes: more requests lost or more minutes spent over the line. Five are slower responses at a percentile, the median or the mean. One is a batch queue that finished later.

**The pod start wait.** The total is summed over the pods started. In the six tests whose total reads LOSS, pods started read power given in all three of our runs in five (all four, wandering, faults, the Google trace, KEDA on the CPU target) and by the mean in the sixth (fairness), while the mean wait of one pod reads the runs disagree in four of the six (`results/live/V25_ALL_FOUR.md`, `results/live/V25_WANDERING.md`, `results/live/V25_FAULTS.md`, `results/live/V25_TRACE_GOOGLE2011.md`, `results/live/V25_KEDA_CPU_REQUESTS.md`, `results/live/V25_FAIRNESS.md`). The three mean-wait rows (fairness, the Google trace, KEDA's HTTP add-on in `results/live/V25_KEDA_REQUESTS.md`) each read LOSS by the mean with one run beyond its noise. The total's rise comes with more pods started; whether each pod also started more slowly these runs do not resolve, and no file writes a cause.

**What the headline does not see.** The index scores work, the 95th percentile and the resource held. Of the 21 rows only the fairness test's 95th percentile is a scored measure; the other twenty sit on gauges outside the index. The headline is not the whole record; the ledger is.

**The one measured cause.** One row has a cause measured from the runs' files: the batch queue (`docs/LOSS_CAUSES_2026-11-05.md`; `results/live/V25_BATCH.md`). On that rig the kind nodes and Omni-Compass share the runner's four cores, and Omni-Compass has no core of its own. At the 10 s on-site beat its own processor read 0.075 to 0.103 of a core, against 0.014 to 0.016 at omni-v21's 60 s beat. The batch pods used about 3.6 of the four cores, so about 2.5% of their processor went to Omni-Compass, the size of the queue's rise. It moved no machine, pod or limit during the queue. The remedy is written, not made: count its own processor in the body's load on a shared host, through the model gate, then three runs. The other twenty rows read "not yet written". The pod start wait was root-caused on omni-v10 and omni-v11 runs (`docs/POD_START_WAIT.md`), but no cause written for an older engine is carried onto an omni-v25 row unread (`docs/LOSS_CAUSES_2026-11-05.md`), so that page does not account for the nine rows above.

### 5.6 The cluster's 34 LOSS rows by gauge, and the stores' 14

The ledger carries 34 LOSS rows against native on the cluster's own omni-v25 tables: the nine index tests, Goldilocks, CruiseKube, the extended faults, the capacity test and the two robustness tests (`docs/LOSS_LEDGER.md`). Grouped by gauge, eighteen of them from the index's tables listed in section 5.5:

| What read LOSS | Rows | Where, and the size across the runs | What it means for the system |
|---|---:|---|---|
| pod start wait, total or mean | 17 | in eleven of the fifteen tests, all but the steady load, CruiseKube, the capacity test and the queue of jobs; e.g. demand that wanders, the total up 73.9% to 176.1% | more time spent starting pods; in the same runs more pods were started (wandering: pods started up 72% to 108%, replicas up 23% to 34%, both power given; `docs/WIRING_VERDICTS.md`), so the wait is summed over more starts. The ledger records the cause as not yet written |
| failed requests | 4 | all four at once (up 1.3% to 5.3%), demand that wanders (up 0.2% to 4.4%), the queue of jobs (from zero, in one run), the 300 s after a kill (section 3.9) | more requests failed |
| response time | 5 | CruiseKube: the mean LOSS in all three of our runs (up 2.8% to 4.0%), the 95th percentile (up 1.4% to 2.7%) and the 99th by the mean of our three runs; the noisy neighbour: the service's 95th percentile (slower in two of the three runs, up 6.6% and 16.5%) and the second app's (up 3.6% to 13.4%), each by the mean of our three runs | slower answers |
| time over the response line | 3 | the queue of jobs, the noisy neighbour's second app, the 300 s after a kill | more time over the line |
| alert minutes | 1 | the queue of jobs | more minutes that would page a person |
| the queue's finish | 1 | the queue of jobs, up 2.6% to 2.9% | the batch finished later; the one measured cause (section 5.5) |
| work inside the line under a CPU quota | 3 | the capacity test, at the 2- and 3-core caps, by the mean of our three runs | less work from the same capacity (`results/live/V25_CAPACITY.md`) |

**The stores.** The ledger carries 14 LOSS rows on the stores' tables (`docs/LOSS_LEDGER.md`): on the counted tables, pgbench `simple_update`'s median response and YCSB `burst`'s mean and 99th percentile, each by the mean of our three runs (slightly slower answers there; section 5.5); on the service-objective and shipped-native sets, 11 more (PgBouncer 1, YCSB 7, sysbench 2, Redis 1). On the shipped-native Redis set the knob is at its limit on native and Omni-Compass writes nothing (section 2.3.4). Its omni-v25 table records no ceiling written in any workload, and still carries one LOSS row: the `large` workload's 95th percentile, by the mean of our three runs (`results/live/V25_REDIS_SHIPPED.md`). With nothing written, that row measures the rig's run-to-run variation, not Omni-Compass (section 5.13, item 6).

### 5.7 The oversight line: the minutes a person would be paged

**The gauge.** An alert minute is a whole minute whose 95th percentile, failed requests counted over, was over the response line: the minute an on-call page would be open. Fewer is GAIN. Nobody is on call on GitHub's runners, so no engineer's hour is on any receipt; what is counted is the event that would call one (`results/OVERSIGHT.md`).

**The reading.** Over 41 omni-v25 Kubernetes tests the alert minutes a repetition fall from 492.9 on native to 456.4 with Omni-Compass on top: **GAIN in all three of our runs, down 7.4%** (`results/OVERSIGHT.md`, `results/SITE_NUMBERS.md`). Summed over the tests, health was lost for fewer minutes.

| Run | Native → Omni-Compass, summed | Reading | 95% interval, minutes fewer |
|---|---|---|---|
| A | 485.03 → 451.67 | GAIN, down 6.9% | 21.94 to 44.79 |
| B | 503.20 → 461.27 | GAIN, down 8.3% | 34.19 to 49.68 |
| C | 490.33 → 456.27 | GAIN, down 6.9% | 24.41 to 43.72 |

**Test by test** (`results/OVERSIGHT.md`). Alert minutes were fewer in 15 tests, falling to none in 3; the same in 2; **more in 24**. Every one of the 24 is a batch test: the batch queue itself, or a scheduler or orchestrator under the batch stream (the default scheduler, the bin-packing profile, Kueue, Volcano, KAI, Koordinator, KubeRay, Gödel, Crane, Karmada, Open Cluster Management and Armada). Four read **LOSS in all three of our runs**, more minutes over the line: Armada and Karmada on the organism alone (up 11.3%, up 16.1%), Karmada on top (up 8.0%) and Open Cluster Management on top (up 17.9%). The 15 with fewer minutes are the service tests (steady, wandering, all four, fairness, the Google trace, both fault tests, both KEDA set-ups, Goldilocks, the cost to match, the two robustness tests), Crane on the organism alone, whose runs disagree, and KubeRay on top, STEADY, under the floor.

**What it is not.** The sum weighs each test by its own minutes, and the two-hour test holds 20% of native's (`results/OVERSIGHT.md`). It counts minutes, not heads or salaries. The page's 7% people share is an example with no receipt, and the bill line built on it is not a result.

### 5.8 The chip: arm A against arm B (class P)

**The rig.** One A10 on Lambda, native's power cap at 70% of the card's top, the full load: more requests offered than the card serves in its window. Three runs of five paired repetitions, read by the card's own meter (`results/gpu/V23_A10_CAP_FULL_ABC.md`, `results/TWO_BILLS.md`); omni-v23. The runs are numbered 1, 2 and 3 here, the run letters A, B and C of its table (the convention of chapter 4).

**Energy.** Energy per request served reads **GAIN in all three of our runs, down 1.3%** by the mean (`results/SITE_NUMBERS.md`): down 1.79%, 1.35% and 0.78% by run (`results/TWO_BILLS.md`). The card spent less energy on each answer, a cut measured at the chip. The card's energy and its mean power also read GAIN in all three of our runs (`results/gpu/V23_A10_CAP_FULL_ABC.md`).

**Work for the bill.** Both arms rent the same window at the same price, so ΔB ≈ 0 and G ≈ ΔW (section 4.2). Requests served went from 2,616 to 2,656, from 2,270 to 2,286 and from 2,255 to 2,239. The bill reads STEADY, under the floor (the three runs' mean 0.01%), because the rented window is the same. The work for the bill reads **the runs disagree**: up 1.5%, up 0.7%, down 0.7%; it is not yet shown to rise. In run 3 Omni-Compass on native served fewer requests and answered more slowly, and that run's own verdict reads "energy improvement with service tradeoff". The 95th-percentile response reads the runs disagree (shorter by 3.68% and 1.38%, longer by 2.25%: no settled change in the slowest answers), as do requests not served and every other response-time gauge (`results/gpu/V23_A10_CAP_FULL_ABC.md`; `results/TWO_BILLS.md`).

**The A100, one card, omni-v21.** An A100 (SXM4, 40 GB, on Lambda), three runs of 5 paired repetitions at the factory tune on native's cap at 70% of the card's top (`results/gpu/V21_A100_CAP_ABC.md`). The work reads STEADY, the same; the energy STEADY, under the floor (its device counter GAIN by the mean of our three runs, beyond the noise in 1 of 3); the mean and the 99th-percentile response LOSS by the mean of our three runs, beyond the noise in none; and the 95th percentile the runs disagree: slightly slower answers for no change in the work. The whole-system page reads the work per energy STEADY, under the floor (the three runs' mean 0.11%): the same work for the same energy. Of the 39 rows that page reads for the card (the factory tune, the same runs' full-load part, and the tune-down's own three runs), 4 read LOSS, each by the mean of our three runs and beyond the noise in none of them: the mean response time and the 99th percentile in the factory tune's part; the requests not served and the 95th percentile in the full-load part. They point to slightly slower answers and slightly more requests missed, though no single run settled any of them (`results/WHOLE_SYSTEM.md`, section 3b).

**The A100, one run on omni-v18's card controller.** One run of ten paired repetitions (`RELEASE_MANIFEST.json`, `physical_meter_results`; `results/gpu/run-20261024T091235Z/GPU_REPS.md`), in the same rental as the kill-switch drill of section 3.11 (the two folders carry one stamp). Every service gauge reads STEADY. Omni-Compass wrote nothing, because both knobs were at their top on native (at its limit on native). The temperature reads power given, up 1.4% to 1.5%, with no setting written. With the knob already at its top on native, the supervisory loop has nothing to add.

**The card inside the organisms, omni-v23.** In the eight-card A100 and the fully loaded A10 stack runs, Omni-Compass's card-side process wrote nothing in any Omni-Compass arm (0 in 15, 12 and 12 arms; 0 in 62 in each A10 run). On the card the two arms were one system, and those cells read the arms' order and the card's drift, not the engine (`results/TWO_BILLS.md`). The eight-card machine ran one paired repetition at each size each run reached within its rented hours, so no row there is judged: each is shown, not judged, or has no value where a run did not reach that size (`results/gpu/V23_A100_8CARD_STACKS_ABC.md`). Three A10 cells read the work LOSS by the mean of our three runs with no run beyond its noise (the spine at one copy, Physics / Robotics / Autonomous at ten, the whole tower at ten), their work per dollar power given; they stand in the record and are read, as the page reads them, as drift. Section 4.8, item 1, reads the same table's card rows.

### 5.9 The cloud: arm C against arm D (class L, omni-v18)

**The rig.** Azure AKS at the tune-down on the machines alone, as section 2.3.6 sets out: run 40069633316, the steady load, 97 of 100 paired repetitions finished (`results/live/AKS_STEADY_100_OMNI_V18.md`). It is one run, so no three-run reading exists: each gauge is the mean of the 97 pairs with its 95% interval, worded as `results/SITE_NUMBERS.md` words it and, for the rows that page leaves out, by the key.

| Gauge | C, native | D, Omni-Compass on native | Reading |
|---|---:|---:|---|
| 99th percentile (ms) | 4,744 | 4,222 | GAIN, down 11.0%, beyond the noise |
| 95th percentile (ms) | 1,245 | 1,195 | GAIN, down 4.0%, inside the noise |
| mean response (ms) | 517.1 | 503.1 | GAIN, down 2.7%, inside the noise |
| time over the response line (% of samples) | 29.06 | 28.81 | GAIN, down 0.9%, inside the noise |
| alert minutes | 14.07 | 13.9 | GAIN, down 1.2%, inside the noise |
| failed requests (%) | 4.758 | 4.945 | **LOSS, up 3.9%, inside the noise** |
| pods with no machine to take them | 2.598 | 2.392 | GAIN, down 7.9%, inside the noise |
| pod start wait, total (s) | 525.4 | 455.2 | GAIN, down 13.4%, inside the noise |
| bill at list price ($ a repetition) | 0.05626 | 0.05694 | power given, up 1.2%, inside the noise |
| machine-hours billed | 0.586 | 0.5931 | power given, up 1.2%, inside the noise |
| energy, 25 W standby (Wh, declared model) | 82.7 | 83.23 | power given, up 0.6%, inside the noise |

**What it means.** The slowest one per cent of requests waited less, the one reading beyond the noise. More requests failed on the mean of the pairs, a LOSS for those users, inside the noise: possibly more failures, not settled by the run. The bill and the machine-hours rose slightly, power given: no bill saving is shown. The preregistered stopping rule read the bill at every look and never decided it, so the set ran to the paid cap. No work was counted, so G(cloud) is **not read** (`results/TWO_BILLS.md`). The Omni index's cloud category stays pending until the omni-v25 Azure sets land (`results/OMNI_INDEX.md`).

### 5.10 The whole-system composition: a second reading (class S)

**The rule** (`results/WHOLE_SYSTEM.md`). Each layer ℓ is measured with the layer under it running as native runs it, and the layers' ratios are multiplied:

  R(g) = ∏ℓ Rℓ(g),  G(g) = R(g) − 1,  log R(g) = Σℓ log Rℓ(g).  (5.1)

The index is the geometric mean of R over work, speed and machines. Energy and the bill are held at native's. The chip, the cloud and the unrun machine layer enter as exactly 1 on every gauge.

**The reading.** Without the card, by the index's rule: **GAIN, up 41.9%** (×1.4194; gauges independent, up 33.7% to up 50.6%; gauges correlated, up 32.5% to up 52.1%). Work reads GAIN, up 27.5%: more work. Speed reads GAIN: native's 95th percentile 298.6% above Omni-Compass's, that is, the 95th-percentile response 74.9% shorter (`README.md`, "Bill by Route"). Machines and resources held read power given: native's 43.7% below Omni-Compass's (×0.5626), that is, 77.7% more machines held (`README.md`). With the chip and the wire at 1, the total is the product of two class L layers: the cluster (23 tests) and the services on it (17 tests).

**Why it is modelled.** No run stacked the layers. The product assumes that a layer's ratio holds when the layers around it also carry Omni-Compass. The page tests that on the products' four ways, where 22 of 33 pairs of orchestrator and gauge agree within the noise; where they do not, the 11 show the orchestrator under Omni-Compass changing its factor, and the page composes the factor measured on top of the orchestrator (section 4 of the page). The page's text dates those tables to omni-v12; its code reads each product's newest table (`tools/whole_system.py`, `newest`), which section 2 of the page names as omni-v25 for every product but Koordinator (omni-v12). The stacked run is preregistered (`docs/WHOLE_SYSTEM_PREREGISTRATION.md`) and not yet run.

### 5.11 The LOSS ledger: 273 rows against native, and their causes as written

Across every benchmark's newest table 520 rows read LOSS: 273 against Omni-Compass's own native, the readings do no harm is judged by; 76 in place of a controller; 171 without Omni-Compass, or with two changes at once (`docs/LOSS_LEDGER.md`). The last two groups answer other questions (section 4.6) and are shown, not read as do no harm.

Of the 273, 267 ran on omni-v25 and 6 on omni-v12. By the gauge's aim, 268 are time waited, missed or failed and 5 are work done. By strength, 83 are strong, 47 moderate, 53 weak and 90 inconclusive. All 273 are class L (`results/verdict_audit/VERDICT_AUDIT.md`). The standing counts beside them, of every word, are in section 4.6.

**Where they sit.** Counted by this monograph from the ledger's rows, table by table (`docs/LOSS_LEDGER.md`): 34 on the cluster's own fifteen tables (section 5.6); 14 on the stores' tables (section 5.6); 56 on the two-way tables of the scheduler rigs (the default scheduler 9, its bin-packing profile 10, Kueue 9, Volcano 9, the KAI scheduler 8, Koordinator 11); 79 on the four-ways tables of Omni-Compass on top of a product; and 90 on those of Omni-Compass on the organism alone. The 6 on omni-v12 are Koordinator's four ways. Armada on the organism alone and Karmada on top carry the most of any table, 12 each. The batch tests therefore hold most of the rows, which agrees with section 5.7, where every test with more alert minutes is a batch test. Section 6.5 reads them product by product.

**Causes, from the ledger's cause column.**

1. **Measured:** the batch queue, Omni-Compass's own processor at the 10 s beat on a shared runner (section 5.5). One row.
2. **Suspected, not yet measured:** the queue rows of the batch-scheduler rigs (the queue finished, the jobs' wait and turnaround, and one count of jobs unfinished at the window's end). On those rigs Omni-Compass has its own core, but the API server that answers its reads runs on the batch pods' cores, and at the 10 s beat it is asked six times as often as at 60 s. omni-v12's four ways at the 60 s beat also read KAI's queue LOSS by the mean, "so the beat is not the whole of it". The control plane's processor is to be read beside the queue in the next runs, then the next version goes through the model gate (`docs/LOSS_CAUSES_2026-11-05.md`).
3. **Every other row** reads "not yet written", among them the failed requests of the all-four test.

Most LOSS rows on the engine that stands have no cause on file; none is cut. The products named appear as the native controllers Omni-Compass sits on, and no row is read as a judgement or ranking of a product.

### 5.12 Can, gives, cannot yet show, does not do

| Kind | Statement | Class, engine | Receipt |
|---|---|---|---|
| **CAN** (measured) | Real Kubernetes: the 95th percentile shorter in 8 of 9 tests; the category GAIN, up 20.5% | L, omni-v25 | `results/OMNI_INDEX.md` |
| **CAN** | Fewer alert minutes over 41 tests: GAIN in all three of our runs, down 7.4%; more in 24 of them, every one a batch test | L, omni-v25 | `results/OVERSIGHT.md` |
| **CAN** | The batch test's jobs on fewer machine-hours: GAIN, a cut, native's 19.1% above; its queue finished later, LOSS in all three of our runs | L, omni-v25 | `results/OMNI_INDEX.md`, `docs/LOSS_LEDGER.md` |
| **CAN** | More work inside the line from Kafka and Redis: GAIN in all three of our runs on all six workloads; MySQL GAIN by the mean on two of four | L, omni-v25 | `results/WHOLE_SYSTEM.md` |
| **CAN** | Hand every setting back after a kill: inside the 60 s allowance in every repetition, at a mean of 11 to 12 s (section 3.9) | L, omni-v25 | `results/live/V25_ROBUST_KILL.md` |
| **CAN** | Less energy per request on one A10, its own meter: GAIN in all three of our runs, down 1.3% | P, omni-v23 | `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| **CAN** | Azure's 99th percentile: GAIN, down 11.0%, beyond the noise, in one run of 97 pairs | L, omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| **GIVES** (power given) | Resources held, native's below Omni-Compass's by: Kafka consumers 57.6% to 63.1%; Redis memory ceiling 73.6% to 81.0%; MySQL buffer pool 16.3% to 58.6%; MongoDB cache 2.3% to 50.8% in three of four workloads; PgBouncer pool 18.0% in `simple_update` and 1.0% in `tpcb_hot` | L, omni-v25 | `results/OMNI_INDEX.md` |
| **GIVES** | Pods and replicas: pods started power given in all three of our runs in five Kubernetes tests (section 5.5); replicas up 4.9%, 5.1% and 6.0% under a noisy neighbour | L, omni-v25 | `results/live/V25_FAIRNESS.md` |
| **GIVES** | Its own processor: 0.075 to 0.103 of a core at the 10 s beat in the batch rig; 0.05539 to 0.0564 in the fairness test; 0.005163 cores on Azure | L | `docs/LOSS_CAUSES_2026-11-05.md`, `results/live/V25_FAIRNESS.md`, `results/live/AKS_STEADY_100_OMNI_V18.md` |
| **GIVES** | Modelled energy under KEDA: native's 1.4% and 2.0% below, shown, not scored | L inputs, declared model, omni-v25 | `results/OMNI_INDEX.md` |
| **GIVES** | Azure's bill and machine-hours up 1.2%, modelled energy up 0.6%, inside the noise | L, omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| **CANNOT YET SHOW** (not measured) | More work for the bill on the chip: the runs disagree; the bill STEADY because the rented window is the same | P, omni-v23 | `results/TWO_BILLS.md` |
| **CANNOT YET SHOW** | Work per dollar in the cloud: no work counted in the set on file; omni-v25 not yet run in the cloud; Google Cloud and Amazon not yet run | — | `results/TWO_BILLS.md` |
| **CANNOT YET SHOW** | The machine layer (the kernel, bare metal, Kepler) and the stacked whole-system run: neither run | — | `results/WHOLE_SYSTEM.md` |
| **CANNOT YET SHOW** | A people or payroll saving: the 7% share is an example with no receipt | — | `results/OVERSIGHT.md` |
| **CANNOT YET SHOW** | Outside review: none; every receipt says "No outside party has reviewed or approved these results" | — | `results/OMNI_INDEX.md` |
| **CANNOT YET SHOW** | Global stability: four theorems on bounded channels over the declared parameter box, not a global-stability proof | — | `docs/FORMAL_STATUS.md` |
| **DOES NOT DO** | Sit in the data path | — | `DISCLOSURES.md` |
| **DOES NOT DO** | Remove a native controller: on Kubernetes the scheduler, the kubelet and the autoscalers stay in every arm. Where the operator names a workload with no autoscaler, it sets that workload's replicas itself; after three refused writes in a row it creates native's pod autoscaler from the operator's recorded target and range and leaves the workload to it | — | `docs/INDUSTRY_LANDSCAPE.md`, `docs/OMNI_V19.md`, `docs/OMNI_V23.md` |
| **DOES NOT DO** | Move the chip's own speed or the place's own software layer; ask a cloud for machines; hold a cloud credential | — | `results/TWO_BILLS.md`, `docs/INDUSTRY_LANDSCAPE.md` |

### 5.13 Threats to validity

1. **The rig shapes the result.** The software end runs on GitHub's shared runners, kind on four cores (`results/live/V25_FAIRNESS.md`). The one measured LOSS cause is Omni-Compass's own processor on that shared host; on a machine of its own the effect is unmeasured.
2. **The index is a chosen aggregate.** It uses equal category weights and three scored measures, with STEADY readings and unmetered energy entering as 1. Twenty of the 21 LOSS rows in its own tables lie outside what it scores. Its construction, Kafka's weight and the wording of its admission rule are item 9 of section 4.8.
3. **Three runs, many gauges.** 90 LOSS and 88 GAIN rows are inconclusive, and 185 rows read the runs disagree (`results/verdict_audit/VERDICT_AUDIT.md`). No correction for the number of gauges is applied to class L tables. `results/MULTIPLICITY.json` is a Holm correction over the 500 modelled runs of two seeds, class S.
4. **Engines differ by place** (section 4.8, item 7). The composition's card layer is an A100 on omni-v21, entered as exactly 1 (`results/WHOLE_SYSTEM.md`). None of these transfers to omni-v25 until it is run there.
5. **Small samples off the software end.** The cloud is one run of 97 pairs, one region, one machine type, with no work counted. The chip is one A10 and three runs of five pairs.
6. **The noise floor of the word.** A word is assigned from a 0.5% floor on the mean of three runs. On the shipped-native Redis set, where Omni-Compass wrote nothing, one LOSS row still stands (section 5.6). Single rows near the floor, especially those beyond the noise in none of the three runs, can reflect run-to-run variation rather than the arm.
7. **The composition is modelled.** It assumes separability, which held for 22 of 33 pairs; where it failed, the page composes the on-top factor, which is itself measured with only one layer carrying Omni-Compass. The stacked run that would replace the composition has not been made.
8. **Self-run.** The company's own code ran and scored everything; preregistration was within the repository only (`results/OMNI_INDEX.md`; section 6.14).
9. **Theory does not cover these outcomes.** The four theorems in `docs/FORMAL_STATUS.md` hold over a declared parameter box, two of them in part on computed checks rather than proofs; they predict none of the readings above (section 3.14).

**Questions the files could not answer.**

- No record prints a count of the LOSS rows by table type or by cause. Sections 5.5 and 5.11 count them from the ledger's rows.
- The A10 full-load receipt does not print how many settings the card-side process wrote.
- `results/OVERSIGHT.md` calls the index's second reading 12.9%, where `results/OMNI_INDEX.md` prints 94.0%. Neither says which is stale.
- `results/OMNI_INDEX.md` says the steady and wandering tests "join when their omni-v25 runs land", while its own table already carries both from omni-v25 tables.
- `results/OMNI_INDEX.md` glosses its resource ratio as Omni-Compass doing the same work on that many percent fewer machine-hours; that matches native's over Omni-Compass's less one only for small changes. This monograph writes every resource size as native's against Omni-Compass's.
- `results/WHOLE_SYSTEM.md` dates its separability tables to omni-v12 in its text, while its code reads the newest tables (section 5.10).
- The LOSS ledger reads no chip table: the three A10 stack cells of section 5.8 that read the work LOSS by the mean are not among its 273.
- No record gives the cause of the rows that read "not yet written", nor of the 24 tests with more alert minutes, beyond the suspected control-plane reads.

## 6. The Native Tools and Products: What They Do, What They Leave, Where Omni-Compass Sits; Reproducing the Engine; Limits

This chapter places Omni-Compass among the controllers and products that already act on the chip, the cloud and the software. It describes other products only from their own public material, as the repository records it (`docs/INDUSTRY_LANDSCAPE.md`, `docs/LANDSCAPE.md`). It then sets out how a reader re-runs each benchmark and re-derives each number from its raw receipts, and it closes with the threats to validity of the whole programme. Nothing here ranks another product or reproduces a grade of one. A description says only which layer a product acts in and which loop it closes.

### 6.1 The three layers: inner loops, the outer loop, the control plane

Every controller in the three layers is an inner loop in the sense of section 2.2: it closes its own loop on its own signal at its own clock, by its own published rule (`docs/INDUSTRY_LANDSCAPE.md`). Omni-Compass is the one supervisory outer loop over them, writing each setting by equation (2.2) inside the band between native's setting, recorded before the first write, and the muscle's own limit; every write is read back, each setting is restored at the end, and if the outer loop stops a lease hands every setting back to native's, gradually in the models and directly live (`docs/INDUSTRY_LANDSCAPE.md`; sections 3.4 and 3.9). The cascade lives in the control plane (section 1.1).

| Layer (`docs/INDUSTRY_LANDSCAPE.md`) | What its tools move, on what signal | What they leave to the other layers | What Omni-Compass writes there |
|---|---|---|---|
| Chip | the power limit, clocks and fans, on the card's own power, temperature and utilisation | how many machines and replicas the work is offered, and when; the service's queues and targets | the power limit and clock ceiling, under the operator's own cap |
| Cloud | the fleet's count, instance types and purchase model, on utilisation and the bill | the card's power limit; the service's own controllers | machines the cloud's autoscaler made and the work does not need, parked for it to remove; the autoscalers' ranges |
| Software | placement, replicas, each service's setting, each on its own signal | the other loops' signals and the layers beside them | the pod autoscalers' targets, replicas ahead of the load, processor given to pods, a database's pool, a cache's memory, a broker's consumers |

### 6.2 The chip layer

The chip's own tools are the card's firmware (power capping, clock and voltage scaling, thermal limits) and the vendor's power profiles (`docs/INDUSTRY_LANDSCAPE.md`). `docs/LANDSCAPE.md` cites NVIDIA's own material for two of them:

- Workload Power Profiles are vendor-set bundles of a card's power, clocks and link states.
- Mission Control adds a power service that makes power a scheduling input for Slurm and Run:ai.

The same page records that Kepler measures each workload's energy and exports it; it moves no setting.

Omni-Compass sits on the card's own firmware limits. It writes the power limit and the clock ceiling through the card's management interface, under the operator's own cap (`docs/INDUSTRY_LANDSCAPE.md`; section 2.3.1). The card's decision rules have C++ twins; its device input and output is Python only (section 3.13). The class P record, one A10 on omni-v23 and the A100 on omni-v21, omni-v18 and omni-v23, is read in section 5.8.

### 6.3 The cloud layer

The cloud's tools are cost visibility and FinOps, node autoscalers and provisioners, rightsizing, purchase planning and the repatriation of steady loads to bare metal. They move the fleet and close their loops on utilisation and the bill (`docs/INDUSTRY_LANDSCAPE.md`). Omni-Compass sits on the cloud's own cluster autoscaler. It parks machines that autoscaler made and the work does not need, for that autoscaler to remove. It asks the cloud for no machine and holds no cloud credential (same source). The one Azure set on file (class L, omni-v18) is read in section 5.9.

**Our own model of a cloud** (class S, modelled). It is omni-v23's rules on the corrected model, the ladder read for the omni-v24 pick (`docs/OMNI_V24.md`), at the max on the cloud's own autoscaler.

- No beat is admissible. The pick rule was frozen before the reading (`docs/PACE_PREREGISTRATION.md`, amendment 4), and in a cloud it does not let the machine-hours rise.
- Every beat raised the machine-hours against native: power given, up 7.8% to 33.7%, and up 14.7% at 60 s. The model's work is held by its own load (`docs/INDUSTRY_LANDSCAPE.md`), so this is more machines billed for the same work.
- Every beat but 90 s raised the pods waiting for a place: LOSS, up 15.4% at 60 s.
- The page's cause: an autoscaler target held ahead of the load buys machines the cloud bills, and a pod waits while the cloud makes one. The factory beat through a cloud therefore stays 60 s, and these rows go on the next version's list (`docs/OMNI_V24.md`).

The cloud category of the Omni index is pending (`results/OMNI_INDEX.md`). Google's and Amazon's sets are gated by their own $0 checks (`docs/LIMITATIONS.md`; section 2.3.6).

### 6.4 The software layer, I: autoscalers and each service's own controllers

The native controllers here are the pod autoscalers (Kubernetes' HPA; KEDA and its HTTP add-on) and each service's own setting, described with what Omni-Compass writes to each in sections 2.3.3 and 2.3.4 and read in sections 5.3 to 5.6. The layer differs from the chip and the cloud in one respect that bears on every reading there: at the data stores native is not a loop but a constant, a setting fixed once and held through every quiet hour and every rush, so a GAIN there measures a moving setting against a fixed one (section 2.3.4; section 2.9, item 1). On top of the pod autoscalers native is a loop, and of that loop Omni-Compass moves only the target and the replica range (section 3.1).

### 6.5 The software layer, II: open-source schedulers and orchestrators, run live

Fourteen schedulers and orchestrators are on file, each run live as its project ships it, with Omni-Compass on top (`results/live/GOVERNORS.md`; the rig, versions and levers in sections 2.3.3 and 2.3.5; workflows in section 6.9). KubeEdge and Nephio have no rig yet. The other twelve have run, the Kubernetes scheduler in two profiles, so thirteen rigs have read. Karmada, Open Cluster Management and Armada run on a group of two clusters (`scripts/reruns.txt`).

Each count below is the number of judged rows reading each word in the omni-v25 table of Omni-Compass on top of the product, against the product as shipped. Where the product runs two ways, the count is from the two-way table. Otherwise it is from the "on top" comparison of the four-way table. The four-way tables of Kueue, Volcano, the KAI scheduler and the bin-packing profile carry their own counts (`results/live/GOVERNORS.md`). The counts read Omni-Compass on our rig and workload; they are not a measurement of the product.

| Product | What it acts on | Omni-Compass on top, against it as shipped | Table |
|---|---|---|---|
| Kubernetes scheduler | pod placement | 6 GAIN, 9 LOSS, 2 power given, 5 STEADY | `results/live/V25_VANILLA.md` |
| its bin-packing profile | pod placement | 6 GAIN, 10 LOSS, 2 power given, 4 STEADY | `results/live/V25_BINPACK.md` |
| Kueue | batch admission by queue quota | 5 GAIN, 9 LOSS, 2 power given, 4 STEADY, 2 disagree | `results/live/V25_KUEUE.md` |
| Volcano | batch scheduling: queues, gangs | 4 GAIN, 9 LOSS, 2 power given, 5 STEADY, 2 disagree | `results/live/V25_VOLCANO.md` |
| KAI scheduler | AI workload scheduling: queues, fair share, gangs | 5 GAIN, 8 LOSS, 2 power given, 4 STEADY, 3 disagree | `results/live/V25_KAI.md` |
| Koordinator | QoS colocation | 1 GAIN, 11 LOSS, 2 power given, 7 STEADY | `results/live/V25_KOORDINATOR.md` |
| CruiseKube | rightsizing: requests and limits, in place | 1 GAIN, 3 LOSS, 1 power given, 7 STEADY, 4 disagree | `results/live/V25_CRUISEKUBE.md` |
| Crane | predictive autoscaling | 0 GAIN, 3 LOSS, 2 power given, 7 STEADY, 4 disagree | `results/live/V25_CRANE_4W_TOP.md` |
| KubeRay | Ray clusters, the Ray autoscaler | 6 GAIN, 2 LOSS, 2 power given, 5 STEADY, 7 disagree | `results/live/V25_KUBERAY_4W_TOP.md` |
| Gödel scheduler | unified online and offline scheduling | 4 GAIN, 9 LOSS, 2 power given, 4 STEADY, 3 disagree | `results/live/V25_GODEL_4W_TOP.md` |
| Armada | multi-cluster batch | 6 GAIN, 3 LOSS, 2 power given, 10 STEADY | `results/live/V25_ARMADA_4W_TOP.md` |
| Karmada | multi-cluster placement | 4 GAIN, 12 LOSS, 2 power given, 4 STEADY | `results/live/V25_KARMADA_4W_TOP.md` |
| Open Cluster Management | multi-cluster management | 4 GAIN, 10 LOSS, 2 power given, 4 STEADY, 2 disagree | `results/live/V25_OCM_4W_TOP.md` |
| KubeEdge; Nephio | edge nodes; network-function automation | not yet run: rigs not built | `results/live/GOVERNORS.md` |

("disagree": the runs disagree.)

On eleven of these thirteen rigs, LOSS rows outnumber GAIN rows; KubeRay and Armada are the exceptions. With the four ways on the organism alone, these rigs' tables carry 225 of the 273 LOSS rows of Omni-Compass against its native: 56 on the two-way tables, 79 on the four-ways tables of Omni-Compass on top and 90 on those of Omni-Compass on the organism alone (section 5.11; `docs/LOSS_LEDGER.md`). The LOSS rows that recur from table to table are the pods' start wait; the web service's 95th and 99th percentiles, and its alert minutes; the queue finishing later; and the jobs' turnaround growing (same source).

**The pattern is a trade, and is reported as one.** On most of these products Omni-Compass on top held fewer machines while the jobs waited longer and the served 95th percentile was slower. In Kueue's four-ways table the 95th percentile reads LOSS in all three of our runs (the oriented ratio ×0.9056, native's 95th percentile over Omni-Compass's: Omni-Compass's answers are the slower), and the machines GAIN by the mean of our three runs, beyond the noise in 2 of 3 (×1.1779, native's machines over Omni-Compass's) (`results/WHOLE_SYSTEM.md`, section 2). Fewer machines were spent and more waiting was bought with them; under the engine's own rule of do no harm the waiting is the harm. Armada is the exception on the oriented ratios: speed GAIN (×1.7452) and machines GAIN (×1.9315), both in all three of our runs, though its table still carries 3 LOSS rows (`results/live/GOVERNORS.md`). On the KAI scheduler's four ways, the queue finished 1.0% to 2.8% later in all three runs and the turnaround grew 5% to 14% (`docs/LOSS_CAUSES_2026-11-05.md`): batch work waited longer.

**Causes.** Only the queue rows carry a cause. The one measured cause is the plain batch stream's, where Omni-Compass's process has no core of its own (section 5.5); on the scheduler rigs, where it has, the cause is suspected and not yet measured: the control plane's answers to its reads (section 5.11). The other recurring LOSS rows read "not yet written" (`docs/LOSS_LEDGER.md`).

**A cost the model counted as a resource.** The 10 s beat was chosen in our own model (class S). That model counted both of its costs as power given (`docs/OMNI_V24.md`): the cluster read 6,897 times an hour, against 2,317; and the process's own processor working 10.3 s an hour, against 1.3 s. It did not count either as processor taken from the work. The live plain batch rig (class L) shows that on a shared host that processor does come out of the work: a cost the model treated as a resource reads, on the real rig, as a LOSS on the work.

Omni-Compass running the organism in place of a controller is a different question. It is recorded apart, with 76 LOSS rows, none of them counted in the 273 (`docs/LOSS_LEDGER.md`, "In place of a controller").

### 6.6 Commercial products in the same layers, from their own material

`docs/LANDSCAPE.md` names products in these layers from their own public pages, read on 24 October 2026. None was benchmarked by us (`docs/INDUSTRY_LANDSCAPE.md`), and that page's grades are not reproduced here. The table lists the products it names that act on a setting.

| Product | Layer | What its own material says it acts on |
|---|---|---|
| StormForge Optimize Live | software | requests, limits and the HPA's target utilisation, alongside the HPA |
| Cast AI | software, cloud | pods resized in place; a node provisioner that replaces the cluster autoscaler |
| ScaleOps | software | pod rightsizing; the HPA's and KEDA's own minimums, maximums and triggers |
| PerfectScale | software | rightsizing, with out-of-memory kills and processor throttling as goals |
| Sedai | software, cloud | gradual changes in observe, approve or autopilot mode, with health checks and rollbacks |
| IBM Turbonomic | software, cloud | requests and limits resized, pods moved, clusters scaled, each action audited |
| Spot Ocean | cloud | an infrastructure autoscaler that keeps headroom spare and replaces the cluster autoscaler |
| Akamas | software | container and runtime configuration under response-time and error constraints |
| DeepMind cooling (2018), Phaidra, BrainBox AI | facility | cooling and building setpoints; at DeepMind the site's own control system checks each action against operator-set limits; BrainBox AI writes setpoints back to an existing building management system over BACnet |

Where a product replaces a native controller (by their own material, the node side of Cast AI and of Spot Ocean), it becomes the native of its layer in a cluster that runs it. The position Omni-Compass takes everywhere, on top of native, would then be on top of that product. Some products write a setting Omni-Compass also writes, such as an HPA's target or a pod's requests and limits. On the open-source rigs that do run, Omni-Compass writes none of the product's objects, and where a product owns the service's autoscaler (Crane), Omni-Compass's moves go through that product's own object (section 2.3.5). No rig runs a commercial stack, so nothing is claimed about one. The catalogue's own cooling, building and grid muscles are our own models (class S).

### 6.7 The live benchmark engine beside the operator's surfaces that exist

`docs/LANDSCAPE.md` describes the operator's surfaces that exist:

- Metrics dashboards are read-only.
- Kubernetes consoles make manual writes.
- Rightsizer consoles read savings against a computed baseline, not against native running beside them.
- SCADA and HMI platforms bind live setpoints to the controllers' own tags and order the screen by ANSI/ISA-101.01 and ANSI/ISA-18.2.

That page names the SCADA surface as the bar the live engine page is held to.

The page shows native beside Omni-Compass on every monitor, gauge by gauge, each read by what the gauge is for (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, the preface's standards). A reader sees what the supervisory loop did and did not do on each recorded run. Three parts of the engine run in the page itself and every other monitor plays a record; the page decides no word itself (section 1.6; same manual, 35.4 and 35.5).

The page can also read a wired system's own Prometheus series beside a record. For each press of a control it prints the request that the system's control panel (`tools/omni_control.py`) would take. It writes nothing to that system (same manual, chapter 2). It therefore does not yet meet the bar on one point: it does not drive a live mechanism from its own controls.

### 6.8 Reproducing the engine: from a workflow to a number

Every number in the index travels one chain: a workflow run, then its raw folder, then a three-run table written by its tool, then the index, the ledger and the page.

**Raw receipts.**

- `.github/workflows/archive-run.yml` copies the files of every finished run, failed runs included, onto the branch `raw` as a folder named for the run, every hour. The files are the captures, response times, audit and controller logs, and a SHA-256 manifest per repetition. A run's raw folder holds audit.jsonl, Omni-Compass's own record of its decisions, and capture.csv, the moves of native's own controllers; the scorer is `tools/live_reps.py` (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, 43.1).
- The receipts live there, not on main. They held 36 GB when they were moved off main (`scripts/raw_archive.sh`).
- The script has four subcommands for a reader. `fetch` fetches the branch as trees only. `open` opens chosen folders under `results/live/raw/`. `has` tests for one folder. `join` rejoins files split under GitHub's file limit.
- Each run's folder carries SHA256SUMS_ALL.txt, the SHA-256 of every file. From 31 October the archive job signs each run's sums with Sigstore, keyless, under GitHub's own identity for that job, and the signature enters Sigstore's public transparency log; a run archived before that day reads "sums only" (`docs/THE_RECEIPTS.md`, `tools/verify_receipt.py`). Set 20's sums are also on main (`results/live/SET20_RAW_SHA256SUMS_ALL.txt`).
- `tools/verify_receipt.py`, given an opened run's folder, checks every file against its sum, and the sums against the signature. A sum "shows that a file has not changed since the sum was written, not who wrote it", and "Neither check is an outside review" (`docs/THE_RECEIPTS.md`).

**Tables.**

- `tools/reproduce.py` rebuilds each three-run table of the engine that stands from its recipe and compares it byte for byte with the committed file; any difference fails. A recipe names the tool, its arguments and the three runs: `results/live/RECIPES.json`, and `results/live/FRONT_PAGE_STATE.json` for the data stores.
- `.github/workflows/reproduce.yml` runs it every Monday at 05:41 UTC and on demand, with a read-only token, so it writes nothing to the repository.

**Aggregates.**

- `tools/omni_index.py` builds the index from the newest three-run tables (section 4.7).
- `tools/whole_system.py` builds the composition (section 5.10).
- `tools/loss_ledger.py` and `tools/verdict_audit.py` build the ledger and the audit (section 4.6).
- `tools/readings.py` applies every word (section 4.4).

### 6.9 Re-running each benchmark

`.github/workflows` holds 71 workflows. The campaign on omni-v25 releases run A of every entry in `scripts/reruns.txt`, then run B, then run C. The letters A, B and C name runs; they are not the four arms.

| Benchmark | Workflow | Native | Cost to the reader |
|---|---|---|---|
| Kubernetes tests of the index | `.github/workflows/benchmark-reps.yml`; `.github/workflows/kind-addons.yml` (KEDA) | the HPA; KEDA and its HTTP add-on | GitHub's own runners, no charge |
| Schedulers and orchestrators | `.github/workflows/kind-orchestrators.yml` (`batch_queue`: kai, koordinator, kueue, volcano, kuberay, vanilla, binpack); `.github/workflows/benchmark-reps.yml` (Kueue and Volcano, two ways); `.github/workflows/kind-crane.yml`, `.github/workflows/kind-godel.yml`, `.github/workflows/kind-cruisekube.yml`, `.github/workflows/kind-group.yml` (Karmada, Open Cluster Management, Armada) | each project as shipped | GitHub's own runners, no charge |
| The five data stores | `.github/workflows/pgbench.yml`, `.github/workflows/kafka.yml`, `.github/workflows/redis.yml`, `.github/workflows/ycsb.yml`, `.github/workflows/sysbench.yml` | the operator's setting, or the vendor's as shipped | GitHub's own runners, no charge |
| The cloud (arms C, D) | `.github/workflows/aks-metered.yml` | AKS and its cluster autoscaler | one's own Azure subscription (`AZURE_CREDENTIALS`), billed |
| The chip (arms A, B) | `.github/workflows/lambda-gpu.yml`, `.github/workflows/lambda-attach.yml` | the card's own firmware limits | one's own Lambda account, billed; a dry run, the default, rents nothing |

Kubernetes repetitions pair the arms on one runner, in an order rotated by repetition (`scripts/kind_paired.sh`; section 4.3), and are scored by `tools/live_reps.py`.

### 6.10 The Python 500 and its C++ twin

Two seeded sets of 500 runs check that the Python, the C++ and the page compute the same mathematics.

**The engine's runs.**

- `tools/engine_runs.py` draws 500 runs from the jump generator: seedₖ = base + k·0x9E3779B9 mod 2³², stream mulberry32.
- Each run is 288 decisions of the brain (RK4), 80 steps of the compass law and one give-back trial judged by the verdict. The tool writes one SHA-256 digest of the receipts.
- The C++ harness (`cpp/tools/engine_runs.cpp`) takes the Python's draws as input and must give the same digest. The page's port, run in node, must give it again (`.github/workflows/engine-runs.yml`, nightly, on GitHub's runners).
- On the omni-v25 record of base 3068730728, 500 of 500 runs agree to 1e-9, with a largest difference of 0.0e+00 (`results/engine_runs/ENGINE_RUNS_500_3068730728.md`). In the record of 6 November, base 3549104563, the C++ harness again gave the same digest on the same draws, 500 of 500 runs agreeing to 10⁻⁹ (`results/engine_runs/ENGINE_RUNS_500_3549104563.md`).

**The core's Monte Carlo.**

- The core (`omnicompass/core.py`) has six states and takes 20 macro steps of 0.1 s, each made of RK4 steps. The command is bounded by |u| ≤ 25.
- It runs native (u = 0, the plant left to its double well) beside Omni-Compass on top.
- A run is conveyed after 5 macro steps in a row in one basin, |U ∓ 1| ≤ 0.10, and certified at 10 (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, 25.4).
- Numpy set, seed 223387268 (`benchmarks/core_evidence.py`): Omni-Compass on top conveyed and certified 500 of 500 runs, its command peaking at 13.93; the plant alone conveyed 476 and certified 427 (`results/core_evidence.json`, its `controlled` and `uncontrolled` sets). With the command, more runs reached and held a basin.
- Jump-generator set, base 1369407155: the C++ twin (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) ran the draws the Python wrote, four ways each. 2,000 of 2,000 run-ways agree to 1e-9 and the digests are one; on that set the plant alone conveyed 467 and certified 431 of 500 (`results/core_runs/CORE_RUNS_500_1369407155.md`).
- `.github/workflows/monte-carlo.yml` runs 1 to 10,000 runs over a reader's own ranges (section 1.7). The input is read as numbers only, never as code.

Both sets are class S: modelled. They show one computation agreeing in three implementations and measure no machine; they are statements about the model, not three-run readings under the key. Agreement between implementations is not evidence that the mathematics fits a real plant; that mapping is open (`docs/FORMAL_STATUS.md`; section 3.14).

### 6.11 verify.py, the verification receipt and the release manifest

`verify.py` takes about 15 to 30 minutes on one core. `--quick` "skips the 20,000-case engine comparison, runs a 1,000,000-decision soak instead of 100,000,000, and replays fewer scenarios" (`verify.py`). The script checks:

- the reference engine's SHA-256;
- that each preregistered file is unchanged, or changed exactly as a recorded amendment says;
- the program fingerprints;
- the C++ core against 500 fixtures;
- the Python/C++ parity tests;
- the seal and the release manifest.

`.github/workflows/verify.yml` runs `verify.py --quick` on every push and pull request, with a read-only token.

**The receipt.** `results/VERIFY_RECEIPT.txt` is the output of `verify.py --quick` at commit 415a18f73d83 on 2026-11-06; its last line reads "VERIFICATION: PASS", and no line reads FAIL. It covers:

- the reference engine's SHA-256, and the preregistered files, each unchanged or amended on record;
- the C++ core against the 500 fixtures, to a largest absolute difference of 2.66e-15;
- the C++ twins against the Python: in each of five profiles, 1,440 directives with 0 discrete mismatches;
- the seal: "all 17 Python/C++ twins unchanged" since their parity was last shown (`results/SEAL.json`; section 3.13);
- the shield's four properties over 100,000 cases, none violated;
- negative controls that show the parity checks can see a fault: a C++ shield altered to stop blocking rollouts during a security block shows 11 mismatches, and a C++ pod autoscaler with 5% in place of 10% tolerance shows 208,204; both are caught.

**The manifest.** `RELEASE_MANIFEST.json` is "the release's one identity". `tools/release_manifest.py` writes it, runs `verify.py --quick` and records the receipt; with `--check` it compares the files against the manifest. The manifest on file is `omni-compass-415a18f73d83`, written at commit 415a18f73d83fe5df1da67ef96a9ec6a0dbc1ec5 at 2026-11-06T10:10:52+00:00. It holds:

- the SHA-256 of the engine, the controller, the shield, the GPU protocol, the preregistration and the test suite, and of the C++ twins through the seal;
- for live sets 20, 21 and 22, the run ids, execution commits and where each run's file digests are kept (`results/live/SET20_RAW_SHA256SUMS_ALL.txt`, `results/live/SET21_ARTIFACTS.json`, `results/live/SET22_ARTIFACTS.json`);
- the mechanism id;
- the receipt file and its own SHA-256 (1dce2272…), marked `passed: true`.

In the receipt's words, it covers the engine, the C++ seal, the GPU protocol, the live evidence and the license.

### 6.12 Checking the page and re-deriving a reading

`.github/workflows/live-engine.yml` rebuilds the page as section 1.4 sets out. A reader checks a copy with the commands of `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, chapter 47:

1. `python3 tools/omni_version.py` prints the engine and its digest, which the page's `<html data-engine>` must match (omni-v25, `cf56fc0a7b707452`).
2. `python3 docs/engine/build_live_engine.py --check` rebuilds the page in memory and writes nothing. It exits 1 if any record differs from the page, and it fails a page whose engine is not the one that stands.
3. `python3 docs/engine/check_live_engine.py` runs the page's brain, compass law and verdict against the Python and the C++. `python3 docs/engine/check_records.py` reproduces every record by an independent path.
4. `python3 -m unittest tests.test_live_monitors` holds every monitor to its wiring (`tests/test_live_monitors.py`).
5. `python3 verify.py` runs everything and must end "VERIFICATION: PASS".

The build's own counts (94 three-run tables played back with 282 runs; 229,338 of 229,338 raw files matching their runs' sums; a LOSS count of its own that differs from the audit's) are given in sections 1.6 and 1.10 (`docs/engine/APPRAISAL.md`).

**Re-deriving one reading.** A tile names its monitor, the monitor its three-run table, and the table its runs. Each link checks by command:

1. `python3 tools/omni_version.py --commit <sha>`: the engine a run's commit carries.
2. `bash scripts/raw_archive.sh open`, with the run's folder name, then `python3 tools/verify_receipt.py` on the opened folder: every file against its sum, and the sums against their signature.
3. `python3 tools/reproduce.py`, with the raw folders it names (`--patterns`) opened: every three-run table of the engine that stands, rebuilt from its raw receipts and compared byte for byte.
4. `python3 tools/verdict_audit.py --check`: every stored word equals the key's.
5. `python3 tools/readings.py --key`: the key in plain text.
6. `python3 verify.py` (or `--quick`), and `python3 tools/release_manifest.py --check`.

### 6.13 What the record establishes

In every layer Omni-Compass takes one position: above the native controller, writing only settings that controller already accepts, in the control plane. Where native has room, the live record reads GAIN: eight of the nine Kubernetes tests of the index; Kafka; Redis and MySQL, which bought speed with memory shown as power given (section 5.3). MongoDB took memory and showed no change in service.

Where native is already at its top (the A100), there is nothing to add (section 5.8). Where Omni-Compass's own processor falls on the work, the record reads LOSS: measured on the plain batch stream and suspected, through the control plane's reads, on the scheduler rigs (sections 5.5 and 5.11). Most other LOSS rows have no written cause, and every LOSS row is named.

The chip's and the cloud's bills are not yet shown to carry more work (sections 5.8 and 5.9). Each statement here can be re-derived from the raw receipts with the commands of sections 6.8 to 6.12. None has yet been re-derived outside The Omni-Compass LLC.

### 6.14 Threats to validity across the programme

The threats particular to the page (section 1.10), the stack (section 2.9), the mechanism (section 3.15), the evidence rules (section 4.8) and the receipts (section 5.13) stand where they are written. Those that run through the whole programme are gathered here.

**Shared machines.**

- Every class L benchmark but the cloud set runs on GitHub's free runners, which differ from run to run.
- On the plain batch rig the kind nodes and Omni-Compass's own process share four cores (`docs/LOSS_CAUSES_2026-11-05.md`).
- On omni-v11's MySQL update workload, throughput moved up 0.3% in every pair of run B and down 0.4% in every pair of run C: a machine effect larger than the change measured (`docs/LIMITATIONS.md`).
- With three pairs a run, the data stores' arm order cannot balance (same source).

Pairing, rotated order, three runs, the 0.5% floor and the reading "the runs disagree" (`tools/readings.py`) bound this noise; they do not remove it.

**kind is not a production cluster.**

- The kind clusters are six workers on one machine. Energy there is a declared model, and node-hours are not a bill (`docs/LIMITATIONS.md`).
- Two costs that a real cluster would put on a separate machine land on the workload here: Omni-Compass's own processor and the control plane's answers to its reads (`docs/LOSS_CAUSES_2026-11-05.md`).

The record does not say what these cost on a production control plane, and there is no production traffic in it (`docs/LIMITATIONS.md`).

**Class S models.** The 1,107 muscles and the seven organisms (`realms/catalog_v5.csv`), the injection grid, the model gate and the beat ladder, the Python 500 and its C++ twin, and the composition are our own models: modelled, never proof (section 4.1). Section 6.5 records a cost that the beat's model counted as power given and that the live batch rig reads as a LOSS on the work.

**The chip.** The class P record is one A10 on omni-v23, whose work and response gauges read the runs disagree, and A100 runs on omni-v21, omni-v18 and omni-v23, in the last two of which nothing was written on the card (section 5.8). No card has run on the engine that stands (`docs/LIMITATIONS.md`), and the card category is pending (`results/OMNI_INDEX.md`).

**One cloud set.** One Azure run of 97 pairs on omni-v18, at the tune-down on the machines alone, with no work counted (`results/live/AKS_STEADY_100_OMNI_V18.md`). It tests neither the engine at the max, nor a second cloud, nor work per dollar.

**Workloads chosen by us.** The loads, windows and native settings are ours. They were preregistered in our own repository and filed with no outside body (`results/OMNI_INDEX.md`). Where native sat at its knee by design, at nine tenths of its measured capacity, a short queue makes the speed ratio large; Kafka's ratio is a hundredfold, and the 94.0% service reading leans on it. In the headline each real category weighs the same.

**Our own code scoring our own results.**

- The rigs, the scorer, the key, the index, the ledger, the audit and the page are The Omni-Compass LLC's own. No outside party has run, reproduced, reviewed or approved these results (`docs/LIMITATIONS.md`).
- The record shows the risk. The verdict audit found 997 printed changes in the standing tables that wore the word's sign, opposite to the raw change, and printed the raw change in their place; no raw value was changed (`results/verdict_audit/DISCREPANCIES.md`).
- The page and the audit count LOSS rows differently (section 1.10).
- The preregistrations carry 99 amendments: 79 written before the runs they apply to, 7 after runs began, and 13 whose heading states no timing (`docs/DEVIATIONS.md`).

The safeguards are mechanical, not independent: byte-for-byte rebuilds from signed receipts, a dated register of amendments, and every LOSS kept. An outside party running the workflows from a fork, or the paired protocol on its own system (`docs/PILOT_PROTOCOL.md`), would remove the dependence.

**Causes not yet written.** Most of the 273 LOSS rows read "not yet written". The queue rows of the scheduler rigs read "suspected, not yet measured". Only the plain batch queue's row carries a measured cause (`docs/LOSS_LEDGER.md`). The rows say what moved, not why.

**Engine churn.** Tables from several engines stand side by side: LOSS rows on omni-v25 and omni-v12, the card on omni-v23, omni-v21 and omni-v18, the cloud on omni-v18 (`docs/LOSS_LEDGER.md`, `results/SITE_NUMBERS.md`). No table is pooled across engines (`results/OMNI_INDEX.md`), and each number is read with its own engine.

**Formal claims.** `docs/FORMAL_STATUS.md` holds four theorems on bounded channels of the forced six-state system over the declared parameter box. It is expressly not a global-stability proof; the discrete bound over the whole box and the mapping onto a real plant are open (section 3.14).

**Documentation drift.**

- `docs/LANDSCAPE.md`, read on 24 October, describes the live page with a third arm, Omni-Compass direct. The current manual shows native and Omni-Compass on top of native, "never Omni-Compass by itself" (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`).
- The descriptions that lag the page itself are listed in section 1.10, and those that lag the stack in section 2.9, item 7.

## References

Every repository file cited in this monograph, by folder, alphabetical. Paths are relative to the repository root.

- (repository root): `DISCLOSURES.md`; `OMNI_V25.json`; `README.md`; `RELEASE_MANIFEST.json`; `verify.py`.
- `.github/workflows/`: `.github/workflows/aks-metered.yml`; `.github/workflows/archive-run.yml`; `.github/workflows/benchmark-reps.yml`; `.github/workflows/eks-metered.yml`; `.github/workflows/engine-runs.yml`; `.github/workflows/front-page.yml`; `.github/workflows/gke-metered.yml`; `.github/workflows/kafka.yml`; `.github/workflows/kind-addons.yml`; `.github/workflows/kind-crane.yml`; `.github/workflows/kind-cruisekube.yml`; `.github/workflows/kind-godel.yml`; `.github/workflows/kind-group.yml`; `.github/workflows/kind-orchestrators.yml`; `.github/workflows/lambda-attach.yml`; `.github/workflows/lambda-gpu.yml`; `.github/workflows/live-engine.yml`; `.github/workflows/monte-carlo.yml`; `.github/workflows/pgbench.yml`; `.github/workflows/redis.yml`; `.github/workflows/reproduce.yml`; `.github/workflows/sysbench.yml`; `.github/workflows/verify.yml`; `.github/workflows/ycsb.yml`.
- `benchmarks/`: `benchmarks/core_evidence.py`.
- `cpp/src/`: `cpp/src/core.cpp`; `cpp/src/governor.cpp`.
- `cpp/tools/`: `cpp/tools/core_runs.cpp`; `cpp/tools/engine_runs.cpp`.
- `deploy/install/`: `deploy/install/omni-compass-cloud.yaml`.
- `docs/`: `docs/BATCH_QUEUE_PREREGISTRATION.md`; `docs/CANONICAL_ENGINE.md`; `docs/CHANGE_CONTROL.md`; `docs/CPU_POWER_PREREGISTRATION.md`; `docs/DEVIATIONS.md`; `docs/ENGINE_PROOFS.md`; `docs/EVIDENCE_INTEGRITY_AUDIT_20261029.md`; `docs/EVIDENCE_LEDGER.md`; `docs/FACTORY_PROFILE.md`; `docs/FORMAL_STATUS.md`; `docs/GPU_PREREGISTRATION.md`; `docs/HOW_TO_READ_THE_RESULTS.md`; `docs/INDUSTRY_LANDSCAPE.md`; `docs/KAFKA_PREREGISTRATION.md`; `docs/LANDSCAPE.md`; `docs/LIMITATIONS.md`; `docs/LOSS_CAUSES_2026-11-05.md`; `docs/LOSS_LEDGER.md`; `docs/MUSCLE_CATALOG.md`; `docs/MYSQL_PREREGISTRATION.md`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `docs/OMNI_COMPASS_MANUAL.md`; `docs/OMNI_COMPASS_OWNERS_MANUAL.md`; `docs/OMNI_V19.md`; `docs/OMNI_V21.md`; `docs/OMNI_V22.md`; `docs/OMNI_V23.md`; `docs/OMNI_V24.md`; `docs/OMNI_V25.md`; `docs/PACE_PREREGISTRATION.md`; `docs/PILOT_PROTOCOL.md`; `docs/POD_START_WAIT.md`; `docs/POSTGRES_PREREGISTRATION.md`; `docs/REDIS_PREREGISTRATION.md`; `docs/REGISTER.md`; `docs/ROBUSTNESS_PREREGISTRATION.md`; `docs/RUN_LEDGER.md`; `docs/SITE_AUDIT.md`; `docs/THE_RECEIPTS.md`; `docs/THE_TUNE.md`; `docs/TRACKING_THEOREM.md`; `docs/WHOLE_SYSTEM_PREREGISTRATION.md`; `docs/wiring_recipes.csv`; `docs/WIRING_VERDICTS.md`; `docs/WORK_PER_BILL.md`; `docs/YCSB_PREREGISTRATION.md`.
- `docs/book/`: `docs/book/THEORY.md`.
- `docs/engine/`: `docs/engine/APPRAISAL.md`; `docs/engine/build_live_engine.py`; `docs/engine/build_standalone.py`; `docs/engine/check_live_engine.py`; `docs/engine/check_records.py`; `docs/engine/LIVE_ENGINE_VERSION.json`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/engine/PAGE_WORD_FOR_WORD.md`.
- `docs/live/`: `docs/live/index.html`.
- `fleet/`: `fleet/harness.py`.
- `hardware/`: `hardware/node_exchange.py`.
- `omni_controller/`: `omni_controller/controller.py`; `omni_controller/gpu_compass.py`; `omni_controller/gpu_governor.py`; `omni_controller/muscles.py`.
- `omnicompass/`: `omnicompass/adapter.py`; `omnicompass/compass_law.py`; `omnicompass/core.py`; `omnicompass/immune.py`; `omnicompass/master.py`; `omnicompass/nervous_system.py`; `omnicompass/shield.py`; `omnicompass/stack_sim.py`; `omnicompass/student_t.py`; `omnicompass/verdict.py`.
- `realms/`: `realms/catalog_v5.csv`; `realms/compass_arm_v5.py`; `realms/harness.py`; `realms/muscle_cards_v5.csv`.
- `results/`: `results/core_evidence.json`; `results/MULTIPLICITY.json`; `results/OMNI_INDEX.json`; `results/OMNI_INDEX.md`; `results/OVERSIGHT.md`; `results/SEAL.json`; `results/SITE_NUMBERS.json`; `results/SITE_NUMBERS.md`; `results/TWO_BILLS.json`; `results/TWO_BILLS.md`; `results/VERIFY_RECEIPT.txt`; `results/WHOLE_SYSTEM.md`.
- `results/core_runs/`: `results/core_runs/CORE_RUNS_500_1369407155.md`.
- `results/engine_runs/`: `results/engine_runs/ENGINE_RUNS_500_3068730728.md`; `results/engine_runs/ENGINE_RUNS_500_3549104563.md`.
- `results/gpu/`: `results/gpu/V21_A100_CAP_ABC.md`; `results/gpu/V23_A100_8CARD_STACKS_ABC.md`; `results/gpu/V23_A10_CAP_FULL_ABC.md`; `results/gpu/V23_A10_STACKS_FULL_ABC.md`.
- `results/gpu/drill-20261024T091235Z/`: `results/gpu/drill-20261024T091235Z/audit-switch.jsonl`; `results/gpu/drill-20261024T091235Z/DRILL.md`; `results/gpu/drill-20261024T091235Z/switch.txt`.
- `results/gpu/run-20261024T091235Z/`: `results/gpu/run-20261024T091235Z/GPU_REPS.md`.
- `results/live/`: `results/live/AKS_STEADY_100_OMNI_V18.md`; `results/live/FRONT_PAGE_STATE.json`; `results/live/GOVERNORS.md`; `results/live/RECIPES.json`; `results/live/SET20_RAW_SHA256SUMS_ALL.txt`; `results/live/SET21_ARTIFACTS.json`; `results/live/SET22_ARTIFACTS.json`; `results/live/V25_ALL_FOUR.md`; `results/live/V25_ARMADA_4W_TOP.md`; `results/live/V25_BATCH.md`; `results/live/V25_BINPACK.md`; `results/live/V25_CAPACITY.md`; `results/live/V25_CRANE_4W_TOP.md`; `results/live/V25_CRUISEKUBE.md`; `results/live/V25_FAIRNESS.json`; `results/live/V25_FAIRNESS.md`; `results/live/V25_FAULTS.md`; `results/live/V25_GODEL_4W_TOP.md`; `results/live/V25_KAI.md`; `results/live/V25_KARMADA_4W_TOP.md`; `results/live/V25_KEDA_CPU_REQUESTS.md`; `results/live/V25_KEDA_REQUESTS.md`; `results/live/V25_KOORDINATOR.md`; `results/live/V25_KUBERAY_4W_TOP.md`; `results/live/V25_KUEUE.md`; `results/live/V25_OCM_4W_TOP.md`; `results/live/V25_REDIS_SHIPPED.md`; `results/live/V25_ROBUST_KILL.md`; `results/live/V25_TRACE_GOOGLE2011.md`; `results/live/V25_VANILLA.md`; `results/live/V25_VOLCANO.md`; `results/live/V25_WANDERING.md`.
- `results/model_gate/`: `results/model_gate/V23_LADDER_CORRECTED.md`; `results/model_gate/V25_VS_V24.md`.
- `results/orchestra/`: `results/orchestra/ORCHESTRA.md`.
- `results/realms_v5/`: `results/realms_v5/REALMS_V5.md`.
- `results/verdict_audit/`: `results/verdict_audit/DISCREPANCIES.md`; `results/verdict_audit/VERDICT_AUDIT.json`; `results/verdict_audit/VERDICT_AUDIT.md`.
- `scripts/`: `scripts/amazon_queue.txt`; `scripts/google_queue.txt`; `scripts/gpu_rented_run.sh`; `scripts/kind_bench.sh`; `scripts/kind_paired.sh`; `scripts/raw_archive.sh`; `scripts/reruns.txt`; `scripts/run_live_local.sh`.
- `systems/`: `systems/README.md`.
- `tests/`: `tests/test_cpp_compass_law_parity.py`; `tests/test_cpp_governor_parity.py`; `tests/test_cpp_immune_parity.py`; `tests/test_cpp_verdict_parity.py`; `tests/test_live_monitors.py`; `tests/test_live_self_update.py`; `tests/test_master_switch.py`; `tests/test_omni_control.py`; `tests/test_readings.py`; `tests/test_verdict_audit.py`.
- `tools/`: `tools/confirm_abc.py`; `tools/core_runs.py`; `tools/engine_runs.py`; `tools/governors_page.py`; `tools/hil_abc.py`; `tools/live_reps.py`; `tools/loss_ledger.py`; `tools/omni_control.py`; `tools/omni_index.py`; `tools/omni_switch.py`; `tools/omni_version.py`; `tools/readings.py`; `tools/release_manifest.py`; `tools/reproduce.py`; `tools/run_cpu_power.py`; `tools/run_realms_v5.py`; `tools/seal.py`; `tools/two_bills.py`; `tools/verdict_audit.py`; `tools/verify_receipt.py`; `tools/whole_system.py`.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
