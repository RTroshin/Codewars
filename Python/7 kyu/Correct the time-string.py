def time_correct(t):
    if not t:
        return t

    t = t.split(':')

    if len(t) != 3:
        return None
    if not t[0].isdecimal() or not t[1].isdecimal() or not t[2].isdecimal():
        return None

    return ':'.join(t)
