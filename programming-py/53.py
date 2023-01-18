def maxSubArray(nums):
    """using kadane approach"""
    max_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_here = max(num, max_here+num)
        max_so_far = max(max_so_far, max_here)
    return max_so_far


# test below
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([5, 4, -1, 7, 8]))
