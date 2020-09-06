from os import rename


class Contact:
    def __init__(self, name, number, address):
        self.name = name.title()
        self.number = number
        self.address = address
        mycontact = open(
            f"Contacts\\{self.name}.txt",
            "w")
        mycontact.write(f"{self.name}\n"
                        f"+2{self.number}\n"
                        f"{self.address}\n")
        mycontact.close()

    def __repr__(self):
        return (f"Name: {self.name}\n"
                f"Number: {self.number}\n"
                f"Address: {self.address}\n")

    def ChangeNumber(self):
        new_number = int(input("Enter the new number: "))
        self.number = new_number
        mycontact = open(
            f"Contacts\\{self.name}.txt",
            'w')
        mycontact.write(f"{self.name}\n"
                        f"{self.number}\n"
                        f"{self.address}\n")
        mycontact.close()

    def ChangeName(self):
        new_name = input("Enter the new name: ")
        oldname = self.name
        self.name = new_name
        mycontact = open(
            f"Contacts\\{oldname}.txt",
            'w')
        mycontact.write(f"{self.name}\n"
                        f"{self.number}\n"
                        f"{self.address}\n")
        mycontact.close()
        rename(
            f"Contacts\\{oldname}.txt",
            f"Contacts\\{self.name}.txt"
        )

    def ChangeAddress(self):
        new_address = input("Enter the new address: ")
        self.address = new_address
        mycontact = open(
            f"Contacts\\{self.name}.txt",
            'w')
        mycontact.write(f"{self.name}\n"
                        f"{self.number}\n"
                        f"{self.address}\n")
        mycontact.close()