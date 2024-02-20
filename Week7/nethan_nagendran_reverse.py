counter = 0
while True:
    user_input = input("Please enter your string: ")
    if user_input.lower() == "quit" or user_input.lower() == "q" :
        print(f'Reversed {counter} times until stopped.') 
        break  
    counter += 1
    print(f"Reversed: {user_input[::-1]}")
