from utils import *


def get_groups(user):
    header = ["group_id", "expense_id", "name"]

    table = get_table(
        f'''
        SELECT group_id, expense_id, group_name  
        FROM USER_HAS_GROUP_EXPENSE 
        NATURAL JOIN HAS_GROUP  
        WHERE user_id =  \'{user}\';
            ''', header)

    print_table(table, header)

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