def get_issuer(num):
    strNum = str(num)
    lenStrNum = len(strNum)

    if lenStrNum == 16:
        if strNum[0] == '4':
            return "VISA"
        elif strNum[:4] == "6011":
            return "Discover"
        elif strNum[0] == '5':
            return {"51": "Mastercard", "52" : "Mastercard", "53" : "Mastercard", "54" : "Mastercard", "55" : "Mastercard"}[strNum[:2]]
    elif lenStrNum == 13 and strNum[0] == '4':
            return "VISA"
    elif lenStrNum == 15:
            return {"34": "AMEX", "37" : "AMEX"}[strNum[:2]]

    return "Unknown"
