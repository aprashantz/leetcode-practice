def nearest_valid_point(x, y, points):
    distances = {}
    for index, point in enumerate(points):
        if x == point[0] or y == point[1]:
            man_distance = abs(x-point[0]) + abs(y-point[1])
            distances[index] = man_distance
    if len(distances) == 0:
        return -1
    return min(distances, key=distances.get)


# test below
print(nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
