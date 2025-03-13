def find_digit(num, nth):
    if nth < 1:
        return -1
    elif nth > len(str(num)):
        return 0
    
    res = str(abs(num))[-nth]

    return int(res)
