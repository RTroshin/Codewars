def sum_array(a):
    if a == 0:
        return []
    else:
        sum = 0
        for i in range(len(a)):
            sum += a[i]
        return sum
