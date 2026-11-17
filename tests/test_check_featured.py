"""Tests for scripts/check_featured.py.

Run from the repository root: python3 -m unittest discover -s tests -v

Every test builds throwaway git repos in a temp dir. None touch the real repos.
"""

import contextlib
import io
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts import check_featured

ROOT = Path(__file__).resolve().parent.parent


def git(repo, *args):
    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.com",
         "-c", "commit.gpgsign=false", *args],
        cwd=str(repo), check=True, capture_output=True)


def make_repo(root, name, files, branch="main"):
    repo = Path(root) / name
    repo.mkdir(parents=True)
    git(repo, "init", "-q", "-b", branch)
    for rel, text in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "init")
    return repo


def row(**over):
    base = {
        "id": "demo.count", "name": "Demo", "url": "", "value": "3",
        "label": "things", "kind": "derived", "repo": "demo", "ref": "main",
        "rederive": 'git show "$CLAIM_REF":data.txt | wc -l | tr -d " "',
        "public_source": "https://example.test/demo", "evidence": "",
    }
    base.update(over)
    return base


class CheckFeaturedBase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        make_repo(self.tmp / "repos", "demo", {"data.txt": "a\nb\nc\n"})

    def write_data(self, rows, raw=None):
        path = self.tmp / "featured.json"
        path.write_text(raw if raw is not None
                        else json.dumps({"version": 1, "projects": rows}))
        return path

    def run_check(self, rows, *extra, raw=None):
        data = self.write_data(rows, raw)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_featured.main(
                ["--data", str(data), "--repo-root", str(self.tmp / "repos"), *extra])
        return code, out.getvalue(), err.getvalue()


class StatusTests(CheckFeaturedBase):
    def test_verified_exit_0_and_prints_sha(self):
        code, out, _ = self.run_check([row()])
        self.assertEqual(code, 0)
        self.assertIn("verified", out)
        sha = subprocess.run(["git", "rev-parse", "--short", "main"],
                             cwd=str(self.tmp / "repos" / "demo"),
                             capture_output=True, text=True).stdout.strip()
        self.assertIn(sha, out)

    def test_drift_exit_1(self):
        code, out, _ = self.run_check([row(value="4")])
        self.assertEqual(code, 1)
        self.assertIn("drift", out)

    def test_missing_repo_is_error(self):
        code, out, _ = self.run_check([row(repo="nope")])
        self.assertEqual(code, 1)
        self.assertIn("error", out)

    def test_missing_ref_is_error(self):
        code, out, _ = self.run_check([row(ref="no-such-ref")])
        self.assertEqual(code, 1)
        self.assertIn("error", out)

    def test_nonzero_command_is_error(self):
        code, out, _ = self.run_check([row(rederive="echo 3; exit 7")])
        self.assertEqual(code, 1)
        self.assertIn("error", out)

    def test_empty_output_is_error(self):
        code, out, _ = self.run_check([row(rederive="true")])
        self.assertEqual(code, 1)
        self.assertIn("error", out)

    def test_timeout_is_error(self):
        code, out, _ = self.run_check([row(rederive="sleep 5; echo 3")],
                                      "--timeout", "1")
        self.assertEqual(code, 1)
        self.assertIn("timeout", out)

    def test_manual_does_not_fail(self):
        manual = row(id="demo.manual", kind="manual", rederive="", repo="",
                     ref="", value="1,653", evidence="Production coverage data.")
        code, out, _ = self.run_check([manual])
        self.assertEqual(code, 0)
        self.assertIn("manual", out)

    def test_last_nonempty_line_is_the_value(self):
        code, _, _ = self.run_check([row(rederive="echo noise; echo 3; echo")])
        self.assertEqual(code, 0)


class NormalizeTests(CheckFeaturedBase):
    def test_commas_and_whitespace_normalized(self):
        self.assertTrue(check_featured.same(" 1,653 ", "1653"))

    def test_numeric_compare(self):
        self.assertTrue(check_featured.same("0.9943", "0.99430"))
        self.assertFalse(check_featured.same("0.9943", "0.9942"))

    def test_non_numbers_compare_as_strings(self):
        self.assertTrue(check_featured.same("v1", " v1 "))
        self.assertFalse(check_featured.same("v1", "v2"))

    def test_end_to_end_comma_value(self):
        code, _, _ = self.run_check([row(value="3.0")])
        self.assertEqual(code, 0)


class MalformedTests(CheckFeaturedBase):
    def test_bad_json_exit_2(self):
        code, _, err = self.run_check([], raw="{not json")
        self.assertEqual(code, 2)
        self.assertTrue(err)

    def test_missing_file_exit_2(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_featured.main(["--data", str(self.tmp / "absent.json")])
        self.assertEqual(code, 2)

    def test_missing_field_exit_2(self):
        bad = row()
        del bad["label"]
        self.assertEqual(self.run_check([bad])[0], 2)

    def test_duplicate_id_exit_2(self):
        self.assertEqual(self.run_check([row(), row()])[0], 2)

    def test_unknown_kind_exit_2(self):
        self.assertEqual(self.run_check([row(kind="guess")])[0], 2)

    def test_manual_with_command_exit_2(self):
        bad = row(kind="manual", evidence="ok")
        self.assertEqual(self.run_check([bad])[0], 2)

    def test_manual_without_evidence_exit_2(self):
        bad = row(kind="manual", rederive="", evidence="")
        self.assertEqual(self.run_check([bad])[0], 2)

    def test_derived_without_command_exit_2(self):
        self.assertEqual(self.run_check([row(rederive="")])[0], 2)

    def test_private_derived_without_evidence_exit_2(self):
        # No public source means the page shows the evidence sentence, so it must exist.
        self.assertEqual(self.run_check([row(public_source="")])[0], 2)

    def test_private_derived_with_evidence_is_checked(self):
        ok = row(public_source="", evidence="Private repo, not yet published.")
        self.assertEqual(self.run_check([ok])[0], 0)

    def test_projects_not_a_list_exit_2(self):
        raw = json.dumps({"version": 1, "projects": {}})
        self.assertEqual(self.run_check([], raw=raw)[0], 2)


class JsonOutputTests(CheckFeaturedBase):
    def test_json_shape(self):
        manual = row(id="demo.manual", kind="manual", rederive="", repo="",
                     ref="", evidence="Private data.")
        code, out, _ = self.run_check([row(), row(id="demo.bad", value="9"), manual],
                                      "--json")
        self.assertEqual(code, 1)
        doc = json.loads(out)
        self.assertEqual(doc["ok"], False)
        self.assertEqual(doc["summary"],
                         {"verified": 1, "drift": 1, "error": 0, "manual": 1})
        by_id = {r["id"]: r for r in doc["results"]}
        self.assertEqual(by_id["demo.count"]["status"], "verified")
        self.assertEqual(by_id["demo.count"]["actual"], "3")
        self.assertTrue(by_id["demo.count"]["sha"])
        self.assertEqual(by_id["demo.bad"]["status"], "drift")
        self.assertEqual(by_id["demo.manual"]["status"], "manual")


class RealDataSchemaTests(unittest.TestCase):
    def test_real_data_file_is_valid(self):
        data = json.loads((ROOT / "_data" / "featured.json").read_text())
        rows = check_featured.validate(data)
        self.assertEqual([r["name"] for r in rows],
                         ["CourtRules", "ARDA", "PhishGuard", "Recursive harness"])
        for r in rows:
            if r["kind"] == "manual":
                self.assertEqual(r["rederive"], "")
                self.assertTrue(r["evidence"])
            else:
                self.assertTrue(r["rederive"])


if __name__ == "__main__":
    unittest.main()
