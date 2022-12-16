def house_robber(houses):
    if not houses:
        return 0
    for i in range(1, len(houses)):
        if i == 1:
            houses[i] = max(houses[i], houses[i-1])
        else:
            houses[i] = max(houses[i-1], houses[i]+houses[i-2])
    return houses[-1]


# test below
print(house_robber([1, 2, 3, 1]))
print(house_robber([2, 7, 9, 3, 1]))
print(house_robber([2, 1, 1, 2]))
print(house_robber([1, 2]))
