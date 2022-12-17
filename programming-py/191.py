def hamming_weight(n):
    bin_n = bin(n)
    one_bit_count = 0
    for each in bin_n:
        if each == '1':
            one_bit_count += 1
    return one_bit_count


# test below
print(hamming_weight(00000000000000000000000000001011))
print(hamming_weight(00000000000000000000000010000000))
print(hamming_weight(11111111111111111111111111111101))
