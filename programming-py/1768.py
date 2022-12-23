def merge_alternate(word1, word2):
    merged = ""
    index = 0
    while index < len(word1) and index < len(word2):
        merged += word1[index]
        merged += word2[index]
        index += 1
    if index < len(word1):
        merged += word1[index:]
    if index < len(word2):
        merged += word2[index:]
    return merged


# test below
print(merge_alternate("abc", "pqr"))  # apbqcr
print(merge_alternate("ab", "pqrs"))  # apbqrs
print(merge_alternate("abcd", "pq"))  # apbqcd
