# Repository Structure

```
image-manager/
├── README.md                 # Project overview
├── LICENSE                   # MIT License
│
├── docs/                     # Documentation
│   ├── README.md            # This file
│   ├── architecture.md       # System architecture
│   ├── api-spec.md          # API specification
│   └── roadmap.md           # Project roadmap
│
├── src/                      # Source code
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── config.py            # Configuration
│   │
│   ├── watcher/             # Folder watching module
│   │   ├── __init__.py
│   │   ├── observer.py      # File system observer
│   │   └── queue.py         # Processing queue
│   │
│   ├── classifier/          # AI classification module
│   │   ├── __init__.py
│   │   ├── vision.py        # Vision model integration
│   │   ├── tags.py          # Tag extraction
│   │   └── category.py      # Category classification
│   │
│   ├── album/               # Album generation module
│   │   ├── __init__.py
│   │   ├── generator.py     # Album creation
│   │   ├── grouper.py       # Image grouping logic
│   │   └── metadata.py      # Album metadata
│   │
│   ├── database/            # Data persistence
│   │   ├── __init__.py
│   │   ├── schema.py         # Database schema
│   │   └── queries.py       # Query helpers
│   │
│   └── api/                 # HTTP API server
│       ├── __init__.py
│       ├── routes.py        # API endpoints
│       ├── websocket.py     # WebSocket handler
│       └── middleware.py    # Auth, logging
│
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── test_watcher.py
│   ├── test_classifier.py
│   ├── test_album.py
│   └── test_api.py
│
├── scripts/                  # Utility scripts
│   ├── setup.sh             # Initial setup
│   ├── migrate.py           # Database migrations
│   └── benchmark.py          # Performance testing
│
├── config/
│   └── default.yaml         # Default configuration
│
├── requirements.txt          # Python dependencies
├── requirements-dev.txt     # Development dependencies
├── setup.py                 # Package setup
│
└── .env.example             # Environment template
```

## Key Files

| File | Purpose |
|------|---------|
| `src/main.py` | Service entry point, starts all components |
| `src/config.py` | Loads configuration from env/yaml |
| `src/watcher/observer.py` | `watchdog` file system observer |
| `src/classifier/vision.py` | Vision AI API client |
| `src/album/generator.py` | Album creation logic |
| `src/database/schema.py` | SQLite schema definition |

## Module Dependencies

```
main.py
├── config.py
├── watcher/
│   └── observer.py
├── classifier/
│   └── vision.py
├── album/
│   └── generator.py
└── database/
    └── schema.py
```

## Development Setup

```bash
# Clone and setup
git clone https://github.com/mln330/image-manager.git
cd image-manager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Start service
python -m src.main
```