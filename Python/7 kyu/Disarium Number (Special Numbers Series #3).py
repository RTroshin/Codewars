def disarium_number(num):
    num = str(num)
    return "Disarium !!" if str(sum(int(num[i]) ** (i + 1) for i in range(len(num)))) == num else "Not !!"
