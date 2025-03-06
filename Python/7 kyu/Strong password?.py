def check_password(str):
    valUpper = False
    valLower = False
    valDigit = False
    valSpecial = False

    if 7 < len(str) < 21:
        for i in range(len(str)):
            if str[i].isupper():
                valUpper = True
            if str[i].islower():
                valLower = True
            if str[i].isdigit():
                valDigit = True
            if str[i] in "!@#$%^&*?":
                valSpecial = True
    else:
        return "not valid"

    return "valid" if valUpper and valLower and valDigit and valSpecial else "not valid"
