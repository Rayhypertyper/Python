import os
import pandas
from time import sleep
contacts = [] # a list of lists to store contacts
print("ICS3U Summative 1: Simple Contacts Database")
def clear():
    os.system('cls')
    os.system('clear')
def main():
    clear()
    # Go back to main menu based on the number of contacts
    if len(contacts) == 0: # no contacts
        print("1. Add a Contact")
        print("2. Exit Program")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            exit_program()
        else:
            print("Invalid choice. Please try again.")
            main()
    else: # contacts exist
        print("1. Add a Contact")
        print("2. Edit a Contact")
        print("3. Delete a Contact")
        print("4. Delete all Contacts")
        print("5. Display Contacts")
        print("6. Exit Program")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2" and len(contacts) > 0:
            edit_contact()
        elif choice == "3" and len(contacts) > 0:
            delete_contact()
        elif choice == "4" and len(contacts) > 0:
            delete_all_contacts()
        elif choice == "5" and len(contacts) > 0:
            display_contacts()
        elif choice == "6":
            exit_program()
        else:
            print("Invalid choice. Please try again.")
            main()
    clear()
def add_contact():
    # add a new contact to the contacts list
    clear()
    # get the contact's first name, last name and phone number
    first_name = input("Enter the contact's first name: ").strip()
    while first_name == "": # validate the input
        print("First name cannot be blank.")
        first_name = input("Enter the contact's first name: ").strip()
    clear()
    last_name = input("Enter the contact's last name: ").strip()
    while last_name == "": # validate the input
        print("Last name cannot be blank.")
        last_name = input("Enter the contact's last name: ").strip()
    clear()
    phone_number = format_phone_number(input("Enter the contact's phone number (10 digits): ").strip().replace("-","").replace("(","").replace(")","").replace(" ",""))
    while not len(phone_number) == 14: # validate the input
        print("Phone number must be 10 numeric characters.")
        phone_number = format_phone_number(input("Enter the contact's phone number (10 digits): ").strip().replace("-","").replace("(","").replace(")","").replace(" ",""))  
    clear()
    email = input("Enter the contact's email: ").strip()
    if email == "":
        email = "N/A"
    clear()
    address = input("Enter the contact's address: ").strip()
    if address == "":
        address = "N/A"
    # create a list of the contact's information
    contact = [first_name, last_name, phone_number, email, address]
    # append the contact to the contacts list
    contacts.append(contact)
    clear()
    # display a success message
    print("The contact was successfully added.")
    sleep(1)
    # Go back to main menu
    main()

def edit_contact():
    # edit an existing contact in the contacts list
    clear()
    # display all the contacts in a table
    standard_table()
    # get the number of the contact to edit
    number = input("Enter the number of the contact you want to edit: ").strip()
    while not number.isnumeric() or int(number) < 1 or int(number) > len(contacts): # validate the input
        print("Invalid contact. Please try again.")
        number = input("Enter the number of the contact you want to edit: ").strip()
    index = int(number) -1 # get the index of the contact in the contacts list
    # get the original values of the contact
    first_name = contacts[index][0]
    last_name = contacts[index][1]
    phone_number = contacts[index][2]
    email = contacts[index][3]
    address = contacts[index][4]
    # get the new values for the contact
    clear()
    new_first_name = input(f"Enter a first name to replace {first_name}. To keep {first_name} press ENTER: ").strip()
    if new_first_name == "": # keep the original value
        new_first_name = first_name
    clear()
    new_last_name = input(f"Enter a last name to replace {last_name}. To keep {last_name} press ENTER: ").strip()
    if new_last_name == "": # keep the original value
        new_last_name = last_name
    clear()
    new_phone_number = format_phone_number(input(f"Enter a phone number to replace {phone_number}. To keep {phone_number} press ENTER: ").strip().replace("-","").replace("(","").replace(")","").replace(" ",""))
    if new_phone_number == "": # keep the original value
        new_phone_number = phone_number
    while not len(new_phone_number) == 14: # validate the input
        print("Phone number must be 10 numeric characters.")
        new_phone_number = format_phone_number(input(f"Enter a phone number to replace {phone_number}. To keep {phone_number} press ENTER: ").strip().replace("-","").replace("(","").replace(")","").replace(" ",""))
    clear()
    new_email = input(f"Enter an email to replace {email}. To keep {email} press ENTER: ").strip()
    clear()
    new_address = input(f"Enter an address to replace {address}. To keep {address} press ENTER: ").strip()
    if new_address == "":
        new_address = address
    # create a list of the new contact information
    new_contact = [new_first_name, new_last_name, new_phone_number, new_email, new_address]
    # update the contact in the contacts list
    contacts[index] = new_contact
    clear()
    # display a success message
    print("The contact was successfully edited.")
    sleep(1)
    # Go back to main menu
    main()

def delete_contact():
    # delete an existing contact from the contacts list
    clear()
    # display all the contacts in a table
    standard_table()
    # get the number of the contact to delete
    number = input("Enter the number of the contact you want to delete: ").strip()
    while not number.isnumeric() or int(number) < 1 or int(number) > len(contacts): # validate the input
        print("Invalid number. Please try again.")
        number = input("Enter the number of the contact you want to delete: ").strip()
    number = int(number) # convert to integer
    # get the index of the contact in the contacts list
    index = number - 1
    # remove the contact from the contacts list
    contacts.pop(index)
    clear()
    # display a success message
    print("The contact was successfully deleted.")
    sleep(1)
    # Go back to main menu
    main()

def delete_all_contacts():
    # delete all the contacts from the contacts list
    clear()
    # get the user's confirmation
    confirm = input("Are you sure you want to delete all the contacts? (y/n): ").strip().lower()
    while confirm not in ["y", "n"]: # validate the input
        print("Invalid input. Please enter y or n.")
        confirm = input("Are you sure you want to delete all the contacts? (y/n): ").strip().lower()
    if confirm == "y": # delete all the contacts
        # clear the contacts list
        contacts.clear()
        clear()
        # display a message
        print("The database is now empty.")
        sleep(1)
    else: # do not delete the contacts
        clear()
    # Go back to main menu
    main()

def display_contacts():
    # display all the contacts in the contacts list
    clear()
    standard_table()
    # Go back to main menu
    input("\n\nEnter any key to return to main menu: ")
    main()

def exit_program():
    # exit the program
    clear()
    print("Goodbye")
    quit()

def standard_table():
    # display the contacts in a table format
    # print the table header
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<40} \n".format('#', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Address'))
    # loop through the contacts list
    for i in range(len(contacts)):
        # get the contact information
        first_name = contacts[i][0]
        last_name = contacts[i][1]
        phone_number = contacts[i][2]
        email = contacts[i][3]
        address = contacts[i][4]
        # print the contact information with the number in a table row
        print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<40}".format(i+1, first_name, last_name, phone_number, email, address))
        
def smart_table():
    # display the contacts in a table format using pandas
    print(pandas.DataFrame(contacts, columns=['First Name', 'Last Name', 'Phone Number', 'Email','Address']))

def format_phone_number(phone_number):
    # formats the phone number as (613) 111-2222
    # get the first three digits
    area_code = phone_number[:3]
    # get the next three digits
    prefix = phone_number[3:6]
    # get the last four digits
    line_number = phone_number[6:]
    # return the formatted phone number
    return f"({area_code}) {prefix}-{line_number}"
# call the main function
main()
