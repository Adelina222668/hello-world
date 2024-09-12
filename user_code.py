import sqlite3

#Hello world
def get_db_connection():
    try:
        conn = sqlite3.connect('autoscraper.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def initialize_db():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS run_counter (
                count INTEGER
            )
        ''')
        cursor.execute
        conn.commit()
        conn.close()
        else: print("Failed to connect to the database.") 


AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' print("AWS Secret Access Key:", AWS_SECRET_ACCESS_KEY)