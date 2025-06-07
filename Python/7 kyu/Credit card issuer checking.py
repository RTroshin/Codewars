def get_issuer(num):
    strNum = str(num)

    if len(strNum) == 16:
        if strNum[0] == '4':
            return "VISA"
        elif strNum[:4] == "6011":
            return "Discover"
        elif strNum[:2] == "51" or strNum[:2] == "52" or strNum[:2] == "53" or strNum[:2] == "54" or strNum[:2] == "55":
            return "Mastercard"
    elif len(strNum) == 13 and strNum[0] == '4':
            return "VISA"
    elif len(strNum) == 15 and strNum[:2] == "34" or strNum[:2] == "37":
            return "AMEX"

    return "Unknown"
