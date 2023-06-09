from utils import *


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
    
    
def get_expenses_in_a_month(user,month):
    header = ["Group Name", "Date", "Amount", "Settled?"]
    table = get_table(
        f'''
    select group_name, expense_date, amount, case when is_settled = 0 then 'No' else 'Yes' end from USER_HAS_GROUP_EXPENSE a natural join HAS_GROUP natural join EXPENSE e join USER
        u on e.creditor = u.user_id where MONTHNAME(expense_date) = \'{month}\' and a.user_id = \'{user}\';
            ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses for this month')
        

def get_expenses_with_a_friend(user, friend):
    
    header = ["User Name", "Date", "Amount", "Group Name", "Friend"]
    
    table = get_table (
        f'''
    SELECT a.user_name, e.expense_date, e.amount, group_name, c.user_name as friend FROM USER a 
    JOIN USER_FRIEND b ON a.user_id = b.user_id 
    JOIN USER c ON b.friend = c.user_id 
    JOIN USER_HAS_GROUP_EXPENSE d on a.user_id = d.user_id 
    natural join HAS_GROUP 
    natural join EXPENSE e where c.user_name = \'{friend}\' and a.user_id = \'{user}\' order by e.expense_date desc;
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('No expenses for this friend')
        
        
def get_expenses_with_a_group(user, group):
    
    header = ["User Name", "Date", "Amount", "Group Name", "Friend"]
    
    table = get_table (
        f'''
    SELECT a.user_name, e.expense_date, e.amount, group_name, c.user_name as friend FROM USER a 
    JOIN USER_FRIEND b ON a.user_id = b.user_id 
    JOIN USER c ON b.friend = c.user_id 
    JOIN USER_HAS_GROUP_EXPENSE d on a.user_id = d.user_id 
    natural join HAS_GROUP 
    natural join EXPENSE e where group_name = \'{group}\' and a.user_id = \'{user}\'order by e.expense_date desc;
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
        
def search_expense(user, expense):
    header = ["Group Name", "Date", "Amount", "Settled?"]
    
    table = get_table (
        f'''
    select group_name, expense_date, amount, case when is_settled = 0 then 'No' else 'Yes' end from USER_HAS_GROUP_EXPENSE a 
    natural join HAS_GROUP 
    natural join EXPENSE e 
    join USER u on e.creditor = u.user_id and expense_id = \'{expense}\' and a.user_id = \'{user}\';
        ''', header)
    
    if table.empty == False:
        print_table(table, header)
    else:
        print('Error! Expense not found!')
        
def edit_expense (expense):
    run_edit(f'''update EXPENSE set amount = 995 where expense_id = \'{expense}\';''')

def delete_expense(expense):
    run_delete(f'''delete from EXPENSE where expense_id = \'{expense}\';''')
    
def add_expense(id, creditor, amount, settled, date):
    """
    add_expense
        Will ask for the new name of the group
        and will print the new group in the data

    params:
        id (shortuuid)- id of the group
    """
    print_msg_box("Add group")

    name = input("Name of the new group: ")

    new_expense_id = shortuuid.uuid()
    
    execute_query(f'''
        INSERT INTO EXPENSE
            VALUES (\'{new_expense_id}\', \'{creditor}\',\'{amount}\',\'{settled}\',\'{name}\') ;
                ''')
    print("Added new expense:")  