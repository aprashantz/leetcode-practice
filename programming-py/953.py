def is_alian_sorted(words, order):
    order_map = {}
    for i in range(len(order)):
        order_map[order[i]] = i

    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        for word_index in range(len(word1)):
            if word_index == len(word2):
                return False
            if word1[word_index] != word2[word_index]:
                if order_map[word2[word_index]] < order_map[word1[word_index]]:
                    return False
                break
    return True


# test below
print(is_alian_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_alian_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_alian_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"
                      ))
print(is_alian_sorted(["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv",
      "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"
                      ))
