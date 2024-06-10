def balanced_num(number):
    number = list(map(int, str(number)))

    return "Balanced" if sum(number[:len(number) // 2]) == sum(number[len(number) // 2 + 1:]) else "Not Balanced"
