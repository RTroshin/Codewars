def remove(str):
    str = str.split()
    res = [str[i].rstrip('!') for i in range(len(str))]

    res = ' '.join(res)
    
    return res
