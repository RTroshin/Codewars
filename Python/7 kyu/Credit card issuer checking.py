def get_issuer(num):
    strNum = str(num)
    lenStrNum = len(strNum)

    if lenStrNum == 16:
        if strNum[0] == '4':
            return "VISA"
        elif strNum[:4] == "6011":
            return "Discover"
        elif strNum[:2] in ["51", "52", "53", "54", "55"]:
            return "Mastercard"
    elif lenStrNum == 13 and strNum[0] == '4':
            return "VISA"
    elif lenStrNum == 15:
            return {"34": "AMEX", "37" : "AMEX"}[strNum[:2]]

    return "Unknown"
