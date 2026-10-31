# Your own system through the core's Monte Carlo

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's words of 24 October: "if somebody wanted to theoretically hook up their own system and hook this to their stack and run
their own system through it, is wired into that other button, which is the simulation that's done within the GitHub."

A system file is a JSON object that writes your own stack as ranges of the engine's core (`omnicompass/core.py`): the same Monte
Carlo the live benchmark engine's monitor 4 draws (500 runs from the jump generator, the fourth-order Runge–Kutta step, 20 macro steps of 10
micro steps, native beside Omni-Compass on top), spread over your ranges instead of the engine's own. It is read as numbers only and
never run as code. Class S: the engine's own mathematics on draws, never a measurement of your stack. Wiring Omni-Compass onto the
stack itself is the plug of the Operator's Manual.

```json
{
 "name": "my stack",
 "about": "one line on what the ranges stand for",
 "state": {"U": [-1, 1], "E": [0, 1]},
 "params": {"beta_ext": [0.6, 1.0], "E_max": [1.0, 3.0], "mu": 2.5}
}
```

- **name**: 1 to 80 characters; the record is named after it.
- **state**: any of the six starting states, each a range `[low, high]` or one number: `E` (energy debt), `U` (order parameter: −1 and
  +1 are the two basins), `I_U` (the integral of need), `S` (stress), `B` (the bath) and `B_dot` (the bath's rate). A state left out keeps the
  engine's own range (E, I_U from 0 to 1; U, S, B, B_dot from −1 to 1).
- **params**: any of the 22 parameters of `omnicompass/core.py` `PARAMETER_RANGES`, each a range or one number; the rest keep the
  engine's own. Among them: `beta_int` and `beta_ext` (the demand into E from inside and outside), `E_max` (the headroom E is read
  against), `c`, `omega_B`, `Q_B` and `lambda_0` to `lambda_2` (the bath's swing: its strength, its frequency, its damping and what
  drives it), `mu` (the depth of the double well), `alpha_s`, `beta_s` and `delta` (the stress potential), `lambda_I` and `lambda_U`
  (the leaks of the need and of U).
- Every end is a finite number within ±10⁶ and low ≤ high. Unknown names are refused.

Run it three ways:

1. **In the live benchmark engine**: the Monte Carlo monitor's "Your own system" panel (section 1f): paste or edit the block, "Run it here"
   draws the runs in your browser through the page's own port of the core.
2. **On GitHub**: the same panel's "Run it on GitHub" copies the block and opens the **monte-carlo** workflow; press **Run workflow**,
   paste the block into **system**, choose the runs and the base, and run. The Python and the C++ twin of the core
   (`cpp/tools/core_runs.cpp`) run the same draws, the page's port is checked against them, and the record is committed to
   `results/core_runs/` with the run's link. A file committed under `systems/` runs on its own on every push that changes it.
3. **On your machine**: `python3 tools/core_runs.py --system systems/my_stack.json --runs 500 --base 1` and, with the C++ built
   (`cmake -S cpp -B cpp/build && cmake --build cpp/build --target oc_core_runs`), `--cpp cpp/build/oc_core_runs`.

`example_heavy_swing.json` is an example of the format, not any real stack.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
