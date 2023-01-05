def find_min_arrow_shots(points):
    if not points:
        return 0
    ballons_diameter = sorted(points)
    ballon_busted_at = ballons_diameter[0]
    arrows_used = 1
    for left_point, right_point in ballons_diameter[1::]:
        if left_point > ballon_busted_at[1]:
            arrows_used += 1
            ballon_busted_at = [left_point, right_point]
        else:
            ballon_busted_at[1] = min(ballon_busted_at[1], right_point)
    return arrows_used


# test below
print(find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]))
