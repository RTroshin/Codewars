def to_alternating_case(str):
    return ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in str)
