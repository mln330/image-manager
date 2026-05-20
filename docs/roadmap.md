# Roadmap

## 1-Week MVP Build Plan

### Day 1: Foundation
- [ ] Initialize project structure
- [ ] Set up SQLite database schema
- [ ] Basic configuration management
- [ ] Logging setup

### Day 2: Folder Watching
- [ ] Implement watchdog observer
- [ ] Queue management for new files
- [ ] Debouncing logic for rapid file changes
- [ ] Support for JPEG, PNG, WebP formats

### Day 3: Classification
- [ ] Vision API client (OpenAI/Anthropic)
- [ ] Category classification (5 categories)
- [ ] Tag extraction
- [ ] Metadata storage

### Day 4: Album Generation
- [ ] Image grouper by date
- [ ] Album folder creation
- [ ] Album metadata JSON
- [ ] Duplicate detection

### Day 5: API Server
- [ ] Status endpoint
- [ ] Stats endpoint
- [ ] Manual trigger endpoints
- [ ] Basic WebSocket updates

### Day 6: Integration
- [ ] Systemd service setup
- [ ] Cron jobs for periodic processing
- [ ] Log rotation
- [ ] Error handling and recovery

### Day 7: Polish
- [ ] Documentation
- [ ] Error messages
- [ ] Configuration validation
- [ ] Smoke tests

---

## Eventual Enhancements

### UI Dashboard
- Web interface for viewing albums
- Image preview
- Manual classification override
- Search and filter

### Advanced Classification
- Event detection (birthday, wedding, graduation)
- Location inference from image content
- People detection (future: face recognition)

### Export
- Export to Google Photos
- Export to Dropbox
- Export to external drive

### Smart Features
- Face clustering
- Similar image detection
- Auto-tagging improvements
- "Best of" album generation