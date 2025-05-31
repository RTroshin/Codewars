def get_issuer(number):
    if len(str(number)) == 16:
        if str(number)[0] == '4':
            return "VISA"
        if str(number)[:4] == "6011":
            return "Discover"
        if str(number)[:2] == "51" or str(number)[:2] == "52" or str(number)[:2] == "53" or str(number)[:2] == "54" or str(number)[:2] == "55":
            return "Mastercard"
    if len(str(number)) == 13:
        if str(number)[0] == '4':
            return "VISA"
    if len(str(number)) == 15:
        if str(number)[:2] == "34" or str(number)[:2] == "37":
            return "AMEX"

    return "Unknown"
