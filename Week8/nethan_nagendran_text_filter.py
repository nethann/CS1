def text_filter(message):

    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    word_split = message.split()  

    filtered_words = []
    for word in word_split:
        if word not in banned_words:
            filtered_words.append(word)

    join_message = " ".join(filtered_words)

    return join_message


message_input = input("Enter your message: ")

filtered_message = text_filter(message_input)

print("Input message: ", message_input)
print("Output message:", filtered_message)

