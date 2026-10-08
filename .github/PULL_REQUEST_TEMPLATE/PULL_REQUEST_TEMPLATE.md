# Pull Request

<!-- Fallback for a title type with no template. Prefer that type's own template. -->

## Linked issue (required)

<!-- The issue must carry `status/ready`. Use a closing keyword on its own line; `Refs #N` does not close it. -->

Closes #

## Type (required)

<!-- Check one. The title type and the label differ: twelve title types, five `type/*` labels. -->

- [ ] `<type>`

<!-- Allowed: breaking-change, build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test. -->

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
