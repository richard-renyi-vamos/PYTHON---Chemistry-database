import sqlite3

# Connect to a database or create one if it doesn't exist
conn = sqlite3.connect('chemistry.db')
cursor = conn.cursor()

# Create tables for chemical elements and compounds
cursor.execute('''
CREATE TABLE IF NOT EXISTS elements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    atomic_number INTEGER NOT NULL,
    atomic_weight REAL,
    group_number INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS compounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    formula TEXT NOT NULL,
    molecular_weight REAL,
    state_at_room_temp TEXT
)
''')

conn.commit()
