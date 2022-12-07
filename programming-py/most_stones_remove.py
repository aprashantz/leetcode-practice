from collections import defaultdict


def remove_stones(stones):
    def dfs(idx):
        seen.add(idx)
        for nidx in adj[idx]:
            if nidx not in seen:
                dfs(nidx)
    adj = defaultdict(set)
    for i in range(len(stones)):
        x1, y1 = stones[i][0], stones[i][1]
        for j in range(i+1, len(stones)):
            x2, y2 = stones[j][0], stones[j][1]
            if x1 == x2 or y1 == y2:
                adj[i].add(j)
                adj[j].add(i)
    seen = set()
    valid_stones = 0
    for i in range(len(stones)-1, -1, -1):
        if i not in seen:
            dfs(i)
            valid_stones += 1
    return len(stones) - valid_stones


# test below
print(remove_stones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
# how many stones were removed is the output
