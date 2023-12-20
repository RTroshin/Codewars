def best_friend(str, a, b):
    str += '.'
    for i in range(len(str) - 1):
        if str[i] == a and str[i + 1] != b:
            return False
    return True
