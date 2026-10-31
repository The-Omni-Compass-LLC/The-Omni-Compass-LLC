# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The immune system's self-knowledge, knob by knob (the founder's order of 25 October): Omni-Compass knows when a knob it holds
is redlining out of its band; if its own pushing cannot bring the knob back and native is stronger there, it hands the knob to
native itself; if native is not stronger, it stays, because redlining less than native would is still a benefit against native.

  "OmniCompass's mechanism must know when something is redlining out of its band when OmniCompass is on it. And if OmniCompass
  couldn't fix it to stop it redlining, then OmniCompass's own mechanism must know that if native is better, then it switches
  itself to native. If native is not better, well, then it'll stay."

Each decision a knob gives three readings:

  p_omni     the knob's gauge against its own line with Omni-Compass's setting, as a ratio: 1 is on the line, over 1 is redlining
  p_native   the native twin's reading of the same moment under native's own setting (the caller's twin of the native rule)
  moved      Omni-Compass changed the knob this decision
  at_limit   Omni-Compass's push on the knob is at the knob's own limit (it cannot push further)

The rule (all in decisions, nothing tuned to a result):

  redlining   p_omni > 1 for `streak` decisions in a row
  stuck       redlining, and Omni-Compass's pushing has not brought it back: at its limit, or p_omni has not fallen by `relief`
              (a fraction of its reading when the redline began) since then
  stronger    native's twin reads lower than Omni-Compass by more than `margin`: p_native < p_omni · (1 − margin)
  hand back   stuck and native stronger: the knob goes to native and stays there `hold` decisions, the hold doubling for each
              hand-back in a row (up to `hold_max`) and halving after a quiet hold
  stay        stuck and native not stronger: Omni-Compass keeps the knob (it redlines less than native would)
  return      after the hold, while native holds the knob: Omni-Compass takes it back only when its own twin reads lower than
              native's by the same margin and nothing redlines with it

The nervous system carries the answer to the organ (omnicompass/nervous_system.py, `native_hold`): an organ handed to native has
no authority of Omni-Compass's until it is returned. The C++ twin is cpp/src/immune.cpp (tests/test_cpp_immune_parity.py)."""
from __future__ import annotations

from typing import Dict, Optional, Tuple


class Immune:
    """One knob's self-knowledge. tick() answers ("omni" or "native", the event for the audit or None)."""

    def __init__(self, streak: int = 3, relief: float = 0.05, margin: float = 0.05, hold: int = 10, hold_max: int = 160):
        self.streak, self.relief, self.margin = int(streak), float(relief), float(margin)
        self.hold0, self.hold_max = int(hold), int(hold_max)
        self.mode = "omni"
        self.red = 0                      # decisions in a row over the line, with Omni-Compass on the knob
        self.red_from: Optional[float] = None   # p_omni when the redline began
        self.left = 0                     # decisions of the hold still to run
        self.hold_len = int(hold)         # the next hold's length
        self.quiet = 0                    # decisions since the last hand-back
        self.handbacks = 0

    def tick(self, p_omni: float, p_native: float, moved: bool = False, at_limit: bool = False) -> Tuple[str, Optional[Dict]]:
        stronger = p_native < p_omni * (1.0 - self.margin)
        if self.mode == "native":
            self.left -= 1
            self.quiet += 1
            if self.left > 0:
                return "native", None
            if p_omni <= 1.0 and p_omni < p_native * (1.0 - self.margin):
                self.mode, self.red, self.red_from = "omni", 0, None
                if self.quiet >= 2 * self.hold_len:          # a quiet hold: the next one is halved
                    self.hold_len = max(self.hold0, self.hold_len // 2)
                return "omni", {"immune": "returned to Omni-Compass", "p_omni": round(p_omni, 6), "p_native": round(p_native, 6)}
            self.left = 1                                     # native still the stronger: held, read again next decision
            return "native", None
        if p_omni > 1.0:
            self.red += 1
            if self.red_from is None:
                self.red_from = p_omni
        else:
            self.red, self.red_from = 0, None
            self.quiet += 1
            return "omni", None
        if self.red < self.streak:
            return "omni", None
        stuck = at_limit or p_omni > self.red_from * (1.0 - self.relief)
        if not stuck:
            return "omni", None
        if stronger:
            self.mode, self.left = "native", self.hold_len
            event = {"immune": "handed to native", "p_omni": round(p_omni, 6), "p_native": round(p_native, 6),
                     "redline_decisions": self.red, "hold": self.hold_len}
            self.handbacks += 1
            self.hold_len = min(self.hold_max, self.hold_len * 2)
            self.quiet, self.red, self.red_from = 0, 0, None
            return "native", event
        return "omni", {"immune": "redlining, native not stronger: stays", "p_omni": round(p_omni, 6),
                        "p_native": round(p_native, 6), "redline_decisions": self.red}


# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
