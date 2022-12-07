def longest_common_prefix(words):
    common_prefix = ""
    if len(words) == 0:
        return common_prefix
    for i in range(len(words[0])):
        for each in words:
            if i == len(each) or each[i] != words[0][i]:
                return common_prefix
        common_prefix += words[0][i]
    return common_prefix


# test below
print(longest_common_prefix(["flower", "flow", "flight"]))
