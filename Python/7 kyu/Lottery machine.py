def lottery(s):
    res = ''

    for ch in s:
        if ch.isdigit() and ch not in res:
            res += ch

    return res if res else "One more run!"
