# AGENTS.md

Instructions for agents working in the test_bots Python package and its GitHub
configuration.

## Organization standards

The mandatory organization conventions are in
[.agents/organization-conventions.md](.agents/organization-conventions.md).
Read them before working; they govern issues, pull requests, labels, reviews,
commits, and workflows.

## Repository scope

This repository contains a small Python package, its tests, and GitHub workflows.
Agents read the nearest `AGENTS.md` above files they edit. Do not modify generated
release artifacts such as `CHANGELOG.md` or `.release-please-manifest.json` by
hand.

## Repository context

`test_bots` is a Python 3.12 package managed with uv. The package lives in
`src/test_bots/`, automated tests in `tests/`, and project metadata and tool
configuration in `pyproject.toml`. The repository has an existing
release-please workflow; release and deployment workflows are not part of
standards adoption.

## Repository-specific conventions

- Use uv for dependency and project commands.
- Run Ruff, mypy, and pytest as listed below.
- Preserve the existing release-please action and configuration. Its branch
  trigger, permissions, concurrency and timeout were tightened during adoption;
  release and deployment changes remain out of scope.
  It lives in `.github/workflows/release-please.yml`.
- Policy status comments are disabled until maintainers configure a
  repository-specific write token and matching comment identity.
- Existing remote labels outside the standard manifest are retained; the
  manifest only records the 27 shared labels.

## Development instructions

From the repository root:

```sh
uv sync --extra dev
uv run test-bots
```

## Testing and validation

Run the repository's checks from the root:

```sh
uv run ruff format --check .
uv run ruff check .
uv run mypy src/
uv run pytest
```

Any non-zero exit means that check failed; do not report success unless every
required check passed.

## Git and pull requests

Use lowercase `<github-username>/<type>/<description>` branches and Conventional
Commit titles. Pull request titles use `type: description`; bodies include
`## Linked issue`, `## Summary`, `## Changes`, and `## Verification`, with a
closing keyword for the issue. Apply exactly one `type/*` label. Follow the
organization conventions for draft status and required checks.

The CODEOWNERS catch-all requests review from `@SiddharthaGF` and
`@AiluraCheetah`, both verified to have repository write access. GitHub branch
protection could not be verified because this private repository plan does not
expose the branch-protection API; do not claim code-owner enforcement.

The shared standard's policy action exempts generated `release-please--branches--`
pull requests. The existing release workflow does not enable release-please's
separate release-PR branch workflow.

## Documentation

Update `README.md` when user-facing setup, commands, or behavior changes. Keep
release-generated changelog and manifest files under release-please control.

## Additional references

- `README.md` — setup, development commands, and release flow.
- `pyproject.toml` — dependencies, scripts, lint, type-check, and test settings.
- `.github/workflows/` — continuous integration and release automation.

## Completion requirements

- Read this file and the linked organization conventions before changing files.
- Test the affected behavior and run the repository checks above.
- Open pull requests as drafts. GitHub Actions in this repository skip draft
  pull requests; mark the PR ready for review before expecting CI checks, then
  continue monitoring until each required check succeeds. Report external
  blockers without claiming success.
- A `gh pr checks` response of `no checks reported` is not success. Continue
  querying until checks appear and all required checks complete, or report an
  external blocker.
- Branch protection and ruleset enforcement could not be verified through the
  GitHub API because this private repository's plan does not expose branch
  protection.
