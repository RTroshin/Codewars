def calculate(strng):
    strng = strng.split()
    res = 0

    numLst = []

    for n in strng:
        if n.isdecimal():
            numLst.append(int(n))

    if "gains" in strng:
        res = numLst[0] + numLst[1]
    elif "loses" in strng:
        res = numLst[0] - numLst[1]

    return res
