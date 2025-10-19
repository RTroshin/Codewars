def remove(str):
    str = str.split()
    res = ''

    for i in range(len(str)):
        res += str[i].rstrip('!')
    
    return res
