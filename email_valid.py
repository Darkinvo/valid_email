import re


def is_valid_email():
    username = input()
    patt = '^\D[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$'
    if (re.search(patt,username)):
        print("OK")
    else:
        print('WRONG')

is_valid_email()