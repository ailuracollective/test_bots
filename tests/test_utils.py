"""Tests for test_bots.utils."""

from test_bots.utils import greet


def test_greet() -> None:
    """greet returns the expected greeting."""
    assert greet("world") == "Hello, world!"
