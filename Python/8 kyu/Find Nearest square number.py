def nearest_sq(n):
    for i in range(0, n):
        nearest_left = i * i
        nearest_right = (i + 1) * (i + 1)
        if nearest_left <= n <= nearest_right:
            return nearest_left if n - nearest_left < nearest_right - n else nearest_right
