def roman_to_integer(roman):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = mapping[roman[len(roman)-1]]
    for i in range(len(roman)-2, -1, -1):
        if mapping[roman[i]] >= mapping[roman[i+1]]:
            result += mapping[roman[i]]
        else:
            result -= mapping[roman[i]]
    return str(result)


# test below
print(roman_to_integer("VI"))
