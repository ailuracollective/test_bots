"""Bot configuration module."""

from dataclasses import dataclass, field


@dataclass
class BotConfig:
    """Configuration for a bot."""

    name: str
    timeout: int = 30
    retries: int = 3
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if self.timeout <= 0:
            raise ValueError("timeout must be positive")
        if self.retries < 0:
            raise ValueError("retries cannot be negative")
