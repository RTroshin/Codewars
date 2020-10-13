def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a >= b + c or b >= a + c or c >= a + b:
            return False
        else:
            return True 
    else:
        return False