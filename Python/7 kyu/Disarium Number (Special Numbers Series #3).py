def disarium_number(num):
    return "Disarium !!" if sum(int(n) ** (i + 1) for i, n in enumerate(str(num))) == num else "Not !!"
