class NumArray:
    def __init__(self, nums) -> None:
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])


# test below
na1 = NumArray([-2, 0, 3, -5, 2, -1])
print(na1.sumRange(0, 2))
print(na1.sumRange(2, 5))
print(na1.sumRange(0, 5))
