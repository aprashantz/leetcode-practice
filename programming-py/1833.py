def max_icecream(costs, coins):
    costs.sort()
    buyable = 0
    for each in costs:
        if each <= coins:
            buyable += 1
            coins -= each
        else:
            return buyable
    return buyable


# test below
print(max_icecream([1, 3, 2, 4, 1], 7))
print(max_icecream([10, 6, 8, 7, 7, 8], 5))
print(max_icecream([7, 3, 3, 6, 6, 6, 10, 5, 9, 2], 56))
