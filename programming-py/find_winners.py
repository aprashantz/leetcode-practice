from collections import defaultdict


def find_winners(matches):
    winners = set()
    losers_count = defaultdict(int)
    for winner, loser in matches:
        winners.add(winner)
        losers_count[loser] += 1
    always_winners = winners - losers_count.keys()
    lost_once = [each for each in losers_count if losers_count[each] < 2]
    return [sorted(always_winners), sorted(lost_once)]


# test below
print(find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [
      5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
