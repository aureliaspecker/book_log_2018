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
    # menu_action(option)


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
    print(all_books)
    file.close()
    return

def display_main_menu():
    menu = ["Add Book", "Remove Book", "View Books", "Exit"]
    option = get_user_menu_selection("Please select one of the following options", menu)
    return option

# def menu_action(x):
#     if x == 0:
#         add_book()
#     elif x == 1:
#         remove_book()
#     elif x == 2:
#         view_books()
#     elif x == 3:
#         exit()
#     else:
#         sys.exit(1)
#
# def add_book():
#
#
#
# def remove_book():
#
#
#
# def view_books():
#
#
#
# def exit():











if __name__ == "__main__":
    main()