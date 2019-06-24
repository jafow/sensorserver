DROP TABLE IF EXISTS climate;

CREATE TABLE climate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    temperature REAL,
    humidity REAL,
    created_at TEXT NOT NULL
)
