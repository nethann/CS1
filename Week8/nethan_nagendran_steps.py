def feet_to_steps(feet):
    steps = feet /2.5
    return int(steps)


distance_in_feet = float(input("Enter the distance walked in feet: "))
    
steps_walked = feet_to_steps(distance_in_feet)
print(f"Steps walked: {steps_walked}")

