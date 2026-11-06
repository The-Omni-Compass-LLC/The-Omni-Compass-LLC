# The founder's ledger — every order, where it stands

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This is the scratch pad and blueprint the founder ordered kept. It holds every order from the design session of
11 October 2026 (89 messages, read top to bottom on 12 October) and the orders after it, grouped by topic. Each line says
what was ordered, in the founder's words where they matter, and where it stands:

- **DONE**: built, tested and in this repository (the file is named).
- **PARTLY**: some of it is built; the line says which part is missing.
- **TO BUILD**: written down and designed (`docs/omni_v5/OMNI_V5_PLAN.md`, `docs/omni_v5/BUILD_STAGES.md`), not yet code.

The standing orders from before 11 October live in `CLAUDE.md`. The build order is `docs/omni_v5/BUILD_STAGES.md`. This
ledger is updated in the same commit as any change it describes. The founder hears what a result says before it goes up.

## 1. The engine: one new engine, v5

| # | Order | Status |
|---|---|---|
| 1.1 | "Not a version 3.5... version 5, a combination of everything": reverse-engineer every result of v1-v4 into gains, cuts and losses, and build one engine ahead of all of them combined (msgs 24, 32). | **DONE**: `realms/compass_arm_v5.py`, declared **omni-v5** (`OMNI_V5.json`, `docs/OMNI_V5.md`). |
| 1.2 | "You build a whole brand new one... a new whole tree", not a modified v3 (msgs 79, 80, 84). | **DONE**: omni-v5 is its own fingerprint over its own tree; v1-v3 are kept only for their results. |
| 1.3 | The study already showed v5 about three times v3; wire it so the repository shows it (12 Oct). | **DONE**: the first in-repo v5 threw most of it away with blanket gates; re-declared 12 Oct. Official table, preregistered seeds: the whole tower saves **0.99% against v3's 0.33% (3.0x)**, the four stacked 0.99% against 0.33% (3.0x), Energy/Facility 1.00% against 0.33% (3.0x), Distribution 1.6x, Physics 1.2x, Compute 1.1x (`results/realms_v5/REALMS_V5.md`). |
| 1.4 | Only two guardrails: "along the edge so nothing riding on the edge can fall off", and "nothing in the middle can go so far into the center that it falls into a hole and can't come out". Everything else free will: "push, pull, stop, start, expand, shrink" (msgs 31, 42). | **DONE** in the law: the edge (moving cushion) and the hole (Lindley reach for rooms, loop reach for process loops, drop and latency floors for serving pools, nothing permanent). A knob stays native only where its own physics says moving it cannot help without harm (`docs/OMNI_V5.md`). |
| 1.5 | The 5% cushion moves in real time, thin for a steady machine, thick for a jumpy one: "minus three times the wobble, that is our 99.9" (msgs 27-30). | **DONE**: cushion = climb x reaction + 3.09 x wobble, widen at once, narrow slowly (`Edge` in `realms/compass_arm_v5.py`). |
| 1.6 | Nothing behind native, the same or ahead, on every muscle (msgs 33, 39, 61). | **DONE** on every muscle alone: 0 of 1,097 LOSS or power given, no service lost (`tests/test_compass_arm_v5.py`, the official table on seeds 3000-3009, development seeds 7100-7109). **PARTLY** inside the organisms (12 Oct, measured): 1 to 3 UPS or power-distribution plants per organism one decision over their line in one of ten seeds (v3: 13 to 35); seven of the eight come right after the safety cutoff, when every knob returns to native at once and the body pays back what Omni saved, one while Omni runs (40 W over a 211 kW line where native sat 9 W under). The strict body guard was built and measured on development seeds: it removes them and almost all of the saving where the UPS lines run full (Compute / AI / Cloud 0.47% to 0.01%). **The founder's decision**: keep v5 as it is and report the residue, take the strict guard, or let the native side ramp the hand-back. |
| 1.7 | Save **and** Max: "push everything to its limit, hold it at its limit, never go beyond its limit"; "we want to know how much can it spend" (msgs 40-43). | **PARTLY**: the Max dial exists in the study (`docs/omni_v5/study/maxarm.py`, `sweep.py`); the engine default is the no-harm Save setting. Stage 3 builds the dial into the engine. |
| 1.8 | "Cost is not a boundary... as long as it's getting a benefit that absorbs the cost": judge net benefit (msg 42). | **TO BUILD**: the bill at every point (energy, machine hours, wear, risk) is stage 3 (a new omnicompass/dial.py). |
| 1.9 | Chip heat: find what the room cools to and how far the chip can go; keep it if the benefit pays (msg 42). | **PARTLY**: the boundary is written (the junction temperature, read from the chip, `OMNI_V5_PLAN.md` §4). The live GPU governor now holds its balance point at the v5 edge; the junction-temperature boundary binds on the Max dial (stage 3), where clocks and power are pushed up. |
| 1.10 | 99.9% against the industry's 85-95%, and "why check it twice?", "why run back 10 minutes on native?" (msgs 20-23). | **DONE** in v5: it acts at once where the physics is safe, a watchdog instead of a gate, re-test only when something changes (v4's interleaved re-test is not in v5). |
| 1.11 | The speed-of-light term: "a speed of light equation" that keeps everything moving faster (msgs 23, 26, 64). | **DONE**: the compass law's tanh drive (`omnicompass/compass_law.py`), used by v5. |
| 1.12 | Early warning: "we see it leading to that and as it's leading to that, Omnicompass has to jump in" (msg 35). Agreed rule: project each muscle ahead by its own reaction time (climb plus three wobbles), move the moment the projection touches the edge. | **PARTLY**: in the engine for motion axes (the wake forecast over a whole deadline, 12 Oct), slow process loops (the loop reach carried ahead), cooled rooms (the headroom's fall read ahead) and serving pools (burst room). Still to do: the same forecast on the autoscaler target, so it can be freed. |
| 1.13 | Idle, never zero: "the system has to go from one or two straight to 99, because it can't never go over 100" (msg 45). Wake straight to the level the work needs, sized from what arrives plus the burst forecast. | **PARTLY**: a motion axis wakes straight to full speed; the breathing floor and proportional wake on every muscle are stage 6. |
| 1.14 | "Omnicompass never sleeps. It sleeps with one eye open" (msg 47). Sleepwalking guard: no jump to full with nothing arriving (msg 56). | **PARTLY**: the brain reads every muscle every decision; the sleep floor and the "wake only on a metered trigger" rule are stage 6. Written in `OMNI_V5_PLAN.md` §3, §24. |
| 1.15 | Omni on the muscle, on the organism and on the cloud or chip, stacked: test whether stacking gains more (msg 36). | **TO BUILD**: the five-way test (native, muscle only, organism only, cloud/chip only, all three). `OMNI_V5_PLAN.md` §7. |
| 1.16 | The five formula knobs to massage: safety factor, look-back, reaction time, widen/narrow speed, which edge (energy or speed). | **DONE** as named settings of `Cfg` (`z`, `window`, `react_mult`, `narrow`, `spend_beyond`). |
| 1.17 | Simulate v5 against every version, not just v3 (msg 32); show every version on the same hour. | **PARTLY**: the official table shows native, v5 and v3 on the same seeds. The all-versions runner (native, v1/v2, v3, v4, v5) is in the scratch study; bringing it into the repository is open. |

## 2. The body: the mechanism of action (the cyborg)

| # | Order | Status |
|---|---|---|
| 2.1 | A cyborg: half living body, half engine, tuned like a carburetor (msgs 45, 48, 49). | Written: `OMNI_V5_PLAN.md` §3, §6. |
| 2.2 | Immune system: see inflammation, attack it, fix it; fever; cancer (spreading, cannot be cured inside): shut Omni off there, restore native, clear it, restart from the seed (msgs 42, 43, 46). | **TO BUILD**: stage 5 (a new omnicompass/immune.py); study in `docs/omni_v5/study/immune.py`. |
| 2.3 | The brain's diseases: amnesia, Alzheimer's, schizophrenia, hallucination, sleepwalking; a brain that does not know it is sick (msgs 55, 56). | Written: `OMNI_V5_PLAN.md` §12. Self-check against physics and the outside watcher: stage 10. |
| 2.4 | The nervous system's diseases: a signal blocked, sent down the wrong pathway (msg 56). | **TO BUILD**: stage 6 (read-back of every write, mis-route guard). |
| 2.5 | Muscle ailments: sprained, torn, broken, cramp, nutrition, exercise (msgs 50, 57). | Written: `OMNI_V5_PLAN.md` §3, §19; the exercise drills are stage 6. |
| 2.6 | The skeleton that holds it all: the rack (msgs 57, 64). | Written: §6, §25; stage 8. |
| 2.7 | The gut: intake, digestion, routing nutrients, waste out, report back (heartburn, diarrhea) and heal itself (msg 58). | **PARTLY**: the Gut family is in the catalog (8 muscles, `realms/catalog_v5.csv`); the gut layer is stage 7. |
| 2.8 | The joints registry: every intersection logs the input, the ailment, the fix and the output (msg 59). | **TO BUILD**: stage 10 (the chain of custody). `OMNI_V5_PLAN.md` §18. |
| 2.9 | Self-repair: software heals; metal wears and a human replaces it (msg 59). | Written: §19. |
| 2.10 | Blood is the code; the heart; the skin; the senses (msg 64). | **PARTLY**: the Skin family is in the catalog (5 muscles); the layers are stage 8. |
| 2.11 | Each muscle knows its one job from the start, "not blind out the gate"; the nervous system computes locally and does not round-trip the brain; the signal moves at the speed of light; anticipation (msg 64). | Written: §24. **TO BUILD**: stage 6. |
| 2.12 | Different vessels, one DNA: car, boat, plane, train, rocket (msg 55). | Written: §14. |
| 2.13 | "Omni never assumes": every step closed-loop, read back (msg 63). | Written: §23. **TO BUILD**: stage 6 read-back. |

## 3. Control, safety and the human

| # | Order | Status |
|---|---|---|
| 3.1 | A physical kill switch on the outside of the system that puts everything back to native (msg 46). | **PARTLY**: software switch and heartbeat lease exist (`omnicompass/master.py`, `tools/omni_switch.py`); the physical switch is stage 10. |
| 3.2 | A switch per muscle and the whole-organism switch; the real threat is a bad actor taking the brain (msg 55). | **PARTLY**: per-knob native fallback and the master switch exist; the per-muscle panel switch is stage 10. |
| 3.3 | A tainted or hijacked brain must alert itself; monitors outside the body, like an operating room (msgs 46, 48). | **TO BUILD**: the outside watcher and the self-check, stage 10. |
| 3.4 | The DNA / seed: the same seed gives the same organism; two seeds can be crossed (msg 46). | **PARTLY**: the engine fingerprint is the seed's core (`tools/omni_version.py`); seed = fingerprint + dial + wiring map, stage 3/10. |
| 3.5 | The dial: Long-life, Balanced (default), Edge, Sprint; the owner may tune past health, "a brain tuned to burn will burn" (msg 46). | **PARTLY**: in the study; stage 3 in the engine. |
| 3.6 | Pushing hard never shortens its life, by default (msgs 43, 46). | **TO BUILD**: the wear gauges and the life rule, stage 4 (a new omnicompass/wear.py). |
| 3.7 | Who serves whom: muscles serve Omni, Omni serves the person who holds the switch (msg 46). | Written: §8, §12. |

## 4. One screen, monitors and self-wiring

| # | Order | Status |
|---|---|---|
| 4.1 | Build every monitor and knob the industry has, for every muscle (msgs 50, 53). | **PARTLY**: mapped muscle by muscle in `docs/omni_v5/CONNECTORS.md`; adapters are stage 11. |
| 4.2 | The babysitting tax: every monitor in one place, green/orange/red, a couple of engineers instead of one per muscle, counted as a benefit (msg 54). | Written: `CONNECTORS.md` "One screen, not a thousand", plan §28. **TO BUILD**: stage 10. |
| 4.3 | Self-wiring: drop Omni (with an AI) on a native stack and it wires itself (msg 55). | Written: §13. **TO BUILD**: stage 10 (auto-discovery). |
| 4.4 | Every muscle gets wired, even one that never needs a signal: "we never know when the wrong thing is eaten" (msgs 61, 62). | **DONE** in the modelled catalog: all 1,097 wired and watched; Omni acts on 208 of them, where it helps. |
| 4.5 | Ride on the real natives: DeepMind-style cooling, Kubernetes, Karpenter, KEDA, VPA, Google Autopilot, Datadog, Dynatrace Davis, New Relic, Moogsoft, NASA, Tesla, Oracle ADB; "real shit, not a model engine" (msg 61). | **PARTLY**: Kubernetes (HPA and cluster autoscaler), KEDA, PostgreSQL, MySQL, MongoDB, Redis, Kafka, CityLearn, pandapower, MuJoCo and PX4 run today on the live controllers. Karpenter is not run yet (first on KWOK, free, then Azure node auto-provisioning). The honest open/closed map is plan §22; the connectors are stage 11. |

## 5. The catalog and the organisms

| # | Order | Status |
|---|---|---|
| 5.1 | Six organisms, never five; the native identical in all six, every parameter, input and knob (msg 0). | **DONE**: all six in the official table. The four stacked keep each realm's own body on one clock, so every muscle in the stack runs exactly the native it runs in its own realm, plant by plant (checked on all 1,773 plants), in the v5 runner and the grid runner (`tools/run_realms_v5.py`, `tools/run_scale.py`). The tower is every muscle once in one body, so its couplings (heat into its rooms, load on its UPS) are the tower's own; each muscle's parameters and inputs are the same as everywhere else. |
| 5.2 | The add-ons in the realms: Karpenter (with a K), KEDA, Kafka, Redis (msgs 2, 11, 12). | **PARTLY**: in the catalog; KEDA, Kafka and Redis also run live; Karpenter's live run is open (4.5). |
| 5.3 | More than 945: "1,000 something"; "a thousand fifty"; more than 59 families; Linux kernel; AI training the biggest (msgs 65, 66, 69, 75, 76, 81). | **DONE** (12 Oct): 1,097 muscles in 70 families (`realms/catalog_v5.csv`): Linux Kernel & OS Control, AI Inference and AI Training the two biggest compute families, and the second wave: Financial Markets & Trading, Media Streaming & CDN, Game Servers (Agones), Blockchain & Ledger Nodes (never a consensus rule), CI/CD & Build Farms, security engines, MQTT brokers, DNS and mail caches, ROS 2, humanoids, PX4 and ArduPilot drones and swarms, edge sites; the GPU family named for the hardware; one numbering (the audited families 64 to 71). 0 of 1,097 LOSS or power given on the official table. |

## 6. The benchmarks

| # | Order | Status |
|---|---|---|
| 6.1 | Every benchmark run, nothing left out; one button (msgs 72, 78, 88). | **DONE** as code: `.github/workflows/v5-all-benchmarks.yml`, the map `docs/omni_v5/BENCHMARKS_V5.md` (23 free benchmarks on GitHub plus the GPU and the clouds). |
| 6.2 | The GPU: one chip, the 1,000 runs, the APU, all written "one shot, same mechanism" (msg 78). | **DONE** as code: `scripts/gpu_rented_run.sh`, `scripts/apu_run.sh`, the 1,000-copy runs in `six.yml`/`gpu-bench.yml`. |
| 6.3 | "Don't forget the 8-GPU benchmark" (msgs 86, 88). | **DONE** as code: one button, `.github/workflows/lambda-gpu.yml` (rents the 8-card machine, runs `scripts/gpu_8card.sh` at the exact commit, brings the results back, always gives the machine back; a dry run shows the price), also in the one-button workflow; needs the three Lambda secrets (`docs/omni_v5/BENCHMARKS_V5.md`, click by click). |
| 6.4 | The GPU run with the chip's own add-ons underneath and Omni on top (msg 15). | **PARTLY**: the operator's power cap underneath is in the one-chip test; the full add-on set is stage 11. |
| 6.5 | The organisms on a cloud and on a GPU chip, with Omni on each level (msg 16). | **PARTLY**: the six organisms with the real cluster inside, and at 1,000 copies with the real card inside, run today; stacked Omni levels are item 1.15. |
| 6.6 | Three clouds: Azure AKS, Google GKE, Amazon EKS (msgs 45, 72, 78); "the code written the same way as Azure's" (12 Oct). | **DONE** as code: `aks-metered.yml`, `gke-metered.yml`, `eks-metered.yml` (the bill tests and the organisms with the cluster inside at 1 to 1,000 copies), and the big machines: Azure's `big-organism-detached.yml`, Google's and Amazon's `cloud-organism.yml` (the same test). Azure runs on v5 since 12 Oct (the 40-machine fleet, the tower and the four stacked at 1,000 copies); Google and Amazon start when their secrets are in (`docs/GOOGLE_SETUP.md`, `docs/AMAZON_SETUP.md`). |
| 6.7 | All the AI benchmarks, metrics and receipts the AI world expects; SaaS products (msg 14). | **PARTLY**: vLLM serving and AI token generation in the GPU test; MLPerf Inference with power, SGLang, TensorRT-LLM/Triton, AI training runs, OpenSearch, Nginx, Spark and stream processing are open. |
| 6.8 | "All my benchmarks, all the muscles, all my organisms, all the versions, 1, 10, 100, 1,000, native and omni" (msg 87). | **PARTLY**: the grid runner runs v5 (`tools/run_scale.py --arm v5`, `six.yml` input `arm`, default v5), the six organisms at 1, 10, 100 and 1,000 copies and runs; the v5 grid runs on GitHub after this push. v1 and v3 grids stand in `results/scale/`; the all-versions table beside them is next. |
| 6.9 | Live benchmarks must run v5, not the v3 live law. | **PARTLY**: done for the live Kubernetes controller and the GPU governor (their compass law holds its balance point at the v5 edge, `omnicompass/edge.py`, the same code the modelled law runs) and for the six organisms with a real cluster or card inside (`tools/run_kil.py`, `tools/run_hil.py`: the v5 law, the v5 catalog, each realm's own body in the stack). The databases' adapters (PostgreSQL, MySQL, MongoDB, Redis, Kafka) are next (stage 11). |

## 7. How results are told

| # | Order | Status |
|---|---|---|
| 7.1 | Numbers must say what they mean against the world: "times over", value and benefit, not just "+0.3%" (msg 31). | **DONE** in the v5 table: energy saved beside v3's on the same seeds, and the times. |
| 7.2 | Show where native sits, the most it can do, and the bill at each point (msg 45). | **TO BUILD**: stage 3 (the Max curve and the bill). |
| 7.3 | The three-run wording must not sound approved by an outside party (msgs 5, 8). | **DONE** (12 Oct): no table or page says a result is "confirmed"; a reading says it is GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) (or the same in all three), and every three-run table carries "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results." with what preregistered means (the rules written in our own repository before the runs; nothing filed outside). The words live in `tools/readings.py`; every three-run tool, the index, the dossier, the benefit sheet and the wiring verdicts use them. Engine files, legal papers and the history keep their own words. |
| 7.4 | Parked machines at standby versus idle; is any machine ever just idle (msgs 6, 9). | Answered in the chat; both rows are shown in the fleet results. |
| 7.5 | The base load no knob can touch, explained (msg 34). | Answered; to go into the manual's reading guide. |

## 8. Legal

| # | Order | Status |
|---|---|---|
| 8.1 | License section 9: the right to change the terms without notice, restored (msg 3). | **DONE**: `LICENSE` section 9 "CHANGES". |
| 8.2 | Governing law Delaware; the company is in Florida (msg 7). | **DONE**: `LICENSE` 19.1-19.2. |
| 8.3 | The whole legal set at underwriter level, A+ (msg 4). | **DONE** on main (`LICENSE`, `NOTICE`, `DISCLOSURES.md`, the enterprise terms); the notice top and bottom of every output (`tools/legal.py`). |

## 9. The manual

| # | Order | Status |
|---|---|---|
| 9.1 | The manual is "almost more important than the engine": front matter, a chapter before the wiring explaining an organism, a stack and a cluster in body terms; 10th-grade English and engineer terms; the superheroes (msgs 55, 58). | **PARTLY**: written as plan §15, §17; the chapters are to be written into `docs/OMNI_COMPASS_MANUAL.md` and the PDF rebuilt. |
| 9.2 | A chapter "The brain you build": the dial, the default, what never changes, the kill switch, the immune reports, the warning. | **TO BUILD** (manual). |

## 10. Process

| # | Order | Status |
|---|---|---|
| 10.1 | Keep the scratch pad and the blueprint current; never lose what was said (msgs 67-71, 85). | **DONE** from 12 Oct: this ledger, updated with every change it describes. |
| 10.2 | Push everything, keep the old runs going, verify before every push (msgs 72, 73, 83). | Every push: `tools/release_manifest.py` under Python 3.12, 0 FAIL, then the GitHub verify run checked. |
| 10.3 | Lock the repository once everything is in (msg 64). | At the v5 freeze (stage 12). |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
