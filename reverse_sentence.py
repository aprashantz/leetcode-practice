def reverse_sentence(sentence):
    splitted_reverse = sentence.split()[::-1]
    return " ".join(splitted_reverse)


# test below
print(reverse_sentence("Sky is blue"))
