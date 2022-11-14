def is_palindrome(number):
    str_num = str(number)
    return True if (str_num == str_num[::-1]) else False


# test below
print(is_palindrome(1231))
