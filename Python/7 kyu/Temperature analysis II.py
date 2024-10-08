def close_to_zero(t):
    if not t:
        return 0

    t = sorted(map(int, t.split()))

    return [n for n in t if n >= 0][0]
