def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# test below
# print(two_sum([2, 7, 15, 11], 9))
print(two_sum([2, 7, 15, 11], 3))
