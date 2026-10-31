// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
// oc_core_runs INJECTION.txt CANON.txt FULL.txt : the core's Monte Carlo, the Python's draws in, the mechanism put on in C++ (the
// founder's words of 24 October: "Monte Carlo 500 Runge-Kutta, my C++ and Python linked together, ran through as a button").
// INJECTION.txt is written by tools/core_runs.py: one line a run, its starting state and its 22 parameters drawn from the jump
// generator, the Python's own numbers written to round-trip exactly. Each run goes through the C++ twin of the engine's core
// (cpp/src/core.cpp, sealed: omnicompass::derivatives and omnicompass::rk4_step, the six state equations and the fourth-order
// Runge-Kutta step), driven here in omnicompass/core.py simulate()'s own loop: 20 macro steps of 10 micro steps, the bounded command
// held across the four stages, the five-in-a-row (convey) and ten-in-a-row (cert) predicates, in the four ways the Python runs:
// controlled toward the nearest basin, uncontrolled (u = 0), aimed at the far basin, and with the double well's mu at 0. Out:
// CANON.txt, one line a run and a way exactly as tools/core_runs.py canonical() writes it (six decimals), whose SHA-256 is the
// C++ digest; FULL.txt, every U at full precision for the run-by-run comparison.
#include "omnicompass/core.hpp"
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace omnicompass;

namespace {
struct Run { long k{}; unsigned long long seed{}; State x0{}; Parameters p{}; };
struct Way { std::vector<double> U; int convey{}, cert{}; };
const char* WAYS[4] = {"controlled", "uncontrolled", "wrong_target", "controlled_mu0"};

double num(std::istream& in) { std::string t; if (!(in >> t)) throw std::runtime_error("the injection ended early"); return std::strtod(t.c_str(), nullptr); }
std::string word(std::istream& in) { std::string t; if (!(in >> t)) throw std::runtime_error("the injection ended early"); return t; }

std::vector<Run> read_injection(const std::string& path) {
  std::ifstream in(path); if (!in) throw std::runtime_error("cannot read " + path);
  if (word(in) != "OCCORE" || num(in) != 1) throw std::runtime_error("not an injection of tools/core_runs.py (OCCORE 1)");
  const long n = static_cast<long>(num(in));
  std::vector<Run> runs; runs.reserve(n);
  for (long i = 0; i < n; ++i) {
    Run r; if (word(in) != "R") throw std::runtime_error("run line expected"); r.k = static_cast<long>(num(in)); r.seed = std::strtoull(word(in).c_str(), nullptr, 10);
    r.x0 = {num(in), num(in), num(in), num(in), num(in), num(in)};
    Parameters& p = r.p;   // omnicompass/core.py PARAMETER_RANGES order
    for (double* f : {&p.alpha, &p.beta_int, &p.beta_ext, &p.k, &p.sigma_1, &p.delta, &p.gamma_1, &p.gamma_c, &p.lambda_0, &p.lambda_1, &p.lambda_2, &p.c,
                      &p.E_max, &p.omega_B, &p.Q_B, &p.alpha_s, &p.beta_s, &p.mu, &p.alpha_E, &p.alpha_U, &p.lambda_I, &p.lambda_U}) *f = num(in);
    runs.push_back(r); }
  return runs;
}

// omnicompass/core.py simulate(): the macro step's clock restarts at (m - 1) * MACRO_DT, the command is control_command() held
// across rk4_step's four stages, the predicates count macro steps in one basin
Way simulate_way(const State& x0, const Parameters& p, int target, bool controlled) {
  Way w; w.U.push_back(x0.U);
  const double h = MACRO_DT / MICRO_STEPS;
  const int b0 = basin_sign(x0.U);
  int streak = b0 ? 1 : 0, ssign = b0;
  State x = x0;
  for (int m = 1; m <= MACRO_STEPS; ++m) {
    double t = (m - 1) * MACRO_DT;
    for (int j = 0; j < MICRO_STEPS; ++j) {
      double u = 0.0;
      if (controlled) { const double drift = derivatives(x, p, t, 0.0).U; const double raw = -drift + KP * (static_cast<double>(target) - x.U); u = std::max(-U_AUTHORITY, std::min(U_AUTHORITY, raw)); }
      x = rk4_step(x, p, t, h, u); t += h; }
    w.U.push_back(x.U);
    const int b = basin_sign(x.U);
    if (b) { if (b == ssign) ++streak; else { ssign = b; streak = 1; } } else { ssign = 0; streak = 0; }
    if (!w.convey && streak >= CONVEY_WINDOW) w.convey = m;
    if (!w.cert && streak >= CERT_WINDOW) w.cert = m; }
  return w;
}

std::string f6(double v) { char b[64]; std::snprintf(b, sizeof b, "%.6f", v); std::string s(b); return s == "-0.000000" ? "0.000000" : s; }
}  // namespace

int main(int argc, char** argv) {
  if (argc < 3) { std::cerr << "usage: oc_core_runs INJECTION.txt CANON.txt [FULL.txt]\n"; return 2; }
  try {
    const auto runs = read_injection(argv[1]);
    std::vector<std::vector<Way>> out(4);
    for (const auto& r : runs) {
      const int near = nearest_basin_sign(r.x0.U);
      Parameters mu0 = r.p; mu0.mu = 0.0;
      out[0].push_back(simulate_way(r.x0, r.p, near, true));
      out[1].push_back(simulate_way(r.x0, r.p, near, false));
      out[2].push_back(simulate_way(r.x0, r.p, -near, true));
      out[3].push_back(simulate_way(r.x0, mu0, near, true)); }
    std::ofstream canon(argv[2]); std::ofstream full; if (argc > 3) full.open(argv[3]);
    bool first = true;
    for (int w = 0; w < 4; ++w)
      for (std::size_t i = 0; i < runs.size(); ++i) {
        const Way& x = out[w][i];
        if (!first) canon << "\n"; first = false;
        canon << WAYS[w] << ":" << runs[i].k << ":" << runs[i].seed << ":";
        for (std::size_t j = 0; j < x.U.size(); ++j) canon << (j ? "," : "") << f6(x.U[j]);
        canon << ":" << x.convey << ":" << x.cert;
        if (full) { char b[40]; full << WAYS[w] << " " << runs[i].k; for (double u : x.U) { std::snprintf(b, sizeof b, " %.17g", u); full << b; } full << "\n"; } }
  } catch (const std::exception& e) { std::cerr << e.what() << "\n"; return 1; }
  return 0;
}
