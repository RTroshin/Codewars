def zipvalidate(postcode):
    return len(postcode) == 6 and postcode.isdecimal() and postcode[0] not in "05789"
