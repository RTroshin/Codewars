def get_issuer(num):
    if len(str(num)) == 16:
        if str(num)[0] == '4':
            return "VISA"
        elif str(num)[:4] == "6011":
            return "Discover"
        elif str(num)[:2] == "51" or str(num)[:2] == "52" or str(num)[:2] == "53" or str(num)[:2] == "54" or str(num)[:2] == "55":
            return "Mastercard"
    elif len(str(num)) == 13 and str(num)[0] == '4':
            return "VISA"
    elif len(str(num)) == 15 and str(num)[:2] == "34" or str(num)[:2] == "37":
            return "AMEX"

    return "Unknown"
