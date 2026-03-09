# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original):
        return False

    if sorted(test.lower()) == sorted(original.lower()):
        return True
    else:
        return False
