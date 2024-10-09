def close_to_zero(t):
    if not t:
        return 0

    return [n for n in sorted(map(int, t.split())) if n >= 0][0]
