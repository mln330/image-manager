# Image Manager

AI-powered image classification and album generation service.

## Overview

A personal AI service that monitors a watched folder for new images, classifies them using vision AI, and generates organized albums based on detected categories, events, locations, and dates.

## Features

- **Folder Watching**: Monitors a designated folder for new images
- **AI Classification**: Uses vision models to categorize images
- **Album Generation**: Automatically groups images into albums
- **Metadata Extraction**: Extracts date, location (inferred), and category data

## Current Status

The runnable foundation is in place: configuration, logging, and SQLite schema
initialization. Folder watching, AI classification, and album generation remain
the next planned work packages.

## Run the foundation

```bash
mkdir -p watched
python -m src.main
```

Configure paths with the `IM_WATCH_DIRECTORY`, `IM_OUTPUT_DIRECTORY`, and
`IM_DATABASE_PATH` environment variables; see `.env.example`.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Watcher    │────▶│ Classifier   │────▶│ Album Gen   │
│  (folder)   │     │ (vision AI)  │     │ (grouping)  │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Project Structure

```
image-manager/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── api-spec.md
│   └── repo-structure.md
├── src/
│   ├── watcher/        # Folder monitoring
│   ├── classifier/     # AI classification
│   └── album/          # Album generation
├── tests/
└── scripts/
```

## Roadmap

### Phase 1: Foundation (Current)
- Folder watching ✅
- Basic AI classification ✅
- Album output (logs + files) ✅

### Phase 2: Enhancements
- [ ] UI dashboard
- [ ] Event detection
- [ ] Location inference
- [ ] Date-based grouping

### Phase 3: Advanced
- [ ] Face recognition
- [ ] Similarity clustering
- [ ] Export to cloud services

## Quick Links

- [Architecture Documentation](docs/architecture.md)
- [API Specification](docs/api-spec.md)
- [Repository Structure](docs/repo-structure.md)
