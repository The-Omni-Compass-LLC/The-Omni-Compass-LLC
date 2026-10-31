// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omnicompass/immune.py. Read the two side by side: every line here has its Python line.
#include "omnicompass/immune.hpp"
#include "omnicompass/verdict.hpp"
#include <algorithm>
namespace omnicompass {

Immune::Immune(long streak, double relief, double margin, long hold, long hold_max)
    : hold_len(hold), streak_(streak), hold0_(hold), hold_max_(hold_max), relief_(relief), margin_(margin) {}

std::string Immune::tick(double p_omni, double p_native, bool /*moved*/, bool at_limit, std::optional<ImmuneEvent>& event) {
  event.reset();
  const bool stronger = p_native < p_omni * (1.0 - margin_);
  if (mode == "native") {
    left -= 1;
    quiet += 1;
    if (left > 0) return "native";
    if (p_omni <= 1.0 && p_omni < p_native * (1.0 - margin_)) {
      mode = "omni"; red = 0; red_from.reset();
      if (quiet >= 2 * hold_len) hold_len = std::max(hold0_, hold_len / 2);
      event = ImmuneEvent{"returned to Omni-Compass", py_round(p_omni, 6), py_round(p_native, 6)};
      return "omni";
    }
    left = 1;
    return "native";
  }
  if (p_omni > 1.0) {
    red += 1;
    if (!red_from) red_from = p_omni;
  } else {
    red = 0; red_from.reset();
    quiet += 1;
    return "omni";
  }
  if (red < streak_) return "omni";
  const bool stuck = at_limit || p_omni > *red_from * (1.0 - relief_);
  if (!stuck) return "omni";
  if (stronger) {
    mode = "native"; left = hold_len;
    event = ImmuneEvent{"handed to native", py_round(p_omni, 6), py_round(p_native, 6), red, hold_len};
    handbacks += 1;
    hold_len = std::min(hold_max_, hold_len * 2);
    quiet = 0; red = 0; red_from.reset();
    return "native";
  }
  event = ImmuneEvent{"redlining, native not stronger: stays", py_round(p_omni, 6), py_round(p_native, 6), red, -1};
  return "omni";
}

}  // namespace omnicompass
// © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
