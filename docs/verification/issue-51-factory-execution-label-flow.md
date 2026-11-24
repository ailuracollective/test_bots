# Factory execution label flow verification (Issue #51)

## Source and scope

- Issue: https://github.com/ailuracollective/test_bots/issues/51
- Repository: ailuracollective/test_bots
- Related issue: https://github.com/ailuracollective/test_bots/issues/44
- Related PR: https://github.com/ailuracollective/test_bots/pull/48
- Factory configuration: `factory.json` declares `labels.prefix: "ai/"`

## Goal

Verify the Factory execution label flow in `test_bots` after adopting the `ai/*`
catalog (issue #44) by observing whether the Factory runtime updates execution
state labels (`ai/queued`, `ai/processing`, etc.) during processing.

## Constraints observed

- The `ai` trigger label was not added by this verification run.
- GitHub issue event history shows the `ai` label was added by
  `SiddharthaGF` at `2026-11-24T04:43:31Z` (event id `37090380200`), which is
  recorded as explicit human action in the issue timeline.
- No Python package behavior, release, or deployment workflows were changed.

## Observation window and evidence

Evidence was collected on 2026-11-24 from the GitHub API for issue #51.

### Current issue labels (at observation time)

- `type/task`
- `status/ready`
- `ai`

No `ai/*` execution state label (`ai/queued`, `ai/processing`, `ai/waiting`,
`ai/blocked`, `ai/needs-input`, `ai/failed`, `ai/cancelled`, `ai/completed`)
was present on the issue at observation time.

### Issue events (GitHub API `/issues/51/events`)

| id | event | label | actor | created_at |
| --- | --- | --- | --- | --- |
| 37090316569 | labeled | type/task | SiddharthaGF | 2026-11-24T04:42:25Z |
| 37090316849 | labeled | status/needs-review | SiddharthaGF | 2026-11-24T04:42:25Z |
| 37090343435 | assigned | - | SiddharthaGF | 2026-11-24T04:42:52Z |
| 37090380200 | labeled | ai | SiddharthaGF | 2026-11-24T04:43:31Z |
| 37090630856 | unlabeled | status/needs-review | SiddharthaGF | 2026-11-24T04:47:53Z |
| 37090630920 | labeled | status/ready | SiddharthaGF | 2026-11-24T04:47:53Z |

### Issue timeline (GitHub API `/issues/51/timeline`)

The timeline returned the same label/assignment events and no `ai/*` execution
state label transitions.

### Repository workflow runs observed (GitHub Actions)

Recent repository runs inspected via `gh run list --repo ailuracollective/test_bots --limit 10`:

| run | event | branch | status | conclusion | createdAt | url |
| --- | --- | --- | --- | --- | --- | --- |
| Contribution policy | issues | main | completed | success | 2026-11-24T04:42:26Z | https://github.com/ailuracollective/test_bots/actions/runs/45328230096 |
| Contribution policy | pull_request | issue-45-test--factory-label-adoption-verificatio | completed | success | 2026-11-24T04:41:57Z | https://github.com/ailuracollective/test_bots/actions/runs/45328175845 |
| CI | pull_request | issue-45-test--factory-label-adoption-verificatio | completed | success | 2026-11-24T04:41:57Z | https://github.com/ailuracollective/test_bots/actions/runs/45328175754 |
| Contribution policy | pull_request | issue-45-test--factory-label-adoption-verificatio | completed | skipped | 2026-11-24T04:41:50Z | https://github.com/ailuracollective/test_bots/actions/runs/45328163329 |
| Contribution policy | pull_request | issue-45-test--factory-label-adoption-verificatio | completed | skipped | 2026-11-24T04:41:50Z | https://github.com/ailuracollective/test_bots/actions/runs/45328163220 |
| CI | pull_request | issue-45-test--factory-label-adoption-verificatio | completed | skipped | 2026-11-24T04:41:50Z | https://github.com/ailuracollective/test_bots/actions/runs/45328163152 |
| Contribution policy | pull_request | release-please--branches--main | completed | action_required | 2026-11-24T04:35:09Z | https://github.com/ailuracollective/test_bots/actions/runs/45327409632 |
| CI | pull_request | release-please--branches--main | completed | action_required | 2026-11-24T04:35:09Z | https://github.com/ailuracollective/test_bots/actions/runs/45327409445 |
| Release Please | push | main | completed | success | 2026-11-24T04:34:47Z | https://github.com/ailuracollective/test_bots/actions/runs/45327368300 |
| Graph Update: uv in /. #1726538574 | dynamic | main | completed | success | 2026-11-24T04:33:22Z | https://github.com/ailuracollective/test_bots/actions/runs/45327203223 |

No GitHub Actions run in the inspected window showed Factory execution label
transition activity for issue #51. Factory runtime processing may occur outside
GitHub Actions in this repository; this verification reports only
GitHub-observable evidence.

## Acceptance criteria status

- [x] Trigger label is added only with explicit confirmation. — The `ai` label
  was added by `SiddharthaGF` at `2026-11-24T04:43:31Z` per issue events; this
  verification run did not add the `ai` label.
- [x] Observed execution label transitions are recorded, or absence of
  transitions is reported with runtime evidence. — No `ai/*` execution state
  label transitions (`ai/queued`, `ai/processing`, `ai/waiting`, `ai/blocked`,
  `ai/needs-input`, `ai/failed`, `ai/cancelled`, `ai/completed`) were observed
  in issue events/timeline or current labels during the observation window.
  Absence is reported with the GitHub-observable event, label, and workflow-run
  evidence above.

## Conclusion

At the time of observation, GitHub-observable evidence for issue #51 shows the
`ai` trigger label was applied by explicit human action and no Factory execution
state label transitions were recorded on the issue. This report does not claim
that no external Factory runtime processed the issue; it reports the absence of
observable `ai/*` execution label transitions in GitHub issue state/events during
the inspected window.
