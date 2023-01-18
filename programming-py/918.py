def maxCircularSubArray(nums):
    """
    using kadane approach
    maximum circular sub array = max(maxiumNonCircularSubArray, SumOfWholeArray - mimimumNonCircularSubArray)
    in case if all the elements of circular subarray is negative, max element of the list is the answer
    """
    max_so_far = min_so_far = max_here = min_here = nums[0]
    negative_so_far = True
    for num in nums[1:]:
        if num >= 0:
            negative_so_far = False
        max_here, min_here = max(num, max_here+num), min(num, min_here + num)
        max_so_far, min_so_far = max(
            max_so_far, max_here), min(min_so_far, min_here)
    if negative_so_far:
        return max(nums)
    return max(max_so_far, sum(nums)-min_so_far)


# test below
print(maxCircularSubArray([1, -2, 3, -2]))
print(maxCircularSubArray([5, -3, 5]))
print(maxCircularSubArray([-3, -2, -3]))
