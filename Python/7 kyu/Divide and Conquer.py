def div_con(arr):
    return sum(n for n in arr if type(n) == int) - sum(int(n) for n in arr if type(n) == str)
