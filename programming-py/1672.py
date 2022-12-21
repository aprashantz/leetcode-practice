def maximum_wealth(accounts):
    # wealths = []
    # for each in accounts:
    #     wealths.append(sum(each))
    # return max(wealths)
    # using list comprehension
    return max([sum(accounts[each])for each in range(0, len(accounts))])


# test below
print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
