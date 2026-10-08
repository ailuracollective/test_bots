# test_bots

A scratch repository in `ailuracollective` where the organisation's bots interact
with each other and where AI automations are tested. It currently holds no
application code — it holds the organisation's GitHub contribution standard and
the tooling that checks it.

- `AGENTS.md` — instructions for agents and contributors. Read it first.
- `.agents/organization-conventions.md` — the organisation's mandatory
  conventions (copied from `ailuracollective/standards`).
- `.github/` — the five standard artifacts: `ISSUE_STANDARD.md`,
  `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE/`, `labels.yml`, `CODEOWNERS`.
- `.github/workflows/` — `policy.yml` (contribution gate), `ci.yml` (lint and
  schema checks), `release.yml` (release-please).

## Checks

```sh
uv sync --locked

uv run yamllint .
uv run mdlint check . .github
uv run actionlint .github/workflows/*.yml
uv run yamlfix --check -i '*.yml' -e '.cache/**' -e '.github/standards.local.example.yml' .
```

The full list, including the schema checks, lives in `.github/workflows/ci.yml`.

## Repository secrets

Two repository secrets drive the automation:

| Secret                       | Used by       | Purpose                                  |
| ---------------------------- | ------------- | ---------------------------------------- |
| `AILURA_PR_COMPLIANCE_TOKEN` | `policy.yml`  | the status comment on every pull request |
| `AILURA_RELEASE_TOKEN`       | `release.yml` | release-please: release PR, tag, release |

## Adopting and customising

The standard is copied by hand from [`ailuracollective/standards`](https://github.com/ailuracollective/standards);
there is no sync mechanism, so drift is the default state. This repository is
currently an exact copy of the standard. To deviate, copy
`.github/standards.local.example.yml` to `.github/standards.local.yml` and
declare each change there — it records the deviation; it does not configure
anything.

## License

MIT — see [LICENSE](LICENSE).
