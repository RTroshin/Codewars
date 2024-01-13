def disemvowel(str_):
    return ''.join([letter if letter.lower() not in "aeuio" else '' for letter in str_])
