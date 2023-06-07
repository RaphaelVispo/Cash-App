import shortuuid
import names
import mariadb
import sys
import pandas as pd

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="admin",
        host='localhost',
        port=3306,
        database="127project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# INSERT USER
for i in range(25):
    id = shortuuid.uuid()
    name = names.get_full_name()
    cur.execute(
    "INSERT INTO USER (user_id, user_name) VALUES (?, ?);", 
    (id, name))

# INSERT USER_FRIEND
# getting the ids
cur.execute('SELECT user_id FROM USER;')
rows = cur.fetchall()
df_user_id = pd.DataFrame(data=rows, columns=['user_id'])

import random
list_user_id = df_user_id.user_id
for user_id in list_user_id:
    l = list_user_id.tolist()
    l.remove(user_id) # removing the user 
    p = random.sample(l, 5) # gettignt the other users as friends

    for u in p: # inserting the new friends
        cur.execute(
        "INSERT INTO USER_FRIEND (user_id, friend) VALUES (?, ?);", 
        (user_id, u))


# INSERT HAS_GROUP, USER_HAS_GROUP_EXPENSE, EXPENSE 
# getting the ids
cur.execute('SELECT user_id FROM USER;')
rows = cur.fetchall()
df_user_id = pd.DataFrame(data=rows, columns=['user_id']).user_id.tolist()

from faker import Faker
import datetime
fake = Faker()
from mariadb.constants import *

groupno=1
for user_id in df_user_id:
    cur.execute("SELECT friend FROM USER_FRIEND where user_id= ? ;",(user_id,)) # getting the friends of the user
    rows = cur.fetchall()
    df_user_id = pd.DataFrame(data=rows, columns=['user_id']).user_id.tolist() # getting the list

    # random generating of group expsense
    x=random.randrange(1,10)
    for i in range(x):
        group_id = shortuuid.uuid()     
        
        samples  = random.randrange(1,5) # for getting the number of debtor 
        p = random.sample(df_user_id, samples) # getting the random debtors
          
        amount = random.randrange(100,1000)
        group_name ='Group {}'.format(groupno) #group no.
        groupno+=1
        
        # INSERT HAS_GROUP
        cur.execute("INSERT INTO HAS_GROUP VALUES (? , ? );", (group_id, group_name)) 

        # INSERT USER_HAS_GROUP_EXPENSE
        exp_date = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d')
        
        expense_id = shortuuid.uuid() # expense id of the creditor
        cur.execute("INSERT INTO USER_HAS_GROUP_EXPENSE VALUES (? , ? , ?);", (user_id, group_id, expense_id)) 
        cur.execute("INSERT INTO EXPENSE VALUES (?, ?, ?, ?, ?)", (expense_id, user_id, amount, 1,exp_date)) # inserting expense

        for debtor in p:
            expense_id = shortuuid.uuid() # expense id of the debtop
            cur.execute("INSERT INTO USER_HAS_GROUP_EXPENSE VALUES (? , ? , ?);", (debtor, group_id, expense_id)) 
            cur.execute("INSERT INTO EXPENSE VALUES (?, ?, ?, ?, ?)", (expense_id, user_id, amount, 0, exp_date)) 

conn.commit()