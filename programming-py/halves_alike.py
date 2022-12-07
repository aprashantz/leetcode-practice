def halves_are_alike(text):
    def vowel_counter(string):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        count = 0
        for each in string:
            if each in vowels:
                count += 1
        return count
    break_index = int(len(text) / 2)
    return vowel_counter(text[0:break_index]) == vowel_counter(text[break_index:])


# test below
print(halves_are_alike("textbook"))
print(halves_are_alike("book"))
