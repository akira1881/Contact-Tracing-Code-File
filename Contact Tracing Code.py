# Contact Tracing Files
# Prgrammed by: Charina C. Vallecera
# BSCOE 2-2

file = {"Rasha Avery": "21 years old ----  Pasig City  ----  09563742834",
        "Rhaenyra Edwards": "19 years old ---- Pasay City ---- 09275463249",
        "Ronnie Karev": "22 years old ---- Quezon City ---- 09182745947"}


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
        user_age = input("Age: ")
        user_address = input("Address: ")
        user_number = input("Phone Number: ")
        whole_info = f"\t{user_input: <20}{user_age: <20}{user_address: <60}{user_number: <15}"
        file.update(whole_info)
        print()
        print("SAVED!")
        print()

        chance = input("Would you like to add another contact? (yes/no) ")
        if chance.casefold() == "yes":
            add()
        elif chance.casefold() == "no":
            main_menu()


def search():
    while True:
        print(">>>>>>> Search Contact <<<<<<<")
        print()
        search_input = input("Type the Fullname")
        file.get(search_input)
        print()
        print(">>>>>>> Contact Found! <<<<<<<")
        print()

        chanceAgain = input("Would you like to search another contact? (yes/no) ")
        if chanceAgain.casefold() == "yes":
            add()
        elif chanceAgain.casefold() == "no":
            main_menu()


def full_tab():
    while True:
        print(">>>>>>> List Format <<<<<<<")
        print()


def exits():
    while True:
        print(">>>>>>> Exit <<<<<<<")
        print()
        print("Thank you for using this program!!!")
        print("Bye!")
        print()
        break


def coding():
    while True:
        main_menu()
        final_option = int(input("Choose the number of your choice: "))
        if final_option