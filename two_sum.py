def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# test below
nums = [2, 7, 15, 11]
target = 9
s = two_sum(nums, target)
print(s)
