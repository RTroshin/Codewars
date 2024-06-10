def div_con(x):
    int_int = [i for i in x if type(i) == int]
    str_int = [i for i in x if type(i) == str]

    return sum(int_int) - sum(map(int, str_int))
