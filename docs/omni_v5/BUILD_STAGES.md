# Omni v5 — the build program (referee level, staged, each stage verified before the next)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

The v5 engine is built as numbered stages, the way v4 was (3, 4a…4e). **Every stage is additive and verified before the
next; the frozen v3 engine on `main` is not touched until v5 is complete, every result is rerun, and the verifier is 0
FAIL.** This is the discipline the standing orders require ("never change the engine without telling the founder first";
"verify 0 FAIL"; "every result run again on the new engine"; "the founder hears what a result says before it goes up").
Each stage lists: files, the math/physics, the test, the acceptance bar, and the rerun it triggers.

## Status
- **Stage 0 — DONE, pushed to branch `v5`.** The whole design: `OMNI_V5_PLAN.md`, `CONNECTORS.md`, the study that produced
  the modelled numbers (`study/`). Legal 0 problems; release manifest matches.
- **Stage 1 — DONE.** The v5 compass law is in the engine: `realms/compass_arm_v5.py`, with its arm in `realms/harness.py`
  (additive; v3's arms are byte-unchanged, so v3's stored results stand). The checkout reads **omni-v5**
  (`tools/omni_version.py`, `OMNI_V5.json`); v1, v2 and v3 stay frozen for their results. While v5 is in development its
  fingerprint is re-declared on each engine change, and no v5 result is published until the freeze. Do-no-harm is proven
  on every muscle by `tests/test_compass_arm_v5.py`. Re-declared on 12 October: the blanket gates of the first v5 engine
  (every generating unit's loop, every power cap, every inverter held native) are replaced by physics floors (the loop
  reach, the cooling headroom's fall read ahead, the latency floor, the power cap only where a pool's line outlasts a
  decision, a cloud pool's machine hand-back left to its autoscaler); the gate on generating units alone had thrown away
  almost all of v5's saving (`docs/OMNI_V5.md`, the amendment).
- **Stage 9 — DONE (two waves).** The v5 catalog `realms/catalog_v5.csv`: 1,097 muscles in 70 families (v3's 945 plus
  Linux Kernel & OS Control, Serverless & FaaS, Virtualization & Hypervisor, Content Delivery & Edge Cache, Gut, Skin; then
  Financial Markets & Trading, Media Streaming & CDN, Game Servers, Blockchain & Ledger Nodes, CI/CD & Build Farms and
  additions to seven families). The official v5 table: `results/realms_v5/REALMS_V5.md`, all six organisms superior
  within guardrails, 0 of 1,097 away from their aims;
  the whole tower saves 0.99% of its energy against v3's 0.33% on the same seeds (3.0 times), the four stacked 0.99% against 0.33% (3.0 times), Energy / Facility 1.00% against 0.33% (3.0 times). Inside the organisms v5 leaves 1 to 3 plants per organism (8 in the four stacked, which are the four realms together) one decision over their line (all of them UPS or
  distribution plants it never touches, moved by the body's power swing), against v3's 13 to 35 (83 in the four stacked);
  seven of the eight right after the safety cutoff (the hand-back), one while Omni runs; the strict body guard and its
  cost are measured and held for the founder (`docs/OMNI_V5.md`).
- **Benchmarks — written.** Google GKE and Amazon EKS paired runs, the AMD APU adapter, the realms-v5 workflow and one
  button for every benchmark (`docs/omni_v5/BENCHMARKS_V5.md`). The live benchmarks measure the v5 law only after stages
  6–11 port it into the live controllers.

## Stages to build (each: files → math → test → acceptance → rerun)
2. **Edge & centre as the only two guards, generalised off the model presets.** Files: realms/compass_arm_v5.py,
   `omnicompass/compass_law.py` (band/cushion read-back). Math: cushion = climb×reaction + z·wobble per knob; centre =
   release_safe + Lindley hole. Test: no muscle over its edge, none stuck in a hole, across all 59 families × seeds.
   Accept: 0 muscles behind native on misses at equal work. Rerun: six organisms, 12 seeds, both hours.
3. **Max mode + the dial (Save→Balanced→Edge→Sprint) + the bill.** Files: new omnicompass/dial.py,
   realms/compass_arm_v5.py, `tools/run_scale.py` (a `--dial` arm, a load sweep). Math: run each pool to its edge
   utilisation + pre-warm; bill = work − energy − wear − risk. Test: at equal service quality v5 carries ≥ native load;
   at 2× load misses ≤ native. Accept: +work shown with its wear/energy bill, never behind native. Rerun: the Max
   sweep on six organisms.
4. **Wear / health gauges + the life rule.** Files: new omnicompass/wear.py. Math: Arrhenius (silicon), Coffin–Manson
   (thermal cycles), battery cycle+calendar, motor/fan. Test: no part aged faster per unit work than native unless the
   dial is turned past it. Accept: life-used reported per muscle; life rule holds at Balanced. Rerun: dial sweep with wear.
5. **The immune system (specific, no autoimmune) + fever + cancer isolation.** Files: new omnicompass/immune.py,
   `realms/harness.py` hook. Math: per-muscle learned physics band; foreign = two signatures together (e.g. busy power +
   ~0 work); quarantine→native; memory. Test: inject runaway/dead-sensor/foreign-writer → flags only the sick muscle, 0
   false positives, body returns to health. Accept: proven in sim already (`study/immune.py`); port + test in-repo.
6. **The nervous system: closed loop, read-back, local reflexes, muscle identity, mis-route guard.** Files: new
   omnicompass/nerve.py, omnicompass/wire.py (read-back already). Math: never-assume (count only measured returns);
   typed muscles; stale/inverted/mis-routed path → native. Test: a dropped/inverted/mis-routed signal never books a gain
   and sends the muscle native. Accept: no gain counted without a measured return.
7. **The gut: intake→digest→route→waste; indigestion self-heal.** Files: new omnicompass/gut.py. Math: intake pacing,
   dead-letter/GC/retry-cap/TTL, waste before it backs up. Test: a poison/retry-storm input is eliminated before disk/mem
   /queue overrun; the body reports it. Accept: no toxic buildup; self-heal logged.
8. **Skeleton / blood / skin / heart / senses as first-class layers.** Files: omnicompass/body.py (extend). Math: the
   skeleton limit caps every muscle on it; blood = data+power vital; heart = loop clock (arrhythmia watch); skin =
   perimeter; senses = external forecasts feeding anticipation. Test: a bone fracture fails muscles over; a blood/heart
   stall is a vital alarm. Accept: shared edges honoured; vitals watched.
9. **The new muscle families → catalog past 1,000 (DONE: 1,097 in two waves).** Files: `realms/presets.py`, `realms/catalog.csv`,
   `docs/REGISTER.md`, `docs/MUSCLE_CATALOG.md`. Add: Serverless/FaaS, Virtualization/hypervisor, Network fabric/SDN/LB/
   CDN, Gut/data-plane controls, Skin/perimeter. Test: catalog loads, each new muscle read-write-read-back. Accept:
   distinct count locked (~1,005–1,065); AI Training stays family 2, AI Inference family 1.
10. **The joint registry (chain of custody) + the one-pane monitor + self-wiring (auto-discovery) + outside watcher +
    physical kill switch.** Files: new omnicompass/registry.py, tools/omni_panel.py, omnicompass/discover.py,
    omnicompass/watcher.py, `tools/omni_switch.py` (extend). Test: replay any input's path; watcher cuts Omni below
    native; lease returns all native on kill. Accept: babysitting-tax saving measured; green/yellow/orange/red tiles.
11. **Connectors to the real open natives.** Files: `omnicompass/connectors/*` (one adapter per muscle, behind the plug).
    Build on the real open systems named in `CONNECTORS.md` (k8s/Karpenter/KEDA, vLLM/Triton, Postgres/MySQL/Mongo/Redis,
    Spark/Kafka/OpenSearch/Nginx, Prometheus/OTel, EnergyPlus/BOPTEST/Sinergym, PyBaMM, GridLAB-D, NASA F´/cFS). Test:
    each adapter read-write-read-back against its real native in CI (free ones) and on cloud (metered).
12. **Freeze v5: fingerprint, version tool, rerun everything, verifier 0 FAIL, merge to main.** Files: `OMNI_V5.json`,
    docs/OMNI_V5.md, `tools/omni_version.py`, `RELEASE_MANIFEST.json`. Rerun: every benchmark on v5 (CPU first), A/B/C,
    the index; the founder hears each result before it goes up. Then GPU on Lambda, one exact commit, add-ons on.

## What is NOT stood in
None of stages 2–12 are claimed done until their test passes and their rerun is in. Modelled numbers stay class S; the
real proof is the clusters and the GPU. The clouds (Azure/GCP/AWS) start when their credentials are in GitHub secrets
(never asked for, never echoed); GPU waits for the CPU side and one exact commit, per the standing orders.

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
