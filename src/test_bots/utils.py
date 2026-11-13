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


def _greeting(name: str, word: str) -> str:
    """Return a greeting of the form ``{Word}, {name}!``."""
    return f"{word}, {name}!"




def greet(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string of the form ``Hello, {name}!``.
    """
    return _greeting(name, "Hello")


def farewell(name: str) -> str:
    """Return a farewell message for the given name.

    Args:
        name: The name to include in the farewell message.

    Returns:
        A farewell string of the form ``Goodbye, {name}!``.
    """
    return _greeting(name, "Goodbye")


def yo(name: str) -> str:
    """Return a yo message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A yo string of the form ``Yo, {name}!``.
    """
    return _greeting(name, "Yo")


def hey(name: str) -> str:
    """Return a friendly greeting for ``name``."""
    return _greeting(name, "Hey")


def welcome(name: str) -> str:
    """Return a welcome message for ``name``."""
    return _greeting(name, "Welcome")


def hi(name: str) -> str:
    """Return a hi message for ``name``."""
    return _greeting(name, "Hi")


def howdy(name: str) -> str:
    """Return a howdy message for ``name``."""
    return _greeting(name, "Howdy")


def hiya(name: str) -> str:
    """Return a hiya message for ``name``."""
    return _greeting(name, "Hiya")


def sup(name: str) -> str:
    """Return a sup message for ``name``."""
    return _greeting(name, "Sup")


def t(name: str) -> str:
    """Return a t message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A t string of the form ``T, {name}!``.
    """
    return _greeting(name, "T")


def b(name: str) -> str:
    """Return a b message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A b string of the form ``B, {name}!``.
    """
    return _greeting(name, "B")
