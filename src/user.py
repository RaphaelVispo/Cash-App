from utils import *


def get_username(user):
    header = ["name"]

    table = get_table(
        f'''
        SELECT user_name FROM USER WHERE user_id =\'{user}\' ;
            ''', header)

    print_table(table, header, False)
