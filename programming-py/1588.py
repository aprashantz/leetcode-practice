def sum_odd_length_subarrays(arr):
    subarrays_collection = []
    sum_of_odd_length_subarrays = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subarrays_collection.append(arr[i:j])

    for each in subarrays_collection:
        if len(each) % 2 != 0:
            sum_of_odd_length_subarrays += sum(each)

    return sum_of_odd_length_subarrays


# test below
print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))  # 58
print(sum_odd_length_subarrays([1, 2]))  # 3
print(sum_odd_length_subarrays([10, 11, 12]))  # 66
