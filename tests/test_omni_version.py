# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine fingerprints (tools/omni_version.py): a checkout reads as exactly one version, or as a version minus the
runners not yet written at that commit, or as no version at all. No result is ever read across versions."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import omni_version as ov  # noqa: E402


class Fingerprints(unittest.TestCase):
    def test_the_checkout_carries_a_declared_version(self):
        files = ov.engine_files()
        self.assertIsNotNone(ov.version_of(files), "the engine in this checkout matches no declared fingerprint")
        self.assertEqual(ov.version_before(files), (None, []))

    def test_every_declared_fingerprint_is_its_own_digest(self):
        for v, path in ov.VERSIONS.items():
            want = json.loads(path.read_text())
            self.assertEqual(want["version"], f"omni-{v}")
            self.assertEqual(ov.digest(want["files"]), want["digest"], v)

    def test_a_commit_before_a_runner_was_written_reads_as_that_version_minus_the_runner(self):
        want = json.loads(ov.VERSIONS["v1"].read_text())["files"]
        files = {n: h for n, h in want.items() if n != "tools/run_pandapower.py"}
        self.assertIsNone(ov.version_of(files))           # not the whole fingerprint
        self.assertEqual(ov.version_before(files), ("omni-v1", ["tools/run_pandapower.py"]))

    def test_one_changed_byte_is_no_version(self):
        want = json.loads(ov.VERSIONS["v1"].read_text())["files"]
        files = dict(want); files["omnicompass/compass_law.py"] = "0" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))
        files.pop("tools/run_pandapower.py")               # a subset with one wrong byte is no version either
        self.assertEqual(ov.version_before(files), (None, []))

    def test_an_extra_engine_file_is_no_version(self):
        want = json.loads(ov.VERSIONS["v3"].read_text())["files"]
        files = dict(want); files["realms/new_rule.py"] = "1" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))

    def test_the_late_wires_count_only_for_the_versions_that_list_them(self):
        """omni-v15 took eight wires into the fingerprint. A tree with omni-v14's 47 files byte for byte reads omni-v14
        whatever those eight hold (its fingerprint never covered them); any other file omni-v14 does not list still makes
        it no version; and on omni-v15, which lists them, one changed byte in a late wire is no version."""
        v14 = json.loads(ov.VERSIONS["v14"].read_text())["files"]
        self.assertFalse(set(v14) & set(ov.LATE_WIRES), "omni-v14 was declared before the late wires")
        files = dict(v14); files.update({n: "2" * 64 for n in ov.LATE_WIRES})
        self.assertEqual(ov.version_of(files), "omni-v14")
        files["omni_controller/new_rule.py"] = "3" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))
        v15 = json.loads(ov.VERSIONS["v15"].read_text())["files"]
        self.assertTrue(set(ov.LATE_WIRES) <= set(v15), "omni-v15 lists every late wire")
        files = dict(v15); files["tools/run_redis.py"] = "4" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))

    def test_a_partial_checkout_reads_the_files_it_left_out_from_git(self):
        """A workflow's sparse checkout that leaves an engine folder out (omni_orchestrator/ in the grid's lists on omni-v18,
        24 October) reads the same version, the left-out files from the index; a file deleted by hand from a full checkout
        still fails, never read from git in its place."""
        import os, shutil, subprocess, tempfile
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
            for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
                env.pop(k, None)
            git = lambda *a: subprocess.run(["git", *a], cwd=repo, env=env, capture_output=True, text=True, check=True)
            tool = lambda: subprocess.run([sys.executable, "tools/omni_version.py"], cwd=repo, env=env, capture_output=True, text=True)
            (repo / "tools").mkdir(); shutil.copy(ROOT / "tools" / "omni_version.py", repo / "tools")
            for n, body in (("omnicompass/law.py", "law"), ("omni_orchestrator/__init__.py", "init"), ("omni_orchestrator/brain.py", "brain")):
                (repo / n).parent.mkdir(exist_ok=True); (repo / n).write_text(body + "\n")
            git("init", "-q"); git("add", "-A")
            self.assertIn("written: 3 files", subprocess.run([sys.executable, "tools/omni_version.py", "--write", "v18"], cwd=repo,
                                                            env=env, capture_output=True, text=True, check=True).stdout)
            git("add", "-A"); git("commit", "-q", "-m", "engine")
            git("sparse-checkout", "set", "--no-cone", "/tools/", "/omnicompass/", "/OMNI_V18.json")
            self.assertFalse((repo / "omni_orchestrator").exists(), "the sparse checkout leaves the folder out")
            r = tool()
            self.assertEqual((r.returncode, r.stdout.split()[0] if r.stdout else r.stderr), (0, "omni-v18"))
            git("sparse-checkout", "disable"); (repo / "omni_orchestrator" / "brain.py").unlink()
            self.assertNotEqual(tool().returncode, 0, "a file deleted from a full checkout is not read from git")


def main():
    r = unittest.TextTestRunner(verbosity=0, stream=open("/dev/null", "w")).run(unittest.defaultTestLoader.loadTestsFromTestCase(Fingerprints))
    assert r.wasSuccessful(), f"{len(r.failures)} failures, {len(r.errors)} errors in tests/test_omni_version.py"
    print("PASS  engine fingerprints: this checkout is one declared version; a commit before a runner was written reads as that version "
          "minus the runner; a changed byte or an extra engine file is no version; the late wires count only for the versions that list them")


if __name__ == "__main__":
    main()
