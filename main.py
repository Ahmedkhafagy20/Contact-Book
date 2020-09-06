from mainfuncs import *


def main():
    valid = True
    while valid:
        operation = input("Enter the next wanted operation: ")
        if operation == "change name":
            current_contact.ChangeName()
        if operation == "change number":
            current_contact.ChangeNumber()
        if operation == "change address":
            current_contact.ChangeAddress()
        if operation == "create new contact":
            current_contact = CreateContact()
        if operation == "info":
            print(current_contact)
        if operation == "search":
            current_contact = SearchContact()
        if operation == "delete":
            DeleteContact()
            current_contact = None
        if operation == "quit":
            valid = False


if __name__ == '__main__':
    main()
