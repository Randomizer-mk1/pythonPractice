def replace_word():

    str = input("Enter sentence ")
    print('original sentence is:', str)

    word_to_replace = input("Enter word to replace: ")

    word_replacement = input("Enter new word: ")
    print(str.replace(word_to_replace, word_replacement))


replace_word()
