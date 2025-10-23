def disarium_number(num):
    num = str(num)
    sum = 0

    for i in range(len(num)):
        sum += int(num[i]) ** (i + 1)

    return "Disarium !!" if str(sum) == num else "Not !!"
