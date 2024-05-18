def lottery(str):
    res = ''

    for ch in str:
        if ch.isdigit() and ch not in res:
            res += ch

    return res if res else "One more run!"
