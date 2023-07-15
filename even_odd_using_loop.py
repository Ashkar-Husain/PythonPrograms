# WAP to print all even and odd numbers between 1 and 100;

# Using while loop
count =1
while(count <= 100):
    
    if(count%2==0):
         print(count,"is an even number")
    else:
        print(count,"is an odd number")
    count+=1    
print("Bye")

# Using for loop
'''
for x in range(1,101,1):
    if(x%2==0):
        print(x,"is an even number")
    else:
        print(x,"is an odd number")
    x+=1
print("Bye")
'''
