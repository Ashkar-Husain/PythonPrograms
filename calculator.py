# Program to create a four function calculator

result = 0;
val1 = float(input("Enter value 1: "))
val2 = float(input("Enter value 2: "))
operator = input("Enter any of the operator (+,-,*,/): ")
# Nested if.....else conditions
if(operator == "+"):
    result = val1 + val2;
elif(operator == "-"):    
    if(val1 > val2):
        result = val1 - val2;
    else:
        result = val2 - val1;
elif(operator == "*"):
    result = val1 * val2;
elif(operator == "/"):
    if(val2 == 0):
        val2 = float(input("Please enter a value other than 0: "))
        result = val1 / val2
    else:   
        print("Better luck next time")
print("Result is ",result)
