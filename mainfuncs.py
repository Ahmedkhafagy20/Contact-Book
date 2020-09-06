from contactclass import *
from os import listdir, remove


def CreateContact():
    contact_name = input("Enter contact name: ")
    contact_number = input("Enter contact number: ")
    contact_address = input("Enter new address: ")
    return Contact(contact_name, contact_number, contact_address)


def SearchContact():
    searched_name = input("Enter contact name: ")
    if f"{searched_name}.txt" not in listdir(
            "Contacts"):
        print("Name doesn't exist")
    else:
        found_contact = open(
            f"Contacts\\{searched_name}.txt",
            "r")
        local_list = []
        for item in found_contact.readlines():
            local_list.append(item.rstrip('\n'))

        contact_name, contact_number, contact_address = tuple(local_list)
        found_contact.close()
        return Contact(contact_name, contact_number, contact_address)


def DeleteContact():
    contact_to_delete = input("Enter contact name: ")
    if f"{contact_to_delete}.txt" not in listdir(
            "Contacts"):
        print("Name doesn't exist")
    else:
        remove(
            f"Contacts\\{contact_to_delete}.txt")
        if f"{contact_to_delete}.txt" not in listdir(
                "Contacts"):
            print("Contact succesfully deleted!!")
