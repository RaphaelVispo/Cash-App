"""
This file will be the main flow of the program
"""
from expense import *
from group import *
from user import *
from friends import *

user = "3xyaufSzzUp9LPkSKTxhqz"

get_unpaid_expenses(user)
get_paid_expenses(user)
get_total_paid_expenses(user)
get_total_unpaid_expenses(user)
get_total_expenses(user)
get_friends(user)
get_username(user)
get_groups(user)

def chooseEfg():
  # pili what to add delete search update(EXPENSE, FRIEND, GROUP)
  
  while True:
    try:
      print("[1] EXPENSE")
      print("[2] FRIEND")
      print("[3] GROUP")
  
      efgChoice = input(print("Your choice: "))
      if efgChoice > 0 and efgChoice < 4:
         #print("")
          break;
      else:
      print("Invalid entry. Please try again.")
    except:
      continue

# then gamitin efgChoice for...
      
def addExpense():
  
  
  
  
def addFriend():
  
  
  

def addGroup():
  
  
  
  
def deleteExpense():
  
  
  
  
def deleteFriend():
  
  
  

def deleteGroup():
  
  
  
  
def searchExpense():
  
  
  
  
def searchFriend():
  
  
  

def searchGroup():

  

  
def updateExpense():
  
  
  
  
def updateFriend():
  
  
  

def updateGroup():  
  
  
  
def chooseView():
  while True:
    try:
      print("What would you like to view?")
      print("[1] ALL EXPENSES MADE WITH WITHIN A MONTH")
      print("[2] ALL EXPENSES MADE WITH A FRIEND")
      print("[3] ALL EXPENSES MADE WITH A GROUP")
      print("[4] CURRENT BALANCE FROM ALL EXPENSES")
      print("[5] ALL FRIENDS WITH OUTSTANDING BALANCE")
      print("[6] ALL GROUPS")
      print("[7] ALL GROUPS WITH OUTSTANDING BALANCE
      #print("What would you like to view?")
            
      viewChoice = input(print("Your choice: "))
      if viewChoice > 0 and viewChoice < 8:
         #print("")
          break;
      else:
      print("Invalid entry. Please try again.")
    except:
      continue  
            
def viewExpensesMonth():
  
  
  
  
def viewExpensesFriend():
  
  
  
  
def viewExpensesGroup():
  
  
  

def viewCurrentBalance():

  

  
def viewFriendsOutstanding():
  
  
  
  
def viewGroups():
  
  
  

def viewGroupsOutstanding():             

            
            
          

# will clean up/ make functions laterrr

## WELCOME SCREEN ##

while True:
  try:
    #print("Welcome to Cash-App kineme")
    print("[1] ADD")
    print("[2] DELETE")
    print("[3] SEARCH")
    print("[4] UPDATE")
    print("[5] VIEW")
    print("[0] EXIT CASH-APP")

    action = input("What would you like to do?")
    if action >= 0 and action <= 5:
      #print("")
      break;
    else:
      print("Invalid entry. Please try again.")
  except:
      continue

if action == 1:
  print("What would you like to add?")
  chooseEfg()
    
elif action == 2:
  print("What would you like to delete?")
  chooseEfg()
  
elif action == 3:
  print("What would you like to search?")
  chooseEfg()
  
elif action == 4:
  print("What would you like to update?")
  chooseEfg() 
  
elif action == 5:
  chooseView()
  
elif action == 0:
  # byebye ty for using cash app

  












