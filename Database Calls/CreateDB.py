import sqlite3
import os

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()

# Create Table
cursor.execute("""CREATE TABLE IF NOT EXISTS Items (
    ItemID INTEGER PRIMARY KEY,
    ItemName TEXT NOT NULL,
    Location TEXT NOT NULL,
    DirecImage TEXT NOT NULL,
    DateFound DATE NOT NULL,
    Tags TEXT NOT NULL,
    Found INTEGER DEFAULT 0,
    Security INTEGER DEFAULT 0,
    FreeToAll INTEGER DEFAULT 0
)""")

conn.commit()
conn.close()
