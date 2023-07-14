# WAP to test a number is divisible by 3 or 5 and both.

num = int(input("Enter an integer: "))
if num == 0 or num < 0:
    print("Enter a positive integer other than 0")
elif num%3==0 and num%5==0:
    print("Number is divisible by 3 as well as 5")
elif num%3==0:
    print("Number is divisible by 3")
elif num%5==0:
    print("Number is divisible by 5")

else:
    print("number is neither divisible by 3 nor 5")
    
