def word_pattern(pattern, s):
    s = s.split()
    pattern_bijection = {}
    if len(s) != len(pattern):
        return False
    for i in range(len(s)):
        if pattern[i] not in pattern_bijection:
            if s[i] in pattern_bijection.values():
                return False
            pattern_bijection[pattern[i]] = s[i]
        else:
            if pattern_bijection[pattern[i]] != s[i]:
                return False
    return pattern_bijection


# test below
print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))
print(word_pattern("abba", "dog dog dog dog"))
