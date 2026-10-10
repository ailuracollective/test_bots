"""Bot runner module."""

import asyncio

from test_bots.config import BotConfig


async def run_bot(config: BotConfig) -> None:
    """Run a bot with the given configuration."""
    print(f"Running bot: {config.name}")
    await asyncio.sleep(0.1)
    print(f"Bot {config.name} completed")
