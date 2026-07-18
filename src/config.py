"""Configuration loading for the Image Manager service."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path


class ConfigurationError(ValueError):
    """Raised when the service configuration is invalid."""


@dataclass(frozen=True)
class Settings:
    """Runtime paths and logging settings.

    Paths are supplied through environment variables so a service unit can run
    the same code in development and production without a checked-in secret.
    """

    watch_directory: Path
    output_directory: Path
    database_path: Path
    log_level: str = "INFO"

    def validate(self) -> None:
        if not self.watch_directory.exists() or not self.watch_directory.is_dir():
            raise ConfigurationError(
                f"IM_WATCH_DIRECTORY must be an existing directory: {self.watch_directory}"
            )
        if self.database_path.exists() and self.database_path.is_dir():
            raise ConfigurationError(
                f"IM_DATABASE_PATH must be a file path: {self.database_path}"
            )
        if self.log_level not in logging.getLevelNamesMapping():
            raise ConfigurationError(
                f"IM_LOG_LEVEL must be a valid logging level: {self.log_level}"
            )


def load_settings(environ: dict[str, str] | None = None) -> Settings:
    """Load settings from ``IM_*`` environment variables and validate them."""
    env = os.environ if environ is None else environ
    settings = Settings(
        watch_directory=Path(env.get("IM_WATCH_DIRECTORY", "./watched")).expanduser(),
        output_directory=Path(env.get("IM_OUTPUT_DIRECTORY", "./output")).expanduser(),
        database_path=Path(env.get("IM_DATABASE_PATH", "./data/image_manager.db")).expanduser(),
        log_level=env.get("IM_LOG_LEVEL", "INFO").upper(),
    )
    settings.validate()
    return settings
