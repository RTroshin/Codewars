def is_opposite(s1, s2):
    return s1 == ''.join([ch.upper() if ch.islower() else ch.lower() for ch in s2]) if s1 and s2 else False
