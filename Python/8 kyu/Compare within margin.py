def close_compare(a, b, *margin):
    if margin and margin[0] <= abs(a - b):
        if a + margin[0] == b or a - margin[0] == b:
            return 0
        elif a + margin[0] > b or a - margin[0] > b:
            return 1
        else:
            return -1
    else:
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1
