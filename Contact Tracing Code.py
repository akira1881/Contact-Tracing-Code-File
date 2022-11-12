# Contact Tracing Files
# Prgrammed by: Charina C. Vallecera
# BSCOE 2-2

print("Contact Tracing Menu")
print()
print(">>>>>>> MENU <<<<<<<")
print(" 1.) ADD    ")
print(" 2.) SEARCH ")
print(" 3.) EXIT   ")

file = {}


def add():
    while True:
        print(">>>>>>> Add New Contact <<<<<<<")
        print()
        user_input = input("Fullname: ")
        file.update(user_input)
        user_age = input("Age: ")
        file.update(user_age)
        user_address = input("Address: ")
        file.update(user_address)
        user_number = input("Phone Number: ")
        file.update(user_number)
        print()
        print("SAVED!")


def search():
    while True:
        print(">>>>>>> Search Contact <<<<<<<")
        print()
        search_input = input("Type the Fullname")
        file.get(search_input)
        print()
        print(">>>>>>> Contact Found! <<<<<<<")

def 