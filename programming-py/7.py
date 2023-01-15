def reverse(x):
    if x < 0:
        reversed = int("-"+str(x)[1::][::-1])
    else:
        reversed = int(str(x)[::-1])
    if reversed < (-2 ** 31) or reversed >= (2 ** 31):
        return 0
    return reversed


# test below
print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
