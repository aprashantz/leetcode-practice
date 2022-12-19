def is_happy_num(n):
    sums_collection = []
    while True:
        sum_of_squares = 0
        for each in str(n):
            sum_of_squares += int(each) ** 2
            n = sum_of_squares
        if sum_of_squares in sums_collection:
            break
        sums_collection.append(sum_of_squares)
    if 1 in sums_collection:
        return True
    return False


# test below
print(is_happy_num(19))
print(is_happy_num(2))
print(is_happy_num(1))
