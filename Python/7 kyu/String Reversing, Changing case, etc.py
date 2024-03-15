def reverse_and_mirror(s1, s2):
    return f"{''.join([ch.upper() if ch.islower() else ch.lower() for ch in s2])[::-1]}@@@{''.join([ch.upper() if ch.islower() else ch.lower() for ch in s1])[::-1]}{''.join([ch.upper() if ch.islower() else ch.lower() for ch in s1])}"
