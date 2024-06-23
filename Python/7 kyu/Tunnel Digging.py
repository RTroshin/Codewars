rock_dict = {'[' : 30, ']' : 30,
             '{' : 25, '}' : 25,
             '(' : 20, ')' : 20,
             '|' : 15, ':' : 10}

def tunnel_digging(r):
    return sum([rock_dict.get(s) for s in ''.join(r).replace(' ', '')]) + (len(r) // 3) * 30
