# API Specification

## Internal API

The Image Manager exposes internal endpoints for status and control.

### Base URL
`http://localhost:8765/api/v1`

### Endpoints

#### `GET /status`
Returns current service status.

**Response:**
```json
{
  "status": "running|idle|error",
  "uptime_seconds": 12345,
  "watching_folder": "/path/to/folder",
  "last_processed": "ISO8601",
  "queue_size": 0
}
```

#### `GET /stats`
Returns processing statistics.

**Response:**
```json
{
  "total_images": 1523,
  "total_albums": 47,
  "processing_rate_per_hour": 12.5,
  "storage_used_gb": 8.2
}
```

#### `GET /images`
Returns list of processed images.

**Query params:**
- `limit` (int, default 50)
- `offset` (int, default 0)
- `category` (string, optional)

**Response:**
```json
{
  "images": [...],
  "total": 1523,
  "limit": 50,
  "offset": 0
}
```

#### `GET /albums`
Returns list of generated albums.

**Response:**
```json
{
  "albums": [
    {
      "id": "uuid",
      "name": "2024-01_beach-day",
      "path": "/output/albums/2024-01_beach-day",
      "image_count": 24,
      "created_at": "ISO8601"
    }
  ]
}
```

#### `POST /classify`
Manually trigger classification of a file.

**Request:**
```json
{
  "path": "/path/to/image.jpg"
}
```

**Response:**
```json
{
  "job_id": "uuid",
  "status": "queued"
}
```

#### `POST /generate-albums`
Manually trigger album generation.

**Response:**
```json
{
  "albums_created": 3,
  "images_processed": 45
}
```

#### `DELETE /images/{id}`
Remove image from database and albums.

**Response:**
```json
{
  "deleted": true
}
```

## WebSocket Events

Connect to `ws://localhost:8765/ws` for real-time updates.

**Event types:**
- `image.classified` — new image classified
- `album.created` — new album generated
- `queue.updated` — queue size changed
- `error` — error occurred