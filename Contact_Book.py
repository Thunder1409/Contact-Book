def add_contact(name, number, email, address):
    f_name = open("names.txt", "a")
    f_number = open("number.txt", "a")
    f_email = open("email.txt", "a")
    f_address = open("address.txt", "a")

    f_name.write(name)
    f_number.write(number)
    f_email.write(email)
    f_address.write(address)

def search_contact(find_in):
    f_name = open("names.txt", "r")
    f_number = open("number.txt", "r")
    f_email = open("email.txt", "r")
    f_address = open("address.txt", "r")

    names_list = f_name.readlines()
    number_list = f_number.readlines()
    email_list = f_email.readlines()
    address_list = f_address.readlines()


    try:
        if (find_in == 1):
            find_name = input("Enter name to find -: ") + "\n"
            location = names_list.index(find_name)

        elif (find_in == 2):
            find_number = str(int(input("Enter number to find -: "))) + "\n"
            location = number_list.index(find_number)

        else:
            print("Wrong input")

        print("\n Name -: ", names_list[location], "Phone Number -: ", number_list[location], "Email -: ",
              email_list[location], "Address -: ", address_list[location])

        data = [names_list[location], number_list[location], email_list[location], address_list[location]]

        return data


    except(ValueError, IndexError):
        print("\nGiven name or number is not saved")

def view_contact():
    f_name = open("names.txt", "r")
    f_number = open("number.txt", "r")
    f_email = open("email.txt", "r")
    f_address = open("address.txt", "r")

    names_list = f_name.readlines()
    number_list = f_number.readlines()
    email_list = f_email.readlines()
    address_list = f_address.readlines()

    for location in range(len(names_list)):
        print("\n Name -: ", names_list[location], "Phone Number -: ", number_list[location], "Email -: ",
              email_list[location], "Address -: ", address_list[location])

def update_contact():
    f_name = open("names.txt", "r")
    f_number = open("number.txt", "r")
    f_email = open("email.txt", "r")
    f_address = open("address.txt", "r")

    print("1. Name \n2. Phone Number")
    find_in = int(input("Find the contact to update details (1,2) -: "))
    contact_details = search_contact(find_in)

    if (contact_details):
        print("1. Name \n2. Number \n3. Email \n4. Address")
        change = int(input("what you want to edit -: "))

        if (change == 1):
            new_name = input("New name to change -: ") + "\n"
            name_data = f_name.read().replace(contact_details[0], new_name)

            w_name = open("names.txt", "w")
            w_name.write(name_data)

        elif (change == 2):
            new_number = str(int(input("New number to change"))) + "\n"
            number_data = f_number.read().replace((contact_details[1], new_number))

            w_number = open("number.txt", "w")
            w_number.write(number_data)

        elif (change == 3):
            new_email = input("New email to change") + "\n"
            email_data = f_email.read().replace((contact_details[2], new_email))

            w_email = open("email.txt", "w")
            w_email.write(email_data)

        elif (change == 4):
            new_address = input("New address to change") + "\n"
            address_data = f_address.read().replace(contact_details[3], new_address)

            w_address = open("address.txt", "w")
            w_address.write(address_data)

        else:
            print("Invalid input")

    else:
        print("Sorry No contact found...")

def delete_contact():
    f_name = open("names.txt", "r")
    f_number = open("number.txt", "r")
    f_email = open("email.txt", "r")
    f_address = open("address.txt", "r")

    print("1. Name \n2. Phone Number")
    find_in = int(input("Find the contact to update details (1,2) -: "))
    contact_details = search_contact(find_in)

    name_data = f_name.read().replace(contact_details[0], "")
    w_name = open("names.txt", "w")
    w_name.write(name_data)

    number_data = f_number.read().replace(contact_details[1], "")
    w_number = open("number.txt", "w")
    w_number.write(number_data)

    email_data = f_email.read().replace(contact_details[2], "")
    w_email = open("email.txt", "w")
    w_email.write(email_data)

    address_data = f_address.read().replace(contact_details[3], "")
    w_address = open("address.txt", "w")
    w_address.write(address_data)

    print("Contact Deleted")


print("--- Welcom to Contact Book ---")

while True:
    print("\n1. Add Contact \n2. View Contact List \n3. Search Contact \n4. Update Contact \n5. Delete Contact \n99. EXIT")
    todo = int(input("What you want to do -: "))
    print("")

    if (todo == 1):
        name = input("Enter the name -: ") + "\n"
        number = str(int(input("Enter the number -: "))) + "\n"
        email = input("Enter email address -: ") + "\n"
        address = input("Enter home address -: ") + "\n"
        add_contact(name, number, email, address)

    elif (todo == 2):
        view_contact()

    elif (todo == 3):
        print("1. Name \n2. Phone Number")
        find_in = int(input("How you want to find the contact (1,2) -: "))
        contact_details = search_contact(find_in)

    elif (todo == 4):
        update_contact()

    elif (todo == 5):
        delete_contact()

    elif(todo == 99):
        print("Quiting")
        break

    else:
        print("Wrong Input...")
