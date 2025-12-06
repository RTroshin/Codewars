def time_correct(t):
    if not t:
        return t

    t = t.split(':')

    if len(t) != 3 or not t[0].isdecimal() or not t[1].isdecimal() or not t[2].isdecimal():
        return None

    while int(t[2]) > 59:
        t[2] = str(int(t[2]) - 60)
        t[1] = str(int(t[1]) + 1)
    while int(t[1]) > 59:
        t[1] = str(int(t[1]) - 60)
        t[0] = str(int(t[0]) + 1)
    while int(t[0]) > 23:
        t[0] = str(int(t[0]) - 24)

    if t[0] == '0':
        t[0] += '0'
    if t[1] == '0':
        t[1] += '0'
    if t[2] == '0':
        t[2] += '0'

    return ':'.join(t)
