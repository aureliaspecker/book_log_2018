# coding=utf-8
"""
This file logs books (title, author, date book was finished) and saves them to an external file

Needs doing: 
- Formalise add book function
- Implement dates into easy IO
- Make it work with real book file
"""

import sys
from datetime import datetime
from easyIO import get_user_menu_selection

def main():
    opening_message()
    book_log = load_book_log("test.txt")
    while True:
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
        add_book(book_log)
    elif option == 1:
        book_log=remove_book(book_log)
    elif option == 2:
        view_books(book_log)
    elif option == 3:
        save_and_exit(book_log)
    else:
        sys.exit(1)

def add_book(book_log):
    title = input("Title?")
    author = input("Author?")
    language = input("Language?")
    score = input("Rating from 1 to 10?")
    date = input("When did you finish reading this book? [DD, MM, YYYY]")
    #Finish
    book_entry = {"title":title, "author":author, "language":language, "score":score, "date":date}
    book_log.append(book_entry)



def remove_book(book_log):
    """ask user for title of book and remove from record"""
    book_titles=[book.get("title",None) for book in book_log]
    del_book=get_user_menu_selection("Select book to remove",book_titles)
    book_log.pop(del_book)
    return book_log

def view_books(book_log):
    for book_number, book in enumerate(book_log):
        print("{})".format(book_number))
        for key, value in book.items():
            print("{}: {} \n".format(key, value))

def save_and_exit(book_log):
    """save books to external file in custom format and close program"""
    file=open("test.txt","w")
    for book in book_log:
        file.write("#start\n")
        for k,v in book.items():
            file.write("{0}:{1}\n".format(k,v))
        file.write("#end\n")
    file.close()
    sys.exit(0)



if __name__ == "__main__":
    main()