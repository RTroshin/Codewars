def high_and_low(numbers):
    numbers = sorted(list(map(int, numbers.split(' '))))
    return str(numbers[-1]) + ' ' + str(numbers[0])
