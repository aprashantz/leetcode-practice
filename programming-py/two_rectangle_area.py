def two_rectangle_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """
    (ax1, ay1) and (ax2, ay2) are two co-ordinates of diagonal of first rectangle. Let this be A
    (bx1, by1) and (bx2, by2) are two co-ordinates of diagonal of second rectangle. Let this be B
    We need to calculate the total area covered by this two rectangle, So
    We need to calculate area of two individual rectangles and subtract the common area overlapped by these two rectangles
    """
    def area_of_rectangle(x1, y1, x2, y2):
        return (x2-x1) * (y2 - y1)

    area_A = area_of_rectangle(ax1, ay1, ax2, ay2)
    area_B = area_of_rectangle(bx1, by1, bx2, by2)

    # formula for area of overlapped region won't look confusing when we see/visualize it in graph/diagram
    overlapped_area = max(min(ax2, bx2) - max(ax1, bx1), 0) * \
        max(min(ay2, by2) - max(ay1, by1), 0)

    return ((area_A + area_B) - overlapped_area)


# test below
print(two_rectangle_area(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
