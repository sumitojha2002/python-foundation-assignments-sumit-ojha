"""
Exercise: Stretch Contact Book
Student: Sumit Ojha
Day: 2
"""

# Default values or variables
contacts = {}
count = 1

# Loop
while(True):
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contact")
    print("5. Exit")

    option = input("Enter your option: ")

    try:
        match int(option):
            case 1:
                # Input
                name = input("\nEnter name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter eamil: ")

                # Adds data to dictionary
                contacts[f"CON-{count}"]={"name":name.strip(),
                                        "phone_number":int(phone_number),
                                        "email":email} 
                count+=1
                print("User added successfully!\n")

            case 2:
                if not contacts:
                    print("Empty contacts\n")
                    continue

                search_contact = input("\nEnter the contact you are searching for: ")
                found_contact = {
                    contact:info for contact,info in contacts.items() if contact == search_contact
                }
                
                if not found_contact:
                    print(f"Contact not found with {search_contact}\n")
                else:
                    print(f"Contact found: {found_contact}\n")

            case 3:
                if not contacts:
                    print("Empty contacts\n")
                    continue

                search_contact = search_contact = input("Enter the contact you are searching for: ")

                found_contact = {
                    contact:info for contact,info in contacts.items() if contact == search_contact
                }

                if not found_contact:
                    print("Contact not found\n")
                    continue
                # makes the list iterable and 
                # next points to the very next item

                key = next(iter(found_contact))
                delete = contacts.pop(key,"Key not found")
                print(delete,"\n")

            case 4: 
                if not contacts:
                    print("Empty contacts\n")
                    continue

                print("All the contacts are: ")
                
                for contact_id,contact_info in contacts.items():
                    print(f"\nContact Id: {contact_id}")
                    for key,val in contact_info.items():
                        print(f"{key}: {val}")
                    print("\n")
            case 5:
                print("Exit\n")
                break
            case _:
                print("Unknown option\n") 
    except ValueError:
        print("Error: Please enter a valid number form the option.\n")   
