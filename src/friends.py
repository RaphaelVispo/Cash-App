"""
This is the file that will have all of the functions for friends


"""
from utils import *
from user import *

user = "3xyaufSzzUp9LPkSKTxhqz"


def get_friends(user):
    header = ["Friends", "user_id"]

    table = get_table(
        f'''
        SELECT u.user_name, u.user_id
            FROM USER_FRIEND f
            JOIN USER u ON u.user_id=f.friend
            WHERE f.user_id=\'{user}\' ;
            ''', header)

    # removing the user_id column for printing the table
    clean_table = table.drop(columns='user_id', axis=1)
    header.remove("user_id")
    print_table(clean_table, header)

    return table


def choice(upper):
    while True:
        choice = int(input("Choice: "))

        if choice >= 0 and choice < upper:
            return choice

        print("Invalid choice")




def search_one_friend(user):

    friend_list = get_friends(user)
    c = choice(len(friend_list))

    get_username(friend_list.user_id[c])



def edit_one_friend(user):

    friend_list = get_friends(user)
    c = choice(len(friend_list))

    get_username(friend_list.user_id[c])

    new_name = input("New name: ")

    execute_query(
        f'''
        UPDATE USER SET user_name = \'{new_name}\'
            WHERE user_id= \'{friend_list.user_id[c]}\' ;
            ''')

    get_username(friend_list.user_id[c])

def delete_one_friend(user):
    pass


# search_one_friend(user)
edit_one_friend(user)
