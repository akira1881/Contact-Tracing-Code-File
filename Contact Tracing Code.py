# Contact Tracing Files
# Programmed by: Charina C. Vallecera
# BSCOE 2-2

main_file = {}


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
            print(f"\t{'Name:': <3s}", search_input, (main_file[search_input]['Age']),
                  (main_file[search_input]['Address']), (main_file[search_input]['Phone']))
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
            exit()
            print()

    else:
        print("Invalid Input!")
        baseline()


while True:
    baseline()
