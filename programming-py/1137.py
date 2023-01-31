def tribonacci(n):
    if n == 0:
        return 0
    t_1, t_2, t_3 = 0, 1, 1
    for i in range(n-2):
        _1, t_2, t_3 = t_2, t_3, t_1 + t_2 + t_3
    return t_3


# test below
print(tribonacci(4))
print(tribonacci(0))
