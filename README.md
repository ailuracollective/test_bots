# test-bots

Proyecto de pruebas con Python + uv + release-please.

## Setup

```bash
# Instalar dependencias (crea .venv automáticamente)
uv sync

# Instalar en modo desarrollo con todas las dependencias
uv sync --extra dev
```

## Desarrollo

```bash
# Ejecutar el CLI
uv run test-bots

# Formatear código
uv run ruff format .

# Lint
uv run ruff check .

# Type checking
uv run mypy src/

# Tests
uv run pytest
```

## Release flow (release-please)

Este proyecto usa [release-please](https://github.com/googleapis/release-please) para generar releases automáticamente desde conventional commits.

### Conventional commits

Los commits **deben** seguir el formato [Conventional Commits](https://www.conventionalcommits.org/):

| Tipo | Descripción | Bump de versión |
|------|-------------|-----------------|
| `feat:` | Nueva feature | minor (`0.1.0` → `0.2.0`) |
| `fix:` | Bug fix | patch (`0.1.0` → `0.1.1`) |
| `docs:` | Solo documentación | ninguno |
| `style:` | Formato, sin cambios de código | ninguno |
| `refactor:` | Refactor, no fix ni feature | ninguno |
| `perf:` | Mejora de performance | patch |
| `test:` | Tests | ninguno |
| `chore:` | Build, deps, tooling | ninguno |
| `ci:` | CI/CD changes | ninguno |
| `revert:` | Revert commit | según el commit revertido |
| `feat!:` o `BREAKING CHANGE:` en footer | Breaking change | major (`0.1.0` → `1.0.0`) |

### Flujo de release

1. **Push a `main`**: Cada push a `main` con conventional commits activa el workflow de release-please.
2. **PR de release**: Release-please crea/actualiza un PR `chore: release X.Y.Z` acumulando todos los cambios desde la última release.
3. **Merge del PR**: Al mergear el PR de release, release-please crea automáticamente:
   - El tag `vX.Y.Z`
   - La GitHub Release con el changelog
   - Actualiza `CHANGELOG.md` y `.release-please-manifest.json`

### Ejemplo de uso

```bash
# Desarrollo normal con conventional commits
git commit -m "feat: add bot configuration module"
git commit -m "fix: handle timeout in bot runner"
git commit -m "feat!: migrate to async architecture"

# Push a main → release-please crea PR de release automáticamente
git push origin main

# En GitHub: review y merge del PR "chore: release 0.2.0"
# → Se crea el tag v0.2.0 y la release con changelog
```

## Estructura

```
.
├── .github/workflows/release-please.yml  # Workflow de release-please
├── src/test_bots/                         # Código fuente
│   └── __init__.py
├── pyproject.toml                         # Configuración del proyecto (uv + hatchling)
├── release-please-config.json             # Config de release-please
└── .release-please-manifest.json          # Versión actual (se actualiza automáticamente)
```
