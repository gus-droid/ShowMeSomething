import sqlite3

# Establish connection with database, and cursor to perform SQL commands 

connection = sqlite3.connect('media.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               image TEXT,
               title TEXT,
               TMDBid TEXT
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Shows(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               image TEXT,
               title TEXT,
               TMDBid TEXT
               )
''')

# after making tables, commit changes
connection.commit()

# Check print tables
# cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

# close connection to database
connection.close()

