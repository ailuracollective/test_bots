"""Tests for test_bots.utils."""

from test_bots.utils import b
from test_bots.utils import t


def test_t() -> None:
    """t returns a t message."""
    assert t("Alice") == "T, Alice!"
    assert t("") == "T, !"


def test_b() -> None:
    """b returns a b message."""
    assert b("Alice") == "B, Alice!"
    assert b("") == "B, !"
