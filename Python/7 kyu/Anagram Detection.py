def is_anagram(test, original):
    if len(test) != len(original):
        return False
    
    return True if sorted(test.lower()) == sorted(original.lower()) else False
