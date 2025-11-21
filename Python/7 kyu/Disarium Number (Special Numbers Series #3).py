def disarium_number(num):
    return "Disarium !!" if sum(int(str(num)[i]) ** (i + 1) for i in range(len(str(num)))) == num else "Not !!"
