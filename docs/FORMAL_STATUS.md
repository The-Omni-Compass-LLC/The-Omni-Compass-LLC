# Formal status

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Not a global-stability proof of the forced six-state system. For exact domain assumptions and machine-proof obligations read `docs/ENGINE_PROOFS.md`, then `docs/TRACKING_THEOREM.md` and `docs/EVIDENCE_LEDGER.md`. A claim called T is conditional on the specified solver/interval-arithmetic certificate, equations, numerical semantics and parameter box; this summary does not independently rerun those certificates.

Held:

- Isolated S-flow is the gradient of Phi (same formula in both cores).
- (T) Unsaturated: dU/dt = KP (sigma − U); V = e²/2 has dV/dt = −KP e² on that channel (Theorem 1).
- (T) Saturated, with the U drift bounded by F[bar] < U_AUTHORITY: V decreases wherever e ≠ 0; over the declared
  parameter box F[bar] = 16.86 < 25, so this holds over the box in continuous time (Theorem 2).
- (T, constant computed) Sampled-data RK4 controller: e_(k+1) = 0.88 eₖ + dₖ; with epsilon_h computed over the
  frozen fixtures (V), the ultimate bound 0.0315 lies inside the 0.10 basin (Theorem 3).
- (T continuous, V on frozen fixtures; conditional computer-assisted T for named coordinates) Admissibility: the later `docs/ENGINE_PROOFS.md` states E1–E2 (E), S1 (S), I1 (I[U]) and U1–U5 (U) over its declared admissible start set, with outward-rounded intervals / SMT obligations. The RK4 sampled U-error ultimate bound is at most 0.0677 on that set. This is **not** the older claim of monotone discrete U error and not a global closed-loop external plant theorem.
- (T conditional on the named engine proof) B1 bounds the damped bath under bounded S; it does **not** supply an explicit numerical bath-amplitude bound or convergence of the full forced system.

Open:

- Independent rerun and machine checking of the stated whole-domain certificates on the current frozen engine, including exact hypotheses, floating-point semantics and non-vacuous premises. The **older blanket open statement** about all discrete bounds is superseded only for E1–E2, S1, I1, U1–U5 and B1 on their declared domains; it is not a new proof of unrestricted six-state convergence.
- CERT-10 for every start in the admissible domain; the current worst-case U5 entry argument guarantees at least nine macro-steps, not ten. Starts below S₋ are excluded.
- Inheritance embedding / intertwining residual against a real plant (Closed Structure Def. 11.1): instrumented in
  the GPU bench (`tools/gpu_reps.py`, representation fidelity), not yet measured on a card.
- Mapping of monograph Theorem 5.6 onto (E,U,I[U],S,B).
- A tracking bound for printed_eight_line (logistic U drift).

Default core remains symmetric_verified (mechanism id in `results/MECHANISM_IDENTITY.json`).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
