// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// C++ twin of omni_controller/controller.py's look-ahead and stand-in arithmetic (omni-v27): every answer the Python's to the
// last bit (tests/test_cpp_lookahead_parity.py).
#include "omnicompass/lookahead.hpp"
#include <algorithm>
#include <cmath>
namespace omnicompass {

double lookahead_slope(const std::vector<std::pair<double, double>>& pts, double beat) {
  // rates = [(v1 - v0) / ((d1 - d0) * beat) for consecutive readings if (d1 - d0) * beat > 0]; min(rates) if rates else 0.0
  bool any = false; double least = 0.0;
  for (std::size_t i = 0; i + 1 < pts.size(); ++i) {
    const double dt = (pts[i + 1].first - pts[i].first) * beat;
    if (!(dt > 0)) continue;
    const double r = (pts[i + 1].second - pts[i].second) / dt;
    if (!any || r < least) { least = r; any = true; }
  }
  return any ? least : 0.0;
}

double lookahead_horizon(double beat, double delivery_s, int beats) {
  return std::max(static_cast<double>(beats) * beat, delivery_s);      // max(beats * beat, delivery_s)
}

double lookahead_delivered(double delivery_s, double took_s) { return 0.5 * delivery_s + 0.5 * took_s; }

StandIns standin_count(double alloc_m, double req_m, long nodes, long pool, long open, double ahead_m, std::optional<long> room,
                       double unit_m, bool off) {
  StandIns r;
  if (alloc_m <= 0 || unit_m <= 0) return r;                            // return 0, 0.0, 0.0, 0.0
  nodes = std::max(1L, nodes);
  const double per_node = alloc_m / static_cast<double>(nodes);
  r.free = std::max(0.0, alloc_m - req_m);
  r.parked = static_cast<double>(std::max(0L, pool - open)) * per_node;
  r.shortfall = std::max(0.0, ahead_m - r.free - r.parked);
  if (room) r.shortfall = std::min(r.shortfall, static_cast<double>(*room) * per_node);
  r.count = (off || r.shortfall <= 0) ? 0 : static_cast<long>(std::ceil((r.free + r.parked + r.shortfall) / unit_m - 1e-9));
  return r;
}

}  // namespace omnicompass
// © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
