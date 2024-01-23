Age = int(input("Please enter your age: "))
Weight = int(input("Please enter your weight in pounds: "))
Heart_Rate = int(input("Please enter your heart rate in beats per minute: "))
Time = int(input("Please enter the length of your workout in minutes: "))

Calories = (Age * 0.2757 + Weight * 0.03295 + Heart_Rate * 1.0781 - 75.4991) * Time/8.368
print(f'Calories burned: {Calories:.2f}')

