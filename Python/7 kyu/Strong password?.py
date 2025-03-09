def check_password(str):
    valUpper = False
    valLower = False
    valDigit = False
    valSpecial = False

    if 7 < len(str) < 21:
        for ch in str:
            if ch.isupper():
                valUpper = True
            elif ch.islower():
                valLower = True
            elif ch.isdigit():
                valDigit = True
            elif ch in "!@#$%^&*?":
                valSpecial = True

    return "valid" if valUpper and valLower and valDigit and valSpecial else "not valid"
