// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_lookahead IN.csv OUT.csv: the look-ahead's script (tests/test_cpp_lookahead_parity.py). S,beat,d1,v1,d2,v2,... is a slope;
// H,beat,delivery_s,beats a horizon; D,delivery_s,took_s a delivery measured; C,alloc_m,req_m,nodes,pool,open,ahead_m,room,unit_m,off
// a stand-in count (room -1 for no top). Each line writes its answer, fields split by |, every number at 17 significant digits.
#include "omnicompass/lookahead.hpp"
#include <cstdio>
#include <fstream>
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
  if (argc != 3) { std::fprintf(stderr, "usage: oc_lookahead IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const auto f = split(line);
    if (f[0] == "S") {
      std::vector<std::pair<double, double>> pts;
      for (std::size_t i = 2; i + 1 < f.size(); i += 2) pts.emplace_back(std::stod(f[i]), std::stod(f[i + 1]));
      out << "S|" << g(lookahead_slope(pts, std::stod(f[1]))) << "\n";
    } else if (f[0] == "H") {
      out << "H|" << g(lookahead_horizon(std::stod(f[1]), std::stod(f[2]), std::stoi(f[3]))) << "\n";
    } else if (f[0] == "D") {
      out << "D|" << g(lookahead_delivered(std::stod(f[1]), std::stod(f[2]))) << "\n";
    } else if (f[0] == "C") {
      const long room = std::stol(f[7]);
      const StandIns r = standin_count(std::stod(f[1]), std::stod(f[2]), std::stol(f[3]), std::stol(f[4]), std::stol(f[5]),
                                       std::stod(f[6]), room < 0 ? std::nullopt : std::optional<long>(room), std::stod(f[8]), f[9] == "1");
      out << "C|" << r.count << "|" << g(r.free) << "|" << g(r.parked) << "|" << g(r.shortfall) << "\n";
    }
  }
  return 0;
}
// © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
