# Wiring Omni-Compass into your Kubernetes

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Before you wire anything:** read [`DISCLOSURES.md`](../DISCLOSURES.md). Omni-Compass acts only through the wires it is given; it cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the first presumption is wiring: check the installation with section 4.5 of the manual (*Wired right or wired wrong*).

> **The current manual is `docs/INTEGRATION_MANUAL.md`** (every stack, every level, every switch). This page is kept for
> reference; where the two differ, the integration manual is current.

> **Which knobs to wire in at all:** `docs/WIRING_VERDICTS.md` gives every knob in every published result one of three
> words from the tables themselves: **write** (wire both ways), **watch** (wire out only: Omni reads, the native controller
> lives by itself) or **operator's choice** (a trade). A knob that showed nothing, or lost, stays native.
> **How to wire for superiority:** every knob starts in watch (wire out only); an observation run shows what native does
> alone; then the brain's own verdict decides on the knob, in real time, whether a notch pays before it is written
> (`tools/knob_verdict.py` around the engine's verdict; the manual, section 6.4); a knob that cannot prove it pays stays
> native, and the operator's setting is always free. Where that verdict stands today, knob by knob, is the last table of
> `docs/WIRING_VERDICTS.md`.

> The full step-by-step manual, with the switch, the living band, parking and the pod reflex, is
> `docs/OPERATOR_MANUAL.md`. This page is the short version.

**Three stages.** Each stage adds only the permissions it needs. A stage is promoted only after its evidence is in,
and the reset works at every stage:

```
kubectl -n omni-compass exec deploy/omni-compass -- touch /tmp/omni.kill
```

The switch is one human-operated switch for the whole harness (OFF restores every HPA target, replica range, CPU
limit and cordon Omni-Compass changed, and records it; removing the file turns Omni-Compass back ON). It never fires by
itself and never switches off one module: a failed decision is skipped, boundaries are held by the living band.

## 0. Build the image
```
docker build -f deploy/Dockerfile -t <registry>/omni-compass:<tag> .
docker push <registry>/omni-compass:<tag>
```
**What the image contains.**
- The engine.
- The nervous system.
- The live controller and its levers.
- The frozen closure-law setting (`/app/law/closure.json`).

**How it runs.** As a non-root user, with a read-only root filesystem and no Linux capabilities.

## 1. Shadow: read-only, decides and logs, never writes
```
kubectl apply -f deploy/install/omni-compass.yaml      # set the image line first
kubectl -n omni-compass logs deploy/omni-compass -f
```
**Proof of read-only.** `scripts/pilot_shadow.sh` runs the same stage from a workstation with `kubectl auth can-i`
receipts that the identity cannot write, and writes `SHADOW_REPORT.md`.

**Run length.** One to two weeks.

**Pass condition.** Zero writes, and recommendations you agree with.

## 2. Target: Omni-Compass sets each HPA's CPU target
```
kubectl apply -f deploy/rbac-target.yaml               # adds: patch horizontalpodautoscalers
kubectl -n omni-compass patch deploy omni-compass --type=json -p \
  '[{"op":"replace","path":"/spec/template/spec/containers/0/args/1","value":"target"}]'
```
**What happens.** The HPAs keep scaling pods. Omni-Compass only moves their target within bounds.

**The SLO reflex.** Add `--latency-file` and `--slo-ms`, and the target is never tighter than native while the SLO is
breached.

**Pass condition.** Latency never behind native, and fewer pod-hours.

## 3. Node pool: Omni-Compass sizes the node pool
**Add permissions.** `patch nodes`, `create pods/eviction` (`deploy/kind/rbac-omni.yaml` is the tested example).

**Set the mode.** `--mode nodepool --node-scale-cmd "<your pool resize command with {n}>"`. Examples of the resize
command:
- a Karpenter NodePool limit;
- a cloud node-group size;
- `scripts/kind_nodepool.sh` on kind.

**What guards a release.** The machine organ gives a node back only when all of these hold:
- every sense is live;
- its last order landed;
- pods are not scaling up;
- nothing is pending;
- the remaining nodes stay at or below the engine's target utilisation.

A PodDisruptionBudget on each service is required, because drains go through the eviction API.

**Optional levers.** Each has its own flag and permissions, and all are listed in `omni_controller/muscles.py`:
- right-sizing;
- cold start;
- batch pacing;
- agent containment;
- cooling;
- CPU frequency.

## Evidence, and where it is
| Evidence | File |
|---|---|
| The controller, every lever and the Unified Control Switch on real Kubernetes (kind) | `results/live/LIVE_LEVERS_2_NERVOUS.txt` |
| Read-only shadow on real Kubernetes: every decision logged, 0 writes | `results/live/LIVE_SHADOW_1.txt` |
| Least-privilege identity receipts | `rbac_omni.txt` in every live run |
| Native vs Omni on top vs Omni alone, paired on one machine, real Kubernetes | `results/live/LIVE_PAIRED.md` |
| The full wiring manual | `docs/OPERATOR_MANUAL.md` |
| The frozen engine's results, three runs each, read by rule | `results/live/V1_*.md`, `results/live/V3_*.md`; `docs/OMNI_V1.md`, `docs/OMNI_V3.md` |
| The same wiring on Azure's managed Kubernetes (the bill), a database pooler, a rented machine, the simulators, a message broker's consumer group, a cache's memory ceiling, a drone swarm's autopilot | the manual, chapter 7 (`docs/OMNI_COMPASS_MANUAL.md`) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
