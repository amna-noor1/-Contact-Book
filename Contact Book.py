contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']}")

def delete_contact():
    view_contacts()
    num = int(input("Enter number to delete: "))
    if 0 < num <= len(contacts):
        removed = contacts.pop(num - 1)
        print(f"Deleted {removed['name']}")
    else:
        print("Invalid number.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid option!")
