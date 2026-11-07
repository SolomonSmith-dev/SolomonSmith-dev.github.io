# Weekly hire-ready maintenance

1. Confirm weekly activity workflow ran (or dispatch it)
2. Skim home metrics still match resume/README sources
3. Run `python3 docs/hire-ready/scripts/link_qa.py`
4. On a machine with MATERIALS: `scripts/sync-resume.sh` if resume changed
5. Check GitHub pins still match hire story
6. Re-run `bundle exec jekyll build` before large content PRs
7. Never hand-edit `_data/activity.json` / `activity_log.json`
