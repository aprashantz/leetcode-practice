def can_visit_all_rooms(rooms):
    keys_in_hand = rooms[0]
    rooms_unlocked = {0}
    while keys_in_hand:
        # popping to remove key from hand once we use that key
        room_to_unlock = keys_in_hand.pop()
        if room_to_unlock not in rooms_unlocked:
            rooms_unlocked.add(room_to_unlock)
            # now keeping the keys in hand that we find in newly unlocked room
            keys_in_hand += rooms[room_to_unlock]
    return len(rooms_unlocked) == len(rooms)


# test below
print(can_visit_all_rooms([[1], [2], [3], []]))  # true
print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))  # false
print(can_visit_all_rooms([[2], [], [1]]))  # true
print(can_visit_all_rooms(
    [[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]]))  # false
