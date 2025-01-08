#phone_book_management_software.py

#Contact data saving area:
contacts = {}

#interface:
print("*****PHONE BOOK*****")
print()
print("\n1.   Add a Contact")
print("\n2.   Delete a Contact")
print("\n3.   Search a Contact")
print("\n4.   Show all Contacts")
print("\n5.   Delete all the Contacts")
print("\n6.   Edit a saved contact number")

#programming 
while True:
    choice = input("\nEnter an option numeber to proceed or enter 'Exit' to exit.... :").strip().upper()
    if choice == 'EXIT':
        print("\nExiting....")
        break
    elif choice =='1':
        key = input("\nEnter the contact name:").upper()
        value = input("Enter contact number:")
        if key not in contacts:
            try:
                value = int(value)
                contacts[key] = value
                print("\nContact name :", key)
                print("Contact number : ", contacts[key])
                print("\nSaved....")
            except ValueError:
                print("\nValue error.. please enter an numeber...")
        else:
            print("\nContact already exist..")             
    elif choice == '2':
        key2 = input("\nEnter the full name of that contact to delete.. :").upper().strip()
        if key2 in contacts:
            print("\nContact found....")
            print(f"\nName: {key2}      Number: {contacts[key2]}")
            confirmation = input("\nAre you sure to delete the contact[Yes/No]... : ").upper().strip()
            if confirmation == 'YES':
                del contacts[key2]
                print("\nThe contact has been deleted successfully.....")
            else:
                continue     
        else:
            print("\nContact not found...")
            print("please enter a saved contact to delete it....")
    elif choice == '3':
        key3 = input("\nEnter the full name of that contact to show the number.. :").upper().strip()
        if key3 in contacts:
            print("\nContact found....")
            print(f"\nContact Name: {key3}")
            print(f"Contact Number: {contacts[key3]}")
        else:
            print("\nContact not found...")    
    elif choice == '4':
        print("\n*****ALL SAVED CONTACTS*****")
        print()
        print()
        sorted_names = sorted(contacts.keys( ))
        for key in sorted_names:
            print(f"""\nName: {key}          Number: {contacts[key]}""")
    elif choice == '5':
        confirmation = input("\nAre you sure to delete all the save contact[Yes/No]... : ").upper().strip()
        if confirmation == 'YES':
            contacts.clear()
            print("\nAll the saved contacts has been deleted successfully.....")
        else:
            continue     
    elif choice == '6':
        key4 = input("\nEnter the full name of the save contact to edit....").upper().strip()
        if key4 in contacts:
            print("\nContact found...")
            print(f"\nName: {key4}      Old Number: {contacts[key4]}")
            new_num = input("\nEnter the new Number:")
            try:
                new_num = int(new_num)
                contacts[key4] = new_num
                print("\nNew number updated successfully on this contact....")
                print(f"\nName: {key4}      New Number: {contacts[key4]}")
            except ValueError:
                print("\nvalue error.. please enter an numeber...")
            
#Credit:          
print("\n\n\n© Copyright By JPM")               