def can_complete_circuit(gas, cost):
    # If total gas we can obtain is not enough to total gas that is going to be consumed, we cannot complete circuit
    if sum(cost) > sum(gas):
        return -1

    gas_remaining, trying_from_index = 0, 0
    for at_station in range(len(gas)):
        gas_remaining += gas[at_station] - cost[at_station]
        if gas_remaining < 0:
            # if not possible to go to next station, we try starting from next station
            trying_from_index = at_station + 1
            # need to reset remaining gas to 0 because we will try again from next station
            gas_remaining = 0
    return trying_from_index


# test below
print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(can_complete_circuit([2, 3, 4], [3, 4, 3]))
