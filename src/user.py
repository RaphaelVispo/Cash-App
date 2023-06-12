from utils import *


def get_username(user):
    """
    get username 
        prints the table of the given user_id

    params:
        user - user_id that will be searched

    """
    header = ["name"]

    table = get_table(
        f'''
        SELECT user_name FROM USER WHERE user_id =\'{user}\' ;
            ''', header)

    print_table(table, header, False)

def pick_user():
    """
    pick_user
        let the person whose usign the app to  pick the user
        with the randomized

    return: 
        dict:
            user_id - user userid of the user picked
            name - the name of the picked user
    """
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
 
