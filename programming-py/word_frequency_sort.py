from collections import Counter


def frequency_sort(word):
    word_count = Counter(word)
    sorted_word = ""
    for char, freq in word_count.most_common():
        sorted_word += char * freq
    return sorted_word


# test below
print(frequency_sort("tree"))
