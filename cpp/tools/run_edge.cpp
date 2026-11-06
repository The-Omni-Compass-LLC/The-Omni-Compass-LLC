// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_edge IN.csv OUT.csv : the edge of cpp/src/edge.cpp driven by a script, one command a line, each answered on one line of
// OUT (17 significant digits).
//   E,react,z,window,narrow,start,memory,fall_decay,est,pace   a new edge                    -> E
//   U,p                                                        one position read           -> U,balance,cushion,react_part,floor
//   F,step                                                     a fall learned              -> F,floor
// tests/test_cpp_edge_parity.py runs the same script through omnicompass/edge.py.
#include "omnicompass/edge.hpp"
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
int main(int argc, char** argv) {
  if (argc < 3) { std::fprintf(stderr, "usage: oc_edge IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  std::unique_ptr<Edge> e;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const std::vector<std::string> f = split(line, ',');
    if (f[0] == "E") {
      e = std::make_unique<Edge>(std::stod(f[1]), std::stod(f[2]), std::stoi(f[3]), std::stod(f[4]), std::stod(f[5]),
                                 std::stod(f[6]), std::stod(f[7]), std::stoi(f[8]), std::stod(f[9]));
      out << "E\n";
    } else if (f[0] == "U") {
      const double b = e->update(std::stod(f[1]));
      out << "U," << g(b) << "," << g(e->cushion()) << "," << g(e->react_part()) << "," << g(e->floor_()) << "\n";
    } else if (f[0] == "F") {
      e->learn_fall(std::stod(f[1]));
      out << "F," << g(e->floor_()) << "\n";
    }
  }
  return 0;
}
