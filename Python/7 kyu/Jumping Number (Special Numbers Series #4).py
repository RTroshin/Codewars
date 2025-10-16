def jumping_number(num):
    num = str(num)

    for i in range(len(num) - 1):
        if not (num[i] + 1 == num[i + 1] or num[i] - 1 == num[i + 1]):
            return "Not!!"

    return "Jumping!!"
