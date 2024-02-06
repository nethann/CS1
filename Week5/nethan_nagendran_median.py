# Input: Taking three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    median = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    median = num2
else:
    median = num3

# Output: Displaying the median
print(f"The median value is: {median}")
