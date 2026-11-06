// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_compass_law IN.csv OUT.csv : the compass law and the plug of cpp/src/compass_law.cpp driven by a script, one
// command a line, each answered on one line of OUT (17 significant digits); "nan" leaves a value as it stands.
//   L,lo,hi,center,cushion,dt,tau,kp,kd,authority,smooth   a new law (kd nan: critical damping)   -> L,kd
//   F,reading,center,cushion,kd                             set what is not nan, then force          -> F,force,p,v
//   P,lo,hi,tol,lever,res                                   a new plug on a device that takes a value to its own
//                                                           resolution (res > 0: floor(v / res + 0.5) x res)  -> P
//   A                                                       attach                                   -> A,snapshot
//   W,value                                                 write -> W,written|none,owned,writes,clipped,lever
//                                                                    or X,owned,lever (a foreign writer found)
//   M,value                                                 another writer moves the lever           -> M
//   S                                                       restore                                  -> S,at,lever
// tests/test_cpp_compass_law_parity.py runs the same script through omnicompass/compass_law.py.
#include "omnicompass/compass_law.hpp"
#include <cmath>
#include <cstdio>
#include <fstream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
using namespace omnicompass;
static std::vector<std::string> fields(const std::string& line) {
  std::stringstream ss(line); std::string f; std::vector<std::string> v;
  while (std::getline(ss, f, ',')) { if (!f.empty() && f.back() == '\r') f.pop_back(); v.push_back(f); }
  return v;
}
static double num(const std::string& s) { return s == "nan" ? NAN : std::stod(s); }
static std::string g(double x) { char b[40]; std::snprintf(b, sizeof b, "%.17g", x); return b; }
int main(int argc, char** argv) {
  if (argc < 3) { std::fprintf(stderr, "usage: oc_compass_law IN.csv OUT.csv\n"); return 2; }
  std::ifstream in(argv[1]); std::ofstream out(argv[2]); std::string line;
  std::unique_ptr<CompassLaw> law;
  std::unique_ptr<Plug> plug;
  double lever = 0.0, res = 0.0;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    const std::vector<std::string> f = fields(line);
    const std::string& c = f[0];
    if (c == "L") {
      const double kd = num(f[8]);
      law = std::make_unique<CompassLaw>(Band{num(f[1]), num(f[2]), num(f[3]), num(f[4])}, num(f[5]), num(f[6]), num(f[7]),
                                         std::isnan(kd) ? std::nullopt : std::optional<double>(kd), num(f[9]), num(f[10]));
      out << "L," << g(law->kd) << "\n";
    } else if (c == "F") {
      const double center = num(f[2]), cushion = num(f[3]), kd = num(f[4]);
      if (!std::isnan(center)) law->band.center = center;
      if (!std::isnan(cushion)) law->band.cushion = cushion;
      if (!std::isnan(kd)) law->kd = kd;
      const double force = law->force(num(f[1]));
      out << "F," << g(force) << "," << g(*law->p) << "," << g(law->v) << "\n";
    } else if (c == "P") {
      lever = num(f[4]); res = num(f[5]);
      plug = std::make_unique<Plug>(num(f[1]), num(f[2]), num(f[3]), [] { return 0.0; }, [&lever] { return lever; },
                                    [&lever, &res](double v) { lever = res > 0 ? std::floor(v / res + 0.5) * res : v; });
      out << "P\n";
    } else if (c == "A") {
      out << "A," << g(plug->attach()) << "\n";
    } else if (c == "W") {
      try {
        const std::optional<double> w = plug->write(num(f[1]));
        out << "W," << (w ? g(*w) : std::string("none")) << "," << int(plug->owned) << "," << plug->writes << ","
            << plug->clipped << "," << g(lever) << "\n";
      } catch (const ForeignWriter&) {
        out << "X," << int(plug->owned) << "," << g(lever) << "\n";
      }
    } else if (c == "M") {
      lever = num(f[1]);
      out << "M\n";
    } else if (c == "S") {
      const bool at = plug->restore();
      out << "S," << int(at) << "," << g(lever) << "\n";
    }
  }
  return 0;
}
