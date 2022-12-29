def sort_by_bits(arr):
    # using bubble sort
    bit_counts = {}
    for each in arr:
        bit_counts[each] = bin(each).count('1')
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if bit_counts[arr[j]] < bit_counts[arr[i]]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            elif bit_counts[arr[j]] == bit_counts[arr[i]]:
                if arr[j] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
    return arr
    # one line below
    # return sorted(sorted(arr), key=lambda i:bin(i).count('1'))


# test below
print(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
