from collections import defaultdict


def next_greater_element(nums1, nums2):
    def return_greater(element, elements):
        for each in elements:
            if each > element:
                return each
        return -1
    next_elements_list = defaultdict(list)
    for each in nums1:
        next_elements = nums2[nums2.index(each)+1::]
        for element in next_elements:
            next_elements_list[each].append(element)

    greater_elements = []
    for each in nums1:
        greater_elements.append(return_greater(each, next_elements_list[each]))
    return greater_elements


# test below
print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_element([2, 4], [1, 2, 3, 4]))
