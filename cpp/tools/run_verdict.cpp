// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_verdict IN.csv OUT.csv : the verdict of cpp/src/verdict.cpp driven by a script, one command a line, each answered on
// one line of OUT (17 significant digits; "none" where the Python has None).
//   V,tolerance,min_samples,probe_every,recheck,max_steps,max_trial,incremental,judge   a new verdict  -> V
//   O,c1;c2;...                                     costs measured since the last decision (empty: none)  -> O
//   T,calm                                          one decision -> T,step,is_trial,allowed,phase,refs,gots,verdict,
//                                                   event step,cost native,cost step,reading,intervals,lo,hi,...
// tests/test_cpp_verdict_parity.py runs the same script through omnicompass/verdict.py.
#include "omnicompass/verdict.hpp"
#include <cstdio>
#include <fstream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
using namespace omnicompass;
static std::vector<std::string> split(const std::string& line, char sep) {
  std::stringstream ss(line); std::string f; std::vector<std::string> v;
  while (std::getline(ss, f, sep)) { if (!f.empty() && f.back() == '\r') f.pop_back(); v.push_back(f); }
  return v;
}
static std::string g(double x) { char b[40]; std::snprintf(b, sizeof b, "%.17g", x); return b; }
static std::string g(const std::optional<double>& x) { return x ? g(*x) : "none"; }
int main(int argc, char** argv) {
  if (argc < 3) { std::fprintf(stderr, "usage: oc_verdict IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  std::unique_ptr<Verdict> v;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const std::vector<std::string> f = split(line, ',');
    const std::string& c = f[0];
    if (c == "V") {
      v = std::make_unique<Verdict>(std::stod(f[1]), std::stol(f[2]), std::stol(f[3]), std::stol(f[4]), std::stol(f[5]),
                                    std::stol(f[6]), f[7] == "1", f[8]);
      out << "V\n";
    } else if (c == "O") {
      std::vector<double> costs;
      if (f.size() > 1) for (const std::string& x : split(f[1], ';')) if (!x.empty()) costs.push_back(std::stod(x));
      v->observe(costs);
      out << "O\n";
    } else if (c == "T") {
      const Tick k = v->tick(f[1] == "1");
      out << "T," << k.step << "," << int(k.is_trial) << "," << v->allowed << "," << (v->phase.empty() ? "none" : v->phase) << ","
          << v->ref.size() << "," << v->got.size();
      if (!k.event) out << ",none";
      else {
        const VerdictEvent& e = *k.event;
        out << "," << e.verdict << "," << e.step << "," << g(e.cost_native) << "," << g(e.cost_step) << ","
            << (e.reading.empty() ? "none" : e.reading) << "," << e.intervals.size();
        for (const auto& [lo, hi] : e.intervals) out << "," << g(lo) << "," << g(hi);
      }
      out << "\n";
    }
  }
  return 0;
}
