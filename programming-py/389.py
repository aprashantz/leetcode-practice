from collections import defaultdict


def find_the_difference(s, t):
    s_count, t_count = defaultdict(int), defaultdict(int)
    for each in s:
        s_count[each] += 1
    for each in t:
        t_count[each] += 1

    for char in t:
        if char not in s_count:
            return char
        elif t_count[char] > s_count[char]:
            return char


# test below
print(find_the_difference("abcd", "abcde"))
print(find_the_difference("", "y"))
print(find_the_difference("a", "aa"))
