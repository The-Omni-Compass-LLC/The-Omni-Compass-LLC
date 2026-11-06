# Intel RAPL evidence specification

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


RAPL is CPU/package-side energy and power-budget infrastructure. It is not a GPU meter and not a wall meter.

## Meter-first path
Discover Linux powercap zones and record each zone's `name`, `energy_uj`, and `max_energy_range_uj`. Package zones are summed across sockets; DRAM and psys remain separate evidence scopes.

For a counter with range `R`:

`dE_J = ((E_end_uJ - E_start_uJ) mod R) * 1e-6`

Average power over the arm is derived from energy and elapsed time:

`P_avg_W = dE_J / dt_s`

The GPU experiment uses RAPL as an observer only. No RAPL value is added to GPU board energy and called wall energy. A PDU/smart-plug meter remains the whole-machine evidence source.

## Cap path, later
Where exposed, `constraint_0_power_limit_uw` / `constraint_0_time_window_us` and `constraint_1_*` are Linux powercap constraints. Any future CPU-cap muscle must snapshot, write, verify, and restore the applicable constraint, and must first establish that no platform daemon owns the same control surface. Raw MSR access is diagnostic fallback, not the production governor interface.

## Evidence labels
- `package-*`: CPU package scope.
- `dram`: DRAM domain when hardware/kernel exposes it.
- `psys`: wider platform/system scope on supporting platforms; not equivalent to a calibrated wall PDU.
- missing/unreadable counter: `UNAVAILABLE`, never estimated.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
