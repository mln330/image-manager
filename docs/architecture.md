# Architecture

## System Overview

The Image Manager service processes images through a pipeline:

```
[Watched Folder] → [Watcher] → [Classifier] → [Album Generator] → [Output]
```

## Components

### 1. Watcher (`src/watcher/`)
- Monitors a configured folder for new image files
- Supports formats: JPEG, PNG, WebP, HEIC, RAW
- Debounces rapid file changes
- Triggers classification pipeline on new files

**States:**
- `idle` — watching for changes
- `processing` — file detected, queued for classification
- `error` — folder inaccessible or unsupported format

### 2. Classifier (`src/classifier/`)
- Sends images to vision model API
- Extracts classification data:
  - **Category**: object type, scene type, activity
  - **Confidence**: classification confidence score
  - **Tags**: detected objects, colors, themes

**Output schema:**
```json
{
  "file_id": "uuid",
  "path": "/path/to/image.jpg",
  "classified_at": "ISO8601",
  "category": {
    "primary": "outdoor|indoor|portrait|event|landscape|other",
    "secondary": "specific type",
    "confidence": 0.95
  },
  "tags": ["beach", "sunset", "family"],
  "inferred_date": "2024-01-15",
  "inferred_location": null
}
```

### 3. Album Generator (`src/album/`)
- Groups images by category, date, event, location
- Creates album folders in output directory
- Generates album metadata JSON

**Album structure:**
```
output/
├── albums/
│   ├── 2024-01_beach-day/
│   │   ├── album.json
│   │   ├── IMG_001.jpg
│   │   └── IMG_002.jpg
│   └── 2024-02_family-event/
│       ├── album.json
│       └── ...
```

## Data Flow

```
1. Watcher detects new file
2. File added to classification queue
3. Classifier processes image → generates metadata
4. Metadata stored in SQLite DB
5. Album Generator runs periodically (cron)
6. Album Generator groups images → creates albums
7. Albums written to output folder
```

## Storage

- **Database**: SQLite (`image_manager.db`)
  - `images` table: all processed images
  - `albums` table: generated albums
  - `classifications` table: AI classification results

- **Output**: 
  - Structured albums in configured output folder
  - Logs in `logs/` directory

## Deployment

- Runs as system service (systemd)
- Cron jobs for periodic processing
- Logs rotated daily