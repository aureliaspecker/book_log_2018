# coding=utf-8
"""
This file logs books (title, author, date book was finished) and saves them to an external file
"""

import sys
from datetime import datetime
from easyIO import get_user_menu_selection

def main():
    opening_message()
    book_log = load_book_log("test.txt")
    option = display_main_menu()
    menu_action(option, book_log)


def opening_message():
    opening_message = "\n Welcome!"
    print(opening_message)

def load_book_log(x):
    file = open(x, "r")
    all_books = []
    book = {}
    for line in file:
        values = line.split(":")
        if values[0].rstrip() == "#start":
            book = {}
        elif values[0].rstrip() == "#end":
            all_books.append(book)
        else:
            book[values[0]] = values[1].rstrip()
    file.close()
    return all_books

def display_main_menu():
    menu = ["Add Book", "Remove Book", "View Books", "Exit"]
    option = get_user_menu_selection("Please select one of the following options", menu)
    return option

def menu_action(option, book_log):
    if option == 0:
        add_book()
    elif option == 1:
        remove_book()
    elif option == 2:
        view_books(book_log)
    elif option == 3:
        exit()
    else:
        sys.exit(1)

# def add_book():
#
#
#
# def remove_book():
#


def view_books(book_log):
    for book_number, book in enumerate(book_log):
        print("{})".format(book_number))
        for key, value in book.items():
            print("{}: {} \n".format(key, value))

# def exit():
#
#
#
#







if __name__ == "__main__":
    main()