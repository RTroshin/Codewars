def my_first_kata(a, b):
    return a % b + b % a if type(a) == type(b) == int and a and b else False
