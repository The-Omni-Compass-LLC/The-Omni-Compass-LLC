// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The immune system's self-knowledge, knob by knob (C++ twin of omnicompass/immune.py; tests/test_cpp_immune_parity.py): a knob
// redlining past its line that Omni-Compass's own pushing cannot bring back goes to native when native's twin reads it lower,
// and stays with Omni-Compass when native is not stronger. Read the two side by side: every line here has its Python line.
#pragma once
#include <optional>
#include <string>
namespace omnicompass {

struct ImmuneEvent {
  std::string what;              // "handed to native", "returned to Omni-Compass", "redlining, native not stronger: stays"
  double p_omni{}, p_native{};   // rounded to six decimals, as the Python's audit
  long redline_decisions{-1};    // -1: not in the event
  long hold{-1};
};

class Immune {
 public:
  explicit Immune(long streak = 3, double relief = 0.05, double margin = 0.05, long hold = 10, long hold_max = 160);
  // one decision: "omni" or "native", and the event for the audit
  std::string tick(double p_omni, double p_native, bool moved, bool at_limit, std::optional<ImmuneEvent>& event);
  std::string mode{"omni"};
  long red{0}, left{0}, hold_len, quiet{0}, handbacks{0};
  std::optional<double> red_from;
 private:
  long streak_, hold0_, hold_max_;
  double relief_, margin_;
};

}  // namespace omnicompass
// © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
