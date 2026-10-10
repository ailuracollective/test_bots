"""Tests for test_bots."""

from test_bots import main


def test_main(capsys):
    """Test that main prints the expected message."""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from test-bots!"
