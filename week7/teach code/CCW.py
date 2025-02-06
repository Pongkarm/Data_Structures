def ccw(a, b, c):
    """
    Determines if point c is to the left, right, or on the same line as the directed line segment ab.
    
    :param a: Tuple (x1, y1) - Point a
    :param b: Tuple (x2, y2) - Point b
    :param c: Tuple (x3, y3) - Point c
    :return: 1 if c is to the left of ab,
             -1 if c is to the right of ab,
              0 if c is on the same line as ab
    """
    # Calculate the cross product
    z = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    if z > 0:
        return 1  # c is to the left of ab
    elif z < 0:
        return -1  # c is to the right of ab
    else:
        return 0  # c is on the same line as ab


# Example points
a = (0, 0)
b = (4, 0)

# Test cases
c1 = (2, 2)  # Point to the left of ab
c2 = (2, -2)  # Point to the right of ab
c3 = (2, 0)  # Point on the line ab

print(ccw(a, b, c1))  # Output: 1 (left)
print(ccw(a, b, c2))  # Output: -1 (right)
print(ccw(a, b, c3))  # Output: 0 (on the line)
