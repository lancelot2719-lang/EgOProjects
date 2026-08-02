import sqlite3, os, json

db_path = os.path.expanduser(r'~\AppData\Local\Happ\subs.db')
if not os.path.exists(db_path):
    print(f'DB not found at {db_path}')
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print('Tables:', tables)
    
    for table in tables:
        t = table[0]
        print(f'\n=== {t} ===')
        cursor.execute(f'SELECT * FROM "{t}"')
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print('Columns:', columns)
        for row in rows:
            for i, col in enumerate(columns):
                val = row[i]
                if isinstance(val, bytes):
                    try:
                        val = val.decode('utf-8')
                    except:
                        val = f'<bytes: {len(val)} bytes>'
                print(f'  {col}: {val}')
            print()
    conn.close()
