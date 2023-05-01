contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone_number": phone_number, "email": email}
    contacts.append(contact)
    print("Contact added successfully.")

def search_contact():
    name = input("Enter contact name: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Name: ", contact["name"])
            print("Phone number: ", contact["phone_number"])
            print("Email: ", contact["email"])
            break
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print("Name: ", contact["name"])
            print("Phone number: ", contact["phone_number"])
            print("Email: ", contact["email"])
            print()

def edit_contact():
    name = input("Enter contact name: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Enter new details:")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact["phone_number"] = phone_number
            contact["email"] = email
            print("Contact updated successfully.")
            break
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            break
    else:
        print("Contact not found.")

while True:
    choice = int(input("Choose an option:\n1. Add a new contact\n2. Search for an existing contact\n3. Display all contacts\n4. Edit an existing contact\n5. Delete an existing contact\n6. Exit the program\n"))

    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        display_contacts()
    elif choice == 4:
        edit_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
