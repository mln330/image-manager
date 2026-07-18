import os
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from src.config import ConfigurationError, load_settings
from src.database.schema import initialize_database


PROJECT_ROOT = Path(__file__).parent.parent


def test_initialize_database_creates_mvp_tables(tmp_path):
    database = tmp_path / "data" / "image_manager.db"

    initialize_database(database)

    with sqlite3.connect(database) as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        version = connection.execute("SELECT version FROM schema_migrations").fetchone()[0]

    assert {"images", "classifications", "albums", "album_images"} <= tables
    assert version == 1


def test_settings_use_environment_paths(tmp_path):
    watched = tmp_path / "watched"
    watched.mkdir()
    settings = load_settings(
        {
            "IM_WATCH_DIRECTORY": str(watched),
            "IM_OUTPUT_DIRECTORY": str(tmp_path / "output"),
            "IM_DATABASE_PATH": str(tmp_path / "data" / "images.db"),
        }
    )

    assert settings.watch_directory == watched
    assert settings.database_path.name == "images.db"


def test_settings_reject_missing_watch_directory(tmp_path):
    with pytest.raises(ConfigurationError):
        load_settings({"IM_WATCH_DIRECTORY": str(tmp_path / "missing")})


def test_main_reports_invalid_log_level_as_configuration_error(tmp_path):
    watched = tmp_path / "watched"
    watched.mkdir()
    environment = os.environ | {
        "IM_WATCH_DIRECTORY": str(watched),
        "IM_OUTPUT_DIRECTORY": str(tmp_path / "output"),
        "IM_DATABASE_PATH": str(tmp_path / "data" / "images.db"),
        "IM_LOG_LEVEL": "not-a-level",
    }

    result = subprocess.run(
        [sys.executable, "-m", "src.main"],
        cwd=PROJECT_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "Invalid configuration: IM_LOG_LEVEL must be a valid logging level" in result.stderr
    assert "Traceback" not in result.stderr
