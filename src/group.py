

def get_groups():
    header  = ["group_id", "expense_id", "name"]
    
    table = get_table(f'''
        SELECT group_id, expense_id, group_name  
        FROM USER_HAS_GROUP_EXPENSE 
        NATURAL JOIN HAS_GROUP  
        WHERE user_id =  '3xyaufSzzUp9LPkSKTxhqz';
            ''', header)

    print_table(table, header)
