def is_vowel(str):
    return True if len(str) == 1 and str.isalpha() and str.lower() in "aeiou" else False
