# Contact Tracing Files
# Prgrammed by: Charina C. Vallecera
# BSCOE 2-2

print("Contact Tracing Menu")
print()
print(">>>>>>> MENU <<<<<<<")
print(" 1.) ADD    ")
print(" 2.) SEARCH ")
print(" 3.) EXIT   ")

file = []


def add():
    while True:
        print(">>>>>>> Add New Contact <<<<<<<")
        user_input = input("Fullname: ")
        file.append(user_input)
        user_age = input("Age: ")
        file.append(user_age)
        user_address = input("Address: ")
        file.append(user_address)
        user_number = input("Phone Number: ")
        file.append(user_number)
        print("SAVED!")

def search():
    while True:
        print(">>>>>>> Search Contact <<<<<<<")
        