def remove_element(elements, target):
    start, end = 0, len(elements)-1
    while start <= end:
        if elements[start] == target:
            elements[start] = elements[end]
            elements[end] = elements[start]
            end -= 1
        else:
            start += 1
    return start


# test below
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
