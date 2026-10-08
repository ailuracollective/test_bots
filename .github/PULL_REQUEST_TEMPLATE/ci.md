# Continuous integration

Use for changes to workflows, actions, or automation that runs on pull requests.

CI runs with repository permissions on every pull request, including from forks. Treat a change
here as a security change.

## Linked issue (required)

<!-- The issue must carry `status/ready`. Use a closing keyword on its own line; `Refs #N` does not close it. -->

Closes #

## Type (required)

<!-- Check one. The title type and the label differ: twelve title types, five `type/*` labels. -->

- [ ] `ci`

<!-- `type/task` is the catch-all label for this type. -->

## What changes in CI

<!-- Which workflow or action changes, and what it will do differently. -->

## Why

<!-- What failure this prevents or what capability it adds. -->

## Effect on pull requests

<!-- Runtime added, checks added or removed, and whether contributors will see new required checks. -->

## Permissions and secrets

<!-- The `permissions:` and `secrets:` this grants, and the blast radius. -->

## Failure mode

<!-- What happens if this workflow is wrong or unavailable: does it block merges or silently pass? -->

## How to reproduce locally

<!-- How to exercise the change before it runs on someone else's pull request. -->

## Test plan

<!-- The checks this repository's CI runs: `.github/workflows/ci.yml`. -->
<!-- Run `uv sync --locked` first; every command below lives in that workflow. -->

- [ ] `uv run yamllint .`
- [ ] `uv run mdlint check . .github`
- [ ] `uv run actionlint .github/workflows/*.yml` (workflow changes only)
- [ ] `uv run yamlfix --check -i '*.yml' -e '.cache/**' -e '.github/standards.local.example.yml' .`
- [ ] Manually exercised the change end to end

## Contributor checklist

- [ ] Linked an approved issue with `Closes #N`, `Fixes #N` or `Resolves #N`
- [ ] The linked issue carries the `status/ready` label
- [ ] Branch is named `<github-username>/<type>/<description>`, all lowercase
- [ ] Applied exactly one `type/*` label
- [ ] Commit messages follow Conventional Commits
- [ ] No `Co-Authored-By` trailers
- [ ] Documentation updated where public behavior or configuration changed
- [ ] All CI checks pass
