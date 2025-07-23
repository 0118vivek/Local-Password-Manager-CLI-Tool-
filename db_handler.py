# SQLite Credential Store

import sqlite3

def init_db():
    conn = sqlite3.connect("vault.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY,
        site TEXT,
        username TEXT,
        password TEXT
    )''')
    conn.commit()
    conn.close()

def add_credential(site, username, enc_password):
    conn = sqlite3.connect("vault.db")
    c = conn.cursor()
    c.execute("INSERT INTO credentials (site, username, password) VALUES (?, ?, ?)", (site, username, enc_password))
    conn.commit()
    conn.close()

def get_credentials():
    conn = sqlite3.connect("vault.db")
    c = conn.cursor()
    c.execute("SELECT site, username, password FROM credentials")
    return c.fetchall()
