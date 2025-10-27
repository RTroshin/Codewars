def disarium_number(num):
    num = str(num)

    res = sum(int(num[i]) ** (i + 1) for i in range(len(num)))

    return "Disarium !!" if str(res) == num else "Not !!"
