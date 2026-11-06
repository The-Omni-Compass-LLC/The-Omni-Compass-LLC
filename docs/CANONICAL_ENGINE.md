# Canonical engine declaration

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

One engine runs Omni-Compass, and every result in this repository comes from it. This page names it, gives its
equations exactly as the code computes them, and names every other form as a variant. Where any document, manual, chart
or filing states the equations differently, this page and the file it fingerprints are what the software runs.

## 1. The canonical engine: `symmetric_verified`

| | |
|---|---|
| Name | `symmetric_verified` (`omnicompass/configurations.py`, `DEFAULT`) |
| Code | `omnicompass/core.py` (Python), `cpp/src/core.cpp` (C++ twin, sealed in `results/SEAL.json`) |
| Fingerprint | SHA-256 of `omnicompass/core.py`, recorded in `results/PREREGISTRATION.json` and `RELEASE_MANIFEST.json`; checked by `verify.py` |
| Evidence | every model, benchmark, live Kubernetes run and GPU harness in this repository |

State: E (deviation), U (coherence), I[U] (unmet-need integral), S (structural stress), B and Ḃ (the bath).

```
v[eff]   = cos(ω[B] t / 2) · c · tanh(λ₀ + λ₁ (U − 0.5) + λ₂ S)        (spinor closure, 720°)
dE/dt    = −α[E] E + β[int] + β[ext] + v[eff]
dU/dt    = μ U (1 − U²) − (dE/dt) / E[max] − λ[U] U + u                  (symmetric double well)
dI[U]/dt = (1 − U) − σ₁ E − δ S − λ[I] I[U]
dS/dt    = δ − αₛ S − (3/4) βₛ S²                                        (gradient of Φ)
dB/dt    = Ḃ
dḂ/dt    = γ[c] δ S − (ω[B] / Q[B]) Ḃ − ω[B]² B
Φ(S)     = αₛ S² / 2 + βₛ S³ / 4 − δ S
```
u is the controller's command, `K[P] (target − U) − drift`, bounded by `U_AUTHORITY`; integration is RK4 with the
macro and micro steps of `omnicompass/core.py`.

### Mechanism identity

`results/MECHANISM_IDENTITY.json` (`tools/mechanism_identity.py`) fingerprints the mechanism
M = (F, Theta, C, h, G, M[act], dt, A) component by component: state law, parameters, controller, observation map,
authority law, actuator map, execution timing, shield. `verify.py` fails if any component changes without the record
being rewritten. Every evidence claim names the mechanism id that produced it; "the eight-line engine" alone names none.

| Configuration | Mechanism id | Role |
|---|---|---|
| `symmetric_verified` | `b10f1b4128ff7fc76b8865e0d1c486817fe56ec347f8d105bcaa657904cb61f2` | canonical |
| `printed_eight_line` | `623934cc31e964120aa7e8a22d17927fef9a7588e599b089b8ae545ec240ef12` | named alternative embodiment |

On the frozen 500-fixture population (`benchmarks/core_evidence.py`, seed 223387268), both are executable and neither
is a stand-in for the other:

| | finite | CONVEY-5 | CERT-10 | mean final target error | mean integrated abs(u) | max abs(u) |
|---|---:|---:|---:|---:|---:|---:|
| `symmetric_verified` | 500/500 | 500/500 | 500/500 | 7.48e-5 | 0.878 | 13.93 |
| `printed_eight_line` | 500/500 | 500/500 | 500/500 | 5.13e-6 | 11.79 | 18.87 |

The printed form reaches its target more tightly with about 13 times the control effort. The structure is Option A:
one canonical configuration, one named alternative; no equivalence is claimed.

## 2. Variants

### `printed_eight_line` (the printed chart)
Implemented in `omnicompass/configurations.py`, checked against the printed plate (`tests/test_engine_configurations.py`),
**not benchmarked**: no result in this repository comes from it.

```
v[eff]   = c · tanh(λ₀ + λ₁ (U − Uₜ) + λ₂ S)                             (no spinor factor)
dE/dt    = −α E + β[int] + β[ext] + v[eff]
dU/dt    = α (1 − U) − (dE/dt) / E[max] − k U (1 − U) + u                (logistic)
dI[U]/dt = (1 − U) − σ₁ E − δ S                                          (no λ[I] term)
dS/dt, dB/dt, dḂ/dt as in section 1
```

Differences from the canonical engine: logistic U instead of the symmetric double well; no spinor factor; a general
target Uₜ; no λ[I] damping; α in place of α[E]. α[U] and k enter the printed form; they do not enter the
canonical engine.

## 3. What would change this declaration

Promoting a variant to canonical needs, in one commit: the variant run through every harness beside the canonical
engine, its results reported next to the canonical results, this page and `RELEASE_MANIFEST.json` updated, and the
preregistration amended on record (`results/LOCK_AMENDMENTS.json`). Until then the canonical engine is
`symmetric_verified`.

## 4. Open mathematical items (from `docs/FORMAL_STATUS.md` and the handoff)

- A global stability proof of the forced six-state system is not closed. What is held on the U channel is proved in
  `docs/TRACKING_THEOREM.md`: unsaturated exponential tracking; the saturated case under a drift bound that holds over
  the declared box (F[bar] = 16.86 < 25); the sampled-data bound of the executed RK4 controller; admissibility.
- Candidate routes: the Unified Circle Principle on a region; Theorem 5.6 of the Closed Structure, if its core maps onto
  (E, U, I[U], S, B).

## 5. For filings

Which form a patent or copyright filing claims as the principal embodiment is a decision for The Omni-Compass LLC and
its counsel. Whatever that decision, the software described by this repository runs the canonical engine of section 1,
and a filing that claims the printed form should name `symmetric_verified` as the embodiment that has been implemented
and tested, or the printed form should be benchmarked first (section 3).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
