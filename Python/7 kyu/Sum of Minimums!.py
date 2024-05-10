def sum_of_minimums(numbers):
    lstMin = []

    for i in range(len(numbers)):
        lstMin.append(min(numbers[i]))

    return sum(lstMin)
