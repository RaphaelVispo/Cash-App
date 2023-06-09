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

def get_groups_with_outstanding_bal(user):
    
    header = ["User Name", "Group"]
    
    table = get_table (
        f'''
    SELECT u.user_name, g.group_name
        FROM USER u
        JOIN USER_HAS_GROUP_EXPENSE uge ON u.user_id = uge.user_id
        JOIN EXPENSE e ON uge.expense_id = e.expense_id
        JOIN HAS_GROUP g ON uge.group_id = g.group_id
        WHERE e.is_settled = 0
        AND u.user_id = \'{user}\';
        ''', header)
    if table.empty == False:
        print_table(table, header)
    else:
        print('No groups with outstanding balances')
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


def add_group(id):
    """
    add_group
        Will ask for the new name of the group
        and will print the new group in the data

    params:
        id (shortuuid)- id of the group
    """
    print_msg_box("Add group")

    name = input("Name of the new group: ")

    execute_query(f'''
        INSERT INTO HAS_GROUP 
            VALUES (\'{id}\', \'{name}\') ;
                ''')
    print("Added new group:")
    get_group_name(id)


def edit_group(user):
    """
    edit_group
        Will ask for the new name of the group
        and will print the new group in the data
    
    params:
        user: will get the users groups

    """
    print_msg_box("Edit group")
    table = get_groups(user)

    c = choice(len(table.group_id))
    new_name = input("New group name: ")

    execute_query(f'''
        UPDATE HAS_GROUP SET group_name = \'{new_name}\'
            WHERE group_id= \'{table.group_id[c]}\' ;
            ''')

    print("Edited the name of the group:")
    get_group_name(table.group_id[c])


def delete_group(id, name):
    """
    delete_group
        will delete group from the id

    params:
        id - id of the group that will be deleted
        name - name of the group

    """
    execute_query(f'''
    DELETE FROM HAS_GROUP WHERE group_id = \'{id}\'
            ''')
    print(f"Deleted the group: {group}")

