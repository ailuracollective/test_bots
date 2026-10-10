"""Bot runner module."""

import asyncio

from test_bots.config import BotConfig


async def run_bot(config: BotConfig) -> None:
    """Run a bot with the given configuration."""
    print(f"Running bot: {config.name}")
    try:
        await asyncio.sleep(0.1)
        print(f"Bot {config.name} completed")
    except asyncio.TimeoutError:
        print(f"Bot {config.name} timed out after {config.timeout}s")
        raise
