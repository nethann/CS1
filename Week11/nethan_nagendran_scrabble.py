def scrabble():
    letter_values = {
        'A': 1,
        'B': 3,
        'C': 3, 
        'D': 2, 
        'E': 1,
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8,
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1,
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1,
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4,
        'Z': 10
    }


    print("Enter words to calculate their Scrabble score. Type 'quit' or 'q' to stop.")

    while True:
        word = input("Enter a word: ").upper()  

        if word.lower() == "quit" or word.lower() == "q": 
            break

        score = 0
        for letter in word:
            if letter in letter_values:
                score += letter_values[letter]
        print(f"{word} is worth {score} points")


scrabble()