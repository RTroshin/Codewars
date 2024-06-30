def sum_digits(number):
    return sum(map(int, list((str(abs(number))))))
