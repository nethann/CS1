
speed_limit_input = int(input("Pleasze enter the speed limit for the road: "))
vehicle_recorded_speed = int(input("Please enter the vehicle's recorded speed: "))

difference_of_speed = vehicle_recorded_speed - speed_limit_input
print(difference_of_speed)


if difference_of_speed <= -10: 
    print("The speeding fine is $50")
elif difference_of_speed <= 20: 
    print("The speeding fine is $75")
elif difference_of_speed <= 40: 
    print("The speeding fine is $150")
elif difference_of_speed > 40: 
    print("The speed limit fine is $300")
else: 
    print("No ticket received")