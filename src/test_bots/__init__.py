"""Test Bots - Proyecto de pruebas."""

import logging

__version__ = "0.1.0"

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the test-bots CLI."""
    logger.info("Hello from test-bots!")


if __name__ == "__main__":
    main()
