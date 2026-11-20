// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The scale-up's look-ahead and the stand-ins (omni-v27; C++ twin of omni_controller/controller.py's lookahead_slope,
// lookahead_horizon, lookahead_delivered and standin_count; tests/test_cpp_lookahead_parity.py). The founder's words of 15
// November: "if it's scaling up, it should be looking forward 3 steps"; "we don't want to make pods scale up when we can't give
// it to them". Read the two side by side: every line here has its Python line.
#pragma once
#include <optional>
#include <utility>
#include <vector>
namespace omnicompass {

constexpr int kLookAheadBeats = 3;        // LOOK_AHEAD_BEATS
constexpr double kDeliveryS = 120.0;      // DELIVERY_S

// the least of the beat-to-beat rates of (decision, value) readings, the time the decisions' count times the beat: the rise held
// at every beat (a single jump or a flat series' wobble gives none); 0 with fewer than two
double lookahead_slope(const std::vector<std::pair<double, double>>& pts, double beat);
// `beats` beats ahead, never nearer than a machine's delivery
double lookahead_horizon(double beat, double delivery_s, int beats = kLookAheadBeats);
// half the last measure, half the new
double lookahead_delivered(double delivery_s, double took_s);

struct StandIns {
  long count{0};
  double free{0.0}, parked{0.0}, shortfall{0.0};
};
// the stand-ins a decision asks for: the room looked ahead beyond the free room and the parked machines, never past what the
// cloud may still add (`room` machines; nullopt for no top); they number the free room, the parked room and the shortfall
StandIns standin_count(double alloc_m, double req_m, long nodes, long pool, long open, double ahead_m, std::optional<long> room,
                       double unit_m, bool off);

}  // namespace omnicompass
// © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
