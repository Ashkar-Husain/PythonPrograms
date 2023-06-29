# Program to display Fibonacci sequence up to n-th term

n = int(input("Please give an integer value : "))

# first two numbers

n1,n2 = 0,1
count = 0

# check if the number of terms is valid

if n <= 0:
    print("Please enter a positive integer")

elif n == 1:
    print("Fiboncci sequence upto " ,n," : ")
    print(n1)

# Generate Fibonacci sequence

else:
    print("Fibonacci Sequence : ")

    while count < n:
        print(n1,end=" ")
        nth = n1 + n2

        # Update values

        n1 = n2
        n2 = nth
        count += 1

