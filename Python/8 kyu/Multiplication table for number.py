def multi_table(num):
    return '\n'.join([str(i) + " * " + str(num) + " = " + str(i * num) for i in range(1, 11)])
