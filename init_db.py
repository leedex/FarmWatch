import sqlite3

def init_db():
    conn = sqlite3.connect('crop_monitor.db')  # Creates the database file
    c = conn.cursor()

    # Create table for storing crop data
    c.execute('''
        CREATE TABLE IF NOT EXISTS crops (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            health_status TEXT NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized")
