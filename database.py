import sqlite3

# 📌 Connect to SQLite database
def connect_db():
    return sqlite3.connect("csv_analyzer.db")

# 🛠️ Create necessary tables
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Table for uploaded file metadata
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS file_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            uploaded_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            rows INTEGER,
            columns INTEGER
        )
    ''')

    # ✅ New table for prediction history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            model_type TEXT,
            target_column TEXT,
            score REAL,
            predicted_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# 📥 Insert file metadata
def insert_metadata(filename, rows, columns):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO file_metadata (filename, rows, columns)
        VALUES (?, ?, ?)
    ''', (filename, rows, columns))
    conn.commit()
    conn.close()

# 📊 Get recent uploaded file metadata
def get_metadata():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT filename, uploaded_on, rows, columns
        FROM file_metadata
        ORDER BY uploaded_on DESC
        LIMIT 10
    ''')
    data = cursor.fetchall()
    conn.close()
    return data

# 🤖 Insert prediction record
def insert_prediction(filename, model_type, target_column, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO prediction_history (filename, model_type, target_column, score)
        VALUES (?, ?, ?, ?)
    ''', (filename, model_type, target_column, score))
    conn.commit()
    conn.close()

# 📂 Get recent prediction records
def get_prediction_history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT filename, model_type, target_column, score, predicted_on
        FROM prediction_history
        ORDER BY predicted_on DESC
        LIMIT 10
    ''')
    data = cursor.fetchall()
    conn.close()
    return data
