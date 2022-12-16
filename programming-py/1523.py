def count_odds(low, high):
    if low % 2 == 0 and high % 2 == 0:
        return int((high-low)/2)
    else:
        return int((high-low)/2) + 1


# test below
print(count_odds(8, 10))
