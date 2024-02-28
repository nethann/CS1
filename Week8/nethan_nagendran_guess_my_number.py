import random 

random_val = random.randint(1,100)
times = 10

for i in range(0, times): 
    guess_input = int(input(f'Guess {i + 1}: '))

    if guess_input > random_val: 
        print("Your guess is greater than my number. Try again")

    if guess_input < random_val: 
        print("Your guess is less than my number. Try again")

    if guess_input == random_val: 
        print(f'Your correctly guessed my random number in {i + 1} times')
        break

