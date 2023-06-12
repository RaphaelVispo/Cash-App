from utils import *
from friends import *
from group import *
import shortuuid


def get_unpaid_expenses(user):

    header = ["Group_name", "Amount", "Creditor Name ", "Date"]

    table = get_table(
        f'''
    SELECT group_name, CONCAT("P ", amount) ,u.user_name creditor_name ,  CASE
        WHEN DATEDIFF(CURDATE(),  e.expense_date )<10 THEN DATE_FORMAT( expense_date, '%W, %M %d %Y')
        ELSE DATE_FORMAT( expense_date, '%M %Y') END AS Date
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id = \'{user}\' AND e.is_settled=0
        ORDER BY DATEDIFF(e.expense_date, CURDATE()) DESC;
            ''', header)

    print_table(table, header)


def get_paid_expenses(user):

    header = ["Group_name", "Amount", "Creditor Name ", "Date"]

    table = get_table(
        f'''
    SELECT group_name, CONCAT("P ", amount) ,u.user_name creditor_name ,  CASE
        WHEN DATEDIFF(CURDATE(),  e.expense_date )<10 THEN DATE_FORMAT( expense_date, '%W, %M %d %Y')
        ELSE DATE_FORMAT( expense_date, '%M %Y') END AS Date
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id = \'{user}\' AND e.is_settled=1
        ORDER BY DATEDIFF(e.expense_date, CURDATE()) DESC;
            ''', header)

    print_table(table, header)


def get_total_paid_expenses(user):

    header = ["Total"]
    

    table = get_table(
        f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' AND e.is_settled=1;

            ''', header)

    print_table(table, header, False)


def get_total_unpaid_expenses(user):
    
    get_unpaid_expenses(user)

    header = ["Total"]

    table = get_table(
        f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' AND e.is_settled=0;

            ''', header)

    print_table(table, header, False)


def get_total_expenses(user):

    header = ["Total"]

    table = get_table(
        f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' 

            ''', header)

    print_table(table, header, False)
    
    
def get_expenses_in_a_month(user):
    header = ["Group Name", "Date", "Amount", "Settled?"]
    
    print_msg_box("Get expense in a month")
    print_msg_box("Choose a month", indent=10)
    month_table = [("January"), ("February"), ("March"), ("April"), ("May"), 
                    ("June"), ("July"), ("August"), ("September"), ("October"), ("November"), ("December")]
    print_table(pd.DataFrame(month_table), ["Month"])
    c=choice(11)

    month = month_table[c]
    
    print(f"Picked month: {month}")
    table = get_table(
        f'''
    select group_name, expense_date, amount, case when is_settled = 0 then 'No' else 'Yes' end 
        from USER_HAS_GROUP_EXPENSE a natural join HAS_GROUP natural join EXPENSE e join USER
        u on e.creditor = u.user_id where MONTHNAME(expense_date) = \'{month}\' and a.user_id = \'{user}\';
            ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses for this month')
        

def get_expenses_with_a_friend(user):
    
    print_msg_box("Select a friend")
    
    friend_list = get_friends(user)
    
    c = choice(len(friend_list))
    
    header = ["User Name", "Date", "Amount", "Group Name", "Friend"]
    
    table = get_table (
        f'''
    SELECT a.user_name, e.expense_date, e.amount, group_name, c.user_name as friend FROM USER a 
    JOIN USER_FRIEND b ON a.user_id = b.user_id 
    JOIN USER c ON b.friend = c.user_id 
    JOIN USER_HAS_GROUP_EXPENSE d on a.user_id = d.user_id 
    natural join HAS_GROUP 
    natural join EXPENSE e where c.user_id= \'{friend_list.user_id[c]}\' and a.user_id = \'{user}\' order by e.expense_date desc;
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses for this friend')
        
        
def get_expenses_with_a_group(user):
    
    print_msg_box("Select a group")
    
    group_list = get_groups(user)
    c = choice(len(group_list))
    
    header = ["User Name", "Date", "Amount", "Group Name", "Friend", "Friend Amount"]
    
    table = get_table (
        f'''
    SELECT a.user_name, e.expense_date, e.amount, group_name, c.user_name, x.amount as friend FROM USER a 
    JOIN USER_FRIEND b ON a.user_id = b.user_id 
    JOIN USER c ON b.friend = c.user_id 
    JOIN USER_HAS_GROUP_EXPENSE d on a.user_id = d.user_id 
    natural join HAS_GROUP 
    natural join EXPENSE e
    join USER_HAS_GROUP_EXPENSE f on c.user_id = f.user_id
    join EXPENSE x on f.expense_id = x.expense_id where group_id = \'{group_list.group_id[c]}\' and a.user_id = \'{user}\'order by e.expense_date desc;
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses yet for this group')
        
def get_expenses_with_a_group_input(user,group):
    
    header = ["User Name", "Date", "Amount", "Group Name", "Friend"]
    
    table = get_table (
        f'''
    SELECT a.user_name, e.expense_date, e.amount, group_name, c.user_name as friend FROM USER a 
    JOIN USER_FRIEND b ON a.user_id = b.user_id 
    JOIN USER c ON b.friend = c.user_id 
    JOIN USER_HAS_GROUP_EXPENSE d on a.user_id = d.user_id 
    natural join HAS_GROUP 
    natural join EXPENSE e 
    where group_id = \'{group}\' and a.user_id = \'{user}\'order by e.expense_date desc;
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses for this group')
        
def get_friends_with_outstanding_bal(user):
    
    header = ["User Name", "Friend"]
    
    table = get_table (
        f'''
    SELECT distinct u.user_name AS user_name, f.user_name AS friend_name
        FROM USER u
        JOIN USER_FRIEND uf ON u.user_id = uf.user_id
        JOIN USER f ON uf.friend = f.user_id
        JOIN USER_HAS_GROUP_EXPENSE uge ON u.user_id = uge.user_id
        JOIN EXPENSE e ON uge.expense_id = e.expense_id
        WHERE e.is_settled = 0 and u.user_id = \'{user}\';
        ''', header)
    if table.empty == False:
        print_table(table, header)
    else:
        print('No friends with outstanding balances')
        
def search_expense(user):
    header = ["Group Name", "Date", "Amount", "Settled?"]
    
    expense_list = get_expense(user)
    select = choice(len(expense_list.expense_id))
    
    table = get_table (
        f'''
    select group_name, expense_date, amount, case when is_settled = 0 then 'No' else 'Yes' end from USER_HAS_GROUP_EXPENSE a 
    natural join HAS_GROUP 
    natural join EXPENSE e 
    join USER u on e.creditor = u.user_id and expense_id = \'{expense_list.expense_id[select]}\' and a.user_id = \'{user}\';
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('Error! Expense not found!')
        
        
def get_expense(user):
    header = ["Group Name", "expense_id", "Date", "Amount", "Settled?"]
    print_msg_box("Edit Expense")
    
    table = get_table(
        f'''
        select group_name, expense_id, expense_date, amount, case when is_settled = 0 then 'No' else 'Yes' end from USER_HAS_GROUP_EXPENSE a 
    natural join HAS_GROUP 
    natural join EXPENSE e 
    join USER u on e.creditor = u.user_id and a.user_id = \'{user}\';
    ''', header
    )
    print_table(table,header)
    
    return table

def edit_expense (user):
    
    expense_list = get_expense(user);
    select = choice(len(expense_list.expense_id))
    
    print("0: edit amount | 1: edit status")
    
    edit_type = choice(2)
    
    if edit_type == 0:
        new_amount = input("New amount: ")

        execute_query(f'''
            update EXPENSE set amount = {new_amount} where expense_id = \'{expense_list.expense_id[select]}\';
                ''')

        print("Successfully edited the amount!")
        search_expense(user, expense_list.expense_id[select])
        
        
    elif edit_type == 1:
        new_status = choice(2)

        execute_query(f'''
            update EXPENSE set is_settled = {new_status} where expense_id = \'{expense_list.expense_id[select]}\';
                ''')
        print("Successfully edited the status!")
        search_expense(user, expense_list.expense_id[select])
        
def delete_expense(expense):
        """
        delete_group
            will delete expense from given id

        params:
            id - id of the group that will be deleted

        """
        execute_query(f'''
        delete from EXPENSE where expense_id = \'{expense}\';
                ''')
        print("Deleted the expense!")
        
def add_expense(id, creditor, amount, settled):

    execute_query(f'''
        INSERT INTO EXPENSE
            VALUES (\'{id}\', \'{creditor}\',{amount},{settled},CURDATE()) ;
                ''')
    print("Added new expense")  
    
def delete_expense_choice(user):
    """
    delete_group
        will delete expense from given id

    params:
        id - id of the group that will be deleted

    """
    expense_list = get_expense(user);
    select = choice(len(expense_list.expense_id))
    
    execute_query(f'''
    delete from EXPENSE where expense_id = \'{expense_list.expense_id[select]}\';
            ''')
    
    execute_query(f'''
    delete from USER_HAS_GROUP_EXPENSE where expense_id = \'{expense_list.expense_id[select]}\';
            ''')
    
    print("Deleted the expense!")
    get_expense(user)
    
def add_expense_choice(user):
    
    group_list = get_groups(user)
    
    groupChoice = choice(len(group_list.group_id))
    
    get_expenses_with_a_group_input(user, group_list.group_id[groupChoice])
    new_id = shortuuid.uuid()
    
    settled = input ("Settled? 0: No | 1: Yes ")
    amount = input ("Amount: ")
    
    # get_friends(user)

    execute_query(f'''
        INSERT INTO EXPENSE
            VALUES (\'{new_id}\', \'{user}\',{amount},{settled},CURDATE()) ;
                ''')
    
    execute_query(f'''
        INSERT INTO USER_HAS_GROUP_EXPENSE
            VALUES (\'{user}\', \'{ group_list.group_id[groupChoice]}\',\'{new_id}\') ;
                ''')
    
    print("Added new expense")  
    
    