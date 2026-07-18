"""Runnable foundation entry point for Image Manager."""

from __future__ import annotations

import logging

from .config import Settings, load_settings
from .database import initialize_database


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def initialize(settings: Settings) -> None:
    """Create service-owned directories and initialize persistent storage."""
    settings.output_directory.mkdir(parents=True, exist_ok=True)
    initialize_database(settings.database_path)


def main() -> int:
    try:
        settings = load_settings()
    except ValueError as error:
        logging.basicConfig(level="ERROR", format="%(levelname)s: %(message)s")
        logging.error("Invalid configuration: %s", error)
        return 2

    configure_logging(settings.log_level)
    initialize(settings)
    logging.getLogger(__name__).info(
        "Image Manager foundation initialized (watching %s)", settings.watch_directory
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
