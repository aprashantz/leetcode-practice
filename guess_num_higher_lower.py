# guess() function is given in LeetCode, so the below code is incomplete to run in outside LeetCode console
def guess(n):
    """Does not work outside LeetCode console"""
    pass


def guess_number_higher_lower(n):
    left = 0
    right = n
    while left <= right:
        mid = (left+right) // 2
        if guess(mid) == 1:
            left = mid + 1
        elif guess(mid) == -1:
            right = mid - 1
        else:
            return mid


# test below
print(guess_number_higher_lower(6))
