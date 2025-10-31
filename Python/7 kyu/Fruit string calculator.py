def calculate(str):
    str = str.split()
    res = 0

    numLst = [int(n) for n in str if n.isdecimal()]

    if "gains" in str:
        return numLst[0] + numLst[1]
    elif "loses" in str:
        return numLst[0] - numLst[1]
