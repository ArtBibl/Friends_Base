# D:\Dev\pyinstaller -F -i"D:\Dev\my.ico" Friends.py
import os
import sqlite3
from table_for_friends import *

con = sqlite3.connect('NewBase.db')


def del_char(name):
    ans = ''
    for letter in name:
        if letter == ':' or \
                letter == '[' or \
                letter == '(' or \
                letter == ')' or \
                letter == ']' or \
                letter == ',' or \
                letter == "'" or \
                letter == ";" or \
                letter == '"' or \
                letter == " ":
            continue
        else:
            ans += letter
    return ans


def show_friend(name):
    cur = con.cursor()
    request = "SELECT * FROM friends WHERE Name = '" + name + "'"
    cur.execute(request)
    rows = cur.fetchall()
    count = 0
    for row in rows:
        print("Name: ", row[1])
        print("Second name: ", row[2])
        print("Phone number: ", row[3])
        print("Age: ", row[0], "\n")
        count += 1
    if count == 0:
        print("\nWe can't find your friend in the database by name:", name, "\n")
    return count


def show_base():
    cur = con.cursor()
    request = "SELECT Name, Second_name, PhoneNumber, Age FROM friends"
    cur.execute(request)
    rows = cur.fetchall()
    head_main = ('Name:', 'Second name:', 'Phone number:', 'Age:')  # Head string !!!
    table_for_friends(rows, head_main)
    input("\nPlease press ENTER to return to the start menu!")


def create_line():
    val2 = True
    while val2:
        val3 = input("\nDo you need to create a new line? (y or n): ")
        if val3 == 'n':
            val2 = False
        if val3 == 'y':
            name = input("Name: ")
            second_name = input("Second name: ")
            age = input("Age: ")
            phone = input("Phone number: ")
            cur = con.cursor()
            request = "INSERT INTO friends (Name,Age,Second_name,PhoneNumber) " \
                      "VALUES ('" + name + "', " + age + ", '" + second_name + "', '" + phone + "')"
            cur.execute(request)
            con.commit()
            print("Records inserted successfully \n")
        else:
            print(" Please, select 'y' or 'n' \n")


def delete_line():
    val_del = True
    while val_del:
        name = input("\nPlease select a worst friend's name: ")
        if show_friend(del_char(name)) > 0:
            fired = input("\nAre you sure you want to delete your friend? Press 'y': ")
            if fired == 'y':
                cur = con.cursor()
                cur.execute("DELETE FROM friends WHERE Name = '" + name + "'")
                con.commit()
                print("Your friend", name, "has been deleted!\n")
        sm = input("\nDo you want to return to start menu? If no press 'n':")
        if sm != 'n':
            val_del = False


def searching():
    name = input("\nPlease select your friend's name: ")
    print('\n')
    friend_name = del_char(name)
    show_friend(friend_name)
    input("Please press ENTER to return to the start menu!")
    print('\n')


def edit():
    val_del = True
    while val_del:
        name = input("Please select a friend's name for changing: ")
        print('\n')
        if show_friend(del_char(name)) > 0:
            print()
            edit_fr = input("What item do you want to change?\nPress number of row (1,2,3..): ")
            print('\n')
            if edit_fr == '1':
                new_data = input("Enter new name: ")
                cur = con.cursor()
                cur.execute("UPDATE friends set Name = '" + del_char(new_data) +
                            "' where name = '" + del_char(name) + "'")
                con.commit()
            if edit_fr == '2':
                new_data = input("Enter new second name: ")
                cur = con.cursor()
                cur.execute("UPDATE friends set Second_name = '" + del_char(new_data) +
                            "' where name = '" + del_char(name) + "'")
                con.commit()
            if edit_fr == '3':
                new_data = input("Enter new phone number: ")
                cur = con.cursor()
                cur.execute("UPDATE friends set PhoneNumber = '" + del_char(new_data) +
                            "' where name = '" + del_char(name) + "'")
                con.commit()
            if edit_fr == '4':
                new_data = input("Enter new age: ")
                cur = con.cursor()
                cur.execute("UPDATE friends set Age = '" + del_char(new_data) +
                            "' where name = '" + del_char(name) + "'")
                con.commit()
            print("Your friend", name, "has been changed!\n")
        sm = input("Do you want to return to start menu? If no press 'n':")
        print('\n')
        if sm != 'n':
            val_del = False


def out():
    ex = (input("\nAre you sure? Press ENTER, if no 'n': "))
    if ex != 'n':
        os.system('cls')
        con.close()
        exit()
    else:
        pass


