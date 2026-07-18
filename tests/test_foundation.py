import sqlite3

import pytest

from src.config import ConfigurationError, load_settings
from src.database.schema import initialize_database


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
