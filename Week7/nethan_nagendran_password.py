original_password = input("Please enter your password: ")

password_replacement = {
    'o': '0',
    'i': '1',
    'a': '@',
    'e': '3',
    'A': '4',
    'B': '8',
    's': '$'
}

strong_pass = ""

for val in original_password:
    if val in password_replacement:
        strong_pass += password_replacement[val]

    else:
        strong_pass += val

strong_pass += "!"

print(f"Your new strong password is: {strong_pass}")
