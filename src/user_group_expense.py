
from group import *
from expense import *
from friends import *
from utils import *
from user import *

def add_user_group_expense(user):
    """
    add_user_group_expense
        add a group, and then pick the users' friends 
        to add expense

    params:
        user (str) - the user of the app
                   - creditor

    """
    # add group
    print_msg_box("Add User Group Expense")

    group_id = shortuuid.uuid()
    add_group(group_id)

    # add friend to the group
    user_ids = []

    friend_list = get_friends(user)
    l = len(friend_list.user_id)
    print(f"Type {l} to exit choice .. ")

    if friend_list.empty: # if the table is empty
        print("No friends yet ...")
        return
    
    # printing the friends with filters
    while True:
        c = choice(l+1)

        if c == l: # if the exit was picked
            if len(user_ids) == 0:
                print("Need atleast 1")
                continue
            else:
                break
        
        user_ids.append(friend_list.user_id[c])
        friend_list = friend_list.drop(c).reset_index(drop=True)
        l-=1
        print_table(friend_list.drop(columns='user_id', axis=1), ["Friends"])
        print(f"Type {l} to exit choice .. ")
    

    # for the creditor
    print_msg_box("Add expsense to friends")
    expense_id = shortuuid.uuid()

    print("Add expense to yourself as creditor")
    amount = int(input("Enter Amount: "))
    add_expense(expense_id, user, amount , 1)
    add_user_expense(user, group_id, expense_id)
    print("Assigned as the creditor Add expenses to group")
    
    # for the debtors
    for user_id in user_ids:
        expense_id = shortuuid.uuid()

        print("Add expense for: " )
        get_username(user_id)
        amount = int(input("Enter Amount: "))
        add_expense(expense_id, user, amount , 0)
        add_user_expense(user_id, group_id, expense_id)


def add_user_expense(user_id, group_id, expense_id):
    execute_query(f'''
    INSERT INTO USER_HAS_GROUP_EXPENSE VALUES (\'{user_id}\' , \'{group_id}\', \'{expense_id}\')
    ''');
    print("Add expenses to group")
    


def delete_user_group_expense(user):

    """
    delete_user_group_expense
        delete the group and all of the expense record 

    params:
        user (str) - the user of the app
                    - the group of the user will be picked

    """
    print_msg_box("Delete user group expense")
    table = get_groups(user)
    if table.empty:
        print("No groups yet ...")
        return

    c = choice(len(table.group_id))
    group_id = table.group_id[c]

    execute_query(f'''
        DELETE FROM EXPENSE WHERE  expense_id IN 
        (SELECT expense_id FROM USER_HAS_GROUP_EXPENSE 
        WHERE group_id = \'{group_id}\'); 
        '''
        );
    

    execute_query(f'''
        DELETE FROM USER_HAS_GROUP_EXPENSE 
        WHERE group_id = \'{group_id}\'; '''
        )
    execute_query(f'''
        DELETE FROM HAS_GROUP WHERE  group_id = "1";
        '''
    )
    print(f"Deleted group {table.name[c]} and all its expenses")


