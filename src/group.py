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
