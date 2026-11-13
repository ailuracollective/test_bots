"""Tests for test_bots.utils."""

from test_bots.utils import hey


def test_hey() -> None:
    """hey returns a friendly greeting."""
    assert hey("Alice") == "Hey, Alice!"
    assert hey("") == "Hey, !"
