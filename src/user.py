from utils import *


def get_username(user):
    header = ["name"]

    table = get_table(
        f'''
        SELECT user_name FROM USER WHERE user_id =\'{user}\' ;
            ''', header)

    print_table(table, header, False)

def pick_user():
    print_msg_box("Choose user")
    header = ["user_id", "name"]
    table = get_table(
        "SELECT * FROM USER ORDER BY RAND() LIMIT 5;",
        header
    )

    clean_table = table.drop(columns='user_id', axis=1)
    header.remove("user_id")    
    print_table(clean_table, header)

    c=choice(5)

    get_username(table.user_id[c])
    return dict(table.loc[c])
 
