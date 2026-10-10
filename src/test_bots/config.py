"""Bot configuration module."""

from dataclasses import dataclass
from dataclasses import field


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
            msg = "timeout must be positive"
            raise ValueError(msg)
        if self.retries < 0:
            msg = "retries cannot be negative"
            raise ValueError(msg)
