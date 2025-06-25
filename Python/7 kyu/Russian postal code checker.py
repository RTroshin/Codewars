def zipvalidate(postcode):
    if postcode[0] in "05789":
        return False
    if len(postcode) != 6:
        return False
    if not postcode.isdecimal():
        return False

    return True
