"""Tests for test_bots.utils."""

from test_bots.utils import yo


def test_yo() -> None:
    """yo returns the expected greeting."""
    assert yo("world") == "Yo, world!"
