def multiply(n):
    return n * 5**sum([1 for i in str(n) if i.isdecimal()])
