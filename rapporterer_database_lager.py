"""this script is used to create the database and add test records"""
import sqlite3

# 1. Configuration - This MUST match what your app uses

DB_FILE = "database.db"

def create_users():
    conn = sqlite3.connect(DB_FILE)
    # Ensure table exists with 'pasword' (matching your app.py)
    conn.execute("CREATE TABLE IF NOT EXISTS problem (email TINYTEXT, extra_info TEXT)")
    
    records_to_add = int(input("How many random records do you want to add? "))
    
    # Hashing logic with the Secret Key (Pepper)

    # Add the Test record (use last_email/last_extra_info for sample output)
    last_email = "test@example.com"
    last_extra_info = "Test problem"
    conn.execute("INSERT INTO problem (email, extra_info) VALUES (?, ?)", 
                 (last_email, last_extra_info))

    # Add Random Records
    for _ in range(records_to_add):
        email = f"user{_}@example.com"
        extra_info = f"Extra info for user {_}"
        
        conn.execute("INSERT INTO problem (email, extra_info) VALUES (?, ?)", 
                     (email, extra_info))
        # remember last values for sample output
        last_email = email
        last_extra_info = extra_info
    conn.commit()
    conn.close()
    
    print("-" * 30)
    print("DATABASE UPDATED SUCCESSFULLY")
    print(f"Try submitting a ticket with -> Email: {last_email} | Extra Info: {last_extra_info}")
    print("-" * 30)

if __name__ == "__main__":
    create_users()
    
#   run
#   CD "C:\Users\henrik\OneDrive - Innlandet fylkeskommune\vidregående\Drifsstøtte\Egen oppgave\Flask test"
#   python rapporterer_database_lager.py
#   flask run

"""Data Types

#* NULL TYPE:
    NULL                no value / unknown value

--------------------------------
#* most popular SQL Data Types
-------------------------------
    TEXT               text strings
        VARCHAR(n)      variable-length string with max length n
        CHAR(n)         fixed-length string with length n
    INTEGER            whole numbers
    REAL               floating point numbers(10.5, -3.14, etc)
    BOOL / BOOLEAN     true or false values
    BLOB               binary large object (images, files, etc)


--------------------------------
#* String / Text Data Types:
--------------------------------
    CHAR(n)             fixed-length string with length n
    VARCHAR(n)          variable-length string with max length n
    TEXT                text strings (up to 65,535 characters)
    TINYTEXT            up to 255 characters
    MEDIUMTEXT          up to 16,777,215 characters
    LONGTEXT            up to 4,294,967,295 characters
    NCHAR(n)            fixed-length Unicode string
    NVARCHAR(n)         variable-length Unicode string
    CLOB                character large object (very large text)
    ENUM('a','b',...)   string object with predefined set of values
    SET('a','b',...)    string object that can store multiple predefined values

--------------------------------
#* Numeric Data Types:
--------------------------------
    TINYINT             very small integer (-128 to 127)
    SMALLINT            small integer (-32,768 to 32,767)
    MEDIUMINT           medium integer (-8,388,608 to 8,388,607)
    INT / INTEGER       standard integer (-2,147,483,648 to 2,147,483,647)
    BIGINT              large integer (-9 quintillion to +9 quintillion)
    FLOAT               single-precision floating point number
    REAL                floating point number (approximate)
    DOUBLE              double-precision floating point number
    NUMERIC(p,s)        exact numeric with precision and scale
    DECIMAL(p,s)        same as NUMERIC; fixed-point exact numbers

--------------------------------
#* Date and Time Data Types:
--------------------------------
    DATE                date value (YYYY-MM-DD)
    TIME                time value (HH:MM:SS)
    DATETIME            date and time combination (YYYY-MM-DD HH:MM:SS)
    TIMESTAMP           date & time with auto-update capabilities
    YEAR                year value (2 or 4 digits)

--------------------------------
#* Binary Data Types:
--------------------------------
    BINARY(n)           fixed-length binary data(n must be between 1 and 8000)
    VARBINARY(n)        variable-length binary data
    TINYBLOB            binary large object (up to 255 bytes)
    BLOB                binary large object (up to 65,535 bytes)
    MEDIUMBLOB          binary large object (up to 16MB)
    LONGBLOB            binary large object (up to 4GB)

--------------------------------
#* Boolean Data Type:
--------------------------------
    BOOLEAN / BOOL      true or false (stored as 1 or 0)

--------------------------------
#* Spatial / Geometric Data Types:
--------------------------------
    GEOMETRY            general spatial data type
    POINT               a single coordinate (x, y)
    LINESTRING          a line of one or more points
    POLYGON             a polygon (area)
    MULTIPOINT          multiple points
    MULTILINESTRING     multiple lines
    MULTIPOLYGON        multiple polygons
    GEOMETRYCOLLECTION  collection of geometries

--------------------------------
#* JSON and XML Data Types:
--------------------------------
    JSON                stores JSON (JavaScript Object Notation) data
    XML                 stores XML data

--------------------------------
#* Miscellaneous / Special Data Types:
--------------------------------
    UUID / UNIQUEIDENTIFIER  universally unique identifier
    ARRAY               array of elements (PostgreSQL)
    HSTORE              key-value pairs (PostgreSQL)
    SERIAL / BIGSERIAL  auto-increment integer values
    MONEY / SMALLMONEY  currency or fixed-point money type
    BIT / BIT(n)        bit-field type (binary digits)
"""

"""SQLite Cheat Sheet
import sqlite3
===============================
#* Connecting & Setup
===============================
# Connect to a database (creates file if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Commit changes and close connection
conn.commit()
conn.close()

===============================
#* Inserting Data
===============================
# Insert a single record
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", 
               ('Alice', 30, 'alice@example.com'))

# Insert multiple records at once
cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", 
                   [('Bob', 25, 'bob@example.com'),
                    ('Charlie', 35, 'charlie@example.com')])

===============================
#* Querying Data
===============================
# Fetch all rows
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Fetch one row
cursor.execute("SELECT * FROM users WHERE name = ?", ('Alice',))
row = cursor.fetchone()

# Loop through results
for row in rows:
    print(row)

===============================
#* Updating Data
===============================
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'Alice'))

===============================
#* Deleting Data
===============================
cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))

===============================
#* Filtering & Sorting
===============================
# Filtering
cursor.execute("SELECT * FROM users WHERE age > ?", (30,))

# Sorting
cursor.execute("SELECT * FROM users ORDER BY age DESC")

# Limiting results
cursor.execute("SELECT * FROM users LIMIT 5")

===============================
#* Aggregate Functions
===============================
cursor.execute("SELECT COUNT(*) FROM users")
cursor.execute("SELECT AVG(age) FROM users")
cursor.execute("SELECT MAX(age), MIN(age) FROM users")

===============================
#* Transactions & Safety
===============================
# Use commit to save changes
conn.commit()

# Rollback changes if needed
conn.rollback()

# Using 'with' context for automatic commit/close
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", ('Diana',))

===============================
#* Misc / Utility
===============================
# Get column names
cursor.execute("SELECT * FROM users")
column_names = [description[0] for description in cursor.description]

# Check database version
cursor.execute("SELECT sqlite_version()")
print(cursor.fetchone())

# Closing connection
conn.close()

"""