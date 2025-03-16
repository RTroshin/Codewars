def find_digit(num, nth):
    if nth < 1:
        return -1

    return int(str(abs(num))[-nth]) if nth <= len(str(num)) else 0
