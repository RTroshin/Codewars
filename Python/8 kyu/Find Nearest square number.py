def nearest_sq(n):
    sqrt = int(pow(n, 1 / 2))
    nearest_left = sqrt ** 2
    nearest_right = (sqrt + 1) ** 2
    return nearest_left if n - nearest_left < nearest_right - n else nearest_right
