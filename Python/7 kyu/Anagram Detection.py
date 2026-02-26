# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original):
        return False

    test == list(test)
    original = list(original)

    if sorted(test) == sorted(original):
        return True
    else:
        return False
