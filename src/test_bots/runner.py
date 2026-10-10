"""Bot runner module."""

import asyncio
import logging

from test_bots.config import BotConfig

logger = logging.getLogger(__name__)


async def run_bot(config: BotConfig) -> None:
    """Run a bot with the given configuration."""
    logger.info("Running bot: %s", config.name)
    try:
        await asyncio.sleep(0.1)
        logger.info("Bot %s completed", config.name)
    except TimeoutError:
        logger.exception("Bot %s timed out after %ss", config.name, config.timeout)
        raise
    except Exception:
        logger.exception("Bot %s failed", config.name)
        raise


async def run_bots(configs: list[BotConfig]) -> None:
    """Run multiple bots concurrently."""
    tasks = [run_bot(config) for config in configs]
    await asyncio.gather(*tasks, return_exceptions=True)
