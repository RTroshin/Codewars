def jumping_number(number):
    number = str(number)

    for i in range(len(number) - 1):
        if not (number[i] + 1 == number[i + 1] or number[i] - 1 == number[i + 1]):
            return "Not!!"

    return "Jumping!!"
