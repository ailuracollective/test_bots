"""Tests for test_bots.utils."""

from test_bots.utils import sup


def test_sup() -> None:
    """sup returns the expected greeting."""
    assert sup("world") == "Sup, world!"
    assert sup("") == "Sup, !"
