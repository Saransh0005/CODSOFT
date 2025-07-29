# Contact Book using Python Dictionary

contacts = {}

def add_contact():
    store = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[store] = {'Phone': phone, 'Email': email, 'Address': address}
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts saved yet.\n")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Store: {name}, Phone: {info['Phone']}")
    print()

def search_contact():
    query = input("Enter store name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if name == query or info['Phone'] == query:
            print(f"\nStore: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter store name to update: ")
    if name in contacts:
        print("Leave field empty to keep current value.")
        phone = input(f"New phone number (current: {contacts[name]['Phone']}): ") or contacts[name]['Phone']
        email = input(f"New email (current: {contacts[name]['Email']}): ") or contacts[name]['Email']
        address = input(f"New address (current: {contacts[name]['Address']}): ") or contacts[name]['Address']
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter store name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option (1–6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Start the app
menu()