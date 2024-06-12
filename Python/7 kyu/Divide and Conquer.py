def div_con(arr):
    return sum([i for i in arr if type(i) == int]) - sum(map(int, [i for i in arr if type(i) == str]))
