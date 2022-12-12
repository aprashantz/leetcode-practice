def climb_stairs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b


# test below
print(climb_stairs(2))
