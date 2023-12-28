def sum_array(a):
    if len(a):
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        return sum
    else:
        return 0
