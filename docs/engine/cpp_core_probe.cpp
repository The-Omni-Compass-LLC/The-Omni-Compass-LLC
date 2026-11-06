// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The C++ twin of the engine's six-state core (cpp/src/core.cpp) answering the live engine page's check
// (docs/engine/check_live_engine.py): each input line is a state (E U I_U S B Bdot), the parameters the page names
// (alpha_E mu E_max lambda_U sigma_1 delta lambda_I alpha_s beta_s gamma_c omega_B Q_B lambda_0 lambda_1 lambda_2 c
// beta_int beta_ext), then t, h and u; each output line is omnicompass::derivatives and omnicompass::rk4_step there.
#include "omnicompass/core.hpp"
#include <cstdio>
#include <iostream>

int main() {
  using namespace omnicompass;
  State s; Parameters p; double t, h, u;
  while (std::cin >> s.E >> s.U >> s.I_U >> s.S >> s.B >> s.B_dot >> p.alpha_E >> p.mu >> p.E_max >> p.lambda_U >> p.sigma_1
                 >> p.delta >> p.lambda_I >> p.alpha_s >> p.beta_s >> p.gamma_c >> p.omega_B >> p.Q_B >> p.lambda_0 >> p.lambda_1
                 >> p.lambda_2 >> p.c >> p.beta_int >> p.beta_ext >> t >> h >> u) {
    const State d = derivatives(s, p, t, u), n = rk4_step(s, p, t, h, u);
    std::printf("%.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g %.17g\n",
                d.E, d.U, d.I_U, d.S, d.B, d.B_dot, n.E, n.U, n.I_U, n.S, n.B, n.B_dot);
  }
  return 0;
}
