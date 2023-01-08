from collections import defaultdict


def max_points(points):
    """slope: (y2-y1)/(x2-x1)"""
    def get_slope(point_a, point_b):
        try:
            return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
        except:
            return "undefined"

    def check_straight_line(points):
        slope = set()
        for i in range(len(points)-1):
            slope.add(get_slope(points[i], points[i+1]))
        return len(slope) == 1

    num_of_coordinates = len(points)
    if num_of_coordinates < 3:
        return num_of_coordinates
    # below var to store slope and and co-ordinates that were used to get this slope
    slopes_and_points = defaultdict(list)
    for i in range(num_of_coordinates):
        for j in range(i+1, num_of_coordinates):
            slope = get_slope(points[i], points[j])
            # print(slope)
            if points[i] not in slopes_and_points[slope]:
                slopes_and_points[slope].append(points[i])
            if points[j] not in slopes_and_points[slope]:
                slopes_and_points[slope].append(points[j])

    # now we have slope and points that are used to get the slope, we now need to check whether these points make straight line or not
    # below var to store total co-ordinates used for each slope in chronological order
    slope_and_its_total_points = []
    for slope, coordinates in slopes_and_points.items():
        if check_straight_line(coordinates):
            slope_and_its_total_points.append(len(coordinates))
    return max(slope_and_its_total_points)
    # return slopes_and_points


# test below
# print(max_points([[1, 1], [2, 2], [3, 3]]))
# print(max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
# print(max_points([[0, 0]]))
# print(max_points([[0, 0], [1, -1], [1, 1]]))
# print(max_points([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]]))
print(max_points([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]))
