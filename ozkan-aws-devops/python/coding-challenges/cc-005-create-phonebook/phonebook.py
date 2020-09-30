def phonebook():
    phonebook = dict()
    while True:
        print(
"""Welcome to the phonebook application
    1. Find phone number
    2. Insert a phone number
    3. Delete a person from the phonebook
    4. Terminate""")
        
        selection = int(input("Select operation on Phonebook App (1/2/3): "))
        if selection == 4:
            print("Goodbye")
            break
        
        elif selection == 1:
            name = input("Enter the name: ").title()
            if name in phonebook:
                print(f"{name}\'s number: ", phonebook[name])
            else:
                print(f"{name} has not been recorded in phonebook.")

        elif selection == 2:
            name = input("Enter the name: ").title()
            number = input("Enter the phone number: ")
            if number.isdecimal():
                phonebook[name] = number
                print("The record has been added.")
            else:
                print("Invalid input format, cancelling operation ...")
        elif selection == 3:
            name = input("Enter the name: ").title()
            if name in phonebook:
                del phonebook[name]
                print("The record has been deleted.")
            else:
                print(f"{name} has not been recorded in phonebook.")
        else:
            print("You have entered incorrectly. Try again.")

phonebook()