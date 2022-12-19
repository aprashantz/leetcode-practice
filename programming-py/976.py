def largest_perimeter_triangle(nums):
    nums.sort()
    for i in range(len(nums)-1, 1, -1):
        if nums[i] < nums[i-1] + nums[i-2]:
            return nums[i] + nums[i-1] + nums[i-2]
    return 0


# test below
print(largest_perimeter_triangle([2, 1, 2]))
print(largest_perimeter_triangle([1, 2, 1, 10]))
print(largest_perimeter_triangle([3, 6, 2, 3]))
