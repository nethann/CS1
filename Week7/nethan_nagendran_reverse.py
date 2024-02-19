counter = 0
while True:
    user_input = input("Please enter your string: ")
    if user_input == "quit":
        print(f'Counted {counter} until stopped.') 
        break  
    counter += 1
    print(f"You entered: {user_input[::-1]}")
