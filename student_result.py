"""The marks obtain by a student in 5 different subjects are input through keyboard.
The student gets the division as per the following rules:-
Percentage above or equal to 60- first division
Percentage between 50 and 59- second division
Percentage between 40 and 49 – third division
Percentage below 40- fails."""

per = eval(input("Enter the percentage of a student : "))
if per >= 60 and per <= 100:
    print("First Division")
elif per >= 50 and per <= 59:
    print("Second Division")
elif per >= 40 and per <= 49:
    print("Third Division")
elif per < 40 and per > 0:
    print("You are failed")
else:
    print("Please enter a valid percentage")
