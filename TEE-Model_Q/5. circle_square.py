import math

radius=int(input("Enter radius of circle: "))
area=int(input("Enter area of square: "))

side_square=math.sqrt(area)

circum=2*math.pi*radius
peri=2*side_square

if (circum>peri):
    print("False")
else:
    print("True")

