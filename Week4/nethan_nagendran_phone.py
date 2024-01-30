def format_phone_number(number):
    # Extract the area code, prefix, and line number using % and //
    phone_area_code = number // 10000000
    phone_prefix = (number // 10000) % 1000
    phone_line_number = number % 10000

    # Format the number according to the specified format
    formatted_number = f"({phone_area_code}) {phone_prefix}-{phone_line_number}"
    return formatted_number

# Example usage
user_phone_num = int(input("Enter a phone number: "))
formatted_phone_number = format_phone_number(user_phone_num)
print(formatted_phone_number)


phone = 1231231233
print(phone)