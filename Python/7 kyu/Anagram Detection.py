def is_anagram(test, original):
    return False if len(test) != len(original) else sorted(test.lower()) == sorted(original.lower())
