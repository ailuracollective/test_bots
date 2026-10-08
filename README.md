# test_bots

A scratch repository in `ailuracollective` where the organisation's bots interact
with each other and where AI automations are tested. It is also the base for
adopting the organisation's GitHub standard: the standard artifacts are copied
here by hand, and the CI/CD workflows are skeletons that a repository's own stack
completes.

The template is **technology-agnostic**: no language or toolchain is fixed here.
Nothing that names one (a package manager, lint tools, a CI command) belongs to
the template.

## Layout

- `AGENTS.md` — instructions for agents and contributors. Read it first.
- `.agents/organization-conventions.md` — the organisation's mandatory
  conventions (copied from `ailuracollective/standards`).
- `.github/` — the five standard artifacts: `ISSUE_STANDARD.md`,
  `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE/`, `labels.yml`, `CODEOWNERS`.
- `.github/workflows/` —
  - `policy.yml` — the contribution gate. **Complete and intact**: branch name,
    pull-request title and body, issue triage.
  - `ci.yml` — **template**: the job skeleton is there, the checks are not. Add
    this repository's own checks.
  - `release.yml` — **template**: the release-aware skeleton with a placeholder
    step. Fill it in once there is something to release.

## Checks

There are none yet: `ci.yml` is a template and runs no checks until this
repository's tooling is chosen, so no pull request claims a check that does not
run. Until then, verify the invariants by hand:

```sh
# every label named by a template or workflow must exist on the remote
gh label list --limit 100 --json name --jq '.[].name' | sort

# the vocabulary the gate reads
grep -A3 'type-labels:\|approved-label:' .github/workflows/policy.yml

# the vocabulary the templates name
grep -rhoE 'type/[a-z-]+|status/[a-z-]+' .github/ISSUE_TEMPLATE .github/PULL_REQUEST_TEMPLATE | sort -u
```

## Repository secrets

- `AILURA_PR_COMPLIANCE_TOKEN` — used by `policy.yml` for the status comment on
  every pull request. Required for the gate to write its comment.
- `AILURA_RELEASE_TOKEN` — needed only once `release.yml` is completed.

## Adopting and customising

The standard is copied by hand from
[`ailuracollective/standards`](https://github.com/ailuracollective/standards);
there is no sync mechanism, so drift is the default state. This repository is
currently an exact copy of the standard. To deviate, copy
`.github/standards.local.example.yml` to `.github/standards.local.yml` and
declare each change there — it records the deviation; it does not configure
anything.

## License

MIT — see [LICENSE](LICENSE).