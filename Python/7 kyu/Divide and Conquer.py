def div_con(arr):
    return sum([n for n in arr if type(n) == int]) - sum(map(int, [n for n in arr if type(n) == str]))
