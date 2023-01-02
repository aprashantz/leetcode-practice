def detect_capital_use(word):
    return word == word.lower() or word == word.upper() or (word[0].isupper() and word[1::].islower())


# test below
print(detect_capital_use("USA"))
print(detect_capital_use("FlaG"))
