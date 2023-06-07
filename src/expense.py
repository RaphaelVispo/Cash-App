from utils import *

user = "3xyaufSzzUp9LPkSKTxhqz"


def get_unpaid_expenses():
    
    header  = [ "Group_name", "Amount" , "Creditor Name ","Date"]
    
    table = get_table(f'''
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


def get_paid_expenses():
    
    header  = [ "Group_name", "Amount" , "Creditor Name ","Date"]
    
    table = get_table(f'''
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


def get_total_paid_expenses():
    
    header  = ["Total"]
    
    table = get_table(f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' AND e.is_settled=1;

            ''', header)

    print_table(table, header, False)



def get_total_unpaid_expenses():
    
    header  = ["Total"]
    
    table = get_table(f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' AND e.is_settled=0;

            ''', header)

    print_table(table, header, False)

def get_total_expenses():
    
    header  = ["Total"]
    
    table = get_table(f'''
    SELECT SUM(amount) total
        FROM USER_HAS_GROUP_EXPENSE a 
        NATURAL JOIN HAS_GROUP 
        NATURAL JOIN  EXPENSE e 
        JOIN USER u ON e.creditor=u.user_id 
        WHERE a.user_id =  \'{user}\' 

            ''', header)

    print_table(table, header, False)