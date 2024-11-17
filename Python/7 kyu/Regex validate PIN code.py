def validate_pin(pin):
    lenPin = len(pin)

    if lenPin != 4 and lenPin != 6:
        return False

    for i in range(lenPin):
        if not pin[i].isdigit():
            return False

    return True
