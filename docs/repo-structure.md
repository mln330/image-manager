# Repository Structure

The repository currently contains the runnable foundation: configuration,
logging, and SQLite schema initialization. Folder watching, image
classification, album generation, and an HTTP API are planned work and are not
implemented yet.

```
image-manager/
├── README.md                 # Project overview and foundation run instructions
├── LICENSE                   # MIT License
├── .env.example              # Environment-variable template
├── requirements-dev.txt      # Development and test dependencies
│
├── docs/                     # Project documentation
│   ├── architecture.md       # Target architecture
│   ├── api-spec.md           # Planned API specification
│   ├── repo-structure.md     # This file
│   └── roadmap.md            # Implementation roadmap
│
├── src/                      # Runnable foundation source
│   ├── __init__.py
│   ├── main.py               # Loads settings, configures logging, initializes storage
│   ├── config.py             # Environment-based settings validation
│   └── database/
│       ├── __init__.py
│       └── schema.py         # SQLite schema initialization
│
└── tests/                    # Foundation test suite
    ├── __init__.py
    └── test_foundation.py
```

## Key Files

| File | Purpose |
|------|---------|
| `src/main.py` | Foundation entry point; configures logging and initializes the output directory and database |
| `src/config.py` | Loads and validates `IM_*` environment variables |
| `src/database/schema.py` | Creates the SQLite schema and records its version |
| `.env.example` | Documents the supported environment variables |
| `requirements-dev.txt` | Lists development and test dependencies |

There is currently no `requirements.txt` or checked-in YAML configuration.
Runtime configuration is supplied through environment variables.

## Current Module Dependencies

```
main.py
├── config.py
└── database/
    └── schema.py
```

## Development Setup

```bash
# Clone and set up
git clone https://github.com/mln330/image-manager.git
cd image-manager
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Start the runnable foundation (the default watched directory must exist)
mkdir -p watched
python -m src.main
```

Configure runtime paths with `IM_WATCH_DIRECTORY`, `IM_OUTPUT_DIRECTORY`, and
`IM_DATABASE_PATH`; see `.env.example` for the full list.
