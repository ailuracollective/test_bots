# Factory ai label projection verification (Issue #53)

## Source and scope

- Issue: https://github.com/ailuracollective/test_bots/issues/53
- Repository: ailuracollective/test_bots
- Related: #51 (first flow test), #44 / PR #48 (execution label adoption)
- Factory config: `factory.json` declares `labels.prefix: "ai/"`

## Goal

Verify that Factory runtime projects `ai/*` execution labels after daemon
rebuild/restart by observing label transitions during issue processing.

## Evidence

### Issue 53 timeline (GitHub issue events API)

Queried via `gh api repos/ailuracollective/test_bots/issues/53/events` on
2026-11-24. Relevant label events, in order:

| Time (UTC) | Event | Label | Actor |
| --- | --- | --- | --- |
| 2026-11-24T05:18:52Z | labeled | `type/task` | SiddharthaGF |
| 2026-11-24T05:18:52Z | labeled | `status/needs-review` | SiddharthaGF |
| 2026-11-24T05:19:07Z | unlabeled | `status/needs-review` | SiddharthaGF |
| 2026-11-24T05:19:07Z | labeled | `status/ready` | SiddharthaGF |
| 2026-11-24T05:19:12Z | labeled | `ai/processing` | SiddharthaGF |

### Current issue state

- State: open
- Labels: `type/task`, `status/ready`, `ai/processing`
- Updated: 2026-11-24T05:19:12Z

### Observation

The `ai/processing` label was added at 2026-11-24T05:19:12Z, 5 seconds after
`status/ready` was applied. This is an observed `ai/*` execution label
transition during issue processing, consistent with Factory projecting
execution state after the issue became ready.

No additional `ai/*` transitions (for example `ai/completed`, `ai/failed`,
`ai/queued`, or removal of `ai/processing`) were present in the captured event
timeline at observation time. The issue remains open with `ai/processing`,
indicating processing was still active or not yet projected to a terminal
state when evidence was captured.

## Acceptance criteria

- [x] `ai/*` execution label transitions are observed and recorded. Evidence:
  `ai/processing` added at 2026-11-24T05:19:12Z (GitHub issue events API).

## Constraints / non-goals

- No Python package behavior, release, or deployment workflow changes.
- Dedicated verification fixture; close/cleanup after confirmation, per issue
  #53.
