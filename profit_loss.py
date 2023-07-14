"""If cost price and selling price of an item is input through keyboard.
Write a program to determine how much profit he made or how much loss he got."""

cp = eval(input("Enter cost price: "))
sp = eval(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp;
    print("you got ",profit," rupees profit")
elif sp == cp:    
    print("you got neither profit nor a loss on this item")
elif sp < cp:
    profit = cp - sp;
    print("you got ",profit," rupees loss")
