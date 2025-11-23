def disarium_number(n):
    return "Disarium !!" if sum(int(d) ** (i + 1) for i, d in enumerate(str(n))) == n else "Not !!"
