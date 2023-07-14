"""Admission to professional course in a college according to following conditions:
Marks in Mathematics are greater than or equal to 60 and marks in physics is greater
than or equal to 50 and marks in chemistry is greater than or equal to 40
			OR
Total marks in mathematics, physics and chemistry is greater than or equal to 200.
					OR
Total marks in mathematics and physics are greater than or equal to 150.
Marks of all three subjects will be entered through the keyboard. WAP to tell whether
a student is qualifying for admission or not."""
t_marks = 0;
mph_marks = 0;

maths = eval(input("Enter the marks in mathematics :"))
physics = eval(input("Enter the marks in physics :"))
chemistry = eval(input("Enter the marks in chemistry :"))

t_marks = maths + physics + chemistry;
mph_marks = maths + physics;
if  maths >= 60 and physics >= 50 and chemistry >= 40:    
    print("Congratulations! You are qualified.")
elif t_marks >= 200:
    print("Congratulations! You are qualified as you got ",t_marks," numbers in total three subjects.")
elif mph_marks >= 150:
    print("Congratulations! You are qualified as you got total ",mph_marks," numbers in maths and physics.")
else:
    print("You are disqualified")
    




