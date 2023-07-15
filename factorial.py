# WAP to print calculate the factorial of number entered through keyboard;
num = eval(input("Enter a number to find factorial "))
factorial = num
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
    
    
