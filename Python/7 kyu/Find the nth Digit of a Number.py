def find_digit(num, nth):
    if nth < 1:
        return -1
    elif nth > len(str(num)):
        return 0

    return int(str(abs(num))[-nth])
