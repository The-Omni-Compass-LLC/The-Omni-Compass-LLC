# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v22 on the Redis cache's ceiling (docs/REDIS_PREREGISTRATION.md, amendment 5): the max, with the working set's floor.
On omni-v21 the verdict's allowance clamped every spend and the wall abandoned every spend trial; the first candidate without the
floor handed memory back within seconds of each rise and evicted the keys it had just kept (a sawtooth, LOSS in the model)."""
import unittest

from tools import run_redis as R


def obs(reading_ms, used_mb, ceiling_mb, evicted=0, n=1500, split=True):
    """One second as the wire's Omni hands it to the Brain: with the application's split (a miss the 5 ms store trip beyond a
    hit, 37% of requests missing) and the host's memory, unless `split` is False (the wire's older records)."""
    inside = int(n * 0.6)
    o = {"reading_s": reading_ms / 1000.0, "n": n, "inside": inside, "evicted_last_s": evicted, "ceiling_mb": ceiling_mb,
         "used_mb": used_mb, "cpu_share": 0.3, "host_avail_mb": 4096.0, "host_total_mb": 7168.0}
    if split:
        o.update({"hit_ms": 0.12, "miss_ms": 5.2, "miss_share": 0.37})
    return o


class Max(unittest.TestCase):
    def grown(self):
        """A brain that has grown the cache under misses with the cache full, and the working set now occupying 180 MB."""
        b = R.Brain(64, "resource")
        cur = 64; spends = []
        for t in range(1, 40):                                 # misses, the cache full: the spend goes through, never clamped
            target, why, info = b.step(float(t), obs(3.0, 0.95 * cur, cur, evicted=50))
            self.assertGreaterEqual(target, cur, why)
            if target > cur:
                spends.append(why)
            cur = target
        self.assertGreater(cur, 64)
        self.assertLessEqual(cur, R.COVER_MB[1], "never past the cover's top")
        self.assertTrue(spends and all("power given" in w for w in spends), spends)
        for t in range(40, 110):                               # the working set settles at 180 MB; the growth's seconds leave the window
            target, why, info = b.step(float(t), obs(0.3, 180.0, cur))
            cur = target
        return b, cur

    def test_the_spend_is_never_clamped_by_an_allowance(self):
        b, cur = self.grown()
        self.assertGreater(b.max.counts["spend"], 0, "the max spends where the misses cost; no allowance is asked")
        self.assertIsNone(b.record()["allowed_high"], "the max keeps no allowance")
        self.assertIn("the max", b.record()["state"])

    def test_nothing_is_taken_where_the_split_or_the_host_is_unread(self):
        b = R.Brain(64, "resource")
        for t in range(1, 15):                                 # the wire's older records: no split, so no account of a miss's cost
            target, why, info = b.step(float(t), obs(3.0, 61.0, 64, evicted=50, split=False))
        self.assertEqual(target, 64, why); self.assertIn("not read", why)
        b = R.Brain(64, "resource")
        for t in range(1, 15):                                 # the host's memory unread
            o = obs(3.0, 61.0, 64, evicted=50); o["host_avail_mb"] = None
            target, why, info = b.step(float(t), o)
        self.assertEqual(target, 64, why); self.assertIn("host", why)
        b = R.Brain(64, "resource")
        for t in range(1, 15):                                 # the host has no notch over its cushion
            o = obs(3.0, 61.0, 64, evicted=50); o["host_avail_mb"] = 0.05 * 7168.0 + 4.0
            target, why, info = b.step(float(t), o)
        self.assertEqual(target, 64, why); self.assertIn("cushion", why)

    def test_calm_hands_back_only_to_the_working_sets_floor(self):
        b, cur = self.grown()
        floor = b.floor_mb(110.0)
        self.assertEqual(floor, 200, "180 MB occupied, the fullness margin, rounded up to a notch")
        for t in range(110, 240):
            target, why, info = b.step(float(t), obs(0.3, 180.0, cur))
            self.assertGreaterEqual(target, floor, why)
            cur = target
        self.assertEqual(cur, floor, "handed back one notch a second down to the floor, and held there")

    def test_the_floor_falls_with_the_working_set_and_never_under_native(self):
        b, cur = self.grown()
        for t in range(110, 400):                              # the working set shrinks to 20 MB: the floor follows it after the window
            target, why, info = b.step(float(t), obs(0.3, 20.0, cur))
            self.assertGreaterEqual(target, 64, why)
            cur = target
        self.assertEqual(cur, 64, "never below the operator's ceiling at the max")

    def test_the_wall_puts_a_quarter_of_the_cover_on_at_once(self):
        b = R.Brain(64, "resource")
        for t in range(1, 12):
            target, why, info = b.step(float(t), obs(1.95, 61.0, 64, evicted=80))
        self.assertGreaterEqual(target, 64 + R.FAILUP_MB, why)
        self.assertTrue(why.startswith("fail up"), why)



class MissPrice(unittest.TestCase):
    def test_memory_is_spent_only_where_misses_cost_the_service(self):
        # MySQL on a runner whose page cache holds the data files: a miss costs nothing, so memory would buy nothing
        cheap = dict(obs(1.5, 61.0, 64, evicted=80), hit_ms=0.12, miss_ms=0.125, miss_share=0.4)   # slow, the cache full: the compass asks; a miss 5 µs beyond a hit
        b = R.Brain(64, "resource")
        for t in range(1, 15):
            target, why, info = b.step(float(t), cheap)
        self.assertEqual(target, 64, why); self.assertIn("buy nothing", why)
        # Redis behind a 5 ms store trip: the misses are the latency, the spend goes through
        dear = dict(obs(2.2, 61.0, 64, evicted=80), hit_ms=0.12, miss_ms=5.5, miss_share=0.37)
        b = R.Brain(64, "resource")
        for t in range(1, 15):
            target, why, info = b.step(float(t), dear)
        self.assertGreater(target, 64, why)
        self.assertEqual(R.miss_time(obs(0.8, 61.0, 64, split=False)), (None, None), "a wire without the split gives no account")
        miss_s, service_s = R.miss_time(dear)
        self.assertAlmostEqual(service_s, 1500 * 2.2e-3)
        self.assertAlmostEqual(miss_s, 1500 * 0.37 * (5.5 - 0.12) / 1000.0)


if __name__ == "__main__":
    unittest.main()
