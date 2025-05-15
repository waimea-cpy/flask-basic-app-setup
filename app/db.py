#===========================================================
# Database Related Functions
#===========================================================

import sqlite3
import os


DB_FOLDER   = os.path.join(os.path.dirname(__file__), "db")
DB_FILE     = os.path.join(DB_FOLDER, "data.db")
SCHEMA_FILE = os.path.join(DB_FOLDER, "schema.sql")


#-----------------------------------------------------------
# Connect to the database file and return the connection
#-----------------------------------------------------------
def connect_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Want rows as dicts
    return conn


#-----------------------------------------------------------
# Initialise the DB from the schema file
#-----------------------------------------------------------
def init_db():
    conn = connect_db()
    with open(SCHEMA_FILE, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

