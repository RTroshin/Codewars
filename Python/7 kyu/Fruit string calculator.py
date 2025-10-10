def calculate(strng):
    strng = strng.split()
    res = 0

    numLst = []

    for i in range(len(strng)):
        if strng[i].isdecimal():
            numLst.append(strng[i])

    if "gains" in strng:
        res = int(numLst[0]) + int(numLst[1])

    if "loses" in strng:
        res = int(numLst[0]) - int(numLst[1])

    return res
