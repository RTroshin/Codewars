def time_correct(t):
    if not t:
        return t

    t = t.split(':')

    if len(t) != 3:
        return None
    elif not t[0].isdecimal() or not t[1].isdecimal() or not t[2].isdecimal():
        return None

    if int(t[2]) > 59:
        t[2] = str(int(t[2]) - 60)
        t[1] = str(int(t[1]) + 1)
    elif int(t[1]) > 59:
        t[1] = str(int(t[1]) - 60)
        t[0] = str(int(t[0]) + 1)
    elif int(t[0]) > 24:
        t[0] = str(int(t[0]) - 24)

    return ':'.join(t)
