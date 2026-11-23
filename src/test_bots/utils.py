import logging
import re

logger = logging.getLogger(__name__)


def ping() -> str:
    return "pong"


def echo(text: str) -> str:
    return text


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def validate_name(name: str) -> bool:
    if not name or not name.strip():
        return False
    return bool(re.match(r"^[a-zA-Z0-9_-]+$", name.strip()))


def sanitize_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "", name.strip())
