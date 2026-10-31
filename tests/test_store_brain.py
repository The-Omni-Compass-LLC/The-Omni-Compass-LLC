# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v22, the max on the store wires' memory knobs (tools/store_brain.py; MySQL and MongoDB through it): the working set's floor,
the store's own account of what its misses cost, the gate that spends memory only where the misses cost the service, and the host's
room."""
import os
import tempfile
import unittest

from tools import store_brain as B
from tools import run_sysbench as S
from tools import run_ycsb as Y

HOST = {"host_avail_mb": 4096.0, "host_total_mb": 7168.0}


class Cost(unittest.TestCase):
    def test_the_worth_is_the_misses_share_of_the_services_own_time(self):
        c = B.MissCost()
        for t in range(10):                                   # Redis behind a 5 ms store trip: 37% missing, a miss 5.1 ms beyond a hit, the mean 2.2 ms
            c.observe(float(t), 1500 * 0.37 * 5.1e-3, 1500 * 2.2e-3)
        self.assertAlmostEqual(c.worth(), 0.37 * 5.1 / 2.2, places=6)
        self.assertGreater(c.worth(), B.MISS_WORTH)

    def test_a_miss_that_costs_nothing_reads_under_the_floor(self):
        c = B.MissCost()
        for t in range(10):                                   # a store whose "misses" are nothing: 3,000 statements of 138 µs, 1,000 file reads of 1 µs
            c.observe(float(t), 1000 * 1e-6, 3000 * 138e-6)
        self.assertAlmostEqual(c.worth(), 1.0 / 414.0, places=6)
        self.assertLess(c.worth(), B.MISS_WORTH)
        from tools.readings import SIZE_FLOOR
        self.assertEqual(B.MISS_WORTH, SIZE_FLOOR, "the gate's floor is the one key's floor, a change of 0.5%")
        d = B.MissCost()
        for t in range(10):                                   # MySQL on this machine (30 October): 3,000 statements of 137 µs, 17% of 3 page reads each missing, a file read 70 µs
            d.observe(float(t), 3000 * 3 * 0.173 * 70e-6, 3000 * 137e-6)
        self.assertGreater(d.worth(), B.MISS_WORTH, "the misses are a quarter of the statements' time: memory is spent")

    def test_nothing_known_until_a_second_with_service_is_read_and_the_window_slides(self):
        c = B.MissCost(window_s=10.0)
        self.assertIsNone(c.worth())
        self.assertFalse(c.observe(0.0, 0.001, 0.0), "a second with no service time tells nothing")
        self.assertFalse(c.observe(1.0, None, 0.4), "a second without the store's account tells nothing")
        self.assertIsNone(c.worth())
        c.observe(2.0, 0.3, 0.4)
        self.assertAlmostEqual(c.worth(), 0.75)
        for t in range(3, 20):
            c.observe(float(t), 0.0, 0.4)
        self.assertEqual(c.worth(), 0.0, "the dear second slid out of the window")
        c.observe(21.0, 9.0, 0.4)
        self.assertEqual(c.worth(), 1.0, "never over one")


class Host(unittest.TestCase):
    def test_the_hosts_room_keeps_the_cushion(self):
        self.assertTrue(B.host_room(1000.0, 7168.0, 128))
        self.assertFalse(B.host_room(0.05 * 7168.0 + 100.0, 7168.0, 128), "128 MB would eat into the 5% cushion")
        self.assertIsNone(B.host_room(None, 7168.0, 128), "unread: nothing known")
        self.assertIsNone(B.host_room(1000.0, 0.0, 128))

    def test_meminfo_is_read_from_the_hosts_own_account(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "meminfo")
            with open(p, "w") as fh:
                fh.write("MemTotal:        7340032 kB\nMemFree:          102400 kB\nMemAvailable:    4194304 kB\nBuffers:           1 kB\n")
            self.assertEqual(B.read_meminfo(p), (4096.0, 7168.0))
            self.assertEqual(B.read_meminfo(os.path.join(d, "none")), (None, None))


class Floor(unittest.TestCase):
    def test_the_floor_follows_the_working_set_inside_the_cover_and_never_under_native(self):
        f = B.WorkingSetFloor(512, 128, (128, 2048), full=0.9)
        for t in range(10):
            f.observe(float(t), 300.0)
        self.assertEqual(f.value(10.0), 512, "never under the operator's setting")
        for t in range(10, 20):
            f.observe(float(t), 1000.0)
        self.assertEqual(f.value(20.0), 1152, "1000 MB over the fullness margin, rounded up to a chunk")
        for t in range(20, 100):
            f.observe(float(t), 100.0)
        self.assertEqual(f.value(100.0), 512, "the window slid past the peak")
        g = B.WorkingSetFloor(64, 8, (16, 512), full=0.9)
        g.observe(0.0, 5000.0)
        self.assertEqual(g.value(0.0), 512, "never over the cover")


class Target(unittest.TestCase):
    def test_a_spend_goes_through_where_misses_cost_and_holds_where_they_do_not(self):
        self.assertEqual(B.max_target(640, 512, 512, 512, 0.6, True, "grow")[0], 640)
        self.assertEqual(B.max_target(640, 512, 512, 512, 0.6, True, "grow")[2], "spend")
        target, why, kind = B.max_target(640, 512, 512, 512, 0.002, True, "grow")
        self.assertEqual((target, kind), (512, "held_worth")); self.assertIn("buy nothing", why)
        self.assertEqual(B.max_target(640, 512, 512, 512, 0.02, True, "grow")[2], "spend", "2% of the service's time is a change the key reads")
        target, why, kind = B.max_target(640, 512, 512, 512, None, True, "grow")
        self.assertEqual((target, kind), (512, "held_unread")); self.assertIn("not read", why)
        target, why, kind = B.max_target(640, 512, 512, 512, 0.6, None, "grow")
        self.assertEqual((target, kind), (512, "held_host")); self.assertIn("unread", why)
        target, why, kind = B.max_target(640, 512, 512, 512, 0.6, False, "grow")
        self.assertEqual((target, kind), (512, "held_host")); self.assertIn("cushion", why)

    def test_a_give_back_never_goes_below_the_floor(self):
        self.assertEqual(B.max_target(384, 512, 512, 512, None, None, "calm")[:3:2], (512, "held_floor"))
        self.assertEqual(B.max_target(640, 768, 512, 704, None, None, "calm")[:3:2], (704, "handed_to_floor"))
        self.assertEqual(B.max_target(640, 768, 512, 640, None, None, "calm")[:3:2], (640, "handed_back"))
        self.assertEqual(B.max_target(512, 512, 512, 512, None, None, "hold")[2], "hold")


def sys_obs(reading_ms, share, pool, used, miss_time_s, full=True, statements=3000, host=HOST):
    o = {"reading_s": reading_ms / 1000.0, "statements": statements, "miss_share": share, "pool_mb": pool, "used_mb": used,
         "full": full, "reads": True, "resizing": False, "cpu_share": 0.15, "miss_time_s": miss_time_s,
         "service_time_s": statements * reading_ms / 1000.0}
    o.update(host)
    return o


def ycsb_obs(reading_ms, share, cache, used, miss_time_s, full=True, reads=3000, host=HOST):
    o = {"reading_s": reading_ms / 1000.0, "reads": reads, "miss_share": share, "cache_mb": cache, "used_mb": used, "full": full,
         "requested": True, "cpu_share": 0.15, "miss_time_s": miss_time_s, "service_time_s": reads * reading_ms / 1000.0}
    o.update(host)
    return o


class Wires(unittest.TestCase):
    def test_mysql_holds_its_pool_where_the_data_files_reads_are_nothing_of_the_statements_time(self):
        b = S.Brain(512)
        cur = 512
        for t in range(1, 90):                               # a store whose misses cost nothing the key could read: 11% of page reads missing, each 0.3 µs
            share = 0.09 + 0.03 * ((t % 4) / 3.0)
            target, why, info = b.step(float(t), sys_obs(0.5, share, cur, 0.95 * cur, miss_time_s=3000 * 3 * share * 0.3e-6))
            self.assertGreaterEqual(target, 512, why)
            cur = target
        self.assertEqual(cur, 512, why)
        self.assertLess(info["miss_worth"], B.MISS_WORTH)
        self.assertGreater(b.record()["counts"]["held_worth"], 0)
        self.assertEqual(b.record()["dial"], "max")

    def test_mysql_spends_where_the_data_files_reads_are_a_share_of_the_statements_time(self):
        for us_a_read in (70e-6, 2e-3):                      # this machine's page cache (70 µs a file read, 30 October) and a disk (2 ms)
            b = S.Brain(512)
            cur = 512
            for t in range(1, 90):
                share = 0.15 + 0.03 * ((t % 4) / 3.0)
                target, why, info = b.step(float(t), sys_obs(0.5, share, cur, 0.95 * cur, miss_time_s=3000 * 3 * share * us_a_read))
                cur = target
            self.assertGreater(cur, 512, why)
            self.assertLessEqual(cur, S.COVER_MB[1])
            self.assertGreater(b.record()["counts"]["spend"], 0)

    def test_mysql_holds_where_the_account_is_not_read(self):
        b = S.Brain(512)
        target, why, info = b.step(1.0, sys_obs(0.5, 0.11, 512, 490.0, miss_time_s=None))
        self.assertEqual(target, 512); self.assertIn("not read", why)
        self.assertEqual(b.record()["counts"]["held_unread"], 1)

    def test_mysql_never_gives_the_pool_back_below_the_operators(self):
        b = S.Brain(512)
        cur = 512
        for t in range(1, 120):
            target, why, info = b.step(float(t), sys_obs(0.05, 0.0, cur, 200.0, miss_time_s=0.0))
            self.assertGreaterEqual(target, 512, why)
            cur = target

    def test_mongodb_holds_its_cache_where_a_miss_costs_the_read_nothing_and_spends_where_it_does(self):
        b = Y.Brain(512)
        cur = 512
        for t in range(1, 90):                               # 14% of pages missing, each 0.3 µs (nothing the key could read), the read 0.6 ms
            share = 0.12 + 0.04 * ((t % 4) / 3.0)
            target, why, info = b.step(float(t), ycsb_obs(0.6, share, cur, 0.9 * cur, miss_time_s=3000 * 2 * share * 0.3e-6))
            cur = target
        self.assertEqual(cur, 512, why)
        b = Y.Brain(512)
        cur = 512
        for t in range(1, 90):                               # a store whose misses cost: each missing page a 2 ms read
            share = 0.10 + 0.06 * ((t % 4) / 3.0)
            target, why, info = b.step(float(t), ycsb_obs(0.3 + share * 5.0, share, cur, 0.9 * cur, miss_time_s=3000 * 2 * share * 2e-3))
            cur = target
        self.assertGreater(cur, 512, why)
        self.assertIn("application's threads", Y.METER)

    def test_the_wires_name_their_meters(self):
        self.assertIn("performance schema", S.METER)
        self.assertEqual(Y.MISS_TIME_KEY, "application threads page read from disk to cache time (usecs)")
        self.assertIn(Y.MISS_TIME_KEY, Y.REQUIRED_CACHE_KEYS)
        self.assertIn("innodb_data_file", S.FILE_READS_SQL)


if __name__ == "__main__":
    unittest.main()
