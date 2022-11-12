# Contact Tracing Files
# Programmed by: Charina C. Vallecera
# BSCOE 2-2

main_file = {
    'Rasha Avery': {'Age': 21, 'Address': 'Pasig City', 'Phone Number': '095656543845'},
    'Mirabel Garcia': {'Age': 32, 'Address': 'Pasay City', 'Phone Number': '09875673424'},
    'Julie Stevens': {'Age': 26, 'Address': 'Cebu City', 'Phone Number': '09315843258'},
    'Cassie del Valle': {'Age': 18, 'Address': 'Bulacan', 'Phone Number': '09125349876'},
    'Avelina Luna': {'Age': 43, 'Address': 'Maasin City', 'Phone Number': '09182322379384'},
    'Jacob Potter': {'Age': 14, 'Address': 'Quezon City', 'Phone Number': '09188675742'},
    'Luther King': {'Age': 61, 'Address': 'Cavite City', 'Phone Number': '09341287834'},
    'Cris Alonzo': {'Age': 36, 'Address': 'Rizal', 'Phone Number': '09342217856'},
    'Chandria Ramirez': {'Age': 25, 'Address': 'Laguna', 'Phone Number': '09518439487'},
    'Emma Dawson': {'Age': 63, 'Address': 'Bulacan', 'Phone Number': '09418675428'}
}


def base():
    print(">>>>>>> CONTACT TRACING <<<<<<<")
    print()
    print(">>>>>>> MENU <<<<<<<")
    print()
    print(" 1.) ADD    ")
    print(" 2.) SEARCH ")
    print(" 3.) EXIT   ")
    print()


def baseline():
    base()
    final_option = int(input("What would you like to do?:"))
    if final_option == 1:
        while True:
            print(">>>>>>> Add New Contact <<<<<<<")
            print()
            one = str(input("Fullname: "))
            two = str(input("Age: "))
            three = str(input("Address: "))
            four = str(input("Phone Number: "))
            align = {'Age': two, 'Address': three, 'Phone': four}
            main_file[one] = align
            print()
            print("SAVED!")
            print()

            again = (input("Go back to main?: (yes or no) ")).casefold()
            if again == 'yes':
                baseline()
            elif again == 'no':
                continue

    elif final_option == 2:
        while True:
            print(">>>>>>> Search Contact <<<<<<<")
            print()
            search_input = input("Type the Fullname: ").casefold()
            print()
            print(f"\t\t\t{'Name': <3s}",search_input,(main_file[search_input]['Age']),
                  (main_file[search_input]['Address']),(main_file[search_input]['Phone']))
            print()
            print(">>>>>>> Contact Found! <<<<<<<")
            print()

            again = (input("Go back to main?: (yes or no) ")).casefold()
            if again == 'yes':
                baseline()
            elif again == 'no':
                continue

    elif final_option == 3:
        while True:
            print(">>>>>>>>>>> Exit <<<<<<<<<<<")
            print()
            print("Thank you for using this program!!!")
            print("Bye!")
            print()

    else:
        print("Invalid Input!")
        baseline()


while True:
    baseline()
