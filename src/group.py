from utils import *
import shortuuid

def get_groups(user):
    header = ["group_id", "expense_id", "name"]

    table = get_table(
        f'''
        SELECT group_id, expense_id, group_name  
        FROM USER_HAS_GROUP_EXPENSE 
        NATURAL JOIN HAS_GROUP  
        WHERE user_id =  \'{user}\';
            ''', header)

    clean_table = table.drop(columns=['group_id', 'expense_id'], axis=1)
    header.remove('group_id')
    header.remove('expense_id')
    print_table(clean_table, header)

    return table


def get_group_name(group):
    header = ["group_name"]
    table = get_table(
        f'''
        SELECT group_name FROM HAS_GROUP WHERE group_id =\'{group}\' ;
            ''', header)
    print_table(table, header, False)


def search_group(user):
    """
    search_group
        picking the user group from the choice of a user

    params:
        user - the user that it will get the friends

    """
    print_msg_box("Search Group")

    group_list = get_groups(user)
    c = choice(len(group_list))

    get_group_name(group_list.group_id[c])


def add_group():
    """
    add_group
        Will ask for the new name of the group
        and will print the new group in the data

    """
    print_msg_box("Add group")
    id = shortuuid.uuid()
    name = input("Name of the new group: ")

    execute_query(f'''
        INSERT INTO HAS_GROUP 
            VALUES (\'{id}\', \'{name}\') ;
                ''')
    print("Added new group:")
    get_group_name(id)


def edit_group():
    pass


def delete_group():
    pass


# search_group('3xyaufSzzUp9LPkSKTxhqz')

add_group('3xyaufSzzUp9LPkSKTxhqz')
