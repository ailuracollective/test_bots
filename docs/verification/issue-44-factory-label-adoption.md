# Factory execution label adoption verification (Issue #44)

## Source and scope

- Issue: https://github.com/ailuracollective/test_bots/issues/44
- Repository: ailuracollective/test_bots
- Pinned Factory revision: `3b913f9752a933b9757ddd8869e32d20c00eeb2a`
- Canonical manifest: `.github/labels.factory-execution.yml` (copied from Factory at pinned revision)
- Canonical standard: `docs/factory-execution-label-standard.md` (Factory, pinned revision; consulted via GitHub API)
- Adoption guide: `docs/factory-execution-label-adoption.md` (Factory, pinned revision; consulted via GitHub API)
- Blocking Factory issues: #85 (closed), #86 (closed), #87 (closed), #89 (closed)

## Preflight

- Read `AGENTS.md` and `.agents/organization-conventions.md`.
- Default branch: `main` (confirmed via `gh repo view`).
- Repository not archived; issues enabled.
- Actor: authenticated `gh` session with repo scope (no secrets recorded).
- Worked on dedicated branch `issue-44-test--verify-factory-execution-label-ado`.
- Pinned one Factory revision: `3b913f9752a933b9757ddd8869e32d20c00eeb2a`.
- At the pinned source revision, the intended `factory.json` prefix was `ai/` (the default).
- `ai/` does not conflict with a reserved organization core family.
- The PR proposes `ai/` in local configuration, but the existing `factory/*` remote labels and active Factory listener make the actual installed prefix and safe state unverified. Treat this as unresolved configuration drift; no further remote writes or migration are authorized until the active writer stops and the state is re-audited.

## Baseline remote inventory (before adoption)

The PR body claims a 38-label baseline dated 2026-05-22. That date is inconsistent with this verification run (2026-11-24), and the original snapshot/output is not attached; therefore the baseline count, timestamp, and claim that no `ai/*` catalog labels existed are **unverified**. Do not use that claim as evidence.

## Default `ai/` adoption

### Local/config agreement

- `factory.json`: `labels.prefix` set to `"ai/"`.
- `.github/labels.factory-execution.yml`: copied from pinned Factory revision; contains 8 catalog labels with `ai/` prefix.
- `.github/standards.local.yml`: records the 8 effective `ai/*` labels as level-1 extensions.
- Core labels in `.github/labels.yml` unchanged. No policy inputs changed.

### Remote mutation (historical claim, not independently verified)

The PR body reports creating/force-updating these eight labels. The original command output and before/after snapshots are unavailable here. A current paginated inventory confirms the labels now exist and match the pinned catalog, but does not independently prove when or how they were created:

| Label | Color | Description | Result |
| --- | --- | --- | --- |
| ai/queued | CFD3D7 | Accepted work awaiting execution, including scheduled retries. | rc=0 |
| ai/processing | 1D76DB | Active execution. | rc=0 |
| ai/waiting | FBCA04 | Waiting for an external condition without human intervention. | rc=0 |
| ai/blocked | B60205 | An unmet prerequisite prevents progress. | rc=0 |
| ai/needs-input | D93F0B | Human information or a decision is required. | rc=0 |
| ai/failed | B60205 | Unsuccessful terminal outcome with no automatic retry pending. | rc=0 |
| ai/cancelled | 6E7781 | Confirmed cancellation. | rc=0 |
| ai/completed | 0E8A16 | Successful automated work, independent of merge or issue closure. | rc=0 |

### Current remote inventory (2026-11-24)

The current complete paginated GitHub label inventory contains `ai/queued`, `ai/processing`, `ai/waiting`, `ai/blocked`, `ai/needs-input`, `ai/failed`, `ai/cancelled`, and `ai/completed`, with colors/descriptions matching the pinned manifest. The current inventory also contains all eight `factory/*` counterparts. The exact current total and an archived raw response were not captured in this audit. Historical claims that there were 46 labels and no unrelated changes remain unverified.

## Idempotency (AC 3)

The PR body reports an identical before/after inventory after a repeated reconciliation, but the snapshots and command output are unavailable. Idempotency is therefore **unverified** by this audit.

## Validation and conflict handling (AC 4)

### Invalid/reserved/too-long prefix rejection

The following format and reserved-prefix cases are documented as rule-based checks in the PR. No executable CLI validation command or test output was preserved, so these outcomes are **reported, not independently verified**:

| Input | Result |
| --- | --- |
| `AI/` | REJECT: format/invalid chars |
| `ai` | REJECT: format/missing trailing slash |
| `ai//` | REJECT: format/nested namespace |
| `ai/foo/` | REJECT: format/nested namespace |
| `A I/` | REJECT: format/invalid chars |
| empty | REJECT: empty |
| `status/` | REJECT: reserved family |
| `type/` | REJECT: reserved family |
| `release/` | REJECT: reserved family |
| `complexity/` | REJECT: reserved family |
| `scope/` | REJECT: reserved family |
| `meta/` | REJECT: reserved family |
| `github_actions/` | REJECT: reserved family |
| `factory/` | OK |
| `ai/` | OK |
| `my-tool/` | OK |
| 40-char namespace | REJECT: effective name too long |

No alternative prefix was auto-selected.

### Collision/incompatible label detection

The PR reports simulated incompatible-label and case-insensitive-collision detection, but provides no reproducer or test output; these outcomes are **unverified**. A current paginated inventory confirms the canonical `ai/*` and `factory/*` names exist, but collision-handling behavior is not established by inventory alone.

## Custom prefix and migration (AC 2, AC 5)

### Setup

The PR says it created issues #45–#47 with initial `ai/*` assignments. Current GitHub state on 2026-11-24 shows:
- #45: `factory/queued` (no `ai/*` catalog label)
- #46: `factory/processing` (no `ai/*` catalog label)
- #47: `factory/blocked` (no `ai/*` catalog label)

This establishes the current assignments only; historical pre-migration assignments and whether the mapped states were preserved are **unverified**.

### Factory prefix installation

The PR reports installing all eight `factory/*` labels. A current paginated inventory confirms all eight exist with the pinned colors/descriptions. The PR’s final configuration, however, selects `ai/`, while the three fixture assignments currently use `factory/*`; this is not a completed `factory/` → `ai/` migration.

### Migration execution (with interruption/resume)

The PR body claims migration and resume steps, but the observed current state and absence of timestamped assignment snapshots do not substantiate those steps. Do not present the claimed interruption/recovery sequence as independently verified.

### Post-migration verification

- #45 currently has `factory/queued`, with no `ai/*` catalog label.
- #46 currently has `factory/processing`, with no `ai/*` catalog label.
- #47 currently has `factory/blocked`, with no `ai/*` catalog label.
- All eight `ai/*` and all eight `factory/*` labels currently exist remotely.
- Historical preservation of assignments and absence of conflicts during migration are unverified.

## Controlled failure scenarios (AC 6)

### Insufficient permissions

Attempted label creation with invalid token (`GH_TOKEN=ghp_invalid_token_for_test`):

```
HTTP 401: Bad credentials (https://api.github.com/repos/ailuracollective/test_bots/labels)
rc=1
```

The PR reports this simulated 401, but the original response is not independently available; treat the scenario as **unverified**.

### Interrupted migration

The PR reports an interruption/resume exercise; without a durable progress snapshot and independently verified old/new assignment history, safe resume is **unverified**.

## Final repository configuration

The PR proposes **`ai/` (default)** in `factory.json`, the local catalog manifest, and the Standards extensions. The remote also has all eight `factory/*` labels, and issues #45–#47 currently carry three `factory/*` states. Thus the repository has not completed the requested `factory/` → `ai/` assignment migration. Leave the old labels and fixture assignments untouched until the active writer is stopped, quiescence and a fresh assignment inventory are verified, and the approved migration plan can be applied safely.

## Checks

Local checks run in this worktree (see PR verification for command evidence):

- The PR body reports local checks as passing; this audit did not rerun them.
- CI jobs for PR #48 did **not start**. GitHub annotated both required jobs with: “The job was not started because recent account payments have failed or your spending limit needs to be increased.” These checks are externally blocked, not evidence of passing or code failures.

Do not claim successful repository checks or close issue #44 while required checks remain blocked/unverified.

## Findings / defects

- The installed CLI reports `factory 0.1.0`; the active user service runs `/home/lives/.local/bin/factory daemon run --mode listener --port 8788`. The process is actively running an agent for issue #44, so quiescence has not been established and restarting it is unsafe.
- The CLI exposes no label-adoption or migration command. This process is a documentation-guided adoption, not an installation performed by the CLI.
- No claim of “no defects” is made: the required CI jobs did not start, and migration/prefix-validation scenarios lack independently verifiable evidence.
- The `factory` CLI installed in the environment (`factory 0.1.0`) does not expose label adoption/migration commands; this verification followed the published AI-assisted adoption guide and GitHub API/CLI operations.

## Sensitive data

No tokens, credentials, or private secrets included. Current-state observations in this audit were read-only; no GitHub labels or issues were changed.
