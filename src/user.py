from utils import *

user = "3xyaufSzzUp9LPkSKTxhqz"


def get_username():
    header = ["name"]

    table = get_table(
        f'''
        SELECT user_name FROM USER WHERE user_id =\'{user}\' ;
            ''', header)

    print_table(table, header)
