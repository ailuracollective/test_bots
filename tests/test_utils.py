"""Tests for test_bots.utils."""

from test_bots.utils import b
from test_bots.utils import farewell
from test_bots.utils import greet
from test_bots.utils import hey
from test_bots.utils import hi
from test_bots.utils import howdy
from test_bots.utils import t
from test_bots.utils import welcome
from test_bots.utils import yo


def test_greet() -> None:
    assert greet("world") == "Hello, world!"


def test_farewell() -> None:
    assert farewell("Alice") == "Goodbye, Alice!"


def test_yo() -> None:
    assert yo("world") == "Yo, world!"


def test_hey() -> None:
    assert hey("Alice") == "Hey, Alice!"
    assert hey("") == "Hey, !"


def test_welcome() -> None:
    assert welcome("Alice") == "Welcome, Alice!"


def test_hi() -> None:
    assert hi("Alice") == "Hi, Alice!"


def test_howdy() -> None:
    assert howdy("Alice") == "Howdy, Alice!"


def test_t() -> None:
    assert t("Alice") == "T, Alice!"


def test_b() -> None:
    assert b("Alice") == "B, Alice!"
