def sum_digits(num):
    return sum(map(int, list((str(abs(num))))))
