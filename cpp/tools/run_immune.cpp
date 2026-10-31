// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_immune IN.csv OUT.csv: the immune self-knowledge's script (tests/test_cpp_immune_parity.py). I,streak,relief,margin,hold,
// hold_max starts a knob; T,p_omni,p_native,moved,at_limit is one decision. Each T writes its answer, fields split by |: the mode, the hold left,
// the next hold's length, the hand-backs, and the event (its words, p_omni, p_native, redline decisions, hold) or none.
#include "omnicompass/immune.hpp"
#include <cstdio>
#include <fstream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
using namespace omnicompass;

static std::vector<std::string> split(const std::string& s) {
  std::vector<std::string> out; std::string f; std::istringstream in(s);
  while (std::getline(in, f, ',')) out.push_back(f);
  return out;
}

static std::string g(double x) { char b[64]; std::snprintf(b, sizeof b, "%.17g", x); return b; }

int main(int argc, char** argv) {
  if (argc != 3) { std::fprintf(stderr, "usage: oc_immune IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]);
  std::unique_ptr<Immune> k; std::string line;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const auto f = split(line);
    if (f[0] == "I") {
      k = std::make_unique<Immune>(std::stol(f[1]), std::stod(f[2]), std::stod(f[3]), std::stol(f[4]), std::stol(f[5]));
      out << "I\n";
    } else if (f[0] == "T") {
      std::optional<ImmuneEvent> ev;
      const std::string m = k->tick(std::stod(f[1]), std::stod(f[2]), f[3] == "1", f[4] == "1", ev);
      out << "T|" << m << "|" << k->left << "|" << k->hold_len << "|" << k->handbacks;
      if (!ev) out << "|none";
      else out << "|" << ev->what << "|" << g(ev->p_omni) << "|" << g(ev->p_native) << "|" << ev->redline_decisions << "|" << ev->hold;
      out << "\n";
    }
  }
  return 0;
}
// © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
