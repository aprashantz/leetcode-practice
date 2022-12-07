def is_ugly_num(n):
    if n == 0:
        return False
    else:
        while (n % 2 == 0):
            n = n/2
        while (n % 3 == 0):
            n = n/3
        while (n % 5 == 0):
            n = n/5
        return n == 1


# test below
print(is_ugly_num(6))
