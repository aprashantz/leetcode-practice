def lengthOfLongestSubstring(s):
    len_of_longest_substring = 0
    for i in range(len(s)):
        str = ""
        for each in s[i::]:
            if each in str:
                break
            str += each
            len_str = len(str)
        if len_str > len_of_longest_substring:
            len_of_longest_substring = len_str
    return len_of_longest_substring


# test below
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("au"))
