"""
This is the file that will have all of the functions for friends


"""
from utils import *
from user import *


def get_friends(user):
    """
    get_friends
        gets the friend of the given user and prints the table
        of the friends with index

    params:
        user - the user that it will get the friends
    
    return:
        table - pandas full table of user name  and user id
            of the friends 

    """
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


def search_friend(user):
    """
    search_friend
        picking the user friend from the choice of a user

    params:
        user - the user that it will get the friends

    """
    print_msg_box("Search Friend")

    friend_list = get_friends(user)
    c = choice(len(friend_list))

    get_username(friend_list.user_id[c])


def edit_friend(user):
    """
    edit_friend
        will change the name of the friend 

    params:
        user - the user that it will get the friends

    """

    print_msg_box("Edit Friend")
    friend_list = get_friends(user)
    c = choice(len(friend_list))

    get_username(friend_list.user_id[c])

    new_name = input("New name: ")

    execute_query(f'''
        UPDATE USER SET user_name = \'{new_name}\'
            WHERE user_id= \'{friend_list.user_id[c]}\' ;
            ''')

    get_username(friend_list.user_id[c])


def delete_friend(user):
    """
    edit_friend
        will delete a friend from the friend list of the user
        and vice versa

    params:
        user - the user that it will get the friends

    """

    print_msg_box("Delete Friend")

    friend_list = get_friends(user)
    c = choice(len(friend_list))

    friend = friend_list.user_id[c]

    # deleting the user friend and vice versa
    execute_query(f'''
    DELETE FROM USER_FRIEND WHERE user_id = \'{user}\'
        AND friend= \'{friend}\' ;
        ''')
    print(f"Deleting {friend_list.Friends[c]} as friend ... ")
    execute_query(f'''
    DELETE FROM USER_FRIEND WHERE user_id = \'{friend}\'
        AND friend= \'{user}\' ;
        ''')

    get_friends(user)
    print(f"Friend deleted: {table.Name[c]}")


def add_friend(user):
    """
    edit_friend
        will add a friend from the friend list of the user
        and vice versa

    params:
        user - the user that it will get the friends

    """
    print_msg_box("Add Friend")


    header = ["user_id", "Name"]

    # getting the non-friend of the user limit = 5
    table = get_table(
        f'''
        SELECT * FROM USER 
            WHERE user_id NOT IN (
                SELECT friend FROM USER_FRIEND 
                WHERE user_id = \'{user}\' 
            )
            ORDER BY RAND()
            LIMIT 5;
        ''', header)

    clean_table = table.drop(columns='user_id', axis=1)
    header.remove("user_id")
    print_table(clean_table, header)

    c = choice(len(table))

    # adding the user for both user ad friends
    friend = table.user_id[c]

    execute_query(f'''
    INSERT INTO  USER_FRIEND 
        VALUES (\'{user}\', \'{friend}\') ;
        ''')
    print(f"Deleting {table.Name[c]} as friend ... ")
    execute_query(f'''
    INSERT INTO  USER_FRIEND 
        VALUES (\'{friend}\', \'{user}\') ;
        ''')
    get_friends(user)
    print(f"Friend added {table.Name[c]}")
