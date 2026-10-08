# Build

Use for build system, bundler, compiler, or packaging changes. A dependency bump that only
changes a lockfile is a `chore`.

Build changes are invisible in review and visible everywhere. State what the output now is, and
prove it is what you intended.

## Linked issue (required)

<!-- The issue must carry `status/ready`. Use a closing keyword on its own line; `Refs #N` does not close it. -->

Closes #

## Type (required)

<!-- Check one. The title type and the label differ: twelve title types, five `type/*` labels. -->

- [ ] `build`

<!-- `type/task` is the catch-all label for this type. -->

## What changed in the build

<!-- The configuration, plugin, or pipeline step that changed, and why. -->

## Why

<!-- What was wrong or missing before this change. -->

## Before / after output

<!-- Bundle size, emitted files or timings, before and after. -->

## Output equivalence

<!-- How you know the artifact is still correct, beyond "it built". -->

## Downstream impact

<!-- Who is affected: package consumers, the publish pipeline, or only this repository's CI. -->

## Packaging and version changes

<!-- What now ships in the artifact and whether the version bumps, or "not published". -->

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
