def shuffle(nums, n):
    shuffled_nums = []
    for i in range(n):
        shuffled_nums.append(nums[i])
        shuffled_nums.append(nums[i+n])
    return shuffled_nums


# test below
print(shuffle([2, 5, 1, 3, 4, 7], 3))
