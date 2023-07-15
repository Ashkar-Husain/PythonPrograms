# WAP to check prime number entered through keyboard.
number = int(input("Enter an whole number :"))
count = 0
i = 1
if number < 1:
    print("Negative values are not allowed,try again")
elif number == 0:
    print("Enter an integer other than 0")
elif number == 1:
    print("1 is neithe a prime number not a composite number")
else:
    while(number>=i):
        if number % i == 0:
            count = count+1
        i+=1
    if count == 2:
        print(number,"is a prime number")
    else:
        print(number,"is not a prime number")
print("Bye")
            
    
