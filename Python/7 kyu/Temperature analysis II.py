def close_to_zero(t):
    return [n for n in sorted(map(int, t.split())) if n >= 0][0] if t else 0
