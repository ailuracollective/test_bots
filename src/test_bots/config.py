"""Bot configuration module."""

from dataclasses import dataclass


@dataclass
class BotConfig:
    """Configuration for a bot."""

    name: str
    timeout: int = 30
    retries: int = 3
