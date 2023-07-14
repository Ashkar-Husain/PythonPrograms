"""Write a program that has following menu:
Enter code w for withdraw.
Enter code d for deposit.
Enter code c for checking balance.

Note: 1 take initial amount as input from user.

Note:2 You can withdraw an amount only if balance is greater than or equal to
500 and withdrawing amount should be less than balance."""

a_b = eval(input("Please enter an amount which you want to assume in your account :"))
print("w for withdraw\nd for deposit\nc for check balance")
option = input()
match(option):
    case "w":
        withdraw = eval(input("Withdraw an amount :"))
        if withdraw > a_b:
            print("Insufficient fund")        
        elif a_b >= 500:
            print("You have just withdrawed",withdraw," rupees")
            print("Your current account balance is ",a_b - withdraw, " rupees")
        else:
            print("Sorry your account balance is less than Rs. 500")
    case "d":
        deposit = eval(input("Deposit an amount :"))
        print("You have just deposited ",deposit," rupees")
        print("Your current account balance is ",a_b + deposit, " rupees")
    case "c":
        print("Your account balance is ",a_b, " rupees")
    case  _:
        print("You chose an invalid option")
        







