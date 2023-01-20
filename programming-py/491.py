def findSubsequences(nums):
    """returns non-decreasing subsequences"""
    subsets = [[]]
    subsequences = []
    for i in range(len(nums)):
        for j in range(len(subsets)):
            subset = subsets[j] + [nums[i]]
            subsets.append(subset)
            if len(subset) > 1 and subset not in subsequences and subset == sorted(subset):
                subsequences.append(subset)
    return subsequences


# test below
print(findSubsequences([4, 6, 7, 7]))
print(findSubsequences([4, 4, 3, 2, 1]))
