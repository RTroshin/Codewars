def calculate(strng):
    strng = strng.split()
    res = 0

    numLst = [int(n) for n in strng if n.isdecimal()]

    if "gains" in strng:
        return numLst[0] + numLst[1]
    elif "loses" in strng:
        return numLst[0] - numLst[1]
