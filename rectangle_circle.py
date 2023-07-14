length = eval(input("Enter length: "))
width = eval(input("Enter width: "))

pi = 3.14;
if length == width:
   rectangle_area = length * width;
   print("It's a square, i.e.; ",rectangle_area,"metre-square")
elif length != width:
   rectangle_area = length * width;
   print("Area of rectangle is ",rectangle_area)
print("====================================")
radius = eval(input("Enter radius: "))
circle_area = pi * radius * radius;
print("Area of circle is ",circle_area)
