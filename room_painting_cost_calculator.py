print("ROOM PAINTING COST CALCULATOR")


l = float(input("enter the length of one wall of the room = "))
w = float(input("enter the width of one wall of the room = "))
h = float(input("enter the hight of one wall of the room = "))
per_cost = float(input("enter the painting cost per square ft. = "))

a = 2 * h * (l+ w)
ca = l * w
ta = a + ca 
tc = per_cost * ta 
print(f"your total painting cost is :{tc}₹")

