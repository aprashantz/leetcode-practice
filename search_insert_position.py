def search_insert(nums, target):
    def binary_search(nums, target):
        left, right = 0, len(nums)
        while left <= right:
            mid = (left+right) // 2
            try:
                if target == nums[mid]:
                    return nums.index(nums[mid])
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            except:
                return left
        return left

    return (binary_search(nums, target))


# test below
print(search_insert([1, 3, 5, 6, 8, 10], 12))
