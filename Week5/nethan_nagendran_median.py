# Input: Taking three integers from the user
val_1 = int(input("Enter the first integer: "))
val_2 = int(input("Enter the second integer: "))
val_3 = int(input("Enter the third integer: "))

if (val_1 >= val_2 and val_1 <= val_3) or (val_1 <= val_2 and val_1 >= val_3):
    median = val_1
elif (val_2 >= val_1 and val_2 <= val_3) or (val_2 <= val_1 and val_2 >= val_3):
    median = val_2
else:
    median = val_3

# Output: Displaying the median
print(f"The median value is: {median}")
