import math 
import random

# calculating the volume of a sphere 
Radius = int(input("Please enter the radius of the sphere: "))
Volume = (4/3)* math.pi * math.pow(Radius,3)
print(f'The volume of a sphere with radius of {Radius} is {Volume:.2f}')

# generating random num factorial
randomized_Num = random.randint(1,10)
print(f'The factorial of {randomized_Num} is {math.factorial(randomized_Num)}')
