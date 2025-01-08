#cafe_management_software.adv.py
import datetime 
now = datetime.datetime.now()

Menu = {}

#Cafe's Item Management Area:

Menu["BURGER"] = 50
Menu["PIZZA"] = 100
Menu["CAKE"] = 80
Menu["COFFEE"] = 40
Menu["SALAD"] = 70
Menu["PASTA"] = 130

#Greet:
print("~~~~~~Welcome to Mom's Cafe~~~~~~")
while True:
    print()
    try:
        name = str(input("Enter your first name to proceed : ")).strip().upper()
    except ValueError:
        print("enter a valid name...")    

    else:
        print()
        print(f" Hey.... '{name}' welcome to Mom's Cafe...")
        print("Choose your item from the Menu given bellow....")
        print()
        print("***MENU***")
        print ("\n\n1. Pizza:   Rs:100\n\n2. Burger:   Rs:50\n\n3. Coffee:   Rs:40\n\n4. Cake:   Rs:80\n\n5. Salad:   Rs:70\n\n6. Pasta:   Rs:130")
        break
        

#Total Order Define:
Order_total = 0

#The First Order:
while True:
    item1 = input(f"\n\nWhat do you want to order {name}...? : ").strip().upper()
    if item1 in Menu:
        Order_total += Menu[item1]
        print(f"\n {name}, your Order '{item1}' has been Confirmed.... ")
        print(f"You have to pay :{Order_total}₹")
        break 
    else:
        print(f"\nSorry... {name} your ordered item '{item1}' is not available in our cafe... please select your order from given Menu..")
    
#The Second Order:
while True:
    another_item = input(f"\nDo you want to order another item {name}...?[Y/N]").strip().upper()
    if another_item == 'Y':
        print()
        item2 = input("Select your order from given Menu...").strip().upper()
        if item2 in Menu:
            Order_total += Menu[item2]
            print(f"\n {name}, your Order '{item1}','{item2}' has been Confirmed successfully..\nYou will receive your order very soon...\nYour Total Amount :{Order_total}₹ ")
            print("\nDate: ", now.strftime("%D"))
            print("Time: ", now.strftime("%H: %M: %S"))
            print("\n\nThankyou for choosing Mom's Cafe.......")
            break 
        else:
            print(f"\nSorry... {name} your ordered item '{item2}' is not available in our cafe... please select your order from given Menu..")
            
    elif another_item == 'N':
        print(f"\n {name}, your Order '{item1}' has been Confirmed successfully..\nYou will receive your order very soon...\nYour Total Amount :{Order_total}₹ ")
        print("\nDate: ", now.strftime("%D"))
        print("Time: ", now.strftime("%H: %M: %S"))
        print("\n\nThankyou for choosing Mom's Cafe.......")
        break
    else:
        print()
        print("Error...  Please enter a valid option...")    
            
        
    
print("\n\n\n\n© Copyright By JPM OFFICIAL")         
        
    
    