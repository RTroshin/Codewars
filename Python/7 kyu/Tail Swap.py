def tail_swap(str):
    return [':'.join([str[0].split(':')[0], str[1].split(':')[1]])] +\
           [':'.join([str[1].split(':')[0], str[0].split(':')[1]])]
