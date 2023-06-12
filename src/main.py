"""
This file will be the main flow of the program
"""
from expense import *
from group import *
from user import *
from friends import *

picked = pick_user()
user = picked["user_id"]
name = picked["name"]
print(f"user_id: {user} , name: {name}" )

get_unpaid_expenses(user)
get_paid_expenses(user)
get_total_paid_expenses(user)
get_total_unpaid_expenses(user)
get_total_expenses(user)
get_friends(user)
get_username(user)
get_groups(user)


def add_Menu():
    global efg_Choice
    while True:
        try:
            print("[1] GROUP EXPENSE")
            print("[2] FRIEND")
            print("[3] EXPENSE TO A GROUP\n")

            efg_Choice = int(input("Your choice: "))
            if efg_Choice > 0 and efg_Choice < 4:
                return efg_Choice
                break;
            else:
                print("Invalid entry. Please try again.\n")
        except:
            print("Invalid entry. Please try again.\n")
            continue


def delete_Menu():
    global efg_Choice
    while True:
        try:
            print("[1] GROUP EXPENSE")
            print("[2] FRIEND")
            print("[3] FRIEND FROM A GROUP\n")

            efg_Choice = int(input("Your choice: "))
            if efg_Choice > 0 and efg_Choice < 4:
                return efg_Choice
                break;
            else:
                print("Invalid entry. Please try again.\n")
        except:
            print("Invalid entry. Please try again.\n")
            continue
        
            
def search_Update_Menu():
    global efg_Choice
    while True:
        try:
            print("[1] EXPENSE")
            print("[2] FRIEND")
            print("[3] GROUP\n")

            efg_Choice = int(input("Your choice: "))
            if efg_Choice > 0 and efg_Choice < 4:
                return efg_Choice
                break;
            else:
                print("Invalid entry. Please try again.\n")
        except:
            print("Invalid entry. Please try again.\n")
            continue
        

def choose_View():
    global view_Choice
    while True:
        try:
            print("What would you like to view?")
            print("[1] ALL EXPENSES MADE WITH WITHIN A MONTH")
            print("[2] ALL EXPENSES MADE WITH A FRIEND")
            print("[3] ALL EXPENSES MADE WITH A GROUP")
            print("[4] CURRENT BALANCE FROM ALL EXPENSES")
            print("[5] ALL FRIENDS WITH OUTSTANDING BALANCE")
            print("[6] ALL GROUPS")
            print("[7] ALL GROUPS WITH OUTSTANDING BALANCE\n")

            view_Choice = int(input("Your choice: "))
            if view_Choice > 0 and view_Choice < 8:
                return view_Choice
                break;
            else:
                print("Invalid entry. Please try again.\n")
        except:
            print("Invalid entry. Please try again.\n")
            continue


def main_Menu():
    global action
    while True:
        try:
            print("What would you like to do?")
            print("[1] ADD")
            print("[2] DELETE")
            print("[3] SEARCH")
            print("[4] UPDATE")
            print("[5] VIEW")
            print("[0] EXIT CASH-APP\n")
            action = int(input("Your choice: "))
        
            if action >= 0 and action <= 5:
                return action
                break;
            else:
                print("Invalid entry. Please try again.\n")
        except:
            print("Invalid entry. Please try again.\n")
            continue


## instead of print, lagay yung function for it
def action_Run():
    if action == 1:
        print("What would you like to add?\n")
        add_Menu()
        #choose_Efg()
        if efg_Choice == 1:
            add_user_group_expense(user):
        elif efg_Choice == 2:
            add_friend(user)
        elif efg_Choice == 3:
            add_user_expense(user_id, group_id, expense_id)
    
    elif action == 2:
        print("What would you like to delete?\n")
        delete_Menu()
        if efg_Choice == 1:
            delete_user_group_expense(user):
        elif efg_Choice == 2:
            delete_friend(user)
        elif efg_Choice == 3:
            print("delete friend from a group")
    
    elif action == 3:
        print("What would you like to search?\n")
        search_Update_Menu()
        if efg_Choice == 1:
            print("search expense")
        elif efg_Choice == 2:
            search_friend(user)
        elif efg_Choice == 3:
            search_group(user)
    
    elif action == 4:
        print("What would you like to update?\n")
        search_Update_Menu()
        if efg_Choice == 1:
            print("update expense")
        elif efg_Choice == 2:
            edit_friend(user)
        elif efg_Choice == 3:
            edit_group(user)
    
    elif action == 5:
        choose_View()
        if view_Choice == 1:
            get_expenses_in_a_month(user)
        elif view_Choice == 2:
             get_expenses_with_a_friend(user)
        elif view_Choice == 3:
            get_expenses_with_a_group(user)
        elif view_Choice == 4:
            get_total_unpaid_expenses(user)
        elif view_Choice == 5:
            get_friends_with_outstanding_bal(user)
        elif view_Choice == 6:
            print("all groups")
        elif view_Choice == 7:
            print("group balance")
        
    elif action == 0:
        print("You have exited Cash-App.")
        
        
print_msg_box(f"Welcome to Cash-App {name}!\n", indent=10)        
main_Menu() 
action_Run()
while True:
    if action != 0:
        print("\n----------------------------------------------------")
        main_Menu()
        action_Run()
    else:
        break
