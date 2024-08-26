def check_three_and_two(arr):
    if arr.count('a') == 3 and (arr.count('b') == 2 or arr.count('c') == 2):
        return True
    elif arr.count('b') == 3 and (arr.count('a') == 2 or arr.count('c') == 2):
        return True
    elif arr.count('c') == 3 and (arr.count('a') == 2 or arr.count('b') == 2):
        return True
    else:
        return False
