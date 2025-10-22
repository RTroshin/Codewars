def disarium_number(number):
    number = str(number)
    sum = 0

    for i in range(len(number)):
        sum += int(number[i]) ** (i + 1)

    return "Disarium !!" if str(sum) == number else "Not !!"
