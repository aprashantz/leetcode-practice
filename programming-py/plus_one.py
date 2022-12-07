def plus_one(nums):
    str_num = ""
    for each in nums:
        str_num += str(each)
    int_num = int(str_num)+1
    ready_nums = []
    for each in str(int_num):
        ready_nums.append(int(each))
    return ready_nums


# test below
print(plus_one([9]))
