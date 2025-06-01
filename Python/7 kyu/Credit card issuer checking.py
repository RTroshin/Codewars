def get_issuer(num):
    if len(str(num)) == 16:
        if str(num)[0] == '4':
            return "VISA"
        if str(num)[:4] == "6011":
            return "Discover"
        if str(num)[:2] == "51" or str(num)[:2] == "52" or str(num)[:2] == "53" or str(num)[:2] == "54" or str(num)[:2] == "55":
            return "Mastercard"
    if len(str(num)) == 13:
        if str(num)[0] == '4':
            return "VISA"
    if len(str(num)) == 15:
        if str(num)[:2] == "34" or str(num)[:2] == "37":
            return "AMEX"

    return "Unknown"
