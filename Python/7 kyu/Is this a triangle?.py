def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return not (a >= b + c or b >= a + c or c >= a + b)
    else:
        return False
