# Disclosures, Declarations and Disclaimers

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page is the one place every declaration about Omni-Compass is made. The README, the manual, the book, every guide
and every report point here. Where any other page seems to say more than this page, this page governs.

## 1. Rights

1. Omni-Compass, its engine, its mathematics, its software and its documentation are the property of The Omni-Compass
   LLC. All patents, copyrights and trademarks covering them have been filed in the
   United States by The Omni-Compass LLC. No filing number is stated here, and no grant, registration or approval is
   claimed.
2. The software is licensed for evaluation and simulation only (`LICENSE`). Running it in production, on any system
   beyond evaluation, or in any product or service, requires a signed, paid Omni-Compass Enterprise License.
3. Names of other companies and products (NVIDIA, Kubernetes, Red Hat OpenShift, Amazon EKS, Google GKE, Microsoft
   AKS, Karpenter, Lambda and others) are the property of their owners. They identify the systems Omni-Compass was
   tested with or connects to. No affiliation, endorsement or certification by any of them is stated or implied.
4. All rights reserved. The Omni-Compass LLC reserves the right to change the software, the documentation, the results
   and the terms at any time, without notice. Every copy, fork, export, report, archive or printout of any part of
   Omni-Compass carries the README's notice, `LICENSE`, `NOTICE` and this page unchanged. The Omni-Compass LLC,
   www.omni-compass.com

## 2. What a result is, and what it is not

1. Every result carries its evidence class: **T** a theorem, **V** verified in code, **S** our own models (modelled),
   **L** live software (real Kubernetes on GitHub's machines), **P** a physical meter (a real card's own power meter).
   A model is a statement about the model. A software benchmark is a statement about the software and machine it ran
   on. Only a meter speaks for hardware.
2. The models were written by the same people who wrote the law. They show how the mechanism behaves; they are not an
   independent test.
3. On Kubernetes in kind every machine stays powered, so energy there is a declared model, not a meter.
4. Every comparison is paired: the same seed, load and clock with and without Omni-Compass, in an order rotated by
   repetition. Intervals are 95% intervals over the paired repetitions. Ratios across seeds are summarised as geometric
   means. Labels are assigned by code from rules written and committed before the run
   (`docs/GPU_PREREGISTRATION.md`, `docs/REALMS_PREREGISTRATION.md`, `docs/K8S_COMPASS_PREREGISTRATION.md`), never by hand.
5. Losses and failed runs are kept beside the wins (`docs/EVIDENCE_LEDGER.md`, `results/live/`, git history). The
   first real-card run, for example, saved energy (+3.6% work per energy, proven) and made the slowest answers 58.5%
   slower; it is published as it happened.
6. No result is a promise of a saving on any other system. No dollar figure in this repository is a measured result.
   Nothing here is a vendor certification, a safety certification, legal advice or investment advice.

## 3. Do no harm, and the rule Omni-Compass keeps on every muscle

**What "do no harm" means** (the founder's words of 19 October 2026; this is its meaning everywhere in Omni-Compass, and
it has no other). Omni-Compass has one goal: to strengthen the organism it governs and keep it healthy, working at the
best state its own muscles can carry. Whatever is fed into the organism (its work, its data, its energy: its nutrients)
passes through its muscles and comes out as its output. Omni-Compass's brain drives the organism toward the most and the
best output it can make from what it is fed (the most work, done fastest, with the fewest misses and failures) while it
keeps every muscle healthy.

- **Harm is judged at the organism.** Harm is the organism turning out less than its native controllers make it turn out
  (less work done; more time waited, missed or failed), or the organism made less healthy: a muscle pushed past its own
  limit, a service pushed over its own line, or anything made to fail. Omni-Compass does neither.
- **Every muscle only as far as it can go.** Omni-Compass can push a muscle only as far as that muscle itself can be
  pushed: its own limit, read live from the system, never past it. It finds the room each muscle already has and uses
  all of it. Whether its mathematics can draw a little more out of a muscle than the muscle was built to give is an open
  question; a measurement answers it before anything is claimed.
- **The muscles work as one body.** Where one muscle's strength cannot be used without straining another, the brain
  offsets and engages the muscles together to bring the whole organism to its best state. It may use one muscle less,
  leave it native, or rest it, so that another can carry more, whenever the organism's whole output comes out ahead and
  every muscle stays healthy. Which muscles to drive and which to leave native is the brain's live decision, at every
  moment and in every run.
- **Reactive and proactive.** Like an immune system, the brain answers a breach at once, and it acts before a line is
  crossed.
- **Every row is still shown.** Each muscle's and each gauge's reading stays in every table beside the organism's, LOSS
  included. Nothing is cut.

**How the engine that stands keeps it.** The engine that stands keeps do no harm in its strictest form. By default it moves each
muscle's settings toward more work, faster, up to the muscle's own limit and never past it (the max); on the dial anyone
can tune it down toward the same work with less (the tune-down). Either way it keeps a step only where the muscle is
never behind native for it: a step that costs the muscle more for each piece of work, or loses more than **2%** in any
measure (work done, response time at the median, p95 or p99, time over the service line, or the machine's own cost of
running Omni-Compass), is undone. A resource spent that rose is **power given**, shown beside the work, the speed and the
wear it bought, never called a loss. Where no move passes that test, Omni-Compass leaves the muscle exactly as it runs
alone. It takes nothing from one muscle to give to another: that form never harms the organism, but it leaves
unused any gain that needs one muscle to give way to another. Letting one muscle give way so that the organism's whole
output comes out ahead, judged on the organism and on every muscle's health, is the next engine version's work. It is
built and proven in our own models first (the model gate), every benchmark is run again on it, and no result claims it
before its runs exist.

**The factory tune: one tuned engine, and a tuning bench.** The engine in this repository is presented as The Omni-Compass LLC
tuned and ships it: self-running, set at the factory. Every muscle in the catalog is wired and runs on the setting found for it
(its own card where one was found on development seeds and kept under the strict rule, 364 muscles in
`realms/muscle_cards_v5.csv`; the engine's own setting for every other), frozen and fingerprinted by version (`python3
tools/omni_version.py`); no setting is presented as universal. **Every published benchmark result is one engine at its one
factory tune**: the engine its table names (`python3 tools/omni_version.py`), run again on each engine that stands. From
omni-v17 that tune is held to a declared rule (`docs/THE_TUNE.md`, `tools/tune_study.py`): of the tunes that harm no gauge against native, the
one against which no other tune tried reads GAIN on one service gauge and LOSS on none, searched on development seeds and read
again on untouched ones; the claim is non-dominance among the tunes searched, never a global optimum. The live benchmark engine page and the
control panel are a live tuning engine: every knob, button and monitor turns in real time (the beat, the dial, the pedal, each
muscle driven or left native, up or down, in or out, minus or plus) to show the mechanism of action with native alone, with
Omni-Compass on top, or both side by side; what it shows at any other setting is the engine's range, never a benchmark result. As
on any engine, where the mixture, the intake, the exhaust, the firing or the pistons change what it delivers, **turning any knob
of Omni-Compass can change every metric, up or down, in any direction a tuner chooses**: one engine for many vessels, tuned many
ways, for many outputs. A licensee may add on, retune, upgrade or tune down any muscle or combination (the dial, the cards, the
bands and the service lines are exposed); a changed tune is the licensee's own, and so are its results. The factory tune is published only where it reads no LOSS: a LOSS found
in The Omni-Compass LLC's own runs is treated as a fault in the mechanism or its wiring, found and fixed before the result is
published, never as a number to live with (the founder's order of 23 October 2026). The one place a LOSS is meant to be seen
is the live benchmark engine, when a person turns its knobs away from the factory tune (the dial, the heartbeat, the sizes, the load)
to watch the system react and the brain hold or recover: that showing is the proof that the mechanism can be broken only by
leaving it, and a changed tune's readings are the licensee's own.

**The factory profile, and the profile that comes next.** The factory tune is one complete configuration profile, the factory
profile: every governing rule, gain, margin, decision interval and default setting shipped together, versioned and fingerprinted.
Today's is omni-v19's. The best validated factory profile for the declared operating conditions is not yet established: it is
chosen only after every mechanism is verified, every knob combination is tested together on development workloads, and the choice
is validated on fresh ones; then it is frozen, carried into every implementation (the C++ harness included) and released under its
own identity. Until then no other profile is presented as the baseline; on the live benchmark engine a candidate is evaluated, never
released, and a custom profile's readings are its own. The words, the mathematics and the bill's arithmetic are written once in
`docs/FACTORY_PROFILE.md`.

## 4. The wiring declaration

**THE PUBLISHED BENCHMARKS ARE THE RECORD OF WHAT OMNI-COMPASS DID ON THE SYSTEMS, LOADS AND ENGINE THEY NAME, EACH WITH ITS EVIDENCE CLASS. WHERE A RESULT ON ANY OTHER SYSTEM DIFFERS FROM THEM, OR ANYTHING LOOKS WRONG, THE FIRST PRESUMPTION IS THE WIRING, THE SETTINGS, OR HOW OMNI-COMPASS WAS IMPLEMENTED OR READ, NOT THE LAW. CHECK THOSE FIRST (THE MANUAL'S "WIRED RIGHT OR WIRED WRONG") BEFORE DRAWING ANY CONCLUSION ABOUT OMNI-COMPASS.**

**Omni-Compass acts only through the wires it is given.** It reads the meters it is pointed at and moves the settings
it is allowed to move. If a reading is the wrong one, slow, or blind; if a lever is the wrong one, already owned by
another controller, or given a range (cover) that is wrong for the machine; if a band or a service line is set for a
different workload; then Omni-Compass will do exactly what its law says with the wrong information, and the result will
not be the published one.

Therefore:

1. **It cannot be slapped on.** Every installation goes through the levels of the manual in order (chapter 6), starting
   read-only, and every writing level begins with the wire check (manual, section 4.4) and a watch arm that must equal
   native.
2. **If your paired receipts differ from the published benchmarks in direction** (service LOSS, or no saving where one
   was shown), **the first presumption is wiring, not the law.** Confirm the installation with the checks in the
   manual's section 4.5 (*Wired right or wired wrong*) before drawing any conclusion about Omni-Compass.
3. **This has happened to us, and is published.** On the first real card (NVIDIA A10, 2026-10-02) the governor read
   being busy as trouble, set its power lid under the card's own working draw and allowed the clock under the card's own
   working clock; the card served bursts more slowly and the slowest answers were 58.5% slower. The cause was found in
   the card's own samples and corrected (`docs/GPU_PREREGISTRATION.md`, amendments 6 and 7). That is what a wiring
   fault looks like, and how it is found.
4. Omni-Compass never writes outside a lever's cover, never fights another writer (it stops and leaves that lever alone),
   reads back every write, and returns every lever to the value it read before its first write when it stops or when the
   OFF switch is used. These protect the machine; they do not make a wrong wiring right.

## 5. Safety and responsibility

1. Run watch mode first; run the wire check before any write; keep the master OFF switch (`python3 tools/omni_switch.py off`, the
   whole harness at once) in reach at every level, and use it at the first sign of anything wrong, a suspected breach included.
2. Omni-Compass is a supervisory governor. The machines' own controls (firmware, autoscalers, safety systems) stay in
   place and keep their own protections; Omni-Compass sets only values they already accept.
3. Do not connect Omni-Compass to safety-critical systems (vehicles, medical devices, grid protection, life safety)
   except as a modelled study, and never without the qualified review those systems require.
4. The software is provided "as is", without warranty of any kind, as stated in `LICENSE`. The operator is responsible
   for its use on their systems.

## 6. Changes to the work and to this page

1. The software, the law's settings, the benchmarks, the results, the documents, the licensing terms and this page may
   change at any time, without notice. The version in the repository's `main` branch at a given commit is the version
   that commit describes; `RELEASE_MANIFEST.json` and `python3 verify.py` identify it.
2. Statements about work in progress, planned features, expected results and future runs are expectations, not
   promises. Where a result has not yet been measured, the documents say so (`docs/STATE_OF_PLAY.md`,
   `docs/DOSSIER.md`, section 8).
3. A signed Omni-Compass Enterprise License governs its own terms for its own term.

## 7. Privacy and data

Omni-Compass contains no telemetry. It sends nothing to The Omni-Compass LLC or anyone else, and makes no network
connection of its own except to the systems an operator points it at. Its logs and receipts stay on the operator's
machines.

## 8. Where everything is

| Question | Page |
|---|---|
| What has been measured, and how strongly | `docs/STATE_OF_PLAY.md`, `docs/DOSSIER.md`, `docs/EVIDENCE_LEDGER.md` |
| The rules written before each run | `docs/GPU_PREREGISTRATION.md`, `docs/REALMS_PREREGISTRATION.md`, `docs/K8S_COMPASS_PREREGISTRATION.md` |
| How to wire it, level by level, and how to confirm it is wired right | `docs/OMNI_COMPASS_MANUAL.md` (chapters 4 and 6), the book `docs/OMNI_COMPASS_MANUAL.pdf` |
| The license, in plain answers, and third-party components | `LICENSE`, `LICENSING_FAQ.md`, `ENTERPRISE_LICENSE.md`, `NOTICE`, `THIRD_PARTY_NOTICES.md`, `PATENTS.md`, `TRADEMARKS.md`, `SECURITY.md`, `.github/CLA.md` |
| The muscles, what each is for and how it is wired | `docs/MUSCLE_CATALOG.md` |
| Proof the code is the code that ran | `python3 verify.py`, `RELEASE_MANIFEST.json`, `results/SEAL.json` |
| The live benchmark engine: every monitor, its feed and its knobs; the third manual, how to read and operate it | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, `docs/engine/monitors.json`, `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` and `.pdf` (the Live Benchmark Engine Manual's Appendix L, the page word for word: `docs/engine/PAGE_WORD_FOR_WORD.md`) |
| The whole organism, composed every way it is bought | `results/WHOLE_SYSTEM.md`, `tools/whole_system.py`, `docs/engine/export_whole.py`, `docs/WHOLE_SYSTEM_PREREGISTRATION.md` |
| The Python's runs that the live benchmark engine runs again | `tools/engine_runs.py`, `results/engine_runs/`, `results/heldout_seed_*/` |

## 9. The whole organism, the cloud's back end, and the live benchmark engine

**The composition is a model of measurements.** `results/WHOLE_SYSTEM.md` (`tools/whole_system.py`) composes each layer's own
measured ratio, native against Omni-Compass on top of native, into one benefit for a whole stack: the product law
R(g) = ∏ℓ Rℓ(g) gauge by gauge, its logarithm a sum with the variances added, each layer's runs A, B and C pooled by the
inverse of their variances, and one index over the gauges with its 95% interval under two bounds (the gauges independent;
perfectly correlated). No run here has stacked the layers: each factor is one layer's own run with the layers under it
native, and the product assumes a layer's ratio does not change when the layers around it also carry Omni-Compass. That
assumption is tested where the tables can test it (the governors' four ways), and the stacked run that replaces the
composition is preregistered in `docs/WHOLE_SYSTEM_PREREGISTRATION.md`. Until it runs, the composition is class S of class P
and L measurements, and every page that shows it says so.

**Every way a stack is bought.** The same law is read four ways (`docs/engine/export_whole.py`): on-site bare metal (the
software on the owner's own racks and chips); through the cloud (the cloud's build, its bare metal at the back end and the
software; and the cloud as two pieces, the back end left to the provider); in the device (Omni-Compass in the bare metal
alone, the card and the machine); and as a service (the software alone, for an owner with neither bare metal of their own
nor a cloud account). A piece with no measurement enters as exactly 1 and is named.

**The cloud's back end is not ours to meter.** Through the cloud, the bare metal belongs to the provider: no tenant can read
its power meters or write its chips' limits, and no run here reaches it. The cloud piece's benefit is what the provider itself
meters and bills, the machines counted every fifteen seconds and the bill at list price, read native against Omni-Compass on
top of the cloud's own autoscaler. The bare-metal piece is gauged on hardware we can meter (a card's own power meter; a processor's energy counter)
and is carried to the provider's bare metal only as the same mechanism on the same kind of part, a modelled factor, never as a
measurement of the provider's machines.

**The cloud is a wire.** A cloud is the wire between the software end (the owner's programs, Kubernetes and the open-source
orchestrators, managers and autoscalers that carry the work) and the hardware end (the bare metal: the GPU chips, the Linux
racks, the data center). Omni-Compass can live in all three places; the wire makes no benefit of its own. Until 31 October
every cloud run here was set on the wire alone (the tune-down on the machines only), so it could at most park machines the
cloud already made and cut the wire's bill a little. From 31 October (the founder's order of that day: no hard rule) every
cloud set runs the whole engine at the max on the cloud's cluster, so its receipt shows that the engine holds there as on site
and the work per dollar beside the bill: more work for the same money, never a smaller bill as the aim. The bare metal's
energy and throughput are not under a tenant; they are measured where Omni-Compass sits on them (the card and the machine) and
composed with the wire by the law above. A provider running Omni-Compass on its own back end would see that benefit on its own
chips and racks; no tenant can meter it, so it is never claimed here as a measurement. The company's expected ranges (the
founder's figures of 24 October: about 3 to 4% from the software end, 2 to 3% from the bare metal, about 5% from the two
together, 1 to 2% from the wire alone) are an expectation, never a result; where a measurement differs, the measurement stands.

**The organisms.** The seven organisms of the catalog (the spine, the four realms, the four stacked, the tower), the orchestra
beside them, the live benchmark engine's own sixty-muscle organism, and the whole organism in its three places (the software end, the
cloud's wire, the bare metal) composed above: ten organisms. Each is read two ways, native and Omni-Compass on top of native
(Omni-Compass is never by itself, the founder's order of 25 October): twenty scenarios, recorded in
`results/scenarios/SCENARIOS_20.json` (class S, our own models, three runs), every cell with no run reading "not yet run".
None is a product.

**The live benchmark engine.** `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` is a monitor of the repository's records and of the engine's
own mathematics running in the page, and the live tuning bench: a setting other than the factory profile shows a variation of
the mechanism, never a result. Every monitor carries its evidence class (P a physical meter, L live software, S our own models)
and its state: live (the engine's port, proven equal to the Python and the C++ on every build by
`docs/engine/check_live_engine.py`), a replay of a recorded run from its own files, a reading of the repository's tables, or
built and awaiting its run, with no invented number and the run that fills it named. The kill switch on the page acts on
what runs in the page, and a recorded result changes its colour, never a value, a word or a row. Pointed at an owner's own
Prometheus, the page only reads it: it writes to no system.

**The three manuals.** The Operator's Manual wires and runs Omni-Compass, the Owner's holds the whole mechanism and every
result, the Live Benchmark Engine Manual reads the page; each carries this notice, the `LICENSE`, the `NOTICE` and this page.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
