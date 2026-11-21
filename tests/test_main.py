"""Tests for test_bots."""

import logging
from typing import Any

from test_bots import main
from test_bots.utils import echo
from test_bots.utils import farewell
from test_bots.utils import ping


def test_main(caplog: Any) -> None:
    """Test that main logs the expected message."""
    with caplog.at_level(logging.INFO):
        main()
    assert "Hello from test-bots!" in caplog.text


def test_ping() -> None:
    """Test that ping returns pong."""
    assert ping() == "pong"


def test_echo() -> None:
    """Test that echo returns the same text."""
    assert echo("hi") == "hi"


def test_farewell() -> None:
    """Test that farewell returns a goodbye message."""
    assert farewell("World") == "Goodbye, World!"
