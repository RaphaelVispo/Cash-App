import termtables as tt
import numpy
import sys
import pandas as pd
import mariadb
import os
from dotenv import load_dotenv

load_dotenv() 

# Connect to MariaDB Platform
try:

    conn = mariadb.connect(
        user=os.getenv("USERNAMEDB", default=None),
        password=os.getenv("PASSWORDDB", default=None),
        host=os.getenv("HOSTDB", default=None),
        port=int(os.getenv("PORTDB", default=None)),
        database=os.getenv("DATABASE", default=None)

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

def print_table(data, header, is_indexed = True):
    tt.print(
        list(data.itertuples(index=is_indexed)),
        header=["Index"]+ header if is_indexed else header,
        padding=(0, 2)
    )  

def get_table(query, cols):

    try:
        cur.execute(query)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    rows = cur.fetchall()
    df_tables = pd.DataFrame(data=rows, columns=cols)
    return df_tables