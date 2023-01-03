from collections import defaultdict


def min_deletion_size(strs):
    """using default dict"""
    to_delete = 0
    column_values = defaultdict(str)
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            column_values[i] += strs[j][i]
    for each in column_values.values():
        if list(each) != sorted(each):
            to_delete += 1
    return to_delete
    """using zip"""
    # for each in zip(*strs):
    #     if list(each) != sorted(each):
    #         to_delete += 1
    # return to_delete


# test below
print(min_deletion_size(["cba", "daf", "ghi"]))
print(min_deletion_size(["a", "b"]))
print(min_deletion_size(["ab", "ba"]))
print(min_deletion_size(["ab", "ab"]))
print(min_deletion_size(["zyx", "wvu", "tsr"]))
print(min_deletion_size(["rrjk", "furt", "guzm"]))
