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

    conn = mariadb.connect(user=os.getenv("USERNAMEDB", default=None),
                           password=os.getenv("PASSWORDDB", default=None),
                           host=os.getenv("HOSTDB", default=None),
                           port=int(os.getenv("PORTDB", default=None)),
                           database=os.getenv("DATABASE", default=None))
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


def print_table(data, header, is_indexed=True):
    """
    print_table
        will format a table to the pretty version format
    
    params
        data (Dataframe) - the dataframe that will be dispplayed
        header (list) -  the header of the dataframe, 
            this could be any as long as the column matches the dataframe
        is_indexed (optional) - will show index if toggled true


    """
    tt.print(list(data.itertuples(index=is_indexed)),
             header=["Index"] + header if is_indexed else header,
             padding=(0, 2))


def get_table(query, cols):

    """
    get_table
        will from query from the table and put it in a table
    
    return:
        df_tables (Dataframe) - The table from the query

    """
    try:
        cur.execute(query)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    rows = cur.fetchall()
    df_tables = pd.DataFrame(data=rows, columns=cols)
    return df_tables


def execute_query(query):
    """
    execute_query
        used in INSERT, DELETE and UPDATE. all of the queries without a table to be output

    params:
        query(str) - the string to be queried 
    """
    try:
        cur.execute(query)
        conn.commit()
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


def print_msg_box(msg, indent=20, width=None, title=None):
    """
    print_msg_box
        prints the banner from the message
    
    params:
        msg (str) - string to be displayed in the banner
    """
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)


def choice(upper):
    """
    choice 
        gets the user's input if the condition is true, else 
        it will loop over until the user provide the correct choice

    params:
        upper - the upper limit of the choice
    
    return:
        choice - the choice of the user

    """
    while True:
        choice = int(input("Choice: "))

        if choice >= 0 and choice < upper:
            return choice

        print("Invalid choice")
