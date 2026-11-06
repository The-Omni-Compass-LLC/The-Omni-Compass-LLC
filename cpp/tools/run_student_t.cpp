// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_student_t IN.csv OUT.csv : Student's t of cpp/src/student_t.cpp driven by a script, one question a line (17 digits).
//   L,x          math.lgamma(x)                -> L,value
//   B,a,b,x      the regularized incomplete beta -> B,value
//   C,t,df       P(|T| <= t)                    -> C,value
//   T,df         the two-sided 95% point          -> T,value
// tests/test_cpp_student_t_parity.py asks omnicompass/student_t.py the same questions.
#include "omnicompass/student_t.hpp"
#include <cstdio>
#include <fstream>
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
  if (argc < 3) { std::fprintf(stderr, "usage: oc_student_t IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const std::vector<std::string> f = split(line, ',');
    if (f[0] == "L") out << "L," << g(py_lgamma(std::stod(f[1]))) << "\n";
    else if (f[0] == "B") out << "B," << g(ibeta(std::stod(f[1]), std::stod(f[2]), std::stod(f[3]))) << "\n";
    else if (f[0] == "C") out << "C," << g(t_coverage(std::stod(f[1]), std::stod(f[2]))) << "\n";
    else if (f[0] == "T") out << "T," << g(t95(std::stoi(f[1]))) << "\n";
  }
  return 0;
}
