"""
This is the file that will have all of the functions for friends


"""

def get_friends():
    header  = ["Friends"]
    
    table = get_table(f'''
        SELECT u.user_name
            FROM USER_FRIEND f
            JOIN USER u ON u.user_id=f.friend
            WHERE f.user_id=\'{user}\' ;
            ''', header)

    print_table(table, header)