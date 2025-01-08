import pandas as pd
import time

def decitobin():
    while True:
        try:
            n = int(input("enter the number to convert into binary :"))
            bin = ""
            while n > 0 :
                r = n % 2 
                bin = str(r) + bin 
                n = n // 2
            print(bin)
            break
            
        except ValueError:
            print("please enter a number to convert...")

def bintodeci():
    while True:
        try:
            n = int(input("enter the binary digits to convert into number :"))
            decimal = 0
            power = 0
            while n > 0:
                d = n % 10
                decimal += d * (2 ** power)
                n = n // 10
                power += 1
            print(decimal)
            break

        except ValueError:
            print("please enter a integer value to convert...")    


dict1 = {
    "*Option*":[1,2],
    "*conversion*":["Decimal to Binary","Binary to Decimal"]
}
df = pd.DataFrame(dict1)


print("\n****WELCOME TO NUMBERS CONVERTER****")
print()
print(df.to_string(index=False))
while True:
    ask = input("\nenter the Option number to procced or enter 'q' to quit:").strip().lower()
    if ask == 'q':
        print("closing...")
        time.sleep(2)
        break
    elif ask == '1':

        decitobin()
    elif ask == '2':
        bintodeci()
    else:
        print("please enter a correct option...")




    



