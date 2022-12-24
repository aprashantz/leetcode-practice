def freq_alphabets(s):
    mapping = {'1': 'a', '2': 'b', '3': 'c', '4': 'd',
               '5': 'e', '6': 'f', '7': 'g', '8': 'h',
               '9': 'i', '10': 'j', '11': 'k', '12': 'l',
               '13': 'm', '14': 'n', '15': 'o', '16': 'p',
               '17': 'q', '18': 'r', '19': 's', '20': 't',
               '21': 'u', '22': 'v', '23': 'w', '24': 'x',
               '25': 'y', '26': 'z'}
    i = 0
    decrypted_string = ''
    while i < len(s):
        if i+2 < len(s) and s[i+2] == '#':
            decrypted_string += mapping[s[i:i+2]]
            i += 3
        else:
            decrypted_string += mapping[s[i]]
            i += 1
    return decrypted_string


# test below
print(freq_alphabets("10#11#12"))
print(freq_alphabets("1326#"))
