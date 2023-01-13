import re


def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]


# test below
print(isPalindrome("A man, a plan, a canal: Panama"))
