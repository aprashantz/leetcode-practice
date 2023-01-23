from collections import defaultdict


def findJudge(n, trust):
    if len(trust) == 0 and n == 1:
        return 1
    elif len(trust) == 0:
        return -1
    trust_counts = defaultdict(int)
    voters = set()
    for each in trust:
        voters.add(each[0])
        trust_counts[each[1]] += 1
    trust_count_winner = max(trust_counts.items(), key=lambda x: x[1])
    return trust_count_winner[0] if trust_count_winner[0] not in voters and trust_count_winner[1] == n - 1 else -1


# test below
print(findJudge(2, [[1, 2]]))
print(findJudge(3, [[1, 3], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(findJudge(1, []))
