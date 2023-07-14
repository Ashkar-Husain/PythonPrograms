"""Formula
   Siple Interest = Principal * rate * time / 100
"""

#Program

Principal = eval(input("Enter the value of principal: "))
Rate = eval(input("Enter the annual rate of interest: "))
Time = int(input("Enter the time in years: "))

Simple_int = Principal*Rate*Time/100
Amount = Principal + Simple_int 

print("Please enter an integer value")
print("Simple interest is ",Simple_int)
print("Payable amount is ",Amount)

# We use type keyword to print datatype of a variable
print(type(Amount))  
