def vowel_one(str):
    return ''.join('1' if l.lower() in "aeiou" else '0' for l in str)
