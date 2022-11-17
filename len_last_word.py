def len_of_last_word(sentence):
    return len(sentence.split()[-1:][0])


# test below
print(len_of_last_word("Hello World"))
