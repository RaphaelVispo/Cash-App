import termtables as tt
import numpy
import sys
import pandas as pd

def print_table(data, header):
    tt.print(
        list(data.itertuples()),
        header=["Index"]+ header,
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