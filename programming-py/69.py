def square_root(x):
    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        if mid ** 2 == x:
            return mid
        if mid ** 2 < x:
            left = mid + 1
        else:
            right = mid
    return left - 1


# test below
print(square_root(4))
