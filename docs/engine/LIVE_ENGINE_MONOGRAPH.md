# The Omni-Compass Live Benchmark Engine: Purpose, Mechanism, Evidence and Limits

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Dubra Software Inc. / The Omni-Compass LLC, 7 November 2026.

**Validity.** <!-- monograph: validity (tools/monograph_words.py) -->Valid for omni-v26 (`OMNI_V26.json`, digest `75d3c22eed4473b9`, 65 fingerprinted files), the verdict audit's record `57045e3ea8d9f45f` (`results/verdict_audit/VERDICT_AUDIT.json`) and the page built 2026-11-13 05:05 UTC at commit `dcc8f68822b8` (`docs/engine/LIVE_ENGINE_VERSION.json`); every count marked in this monograph is written from its record by `tools/monograph_words.py`, whose `--check` fails when one falls out of step.<!-- end of monograph: validity --> (threat T31)

## Abstract

This monograph is a referee-level account of the Omni-Compass live benchmark engine, one web page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`) that plays back from their raw files the three-run tables of Omni-Compass against its native controllers and runs three parts of the engine in the browser. Omni-Compass is a supervisory control layer: it sits on top of the native controllers, reads their meters and acts in the control plane only; no byte of the work passes through it. Most of what it writes are settings those controllers already accept; section 2.2 names the four kinds that are not: a parked worker's marks, the rollout guard's pause, resume and undo, the scale writes of the arm that runs by itself, and the annotations recording each original (threat T16). The engine that stands is <!-- monograph: engine (tools/monograph_words.py) -->omni-v26, digest `75d3c22eed4473b9`, 65 files<!-- end of monograph: engine -->.

The headline, the Omni index, reads <!-- monograph: index_headline (tools/monograph_words.py) -->GAIN, up 20.0%<!-- end of monograph: index_headline -->: more work and shorter waits on real software on GitHub's machines (class L), not the chip, a cloud or a bill (threat T21). Section 4.8 gives its interval over the three runs and reads it with each product left out: it stays GAIN except without Apache Kafka, where it reads power given (threats T11, T12). Against native the record holds <!-- monograph: loss_against_native (tools/monograph_words.py) -->281<!-- end of monograph: loss_against_native --> LOSS rows, every one shown. The ledger attributes <!-- monograph: flip_split (tools/monograph_words.py) -->21 rows with the fault as their one written cause and 17 queue rows that name it beside a suspected second cause<!-- end of monograph: flip_split --> to one known fault of omni-v25, the web service's autoscaler target flipping at the fail-up's floor (section 3.9): a diagnosis from the runs' own files, on most rigs one run of ten repetitions, that omni-v26's three runs are to test (threat T1). On the chip the work for the bill reads the runs disagree; through the cloud it is not yet read (threat T22).

In the counted arm, at the max under `--law compass`, the six-state core reaches three writes: it can withhold a machine's release; it bounds the depth of the idle floor, which can take the pool below the count the cluster started with; and it drives the rollout guard, which pauses the Deployment whenever the core's alignment U is below 0.85 or a security hold stands, resumes it, and undoes a rollout past its progress deadline on the core's rollback authorisation (section 3.16; threat T4). Every other write comes from the compass law and its guards, the conveyance and the scheduling floor; no ablation of the core has been run. Four theorems bound the core under its own law, which the live adapter does not apply; none is a global-stability proof (threat T20).

## Contents

- [Abstract](#abstract)
- [Notation](#notation)
- [How to read this monograph](#how-to-read-this-monograph)
- [1. Purpose and Scope of the Live Benchmark Engine](#1-purpose-and-scope-of-the-live-benchmark-engine)
- [2. The System Under Test: the Stack, its Native Controllers and the Muscle Catalogue](#2-the-system-under-test-the-stack-its-native-controllers-and-the-muscle-catalogue)
- [3. The Mechanism: the Compass Law, the Supervisory Loop, the Immune System and the Kill Switch](#3-the-mechanism-the-compass-law-the-supervisory-loop-the-immune-system-and-the-kill-switch)
- [4. The Evidence: Classes, Arms, the Three-Run Key and How Every Reading Is Judged](#4-the-evidence-classes-arms-the-three-run-key-and-how-every-reading-is-judged)
- [5. What the Receipts Show on omni-v25: What Omni-Compass Does, What It Gives, What It Does Not Do](#5-what-the-receipts-show-on-omni-v25-what-omni-compass-does-what-it-gives-what-it-does-not-do)
- [6. The Native Tools and Products: What They Do, What They Leave, Where Omni-Compass Sits](#6-the-native-tools-and-products-what-they-do-what-they-leave-where-omni-compass-sits)
- [7. The Page, Section by Section](#7-the-page-section-by-section)
- [8. Reproducing the Engine](#8-reproducing-the-engine)
- [9. Threats to Validity](#9-threats-to-validity)
- [References](#references)

## Notation

Each symbol has one meaning; letters that repeat differ by a tag in brackets, a subscript or their arguments, and a symbol renamed from its source names the source's own (threat T36). The bill's E, W, B and G always carry place and arm, as E(p, a); bare, E and B are the core's states. [n] alone is an outside source.

| Symbol | Meaning | Unit | Value or range | Declared in |
|---|---|---|---|---|
| g, i, Nᵢ | a gauge; a run (1 to 3 for runs A to C); its paired repetitions | count | — | `tools/confirm_abc.py` |
| nᵢ(g), dᵢ(g), SDᵢ(g), CIᵢ(g) | native's mean in run i; the mean paired difference, Omni-Compass minus native; its standard deviation; its 95% interval | the gauge's | — | `omnicompass/student_t.py` |
| Δᵢ(g), Δ̄(g) | run i's raw change (1.1); the three runs' mean | ratio | — | `tools/readings.py` |
| φ, ℳ, b | the floor; the signs of runs moving at least φ; the runs beyond their noise | ratio; —; count | φ = 0.005 | `SIZE_FLOOR` |
| p, a; W, c, B, E; ΔW, ΔB, G | a place, an arm; the work, a cost line, the bill, the work per dollar; their changes and the benefit (section 4.2) | work; dollars; ratio | — | `tools/two_bills.py` |
| s, c, 𝒞, \|c\|, m, M(s); o, n[s] | a test, a category, the real categories, the tests of c, a measure, the measures of s; Omni-Compass's and native's values | — | — | `tools/omni_index.py` |
| Xᵢ(s, m), X̄(s, m); I(s), I(c), I | run i's ratio, above 1 a GAIN, and the value admitted (4.1); the indexes (4.2) | ratio | — | same |
| ℓ, Hℓ(g), H(g) | a layer, its ratio, their product (5.1) | ratio | — | `tools/whole_system.py` |
| R₁ to R₄ | the four realms, as sets of muscles | — | — | `realms/catalog_v5.csv` |
| Cⱼ, yⱼ, uⱼ, ψⱼ, Ψⱼ; Π(v; Ψⱼ), ζⱼ(k) | native controller j, its signal, actuator, setting and cover; the point of Ψⱼ nearest v; the compass law's step | the setting's | — | `omnicompass/compass_law.py` |
| k, tₖ, P | a decision, its instant; the beat | s | P: 10 on site, 60 through a cloud | `FACTORY_BEAT` |
| θ, x | the configuration profile; the supervised system's state | — | — | `docs/FACTORY_PROFILE.md` |
| z = (E, U, I[U], S, B, Ḃ); t, h | the core's states (deviation; alignment, a double well with poles at ±1; memory of misalignment; basin; the bath and its rate); its time and micro step | core time | h = 0.01 | `omnicompass/core.py` |
| u[U], U[auth], sat; K[P], σ, f[U] | the command on U, its bound, the clip; the gain, the target pole, U's drift at u[U] = 0 | — | 25; 12; σ = +1 | `control_command` |
| v[eff], Φ(S), S*; e, Vₑ, ε[h], F̄ | the drive, the basin potential, its stable root; U − σ, e²/2, the sampled loop's largest defect, the bound on \|f[U]\| | — | below | `docs/TRACKING_THEOREM.md` |
| z[obs], ξ(P), push | the observed state; its weight at beat P (3.15); u[U]/U[auth] | — | 0.339 at 60 s; −1 to 1 | `assimilate` |
| ρ*; ρ₀, ρ[min], k[I], k[E] | the target utilisation (3.9); its constants | ratio | ρ* 0.5 to 0.95; fleet 0.829, 0.769, 0.072, 0.487 | `FLEET_MODE` |
| U[gate], push[rel], S[rb] | the gates on U, on the push and on S for rollback | — | fleet 0.85, 0.053, 0.55 | same |
| χ, η, ν, calm; Θ[o], BAND | convergence, basin health, unmet need (the code's kappa, h, nu) and the calm (3.10); organ o's give-back threshold; the living band | — | 0 to 1; pods 0.5, machines 0.7; 0.05 to 0.95 | `omnicompass/nervous_system.py` |
| r, r[lo], r[hi], q, q[prev], q̇, q* | the service reading, its band's ends; its place in the band, its last value, its velocity; the centre | q̇ per s | walls 0.05, 0.95; q* 0.3 | `omnicompass/compass_law.py` |
| λ[v], F, F[max], κ[P], κ[D], τ | the smoothing; the force, its ceiling; the pull; the push against motion; the response time | κ[D], τ in s | 0.3; 1; 1; 3 × 60 s; 60 s | `CompassLaw` |
| T, T[op], T[lo], T[hi], Γ | the HPA's CPU target; the operator's; the cover's ends; the gain of a raised limit | percent; ratio | Γ ≥ 1 | `_gain` |
| COMPASS_UP, _DOWN, _RELEASE | the target's moves a minute per unit force; the force below which a machine may go back | — | 0.10, 0.02, −0.2 | `omni_controller/controller.py` |
| y[trial], y[ref], d[v], se, tol | the costs under the trial and the reference; their mean log difference; its Welch error; the allowance | — | tol = 0.02 | `omnicompass/verdict.py` |
| L[omni], L[native], L[red]; demand, replicas, n[native], ρ[omni], ρ[native] | the gauge over its line, native's twin, its value at the redline's start; the service's demand and replicas, native's replicas, the busy shares | ratio | ρ at most 0.98 | `omnicompass/immune.py` |

**The core's parameters.** The declared box is `PARAMETER_RANGES` (`omnicompass/core.py`, lines 35 to 42), with E at the start in [0, 1] and \|U\| ≤ 1.1; the adapter integrates one point, `STACK_PARAMS` (`omnicompass/adapter.py`).

| Symbol | Role | Box | Integrated |
|---|---|---|---|
| α[E]; β[int], β[ext] | E's decay; the pressures | 4.2; [0, 1] | 3.487 (threat T20); each decision |
| μ; E[max] | U's well; the scale of dE/dt in dU/dt | [2, 6]; [1, 10] | 3.782; 2.0 |
| λ[U], λ[I]; σ₁; δ | the leaks; E's weight in dI[U]/dt; the basin's drive | [0, 0.5], [0.5, 2]; 0.38; [0.01, 1] | 0.0, 0.719; 0.38; 0.705 |
| c[v]; λ₀, λ₁, λ₂ | the drive's amplitude (the code's c), offset and weights | [0.5, 5]; [−2, 2], [0.1, 3], [0, 2] | 1.0; −0.40, 1.55, 1.15 |
| α[s], β[s]; ω[B], Q[B], γ[c] | the basin's terms; the bath's frequency, quality and coupling | [0.05, 0.25]; [0.1, 5], [0.5, 10], 1.0 | 0.12, 0.10; 1.0, 2.5, 1.0 |

The theorems' constants (`results/TRACKING_BOUNDS.json`): <!-- monograph: formal_bounds (tools/monograph_words.py) -->over the declared parameter box F̄ = 16.86 < 25; the sampled-data error contracts by 0.88 a step, ε[h] = 0.0038 over the frozen fixtures (benchmarks/core_evidence.py, seed 223387268, 500 fixtures), and the ultimate bound 0.0315 lies inside the 0.10 basin<!-- end of monograph: formal_bounds -->.

## How to read this monograph

Chapter 9 numbers the threats to validity, T1 to T36. Every count quoted from a record sits between its markers, written by `tools/monograph_words.py`; any other number names its file. A reading is the one key's (section 4.4): the word, the direction in words, the size, the reason; GAIN and LOSS follow what a gauge is for, never its sign, and a resource that rose is power given. Class S is our own modelling, never proof.

## 1. Purpose and Scope of the Live Benchmark Engine

### 1.1 The object: Omni-Compass on top of native

Omni-Compass is a supervisory control layer. It sits on top of the native controllers a stack already runs (an autoscaler, a scheduler, a card's power limit, a database's pool), reads their gauges and writes settings those controllers already accept; section 2.2 names the four kinds of write that are not settings, and in the counted arm only the node pool's marks, the rollout guard's writes and the records occur (section 3.16). No request or byte of the work passes through it (`DISCLOSURES.md`, section 10), and it removes no controller. Every comparison has two sides: *native*, the system with every controller it ships, and *Omni-Compass on top of native*; the arm of Omni-Compass by itself appears only set apart, "in place of a controller", never as a reading against native. The engine that stands is <!-- monograph: engine (tools/monograph_words.py) -->omni-v26, digest `75d3c22eed4473b9`, 65 files<!-- end of monograph: engine --> (`OMNI_V25.json`, as `python3 tools/omni_version.py` prints it); no result is read across engines.

**Naming.** "Governor" names only a product Omni-Compass sits on; what Omni-Compass does is supervisory. Older names that carry the word stay where a lock or a record holds them: the option `--law governor` (the parser's default; the counted arms run `--law compass`), the class `Governor` in `omnicompass/adapter.py`, its twin `cpp/src/governor.cpp` and `omni_controller/gpu_governor.py`, locked by the fingerprint or the seal; the page's monitor 14, "Governor Heartbeat and Lease", and section 5j, "Self-Governed Rendering", which name Omni-Compass's own lease and the page's frame loop; and the appraisal's "governor decisions", the core's steps (section 1.6).

### 1.2 The question the engine exists to answer

The Live Engine Manual asks, in an operator's words, "is it doing what the receipts say, right now, on this body, and would I see it if it were not?". Each run of a three-run table (runs A, B and C, i = 1, 2, 3) holds paired repetitions of native and of Omni-Compass on top of native on the same seed, load and clock; for a gauge g the raw change of run i and the mean the reading is judged on are

  Δᵢ(g) = dᵢ(g) / |nᵢ(g)|,  Δ̄(g) = (Δ₁(g) + Δ₂(g) + Δ₃(g)) / 3.  (1.1)

The reading is a word, never a sign, computed once by `three_run_reading` in `tools/readings.py` (section 4.4). The engine answers four questions; the anchors are the page's (chapter 7).

| | Question | Where it is read |
|---|---|---|
| Q1 | **Hold.** In each place, does any judged gauge read LOSS against native? | `#s-loss`, `#s-status`; `docs/LOSS_LEDGER.md` |
| Q2 | **Benefit.** Which gauges read GAIN, and what resource was given for them? | `#s-bottom`, `#s-board`; `results/OMNI_INDEX.md` |
| Q3 | **Bill.** In each place, does the work done for each dollar rise? | `#s-answer`; `results/TWO_BILLS.md` |
| Q4 | **Fidelity.** Does every number and word on the page equal what the repository's code computes from its raw files? | `docs/engine/APPRAISAL.md` (its floored LOSS tally a builder defect, threat T31); section 8.5 |

Q4 comes first in logic; on the page Q1 leads. Do no harm is judged on the rows against native alone; section 5.11 places their LOSS rows by cause.

### 1.3 What the engine is: one page and its copies

The engine is one page, `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, built by `docs/engine/build_live_engine.py` from the engine that stands and the repository's results, "a monitor of the engine, never a drawing of it". It carries its records as JSON blocks: <!-- monograph: page_records (tools/monograph_words.py) -->the page built 2026-11-13 05:05 UTC carries 25 records; it plays back 96 three-run tables with 288 runs, and 235,257 of 235,257 raw files matched their runs' own sums<!-- end of monograph: page_records -->. It reaches readers as the source page; as the one-file copy `docs/live/index.html`; and as a split copy published by hand at the address in `README.md` (threat T31).

### 1.4 How the page is fed and rebuilt

One workflow, `.github/workflows/live-engine.yml`, rebuilds the page on a push to main that changes the engine, a result or the page's tools, after every successful `front-page` run, every third hour and by hand. Each build opens the raw folders the page plays from the branch `raw`, rebuilds every record, writes the stamp and the one-file copy, and runs the checks of section 8.5; a failed check commits nothing. The page cannot run ahead of the engine; it can run behind its records (threat T31).

### 1.5 The self-update and its stamp

Every copy carries `omniSelfUpdate`, which reads the stamp, `docs/engine/LIVE_ENGINE_VERSION.json`, on main: <!-- monograph: page_stamp (tools/monograph_words.py) -->omni-v26 (digest `75d3c22eed4473b9`), built 2026-11-13 05:05 UTC, 61,647,870 bytes, SHA-256 `af05e12a0ba61f8b…`, page identity `0e0203773b1268a7…`<!-- end of monograph: page_stamp -->, the identity being the SHA-256 of the page with its own tag read as zeros. A copy reads the stamp when it opens and every 24 hours after, and opens a newer page only when its bytes, SHA-256 and identity match and its scripts compile; the script only reads (`tests/test_live_self_update.py`). The stamp shows that a copy is the published page; that its content is right is Q4.

### 1.6 What runs live, what plays back, and the three evidence classes

Three parts of the engine run in the page, ported and held to the Python and the C++ at every build: the core (`omnicompass/core.py`), the compass law and the verdict; <!-- monograph: appraisal_method (tools/monograph_words.py) -->against the Python on seeded inputs (8,000 governor decisions, 48,000 organ grants, 4,800 compass forces, 300 verdict intervals, 400 whole verdict trials, 500 degrees of freedom of the exact t) the largest difference is 2 × 10⁻¹⁵, and 0 grants, 0 verdicts, 0 t values differ; against the C++ twin of the core on 2,000 seeded states, the largest relative difference is 4.4 × 10⁻¹⁶ (derivative), 2.2 × 10⁻¹⁶ (RK4 step)<!-- end of monograph: appraisal_method --> (`docs/engine/APPRAISAL.md`). They drive a stress-test model of sixty muscles and the runs of section 8.3, all class S. Everything else is a record played back, each raw file's SHA-256 matched against its run's own list first. Every monitor states its class (`DISCLOSURES.md`, section 9): **L**, live software on real machines; **P**, a chip's own meter; **S**, the repository's own models (the <!-- monograph: catalogue_size (tools/monograph_words.py) -->1,107 muscles in 70 families<!-- end of monograph: catalogue_size -->, the organisms, the injection grid, the model gate), modelled, never proof, and written by the authors of the law.

### 1.7 Who can run what

Anyone can read the page (the address in `README.md`) and check it (section 8.5), which shows the records are the repository's and the ported mathematics the Python's and the C++'s, not that the runs measured what they claim; run the mathematics (the page's buttons, `tools/engine_runs.py`, `tools/core_runs.py`, class S); run a benchmark (section 8.2, or `bash scripts/run_live_local.sh 3` on one's own kind cluster), a paired comparison on that machine and load; or read one's own system on one's own Prometheus, never a paired benchmark (threat T28). Card rentals go on the founder's word; serving the page to others needs the Enterprise License.

### 1.8 What the engine can answer today, place by place

Omni-Compass runs in one of two places, each with two arms (section 4.2): on the chip, arms A (native) and B; through a cloud, arms C and D.

| Place | Class; engine | Reading | Section |
|---|---|---|---|
| The software end: Kubernetes and five data stores on GitHub's runners | L; <!-- monograph: tables_engine (tools/monograph_words.py) -->omni-v26<!-- end of monograph: tables_engine --> | **the Omni index, <!-- monograph: index_headline (tools/monograph_words.py) -->GAIN, up 20.0%<!-- end of monograph: index_headline -->**: more work and shorter waits, the resources scored beside them; on work and speed alone <!-- monograph: index_service (tools/monograph_words.py) -->GAIN, up 96.5%<!-- end of monograph: index_service --> | 4.8, 5.2 |
| The chip: one rented A10, fully loaded | P; omni-v23 | the bill STEADY, under the floor; the work for the bill: the runs disagree; energy for each request: <!-- monograph: chip_energy (tools/monograph_words.py) -->GAIN in all three of our runs, down 1.3% by the mean (down 1.79%, down 1.35%, down 0.78% by run)<!-- end of monograph: chip_energy --> | 5.8 |
| Through the cloud: Azure AKS | L; omni-v18 | one set at the tune-down on the machines alone; no work counted, so no work per dollar | 5.9 |
| The whole organism, composed | S of L | a second reading, the machines power given | 5.10 |
| Against its native | L | <!-- monograph: loss_against_native (tools/monograph_words.py) -->281<!-- end of monograph: loss_against_native --> LOSS rows, each named, its cause where written | 5.11 |

The kind clusters run on GitHub's rented runners, never called bare metal. The A10's run files record the card (an NVIDIA A10, driver 570.148.08; run 41243352339 on the branch `raw`) and the workflow's default machine `gpu_1x_a10` (`.github/workflows/lambda-gpu.yml`), not whether it is passed through to a virtual machine, so it is called the chip, a rented card. No chip or cloud three-run table stands on the engine that stands (threat T22).

### 1.9 What the engine is not

**Not a sales claim, nor a bill saving yet.** The README's aim, "more work, faster, on fewer machines, for the same energy and the same bill", is not yet a result: the machines are not yet fewer (section 5.10), neither place's bill is resolved, and no dollar figure in the repository is a measured result (`DISCLOSURES.md`, section 2; threat T10). **Not outside review** (threat T29). **Not a benchmark when a knob is turned**: any knob can move any metric either way, and a setting other than the factory profile shows the engine's range, never a result. **Not a proof of stability** (section 3.15).

## 2. The System Under Test: the Stack, its Native Controllers and the Muscle Catalogue

### 2.1 What this chapter fixes

Each layer of the stack, its native controller, its clock and what Omni-Compass may write there (2.2 to 2.4); the muscle catalogue, the stack's modelled counterpart (2.5 to 2.7); the receipts (2.8). A receipt on an older engine than <!-- monograph: engine_name (tools/monograph_words.py) -->omni-v26<!-- end of monograph: engine_name --> names it (threat T23).

### 2.2 Where Omni-Compass sits: the cascade

The native controllers are inner loops, each on its own signal and clock, and Omni-Compass one outer, supervisory loop over them (section 6.8). Native controller Cⱼ moves its actuator uⱼ from its signal yⱼ by its own rule, under a setting ψⱼ an operator gave it:

  uⱼ(t) = Cⱼ(yⱼ(t); ψⱼ).  (2.1)

Omni-Compass leaves every Cⱼ in place and, at its decision instants tₖ, moves the settings:

  ψⱼ(k + 1) = Π(ψⱼ(k) + ζⱼ(k); Ψⱼ),  ζⱼ(k) computed from y(k) = (y₁(k), …, yₙ(k)),  (2.2)

with Π(v; Ψⱼ) the point of the cover Ψⱼ nearest v. A cover runs from native's value toward a limit read live: a pod's CPU limit up to what its machine can spare, less 5%; the replica cap up to one pod under what the machines can place; the CPU target toward 60% of the operator's (section 3.4). Equation (2.2) is a schematic; section 3.16 lists every write. Four kinds of write are not a controller's setting (threat T16):

1. **The node pool** (`scripts/kind_nodepool.sh`) closes a worker with the taint `omnicompass.io/idle=true:PreferNoSchedule`, a preference to the scheduler, not a fence [1], and gives its served pods a negative `controller.kubernetes.io/pod-deletion-cost`, so native's scale-down removes them first [2]; by its header it evicts no pod, though the recipe says "taint and drain" (threat T33). A closed worker can take the count in service below native's.
2. **The rollout guard** (`--rollout-guard`, in every counted kind arm) pauses, resumes and undoes the Deployment's rollout (`_rollout`, section 3.16) [3]; an undo is an actuation.
3. **The arm by itself** writes a workload's replica count through its scale subresource and, after three refusals in a row (`OWN_REFUSALS`), creates native's autoscaler with `kubectl autoscale`; it is never read against native.
4. **The records**: each object is annotated with the operator's value before the first change (`omnicompass.io/original-target-utilization`, `original-replica-range`, `original-cpu-limit`, `paused-by-omni`, `original-own-replicas`), removed on hand-back.

Every write passes through the two-way plug (`Plug`, section 3.4); a lease lets a watchdog restore everything if the process dies (section 3.10). Each layer was measured with the layer under it native (threat T24).

### 2.3 The layers, from the chip to the cloud

#### 2.3.1 The chip: power limit and clock ceiling

**Native** is the card's own firmware limits, through NVML and `nvidia-smi` [4, 5]; no rig runs NVIDIA's DCGM. In the A10 benchmark native runs under the operator's power cap at 70% of the card's top. **Omni-Compass writes** the clock ceiling (`-lgc`, reset by `-rgc`), from the card's own lowest supported clock, read live, to the top (`--clock-min-share` can raise that floor to a share of the top; no rig sets it), never under the card's own busy clock while there is work; and the power limit (`-pl`), never over its starting value (`omni_controller/gpu_compass.py`). A blind reading fails up, a limit it did not write stops its writes, and both are reset on exit.

#### 2.3.2 The host: the kernel's frequency governor

**Native** is cpufreq with its scaling policy [6]. **Omni-Compass would write** `scaling_max_freq` with RAPL as the meter (`tools/run_cpu_power.py`); GitHub's virtual machines cannot write it, so there is no receipt and the whole-system page enters this layer as exactly 1 (threat T24).

#### 2.3.3 The cluster: Kubernetes and its autoscalers

**The rig** is a six-worker kind cluster (kind v0.31.0, Kubernetes v1.35.0), each arm on a fresh cluster, both back to back on one four-core runner, ten paired repetitions a run, three runs a reading (threat T21). **Native:** the default scheduler; the HPA, through KEDA 2.21.0 and its HTTP add-on 0.16.0 on the KEDA tests; Goldilocks 4.16.2 over the VPA 1.7.1 recommender; CruiseKube right-sizing in place. The Cluster Autoscaler runs only on AKS; on kind the machines are made at the start. Karpenter has no receipt; a NodePool's `limits` cap what it may provision for pods that cannot be placed [7, 8], a ceiling, not a size (threat T25). **Omni-Compass writes** the HPA's CPU target and, at its cap, its `maxReplicas`, or KEDA's ScaledObject through a plug; the running pod's CPU limit through its `resize` subresource, so no rollout [9]; the node pool and the rollout guard (`scripts/kind_bench.sh`). The HPA's floor is written only in the strict arm, though the recipe lists "target and floor" (threat T33).

#### 2.3.4 The services: five data stores

Here native is not a loop: each store's setting is set once, by the operator or as shipped, and held through every quiet hour and rush (threat T14). Omni-Compass reads the store's latency once a second and writes one setting through the store's own interface; the index scores the resource each knob holds.

| Store and driver | Native (fixed) | Omni-Compass's setting, its cover |
|---|---|---|
| PostgreSQL 16, PgBouncer 1.22, pgbench | the shipped pool, 20 server connections | `default_pool_size`, 2 to 90 |
| Apache Kafka 3.9.1 | the operator's 2 consumers | the group's size, 1 to 8 |
| Redis, as Ubuntu ships it | 64 MB ceiling, allkeys-lru | `maxmemory`, 16 MB to 512 MB |
| MongoDB 8.0, YCSB | 512 MB cache | WiredTiger's cache, 256 MB to 2,048 MB |
| MySQL 8.0, sysbench | 512 MB pool | `innodb_buffer_pool_size`, 128 MB to 2,048 MB |

MySQL, Redis and MongoDB also run against native as the vendor ships it; Redis then has no ceiling, so the knob is at its limit on native and nothing is written (`docs/REDIS_PREREGISTRATION.md`, amendment 4).

#### 2.3.5 The batch schedulers and the multi-cluster products

Each runs as shipped (`results/live/GOVERNORS.md`): Kueue v0.20.2, Volcano v1.16.0, the KAI scheduler v0.18.6, Koordinator 1.8.0, CruiseKube, Crane 0.11.0 on Kubernetes 1.25.16, KubeRay 1.7.1 with Ray 2.52.0, the Gödel scheduler on Kubernetes 1.24.17, Armada v0.22.14, Karmada v1.19.0 and Open Cluster Management (bundle 1.4.0), the last three on two member clusters. Crane's and Gödel's releases predate in-place resize, alpha in 1.27 [10], so no processor limit moves in their arms (threat T14). Omni-Compass uses its own levers only, reaching Crane's autoscaler through its own object, on a core of its own (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 5); every product but CruiseKube also runs four ways (section 4.6).

#### 2.3.6 The cloud: Azure AKS, with Google and Amazon wired

**Native** is AKS with its Cluster Autoscaler at the default profile. In the one set of section 5.9 (eastus, Standard_D2s_v4) Omni-Compass ran at the tune-down on the machines alone, closing only machines the cloud had made; that rule was struck on 31 October, and Azure's queue now runs uncounted tuning cases at the max (`scripts/azure_queue.txt`; threat T22). **Google and Amazon** are wired the same way and switched on; each set waits on the provider's $0 check, which needs Google's key stored whole and Amazon's account on its paid plan, and none has run; `DISCLOSURES.md`, section 9, says their keys are not stored (threat T33).

### 2.4 The clocks side by side

| Loop | Period | Source |
|---|---|---|
| HPA sync; its metrics | 15 s; 15 s | [11, 12] |
| HPA scale-down window | 300 s by default | [13] |
| Cluster Autoscaler scan | 10 s | [14] |
| KEDA polling | 30 s | [15] |
| AKS: unneeded before deletion | 10 min by default | [16] |
| Omni-Compass's decision: on site; through a cloud | 10 s; 60 s | `docs/OMNI_V24.md` |
| Omni-Compass's fast checks; on a store; on a card | 5 s; 1 s; 2 s | `omni_controller/controller.py`; the preregistrations |

A cascade usually keeps its outer loop slower than its inner loops; on site this stack does not, the 10 s beat being shorter than the HPA's sync (section 3.7; threat T20).

### 2.5 The muscle catalogue

A muscle is one setting on one machine that already has its own control (`docs/MUSCLE_CATALOG.md`). `realms/catalog_v5.csv` holds <!-- monograph: catalogue_size (tools/monograph_words.py) -->1,107 muscles in 70 families<!-- end of monograph: catalogue_size -->; by kind, <!-- monograph: catalogue_kinds (tools/monograph_words.py) -->capacity 539, admission 275, setpoint 174 and power 119<!-- end of monograph: catalogue_kinds -->; by plant, <!-- monograph: catalogue_plants (tools/monograph_words.py) -->`compute_pool` 695, `process_loop` 195, `motion_axis` 116, `energy_storage` 54 and `thermal_zone` 47<!-- end of monograph: catalogue_plants -->; by home realm, <!-- monograph: catalogue_home_realms (tools/monograph_words.py) -->Compute / AI / Cloud 444, Physics / Robotics / Autonomous 137, Energy / Facility / Industrial 249 and Distribution / Specialized 277<!-- end of monograph: catalogue_home_realms -->. <!-- monograph: catalogue_cards (tools/monograph_words.py) -->364 muscles carry a card of their own<!-- end of monograph: catalogue_cards -->. Each muscle alone on its plant, at the max, on omni-v8: <!-- monograph: catalogue_verdicts (tools/monograph_words.py) -->of the 1,107 modelled muscles, 530 read GAIN and earn a wire in; 577 stay native: 421 at their limit on native and 156 the same as native; none read LOSS<!-- end of monograph: catalogue_verdicts --> (`results/WIRING_VERDICTS.csv`); every admission knob is at its limit on native. These are a model's readings on plants we wrote (threat T19).

### 2.6 The seven organisms and the eighth

The organisms are groupings of catalogue rows made in the runners (`tools/run_realms_v5.py`). With R₁ to R₄ the muscles whose realm list includes each realm, the spine is R₁ ∩ R₂ ∩ R₃ ∩ R₄, the tower R₁ ∪ R₂ ∪ R₃ ∪ R₄, and the four stacked keep every duplicate; every muscle sits in all four realms or in one, so

  |R₁| + |R₂| + |R₃| + |R₄| = |R₁ ∪ R₂ ∪ R₃ ∪ R₄| + 3 · |R₁ ∩ R₂ ∩ R₃ ∩ R₄|,  (2.3)

as the counts bear out: <!-- monograph: catalogue_realms (tools/monograph_words.py) -->|R₁| = 540, |R₂| = 404, |R₃| = 480, |R₄| = 484; the spine, in all four, 267; in one realm only, 840; the whole tower 1,107; the four stacked 1,908, and 1,908 = 1,107 + 3 × 267<!-- end of monograph: catalogue_realms -->. With every muscle written at once, <!-- monograph: organisms_v8 (tools/monograph_words.py) -->on omni-v8, seeds 3000 to 3009, each of the 7 organisms read GAIN, fewer misses, under each of its 3 loads; energy STEADY, under the floor, up at most 0.046%; the work moved at most 0.003%; the whole tower under the climb read misses down 0.094 percentage points<!-- end of monograph: organisms_v8 --> (class S). **The orchestra** gathers the muscles that stand for a named scheduler's or orchestrator's knobs: <!-- monograph: orchestra (tools/monograph_words.py) -->55 muscles in one body, on omni-v12: its energy power given, up 25.4% under its own load, up 54.5% under the climb and up 42.4% under work waiting in line<!-- end of monograph: orchestra -->, buying GAIN, fewer misses, under each load, with the work moved under the floor (`results/orchestra/ORCHESTRA.md`); its Kueue body reads STEADY where the live table carries LOSS rows, and the file says "a plant written by the people who wrote the law is not an independent test".

### 2.7 From a muscle to a real knob

`docs/wiring_recipes.csv` gives each family its native controller, wire out, wire in, restore and whether it has run live: <!-- monograph: wiring_families (tools/monograph_words.py) -->70 families, one row each; by its live column 7 have run live, 3 in part, 2 are written, 1 is read only and 57 are modelled<!-- end of monograph: wiring_families -->. Live: the HPA's target (muscle 18), a pod's CPU limit (34), the node pool (66, 67) on kind and AKS, and the stores' pools and caches (283, 1102); Kafka's consumer group has no row of its own (threat T19). Per knob, from every result on file (`docs/WIRING_VERDICTS.md`): <!-- monograph: real_knob_verdicts (tools/monograph_words.py) -->of 26 knob-cases on the real stacks, 22 operator's choice and 4 watch<!-- end of monograph: real_knob_verdicts -->.

### 2.8 Where the receipts are

| Part | Class | Engine | Receipt | Section |
|---|---|---|---|---|
| The chip: A10; A100 | P | omni-v23; omni-v21, omni-v23 (eight cards) | `results/gpu/`, `results/TWO_BILLS.md` | 5.8 |
| The cluster, its add-ons, the stores | L | omni-v25 | `results/OMNI_INDEX.md`, `results/live/V25_*` | 5.2 to 5.7 |
| The batch and multi-cluster products | L | omni-v25 (Koordinator's four ways omni-v12) | `results/live/GOVERNORS.md` | 6.5 |
| The cloud: Azure | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` | 5.9 |
| The catalogue and organisms; the orchestra | S | omni-v8; omni-v12 | `results/realms_v5/REALMS_V5.md`; `results/orchestra/ORCHESTRA.md` | 2.5, 2.6 |
| The layers composed | S | across engines | `results/WHOLE_SYSTEM.md` | 5.10 |

The host, Google and Amazon have no receipt; none comes from production (threat T21).

## 3. The Mechanism: the Compass Law, the Supervisory Loop, the Immune System and the Kill Switch

This chapter states, from the code, what Omni-Compass computes and writes at each decision and what happens when it stops, on <!-- monograph: engine (tools/monograph_words.py) -->omni-v26, digest `75d3c22eed4473b9`, 65 files<!-- end of monograph: engine -->. That engine changes no rule, gain, guard, card or law of omni-v24; it fixes the Kafka wire (`docs/OMNI_V25.md`), and <!-- monograph: model_gate (tools/monograph_words.py) -->the model gate read differs from omni-v25: omni_controller/controller.py against omni-v25 identical on all 12 models, 104 readings and none different (`results/model_gate/V26_VS_V25.md`, class S, modelled)<!-- end of monograph: model_gate -->.

### 3.1 Where the mechanism sits

Every muscle keeps the native controller chapter 2 names for its layer; the docstring of `omnicompass/nervous_system.py` also names the VPA, Karpenter and DCGM, which no counted rig runs (the VPA only as Goldilocks' recommender). When Omni-Compass stops, the native controllers run on the settings then in force, so safety at a stop rests on the hand-back (sections 3.10 to 3.12).

### 3.2 The state, the observation and the control law

The core's state is z = (E, U, I[U], S, B, Ḃ) (`omnicompass/core.py`):

  dE/dt = −α[E]·E + β[int] + β[ext] + v[eff]  (3.1)
  dU/dt = μ·U·(1 − U²) − (dE/dt)/E[max] − λ[U]·U + u[U],  |u[U]| ≤ U[auth] = 25  (3.2)
  dI[U]/dt = (1 − U) − σ₁·E − δ·S − λ[I]·I[U]  (3.3)
  v[eff] = cos(ω[B]·t/2)·c[v]·tanh(λ₀ + λ₁·(U − 0.5) + λ₂·S)  (3.4)
  Φ(S) = α[s]·S²/2 + β[s]·S³/4 − δ·S  (3.5)
  dS/dt = −dΦ/dS = δ − α[s]·S − (3/4)·β[s]·S²  (3.6)
  dB/dt = Ḃ,  dḂ/dt = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B  (3.7)

Integration is classical fourth-order Runge–Kutta, ten micro steps of h = 0.01 in each macro step of 0.1, the command held through all four stages (`macro_step`). Each decision clips the telemetry into nine channels and a clean flag (`observe_vector`); on Kubernetes queue is the pods waiting per replica or the latency pressure, whichever is higher, and clean means no breach and no blind sense for 180 s. The state is blended toward the observation, z ← (1 − ξ)·z + ξ·z[obs], ξ = 0.339 at the reference minute, then evolved one macro step with u[U] = 0 (`assimilate`, `Governor.step`). On U the core evaluates

  u[U] = sat(−f[U](z, t) + K[P]·(σ − U)),  K[P] = 12,  (3.8)

with σ = +1 in the adapter (`control_command`). In the live loop u[U] is never applied and moves no lever; only push = u[U]/U[auth] goes on, to the nervous system. The state U itself gates writes (section 3.16).

### 3.3 The allocation law and the body's calm

The allocation law sets the target utilisation

  ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρ[min], ρ₀)  (3.9)

(`AllocationLaw`); the Kubernetes controller uses `FLEET_MODE` and clamps ρ* between 0.5 and 0.95. Under the parser's default, `--law governor`, the HPA target is 100·min(ρ*, T[op]/100)·Γ, in percent; under `--law compass`, the counted arm's, ρ* is audited and enters only the machine release gate and the idle floor (section 3.16). The body's calm is

  calm = χ·η·(1 − clamp(S/S* − 1, 0, 1))·(1 − clamp(ν, 0, 1)),  (3.10)

with χ = 1 if push ≤ push[rel], else push[rel]/push; η = clamp((U − U[gate])/(1 − U[gate]), 0, 1); and ν = max(0, I[U]) (`scalars`). An organ may give back only while calm ≥ Θ[o], the line is clean and no sense is blind (`authority`).

### 3.4 The compass law

The compass law (`CompassLaw`) is one law for every muscle; on Kubernetes it runs under `--law compass`, as the kind rig's arm `compass` and the cloud install file start it. Every write is clipped to the lever's hard range, its **cover**; the **compass** places the reading r as q = (r − r[lo])/(r[hi] − r[lo]), 0 calm and 1 the service line, walls at 0.05 and 0.95:

  q̇ ← λ[v]·q̇ + (1 − λ[v])·(q − q[prev])/P  (3.11)
  F = F[max]·tanh((κ[P]·(q − q*) + κ[D]·q̇)/F[max])  (3.12)

At q ≥ 0.95, F = F[max] at once (fail up); if F < 0 while q̇ > 0 and q > q*, F = 0. By default κ[D] is critical damping for a first-order muscle of response time τ:

  κ[D] = max(0, 2·√(κ[P]·τ/P) − 1)·P.  (3.13)

The Kubernetes controller sets κ[P] = F[max] = 1, τ = 60 s and λ[v] to 0.3 a minute, evaluates (3.13) at P = 60 s and triples it, "the same push as on every realm muscle" (threat T5). There r is the mean response time between a tenth of the SLO and the SLO, and q = 1 whenever a pod waits anywhere in the cluster, a latency sense is blind, or the 95th percentile reaches the SLO. The HPA target T moves in its cover, from T[lo] = max(10, 0.6·T[op])·Γ to T[hi] = T[op]·Γ, by COMPASS_UP·F toward more pods or COMPASS_DOWN·F toward fewer, times the cover's width, a minute; a machine is asked back only when F < COMPASS_RELEASE with q below q*. The plug (`Plug`) reads the lever before any write, reads back every write, restores the snapshot at the end, and stops writing a lever found at a value it did not write.

### 3.5 Every muscle to its own limit, never past it

At the default dial, the max, each setting moves toward more work, faster, up to the muscle's own limit (`DISCLOSURES.md`, section 3), and never below native with one exception: the idle floor, which carries no test of the dial and can take the pool below the count the cluster started with (section 3.16; threat T4). In the Kubernetes controller the centre is q* = 0.3; the verdict's deepest step is forced to zero, so no give-back trial runs, and apart from the idle floor a machine goes back only above the starting count; T stays in its cover, so, the conveyed gain Γ counted, the autoscaler is never asked for fewer pods than its own rule asks at T[op]; and the pool never falls below the pods' CPU requests with 50% headroom, current use, or two machines. The walls, BAND and the shield's invariants (`omnicompass/shield.py`) keep the cushion; they bound the levers, not the service (threat T15).

### 3.6 The verdict: do no harm as a trigger

A lever slow to reverse moves only after a paired trial (`omnicompass/verdict.py`): the reference is measured, then one step deeper, read on log costs,

  d[v] = mean ln y[trial] − mean ln y[ref],  interval d[v] ± 1.96·se,  allowance ln(1 + tol),  (3.14)

with se Welch's unpooled standard error. An interval wholly above zero is a LOSS, the step undone; otherwise the step stands only if the median and the mean lie within the allowance. The Kubernetes controller runs it with tol = 0.02, 200 requests a phase and a trial every 600 s; at the max it gives nothing back. For an interval straddling zero the fingerprinted file still prints the word retired on 25 October, which the key reads as STEADY.

### 3.7 The beat and the loop

The full decision runs every P = 10 s on site and 60 s through a cloud (`FACTORY_BEAT`), the place read once from the nodes' `providerID`, `--interval` winning when set; the fast checks run every 5 s (the scheduling floor, the waiting-pod hand-back, the pod reflex, the conveyance's clock). The beats were picked by a rule written before a modelled ladder was read (`docs/PACE_PREREGISTRATION.md`, amendments 4 to 6; `results/model_gate/V23_LADDER_CORRECTED.md`, class S; threat T3); their processor cost on a shared runner is read in section 5.5. At a beat of P seconds the observation's weight is

  ξ(P) = 1 − (1 − 0.339)^(P/60),  (3.15)

the core advances P/60 of a macro interval, and dwells and per-minute limits keep their seconds. A decision that raises an error writes nothing more and is audited (`safe_step`).

### 3.8 The immune system and the redline reflex

The redline reflex has two layers: the fail-up at 0.95, before the line, and the immune rule (`omnicompass/immune.py`) when that push is not enough. With the factory constants (a streak of 3, margin 0.05): redlining ⇔ L[omni] > 1 for 3 decisions in a row; stuck ⇔ redlining ∧ (at its limit ∨ L[omni] > L[red]·(1 − 0.05)); stronger ⇔ L[native] < L[omni]·(1 − 0.05). Stuck with native stronger, the lever goes to native for a hold of 10 to 160 decisions; otherwise Omni-Compass keeps it and audits why. On Kubernetes L[omni] = p95/SLO, and native's twin is modelled, not measured (threat T5): with n[native] = ⌈100·demand/T[op]⌉,

  L[native] = L[omni]·(1 − ρ[omni])/(1 − ρ[native]),  ρ[omni] = min(0.98, demand/replicas),  ρ[native] = min(0.98, demand/n[native])  (3.16)

(`_immune_native`). Beside it stands omni-v19's hand-back on a waiting pod (`_pods_wait_handback`): from a fast check, while a pod waits, every target held below native's goes back to native's for 600 s, doubled in a row up to 7,200 s. No omni-v25 receipt reports an immune event as a row.

### 3.9 A known fault of omni-v25: the target's flip at the fail-up's floor

**The rule.** At the wall, two branches of `Controller.step` set a sensed target:

  T ← T[lo] if q ≥ 0.95 and load;  T ← T[hi] if q ≥ 0.95 and not load;  load ⇔ no sense blind ∧ no pod waits in the cluster ∧ the line not clean.  (3.17)

The first is the fail-up. The second, "past the wall, but not from load", reads a waiting pod, anywhere in the cluster, as one waiting for a machine that is gone and returns native's target. The hold of section 3.8 is meant to keep native's target then, but only the fast check starts it, and only while the target stands below T[op]·Γ (`if int(cur) >= back_to: continue`). Where no processor limit is conveyed (Γ = 1), as in the captures below, the decision has already written native's target, so the hold almost never starts and the next decision with no pod waiting fails up again; with Γ > 1 and the line not clean, the decision's reflex writes T[op] (`want_h = min(want, orig)`), below T[op]·Γ, and the fast check can start the hold. Where a batch queue's pods wait on and off, the target flips with the queue.

**The evidence**, from the runs' own files on the branch `raw`: <!-- monograph: flip_evidence (tools/monograph_words.py) -->the target flips between the cover's floor (30%) and native's (50%) every one or two decisions: 304 flips over 30 repetitions of the KAI scheduler's four ways, the hold caught on 21 times; in run 41810759693, repetition 2, 13 target writes in 270 s and the hold only at 274.5 s, with 5 of the queue's pods waiting and all 7 web pods Ready; where the queue ran long the queue finished 0.1% to 6.8% later; after the queue the same arms served 41% to 54% faster than native in all 30 repetitions<!-- end of monograph: flip_evidence --> (`docs/LOSS_CAUSES_2026-11-06.md`, section 1). The autoscaler answers a lower target at once and a higher one only after its 300 s scale-down window [13], so the flips keep extra web pods on room the queue was owed, a trade between muscles the strict form of do no harm forbids. Where the queue waits outside the cluster's pods (Armada and KubeRay on top) the target hardly flips, and the web service's 95th percentile reads lower than native's. The same file rules out the conveyance and the immune comparison as the cause, and records a defect of the conveyance's law: one raise gives a pod 2.2 to 3.2 more cores on a four-core machine, jumping the band's 5-point cushion (threat T1).

**The rows the ledger attributes to it** (`tools/loss_ledger.py`): <!-- monograph: flip_rows (tools/monograph_words.py) -->21 rows on 5 tables carry the fault as their cause, all on the web service (time over the response line 3, alert minutes 5, a slower response 13), and 17 queue rows on 5 tables name it beside the control plane's reads (the queue's finish 5, the jobs' wait, turnaround or count unfinished 12); together 38 of the 281 rows against native, and 0 name omni-v27 as their fix<!-- end of monograph: flip_rows -->. This is a diagnosis with a dose-response pattern (more flips, a larger rise), not an intervention: the KAI scheduler's four ways were read over their three runs, every other rig from "one run of ten repetitions ... a reading of one run, not a three-run reading" (the same page, section 2), and the queue rows name a second, suspected cause beside it.

**The remedy, landed.** omni-v26 (`docs/OMNI_V26.md`, digest `75d3c22eed4473b9`) stands from 7 November with this one change in `omni_controller/controller.py`, the other 64 fingerprinted files omni-v25's bytes: when the decision returns a service's target to native's because pods wait while the target stood below native's, and some of the waiting pods are another workload's (`_others_waiting`: any Pending pod that is not the service's own and not a DaemonSet's), it starts the hand-back's hold itself (`_hold_for_waiting`), so the fail-up is not taken again while the hold runs; where only the service's own new pods wait, omni-v25's rule is kept. It passed the model gate against omni-v25 and `tests/test_neighbour_hold.py` holds it (on the stand-in cluster omni-v25 writes the target 30, 50, 30, 50, 30; omni-v26 writes 30, 50 and holds). What it does on the batch rigs is not yet measured: every benchmark's three runs on omni-v26, which test the attribution, have not landed, so the rows above remain omni-v25's record (threat T1).

### 3.10 The lease and the heartbeat

The Kubernetes controller registers its process id, a staleness limit of max(120 s, 5 × P) and the commands that put every setting back (`omnicompass/master.py`), and renews the lease every decision; a watchdog (`tools/omni_switch.py watchdog`) finds a controller gone or stale and runs those commands, each step tried five times (`RESTORE_TRIES`). **Receipt** (class L, omni-v25, three runs of ten pairs; `results/live/V25_ROBUST_KILL.md`): the controller is killed outright mid-run, the kill marking the same window in both arms. The record reads <!-- monograph: kill_numbers (tools/monograph_words.py) -->75.9 to 83.0 settings commands a repetition written on its own; every setting back at the operator's inside the 60 s allowance in every repetition of all three runs, at a mean of 10.5 to 11.0 s and at most 14 to 17 s; over the response line 14.81% to 15.14% of samples against native's 21.84% to 22.91%<!-- end of monograph: kill_numbers -->. It carries <!-- monograph: kill_losses (tools/monograph_words.py) -->2 LOSS rows in the kill test (`V26_ROBUST_KILL`), no cause yet written for any of them (`docs/LOSS_LEDGER.md`): pod start wait, total (s), LOSS in all three of our runs, up 104.5% to 181.0%; failed requests in the 300 s after the kill (%), LOSS by the mean of our three runs, beyond the noise in 1 of 3, up 3.9% to 9.0%<!-- end of monograph: kill_losses -->. The rows of the 300 s after the kill are the hand-back window itself (threat T6); every other judged row reads GAIN, power given or STEADY, except the 99th percentile, where the runs disagree.

### 3.11 The factory profile and the two restoring controls

The factory profile is one vector θ (rules, gains, margins, the beat, the dial, every card), with θ(k + 1) = θ(k) = θ[factory] after release (`docs/FACTORY_PROFILE.md`); the released one is the engine that stands, <!-- monograph: engine_name (tools/monograph_words.py) -->omni-v26<!-- end of monograph: engine_name -->'s, and the repository stands at steps 1 and 2 of eight toward the best validated one (threat T27). The control panel (`tools/omni_control.py`) offers *Restore factory profile* and *Return to native*, each passing through native: it creates the controller's kill file, waits up to 120 s, then sends SIGTERM, whose handler restores every setting first. The controller, against the panel's docstring, restores on its kill file and stays running in observe mode, so every press is recorded with `handed_back` false although the settings were restored (threat T7).

### 3.12 The kill switch

The kill switch is a third way back, for security (`omnicompass/master.py`): a file (`OMNI_MASTER_OFF`) on which every controller restores at its next decision, `tools/omni_switch.py off` signalling each to restore and exit; an unreadable switch counts as OFF, and while OFF no controller starts. On the panel the kill needs the security role and a reason, re-arming two holders within ten minutes. `tests/test_master_switch.py` checks that one OFF hands both controllers back, and the watchdog both after both are killed. A real card's drill (class P; A100, Lambda run 40079645681, omni-v18; `results/gpu/drill-20261024T091235Z/DRILL.md`) passed 5 of 5 checks, but native already ran both levers at their top and the controller wrote nothing in 3,050 decisions, so it shows the switch path, not a reversal; the two-person arm has run only in unit tests (threat T7).

### 3.13 The audit of every write

`Kube.write` appends a JSON line with the command, the reason and the dry-run flag before it executes; each decision appends its authority record, its compass record and any verdict or immune event. The writer appends its own audit, and no hash chain or signature binds the lines (threat T17).

### 3.14 The C++ twin and the seal

The allocation law's step has a C++ twin, `cpp/src/governor.cpp`, held to it on 60 recorded scenarios of 72 steps in nine cases (five modes at 60 s, power_protect, throughput, fleet, fleet_balanced and fleet_wear; fleet at 15, 10 and 5 s; power_protect at 15 s), with no discrete mismatch and every continuous output within 10⁻¹² (`tests/test_cpp_governor_parity.py`); `verify.py` runs the five modes at 60 s, 20 scenarios under `--quick`. The compass law, the verdict and the immune rule have parity tests of their own. The seal (`results/SEAL.json`): <!-- monograph: seal (tools/monograph_words.py) -->sealed 2026-11-12T23:29:21+00:00: 17 twins; of the 19 Python files it records, the 16 that omni-v26's fingerprint also holds carry the same hash there; 3 lie outside the fingerprint (`fleet/harness.py`, `tools/core_runs.py`, `tools/engine_runs.py`); 7 parts have no twin (`python_only`)<!-- end of monograph: seal -->. It shows that both implementations decide alike on those inputs, not that any rule suits a plant; the Kubernetes controller and the card's device input and output have no twin (threat T19).

### 3.15 The formal status, stated exactly

`docs/FORMAL_STATUS.md` opens: "Not a global-stability proof of the forced six-state system." It holds that the isolated S-flow is the gradient of Φ, and four theorems on e = U − σ (`docs/TRACKING_THEOREM.md`): unsaturated, dU/dt = K[P]·(σ − U) and dVₑ/dt = −K[P]·e²; saturated, with |f[U]| ≤ F̄ < U[auth] over the declared box, Vₑ decreasing wherever e ≠ 0; the sampled-data RK4 loop contracting to an ultimate bound inside the basin; and the admissible box forward invariant. Open: ε[h] and discrete invariance over the whole box, the residual against a real plant, and the mapping of `docs/CANONICAL_ENGINE.md`'s Theorem 5.6 onto the core. Three limits follow from the code: the theorems concern the core under its own law, while the live adapter evolves it with u[U] = 0, a loop the live controller does not close; the integrated point lies outside the box in α[E], and the observed E is clipped to 0 to 1.5 (threat T20); and they reach neither the compass law, the verdict, the immune rule, the plug, the lease nor the beat's interaction with native loops, so they predict none of chapter 5's readings.

### 3.16 From the core to a counted write

The counted Kubernetes arm is the kind rig's arm `compass` (`scripts/kind_bench.sh`, `start_controller`): `--mode nodepool --law compass` at the max, with `--cap-deployments`, `--rollout-guard`, `--thermal-model`, `--security-configmap`, `--sensed`, `--latency-file` and `--slo-ms`. Every write it can make:

| Write | Computed by (`omni_controller/controller.py` unless named) | Does the core enter? |
|---|---|---|
| each sensed HPA's CPU target, at a decision | the compass's force and fail-up in its cover, with (3.17); the waiting-pod hold; the immune rule; the placeable target; the line's reflex, coasting, the autoscaler's window (`Controller.step`) | no: ρ* is audited, then replaced by the compass's target (threat T17) |
| the same target back to native's, at a fast check | `_pods_wait_handback` | no |
| the HPA's `maxReplicas`, at its ceiling | `_replica_room`, `_live_ceiling` | no |
| the HPA's `minReplicas` | gauged only; no `--pod-reflex-writes` | no write |
| serving pods' CPU limit in place (`pods/resize`), at every decision (`Muscles.push`, `_power_cap`, `convey`) and every 15 s on the conveyance's clock (`_convey_due`) | `Muscles.convey`, bounded by the host's busy share, BAND and the namespace quota | no: at the max the core's power-cap request is replaced by 1 |
| the node pool (`scripts/kind_nodepool.sh {n}`), at a decision | one more at the wall; machines first for the pods the fail-up asks (`_placeable_target`); one back below the centre above the starting count; cruise; the idle floor; the reserve; the shield | for a decrease only: `node_release_gate` needs the machine organ's calm ≥ 0.7 and the machines left at or under ρ*; the idle floor passes the same gate, and ρ* bounds its depth |
| the node pool up, at a fast check | the scheduling floor (`floor_step`) | no |
| the Deployment: pause, resume, undo | `Muscles._rollout`, on the whole body's core | yes: paused whenever U < U[gate] (0.85) or a security hold stands, whether or not a rollout is in progress; resumed when change is permitted; undone on the rollback authorisation once `ProgressDeadlineExceeded` |
| the annotations recording each original, removed on hand-back | `Controller`, `Muscles` | only the pause record |
| every setting back to its original | `Controller.restore`, `Muscles.restore` | no |

**What the code says.** Under `--law compass` at the max the six-state core changes no HPA target, replica ceiling or CPU limit, and adds no machine. It reaches the three writes the table marks: a machine's release withheld (`node_release_gate`); the idle floor's depth, bounded by ρ*, the floor able to go below the starting count (threat T4); and the rollout guard. The rigs start no new template's rollout inside the window, and a pause holds back only such a rollout [17], so a pause there moves no running pod, though it is a write. How often each gate decided is in every run's audit (`node_gate`, `idle_floor` and rollout lines), not counted here. An ablation through the model gate (`tools/model_gate.py`) would show the core's effect: the same arm with the gate's two engine checks held open and the rollout guard unwired. None has been run or scheduled (threat T4).

## 4. The Evidence: Classes, Arms, the Three-Run Key and How Every Reading Is Judged

This chapter sets out what counts as evidence, how a difference becomes a word and how the aggregates are composed; sections 8.1 to 8.5 check each step (threat T29).

### 4.1 Evidence classes, and why class S is never proof

`docs/HOW_TO_READ_THE_RESULTS.md` adds to L, P and S two classes, T, a theorem, and V, verified in code, and says: "Only **P** speaks for hardware energy." A class belongs to a gauge, not a table: on kind the energy row is "a declared model, not a meter" (threats T18, T21). Class S is never proof, because a model shows only what its plant allows: "no model refuses a write of the cluster", yet from omni-v19 to omni-v22 the kind rig's own identity refused the pod writes of the arm that ran by itself (`docs/OMNI_V23.md`), a fault only the live files exposed (threat T19). Among the standing rows against native, <!-- monograph: audit_by_class (tools/monograph_words.py) -->class L reads 385 GAIN, 179 power given, 407 STEADY, 281 LOSS and 205 the runs disagree; class S reads 97 GAIN, 10 power given, 160 STEADY, 32 the runs differ and no LOSS<!-- end of monograph: audit_by_class -->; class S there means outside simulators, and the audit holds no class P table.

### 4.2 The four arms, the two bills and the one equation

<!-- monograph: four_arms_table (tools/monograph_words.py) -->
| Arm | What it is | Place and bill | Class | Engine | Receipt |
|---|---|---|---|---|---|
| A | the chip native | one A10 card rented directly; its bill the rental | P | omni-v23 | `results/TWO_BILLS.md`, `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| B | the chip with Omni-Compass on native | the same card, the same rented window | P | omni-v23 | `results/TWO_BILLS.md`, `results/gpu/V23_A10_CAP_FULL_ABC.md` |
| C | the cloud native | Azure (AKS), its own bill | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
| D | the cloud with Omni-Compass on native | Azure (AKS), the same machines, paired with C | L | omni-v18 | `results/live/AKS_STEADY_100_OMNI_V18.md` |
<!-- end of monograph: four_arms_table -->

In arms B and D native's controller stays under the supervisory layer; neither pair ran on the engine that stands (threat T22). For a place p and an arm a, under the same offered load over the same window (`results/TWO_BILLS.md`, `docs/WORK_PER_BILL.md`):

```
B(p, a) = Σ c(p, a, line), over the cost lines inside the place's boundary      E(p, a) = W(p, a) / B(p, a)
G(p) = E(p, Omni-Compass on native) / E(p, native) − 1 = (1 + ΔW) / (1 + ΔB) − 1
G(chip) = E(chip, arm B) / E(chip, arm A) − 1     G(cloud) = E(cloud, arm D) / E(cloud, arm C) − 1
```

On the chip both arms rent the same window, so ΔB ≈ 0 and G ≈ ΔW; through the cloud both move. Places are never added. Today, with `results/TWO_BILLS.md`'s runs 1, 2 and 3:

<!-- monograph: chip_bill_table (tools/monograph_words.py) -->
| Place | Run | Work, ΔW | Bill, ΔB | G, the work for the bill |
|---|---|---|---|---|
| the chip, arm B against arm A | 1 | GAIN, up 1.51% | STEADY, up 0.04% | GAIN, up 1.46% |
| the chip, arm B against arm A | 2 | GAIN, up 0.73% | STEADY, unchanged (0.00%) | GAIN, up 0.73% |
| the chip, arm B against arm A | 3 | LOSS, down 0.70% | STEADY, down 0.01% | LOSS, down 0.69% |
| the chip, three runs | | **the runs disagree** | STEADY, under the floor (the three runs' mean 0.01%) | **the runs disagree** |
| the cloud, arm D against arm C | one set of 97 paired repetitions | not counted | power given, up 1.21%, inside the noise | not read |
<!-- end of monograph: chip_bill_table -->

Runs 1 and 2 served more requests in the rented window and run 3 fewer, so the chip's work for the bill reads the runs disagree (another tool reads the same quantity with another aim: threat T18); the cloud set sent a fixed rate of requests and counted no work, so G(cloud) is not read.

### 4.3 Paired repetitions and the three runs

In each repetition the arms run back to back on one runner, each on a fresh kind cluster, "in an order rotated by repetition", because "separate runners differ by about 15% in p95 on their own" (`scripts/kind_paired.sh`). Run i, of Nᵢ paired differences, reports CIᵢ(g) = dᵢ(g) ± t[0.975; Nᵢ − 1] · SDᵢ(g) / √Nᵢ, the exact Student point [18] (4.303 at 3 pairs, 2.262 at 10); the run is *beyond the noise* when CIᵢ(g) excludes zero. A run holds ten pairs on kind, three on the stores and five on the A10; the cloud holds one set (threats T8, T22). A run's interval measures the noise inside one job; the three runs ask whether a change recurs on other machines at other times.

### 4.4 The one key

`three_run_reading` in `tools/readings.py` is "the only place a word is decided". For a gauge g it takes Δᵢ(g), Δ̄(g), CIᵢ(g), the floor φ = 0.005, ℳ and b, and decides in this order:

1. a run with no value: *no value*; a gauge declared shown: *shown, not judged*; a count that must never rise: "LOSS in at least one of our runs" on any rise, else "GAIN or STEADY in all three of our runs";
2. every run's two values equal to 10⁻⁹ of native's: **STEADY, the same**;
3. ℳ holds both signs: **the runs disagree**;
4. |Δ̄(g)| < φ: **STEADY, under the floor**;
5. otherwise the word w of the table below: "w **in all three of our runs**" where b = 3 and the signs agree, else "w **by the mean of our three runs**, beyond the noise in b of 3".

| What the gauge is for | It fell | It rose | Examples |
|---|---|---|---|
| work done | LOSS | GAIN | requests inside the response line |
| time waited, missed or failed | GAIN | LOSS | response time, failed requests, pod start wait |
| a resource spent or held | GAIN (a cut) | power given | machines, energy, memory, replicas, the bill |
| work per resource | power given | GAIN | work per energy |
| a count that must never rise | GAIN or STEADY, if no run rose | LOSS on any rise | lost messages |

So the sign never decides, and a run under the floor cannot make a disagreement. "In all three" turns on sign and interval, not on each run's own floor: on the A10 at full load, <!-- monograph: chip_card_energy (tools/monograph_words.py) -->the card's energy GAIN in all three of our runs, down 0.31%, down 0.63% and down 1.48% by run; run 1's own word STEADY, under the floor<!-- end of monograph: chip_card_energy -->. Strength sits beside the word: strong, moderate, weak or inconclusive as all, all but one, one or none of the runs stand beyond their noise on the mean's side; unresolved where they disagree. Among the standing rows against native, <!-- monograph: audit_inconclusive (tools/monograph_words.py) -->115 LOSS and 91 GAIN rows are inconclusive, and 205 rows read the runs disagree<!-- end of monograph: audit_inconclusive -->; they also hold <!-- monograph: audit_steady_kinds (tools/monograph_words.py) -->567 STEADY rows: 352 exactly the same and 215 under the floor<!-- end of monograph: audit_steady_kinds -->. Only "in all three" carries an error bound, 2 × 0.025³ ≈ 3.1 × 10⁻⁵ under no true difference and independent runs (threat T9).

### 4.5 A worked example: four readings where the sign and the word differ

The noisy-neighbour test puts a second workload on the same workers (`results/live/V25_FAIRNESS.md`, omni-v25):

<!-- monograph: fairness_table (tools/monograph_words.py) -->
| Gauge (what it is for) | Raw change, runs A / B / C | Raw mean of three | Reading | Strength |
|---|---|---|---|---|
| HPA replicas, mean (resource spent or held) | up 2.41% / up 3.95% / up 2.00% | up 2.79% | **power given by the mean of our three runs, beyond the noise in 0 of 3** | inconclusive |
| failed requests (%) (time waited, missed or failed) | down 26.00% / down 30.71% / up 4.82% | down 17.30% | **the runs disagree** | unresolved |
| response time (ms), mean (time waited, missed or failed) | down 2.52% / down 0.36% / down 7.97% | down 3.62% | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** | inconclusive |
| response time (ms), 95th percentile (time waited, missed or failed) | up 8.41% / up 11.17% / up 4.71% | up 8.10% | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** | inconclusive |
<!-- end of monograph: fairness_table -->

The replicas rose: power given, more pods kept serving. Failed requests fell far past the floor: GAIN, inconclusive since no run is beyond its own noise. The mean response time would read GAIN by its sign, but its runs moved both ways by φ or more: the runs disagree, never averaged. In the 95th percentile run A's fall is under the floor and makes no disagreement, so it reads LOSS by the mean of our three runs, up by the size the table prints, the slowest twentieth waiting longer; it is why the index reads this test LOSS (section 5.4).

### 4.6 The verdict audit and its four comparisons

The batch rigs run a product two ways or four: *nativebare*, the organism alone; *native*, the product as shipped; *compassbare* and *compass*, Omni-Compass on top of each (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6). The verdict audit (`tools/verdict_audit.py`) files every table under one comparison: against its native (plain tables, `_4W_TOP`, `_4W_BARE`: compass against native, compassbare against nativebare); in place of a controller (`_4W_VS`, `SOLO`); the orchestrator's own (`_4W_ORCH`, Omni-Compass in neither arm); two changes at once (`_4W_BOTH`). Only the first changes one thing, so only it judges *do no harm*. The audit recomputes every judged row with the one key, its `--check` failing on any stale or differing word. Its record holds <!-- monograph: audit_tables (tools/monograph_words.py) -->420 three-run tables (100 standing, 258 superseded, 60 the road, 2 taken out); 12,806 of their 17,729 rows recomputed by the one key, 0 stored readings the key reads otherwise and 0 Markdown readings unlike their JSON twin<!-- end of monograph: audit_tables -->; <!-- monograph: audit_standing (tools/monograph_words.py) -->63 standing tables against native; 80 of the 100 standing tables on omni-v26, 20 not yet run again on it<!-- end of monograph: audit_standing -->:

<!-- monograph: audit_counts_table (tools/monograph_words.py) -->
| Comparison | GAIN | power given | STEADY | LOSS | the runs disagree | shown |
|---|---:|---:|---:|---:|---:|---:|
| against its native | 482 | 189 | 567 | 281 | 205 | 654 |
| in place of a controller | 110 | 29 | 72 | 70 | 18 | 137 |
| the orchestrator's own | 28 | 10 | 86 | 76 | 35 | 99 |
| two changes at once | 57 | 25 | 43 | 96 | 14 | 99 |

The first row also carries 32 *the runs differ* and 201 *tuning* (a tuning workload is shown and never counted).
<!-- end of monograph: audit_counts_table -->

It reads `results/live/` and `results/orchestrator/` only, so the card's tables stand outside it and the ledger (threat T32).

### 4.7 The Omni index and how it is composed

`tools/omni_index.py` turns measure m of test s in run i into a ratio Xᵢ(s, m), above 1 a GAIN, from Omni-Compass's value o and native's n[s]: o / n[s] for work, n[s] / o for the 95th percentile, energy and the resource held. A measure enters only as its reading allows:

  X̄(s, m) = (X₁(s, m) · X₂(s, m) · X₃(s, m))^(1/3) where the reading is GAIN, LOSS or power given, in all three of our runs or by the mean; else 1.  (4.1)

Energy enters as measured only where a meter read it, elsewhere as 1. With M(s) the measures of test s, |c| the tests of category c and 𝒞 the real categories,

  I(s) = (∏ over m ∈ M(s) of X̄(s, m))^(1/|M(s)|),  I(c) = (∏ over s ∈ c of I(s))^(1/|c|),  I = (∏ over c ∈ 𝒞 of I(c))^(1/|𝒞|),  (4.2)

the headline being I − 1, each category weighted alike: a geometric mean of normalised ratios, independent of the system they are normalised to [19] but blind to the totals behind them [20]. A combined number below 1 reads LOSS only where its service reading, work and speed alone, is below 1 too, otherwise power given (`index_word`). As a check, <!-- monograph: index_check (tools/monograph_words.py) -->(1.222 × 0.982 × 3.211 × 0.951 × 0.929 × 0.875)^(1/6) ≈ 1.200<!-- end of monograph: index_check -->, the headline <!-- monograph: index_headline (tools/monograph_words.py) -->GAIN, up 20.0%<!-- end of monograph: index_headline -->. The index page calls Kafka's speed ratio "a hundredfold (native's queue grew at nine tenths of its capacity by design)", and states the admission rule more narrowly than the code (threats T10, T33).

### 4.8 The headline's uncertainty: an interval and a leave-one-category-out reading

Both are computed by `tools/monograph_words.py` with `tools/omni_index.py`'s own functions, refused unless the three runs' own indexes compose to the headline exactly; the index's page does not print them yet (threat T12). **The interval:** <!-- monograph: index_interval (tools/monograph_words.py) -->GAIN, up 20.0%, the three runs as replicates: each run's own index (every measure entering at that run's ratio where its three-run reading is judged, else 1; composed as the headline is) reads run A up 19.2%, run B up 21.6% and run C up 19.1%, and the 95% interval of their mean runs from up 16.5% to up 23.5% (Student t on 2 degrees of freedom, t = 4.303, as `evidence()` in `tools/readings.py` reads a gauge's runs, taken on the log of each run's index so that its centre is the headline); it measures how far the three runs' own indexes spread, not the choice of categories, their equal weights or which measures the key admits<!-- end of monograph: index_interval -->. Such a spread beside a summary follows benchmarking practice [21]; it is conditional on the measures each run admitted, chosen by the same runs, and takes the runs as independent. **Each category left out in turn**, the rest composed by (4.2):

<!-- monograph: index_leave_one_out (tools/monograph_words.py) -->
- All 6 categories: GAIN, up 20.0%
- Without Kubernetes, the other 5: GAIN, up 19.5%
- Without PostgreSQL behind PgBouncer, the other 5: GAIN, up 24.9%
- Without Apache Kafka, the other 5: power given, the index down 1.5% (its service reading GAIN, up 28.8%: the resources put in outweigh what they bought on the index's equal weights, so the word is power given, not LOSS)
- Without Redis, the other 5: GAIN, up 25.7%
- Without MongoDB under YCSB, the other 5: GAIN, up 26.3%
- Without MySQL under sysbench, the other 5: GAIN, up 27.8%
<!-- end of monograph: index_leave_one_out -->

The headline's word GAIN rests on Apache Kafka: without it the rise in work and speed survives, the rise of the combined number does not. This reads the choice of categories, which the interval does not (threat T11).

## 5. What the Receipts Show on omni-v25: What Omni-Compass Does, What It Gives, What It Does Not Do

### 5.1 The engines, the places and the key

The software end ran on <!-- monograph: tables_engine (tools/monograph_words.py) -->omni-v26<!-- end of monograph: tables_engine -->, the chip on omni-v23 and the cloud on omni-v18 (threat T22); no table is pooled across engines, and each row is worded by the one key with the audit's strength beside it.

### 5.2 The headline: the Omni index

The Omni index reads **<!-- monograph: index_headline (tools/monograph_words.py) -->GAIN, up 20.0%<!-- end of monograph: index_headline -->**: more work inside the response line and a shorter 95th percentile, the resources taken scored beside them (`results/OMNI_INDEX.md`), over <!-- monograph: index_tests (tools/monograph_words.py) -->26 tests from 14 three-run tables (14 tables on omni-v26): Kubernetes 9; PostgreSQL behind PgBouncer 3; Apache Kafka 3; Redis 3; MongoDB under YCSB 4; MySQL under sysbench 4<!-- end of monograph: index_tests -->, class L on GitHub's shared runners (threat T21); section 4.8 gives its interval and its reading with each category left out. The second readings: on work and speed alone, <!-- monograph: index_service (tools/monograph_words.py) -->GAIN, up 96.5%<!-- end of monograph: index_service -->; with the modelled energy scored, as declared on 4 October, <!-- monograph: index_resource (tools/monograph_words.py) -->GAIN, up 20.5%<!-- end of monograph: index_resource -->; the composition of section 5.10, class S.

### 5.3 By product: the categories

Work is Omni-Compass's over native's; speed and the resource held are native's over Omni-Compass's.

<!-- monograph: index_categories_table (tools/monograph_words.py) -->
| Product | Tests | Index | Service reading (work and speed) | Work | Speed (native's 95th percentile against Omni-Compass's) | Resource held (native's against Omni-Compass's) |
|---|---:|---|---|---|---|---|
| Kubernetes | 9 | GAIN, up 22.2% | GAIN, up 68.4% | GAIN, 18.9% more | GAIN, native's 82.0% longer | GAIN, a cut: native's machines in service 2.3% above |
| PostgreSQL behind PgBouncer | 3 | power given, the index down 1.8% | GAIN, up 0.5% | STEADY, under the floor (0.5%) | GAIN, native's 0.6% longer | power given: native's connections 7.8% below |
| Apache Kafka | 3 | GAIN, up 221.1% | GAIN, up 1,524.3% | GAIN, 18.9% more | GAIN, native's 22,090.3% longer | power given: native's consumers 59.7% below |
| Redis | 3 | power given, the index down 4.9% | GAIN, up 93.7% | GAIN, 21.8% more | GAIN, native's 208.1% longer | power given: native's memory ceiling 78.2% below |
| MongoDB under YCSB | 4 | power given, the index down 7.1% | STEADY, under the floor (0.0%) | STEADY | STEADY, under the floor (0.1%) | power given: native's cache 25.5% below |
| MySQL under sysbench | 4 | power given, the index down 12.5% | GAIN, up 7.9% | GAIN, 4.0% more | GAIN, native's 12.0% longer | power given: native's buffer pool 49.6% below |
<!-- end of monograph: index_categories_table -->

For the system: Kafka's extra consumers drain a queue that grows under native, run by design at nine tenths of its capacity, hence the very large speed ratio; PgBouncer held more connections for a service gain just over the floor; Redis's memory bought work and speed; MongoDB's larger cache bought no service change; MySQL's buffer pool grew more than the service it bought. The four stores read power given because at the max a resource that rose is power given, which the index counts below 1; in none does a scored work or speed measure read LOSS. Energy is shown, not scored (threat T18).

### 5.4 Real Kubernetes: the tests, and the one that reads LOSS

<!-- monograph: index_kubernetes_table (tools/monograph_words.py) -->
| Test | Index | Work | Speed (native's 95th percentile against Omni-Compass's) | Machines in service | Energy (a declared model) |
|---|---|---|---|---|---|
| the steady load (`V26_STEADY`) | GAIN, up 31.5% | STEADY, equal by design | GAIN, native's 198.7% longer | STEADY, the same | STEADY, under the floor (the three runs' mean 0.30%) |
| demand that wanders (`V26_WANDERING`) | GAIN, up 27.6% | not taken | GAIN, native's 107.8% longer | STEADY, the same | STEADY, under the floor (the three runs' mean 0.11%) |
| all four in one run (`V26_ALL_FOUR`) | GAIN, up 28.6% | GAIN, 41.3% more | GAIN, native's 93.4% longer | STEADY, the same | STEADY, under the floor (the three runs' mean 0.07%) |
| the noisy neighbour (`V26_FAIRNESS`) | LOSS, down 2.6% | not taken | LOSS, native's 7.5% shorter | STEADY, the same | STEADY, under the floor (the three runs' mean 0.15%) |
| the four faults (`V26_FAULTS`) | GAIN, up 34.3% | not taken | GAIN, native's 142.3% longer | STEADY, under the floor (the three runs' mean 0.01%) | STEADY, under the floor (the three runs' mean 0.02%) |
| the batch queue (`V26_BATCH`) | GAIN, up 10.2% | not taken | GAIN, native's 8.8% longer | GAIN, a cut: native's machines 23.0% above | GAIN, a cut: native's energy 14.7% above (shown, not scored) |
| the Google trace of 2011 (`V26_TRACE_GOOGLE2011`) | GAIN, up 37.4% | not taken | GAIN, native's 159.2% longer | STEADY, the same | STEADY, under the floor (the three runs' mean 0.15%) |
| KEDA on the CPU target and requests in flight (`V26_KEDA_CPU_REQUESTS`) | GAIN, up 16.8% | not taken | GAIN, native's 59.4% longer | STEADY, the same | power given: native's energy 1.5% below (shown, not scored) |
| KEDA's HTTP add-on (`V26_KEDA_REQUESTS`) | GAIN, up 22.0% | not taken | GAIN, native's 81.4% longer | STEADY, the same | power given: native's energy 1.7% below (shown, not scored) |
<!-- end of monograph: index_kubernetes_table -->

In every test but the noisy neighbour the 95th percentile was shorter: users at the tail waited less. Only the batch queue moved the machines, a cut, though its queue finished later (section 5.5). In the noisy neighbour (section 4.5) the index's LOSS comes from the first application's 95th percentile: more replicas went in, power given in all three of our runs, and the tail did not shorten, while failed requests and alert minutes fell. Its table carries <!-- monograph: fairness_losses (tools/monograph_words.py) -->4 LOSS rows in the noisy neighbour (`V26_FAIRNESS`), no cause yet written for any of them (`docs/LOSS_LEDGER.md`): response time (ms), 95th percentile, LOSS by the mean of our three runs, beyond the noise in 0 of 3, up 4.7% to 11.2%; pod start wait, total (s), LOSS by the mean of our three runs, beyond the noise in 1 of 3, up 9.7% to 22.6%; second app: response time (ms), 95th percentile, LOSS by the mean of our three runs, beyond the noise in 0 of 3, up 0.4% to 11.9%; second app: failed requests (%), LOSS by the mean of our three runs, beyond the noise in 0 of 3, up 2.0% to 3.3%<!-- end of monograph: fairness_losses -->.

### 5.5 The LOSS rows inside the index's own tables

In the ledger, <!-- monograph: index_loss_rows (tools/monograph_words.py) -->21 of the 281 rows against native sit in the index's own 14 tables: the pod start wait 10; failed requests 1; alert minutes 1; a slower response 8; the queue's finish 1; 3 of the 21 on a measure the index scores (the noisy neighbour's response time (ms), 95th percentile, PostgreSQL behind PgBouncer's select: 95th percentile and MongoDB under YCSB's burst: 95th percentile)<!-- end of monograph: index_loss_rows -->. The strong ones: <!-- monograph: index_loss_strong (tools/monograph_words.py) -->pod start wait, total (s) in all four in one run, LOSS in all three of our runs, up 106.8% to 166.7%; batch: queue finished (s) in the batch queue, LOSS in all three of our runs, up 2.4% to 3.1%; pod start wait, total (s) in the Google trace of 2011, LOSS in all three of our runs, up 162.6% to 173.1%; pod start wait, total (s) in demand that wanders, LOSS in all three of our runs, up 108.2% to 133.3%<!-- end of monograph: index_loss_strong -->; the rest are moderate, weak or inconclusive. The headline is not the whole record; the ledger is (threat T10).

**The pod start wait.** The total sums over the pods started; where it reads LOSS, pods started read power given and the mean wait of one pod mostly the runs disagree, so whether each pod started slower these runs do not resolve. The cause read on omni-v10 (`docs/POD_START_WAIT.md`) is not carried onto an omni-v25 row unread (threat T2).

**The one measured cause** (`docs/LOSS_CAUSES_2026-11-05.md`, section 1). On the plain batch queue's rig every kind node and Omni-Compass share the runner's four cores: <!-- monograph: beat_load_cause (tools/monograph_words.py) -->Omni-Compass's own processor read 0.075 to 0.103 of a core over each window at the 10 s beat, against 0.014 to 0.016 at omni-v21's 60 s beat; the batch pods ran on about 3.6 of the runner's four cores, so about 2.5% of their processor went to it, the size of the queue's rise<!-- end of monograph: beat_load_cause -->. It moved no machine, pod or limit during the queue, and its target never flipped. The 10 s beat was picked on a model that counted this processor as power given (`docs/OMNI_V24.md`); the remedy, its own processor counted in the body's load on a shared host, is written, not made (threat T3).

### 5.6 The cluster's LOSS rows by gauge, and the stores'

<!-- monograph: loss_cluster_by_gauge (tools/monograph_words.py) -->35 on the cluster's own tests: the pod start wait 19 (all four in one run 2, the batch queue 2, CruiseKube 1, CruiseKube with the recorder 1, the noisy neighbour 1, the four faults 1, the extended faults 2, Goldilocks 2, KEDA on the CPU target and requests in flight 1, the kill test 1, the long run 2, the Google trace of 2011 1, demand that wanders 2); failed requests 3 (CruiseKube 1, the noisy neighbour 1, the kill test 1); alert minutes 1 (the batch queue 1); a slower response 8 (CruiseKube 3, CruiseKube with the recorder 3, the noisy neighbour 2); the queue's finish 1 (the batch queue 1); work done 3 (the capacity test 3)<!-- end of monograph: loss_cluster_by_gauge -->. Both CruiseKube sets answer more slowly with Omni-Compass on top of its rightsizing (`V25_CRUISEKUBE_RECORDER` counting a worker CruiseKube marks overloaded as in service), and the capacity test does less work inside the line under its 2- and 3-core quotas. Only the batch queue's finish carries a cause. **The stores:** <!-- monograph: loss_stores (tools/monograph_words.py) -->18 on the stores' tables: 6 on the counted tables (MongoDB under YCSB 4, PostgreSQL behind PgBouncer 2) and 12 on the service-objective and shipped-native sets (MongoDB under YCSB 5, MySQL under sysbench 4, PostgreSQL behind PgBouncer 3)<!-- end of monograph: loss_stores -->: <!-- monograph: loss_stores_range (tools/monograph_words.py) -->each LOSS by the mean of our three runs, 18 inconclusive; the 18 response times longer by the mean of the three runs, up 0.57% to up 57.70%<!-- end of monograph: loss_stores_range -->. On Redis as shipped Omni-Compass writes nothing, so that row measures the rig's run-to-run variation (threat T8). No store row carries a cause.

### 5.7 The oversight line: the minutes a person would be paged

An alert minute is a whole minute whose 95th percentile, failed requests counted over, was over the line, the minute an on-call page would be open; fewer is GAIN (`results/OVERSIGHT.md`). By the record, <!-- monograph: oversight (tools/monograph_words.py) -->over 37 omni-v26 Kubernetes tests the alert minutes of a repetition, summed, fall from 349.9 on native to 311.5 with Omni-Compass on top: GAIN in all three of our runs, down 11.0%<!-- end of monograph: oversight -->:

<!-- monograph: oversight_runs_table (tools/monograph_words.py) -->
| Run | Native → Omni-Compass, summed | Reading | 95% interval, minutes fewer |
|---|---|---|---|
| A | 348.90 → 308.17 | GAIN, down 11.7% | 26.69 to 54.77 |
| B | 393.97 → 349.87 | GAIN, down 11.2% | 31.08 to 57.12 |
| C | 306.93 → 276.37 | GAIN, down 10.0% | 20.43 to 40.70 |
<!-- end of monograph: oversight_runs_table -->

Test by test, <!-- monograph: oversight_count (tools/monograph_words.py) -->fewer in 13 tests, falling to none in 3; the same in 2 (CruiseKube and CruiseKube with the recorder); more in 22<!-- end of monograph: oversight_count -->. Every test with more is the plain batch queue or a product under the batch stream; among them, <!-- monograph: oversight_loss_all_three (tools/monograph_words.py) -->1 test reads LOSS in all three of our runs, more minutes over the line: Open Cluster Management on the organism alone (four ways), up 12.3%<!-- end of monograph: oversight_loss_all_three -->. Where the target flips, those alert-minute rows carry the fault of section 3.9. The sum weighs each test by its own minutes, and <!-- monograph: oversight_largest_share (tools/monograph_words.py) -->the long run holds 20.9% of native's minutes, the largest share of any test<!-- end of monograph: oversight_largest_share --> (threat T13); it counts minutes, not heads, and the page's <!-- monograph: oversight_example (tools/monograph_words.py) -->7%<!-- end of monograph: oversight_example --> people share is an example with no receipt.

### 5.8 The chip: arm A against arm B (class P)

One rented A10, native's power cap at 70% of the card's top, the full load, three runs of five pairs read by the card's own meter, on omni-v23 (`results/gpu/V23_A10_CAP_FULL_ABC.md`; threat T22). Energy for each request served reads <!-- monograph: chip_energy (tools/monograph_words.py) -->GAIN in all three of our runs, down 1.3% by the mean (down 1.79%, down 1.35%, down 0.78% by run)<!-- end of monograph: chip_energy -->, a cut measured at the chip, and the card's energy reads as section 4.4 gives it. The work for the bill reads the runs disagree (section 4.2). The 95th percentile reads <!-- monograph: chip_p95 (tools/monograph_words.py) -->the runs disagree (run 1 shorter by 3.68%, run 2 shorter by 1.38%, run 3 longer by 2.25%)<!-- end of monograph: chip_p95 -->; the receipt prints no count of writes (threat T9). **Inside the organisms** the records count the <!-- monograph: card_writes (tools/monograph_words.py) -->writes of the card-side process in the Omni-Compass arms, run by run: the eight-card machine 0 in 15, 0 in 12, 0 in 12 arms; the fully loaded A10 0 in 62, 0 in 62, 0 in 62 arms<!-- end of monograph: card_writes -->: with nothing written the arms were one system, so the A10's card LOSS rows (the work in three cells, the 95th percentile in four, by the mean, beyond the noise in no run) are the card's drift (threat T18).

**The A100.** On omni-v21 an A100 ran three runs of five pairs at native's 70% cap and at full load (`results/gpu/V21_A100_CAP_ABC.md`, `V21_A100_CAP_FULL_ABC.md`): at the cap the work STEADY, the same, and the energy STEADY, under the floor; it carries <!-- monograph: a100_v21_losses (tools/monograph_words.py) -->4 LOSS rows, each LOSS by the mean of our three runs, beyond the noise in 0 of 3: at the operator's cap, response time, mean (ms) (run A up 1.9%, run B down 0.1%, run C up 0.8%); response time, 99th percentile (ms) (run A up 1.7%, run B down 0.3%, run C up 0.5%); at the full load, requests not served (run A up 2.2%, run B down 0.1%, run C up 0.1%); response time, 95th percentile (ms) (run A up 1.5%, run B up 0.1%, run C up 0.1%)<!-- end of monograph: a100_v21_losses -->: slightly slower answers and a few more requests not served. On omni-v18 one run of ten pairs, the power limit already at the card's 400 W top, read every service gauge STEADY with nothing written: both knobs at their top, there was nothing to add. Its receipt reads the temperature STEADY, up 1.4% (mean) and 1.5% (peak), in words written before the 0.5% key (`results/gpu/run-20261024T091235Z/GPU_REPS.md`; threat T33).

### 5.9 The cloud: arm C against arm D (class L, omni-v18)

Azure AKS at the tune-down on the machines alone (section 2.3.6): <!-- monograph: cloud_set (tools/monograph_words.py) -->one set of 97 paired repetitions, run 40069633316, on omni-v18<!-- end of monograph: cloud_set -->, the steady load (`results/live/AKS_STEADY_100_OMNI_V18.md`):

<!-- monograph: cloud_table (tools/monograph_words.py) -->
| Gauge | C, native | D, Omni-Compass on native | Reading | Why |
|---|---:|---:|---|---|
| worker nodes in service, mean | 2.814 | 2.832 | power given, up 0.7%, inside the noise | more resource held, put in for what it bought |
| node-hours | 0.7104 | 0.715 | power given, up 0.7%, inside the noise | more resource held, put in for what it bought |
| energy, parked workers still on at idle power (Wh) | 86.62 | 87.77 | power given, up 1.3%, inside the noise | more resource held, put in for what it bought |
| energy (Wh) | 82.7 | 83.23 | power given, up 0.6%, inside the noise | more resource held, put in for what it bought |
| response time (ms), mean | 517.1 | 503.1 | GAIN, down 2.7%, inside the noise | less time waited, missed or failed |
| response time (ms), 95th percentile | 1,245 | 1,195 | GAIN, down 4.0%, inside the noise | less time waited, missed or failed |
| response time (ms), 99th percentile | 4,744 | 4,222 | GAIN, down 11.0%, beyond the noise | less time waited, missed or failed |
| time over the response line (% of samples) | 29.06 | 28.81 | GAIN, down 0.9%, inside the noise | less time waited, missed or failed |
| failed requests (%) | 4.758 | 4.945 | LOSS, up 3.9%, inside the noise | more time waited, missed or failed |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.07 | 13.9 | GAIN, down 1.2%, inside the noise | less time waited, missed or failed |
| pods with no machine to take them (unschedulable) | 2.598 | 2.392 | GAIN, down 7.9%, inside the noise | less time waited, missed or failed |
| time pods had no machine to take them, pod-minutes | 7.018 | 5.993 | GAIN, down 14.6%, inside the noise | less time waited, missed or failed |
| HPA replicas, mean | 9.371 | 9.348 | STEADY, under the floor (0.2%) | no change of 0.5% or more |
| pods started | 5.01 | 4.753 | GAIN, down 5.1%, inside the noise | less of the resource held: a cut |
| pod start wait, total (s) | 525.4 | 455.2 | GAIN, down 13.4%, inside the noise | less time waited, missed or failed |
| pod start wait, mean (s) | 98.43 | 89.88 | GAIN, down 8.7%, inside the noise | less time waited, missed or failed |
| machines billed, machine-hours | 0.586 | 0.5931 | power given, up 1.2%, inside the noise | more resource held, put in for what it bought |
| compute bill at list price ($) | 0.05626 | 0.05694 | power given, up 1.2%, inside the noise | more resource held, put in for what it bought |

Every judged gauge of the set: the mean of the 97 paired repetitions with its 95% interval, one run, so no three-run reading exists; the energy rows are declared models, never a meter.
<!-- end of monograph: cloud_table -->

The slowest one per cent waited less, the one reading beyond the noise; more requests failed, a LOSS inside the noise; the bill rose slightly, power given, so no saving is shown, and the stopping rule's looks never decided it.

### 5.10 The whole-system composition: a second reading (class S)

Each layer ℓ is measured with the layer under it native, and the ratios multiply (`results/WHOLE_SYSTEM.md`):

  H(g) = ∏ℓ Hℓ(g),  log H(g) = Σℓ log Hℓ(g),  read as H(g) − 1.  (5.1)

Its index is the geometric mean over work, speed and machines; energy and the bill are held at native's, and the chip, the cloud and the machine layer enter as exactly 1, so it composes the cluster and its services. It reads <!-- monograph: whole_system (tools/monograph_words.py) -->GAIN, up 43.5% (×1.4347; gauges independent, up 29.1% to up 59.5%; gauges correlated, up 27.8% to up 61.1%); work GAIN, 26.6% more; speed GAIN, native's 305.7% longer, that is, the 95th-percentile response 75.4% shorter; machines and resources held power given, native's 42.5% below Omni-Compass's (×0.5748), that is, 74.0% more held; the cluster's 23 tests and the services' 17 (`results/WHOLE_SYSTEM.md`, class S: a composition of measured layers, never one stacked run)<!-- end of monograph: whole_system -->. No run stacked the layers, so the product assumes a layer's ratio holds when its neighbours also carry Omni-Compass; on the products' four ways <!-- monograph: whole_separability (tools/monograph_words.py) -->23 of 33 pairs of orchestrator and gauge agree within the noise; 10 do not<!-- end of monograph: whole_separability --> (threat T24).

### 5.11 The LOSS ledger: the rows against native, and their causes as written

By the ledger, <!-- monograph: loss_all (tools/monograph_words.py) -->523 rows read LOSS across their three runs in every benchmark's newest table: 281 against Omni-Compass's own native, the rows do no harm is judged by; 70 in place of a controller; 172 without Omni-Compass, or with two changes at once<!-- end of monograph: loss_all --> (`docs/LOSS_LEDGER.md`); the last two groups answer other questions (section 4.6). Of the <!-- monograph: loss_against_native (tools/monograph_words.py) -->281<!-- end of monograph: loss_against_native --> against native: <!-- monograph: loss_by_engine (tools/monograph_words.py) -->220 on omni-v26, 55 on omni-v25 and 6 on omni-v12<!-- end of monograph: loss_by_engine --> (the latter Koordinator's four ways); <!-- monograph: loss_by_aim (tools/monograph_words.py) -->278 on time waited, missed or failed and 3 on work done<!-- end of monograph: loss_by_aim -->; <!-- monograph: loss_by_strength (tools/monograph_words.py) -->62 strong, 54 moderate, 50 weak and 115 inconclusive<!-- end of monograph: loss_by_strength -->; <!-- monograph: loss_by_class (tools/monograph_words.py) -->all 281 class L<!-- end of monograph: loss_by_class -->. **Where they sit:** <!-- monograph: loss_by_place (tools/monograph_words.py) -->35 on the cluster's own tests, in 14 of their 17 tables; 18 on the data stores, in 6 of their 13 tables; 58 on the two-way tables of the batch-stream rigs, in 7 of their 7 tables (the Kubernetes scheduler as shipped 9, the scheduler's bin-packing profile 9, Kueue 10, Volcano 9, the KAI scheduler 7, Koordinator 5, Koordinator on the cgroup root its own tests use 9); 78 on the four ways, Omni-Compass on top of the product, in 11 of their 11 tables; 92 on the four ways, Omni-Compass on the organism alone, in 11 of their 11 tables<!-- end of monograph: loss_by_place -->; the most on one table, <!-- monograph: loss_most (tools/monograph_words.py) -->Armada on the organism alone (four ways, `V25_ARMADA_4W_BARE`) and Karmada on top (four ways, `V25_KARMADA_4W_TOP`), 12 each<!-- end of monograph: loss_most -->.

**Causes:** <!-- monograph: loss_causes (tools/monograph_words.py) -->216 of the 281 carry a written cause and 65 read "not yet written": 21 an engine fault of omni-v26 found in the files (the web service's autoscaler target flipping at the fail-up's floor); 17 queue rows that name the same flip, the control plane's reads suspected beside it; 178 with another cause written<!-- end of monograph: loss_causes -->. The flip's rows are those section 3.9 attributes to it, on the batch-stream rigs' tables but Koordinator's and Crane's, and Armada's and KubeRay's on top. The plain batch queue never flips; its row is the measured cause of section 5.5. Koordinator's two-way rigs flip a tenth as often and still rise: its web rows and its cgroup-root set (`V25_KOORDINATOR_CGROUP`) carry no cause, and its queue rows carry the suspicion that the control plane answering Omni-Compass's reads, six times as often at the 10 s beat as at 60 s, runs on the batch pods' cores, a suspicion that also stands beside the flip on the other product rigs' queue rows (`docs/LOSS_CAUSES_2026-11-05.md`, section 2). omni-v26's three runs decide the flip's share (threat T1).

### 5.12 Can, gives, cannot yet show, does not do

| Kind | Statement (section) | Class, engine |
|---|---|---|
| **CAN** | Shorten the 95th percentile in every Kubernetes index test but the noisy neighbour (5.4); cut the alert minutes summed over the Kubernetes tests, GAIN in all three of our runs (5.7); more work inside the line on Kafka and Redis, GAIN in all three of our runs on every counted workload, and on MySQL by the mean (5.3); hand every setting back after a kill inside the 60 s allowance (3.10) | L, omni-v25 |
| **CAN** | Less energy for each request on one A10, by its own meter (5.8) | P, omni-v23 |
| **GIVES** | The store knobs' resource; pods started and replicas; its own processor on a shared runner; Azure's bill, inside the noise (5.3 to 5.5, 5.9) | L |
| **CANNOT YET SHOW** | More work for the bill on the chip or in a cloud; fewer machines across the composed whole; a people saving; outside review; global stability | P; L; S |
| **KNOWN FAULT** | The web target's flip at the fail-up's floor, the cause the ledger writes most, its fix landed as omni-v26, whose own runs have not landed yet (3.9) | L, omni-v25 |
| **DOES NOT DO** | Sit in the data path; remove a native controller in a counted arm; ask a cloud for machines; replace the card's firmware loop | — |

## 6. The Native Tools and Products: What They Do, What They Leave, Where Omni-Compass Sits

Each product is described only from its own documentation, with the version described and how it was read on 7 November 2026 (threat T36); no vendor's savings figure is reproduced and no product is ranked.

### 6.1 The three layers: inner loops, the outer loop, the control plane

On the chip firmware limits move power, clocks and heat; in the cloud node autoscalers and provisioners move the fleet on unplaced pods, use and the bill; in the software schedulers, autoscalers and each service's own setting move placement, replicas and the service. Each is an inner loop in the sense of section 2.2 (`docs/INDUSTRY_LANDSCAPE.md`); Omni-Compass is one outer, supervisory loop over them, writing in each layer what sections 2.3.1 to 2.3.6 list.

### 6.2 The chip layer

Native is the card's firmware limits, set through NVIDIA's management library and command-line tool [4, 5]. NVIDIA's Workload Power Profiles, bundles of a card's settings reached through nvidia-smi, DCGM or Base Command Manager and, NVIDIA expects, mostly through a scheduler [22], are not supported before Blackwell [23], so neither card on file offers them; Mission Control documents its own [24]. Kepler, a CNCF sandbox project, exports each container's, pod's and node's energy to Prometheus; version 0.11.4, the one `scripts/kind_addons_kepler.sh` pins, reads only RAPL/powercap, has no GPU power support yet and supports bare metal only, and it moves no setting [25]. Omni-Compass writes no power profile; a card running one would make it the native Omni-Compass sits on, untried on any rig (threat T25).

### 6.3 The cloud layer

On AKS native is Azure's Cluster Autoscaler at its default profile [16], adding a node when a pod cannot be placed and removing one its pods do not need [14]; Karpenter is on no rig (section 2.3.3). Omni-Compass parks machines that autoscaler made, for it to remove, and asks the cloud for none. **Our own model of a cloud** (class S; omni-v23's rules at the max on the cloud's own autoscaler, `docs/OMNI_V24.md`) read no beat admissible under the pick rule frozen before the reading: every beat raised the machine-hours against native, power given, up 7.8% to 33.7%, a fall in the work for the bill with the model's work fixed by its load; every beat but 90 s raised the pods waiting for a place, LOSS, up 15.4% at 60 s. A target held ahead of the load buys machines the cloud bills (threat T22).

### 6.4 The software layer, I: autoscalers and each service's own controllers

Kubernetes' HPA sizes a workload from its target [13]; KEDA creates and drives an HPA from its triggers [15], and its HTTP add-on counts the requests in flight it scales on [26]; Goldilocks creates a VPA in recommendation mode for each workload of a labelled namespace [27, 28]. A data store's setting is native of another kind, a constant (threat T14).

### 6.5 The software layer, II: open-source schedulers and orchestrators, run live

Each product runs live as its project ships it, Omni-Compass on top using its own levers only (section 2.3.5). From each one's documentation: the default scheduler filters and then scores nodes [29], its bin-packing profile using `MostAllocated` [30]; Kueue admits jobs by quota [31]; Volcano schedules batch work in queues and gangs [32]; the KAI scheduler by queue, fair share and gang [33]; Koordinator colocates batch work on what latency-sensitive pods leave unused [34]; CruiseKube right-sizes in place, skipping a workload whose HPA scales on CPU or memory [35]; Crane adds prediction to the HPA [36]; KubeRay's Ray autoscaler runs in the head pod [37]; the Gödel scheduler unifies online and offline scheduling [38]; Armada queues jobs outside the clusters [39]; Karmada places work across clusters [40]; Open Cluster Management manages a fleet of them [41]; KubeEdge [42] and Nephio [43] have no rig yet. Each count is the judged rows of the omni-v25 table of Omni-Compass on top of the product against it as shipped, read on our rig and workload, never the product's own (threat T26):

<!-- monograph: governors_table (tools/monograph_words.py) -->
| Product | What it acts on | Omni-Compass on top, against it as shipped | Table |
|---|---|---|---|
| the Kubernetes scheduler as shipped | pod placement | 5 GAIN, 9 LOSS, 2 power given, 5 STEADY, 1 the runs disagree | `results/live/V26_VANILLA.md` |
| the scheduler's bin-packing profile | pod placement | 6 GAIN, 9 LOSS, 2 power given, 4 STEADY, 1 the runs disagree | `results/live/V26_BINPACK.md` |
| Kueue | batch admission (a job at a time, by queue quota) | 5 GAIN, 10 LOSS, 2 power given, 4 STEADY, 1 the runs disagree | `results/live/V26_KUEUE.md` |
| Volcano | batch scheduling (queues, gangs) | 4 GAIN, 9 LOSS, 2 power given, 5 STEADY, 2 the runs disagree | `results/live/V26_VOLCANO.md` |
| KAI scheduler | AI workload scheduling (queues, fair share, gangs) | 4 GAIN, 7 LOSS, 2 power given, 4 STEADY, 5 the runs disagree | `results/live/V26_KAI.md` |
| Koordinator | QoS colocation (batch work on what latency-sensitive pods leave unused) | 4 GAIN, 5 LOSS, 4 STEADY, 8 the runs disagree | `results/live/V26_KOORDINATOR.md` |
| Koordinator on the cgroup root its own tests use | QoS colocation (batch work on what latency-sensitive pods leave unused) | 2 GAIN, 9 LOSS, 2 power given, 6 STEADY, 2 the runs disagree | `results/live/V26_KOORDINATOR_CGROUP.md` |
| CruiseKube | rightsizing (requests and limits, in place) | 3 GAIN, 5 LOSS, 1 power given, 5 STEADY, 2 the runs disagree | `results/live/V26_CRUISEKUBE.md` |
| CruiseKube, a worker it marks overloaded counted as in service | rightsizing (requests and limits, in place) | 3 GAIN, 4 LOSS, 2 power given, 6 STEADY, 1 the runs disagree | `results/live/V26_CRUISEKUBE_RECORDER.md` |
| Crane | predictive autoscaling and resource governance | 4 GAIN, 2 LOSS, 2 power given, 7 STEADY, 1 the runs disagree | `results/live/V26_CRANE_4W_TOP.md` |
| KubeRay | Ray clusters (the Ray autoscaler) | 4 GAIN, 7 LOSS, 2 power given, 4 STEADY, 5 the runs disagree | `results/live/V26_KUBERAY_4W_TOP.md` |
| Gödel scheduler | unified online and offline scheduling | 4 GAIN, 8 LOSS, 2 power given, 4 STEADY, 4 the runs disagree | `results/live/V26_GODEL_4W_TOP.md` |
| Armada | multi-cluster batch | 6 GAIN, 3 LOSS, 2 power given, 10 STEADY | `results/live/V25_ARMADA_4W_TOP.md` |
| Karmada | multi-cluster placement | 4 GAIN, 12 LOSS, 2 power given, 4 STEADY | `results/live/V25_KARMADA_4W_TOP.md` |
| Open Cluster Management | multi-cluster management | 4 GAIN, 10 LOSS, 2 power given, 3 STEADY, 3 the runs disagree | `results/live/V26_OCM_4W_TOP.md` |
| KubeEdge | edge nodes | not yet run; its test not yet written | — |
| Nephio | network-function automation | not yet run; its test not yet written, a candidate: its sandbox asks more than a free runner gives | — |
<!-- end of monograph: governors_table -->

By the record, <!-- monograph: governors_loss_outnumber (tools/monograph_words.py) -->on 13 of these 15 tables LOSS rows outnumber GAIN rows; the exceptions are Crane on top (four ways) and Armada on top (four ways)<!-- end of monograph: governors_loss_outnumber -->; section 5.11 counts the rows by place and cause. **The pattern is a trade, reported as one.** The whole-system page gives <!-- monograph: whole_on_top_ratios (tools/monograph_words.py) -->the factors measured with Omni-Compass on top of each product, oriented so that above 1 is a GAIN (native's over Omni-Compass's for speed, machines and energy): Kueue, speed ×0.9288, machines ×1.2727, energy ×1.1757; Volcano, speed ×0.8675, machines ×1.2018, energy ×1.1294; the KAI scheduler, speed ×0.8976, machines ×1.2871, energy ×1.1829; Koordinator, speed ×1.0746, machines ×1.0055, energy ×1.0046; the scheduler's bin-packing profile, speed ×0.9878, machines ×1.4284, energy ×1.2666; Crane, speed ×1.0199, machines ×1.0000, energy ×0.9989; KubeRay, speed ×0.9886, machines ×1.0079, energy ×1.0051; the Gödel scheduler, speed ×0.9449, machines ×1.2458, energy ×1.1601; Karmada, speed ×0.8667, machines ×1.0866, energy ×1.0612; Open Cluster Management, speed ×0.8081, machines ×1.1087, energy ×1.0734; Armada, speed ×1.7452, machines ×1.9315, energy ×1.5587<!-- end of monograph: whole_on_top_ratios -->. Speed under 1 with machines over 1 is fewer machines held for a longer 95th percentile: on Kueue the speed reads LOSS in all three of our runs and the machines GAIN by the mean of our three runs, beyond the noise in 2 of 3. In the strict form of do no harm the engine keeps, a machine handed back does not pay for a longer wait, so those rows stay LOSS. Armada differs, speed and machines GAIN in all three of our runs, though its table still carries LOSS rows.

### 6.6 Commercial products in the same layers, from their own material

None was run by us, so nothing is claimed about one (`docs/LANDSCAPE.md` keeps the wider list; threat T25).

| Product | Layer | What its own material says it acts on |
|---|---|---|
| StormForge Optimize Live (CloudBolt) | software | requests, limits and the HPA's target utilisation, set alongside the HPA [44] |
| Cast AI | software; cloud | pods resized in place on Kubernetes 1.33 and later [45]; nodes added for unplaced pods, and pods packed onto fewer nodes [46] |
| ScaleOps | software | pod requests adjusted continuously beside the HPA and KEDA [47] |
| PerfectScale (DoiT) | software | requests and limits rightsized, memory raised no further on a suspected leak, a CPU runaway flagged [48] |
| Sedai | software; cloud | changes in three modes: none made, each approved, or made on its own [49] |
| IBM Turbonomic | software; cloud | containers resized through their controller, pods moved, nodes provisioned or suspended [50] |
| Spot Ocean (Flexera) | cloud | an autoscaler keeping headroom, to which its documentation describes migrating from the cluster autoscaler [51, 52] |
| Akamas | software | container limits and runtime options tuned under response-time or error constraints, as its partner Dynatrace describes it [53] |
| Google DeepMind's cooling control (2018) | facility | actions every five minutes from a cloud model, each checked by the site's own control system [54] |
| Phaidra | facility | AI agents for data-centre cooling control [55] |
| BrainBox AI | facility | setpoints written over BACnet to an existing building management system [56] |

A product that takes over a native controller's job is the native of its layer; one writing a setting Omni-Compass also writes would fight it unless one yields, and no rig pairs them (threat T25).

### 6.7 The live benchmark engine beside the operator's surfaces that exist

A metrics dashboard closes no loop; the Kubernetes Dashboard's writes are manual, and it is marked deprecated [57]. A SCADA or HMI screen binds live setpoints to the plant controllers' own tags, its design set out in ANSI/ISA-101.01-2015 [58] and its alarms' life cycle in ANSI/ISA-18.2-2016 [59]. `docs/LANDSCAPE.md` holds the live engine to the HMI's bar; the page reads a wired system's Prometheus and, for a slot's switch, prints the request that system's control panel takes (`POST /v1/mode`, `POST /v1/reset`), writing nothing, so no control on the page drives a live mechanism (threat T28).

### 6.8 Related work

**Cascade and supervisory control.** An outer loop that sets the setpoint of an inner loop which keeps its own actuation is cascade control [60]. Plantwide control orders the loops in layers, regulatory under supervisory under optimisation, each writing setpoints to the one below [61], and industrial model predictive control usually sits in the supervisory layer [62]. Omni-Compass is supervisory in that sense, not in the discrete-event sense of Ramadge and Wonham, where a supervisor disables a plant's events [63]. **Feedback control of computing systems** is set out in [64]; early cases are performance guarantees for web servers [65] and coupled control of virtualised tiers' resources [66], and autonomic computing's monitor, analyse, plan and execute loop is the same outer loop [67]. **Autoscaling and cluster management:** surveys [68, 69]; dynamic capacity management for multi-tier data centres [70]; Google's Borg [71] and Autopilot, which sets jobs' limits and task counts from their history [72]; Heracles, colocating latency-critical and batch work under a controller of its own [73], Koordinator's problem on Kubernetes. **Several controllers on one system:** power controllers at different levels of a data centre can work at cross purposes [74]; model predictive control of a data centre's cooling, learned from operating data [75]. None was run beside Omni-Compass (threat T25).

## 7. The Page, Section by Section

The page opens on its monitor wall and control panel, then its contents, four parts (2 Results, 3 Live Operation, 4 Real Runs and Platforms, 5 Proof and Models) and appendixes A to G. This chapter reads the build <!-- monograph: page_stamp (tools/monograph_words.py) -->omni-v26 (digest `75d3c22eed4473b9`), built 2026-11-13 05:05 UTC, 61,647,870 bytes, SHA-256 `af05e12a0ba61f8b…`, page identity `0e0203773b1268a7…`<!-- end of monograph: page_stamp --> in that order.

### 7.1 The sections, their monitors and their code

Native shows in orange and Omni-Compass in blue; each monitor's light is a red octagon (REDLINING, OVER THE LINE, or a LOSS row in its record), a yellow diamond (STEADY) or a green circle (GAINING), and a dark or grey lamp never counts green. The page opens at the factory profile, at the beat its `build` record names, 10 s on site and 60 s through a cloud (the manual says 60 s; threat T34). A knob moves the page's models, never a recorded result; the kill switch turns every Omni-Compass side to native's colour, never a recorded value or word. `tools/monograph_words.py` writes Table 7.1 from the page: the monitors from its registry; the named functions most of whose elements lie in the section; the records they read, helpers one call deep, read from the script without running it (threat T35); the manual's chapter.

<!-- monograph: page_sections (tools/monograph_words.py) -->
| Section | Anchor | Monitors (number, name, class) | The page's own code | Records read | Live Engine Manual |
|---|---|---|---|---|---|
| 0 Monitor Wall | `#s-wall` | none | `auxBuild`, `auxRender`, `drawWall`, `engineBanner`, `lampSweep`, `tourFollow` | `beatsweep`, `build`, `cpuhost`, `fleet`, `gpurun`, `monitors`, `runs` | chapter 1 |
| 1 Control Panel | `#s-health` | none | `beatSweepShow`, `cmdEcho`, `fuseBuild`, `fuseCmdsBuild`, `fuseMetricsRender`, `fuseSync`, `fuseTab`, `fuseTabsInit`, `igRender`, `jgPaint`, `jgSetup`, `jgTick`, `mechBuild`, `mechLive`, `mechSync`, `mechTab`, `monToc`, `rptOpen`, `swMirror`, `swSet` | `build`, `coremc`, `dial`, `engineruns`, `injgrid`, `monitors`, `scenarios`, `whole` | chapter 2 |
| 2a Scorecard | `#s-bottom` | none | `bottomRender` | `audit`, `fleet`, `onnative`, `whole` | chapter 4 |
| 2b Benefit Against Native | `#s-answer` | none | `answerCheck`, `armsLive` | `bills`, `build`, `onnative` | chapter 5 |
| 2c Benefit Board | `#s-board` | 1 Benefit by Domain (L/S); 4 Benefit by Gauge Family (L/S); 3 Market Map (L/S); 20 Quote Board (L/S) | `buildFamTable`, `buildFleet`, `drawBenefit`, `drawFam`, `drawQuotes`, `drawTradeMap`, `fxCursor`, `tally`, `tradeWire` | `audit`, `build`, `fleet`, `gpurun`, `scen` | chapter 6 |
| 2d LOSS Register | `#s-loss` | none | `buildAudit`, `buildLossKnobs` | `audit`, `coremc`, `gpurun`, `scen`, `whole` | chapter 7 |
| 2e Status Board | `#s-status` | none | `hbRender`, `hbTick` | `audit`, `build`, `fleet`, `glossary`, `gpurun`, `scen`, `whole` | chapter 8 |
| 3a Live Organism | `#s-engines` | 5 Native Organism Ring (S); 6 Omni-Compass Organism Ring (S); 11 Immune System (S); 35 Body Parts on the Band (S) | `buildImm`, `drawImm`, `drawSwarm`, `factoryBeat`, `factoryBeatCloud`, `tNarrate`, `updateImmune`, `updateScan` | `build`, `harness`, `runs` | chapter 9 |
| 3b Golden Signals and Event Log | `#s-feed` | 7 Errors per Decision (S); 8 Throughput per Decision (S); 9 Latency Stand-In per Decision (S); 10 Saturation Stand-In per Decision (S) | `drawInstruments`, `drawLog` | `build` | chapter 10 |
| 3c Control Console | `#s-desk` | 60 System Response per Decision (S); 61 Inter-Frame Interval (S) | `buildDesk`, `buildInstruments`, `cqRender`, `deskSync`, `drawDeskCv`, `drawFrameCv`, `factoryTune`, `hbAct`, `injectProfile`, `knobFault`, `logKnob`, `monKill`, `monSync`, `profileSeq`, `setDial`, `skPressed` | `audit`, `build`, `fleet`, `injgrid`, `scen`, `whole` | chapter 11 |
| 3d Heartbeat Dial | `#s-dial` | none | `buildDial`, `factoryBeat`, `factoryBeatCloud` | `build`, `dial` | chapter 12 |
| 3e Control Cycle | `#s-decision` | 25 Compass Band of the Followed Muscle (S) | `drawBand`, `frame`, `mHandSync`, `monInit`, `setBody`, `setKill`, `updateCard`, `updateText` | `ctlrec`, `engineruns`, `harness`, `monitors` | chapter 13 |
| 3f Phase Plane and Scoreboard | `#s-plane` | 27 Native Phase Plane (S); 28 Omni-Compass Phase Plane (S); 26 Scoreboard Strip (S) | `buildStats`, `drawStats`, `updateScore` | `build`, `harness` | chapter 14 |
| 3g Brain State | `#s-brain` | 29 Double-Well Potential of U (S); 30 Cubic Potential of Stress S (S); 31 Bath Oscillator B (S); 32 Native Controller Trace (S) | `buildOrgans`, `drawBrain`, `drawNat6c` | none | chapter 15 |
| 3h Verdict | `#s-verdict` | 33 Trial Costs and 95% Interval (S); 34 Share of Trials Allowed (S) | `buildFail`, `drawVerdict`, `drawVerdict2`, `keepWords`, `noiseWords`, `vLabels`, `vParams`, `vPreset`, `vTick` | `audit`, `build`, `fleet`, `scen` | chapter 16 |
| 3i Dashboards | `#s-dash` | none | `dashInit`, `dashRender`, `fieldTable` | `field` | chapter 17 |
| 4a Kubernetes Run Playback | `#s-ops` | 13 Data Pipeline (L); 14 Governor Heartbeat and Lease (L); 36 Heartbeat Sweep (S); 15 Response Time Candlesticks (L); 16 Latency Heatmap (L); 17 Throughput per 30 s Bin (L); 18 Paired Repetitions (L) | `beatRender`, `beatSetup`, `beatSync`, `buildOps`, `drawBars`, `drawBeat`, `drawCandle`, `drawHeart`, `drawHeat`, `drawPipe`, `drawReps`, `execute`, `factoryBeat`, `factoryBeatCloud`, `heartUpdate`, `opsSync`, `opsUpdate`, `runEngines` | `audit`, `beatsweep`, `build`, `runs`, `scen`, `whole` | chapter 18 |
| 4b Repetition Telemetry | `#s-runs` | 19 Repetition Telemetry per 30 s Bin (L) | `buildBoard`, `drawRuStrip`, `setRuns`, `stepRuns`, `updateRuns` | `build`, `runs` | chapter 19 |
| 4c Controller Decision Trace | `#s-live` | 21 Native Cluster Trace (S); 22 Omni-Compass Cluster Trace (S); 23 Machines and Response Time (S) | `buildRealK8s`, `buildSteering`, `drawCStrip`, `setCtl`, `updateCScore`, `updateCtl` | `audit`, `bills`, `build`, `ctlrec`, `fleet`, `gpurun`, `runs`, `scen`, `whole` | chapter 20 |
| 4d Cloud Providers | `#s-cloud` | 37 Azure Bill (L); 38 Google Cloud Gate and Bill (L); 39 Amazon Web Services Gate and Bill (L); 40 Native Cloud Machines (S); 41 Omni-Compass Cloud Machines (S) | `buildBill`, `buildLedgers`, `buildPlaces`, `stepC4`, `updC4` | `bills`, `build`, `ctlrec`, `gpurun`, `runs`, `whole` | chapter 21 |
| 4e Orchestrators and Governors | `#s-orch` | 42 Road to a Result (L); 24 Orchestration Stack (L) | `buildFour`, `buildOrch`, `buildOrchDetail`, `buildOrchestra`, `drawOrch`, `drawOrchRoad`, `orchSelect` | `build`, `fleet` | chapter 22 |
| 4f GPU and CPU Hardware | `#s-stacks` | 43 Metered A100 Run (P); 44 CPU Host Model (S); 45 8-Card GPU Node (S); 46 Stack Models (S) | `buildMech`, `cpuInit`, `cpuStands`, `drawCpuHost`, `drawGpu8`, `drawGpuRun`, `drawSStrip`, `gpuInit`, `gpuStands`, `mechSame`, `setStack`, `updateStack` | `bills`, `build`, `cpuhost`, `gpurun`, `scen` | chapter 23 |
| 4g CI Pipeline | `#s-github` | 59 GitHub Actions in Flight (L) | `drawCi` | `build` | chapter 24 |
| 5a Python Runs and Monte Carlo | `#s-proof` | 50 Three-Way Run Check (S); 51 Held-Out Scenario Replay (S); 52 Engine Core Monte Carlo (S) | `drawHeld`, `drawMC`, `drawProof`, `hoInit`, `hoNote`, `mcLinkPaint`, `mcLinkedRun`, `mcRender`, `mcSetup`, `mcSysSetup`, `ownOpen`, `proofInit`, `proofPrint`, `proofSets`, `proofTable` | `build`, `coremc`, `engineruns`, `heldout`, `monitors`, `scen`, `whole` | chapter 25 |
| 5b C++ Twin | `#s-cpp` | none | `cppRender`, `find` | `cpptwin` | chapter 26 |
| 5c Scenarios and Injection Grid | `#s-scn` | none | `scnRender` | `injgrid`, `scenarios` | chapter 27 |
| 5d Whole Organism | `#s-whole` | 2 Stack Composition (S) | `buildWhole`, `drawWhole` | `audit`, `build`, `coremc`, `fleet`, `scen`, `whole` | chapter 28 |
| 5e Measured Effect | `#s-fleet` | 47 Seven Organisms Under Three Loads (S); 48 Catalog Muscle Matrix (S); 49 Scale-Out Grid (S/L) | `buildRealms`, `buildReceipts`, `buildRegister`, `drawGridCv`, `drawMuscleCv`, `drawOrgCv`, `findMuscles`, `setRealmLoad` | `audit`, `build`, `fleet`, `gpurun`, `scen`, `whole` | chapter 29 |
| 5f Telemetry Analytics | `#s-lab` | 53 Telemetry Tensor Cube (S); 54 Tensor Difference Matrix (S); 55 Tensor Principal Modes (S); 56 Service Level (L); 57 Error Budget Burn (L); 58 Repetition Gauges Against Native (L) | `aiAsk`, `aiOff`, `buildAI`, `buildHealth`, `buildLab`, `drawCube`, `drawDelta`, `drawModes`, `drawRadar`, `drawSankey`, `onText`, `tEig`, `voiceWire` | `build`, `ctlrec`, `fleet`, `harness`, `runs`, `scen` | chapter 30 |
| 5g Master Switch Wiring | `#s-master` | 12 Master Switch and Kill Switch (S) | `buildMaster`, `drawMaster`, `masterTable` | `scen` | chapter 31 |
| 5h Specification and Mathematics | `#s-math` | none | `brainBeat`, `eqLive`, `lawWires`, `mathLive`, `modelDay`, `rhoRange` | `audit`, `bills`, `build`, `ctlrec`, `fleet`, `lawwires`, `scen`, `whole` | chapter 32 |
| 5i Failure Modes and Controls | `#s-fail` | none | `shDraw`, `skSync` | `audit`, `fleet`, `scen` | chapter 33 |
| 5j Self-Governed Rendering | `#s-self` | 62 Inter-Frame Interval by Window (S) | `drawSelf`, `selfTable`, `selfUpdate` | `build` | chapter 34 |
| A Title Page and Build | `#title-page` | none | `buildInfo`, `engRuns` | `build`, `scen` | chapter 35 |
| B Reading Guide | `#s-guide` | none | — | `build`, `scen` | chapter 36 |
| C Problem and Answer | `#s-problem` | none | `buildBottom`, `factoryBeat`, `factoryBeatCloud` | `audit`, `build`, `fleet`, `gpurun`, `harness`, `runs`, `scen`, `whole` | chapter 37 |
| D Executive Summary and Reading Key | `#s-read` | none | `buildKeyEx`, `fillSumIndex` | `audit`, `build`, `fleet`, `gpurun`, `harness`, `runs`, `scen`, `whole` | chapter 38 |
| E Monitor List | `#s-monlist` | none | `monInventory`, `mvShow` | `monitors` | chapter 39 |
| F Glossary and Index | `#s-glossary` | none | `glInit`, `glRender`, `pad`, `screenFit`, `screenWire`, `secSigSweep`, `tourLight`, `tourOff`, `tourOn`, `tourPlaceCard`, `tourPlaceTab`, `tourPoint`, `tourRate`, `tourReveal`, `tourShow`, `tourWire`, `wire`, `wireScene` | `audit`, `build`, `fleet`, `glossary`, `onnative`, `whole` | chapter 40 |
| G Disclosures, Law and Contact | `#s-disclose` | none | `hwState` | `build`, `gpurun` | chapter 41 |
<!-- end of monograph: page_sections -->

### 7.2 What a viewer should see

Table 7.2. "The live model" is the stress-test model of sixty muscles the ported core, compass law and verdict run in the browser.

| Section | Class | What a viewer should see |
|---|---|---|
| 0, 1 | each monitor's; S | the wall, each tile with its number and light; the fuse box, the heartbeat buttons (10 to 120 s), the switchboard and the four reports |
| 2a to 2e | L, P, S | the Omni index with its LOSS rows; arms A to D, each place's bill and work, never added; each domain's bar; every standing LOSS row, its cause where written, an alarm on the status board |
| 3a to 3i | S | the live model: each muscle in its band, the immune monitor, signals and log, injected faults, each beat's cost, one decision traced, the six states, a trial's interval |
| 4a, 4b | L | a chosen repetition on both sides, second by second, from raw files whose SHA-256 is matched first |
| 4c | S, L | the shipped controller's audited chain on the modelled cluster, a decision every 60 s (threat T35) |
| 4d to 4g | L, S, P | Azure's bill of section 5.9, Google's and Amazon's gates not yet run; each product's road to its table; the A100's meter; the host and eight-card models; GitHub's runs as of the build |
| 5a to 5e | S, L | one digest from the Python, the C++ and the page; each scenario's word and the injection grid; the composition of section 5.10; the organisms and the catalogue |
| 5f to 5j | S, L | the tensor; a run's service level; **Ask Omni-Compass**, a language model's answer, not a record; the master switch; each part's equation; every shortfall and its control; the page's frame loop |
| A to G | — | the build, the guide, the problem and the answer, the key, the monitor list, the glossary, the disclosures |

### 7.3 The records and the Python that writes them

Table 7.3. Every record the page carries, with the Python that writes it (the builder's `records()` traced to its function or export script, the tools and results files that function reads, and the record's own file, source or tool) and the engine, base, batch or seed it names.

<!-- monograph: page_records_table (tools/monograph_words.py) -->
| Record | Written by | Engine, base, batch or seed |
|---|---|---|
| `ctlrec` | `docs/engine/export_controller_trace.py` | names none |
| `build` | `docs/engine/build_live_engine.py` `records()` | omni-v26; the organisms omni-v8 |
| `runs` | `docs/engine/export_runs.py` | omni-v26 76 tables; omni-v25 15 tables; omni-v12 5 tables |
| `fleet` | `docs/engine/build_live_engine.py` `fleet()`; `tools/omni_index.py`; `results/BENEFIT_SHEET.json`; `results/OMNI_INDEX.md`; `results/OMNI_INDEX.json`; `results/STEERING.json` | names none |
| `whole` | `docs/engine/export_whole.py`; `results/WHOLE_SYSTEM.md`; `tools/whole_system.py` | names none |
| `gpurun` | `docs/engine/export_gpu_run.py`; `results/gpu/run-20261024T091235Z/GPU_REPS.md` | omni-v18 |
| `cpuhost` | `docs/engine/export_cpu_model.py`; `results/sim/cpu_power_model/CPU_POWER.md` | omni-v12 |
| `monitors` | `docs/engine/build_live_engine.py` `records()`; `docs/engine/monitors.json` | names none |
| `engineruns` | `results/engine_runs/ENGINE_RUNS_500_375788794.json`; `tools/engine_runs.py` | omni-v26; base 375788794 |
| `heldout` | `docs/engine/export_heldout.py`; `benchmarks/stack_benchmark.py` | names none |
| `cpptwin` | `docs/engine/export_cpp_twins.py` | seed 3000 |
| `beatsweep` | `docs/engine/build_live_engine.py` `beat_sweep()`; `tools/heartbeat_sweep.py`; `tools/model_gate.py`; `results/model_gate/HEARTBEAT_SWEEP.json` | names none |
| `dial` | `docs/engine/build_live_engine.py` `dial()`; `tools/beat_ladder.py`; `results/model_gate/V23_LADDER_CORRECTED.json` | omni-v23 |
| `coremc` | `docs/engine/build_live_engine.py` `core_mc()`; `results/core_evidence.json`; `benchmarks/core_evidence.py` | seed 223387268 |
| `onnative` | `docs/engine/build_live_engine.py` `on_native_abc()`; `tools/headline.py`; `tools/orchestrator_abc.py`; `results/orchestrator/V21_THREE_ARMS_ABC.json` | omni-v21 |
| `scenarios` | `docs/engine/build_live_engine.py` `scenarios20()`; `tools/scenarios_20.py`; `tools/whole_system.py`; `results/scenarios/SCENARIOS_20.json` | omni-v23 |
| `glossary` | `docs/engine/build_live_engine.py` `glossary()`; `tools/live_glossary.py`; `docs/engine/glossary.json` | omni-v26 |
| `injgrid` | `docs/engine/build_live_engine.py` `injection_grid()`; `tools/injection_grid.py`; `results/injection_grid/INJECTION_GRID_249031878.json` | batch 249031878; omni-v26 |
| `audit` | `docs/engine/build_live_engine.py` `verdict_audit()`; `tools/loss_ledger.py`; `tools/verdict_audit.py`; `results/verdict_audit/DISCREPANCIES.json`; `results/verdict_audit/VERDICT_AUDIT.md` | record `57045e3ea8d9f45f` |
| `lawwires` | `docs/engine/build_live_engine.py` `law_wires()`; `omnicompass/compass_law.py` | names none |
| `field` | `docs/engine/build_live_engine.py` `field()`; `docs/THE_FIELD.md` | names none |
| `bills` | `docs/engine/build_live_engine.py` `bills()`; `tools/site_numbers.py`; `tools/two_bills.py`; `tools/work_per_bill.py`; `results/TWO_BILLS.json`; `results/WORK_PER_BILL.json`; `results/OVERSIGHT.json`; `results/SITE_NUMBERS.json` | names none |
| `tour` (read by no section: the page script reads it at load) | `docs/engine/build_live_engine.py` `tour()`; `tools/tour_script.py`; `tools/tour_voice.py` | names none |
| `harness` | `docs/engine/export_harness_trace.py` | names none |
| `scen` | `docs/engine/export_scenarios.py` | names none |
<!-- end of monograph: page_records_table -->

### 7.4 What the tables establish

Each monitor is read on its own record's engine: beside the omni-v25 tables and the records rebuilt at every build, the page plays the older engines Table 7.3 names (threat T23); and it is true only for its build, playing <!-- monograph: page_lag (tools/monograph_words.py) -->the Python's runs of base 375788794, the newest on file; the injection grid of batch 249031878, the newest on file<!-- end of monograph: page_lag --> (threat T31).

## 8. Reproducing the Engine

Each command below was run on 7 November 2026, read-only, on a four-core container with a partial clone (Python 3.13; the workflows use 3.12), except those marked *not run here*, timed from GitHub's run records. All need `pip install -r requirements.txt`; the page's checks also `node`, the twins `cmake` and a C++ compiler.

### 8.1 From a workflow to a number

**Raw receipts.** Every hour `.github/workflows/archive-run.yml` copies every finished run's files to the branch `raw`, one folder a run with `SHA256SUMS_ALL.txt`, signed with Sigstore from 31 October. To check one run (`open`, not run here, adds a worktree; the check needs `pip install sigstore==4.5.1`):

```
bash scripts/raw_archive.sh open /run-<id>/
python3 tools/verify_receipt.py --offline results/live/raw/run-<id>
```

On run 41810759693, extracted from the branch's objects, it took a second: "1565 files match their sums; the sums carry a valid signature by the archive job". A sum "shows that a file has not changed since the sum was written, not who wrote it" (`docs/THE_RECEIPTS.md`). **Tables.** `tools/reproduce.py` rebuilds every three-run table of the engine that stands from its recipe and compares the files byte for byte, its runs opened first:

```
bash scripts/raw_archive.sh open $(python3 tools/reproduce.py --patterns)
python3 tools/reproduce.py
```

The folders held about ten gigabytes; not run here, for want of disk. `.github/workflows/reproduce.yml` runs both on Mondays; its newest run (42263774475, 6 November) took under ten minutes and found one file not identical, `V25_ALL_FOUR.md` (threat T30). **Aggregates.** `tools/omni_index.py`, `tools/whole_system.py`, `tools/loss_ledger.py`, `tools/verdict_audit.py` and `tools/readings.py` write the index, the composition, the ledger, the audit and every word; `python3 tools/verdict_audit.py --check` (1.5 s) printed "0 disagree with the key; record current", and `python3 tools/monograph_words.py --check` holds this monograph's counts to their records (threat T31).

### 8.2 Re-running each benchmark

<!-- monograph: workflows (tools/monograph_words.py) -->74 workflows<!-- end of monograph: workflows --> hold the automation; the campaign releases run A of every entry in `scripts/reruns.txt`, then B, then C. None was run here. The limit is the workflow's `timeout-minutes`; the time is its newest successful run's, start to last update, queue included, from GitHub's run record of 7 November.

| Benchmark | Workflow (`.github/workflows/`) | Native | Limit | Newest run's time | Cost |
|---|---|---|---|---|---|
| Kubernetes tests of the index | `benchmark-reps.yml`; `kind-addons.yml` | the HPA; KEDA | 240; 150 min | 133 min (run 41832900683) | none |
| Schedulers and orchestrators | `kind-orchestrators.yml`; `kind-crane.yml`, `kind-godel.yml`, `kind-cruisekube.yml`, `kind-group.yml` | each project as shipped | 330; 240 min | 145 min (run 42314446639) | none |
| The five data stores | `pgbench.yml`, `kafka.yml`, `redis.yml`, `ycsb.yml`, `sysbench.yml` | the operator's or vendor's setting | 150 to 180 min | 95 min (pgbench, run 41794373430); 100 min (kafka, run 41785350365) | none |
| The cloud (arms C, D) | `aks-metered.yml`, after Azure's $0 check | AKS and its autoscaler | 300 min | 92 min (run 41914478995, a tuning case) | one's Azure subscription |
| The chip (arms A, B) | `lambda-gpu.yml`, `lambda-attach.yml` | the card's firmware limits | 355 min a job | 249 min (run 41243352339, the A10's run A) | one's Lambda account; the default dry run rents nothing |

`bash scripts/run_live_local.sh 3` builds a kind cluster a repetition on one's own machine (Docker, kind, kubectl, jq, curl; "About 20 minutes per arm").

### 8.3 The Python 500 and its C++ twin

Two seeded sets of 500 runs check that the Python, the C++ and the page compute the same mathematics. `tools/engine_runs.py` draws run k's seed as seedₖ = base + k·0x9E3779B9 mod 2³² into a mulberry32 stream; a run is a day of the core's decisions, steps of the compass law and one give-back trial, and one SHA-256 digest covers the receipts, which the C++ harness and the page's port must equal. The record: <!-- monograph: engine_runs (tools/monograph_words.py) -->the newest record, base 378660628, written 2026-11-13T00:59:35Z on omni-v26: 500 runs, 288 decisions of the brain, 80 steps of the compass law and one give-back trial each, digest `f18a6a40767bc885…`; the C++ harness gave the same digest on the same draws, 500 of 500 runs agreeing to 1e-9, largest difference 0.0e+00 (`results/engine_runs/ENGINE_RUNS_500_378660628.md`, the newest of 186 sets on file)<!-- end of monograph: engine_runs -->. With B that base and `T=$(mktemp -d)`:

```
cmake -S cpp -B "$T" -DCMAKE_BUILD_TYPE=Release && cmake --build "$T" --target oc_engine_runs oc_core_runs
python3 tools/engine_runs.py --runs 500 --base B --cpp "$T"/oc_engine_runs --out "$T"/er.json
python3 tools/engine_runs.py --verify docs/engine/OMNI_COMPASS_LIVE_ENGINE.html --all --runs 500 --base B
python3 tools/core_runs.py --runs 500 --base B --cpp "$T"/oc_core_runs --out "$T"/cr.json
```

Here the build took 8 s, each `engine_runs.py` line 16 s and `core_runs.py` 3 s; both digests equalled the records'. **The core's Monte Carlo** runs native (u = 0, the plant left to its double well) beside Omni-Compass on top; a run is conveyed after 5 macro steps in a row in one basin, |U ∓ 1| ≤ 0.10, and certified at 10. The numpy set (`benchmarks/core_evidence.py`, 4 s): <!-- monograph: core_evidence (tools/monograph_words.py) -->seed 223387268: Omni-Compass on top conveyed 500 and certified 500 of 500 runs, its command peaking at 13.93; the plant alone conveyed 476 and certified 427<!-- end of monograph: core_evidence -->. The jump-generator set, the last line above: <!-- monograph: core_runs (tools/monograph_words.py) -->base 378660628, written 2026-11-13T01:00:13Z: Omni-Compass on top conveyed 500 and certified 500 of 500, the plant alone conveyed 480 and certified 432; the C++ twin 2,000 of 2,000 run-ways agreeing to 1e-9, one digest `12325ab6bc5ee7c7…` (`results/core_runs/CORE_RUNS_500_378660628.md`)<!-- end of monograph: core_runs -->. Both are class S, one computation in three implementations (threat T19).

### 8.4 verify.py, the verification receipt and the release manifest

`python3 verify.py` checks the reference engine, the preregistered files, the fingerprints, the C++ against the Python, the seal and the release manifest, in "about 15-30 minutes, single core"; `.github/workflows/verify.yml` runs its `--quick` form on every push (27 minutes at the release commit, run 42313737713). Not run here. **The receipt** (`results/VERIFY_RECEIPT.txt`): `results/VERIFY_RECEIPT.txt`, rewritten by every release: every check with its PASS or FAIL and the last line "VERIFICATION: PASS" or "FAIL"; the C++ core against its fixtures; the C++ twins against the Python, profile by profile; every Python/C++ twin under the seal; the shield's properties over its cases; and the negative controls, each one a deliberately broken twin the check must catch. The receipt's word for Omni-Compass's own C++ loop is the name its sealed files carried before the naming rule (section 1.1). **The manifest** (`RELEASE_MANIFEST.json`): the release that `RELEASE_MANIFEST.json` names (its `written_at_commit`) and its receipt `results/VERIFY_RECEIPT.txt` with its SHA-256, both rewritten by every release and so read there, never quoted here. Its `--check`, and `verify.py` which runs it, pass only at a release commit; later each file changed since prints a line and the check exits 1. The commit the manifest names is on no branch (threat T30); the release commit is the one that committed the manifest:

```
git log -1 --format='%H %s' -- RELEASE_MANIFEST.json
git worktree add --detach ../omni-release <that commit>
cd ../omni-release && python3 tools/release_manifest.py --check
```

That commit is on main; run here on its files, extracted, the check printed "release manifest matches the files" in under a second.

### 8.5 Checking the page and re-deriving a reading

A reader checks a copy by the manual's chapter 47:

1. `python3 tools/omni_version.py` prints <!-- monograph: engine (tools/monograph_words.py) -->omni-v26, digest `75d3c22eed4473b9`, 65 files<!-- end of monograph: engine -->; the name must equal the page's `<html data-engine>`, the digest the stamp's, and `sha256sum` and `wc -c` the stamp's (section 1.5).
2. `python3 docs/engine/check_live_engine.py` (4 s) holds the page's core, compass law and verdict to the Python and the C++.
3. `python3 docs/engine/check_records.py --seed 3000 3001 3002` (97 s) reproduces the modelled records by an independent path.
4. `python3 -m unittest discover -s tests -p "test_live_*.py" -t .` (29 s) holds every monitor to its wiring and the page to its stamp.
5. `python3 docs/engine/build_live_engine.py --check` rebuilds every record in memory and exits 1 if any differs from the page; it reads every raw file the page plays, so the page's folders are opened first:

   ```
   bash scripts/raw_archive.sh open $(python3 tools/reproduce.py --patterns)
   bash scripts/raw_archive.sh open $(python3 docs/engine/export_runs.py --dirs | sed 's#^/results/live/raw/#/#')
   ```

   Not run here: on GitHub the opening took nine minutes and the check step 22 (page-build run 42322511565); with the folders closed the builder fetches each raw file one at a time and did not finish in 900 s for the referee (threat T30).
6. `python3 verify.py` ends "VERIFICATION: PASS" only at a release commit (section 8.4).

**Re-deriving one reading.** A tile names its monitor, the monitor its table, the table its runs; `bash scripts/raw_archive.sh open $(python3 tools/reproduce.py --patterns --table <NAME>)` opens them for `tools/verify_receipt.py` and `python3 tools/reproduce.py --table <NAME>`, which rebuilds the table byte for byte; `python3 tools/readings.py --key` prints the key.

### 8.6 What the record establishes

In every layer Omni-Compass sits above the native controller, in the control plane, writing settings it already accepts and the four other kinds of section 2.2. Where native has room the live record reads GAIN: every Kubernetes test of the index but the noisy neighbour, and Kafka; Redis, MySQL and PostgreSQL read GAIN on their service and power given on the index; MongoDB took cache and its service read STEADY. The headline, <!-- monograph: index_headline (tools/monograph_words.py) -->GAIN, up 20.0%<!-- end of monograph: index_headline -->, carries its interval and its reading with each category left out (section 4.8). <!-- monograph: loss_against_native (tools/monograph_words.py) -->281<!-- end of monograph: loss_against_native --> rows read LOSS against native, every one shown; the ledger attributes <!-- monograph: flip_split (tools/monograph_words.py) -->21 rows with the fault as their one written cause and 17 queue rows that name it beside a suspected second cause<!-- end of monograph: flip_split --> to one fault of the engine that stands (section 3.9), a diagnosis mostly from one run each that omni-v26's three runs are to test, and the rest have a suspected or measured cause or none yet (threats T1, T2). Each can be re-derived from the raw receipts with sections 8.1 to 8.5; none has yet been re-derived outside Dubra Software Inc. / The Omni-Compass LLC (threat T29).

## 9. Threats to Validity

Each limit is numbered once, with the sections that carry its evidence, and holds on the commit the validity line names.

### 9.1 Internal validity: what moved, and why

**T1. The flip.** The rows given this cause measure a known fault of omni-v25, fixed in omni-v26, whose own three runs have not landed; the attribution is a diagnosis, mostly from one run per rig, with no intervention yet; one conveyance raise also jumps the band's cushion (3.9, 5.11).

**T2. Causes not yet written.** Every pod start wait, failed-request and store row, Koordinator's web rows and cgroup-root set, and the kill test's carry none; the control-plane cause on the product rigs' queue rows is suspected, not measured (5.5, 5.11).

**T3. The beat, picked in a model, paid on a shared runner.** The model counted Omni-Compass's own processor as power given; on the plain batch rig it came from the batch pods (3.7, 5.5).

**T4. The core not ablated; the idle floor.** No run or model has held open the release gate and the idle floor's depth or unwired the rollout guard, the core's three ways to a write; the idle floor, untested by the dial, can take the pool below its starting count (3.5, 3.16).

**T5. Parts no receipt isolates.** The threefold damping; the immune rule's modelled twin (3.4, 3.8).

**T6. The hand-back window.** In the 300 s after the kill more requests failed under Omni-Compass than under native (3.10).

**T7. The switch, as exercised.** Every panel press records `handed_back` false; the card drill moved no setting; the two-person re-arm has run only in unit tests (3.11, 3.12).

**T8. Few pairs, shared machines.** Three pairs a run leave the stores' intervals wide; runs on one kind of machine can share a bias; Redis as shipped, writing nothing, reads a LOSS row (4.3, 5.6).

**T9. What a word can bear.** Only "in all three of our runs" carries an error bound; one 0.5% floor serves every gauge, with no correction for their number (4.4).

### 9.2 Construct validity: what the measures mean

**T10. The headline's construction.** A geometric mean of unlike ratios on equal weights, unmetered energy and STEADY entering as 1, its admission rule stated more narrowly on its page than in its code (4.7, 5.5).

**T11. The headline leans on one category.** Without Apache Kafka, native run by design at nine tenths of its capacity, the rest read power given (4.8).

**T12. The headline's interval.** It measures only the three runs' spread, takes them as independent, is conditional on the measures they admitted, and with the leave-one-out reading is this monograph's computation, on no table (4.8).

**T13. The oversight sum.** Each test weighs by its own minutes; it counts minutes, not people (5.7).

**T14. Native as a constant; levers by product.** At the stores native is one fixed setting; Crane and Gödel move no processor limit (2.3.4, 2.3.5).

**T15. Limits on levers, not on the service** (3.5, 3.10).

**T16. Writes that are not settings.** A permission review must admit the taint and deletion cost, the annotations, the scale writes and created autoscaler, and the Deployment's pause, resume and undo (2.2, 3.16).

**T17. The audit's label and seal.** Under `--law compass` each target write reads "HPA target to rho* = …%", crediting the core with the compass law's target; no hash chain binds the lines (3.13, 3.16).

**T18. One quantity, two aims; energy a model.** A fall in work per dollar reads LOSS in `tools/two_bills.py` and power given in `tools/hil_abc.py`; at the software end energy is never scored (4.2, 5.3).

**T19. Our own models and twins.** Class S plants are written by the authors of the law; the live controller has no C++ twin, and three implementations agreeing is one computation (2.5, 3.14, 8.3).

**T20. The formal statements and the live loop.** The theorems describe neither the core as the adapter runs it nor the on-site beat outrunning the HPA's sync (2.4, 3.15).

### 9.3 External validity: how far the readings reach

**T21. The rig is not bare metal.** Six kind workers share one rented four-core runner; where a result elsewhere differs, the wiring is presumed first (`DISCLOSURES.md`, section 4).

**T22. The chip and the cloud.** The chip stands on older engines and one rented A10; the cloud on one omni-v18 set at a struck tune-down, no work counted; Google and Amazon have not run (1.8, 5.8, 5.9, 6.3).

**T23. Engines differ by layer.** Koordinator's four ways and the orchestra stand on omni-v12, the catalogue on omni-v8 (2.3.5, 7.4).

**T24. Layers measured one at a time.** No run has stacked them, and the composition's separability fails on some pairs (5.10).

**T25. Not yet under test.** Karpenter, the VPA's updater, GKE, EKS, KubeEdge, Nephio, NVIDIA's power profiles, DCGM, any commercial product, a second writer on one setting, a published method beside Omni-Compass (2.3, 6).

**T26. The product rigs.** One rig and batch stream per product; on most, fewer machines with a longer 95th percentile, read as LOSS (6.5).

**T27. The factory profile not yet validated.** Steps 1 and 2 of eight (3.11).

**T28. One's own system.** One run over two windows, never a paired benchmark; the page writes to no live system (1.7, 6.7).

### 9.4 The record and the page

**T29. One source.** Every run, rule, scorer, check, load and native setting is Dubra Software Inc. / The Omni-Compass LLC's own; no outside party has run, reviewed or approved the results. "Preregistered" means written in the repository, whose preregistrations carry <!-- monograph: deviations (tools/monograph_words.py) -->101 amendments in 18 preregistrations: 81 written before the runs they apply to, 13 whose heading states no timing and 7 written after runs began<!-- end of monograph: deviations -->.

**T30. Reproduction.** Sums show files unchanged, not a right measurement; the newest byte-for-byte rebuild found one table not identical; the release check passes only at a release commit; a receipt needs about ten gigabytes of raw folders (8.1, 8.4, 8.5).

**T31. The page's builds, and this monograph's.** The page is true only for its build, and a matching stamp shows a copy whole, not right. This monograph's page and stamp blocks hold only for the build the validity line names: neither a workflow nor `verify.py` runs `tools/monograph_words.py`, so the monograph is in step only at a commit carrying that page, its stamp and the monograph's `--fix` together. The appraisal's count of LOSS rows "after the page's own 0.5% floor at load" is a defect of the builder's tally: its `_size` takes each cell's first number, native's mean, for the run's change, so rows far past the floor are counted STEADY; this monograph quotes none of it (1.3, 7.4).

**T32. The audit's reach.** The audit and the ledger read no card table (4.6).

**T33. Descriptions that lag.** The receipt prevails over: `docs/wiring_recipes.csv` (a park "by taint and drain", the HPA's floor, omni-v3 tables); `README.md` and the one-file builder's header (the copy's records); `DISCLOSURES.md`, section 9 (the clouds' keys); `results/OMNI_INDEX.md` (its admission rule); `results/WHOLE_SYSTEM.md`, section 4 ("on omni-v12"); the omni-v18 A100 receipt, whose words predate the 0.5% key; `docs/LANDSCAPE.md` (a third arm).

**T34. The manual lags the page.** The Live Engine Manual gives the factory beat as 60 s (its sections 2.5, 11.2, 35.2), 4c's cloud as the tune-down (20.1), 5j as class L (34.1) and the eight-card run as not made (23.2, 23.4); names the released profile omni-v24's (line 405 of its file); titles its section 35.3 "The five records"; and says every loop exits at the switch (31.1) (section 7.1 here).

**T35. The page's marks, and chapter 7's reading.** Class marks and text differ on 3c, 5j and 4e; the 4c trace runs at 60 s; the 5f answers are a language model's. Tables 7.1 and 7.3 read the page's script statically, one call deep; code reached only through an inline handler or a computed name is not seen (7.1, 7.3).

**T36. Sources and symbols.** Vendors' pages were read through search results, their hosts not reachable from this session, as each entry says; the Notation maps every symbol renamed from its source.

## References

### Repository files

Every repository file cited is named in full where it is used, under the root and `.github/workflows/`, `benchmarks/`, `cpp/`, `deploy/`, `docs/`, `fleet/`, `omni_controller/`, `omnicompass/`, `pilot/`, `realms/`, `results/`, `scripts/` (`scripts/kind_addons_kepler.sh` among them, [25]), `systems/`, `tests/` and `tools/`.

### External sources

Numbered in order of first citation, with the version each describes. "Source read": the page's text in its project's repository, opened on 7 November 2026; "read", a repository or its README opened that day; "via search", the host not reachable from this session and the claim read in search results that day.

- [1] Taints and Tolerations. https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ (current; source read).
- [2] ReplicaSet: pod deletion cost. https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#pod-deletion-cost (current; source read).
- [3] kubectl rollout. https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/ (current; source read).
- [4] NVML API Reference Guide. NVIDIA. https://docs.nvidia.com/deploy/nvml-api/ (current; via search).
- [5] nvidia-smi (-pl, -lgc, -rgc). NVIDIA. https://docs.nvidia.com/deploy/nvidia-smi/ (current; via search).
- [6] CPU Performance Scaling. Linux kernel documentation. https://docs.kernel.org/admin-guide/pm/cpufreq.html (mainline; source read).
- [7] NodePools. Karpenter. https://karpenter.sh/docs/concepts/nodepools/ (current; source read in aws/karpenter-provider-aws).
- [8] Karpenter overview. https://karpenter.sh/docs/ (current; source read in aws/karpenter-provider-aws).
- [9] Resize CPU and Memory Resources assigned to Containers. https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/ (1.33 and later; source read).
- [10] KEP-1287: In-Place Update of Pod Resources. https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/1287-in-place-update-pod-resources (alpha 1.27, beta 1.33, stable 1.35; read).
- [11] kube-controller-manager. https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/ (sync period 15 s, downscale stabilisation 5 min; source read).
- [12] metrics-server. https://github.com/kubernetes-sigs/metrics-server (v0.9.0 pinned; read).
- [13] Horizontal Pod Autoscaling. https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/ (v1.35; source read).
- [14] Cluster Autoscaler FAQ. https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md (master; read).
- [15] ScaledObject specification. KEDA. https://keda.sh/docs/2.21/reference/scaledobject-spec/ (2.21, the version pinned; source read in kedacore/keda-docs).
- [16] Use the cluster autoscaler in AKS. Microsoft Learn. https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler (current; source read in MicrosoftDocs/azure-aks-docs).
- [17] Deployments: pausing and resuming a rollout. https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ (current; source read).
- [18] Student (W. S. Gosset). The probable error of a mean. Biometrika 6(1), 1–25, 1908.
- [19] P. J. Fleming and J. J. Wallace. How not to lie with statistics: the correct way to summarize benchmark results. Communications of the ACM 29(3), 218–221, 1986.
- [20] J. E. Smith. Characterizing computer performance with a single number. Communications of the ACM 31(10), 1202–1206, 1988.
- [21] T. Hoefler and R. Belli. Scientific benchmarking of parallel computing systems: twelve ways to tell the masses when reporting performance results. SC15, ACM, 2015, article 73.
- [22] Optimize Data Center Efficiency for AI and HPC Workloads with Power Profiles. NVIDIA Technical Blog. https://developer.nvidia.com/blog/optimize-data-center-efficiency-for-ai-and-hpc-workloads-with-power-profiles/ (Blackwell B200; via search).
- [23] Workload Power Profiles Settings. NVIDIA. https://docs.nvidia.com/datacenter/dps/versions/latest/guides/concepts/workload-power-profiles.html (latest; via search).
- [24] Workload Power Profile Solution Introduction. NVIDIA Mission Control. https://docs.nvidia.com/mission-control/docs/systems-administration-guide/latest/wpps/introduction.html (2.1.0; via search).
- [25] Kepler. CNCF sandbox. https://github.com/sustainable-computing-io/kepler (v0.11.4, pinned by `scripts/kind_addons_kepler.sh`; its README's "Current Limitations" read).
- [26] HTTP Add-on: Architecture. KEDA. https://keda.sh/http-add-on/0.16/concepts/architecture/ (0.16, pinned; source read in kedacore/keda-docs).
- [27] Goldilocks. FairwindsOps. https://github.com/FairwindsOps/goldilocks (4.16.2 run; read).
- [28] Vertical Pod Autoscaler. https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler (1.7.1 run; read).
- [29] Kubernetes Scheduler. https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/ (v1.35; source read).
- [30] Resource Bin Packing. https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/ (v1.35; source read).
- [31] Kueue overview. https://kueue.sigs.k8s.io/docs/overview/ (v0.20.2 run; source read in kubernetes-sigs/kueue).
- [32] Volcano. https://volcano.sh/en/docs/ (v1.16.0 run; README read).
- [33] KAI Scheduler. https://github.com/kai-scheduler/KAI-Scheduler (v0.18.6 run; read).
- [34] Koordinator. https://koordinator.sh/docs/ (1.8.0 run; README read).
- [35] CruiseKube. TrueFoundry. https://github.com/truefoundry/cruisekube (0.3.4 run; read; its HPA exclusion as `docs/REGISTER.md` row 81 records it).
- [36] Crane. https://github.com/gocrane/crane (0.11.0 run; read).
- [37] KubeRay Autoscaling. Ray. https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html (KubeRay 1.7.1, Ray 2.52.0 run; via search).
- [38] Gödel Scheduler. kubewharf. https://github.com/kubewharf/godel-scheduler (commit 90de2d0dd7e8 run; read).
- [39] Armada. CNCF sandbox. https://github.com/armadaproject/armada (v0.22.14 run; read).
- [40] Karmada. https://github.com/karmada-io/karmada (v1.19.0 run; read).
- [41] Open Cluster Management. https://open-cluster-management.io/ (bundle 1.4.0 run; README read).
- [42] KubeEdge. https://kubeedge.io/ (not run; README read).
- [43] Nephio. https://nephio.org/ (not run; README read).
- [44] Optimize Live. StormForge by CloudBolt. https://www.cloudbolt.io/stormforge-by-cloudbolt/optimize-live/ (a vendor's description; via search).
- [45] In-Place Pod Resizing. Cast AI. https://docs.cast.ai/docs/woop-in-place-resizing (Workload Autoscaler v0.53.0 and later; via search).
- [46] Autoscaler and Evictor. Cast AI. https://docs.cast.ai/docs/autoscaler (current; via search).
- [47] Automated Pod Rightsizing. ScaleOps. https://scaleops.com/product/automated-pod-rightsizing/ (a vendor's description; via search).
- [48] Understanding At-Risk Indicators. PerfectScale by DoiT. https://help.doit.com/docs/perfectscale-for-kubernetes/saas/visibility-and-optimization/podfit-or-vertical-pod-right-sizing/understanding-at-risk-indicators (SaaS; via search).
- [49] Kubernetes optimization. Sedai. https://docs.sedai.io/get-started/platform/optimization/kubernetes (current; via search).
- [50] Container platform actions. IBM Turbonomic. https://www.ibm.com/docs/SSFV9Z_latest/ux-app/_Target_Configuration_Topics/Container_Opt.html (latest; via search).
- [51] Headroom. Spot Ocean, Flexera. https://docs-spot.flexera.com/ocean/features/headroom (current; via search).
- [52] Scaling (Kubernetes). Spot Ocean, Flexera. https://docs-spot.flexera.com/ocean/features/scaling-kubernetes (current; via search).
- [53] Dynatrace Apps showcase: Akamas Kubernetes optimization. Dynatrace, Akamas's partner; no documentation of Akamas's own was reachable or found. https://www.dynatrace.com/news/blog/dynatrace-apps-showcase-akamas-kubernetes-optimization/ (undated; via search).
- [54] C. Gamble and J. Gao. Safety-first AI for autonomous data centre cooling and industrial control. Google DeepMind, 17 August 2018. https://deepmind.google/discover/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/.
- [55] Applications. Phaidra. https://phaidra.ai/applications (a vendor's description; via search).
- [56] Case study: Cammeby's, 45 Broadway. BrainBox AI. https://brainboxai.com/hubfs/BBAI_Cammebys_45th%20Broadway_Case%20Study%20V3.pdf (its savings figure not reproduced; via search).
- [57] Deploy and Access the Kubernetes Dashboard. https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/ (marked deprecated; source read).
- [58] ANSI/ISA-101.01-2015, Human Machine Interfaces for Process Automation Systems. ISA. https://www.isa.org/products/isa-101-01-2015-human-machine-interfaces-for (the standard not read).
- [59] ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries. ISA. https://www.isa.org/products/ansi-isa-18-2-2016-management-of-alarm-systems-for (the standard not read).
- [60] K. J. Åström and T. Hägglund. Advanced PID Control. ISA, 2006.
- [61] S. Skogestad. Plantwide control: the search for the self-optimizing control structure. Journal of Process Control 10(5), 487–507, 2000.
- [62] S. J. Qin and T. A. Badgwell. A survey of industrial model predictive control technology. Control Engineering Practice 11(7), 733–764, 2003.
- [63] P. J. Ramadge and W. M. Wonham. Supervisory control of a class of discrete event processes. SIAM Journal on Control and Optimization 25(1), 206–230, 1987.
- [64] J. L. Hellerstein, Y. Diao, S. Parekh and D. M. Tilbury. Feedback Control of Computing Systems. Wiley-IEEE Press, 2004.
- [65] T. F. Abdelzaher, K. G. Shin and N. Bhatti. Performance guarantees for Web server end-systems: a control-theoretical approach. IEEE Transactions on Parallel and Distributed Systems 13(1), 80–96, 2002.
- [66] P. Padala, K.-Y. Hou, K. G. Shin, X. Zhu, M. Uysal, Z. Wang, S. Singhal and A. Merchant. Automated control of multiple virtualized resources. EuroSys, 2009.
- [67] J. O. Kephart and D. M. Chess. The vision of autonomic computing. IEEE Computer 36(1), 41–50, 2003.
- [68] T. Lorido-Botran, J. Miguel-Alonso and J. A. Lozano. A review of auto-scaling techniques for elastic applications in cloud environments. Journal of Grid Computing 12(4), 559–592, 2014.
- [69] C. Qu, R. N. Calheiros and R. Buyya. Auto-scaling web applications in clouds: a taxonomy and survey. ACM Computing Surveys 51(4), article 73, 2018.
- [70] A. Gandhi, M. Harchol-Balter, R. Raghunathan and M. A. Kozuch. AutoScale: dynamic, robust capacity management for multi-tier data centers. ACM Transactions on Computer Systems 30(4), article 14, 2012.
- [71] A. Verma, L. Pedrosa, M. Korupolu, D. Oppenheimer, E. Tune and J. Wilkes. Large-scale cluster management at Google with Borg. EuroSys, 2015.
- [72] K. Rzadca et al. Autopilot: workload autoscaling at Google. EuroSys, 2020.
- [73] D. Lo, L. Cheng, R. Govindaraju, P. Ranganathan and C. Kozyrakis. Heracles: improving resource efficiency at scale. ISCA, 2015.
- [74] R. Raghavendra, P. Ranganathan, V. Talwar, Z. Wang and X. Zhu. No "power" struggles: coordinated multi-level power management for the data center. ASPLOS, 2008.
- [75] N. Lazic, T. Lu, C. Boutilier, M. Ryu, E. Wong, B. Roy and G. Imwalle. Data center cooling using model-predictive control. NeurIPS 31, 2018.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
