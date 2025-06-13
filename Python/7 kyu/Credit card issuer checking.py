def get_issuer(num):
    strNum = str(num)
    lenStrNum = len(strNum)

    if lenStrNum == 13 or lenStrNum == 16 and strNum[0] == '4':
        return "VISA"
    elif lenStrNum == 16:
        if strNum[:4] == "6011":
            return "Discover"
        elif strNum[:2] in ["51", "52", "53", "54", "55"]:
            return "Mastercard"
    elif lenStrNum == 15 and strNum[:2] in ["34", "37"]:
        return "AMEX"
    
    return "Unknown"
