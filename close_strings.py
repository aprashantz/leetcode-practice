from collections import defaultdict


def is_close_strings(word1, word2):
    """
    returns True if both the words have same alphabets and
    sum of frequency of chars of word1 matches to sum of frequency of chars of word2
    else returns False
    """
    def word_frequency(word):
        count = defaultdict(int)
        for each in word:
            if each not in word:
                count[each] = 1
            else:
                count[each] += 1
        return sorted(count.values())
    return word_frequency(word1) == word_frequency(word2) and set(word2) == set(word1)


    # test below
print(is_close_strings("a", "aa"))
print(is_close_strings("abc", "bca"))
print(is_close_strings("cabbba", "abbccc"))
