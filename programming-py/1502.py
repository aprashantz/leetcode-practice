def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True


# test below
print(canMakeArithmeticProgression([3, 5, 1]))
print(canMakeArithmeticProgression([1, 2, 4]))
