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
    except Exception as e:
        print(f"Bot {config.name} failed: {e}")
        raise


async def run_bots(configs: list[BotConfig]) -> None:
    """Run multiple bots concurrently."""
    tasks = [run_bot(config) for config in configs]
    await asyncio.gather(*tasks, return_exceptions=True)
