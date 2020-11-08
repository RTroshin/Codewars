def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        return sum
