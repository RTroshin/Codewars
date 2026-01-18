def get_issuer(n):
    strN = str(n)
    lenStrN = len(strN)

    if (lenStrN == 13 or lenStrN == 16) and strN[0] == '4':
        return "VISA"
    elif lenStrN == 15 and strN[:2] in ["34", "37"]:
        return "AMEX"
    elif lenStrN == 16 and strN[:4] == "6011":
        return "Discover"
    elif lenStrN == 16 and strN[:2] in ["51", "52", "53", "54", "55"]:
        return "Mastercard"
    
    return "Unknown"
