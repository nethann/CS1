#Thinisha Nethan Nagendran


import math 

#fetching the user inputs
A_length = int(input("Please enter the length of side A of the triangle (in meters): "))
B_length = int(input("Please enter the length of side B of the triangle (in meters): "))
C_length = int(input("Please enter the length of side C of the triangle (in meters): "))

#finding the side parameter
side_parameter = (A_length + B_length + C_length)
print(f'The perimeter of the triangle is {side_parameter}m')

#using heron formula 
heron_formula = (1/2*(A_length + B_length + C_length))
#fiding the area combining the heron formula 
area = math.sqrt(heron_formula * (heron_formula - A_length)*(heron_formula-B_length)*(heron_formula-C_length))
#printing out the value with 2 decimal places 
print(f'The area of the triangle is {"%.2f" % area}m^2')


#using conditionals to check the type of triangle
pythagorean_theorem = (A_length**2 + B_length**2)
if pythagorean_theorem == C_length**2:
    print("It is a Right Triangle")
elif pythagorean_theorem > C_length**2:
    print("It is a acute triangle")
elif pythagorean_theorem < C_length**2: 
    print("It is an Obtuse Triangle")

