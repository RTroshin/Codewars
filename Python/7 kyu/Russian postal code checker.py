def zipvalidate(postcode):
    if postcode[0] in "05789" or len(postcode) != 6:
        return False
    elif not postcode.isdecimal():
        return False

    return True
