"""Tests for test_bots.utils."""

from test_bots.utils import sup


def test_sup() -> None:
    assert sup("world") == "Sup, world!"
    assert sup("") == "Sup, !"
