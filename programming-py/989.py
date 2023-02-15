def addToArrayForm(num, k):
    number = ""
    for each in num:
        number += str(each)
    sum = int(number) + k
    new_arr = []
    for each in str(sum):
        new_arr.append(int(each))
    return new_arr


# test below
print(addToArrayForm([1, 2, 0, 0], 34))
