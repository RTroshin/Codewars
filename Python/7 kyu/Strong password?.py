def check_password(s):
    valUpper = False
    valLower = False
    valDigit = False
    valSpecial = False

    if 7 < len(s) < 21:
        for i in range(len(s)):
            if s[i].isupper():
                valUpper = True
            if s[i].islower():
                valLower = True
            if s[i].isdigit():
                valDigit = True
            if s[i] in "!@#$%^&*?":
                valSpecial = True
    else:
        return "not valid"

    return "valid" if valUpper and valLower and valDigit and valSpecial else "not valid"
