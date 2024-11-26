import time 
import sqlite3 as sql 

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE growth_experiences (
    growth_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT NOT NULL,  -- 'education', 'money', 'programming'
    description TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
""")
    print("Tabla Creada")
    conn.commit()
    conn.close()

if __name__== "__main__":
    createDB()
    createTable()
   