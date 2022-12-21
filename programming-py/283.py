def move_zeroes(nums):
    zero_count = 0
    for each in nums:
        if each == 0:
            zero_count += 1
    for i in range(zero_count):
        nums.remove(0)
        nums.append(0)


# test below
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0]))
