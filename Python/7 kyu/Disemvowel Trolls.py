def disemvowel(str_):
    return ''.join([ch if ch.lower() not in "aeuio" else '' for ch in str_])
