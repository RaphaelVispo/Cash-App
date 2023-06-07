"""
This file will be the main flow of the program
"""

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="AXOYu0mzs8vWyMGTBPLl",
        host='containers-us-west-16.railway.app',
        port=5604,
        database="railway"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()