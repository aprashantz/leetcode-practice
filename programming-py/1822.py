def array_sign(nums):
    def signFunc(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0
    product = 1
    for each in nums:
        product *= each
    return signFunc(product)


# test below
print(array_sign([-1, -2, -3, -4, 3, 2, 1]))
