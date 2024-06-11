def div_con(x):
    return sum([i for i in x if type(i) == int]) - sum(map(int, [i for i in x if type(i) == str]))
