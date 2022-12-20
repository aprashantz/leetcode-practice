def are_almost_equal(s1, s2):
    s1_chars, s2_chars, char_diff = set(), set(), 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            char_diff += 1
            s1_chars.add(s1[i])
            s2_chars.add(s2[i])
        if char_diff > 2:
            return False
    return s1_chars == s2_chars


# test below
print(are_almost_equal('bank', 'kanb'))
print(are_almost_equal('attack', 'defend'))
print(are_almost_equal('kelb', 'kelb'))
