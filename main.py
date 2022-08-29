from Friends import *
from neo import *
import os
import time

if __name__ == '__main__':
    matrix()
    while True:
        os.system('cls')
        print("\nWelcome to the friend base! \n ")
        print("1. Show full database")
        print("2. Create a new line")
        print("3. Deleting a friend")
        print("4. Searching by name")
        print("5. Edit your friend's information")
        print("0. Exit! \n ")
        val = input("Choice action with your database (1, 2, 3, 4, 5 or 0): ")
        print('\n')
        if val == '1':
            show_base()
        elif val == '2':
            create_line()
        elif val == '3':
            delete_line()
        elif val == '4':
            searching()
        elif val == '5':
            edit()
        elif val == '0':
            out()
        else:
            os.system('cls')
            print("\n Only 1, 2, 3, 4, 5 or 0. Please, write correct choice!")
            time.sleep(2)
