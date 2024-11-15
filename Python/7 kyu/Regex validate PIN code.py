def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False

    for i in range(len(pin)):
        if not pin[i].isdigit():
            return False

    return True
