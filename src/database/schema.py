"""SQLite schema creation and migration entry point."""

from __future__ import annotations

import sqlite3
from pathlib import Path


SCHEMA_VERSION = 1


def initialize_database(database_path: Path) -> None:
    """Create the MVP schema if it has not already been initialized."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database_path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version INTEGER PRIMARY KEY,
                applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS images (
                id TEXT PRIMARY KEY,
                path TEXT NOT NULL UNIQUE,
                captured_at TEXT,
                processed_at TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS classifications (
                id TEXT PRIMARY KEY,
                image_id TEXT NOT NULL REFERENCES images(id) ON DELETE CASCADE,
                primary_category TEXT NOT NULL,
                secondary_category TEXT,
                confidence REAL NOT NULL CHECK(confidence >= 0 AND confidence <= 1),
                tags_json TEXT NOT NULL DEFAULT '[]',
                inferred_date TEXT,
                inferred_location TEXT,
                classified_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS albums (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                path TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS album_images (
                album_id TEXT NOT NULL REFERENCES albums(id) ON DELETE CASCADE,
                image_id TEXT NOT NULL REFERENCES images(id) ON DELETE CASCADE,
                PRIMARY KEY (album_id, image_id)
            );

            CREATE INDEX IF NOT EXISTS idx_classifications_image_id
                ON classifications(image_id);
            CREATE INDEX IF NOT EXISTS idx_album_images_image_id
                ON album_images(image_id);
            """
        )
        connection.execute(
            "INSERT OR IGNORE INTO schema_migrations (version) VALUES (?)",
            (SCHEMA_VERSION,),
        )
