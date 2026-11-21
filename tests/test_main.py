"""Tests for test_bots."""

import logging

from test_bots import main
from test_bots.utils import farewell


def test_main(caplog):
    """Test that main logs the expected message."""
    with caplog.at_level(logging.INFO):
        main()
    assert "Hello from test-bots!" in caplog.text


def test_farewell():
    """Test that farewell returns a goodbye message."""
    assert farewell("World") == "Goodbye, World!"
