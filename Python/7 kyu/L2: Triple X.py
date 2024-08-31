def triple_x(s):
    if not s:
        return False

    for i in range(len(s)):
        if s[i] == 'x' and s[i + 1] == 'x' and s[i + 2] == 'x':
            return True
        elif s[i] == 'x' and s[i + 1] != 'x':
            return False

    return False
