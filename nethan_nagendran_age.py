age_set = {
    "Child": 20, 
    "Teenager": 10,
    "Adult": 5,
    "Senior": 15,
}


age_input = int(input("Enter your age: "))

if age_input < 13: 
    print(f'You are in the Child age group and receive a {age_set["Child"]}% Discount')

elif 13 <= age_input <= 19: 
    print(f'You are in the Teenager age group and receive a {age_set["Teenager"]}% Discount')

elif 20 <= age_input <= 64: 
    print(f'You are in the Adult age group and receive a {age_set["Adult"]}% Discount')

elif age_input >= 65: 
    print(f'You are in the Senior age group and receive a {age_set["Senior"]}% Discount')

