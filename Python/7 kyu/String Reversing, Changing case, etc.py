def reverse_and_mirror(s1, s2):
    s1 = ''.join(ch.upper() if ch.islower() else ch.lower() for ch in s1)
    s2 = ''.join(ch.upper() if ch.islower() else ch.lower() for ch in s2)[::-1]
    return f"{s2}@@@{s1[::-1]}{s1}"
