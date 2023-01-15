import re


def myAtoi(s):
    filtered_string = ""
    till_now = ""
    for each in s:
        if each == ".":
            break
        if re.match("[0-9-+]", each):
            if not re.search("[a-zA-Z]+", till_now):
                if (filtered_string != "" and re.search(r"\s$", till_now)) or ((each == "-" or each == "+") and re.search("[-+0-9]+", filtered_string)):
                    break
                filtered_string += each
        till_now += each
    try:
        numb = int(filtered_string)
        if numb < -2147483648:
            return -2147483648
        elif numb >= 2147483648:
            return 2147483647
        else:
            return numb
    except:
        return 0


# test below
print(myAtoi("42"))
print(myAtoi("    -42"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("0032"))
print(myAtoi("3.14159"))
print(myAtoi("   +0 123"))
print(myAtoi("-5-"))
print(myAtoi("-13+8"))
print(myAtoi("123-"))
