def check_straight_line(coordinates):
    """slope: (y2-y1)/(x2-x1)"""
    def get_slope(point_a, point_b):
        try:
            return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
        except:
            return "undefined"
    if len(coordinates) < 3:
        return True
    slope = set()
    for i in range(len(coordinates)-1):
        slope.add(get_slope(coordinates[i], coordinates[i+1]))
    # print(slope)
    return len(slope) == 1


# test below
print(check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(check_straight_line([[1, 2], [2, 3]]))
print(check_straight_line([[0, 0], [0, 1], [0, -1]]))
print(check_straight_line([[1, 2], [2, 3], [3, 5]]))  # false
print(check_straight_line([[0, 0], [0, 5], [5, 5], [5, 0]]))  # false
print(check_straight_line([[1, 1], [2, 2], [2, 0]]))  # false
