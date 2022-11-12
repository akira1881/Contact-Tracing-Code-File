# Contact Tracing Files
# Prgrammed by: Charina C. Vallecera
# BSCOE 2-2

file = {"Rasha Avery": "21 years old ----  Pasig City  ----  09563742834",
        "Rhan"}


def main_menu():
    print(">>>>>>> CONTACT TRACING <<<<<<<")
    print()
    print(">>>>>>> MENU <<<<<<<")
    print()
    print(" 1.) ADD    ")
    print(" 2.) SEARCH ")
    print(" 3.) EXIT   ")
    print()


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


def full_tab():
    while True:
        print(">>>>>>> List Format <<<<<<<")
        print()
        print("Fullname: ", file)


def exits():
    while True:
        print(">>>>>>> Exit <<<<<<<")
        print()
        print("Thank you for using this program!!!")
        print()
        break


def coding():
    while True:
        main_menu()
