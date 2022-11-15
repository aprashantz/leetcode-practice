def remove_duplicates(data):
    p = 0
    for i in range(1, len(data)):
        if data[i] != data[p]:
            p += 1
            data[p] = data[i]
        print(data)
    return len(data[0:p+1])


# test below
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
