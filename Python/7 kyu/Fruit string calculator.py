def calculate(strng):
    strng = strng.split()
    res = 0

    numLst = []

    for n in strng:
        if n.isdecimal():
            numLst.append(n)

    if "gains" in strng:
        res = int(numLst[0]) + int(numLst[1])
    elif "loses" in strng:
        res = int(numLst[0]) - int(numLst[1])

    return res
