##Project: User Manager (CLI)

import json
from os import system


OP_ADD_USER = '1'
OP_SHOW_ADULTS = '2'
OP_LOAD = '3'
OP_SAVE = '4'
OP_EXIT = '0'

FILE_NAME = "users.json"


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toDict(self):
        return {
            "name": self.name,
            "age": self.age
        }

    def __str__(self):
        return self.name + " (" + str(self.age) + " years)"


users = []


option = ""

while option != OP_EXIT:
    system("clear")  

    print("\n--- USER MANAGER ---")
    print(OP_ADD_USER + ". Add user")
    print(OP_SHOW_ADULTS + ". Show users over 18")
    print(OP_LOAD + ". Load from file")
    print(OP_SAVE + ". Save to file")
    print(OP_EXIT + ". Exit")

    option = input("Choose an option: ")

    
    if option == OP_ADD_USER:
        name = input("Name: ")

        try:
            age = int(input("Age: "))
            if age < 0:
                print("Invalid age.")
            else:
                users.append(User(name, age))
                print("User added.")
        except:
            print("Error: age must be a number.")

    
    if option == OP_SHOW_ADULTS:
        found = False
        for user in users:
            if user.age >= 18:
                print(user)
                found = True

        if found == False:
            print("No users over 18.")

    
    if option == OP_LOAD:
        users.clear()
        try:
            file = open(FILE_NAME, "r")
            data = json.load(file)
            for u in data:
                users.append(User(u["name"], u["age"]))
            file.close()
            print("Data loaded.")
        except:
            print("Error loading file.")

    
    if option == OP_SAVE:
        try:
            data = []
            for user in users:
                data.append(user.toDict())

            file = open(FILE_NAME, "w")
            json.dump(data, file, indent=4)
            file.close()
            print("Data saved.")
        except:
            print("Error saving file.")

    
    if option != OP_EXIT:
        input("Press Enter to return to menu")
