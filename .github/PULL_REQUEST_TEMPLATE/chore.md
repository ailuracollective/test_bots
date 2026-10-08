# Chore

Use for technical maintenance with no intended functional change. If the change is user-visible
it is not a chore.

State the preservation guarantees explicitly. "No functional change" is a claim that has to be
defended, not asserted.

## Linked issue (required)

<!-- The issue must carry `status/ready`. Use a closing keyword on its own line; `Refs #N` does not close it. -->

Closes #

## Type (required)

<!-- Check one. The title type and the label differ: twelve title types, five `type/*` labels. -->

- [ ] `chore`

<!-- `type/task` is the catch-all label for this type. -->

## What is being changed

<!-- The cleanup: what is removed, simplified, or maintained. -->

## Why now

<!-- What makes this worth doing now rather than later. -->

## Behavior preserved

<!-- State that observable behavior is unchanged. If it changes, this is not a chore. -->

## Public API preserved

<!-- State explicitly whether exported signatures change. If none do, say "no public API change". -->

## Risk and rollback

<!-- What could go wrong, and how to revert it if it does. -->

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
