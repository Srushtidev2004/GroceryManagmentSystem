import sqlite3

def initialize_db():
    conn = sqlite3.connect('grocery.db')
    cursor = conn.cursor()

    # Create admin, employee, and product tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            Date INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            username TEXT UNIQUE,
            password TEXT)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            quantity INTEGER)
    ''')

    # Insert default admin
    cursor.execute('''
        INSERT OR IGNORE INTO admin (username, password) VALUES (?, ?)
    ''', ('admin', 'admin123'))

    conn.commit()
    conn.close()

initialize_db()
