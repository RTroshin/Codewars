def zipvalidate(postcode):
    return not (len(postcode) != 6 or postcode[0] in "05789" or not postcode.isdecimal())
