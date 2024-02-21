# counter = 0
# while True:
#     user_input = input("Please enter your string: ")
#     if user_input.lower() == "quit" or user_input.lower() == "q" :
#         print(f'Reversed {counter} times until stopped.') 
#         break  
#     counter += 1
#     print(f"Reversed: {user_input[::-1]}")


str = input("Enter a string: ")

while str.lower()!= "quit" and str != "q": 
    for i in range(len(str)-1,1,-1): 
        str_reversed += str[i]
    print(str_reversed)
    str_reversed = ""
    str = input("Enter another word: ")
    