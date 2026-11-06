# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The raw receipts on their own branch (18 October). Main's tree carried 182,161 raw files (35.6 GB), and Dependabot's every
clone of main timed out after 15 minutes. scripts/raw_archive.sh moves every archived run to the branch `raw` from trees
alone, never drops a folder (a second copy under the same name is kept beside the first), saves a new run on the branch's
newest tip, and opens the branch at results/live/raw/ with only the folders a job reads. Exercised here on a scratch
repository with a bare remote, the same commands the workflows run."""
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "raw_archive.sh"


def git(cwd, *args, check=True):
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    return subprocess.run(["git", "-c", "commit.gpgsign=false", "-c", "protocol.file.allow=always", *args], cwd=cwd,
                          capture_output=True, text=True, check=check, env=env).stdout.strip()


class RawArchive(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.bare = t / "remote.git"
        git(t, "init", "-q", "--bare", "-b", "main", str(self.bare))
        git(self.bare, "config", "uploadpack.allowFilter", "true")
        seed = t / "seed"
        git(t, "init", "-q", "-b", "main", str(seed))
        for run, text in (("run-1", "one"), ("run-2", "two")):
            d = seed / "results" / "live" / "raw" / run
            d.mkdir(parents=True)
            (d / "SHA256SUMS_ALL.txt").write_text(text + "\n")
        (seed / "README.md").write_text("code\n")
        (seed / ".gitignore").write_text("/results/live/raw/\n")
        (seed / "scripts").mkdir()
        (seed / "scripts" / "raw_archive.sh").write_bytes(SCRIPT.read_bytes())
        git(seed, "add", "-f", ".")
        git(seed, "commit", "-q", "-m", "seed")
        git(seed, "remote", "add", "origin", str(self.bare))
        git(seed, "push", "-q", "origin", "main")
        self.repo = t / "work"
        git(t, "clone", "-q", str(self.bare), str(self.repo))

    def tearDown(self):
        self.tmp.cleanup()

    def run_(self, *args, cwd=None, **env):
        e = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t",
                 GIT_CONFIG_COUNT="2", GIT_CONFIG_KEY_0="commit.gpgsign", GIT_CONFIG_VALUE_0="false",
                 GIT_CONFIG_KEY_1="protocol.file.allow", GIT_CONFIG_VALUE_1="always", **env)
        return subprocess.run(["bash", "scripts/raw_archive.sh", *args], cwd=cwd or self.repo, capture_output=True, text=True, env=e)

    def test_sweep_moves_every_run_and_main_keeps_none(self):
        out = self.run_("sweep")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(git(self.bare, "ls-tree", "--name-only", "raw").split(), ["run-1", "run-2"])
        self.assertEqual(git(self.bare, "show", "raw:run-2/SHA256SUMS_ALL.txt"), "two")
        self.assertNotIn("results/live/raw", git(self.bare, "ls-tree", "-r", "--name-only", "main"))
        self.assertEqual(self.run_("sweep").returncode, 0)                 # once moved, a second sweep has nothing to do
        self.assertEqual(self.run_("has", "run-1").returncode, 0)
        self.assertNotEqual(self.run_("has", "run-9").returncode, 0)

    def test_open_checks_out_only_what_is_asked(self):
        self.run_("sweep")
        shutil.rmtree(self.repo / "results" / "live" / "raw")               # a fresh checkout of main holds none
        out = self.run_("open", "/run-2/")
        self.assertEqual(out.returncode, 0, out.stderr)
        raw = self.repo / "results" / "live" / "raw"
        self.assertEqual((raw / "run-2" / "SHA256SUMS_ALL.txt").read_text(), "two\n")
        self.assertFalse((raw / "run-1").exists())
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")       # main never sees the worktree

    def test_open_again_reaches_a_run_saved_since(self):
        self.run_("sweep")
        shutil.rmtree(self.repo / "results" / "live" / "raw")
        self.assertEqual(self.run_("open", "/run-1/").returncode, 0)        # opened once, at the branch as it was then
        other = Path(self.tmp.name) / "other"                               # another job saves a run afterwards
        git(Path(self.tmp.name), "clone", "-q", str(self.bare), str(other))
        o = other / "results" / "live" / "raw" / "run-5"
        o.mkdir(parents=True)
        (o / "SHA256SUMS_ALL.txt").write_text("five\n")
        self.assertEqual(self.run_("save", "run-5", "run 5", cwd=other).returncode, 0)
        out = self.run_("open", "/run-5/")
        self.assertEqual(out.returncode, 0, out.stderr)
        raw = self.repo / "results" / "live" / "raw"
        self.assertEqual((raw / "run-5" / "SHA256SUMS_ALL.txt").read_text(), "five\n")   # 18 October: it stayed absent
        self.assertEqual((raw / "run-1" / "SHA256SUMS_ALL.txt").read_text(), "one\n")

    def test_a_file_over_githubs_cap_goes_up_in_parts_and_comes_back_whole(self):
        """2 November: the eight-card runs' result tarballs (393 MB and 195 MB) were over GitHub's 100 MB a file, and every
        attempt of every pass was refused, so their runs never reached the branch."""
        self.run_("sweep")
        d = self.repo / "results" / "live" / "raw" / "run-8"
        d.mkdir(parents=True)
        body = bytes(range(256)) * 10 + b"end"                              # 2,563 bytes
        (d / "pack.tar.gz").write_bytes(body)
        (d / "small.txt").write_text("kept as it is\n")
        out = self.run_("save", "run-8", "run 8", RAW_FILE_BYTES="1000")
        self.assertEqual(out.returncode, 0, out.stderr)
        names = git(self.bare, "ls-tree", "--name-only", "raw:run-8").split()
        self.assertEqual(names, ["pack.tar.gz.part-000", "pack.tar.gz.part-001", "pack.tar.gz.part-002", "pack.tar.gz.parts", "small.txt"])
        self.assertNotIn("pack.tar.gz", names)                               # no file on the branch over the cap
        shutil.rmtree(self.repo / "results" / "live" / "raw")
        out = self.run_("open", "/run-8/")
        self.assertEqual(out.returncode, 0, out.stderr)
        raw = self.repo / "results" / "live" / "raw" / "run-8"
        self.assertEqual((raw / "pack.tar.gz").read_bytes(), body)          # put back whole, checked against its SHA-256
        self.assertEqual((raw / "small.txt").read_text(), "kept as it is\n")
        (raw / "pack.tar.gz").unlink()
        (raw / "pack.tar.gz.part-001").write_bytes(b"tampered")
        self.assertNotEqual(self.run_("join", "run-8").returncode, 0)       # parts that do not make the file are refused
        self.assertFalse((raw / "pack.tar.gz").exists())

    def test_a_run_over_one_push_goes_up_in_parts_and_is_named_only_whole(self):
        """1 November: run 40649651196 handed in 2.9 GB, over GitHub's 2 GB a push, and every pass was refused six times."""
        self.run_("sweep")
        d = self.repo / "results" / "live" / "raw" / "run-7"
        d.mkdir(parents=True)
        for name in ("a.csv", "b.csv", "c.csv"):
            (d / name).write_text("0123456789")                         # ten bytes each
        out = self.run_("save", "run-7", "run 7", RAW_SPLIT_BYTES="15")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("saved in 2 pushes", out.stdout)
        self.assertEqual(git(self.bare, "ls-tree", "--name-only", "raw:run-7").split(), ["a.csv", "b.csv", "c.csv"])
        self.assertNotIn("run-7.partial", git(self.bare, "ls-tree", "--name-only", "raw").split())   # the staging name is gone
        log = git(self.bare, "log", "--format=%s", "raw")
        self.assertIn("run 7 (part 1)", log)
        self.assertEqual(self.run_("save", "run-7", "run 7", RAW_SPLIT_BYTES="15").stdout.strip(),
                         "raw archive: run-7 is already on the branch, unchanged")

    def test_save_adds_a_run_on_the_newest_tip_and_never_twice(self):
        self.run_("sweep")
        d = self.repo / "results" / "live" / "raw" / "run-3"
        d.mkdir(parents=True)
        (d / "SHA256SUMS_ALL.txt").write_text("three\n")
        other = Path(self.tmp.name) / "other"                               # another job saves first: the branch moved
        git(Path(self.tmp.name), "clone", "-q", str(self.bare), str(other))
        o = other / "results" / "live" / "raw" / "run-4"
        o.mkdir(parents=True)
        (o / "SHA256SUMS_ALL.txt").write_text("four\n")
        self.assertEqual(self.run_("save", "run-4", "run 4", cwd=other).returncode, 0)
        out = self.run_("save", "run-3", "run 3")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(git(self.bare, "ls-tree", "--name-only", "raw").split(), ["run-1", "run-2", "run-3", "run-4"])
        self.assertIn("already on the branch", self.run_("save", "run-3", "again").stdout)

    def test_a_second_copy_under_one_name_is_kept_beside_the_first(self):
        self.run_("sweep")
        git(self.repo, "pull", "-q", "origin", "main")
        d = self.repo / "results" / "live" / "raw"                        # a bot of the old kind commits to main again
        for run, text in (("run-1", "one, again"), ("run-5", "five")):
            (d / run).mkdir(parents=True, exist_ok=True)
            (d / run / "SHA256SUMS_ALL.txt").write_text(text + "\n")
        git(self.repo, "add", "-f", "results/live/raw")
        git(self.repo, "commit", "-q", "-m", "old-style archive")
        out = self.run_("sweep")
        self.assertEqual(out.returncode, 0, out.stderr)
        names = git(self.bare, "ls-tree", "--name-only", "raw").split()
        self.assertIn("run-5", names)
        kept = [n for n in names if n.startswith("run-1.main-")]
        self.assertEqual(len(kept), 1)
        self.assertEqual(git(self.bare, "show", f"raw:{kept[0]}/SHA256SUMS_ALL.txt"), "one, again")
        self.assertEqual(git(self.bare, "show", "raw:run-1/SHA256SUMS_ALL.txt"), "one")
        self.assertNotIn("results/live/raw", git(self.bare, "ls-tree", "-r", "--name-only", "main"))


class Writers(unittest.TestCase):
    def test_no_workflow_commits_raw_receipts_to_its_own_branch(self):
        for wf in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            text = wf.read_text()
            with self.subTest(workflow=wf.name):
                self.assertNotRegex(text, r'git add --sparse "\$d"', "raw receipts go to the branch raw (scripts/raw_archive.sh save)")
                self.assertNotIn("git sparse-checkout add $(cat raw_dirs.txt)", text)

    def test_main_ignores_the_opened_branch(self):
        self.assertIn("/results/live/raw/", (ROOT / ".gitignore").read_text().split())


if __name__ == "__main__":
    unittest.main()
