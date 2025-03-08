def check_password(str):
    valUpper = False
    valLower = False
    valDigit = False
    valSpecial = False

    if 7 < len(str) < 21:
        for i in range(len(str)):
            if str[i].isupper():
                valUpper = True
            elif str[i].islower():
                valLower = True
            elif str[i].isdigit():
                valDigit = True
            elif str[i] in "!@#$%^&*?":
                valSpecial = True

    return "valid" if valUpper and valLower and valDigit and valSpecial else "not valid"
