def zipvalidate(postcode):
    return not (len(postcode) != 6 or not postcode.isdecimal() or postcode[0] in "05789")
