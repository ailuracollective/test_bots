"""Utility functions for test bots."""

import logging
import re

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def validate_name(name: str) -> bool:
    """Validate that a bot name is not empty and contains only valid characters."""
    if not name or not name.strip():
        return False
    return bool(re.match(r"^[a-zA-Z0-9_-]+$", name.strip()))


def sanitize_name(name: str) -> str:
    """Sanitize a bot name by removing invalid characters."""
    return re.sub(r"[^a-zA-Z0-9_-]", "", name.strip())
