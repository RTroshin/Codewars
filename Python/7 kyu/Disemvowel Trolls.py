def disemvowel(string_):
    return ''.join([letter if letter.lower() not in "aeuio" else '' for letter in string_])
