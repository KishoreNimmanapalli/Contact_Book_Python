contacts={}
def add_contact():
    name=input("Enter Contact Name:")
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        mobile=int(input("Enter Mobile Number:"))
        contacts[name]=mobile
        print(f"Contact {name} added.")

def search_contact():
    name=input("Enter name to search:")
    if name in contacts:
        print(f"Match Found: Name={name} | Mobile={contacts[name]}")
    else:
        print(f"{name} not exists")

def update_contact():
        name=input("Enter name to update:")
        if name in contacts:
            new_mobile=int(input("Enter new mobile number:"))
            contacts[name]=new_mobile
            print(f"{name} updated")
        else:
            print(f"{name} not found.cannot update.")

def delete_contact():
        name=input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted")
        else:
            print(f"{name} not found.")

def view_contacts():
        if not contacts:
            print("Contact book is empty.")
        else:
            print("--- Saved Contacts ---")
            for name,mobile in contacts.items():
                print(f"{name}:{mobile}")

while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_contacts()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice!")





