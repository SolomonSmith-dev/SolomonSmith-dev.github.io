"""Offline regression tests for local-calendar activity windows.

Run from the repository root: python3 -m unittest discover -s tests -v
"""

import unittest
from datetime import date, datetime, timedelta, timezone
from unittest.mock import patch
from zoneinfo import ZoneInfo

from scripts import activity


class WeekBoundaryTests(unittest.TestCase):
    def window(self, monday, timezone_name="America/Los_Angeles"):
        repo = {"name": "example", "private": False,
                "created_at": "2020-01-01T00:00:00Z"}
        empty = {"commits": 0, "prs": [], "releases": [], "new": False}
        with patch.object(activity, "list_repos", return_value=[repo]), \
                patch.object(activity, "repo_activity", return_value=empty) as collect:
            activity.build_week(date.fromisoformat(monday),
                                {"timezone": timezone_name, "user": "example"}, "")
        return collect.call_args.args[2:4]

    def test_dst_and_adjacent_weeks_have_local_monday_boundaries(self):
        cases = [
            ("2026-02-23", "2026-02-23T08:00:00+00:00", "2026-03-02T08:00:00+00:00", 168),
            ("2026-03-02", "2026-03-02T08:00:00+00:00", "2026-03-09T07:00:00+00:00", 167),
            ("2026-03-09", "2026-03-09T07:00:00+00:00", "2026-03-16T07:00:00+00:00", 168),
            ("2026-10-19", "2026-10-19T07:00:00+00:00", "2026-10-26T07:00:00+00:00", 168),
            ("2026-10-26", "2026-10-26T07:00:00+00:00", "2026-11-02T08:00:00+00:00", 169),
            ("2026-11-02", "2026-11-02T08:00:00+00:00", "2026-11-09T08:00:00+00:00", 168),
        ]
        for monday, expected_since, expected_until, hours in cases:
            with self.subTest(monday=monday):
                since, until = self.window(monday)
                self.assertEqual(since, datetime.fromisoformat(expected_since))
                self.assertEqual(until, datetime.fromisoformat(expected_until))
                self.assertEqual(until - since, timedelta(hours=hours))
                self.assertEqual(since.tzinfo, timezone.utc)
                self.assertEqual(until.tzinfo, timezone.utc)
                for boundary in (since, until):
                    local = boundary.astimezone(ZoneInfo("America/Los_Angeles"))
                    self.assertEqual((local.weekday(), local.hour, local.minute), (0, 0, 0))

    def test_adjacent_windows_have_no_gap_or_overlap(self):
        for monday in ("2026-02-23", "2026-03-02", "2026-10-19", "2026-10-26"):
            with self.subTest(monday=monday):
                next_monday = (date.fromisoformat(monday) + timedelta(days=7)).isoformat()
                since, until = self.window(monday)
                next_since, next_until = self.window(next_monday)
                self.assertEqual(until, next_since)
                for instant in (until - timedelta(seconds=1), until,
                                until + timedelta(seconds=1)):
                    memberships = [since <= instant < until,
                                   next_since <= instant < next_until]
                    self.assertEqual(sum(memberships), 1)

    def test_utc_weeks_remain_seven_days(self):
        for monday in ("2026-03-02", "2026-10-26"):
            with self.subTest(monday=monday):
                since, until = self.window(monday, "UTC")
                self.assertEqual(since.hour, 0)
                self.assertEqual(until - since, timedelta(days=7))


if __name__ == "__main__":
    unittest.main()
