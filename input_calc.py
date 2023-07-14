"""WAP that implements the simple calculator that has following menu:
Enter 1 to find the addition of two numbers.
Enter 2 to find the subtraction of two numbers.
Enter 3 to find the multiplication of two numbers.
Enter 4 to find the division of two numbers.
Enter 5 to find the inverse of a number.
Enter 6 to find the square of a number.
Enter 7 to find the cube of a number."""

print("1 for add\n2 for sub\n3 for mul\n4 for div\n5 for inverse\n6 for sqr\n7 for qube")
option = int(input())
match(option):
    case 1:            
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))        
        print(a + b)
    case 2:                   
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))        
        print(a - b)
    case 3:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))        
        print(a * b)
    case 4:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))        
        print(a / b)
    case 5:
        a = int(input("Enter a number :"))
        print(1/a)
    case 6:
        a = int(input("Enter a number :"))
        print(a * a)
    case 7:
        a = int(input("Enter a number :"))
        print(a * a * a)
    case _:
        print("You chose an invalid number, try again")
        
                   
            

                   
                     
                   
                   
                   
                
