# WAP to print all even and odd numbers between 100 and 1;

# Using for loop
for x in range(101,0,-1):
    if(x%2==0):
        print(x,"is an even number")
    else:
        print(x,"is an odd number")
print("Bye")

# Using while loop
'''
x = 100
while(x>=1):
    if(x%2==0):
        print(x,"is an even number")
    else:
        print(x,"is an odd number")
    x-=1
print("Bye")
'''
