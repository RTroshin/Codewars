def check_three_and_two(array):
    if array.count('a') == 3 and (array.count('b') == 2 or array.count('c') == 2):
        return True
    elif array.count('b') == 3 and (array.count('a') == 2 or array.count('c') == 2):
        return True
    elif array.count('c') == 3 and (array.count('a') == 2 or array.count('b') == 2):
        return True
    else:
        return False
