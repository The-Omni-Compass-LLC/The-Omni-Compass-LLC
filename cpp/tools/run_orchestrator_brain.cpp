// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_orchestrator_brain IN.csv OUT.csv : Omni direct's brain and room rule (cpp/src/orchestrator_brain.cpp) driven by a script, one line
// a step (numbers to 17 digits, "-" for none).
//   B,line_ms,beat_s,mn,mx,max_step,hold          a new brain                -> B
//   D,now,units,busy,p95,waiting,depth,trial,twin,anchor   one beat          -> D,want,force,position,twin,floor,depth,
//                                                                               trial,p95,busy,waiting,calm
//   Y,mn,mx                                       a new yardstick            -> Y
//   R,now,units,busy                              the yardstick's count      -> R,rec
//   C,cpu_m,busy_m,others_m,others_room,id,req,...  the conveyed walls       -> C,- or C,id,wall,...
//   M,units,req_m,room_m,step_units,floor,extra_m the machines the units need -> M,n
//   P,req_m,service,how,rule,n,(name,cpu_m,busy_m,state)×n,(machine,req_m,service)…   where the unit goes  -> P,name or P,-
// tests/test_cpp_orchestrator_brain_parity.py drives omni_orchestrator/brain.py and scheduler.py with the same script.
#include "omnicompass/orchestrator_brain.hpp"
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
static std::optional<double> optd(const std::string& s) { return s == "-" ? std::nullopt : std::optional<double>(std::stod(s)); }
static std::optional<int> opti(const std::string& s) { return s == "-" ? std::nullopt : std::optional<int>(std::stoi(s)); }
int main(int argc, char** argv) {
  if (argc < 3) { std::fprintf(stderr, "usage: oc_orchestrator_brain IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  std::unique_ptr<OmniBrain> brain; std::unique_ptr<Yardstick> yard;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const std::vector<std::string> f = split(line, ',');
    if (f[0] == "B") {
      brain = std::make_unique<OmniBrain>(std::stod(f[1]), std::stod(f[2]), std::stoi(f[3]), std::stoi(f[4]), std::stoi(f[5]),
                                          std::stoi(f[6]));
      out << "B\n";
    } else if (f[0] == "D") {
      const auto [want, i] = brain->decide(std::stod(f[1]), std::stoi(f[2]), optd(f[3]), std::stod(f[4]), std::stoi(f[5]),
                                           std::stoi(f[6]), f[7] == "1", opti(f[8]), opti(f[9]));
      out << "D," << want << "," << g(i.force) << "," << g(i.position) << "," << i.twin << "," << i.floor << "," << i.depth << ","
          << (i.trial ? 1 : 0) << "," << g(i.p95_ms) << "," << (i.busy ? g(*i.busy) : "-") << "," << i.waiting << ","
          << brain->calm << "\n";
    } else if (f[0] == "Y") {
      yard = std::make_unique<Yardstick>(std::stoi(f[1]), std::stoi(f[2]));
      out << "Y\n";
    } else if (f[0] == "R") {
      out << "R," << yard->recommend(std::stod(f[1]), std::stoi(f[2]), optd(f[3])) << "\n";
    } else if (f[0] == "C") {
      std::vector<Unit> ours;
      for (size_t k = 5; k + 1 < f.size(); k += 2) ours.push_back({f[k], std::stod(f[k + 1])});
      const auto walls = conveyed_limits(std::stod(f[1]), optd(f[2]), ours, std::stod(f[3]), f[4] == "1");
      out << "C";
      if (!walls) out << ",-";
      else for (const auto& u : ours) out << "," << u.id << "," << g(walls->at(u.id));
      out << "\n";
    } else if (f[0] == "M") {
      out << "M," << machines_needed(std::stoi(f[1]), std::stod(f[2]), std::stod(f[3]), std::stoi(f[4]), std::stoi(f[5]),
                                     std::stod(f[6])) << "\n";
    } else if (f[0] == "P") {
      const int n = std::stoi(f[5]);
      std::vector<Machine> ms; std::vector<Placed> us;
      for (int k = 0; k < n; ++k) ms.push_back({f[6 + 4 * k], std::stod(f[7 + 4 * k]), optd(f[8 + 4 * k]), f[9 + 4 * k]});
      for (size_t k = 6 + 4 * n; k + 2 < f.size(); k += 3)
        us.push_back({f[k], std::stod(f[k + 1]), f[k + 2] == "-" ? std::nullopt : std::optional<std::string>(f[k + 2])});
      const auto where = place(std::stod(f[1]), f[2], ms, us, f[3], f[4]);
      out << "P," << (where ? *where : "-") << "\n";
    }
  }
  return 0;
}
