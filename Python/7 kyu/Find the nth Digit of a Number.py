def find_digit(num, nth):
    if nth < 1:
        return -1

    if nth > len(str(num)):
        return 0

    num = abs(num)

    num = str(num)
    
    res = num[-nth]

    return int(res)
