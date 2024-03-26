def build_dictionary():
    word = input("Enter something: ")
    word_list = word.lower().split()

    dict = {}

    for word in word_list: 
        if word in dict: 
            dict[word] += 1 
        else: 
            dict[word] = 1


    for x,y in dict.items(): 
        print(x,y)

build_dictionary()