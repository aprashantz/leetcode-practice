def minFlipsMonoIncr(s):
    flips, ones = 0, 0
    for char in s:
        if char == "1":
            ones += 1
        elif ones > 0:
            flips += 1
            ones -= 1
    return flips


# test below
print(minFlipsMonoIncr("00110"))
print(minFlipsMonoIncr("010110"))
print(minFlipsMonoIncr("00011000"))
print(minFlipsMonoIncr("0101100011"))
