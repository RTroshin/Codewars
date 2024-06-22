rock_dict = {'[' : 30, ']' : 30,
             '{' : 25, '}' : 25,
             '(' : 20, ')' : 20,
             '|' : 15, ':' : 10}

def tunnel_digging(r):
    time = 0
    for s in ''.join(r).replace(' ', ''):
        time += rock_dict.get(s)
    
    return time + (len(r) // 3) * 30
