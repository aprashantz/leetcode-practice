from collections import defaultdict


def possible_bipartition(n, dislikes):
    people_and_their_dislikes = defaultdict(list)
    for each in dislikes:
        people_and_their_dislikes[each[0]].append(each[1])
        people_and_their_dislikes[each[1]].append(each[0])

    # assigning group None for each numbers initially
    people_and_their_group = {i: None for i in range(1, n+1)}

    def dfs_try_partition(person, possible_group):
        if not people_and_their_group[person]:
            people_and_their_group[person] = possible_group
        else:
            return people_and_their_group[person] == possible_group

        for disliked_person in people_and_their_dislikes[person]:
            if not dfs_try_partition(disliked_person, 2 if possible_group == 1 else 1):
                return False
        return True

    for each_person in range(1, n+1):
        if not people_and_their_group[each_person] and not dfs_try_partition(each_person, 1):
            return False
    return True


# test below
print(possible_bipartition(4, [[1, 2], [1, 3], [2, 4]]))  # True
print(possible_bipartition(3, [[1, 2], [1, 3], [2, 3]]))  # False
print(possible_bipartition(
    5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))  # False
