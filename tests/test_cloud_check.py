# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The clouds' $0 check (Google Cloud and Amazon, 18 October; Azure, 22 October). A Google key cut short when it was copied,
and an Amazon account on the Free plan, failed every set started there at the login, each using up its A or B; for a while on
21 October the stored Azure key held a text Azure's login refuses, and Azure's own login step quoted its first characters on
the run's page. Now the key's shape is read before Google's and every Azure login (never a character of it printed), each
cloud's pre-flight names every short quota or Amazon's plan in plain words, the check stops before anything is built, and
the conductor starts a cloud's sets only after that cloud's newest check passed."""
import json
import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

from scripts import dispatch_grid as grid
from tools import cloud_key_check

ROOT = Path(__file__).resolve().parents[1]
# the environment a test hands the program, without a runner's own GITHUB_ENV and GITHUB_OUTPUT: on GitHub's runners the
# program's masked hand-off line (and its write to the job's env file) would otherwise run inside the test, print the test
# block on the mask line and leave it in the job's environment (24 October: main's verify failed so, never on a laptop)
CLEAN = {k: v for k, v in os.environ.items() if k not in ("GITHUB_ENV", "GITHUB_OUTPUT")}
SECRET = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7" * 30


def key(**over):
    k = {"type": "service_account", "project_id": "omni-compass-123456", "private_key_id": "abc123",
         "private_key": f"-----BEGIN PRIVATE KEY-----\n{SECRET}\n-----END PRIVATE KEY-----\n",
         "client_email": "omni-compass-github@omni-compass-123456.iam.gserviceaccount.com", "client_id": "1",
         "token_uri": "https://oauth2.googleapis.com/token"}
    k.update(over)
    return json.dumps(k, indent=2)


class KeyShape(unittest.TestCase):
    def test_a_whole_key_passes(self):
        self.assertEqual(cloud_key_check.problems(key(), "omni-compass-123456"), [])

    def test_a_key_cut_short_is_named_without_a_character_of_it(self):
        whole = key()
        for cut in (whole[:900], whole[:-3], whole[: len(whole) // 2]):
            bad = cloud_key_check.problems(cut)
            self.assertTrue(bad, cut[-20:])
            self.assertIn("cut", " ".join(bad))
            self.assertFalse(any(SECRET[:12] in b or "omni-compass-123456" in b for b in bad))

    def test_broken_json_missing_fields_and_another_project(self):
        self.assertIn("not whole JSON", cloud_key_check.problems(key().replace('",', '"', 1))[0])
        self.assertIn("private_key", cloud_key_check.problems(key(private_key=""))[0])
        self.assertIn("not whole", cloud_key_check.problems(key(private_key="-----BEGIN PRIVATE KEY-----\nMIIE"))[0])
        self.assertIn("GCP_PROJECT", cloud_key_check.problems(key(), "another-project")[0])
        self.assertEqual(cloud_key_check.problems(""), ["the secret is empty"])

    def test_what_a_stored_text_holds_is_named_from_its_shape(self):
        whole = key()
        cases = {whole[whole.index('"private_key_id"'):]: "piece from inside the file",
                 json.loads(whole)["private_key"]: "private key alone",
                 SECRET[:600]: "encoded string",
                 "ya29." + "a0AfB_xyZ-9q." * 45: "token",
                 "omni-compass-github@omni-compass-123456.iam.gserviceaccount.com": "account's address",
                 "GCP_CREDENTIALS = " + whole: "18 characters stand before its first {",
                 'P=$(gcloud config get-value project)\ngcloud iam service-accounts keys create key.json --iam-account "x"':
                     "the setup lines that are run in Google's Cloud Shell",
                 "Created key of type json for\n" + SECRET[:300] + " (see https://console.cloud.google.com)":
                     "2 lines, with spaces, a web address in it"}
        for raw, words in cases.items():
            with self.subTest(words=words):
                bad = cloud_key_check.problems(raw)[0]
                self.assertIn(words, bad)
                self.assertNotIn(SECRET[:12], bad)

    def test_the_program_exits_two_and_prints_no_secret(self):
        env = dict(CLEAN, GCP_CREDENTIALS=key()[:1200], GCP_PROJECT="omni-compass-123456")
        out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py")], env=env, capture_output=True, text=True)
        self.assertEqual(out.returncode, 2)
        self.assertNotIn(SECRET[:12], out.stdout + out.stderr)
        self.assertIn("docs/GOOGLE_SETUP.md", out.stdout)


AZ_SECRET = "Xq8Q~kLm.0aB1cD2eF3gH4iJ5kL6mN7oP8qR9sT0"
AZ_STORAGE = "Ab" * 43 + "=="   # the shape of a storage account's access key (88 characters of base64), made up


def az_block(**over):
    b = {"clientId": "0b1c2d3e-1111-2222-3333-444455556666", "clientSecret": AZ_SECRET,
         "subscriptionId": "11111111-2222-3333-4444-555555555555", "tenantId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
         "activeDirectoryEndpointUrl": "https://login.microsoftonline.com", "resourceManagerEndpointUrl": "https://management.azure.com/"}
    b.update(over)
    return json.dumps(b, indent=2)


class AzureKeyShape(unittest.TestCase):
    def test_the_whole_block_passes(self):
        self.assertEqual(cloud_key_check.azure_problems(az_block()), [])

    def test_every_wrong_form_is_named_without_a_character_of_it(self):
        whole = az_block()
        cases = {AZ_SECRET: "client secret's value alone",
                 AZ_STORAGE: "a storage account's access key",
                 "0b1c2d3e-1111-2222-3333-444455556666": "one identifier alone",
                 whole[whole.index('"clientSecret"'):]: "piece from inside the block",
                 whole[:150]: "cut short",
                 "'" + whole + "'": "1 character stands before its first {",
                 "Ab9+" * 21 + "Xy==": "storage account's access key",
                 "see https://portal.azure.com for the key " + AZ_SECRET: "1 line, with spaces, a web address in it",
                 whole.replace('",', '"', 1): "not whole JSON",
                 json.dumps({"appId": "0b1c2d3e-1111-2222-3333-444455556666", "password": AZ_SECRET,
                             "tenant": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"}): "fields missing: clientId, clientSecret, subscriptionId, tenantId",
                 az_block(tenantId="contoso"): "not a 36-character GUID: tenantId",
                 "": "the secret is empty"}
        for raw, words in cases.items():
            with self.subTest(words=words):
                bad = " ".join(cloud_key_check.azure_problems(raw))
                self.assertIn(words, bad)
                for piece in (AZ_SECRET[:10], AZ_SECRET[-10:], AZ_STORAGE[:10], "0b1c2d3e", "aaaaaaaa", "11111111"):
                    self.assertNotIn(piece, bad)

    def test_the_program_exits_two_and_prints_no_secret(self):
        for raw in (AZ_SECRET, az_block()[:300]):
            env = dict(CLEAN, AZURE_CREDENTIALS=raw)
            out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env, capture_output=True, text=True)
            self.assertEqual(out.returncode, 2)
            self.assertNotIn(AZ_SECRET[:10], out.stdout + out.stderr)
            self.assertIn("docs/AZURE_SETUP.md", out.stdout)
        env = dict(CLEAN, AZURE_CREDENTIALS=az_block())
        out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env, capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout)
        self.assertNotIn(AZ_SECRET[:10], out.stdout + out.stderr)

    def test_every_azure_login_reads_the_key_shape_first(self):
        """A key in another form never reaches azure/login, whose refusal quotes the stored text's first characters."""
        seen = 0
        for f in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            w = yaml.safe_load(f.read_text())
            for name, job in (w.get("jobs") or {}).items():
                steps = job.get("steps") or []
                for k, s in enumerate(steps):
                    if str(s.get("uses", "")).startswith("azure/login@"):
                        given = s.get("with") or {}
                        if "creds" not in given:
                            # the sign-in without a password (OIDC, the inventory since 23 October): no stored key text
                            # reaches azure/login, only the three IDs, and the job asks GitHub for its token
                            with self.subTest(workflow=f.name, job=name, login="oidc"):
                                self.assertTrue({"client-id", "tenant-id", "subscription-id"} <= set(given))
                                self.assertEqual((w.get("permissions") or job.get("permissions") or {}).get("id-token"), "write")
                            continue
                        seen += 1
                        prev = steps[k - 1]
                        with self.subTest(workflow=f.name, job=name):
                            self.assertIn("cloud_key_check.py azure", str(prev.get("run", "")))
                            for box in ("AZURE_CREDENTIALS", "AZURE_CLIENT_ID", "AZURE_TENANT_ID", "AZURE_SUBSCRIPTION_ID",
                                        "AZURE_CLIENT_SECRET"):
                                self.assertEqual(prev.get("env", {}).get(box), "${{ secrets.%s }}" % box)
                            # the login reads the block the check wrote, from the one box or the four
                            self.assertEqual(given.get("creds"), "${{ env.AZ_CREDS }}")
                            self.assertEqual(prev.get("if"), s.get("if"))       # skipped exactly when the login is
        self.assertGreaterEqual(seen, 9)      # the nine logins with the key (the inventory signs in without one since 23 October)


AZ_IDS = {"AZURE_CLIENT_ID": "0b1c2d3e-1111-2222-3333-444455556666", "AZURE_TENANT_ID": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
          "AZURE_SUBSCRIPTION_ID": "11111111-2222-3333-4444-555555555555"}


class AzureFourBoxes(unittest.TestCase):
    """24 October: the login typed one value to a box, as the portal shows each value, so no block is assembled by hand."""

    def test_the_whole_block_still_wins(self):
        block, where, bad = cloud_key_check.azure_login({"AZURE_CREDENTIALS": az_block()})
        self.assertEqual(bad, [])
        self.assertEqual(json.loads(block)["clientSecret"], AZ_SECRET)
        self.assertIn("whole block", where)

    def test_four_boxes_make_the_block(self):
        block, where, bad = cloud_key_check.azure_login(dict(AZ_IDS, AZURE_CLIENT_SECRET=AZ_SECRET))
        self.assertEqual(bad, [])
        self.assertEqual(json.loads(block), {"clientId": AZ_IDS["AZURE_CLIENT_ID"], "clientSecret": AZ_SECRET,
                                             "subscriptionId": AZ_IDS["AZURE_SUBSCRIPTION_ID"],
                                             "tenantId": AZ_IDS["AZURE_TENANT_ID"]})
        self.assertIn("four boxes", where)

    def test_the_password_alone_in_the_one_box_with_the_three_ids(self):
        block, where, bad = cloud_key_check.azure_login(dict(AZ_IDS, AZURE_CREDENTIALS=AZ_SECRET))
        self.assertEqual(bad, [])
        self.assertIn("AZURE_CREDENTIALS", where)

    def test_each_wrong_box_is_named_without_a_character_of_it(self):
        cases = [(dict(AZ_IDS, AZURE_CREDENTIALS=AZ_IDS["AZURE_CLIENT_ID"]), "AZURE_CLIENT_SECRET is empty"),
                 (dict(AZ_IDS, AZURE_CLIENT_SECRET="99999999-8888-7777-6666-555555555555"), "never the Secret ID"),
                 ({"AZURE_CLIENT_SECRET": AZ_SECRET}, "AZURE_CLIENT_ID is empty"),
                 (dict(AZ_IDS, AZURE_TENANT_ID="contoso", AZURE_CLIENT_SECRET=AZ_SECRET), "AZURE_TENANT_ID is not a 36-character ID"),
                 (dict(AZ_IDS, AZURE_CREDENTIALS="Ab9+" * 21 + "Xy=="), "storage account's access key")]
        for env, words in cases:
            with self.subTest(words=words):
                block, _, bad = cloud_key_check.azure_login(env)
                self.assertIsNone(block)
                said = " ".join(bad)
                self.assertIn(words, said)
                for piece in (AZ_SECRET[:10], "0b1c2d3e", "aaaaaaaa", "11111111", "99999999"):
                    self.assertNotIn(piece, said)

    def test_the_program_writes_the_masked_block_for_the_login(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "env"
            env = dict(CLEAN, GITHUB_ENV=str(out), AZURE_CREDENTIALS="", AZURE_CLIENT_SECRET=AZ_SECRET, **AZ_IDS)
            run = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env,
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout)
            written = out.read_text()
            self.assertTrue(written.startswith("AZ_CREDS={"))
            self.assertEqual(json.loads(written.split("=", 1)[1])["clientSecret"], AZ_SECRET)
            # the only line that carries it is the mask command, which the runner swallows
            shown = [ln for ln in run.stdout.splitlines() if AZ_SECRET in ln]
            self.assertTrue(shown and all(ln.startswith("::add-mask::") for ln in shown))
            bad = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"],
                                 env=dict(CLEAN, AZURE_CREDENTIALS="0b1c2d3e-1111-2222-3333-444455556666"),
                                 capture_output=True, text=True)
            self.assertEqual(bad.returncode, 2)
            self.assertIn("AZURE_CLIENT_SECRET", bad.stdout)
            self.assertIn("docs/AZURE_SETUP.md", bad.stdout)


def standin_bin(d, name, body):
    p = Path(d) / name
    p.write_text("#!/usr/bin/env bash\n" + body)
    p.chmod(p.stat().st_mode | stat.S_IEXEC)


GCLOUD = r'''
case "$*" in
  *"services list"*) if [ -n "$OFF" ]; then echo compute.googleapis.com; else printf 'compute.googleapis.com\ncontainer.googleapis.com\n'; fi ;;
  *"services enable"*) echo "PERMISSION_DENIED: Permission denied to enable service [container.googleapis.com]" >&2; exit 1 ;;
  *"machine-types describe"*) echo 2 ;;
  *"regions describe"*) echo '{"quotas": [{"metric": "CPUS", "limit": 24, "usage": 0}, {"metric": "SSD_TOTAL_GB", "limit": '"${SSD:-500}"', "usage": 0}, {"metric": "IN_USE_ADDRESSES", "limit": 8, "usage": 0}]}' ;;
  *"project-info describe"*) echo '{"quotas": [{"metric": "CPUS_ALL_REGIONS", "limit": '"${ALL:-32}"', "usage": 0}]}' ;;
  *) echo "unexpected gcloud $*" >&2; exit 9 ;;
esac
'''
AWS = r'''
case "$*" in
  *"sts get-caller-identity"*) echo arn:aws:iam::0:user/x ;;
  *"describe-instance-types"*)
    if [ -n "$DENY" ]; then echo "An error occurred (UnauthorizedOperation) when calling the DescribeInstanceTypes operation: You are not authorized to perform this operation. User: arn:aws:iam::0:user/x is not authorized to perform: ec2:DescribeInstanceTypes with an explicit deny in a service control policy" >&2; exit 254; fi
    echo 2 ;;
  *"get-service-quota"*) echo "${QUOTA:-32}.0" ;;
  *"list-requested-service-quota-change-history-by-quota"*) echo 0 ;;
  *"request-service-quota-increase"*) echo "$*" > "$ASKED"; echo '{}' ;;
  *) echo "unexpected aws $*" >&2; exit 9 ;;
esac
'''


class PreFlight(unittest.TestCase):
    def run_script(self, script, env):
        with tempfile.TemporaryDirectory() as d:
            standin_bin(d, "gcloud", GCLOUD)
            standin_bin(d, "aws", AWS)
            for tool in ("eksctl", "kubectl", "helm"):          # the pre-flight stops before any of them is reached
                standin_bin(d, tool, f'echo "{tool} reached" >&2; exit 9\n')
            e = dict(CLEAN, PATH=f"{d}:{os.environ['PATH']}", REP="1", PREFLIGHT_ONLY="1", GCP_PROJECT="p",
                     ASKED=str(Path(d) / "asked"), **env)
            out = subprocess.run(["bash", str(ROOT / "scripts" / script)], env=e, capture_output=True, text=True, cwd=d)
            asked = (Path(d) / "asked").read_text() if (Path(d) / "asked").exists() else ""
            return out.returncode, out.stdout + out.stderr, asked

    def test_google_ready_stops_after_the_preflight(self):
        code, out, _ = self.run_script("gke_paired.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("pre-flight only: nothing built, nothing billed", out)
        self.assertNotIn("creating", out)

    def test_google_free_trial_and_short_disk_are_named(self):
        code, out, _ = self.run_script("gke_paired.sh", {"ALL": "8", "SSD": "250"})
        self.assertEqual(code, 2, out)
        self.assertIn("CPUS_ALL_REGIONS needs 10, 8 free", out)
        self.assertIn("SSD_TOTAL_GB needs 500, 250 free", out)
        self.assertIn("activate the full account", out)

    def test_google_services_already_on_are_never_asked_for(self):
        code, out, _ = self.run_script("gcp_services.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("services are on", out)
        code, out, _ = self.run_script("gcp_services.sh", {"OFF": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("container.googleapis.com is off", out)
        self.assertIn("section 4", out)

    def test_amazon_free_plan_is_named(self):
        code, out, _ = self.run_script("eks_paired.sh", {"DENY": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("Free plan", out)
        self.assertIn("Paid plan", out)

    def test_amazon_short_quota_is_asked_of_amazon(self):
        code, out, asked = self.run_script("eks_paired.sh", {"QUOTA": "5", "QUOTA_REQUEST": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("an increase to 10 was asked of Amazon", out)
        self.assertIn("--desired-value 10", asked)

    def test_amazon_ready_stops_after_the_preflight(self):
        code, out, asked = self.run_script("eks_paired.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("pre-flight only: nothing built, nothing billed", out)
        self.assertNotIn("reached", out)
        self.assertEqual(asked, "")


class ConductorGate(unittest.TestCase):
    NOW = "2026-10-18T20:00:00Z"

    def run_(self, cloud, status, conclusion, created):
        return {"display_title": f"cloud-check {grid.CHECKS[cloud]}", "status": status, "conclusion": conclusion,
                "created_at": created, "id": 1}

    def test_the_states(self):
        g = "Google Cloud"
        cases = [([], "check"),
                 ([self.run_(g, "in_progress", None, "2026-10-18T19:58:00Z")], "wait"),
                 ([self.run_(g, "completed", "success", "2026-10-18T19:00:00Z")], "go"),
                 ([self.run_(g, "completed", "success", "2026-10-17T19:00:00Z")], "check"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T18:30:00Z")], "check"),
                 ([self.run_(g, "completed", "success", "2026-10-18T17:00:00Z"),
                   self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),     # the newest decides
                 ([self.run_("Amazon", "completed", "success", "2026-10-18T19:00:00Z")], "check")]  # another cloud's
        for runs, want in cases:
            with self.subTest(runs=runs):
                self.assertEqual(grid.check_state(runs, g, self.NOW)[0], want)

    def test_the_workflow_titles_match_the_conductor(self):
        w = yaml.safe_load((ROOT / ".github" / "workflows" / "cloud-check.yml").read_text())
        self.assertEqual(w["run-name"], "cloud-check ${{ github.event.inputs.cloud || 'azure' }}")
        byoc = {"oracle", "digitalocean", "alibaba", "linode", "ibm"}
        self.assertEqual(set(grid.CHECKS.values()), {"google", "amazon", "azure"} | byoc)
        # one job a cloud, its title the conductor's; the clusters built in a provider's console share one job, by its input
        self.assertEqual(set(w["jobs"]), {"google", "amazon", "azure", "byoc"})
        self.assertTrue(byoc <= set(json.loads(w["jobs"]["byoc"]["if"].split("fromJSON('")[1].split("')")[0])))
        self.assertNotIn('"all"', w["jobs"]["byoc"]["if"])                # no such secret stands until a tester stores one
        text = (ROOT / ".github" / "workflows" / "cloud-check.yml").read_text()
        self.assertEqual(text.count('PREFLIGHT_ONLY: "1"'), 2)          # it never builds a cluster
        self.assertEqual(text.count("azure_capacity.py preflight"), 1)    # Azure's pre-flight waits for nothing and builds nothing
        self.assertNotIn("az aks create", text)
        self.assertNotIn("az group create", text)
        for cloud, runs in (("google", ("google", "both", "all")), ("amazon", ("amazon", "both", "all")), ("azure", ("azure", "all"))):
            # a push of this file to main runs the two free checks as "both" (23 October); a hand or conductor start names its cloud
            self.assertEqual(w["jobs"][cloud]["if"], "contains(fromJSON('" + json.dumps(list(runs)) + "'), (github.event.inputs.cloud || 'azure'))")
        self.assertNotIn("eksctl create", text)
        self.assertNotIn("clusters create", text)

    def test_a_set_waits_for_its_check_and_the_conductor_starts_one(self):
        calls = []

        def api(path, method="GET", data=None, tries=4):
            calls.append((method, path, data))
            if "cloud-check.yml/runs" in path:
                return {"workflow_runs": []}
            if "/runs" in path:
                return {"workflow_runs": []}
            return {}
        with mock.patch.object(grid, "api", side_effect=api), \
             mock.patch.object(grid, "engine", return_value=grid.ENGINE), \
             mock.patch.object(grid, "campaign_open", return_value=True), \
             mock.patch.object(grid, "grid_runs", return_value=[]), \
             mock.patch.object(grid, "next_dispatches", return_value=[]), \
             mock.patch.object(grid, "rerun_queue", return_value=[]), \
             mock.patch.object(grid, "yield_repair_coordinator", return_value=False), \
             mock.patch.object(grid, "jobs_in_flight", return_value=(0, 0, [])), \
             mock.patch.object(grid, "cloud_switch", side_effect=lambda p: "azure" not in str(p)), \
             mock.patch.object(grid.time, "sleep"), \
             mock.patch.dict(CLEAN, {"GITHUB_STEP_SUMMARY": os.devnull}):
            self.assertEqual(grid.main(["tick", "--ref", "main"]), 0)
        posts = [(p, d) for m, p, d in calls if m == "POST"]
        self.assertTrue(posts)
        self.assertTrue(all("cloud-check.yml/dispatches" in p for p, _ in posts), posts)   # no set started
        # every queue switched on but Azure's: a check for each, the five console-built clusters' too
        self.assertEqual(sorted(d["inputs"]["cloud"] for _, d in posts), ["alibaba", "amazon", "digitalocean", "google", "ibm", "linode", "oracle"])

    def test_an_azure_set_waits_for_azures_check(self):
        """22 October: an Azure set that failed at the login counted as started; Azure's sets now wait for its own check."""
        calls = []

        def api(path, method="GET", data=None, tries=4):
            calls.append((method, path, data))
            return {"workflow_runs": []} if "/runs" in path else {}
        with mock.patch.object(grid, "api", side_effect=api), \
             mock.patch.object(grid, "engine", return_value=grid.ENGINE), \
             mock.patch.object(grid, "campaign_open", return_value=True), \
             mock.patch.object(grid, "grid_runs", return_value=[]), \
             mock.patch.object(grid, "next_dispatches", return_value=[]), \
             mock.patch.object(grid, "rerun_queue", return_value=[]), \
             mock.patch.object(grid, "yield_repair_coordinator", return_value=False), \
             mock.patch.object(grid, "jobs_in_flight", return_value=(0, 0, [])), \
             mock.patch.object(grid, "cloud_switch", side_effect=lambda p: "azure" in str(p)), \
             mock.patch.object(grid.time, "sleep"), \
             mock.patch.dict(CLEAN, {"GITHUB_STEP_SUMMARY": os.devnull}):
            self.assertEqual(grid.main(["tick", "--ref", "main"]), 0)
        posts = [(p, d) for m, p, d in calls if m == "POST"]
        self.assertEqual([(p.split("/")[-2], d["inputs"]) for p, d in posts], [("cloud-check.yml", {"cloud": "azure"})])
        self.assertEqual(grid.check_state([], "Azure")[0], "check")


KUBE = """apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t
    server: https://203.0.113.10:6443
  name: work
contexts:
- context: {cluster: work, user: omni}
  name: work
current-context: work
users:
- name: omni
  user:
%s
"""


class Kubeconfig(unittest.TestCase):
    """A cluster built in a provider's own console (docs/BYOC_SETUP.md): its kubeconfig's shape is read before anything is
    measured, never a character of it printed, and a kubeconfig that logs in only through a provider's command line (which
    GitHub's runner does not carry) is refused there."""

    def run_check(self, raw):
        env = dict(CLEAN, KUBECONFIG_RAW=raw)
        return subprocess.run(["python3", "tools/cloud_key_check.py", "kubeconfig"], cwd=ROOT, env=env, capture_output=True, text=True)

    def test_a_token_kubeconfig_is_whole_and_never_printed(self):
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Ik9tbmkifQ.secret-part-never-printed"
        r = self.run_check(KUBE % f"    token: {token}")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("logging in by a token", r.stdout)
        self.assertNotIn("secret-part", r.stdout + r.stderr)
        self.assertNotIn("203.0.113.10", r.stdout + r.stderr)

    def test_base64_of_it_is_read_too(self):
        import base64
        r = self.run_check(base64.b64encode((KUBE % "    token: abc").encode()).decode())
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_a_provider_plugin_is_refused_by_name(self):
        r = self.run_check(KUBE % "    exec:\n      apiVersion: client.authentication.k8s.io/v1beta1\n      command: oci")
        self.assertEqual(r.returncode, 2)
        self.assertIn("oci", r.stdout)
        self.assertIn("service-account token", r.stdout)

    def test_not_a_kubeconfig_says_what_was_stored(self):
        r = self.run_check("hello there")
        self.assertEqual(r.returncode, 2)
        self.assertIn("11 characters stored", r.stdout)
        self.assertNotIn("hello", r.stdout)
        self.assertEqual(self.run_check("").returncode, 2)

    def test_the_workflow_reads_it_before_the_run(self):
        body = (ROOT / ".github/workflows/byoc-metered.yml").read_text()
        self.assertLess(body.index("cloud_key_check.py kubeconfig"), body.index("bash scripts/byoc_paired.sh"))
        self.assertNotIn("setup-kubectl", body)


class ConsoleClouds(unittest.TestCase):
    """Oracle, DigitalOcean, Alibaba Cloud, Linode and IBM Cloud: wired as Azure's sets run, switched off, never run."""

    def test_each_queue_is_off_and_carries_the_four_sets(self):
        for name, key in grid.BYOC.items():
            with self.subTest(cloud=name):
                q = ROOT / "scripts" / f"{key}_queue.txt"
                self.assertFalse(grid.cloud_switch(q))
                sets = [ln.split("|")[0] for ln in q.read_text().splitlines() if ln and not ln.startswith(("#", "switch="))]
                self.assertEqual(sets, ["steady", "burst 1 4 1 6 1 9", "burst 1 6 1 8 1 6", "the real day on 1 to 9"])
                self.assertTrue(all(f"cloud={key}" in ln for ln in q.read_text().splitlines() if "|" in ln and not ln.startswith("#")))

    def test_the_title_is_the_workflows_own(self):
        w = (ROOT / ".github/workflows/byoc-metered.yml").read_text()
        self.assertIn("format('byoc-metered {7} {0}{1}{2}{6} dial {3} {4} {5}'", w)
        kv = {"cloud": "oracle", "replica_ceiling": "0", "stop_looks": "10,20,40,70", "dial": "save"}
        self.assertEqual(grid.cloud_title("byoc-metered.yml", kv),
                         "byoc-metered oracle steady replica room 0 to the cap, stopping rule dial save oracle work0")


if __name__ == "__main__":
    unittest.main()
