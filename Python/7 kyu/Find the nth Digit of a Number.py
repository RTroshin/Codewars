def find_digit(num, nth):
    if nth < 1:
        return -1

    return 0 if nth > len(str(num)) else int(str(abs(num))[-nth])
