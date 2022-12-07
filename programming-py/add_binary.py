def binary_add(str1, str2):
    if len(str1) == 0:
        return str2
    if len(str2) == 0:
        return str1
    if str1[-1] == '1' and str2[-1] == '1':
        return binary_add(binary_add(str1[0:-1], str2[0:-1]), '1') + '0'
    if str1[-1] == '0' and str2[-1] == '0':
        return binary_add(str1[0:-1], str2[0:-1]) + '0'
    else:
        return binary_add(str1[0:-1], str2[0:-1]) + '1'


# test below
print(binary_add("11", "1"))
