def text_filter(message):

    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    words = message.split()  

    filtered_words = []
    for word in words:
        if word not in banned_words:
            filtered_words.append(word)

    new_message = " ".join(filtered_words)

    return new_message


message_input = input("Enter your message: ")

filtered_message = text_filter(message_input)

print("Input message: ", message_input)
print("Output message:", filtered_message)

