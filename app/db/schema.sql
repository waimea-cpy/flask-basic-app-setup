-- The schema of the DB, used to initialise it

CREATE TABLE IF NOT EXISTS things (
    `id`    INTEGER PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL
);

