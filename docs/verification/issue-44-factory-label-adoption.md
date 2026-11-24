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
- `factory.json` resolved with default `labels.prefix: "ai/"`.
- No reserved-family conflict (`ai/` is not a reserved organization core family).
- No configuration drift detected before mutation.

## Baseline remote inventory (before adoption)

Complete paginated inventory captured via `gh label list --repo ailuracollective/test_bots --limit 200 --json name,color,description` on 2026-05-22. Total: 38 labels. Included 27 core labels plus legacy labels (`ai`, `autorelease: pending`, `autorelease: tagged`, `bug`, `documentation`, `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, `wontfix`). No `ai/*` execution catalog labels existed.

## Default `ai/` adoption

### Local/config agreement

- `factory.json`: `labels.prefix` set to `"ai/"`.
- `.github/labels.factory-execution.yml`: copied from pinned Factory revision; contains 8 catalog labels with `ai/` prefix.
- `.github/standards.local.yml`: records the 8 effective `ai/*` labels as level-1 extensions.
- Core labels in `.github/labels.yml` unchanged. No policy inputs changed.

### Remote mutation (explicitly authorized by issue-resolution request)

Created/force-updated 8 labels via `gh label create --force`:

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

### Post-adoption verification

Complete paginated remote inventory after adoption: 46 labels. All 8 catalog labels present with exact name, color, and description. No unrelated labels changed. `ALL_OK True`.

## Idempotency (AC 3)

Repeated the same `gh label create --force` reconciliation for all 8 labels. Before/after remote inventories were identical (`identical True`, count 46). No unnecessary changes. Unrelated labels and existing assignments remained intact.

## Validation and conflict handling (AC 4)

### Invalid/reserved/too-long prefix rejection

Validated with the catalog rules (single lowercase ASCII namespace + `/`, no nested namespace, GitHub 50-char effective name limit, reserved families protected for Standards adopters):

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

Simulated incompatible existing label: `ai/queued` with different color/description was detected as conflict. Simulated case-insensitive collision (`AI/Queued`) detected. Real remote inventory: no collisions, no incompatible catalog labels. No destructive changes performed.

## Custom prefix and migration (AC 2, AC 5)

### Setup

Created dedicated test issues: #45, #46, #47 (fixtures for migration; labeled `type/task`, `status/needs-review` by creation/triage flow). Assigned representative states:
- #45: `ai/queued`
- #46: `ai/processing`
- #47: `ai/blocked`

### Factory prefix installation

Created all 8 `factory/*` labels remotely with identical colors/descriptions and `factory/` prefix. No old `ai/*` labels deleted.

### Migration execution (with interruption/resume)

1. Migrated #45: added `factory/queued`, removed `ai/queued`.
2. Migrated #46: added `factory/processing`, removed `ai/processing`.
3. **Interruption point recorded**: #45,#46 migrated; #47 still had `ai/blocked`.
4. Resumed: migrated #47: added `factory/blocked`, removed `ai/blocked`.

### Post-migration verification

- #45 labels include `factory/queued`, no old `ai/*` catalog label.
- #46 labels include `factory/processing`, no old `ai/*` catalog label.
- #47 labels include `factory/blocked`, no old `ai/*` catalog label.
- All 8 `ai/*` labels still exist remotely (not deleted by default).
- All 8 `factory/*` labels exist remotely.
- No conflicting assignments guessed.

## Controlled failure scenarios (AC 6)

### Insufficient permissions

Attempted label creation with invalid token (`GH_TOKEN=ghp_invalid_token_for_test`):

```
HTTP 401: Bad credentials (https://api.github.com/repos/ailuracollective/test_bots/labels)
rc=1
```

Reported as unverified/failed permission scenario; no mutation performed. No unrelated work disrupted.

### Interrupted migration

Demonstrated by controlled interruption after migrating 2/3 fixture issues and resuming from recorded progress. Resume completed successfully with no duplicate or missing assignment.

## Final repository configuration

Final chosen catalog: **`ai/` (default)**. `factory.json`, `.github/labels.factory-execution.yml`, and `.github/standards.local.yml` agree on `ai/` effective names. `factory/*` labels remain on remote as exercised catalog (no destructive deletion). Fixture issues #45-#47 retain `factory/*` labels as migration evidence unless maintainers request cleanup; they are dedicated test fixtures and can be closed.

## Checks

Local checks run in this worktree (see PR verification for command evidence):

- `uv run ruff check .`
- `uv run ruff format --check .`
- `uv run mypy src/`
- `uv run pytest`

CI/policy checks are reported from the PR after marking ready; `no checks reported` is treated as unresolved.

## Findings / defects

- No Factory catalog/guide defects observed during this exercise. If defects are found during PR review or CI, they will be linked here and to upstream Factory issues; unresolved defects prevent a successful verification claim.
- The `factory` CLI installed in the environment (`factory 0.1.0`) does not expose label adoption/migration commands; this verification followed the published AI-assisted adoption guide and GitHub API/CLI operations.

## Sensitive data

No tokens, credentials, or private secrets included.
