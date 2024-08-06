import os
library = {}

# read file with checking if empty or unsupported format
def load_file(file):
    try:
        lines = file.readlines()
        if not lines:
            print("File is empty :?")
            return False
        for line in lines:
            try:
                if len(line.strip().split(",")) == 2:
                    [book, author] = line.strip().split(",")
                    library[book] = author
                else:
                    raise ValueError
            except ValueError:
                print("Invalid format:/")
                return False
        return True
    except Exception:
        print("Error reading file")
        return False


# check if the file exist and run method that check its validation and load it
def check_file_valid(path):
    global file
    try:
        file = open(path,"r")
    except Exception:
        print("File not valid :/")
        return False
    else:
        return load_file(file)


def printBooks():
    print("\nbooks in our library:")
    for book in library:
        print(book)
    print("\n")


def searchForBook():
    nobooksforauthor = True
    author = input("Enter an author name to search: ")
    for books in library:
        if str(library[books]).strip().lower().__eq__(author.strip().lower()):  # strip to remove white spaces around
            if nobooksforauthor:                                                # lower to ignore case-sensitivity
                print("The books found for this author are: ")
                nobooksforauthor = False
            print(books)
    if nobooksforauthor:
        print("the author "+ author +" has no books in our library")
    print("\n")

def start():
    while True:
        print("Nice, select an operation to start: ")
        print("1. display books ")
        print("2. search for a book by author")
        print("other to exit: ",end="")
        choice =input()
        if choice == "1":
            printBooks()
        elif choice == "2":
            searchForBook()
        else:
            print("Ok ... goodBye")
            break

path = input("Hi, Enter input file to start: ")
while True:
    if check_file_valid(path):  #if file is valid we break
        break
    else:
        print("try again: ")
        path = input()
        continue
start() # start after checking validation
