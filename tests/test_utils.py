"""Tests for test_bots.utils."""

from test_bots.utils import farewell


def test_farewell() -> None:
    """Test that farewell returns the expected message."""
    assert farewell("Alice") == "Goodbye, Alice!"
