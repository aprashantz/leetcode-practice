def strStr(haystack, needle):
    needle_len = len(needle)
    new_hay_pos = 0
    for i in range(len(haystack)):
        new_hay = haystack[i::][0:needle_len]
        if len(new_hay) != needle_len:
            break
        elif new_hay == needle:
            return new_hay_pos
        new_hay_pos += 1
    return -1


# test below
print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
