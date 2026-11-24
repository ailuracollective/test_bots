"""CLI for test-bots provider/model management."""

import json
from pathlib import Path
from typing import Annotated
from typing import Any

import typer

app = typer.Typer(help="test-bots CLI")

PROVIDERS = {
    "openai": ["gpt-4o", "gpt-4o-mini", "o3"],
    "anthropic": ["claude-sonnet-4-5", "claude-haiku-4-5"],
    "google": ["gemini-2.5-pro", "gemini-2.5-flash"],
}

CONFIG_PATH = Path.home() / ".config" / "test-bots" / "config.json"


def _load_config() -> dict[str, Any]:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())  # type: ignore[no-any-return]
    return {}


def _save_config(cfg: dict[str, Any]) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))


@app.command()
def providers() -> None:
    """List available providers."""
    for name in PROVIDERS:
        typer.echo(name)


@app.command()
def models(provider: str) -> None:
    """List models for a provider."""
    if provider not in PROVIDERS:
        typer.echo(f"Unknown provider: {provider}", err=True)
        raise typer.Exit(code=1)
    for m in PROVIDERS[provider]:
        typer.echo(m)


@app.command()
def configure(
    provider: Annotated[str, typer.Option("--provider", "-p")],
    model: Annotated[str, typer.Option("--model", "-m")],
) -> None:
    """Set the active provider and model."""
    if provider not in PROVIDERS:
        typer.echo(f"Unknown provider: {provider}", err=True)
        raise typer.Exit(code=1)
    if model not in PROVIDERS[provider]:
        typer.echo(f"Unknown model: {model}", err=True)
        raise typer.Exit(code=1)
    cfg = _load_config()
    cfg["provider"] = provider
    cfg["model"] = model
    _save_config(cfg)
    typer.echo(f"Set provider={provider}, model={model}")


@app.command()
def show() -> None:
    """Show the currently configured provider and model."""
    cfg = _load_config()
    typer.echo(f"provider: {cfg.get('provider')}")
    typer.echo(f"model: {cfg.get('model')}")


if __name__ == "__main__":
    app()
