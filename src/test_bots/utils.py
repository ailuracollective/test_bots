"""Utility functions for test bots."""

import logging

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def validate_name(name: str) -> bool:
    """Validate that a bot name is not empty."""
    return bool(name and name.strip())
