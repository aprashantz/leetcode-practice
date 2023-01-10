def topKFrequent(nums, k):
    nums_and_its_frequency = {each: nums.count(each) for each in set(nums)}
    return list(dict(sorted(nums_and_its_frequency.items(),
                            key=lambda item: item[1], reverse=True)).keys())[0:k]


# test below
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
