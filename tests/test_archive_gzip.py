# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The archive stores gzipped only what nothing reads once a run has made its own tables.

archive-run.yml gzips a run's YCSB raw latencies, request logs and Kafka consumer logs. Every tool that reads an archived
run (the three-run tables, the recomputation, the own-cost and dossier pages) must read none of those names, or a table
built from the archive would find its file gone; only the runners that write them during the run may name them."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/archive-run.yml"
# the runners write these files and read them back inside the same run, before the archive exists
WRITERS = {"run_ycsb.py", "run_redis.py", "run_kafka.py", "run_cpu_power.py", "run_sysbench.py"}
# a reader that reads a gzipped file in its stored form too (it names the .gz form and opens it with gzip)
GZ_AWARE = {"store_gate.py", "store_causes.py"}
GZ_READS = ("gzip.decompress", "gzip.open")


def gzipped_names():
    line = next(ln for ln in WORKFLOW.read_text().splitlines() if "-size +1M" in ln and "gzip" in ln)
    return re.findall(r"-name '([^']+)'", line)


class ArchiveGzip(unittest.TestCase):
    def test_the_list_is_the_bulk(self):
        self.assertEqual(sorted(gzipped_names()), ["*.raw", "consumer-*.log", "requests.log"])

    def test_no_archive_reader_names_a_gzipped_file(self):
        pats = {"*.raw": r"\.raw\b|notch-(\d|\*|\{|%)", "requests.log": r"requests\.log", "consumer-*.log": r"consumer-"}   # notch-<n>.raw, never a flag like --notch-s
        readers = [p for p in sorted((ROOT / "tools").glob("*.py")) + sorted((ROOT / "scripts").glob("*.py"))
                   if p.name not in WRITERS and not (p.name in GZ_AWARE and any(g in p.read_text() for g in GZ_READS))]
        readers += [ROOT / ".github/workflows/reaggregate.yml"]
        for name in gzipped_names():
            for p in readers:
                with self.subTest(name=name, reader=p.name):
                    self.assertIsNone(re.search(pats[name], p.read_text(encoding="utf-8", errors="replace")))

    def test_the_hashes_cover_the_stored_files(self):
        lines = WORKFLOW.read_text().splitlines()
        gz = max(i for i, ln in enumerate(lines) if "gzip -n -9" in ln)
        sums = next(i for i, ln in enumerate(lines) if "SHA256SUMS_ALL.txt" in ln and "sha256sum" in ln)
        self.assertLess(gz, sums)                         # the manifest is written after every file is in its stored form


if __name__ == "__main__":
    unittest.main()
